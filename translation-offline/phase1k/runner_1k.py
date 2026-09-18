#!/usr/bin/env python3
"""Phase 1k — agent R: DEV measurement, mechanical selection, freeze, and the ONE final runner.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1k/runner_1k.py measure --max-calls 750
    PYTHONDONTWRITEBYTECODE=1 python3 phase1k/runner_1k.py final --side dev
    PHASE1K_OPEN_FRESH is set by the script itself for --side fresh; never by hand.
    PYTHONDONTWRITEBYTECODE=1 python3 phase1k/runner_1k.py final --side fresh    --max-calls N
    PYTHONDONTWRITEBYTECODE=1 python3 phase1k/runner_1k.py final --side replay1j --max-calls N

Model: gemini-3.1-flash-lite, temperature 0, thinkingBudget 0. Counted = HTTP 200 only; non-200
attempts are logged with counted:false and retried with backoff; an EMPTY 200 is counted, never
retried, never guessed, scored as rejected. Byte-identical prompts already in phase1j/ledger.jsonl or
phase1k/ledger.jsonl are reused (0 calls). Every data read goes through loader_1k (logged).
"""
import sys
sys.dont_write_bytecode = True                                            # $J is chmod a-w

import argparse                                                           # noqa: E402
import collections                                                        # noqa: E402
import copy                                                               # noqa: E402
import hashlib                                                            # noqa: E402
import json                                                               # noqa: E402
import os                                                                 # noqa: E402
import random                                                             # noqa: E402
import time                                                               # noqa: E402
from concurrent.futures import ThreadPoolExecutor                         # noqa: E402

K = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(K)
P1J = os.path.join(TOFF, 'phase1j')
for _p in (K, os.path.join(K, 'taskB'), os.path.join(P1J, 'taskC')):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import loader_1k as L                                                     # noqa: E402  (neuters loader_1j._log)
import runner_1j as R                                                     # noqa: E402
import pipeline_1i as P                                                   # noqa: E402
import f8, f9                                                             # noqa: E402

LEDGER_K = os.path.join(K, 'ledger.jsonl')
LEDGER_J = os.path.join(P1J, 'ledger.jsonl')
TASKA = os.path.join(K, 'taskA')
TASKD = os.path.join(K, 'taskD')
JUDGE = os.path.join(K, 'judge')
FROZEN = os.path.join(K, 'FROZEN_CONFIG_1K.json')
DONE = os.path.join(K, 'FINAL_RUN_DONE')
PHASE_CAP = 2000
MY_CAP = 750
PRICE_IN, PRICE_OUT = 0.25 / 1e6, 1.50 / 1e6
TYPES = ('T', 'W', 'M', 'S', 'V', 'E')

# ------------------------------------------------------------------ the P-1K extra rules
NEW_RULES = [
    'Judge the learner sentence against the SLOVAK sentence, not against the English reference. A '
    'different structure that is correct English and means what the Slovak means is SAME, even when it '
    'avoids the structure the reference uses.',
    'Voice: if the Slovak names an agent in the nominative and the learner sentence moves that agent out '
    'of subject position or drops it (an active Slovak sentence turned into an English passive), that is '
    'DIFF. Where the Slovak is itself impersonal or passive, an English passive is SAME.',
    'Time: the time frame (past, present or future) must match the Slovak — a Slovak perfective present '
    'form ("dokonci") means the FUTURE, and an English present tense inside an if- or when-clause about '
    'the future is fine. A different English tense inside the Slovak\'s own time frame (for a Slovak past '
    'imperfective: "trained", "was training", "had been training") is SAME.',
]
PROMPTS = ('P-FROZEN', 'P-1K')


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def fsha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]


# ================================================================== requests
def build_req(st, r, prompt_id):
    """(system, user, generationConfig, hash). prompt_id P-FROZEN is byte-identical to Phase 1j arm B."""
    it = P.to_item(r)
    lines = P.pb_lines(st, it)
    head, tail = lines[:-1], lines[-1]
    g = P.gender_chain(st, r['sid'])
    gline = P.GENDER_TMPL.format(words=', '.join('"%s"' % w for w in g)) if g else None
    extra = ([gline] if gline else []) + [P.GROUND_LINE, P.WORDING_LINE]
    if prompt_id == 'P-1K':
        extra = extra + list(NEW_RULES)
    sysx, gcfg = P.sys_text(st, 'P-E4b'), P.GEN_CFG
    user = '\n'.join(head + extra + [tail])
    return sysx, user, gcfg, R.req_hash(sysx, user, gcfg)


def prompt_template_sha(prompt_id):
    body = {'system': P.sys_text.__doc__ or '', 'sys': SYS_TEXT_CACHE.get('sys', ''),
            'lines': [P.GROUND_LINE, P.WORDING_LINE] + (list(NEW_RULES) if prompt_id == 'P-1K' else []),
            'gender_template': P.GENDER_TMPL, 'tail': 'SAME, TIP or DIFF?',
            'base': 'checker_1i.prompt(it, "P-B") lines, last line replaced by the tail'}
    return sha(json.dumps(body, sort_keys=True, ensure_ascii=False))


SYS_TEXT_CACHE = {}


def ledger_state():
    """Verdicts and replies from BOTH ledgers ($J read-only, $K ours). HTTP-200 rows only."""
    rep, ver, failed = {}, {}, set()
    counted_k = 0
    for path, mine in ((LEDGER_J, False), (LEDGER_K, True)):
        for row in R.ledger_rows(path):
            if row.get('http') != 200:
                continue
            if mine:
                counted_k += 1
            h = row.get('req_hash')
            if not h:
                continue
            rep[h] = row.get('reply', '')
            if row.get('verdict') == 'PARSE_FAIL':
                failed.add(h)
                ver.pop(h, None)
            else:
                ver[h] = row.get('verdict')
                failed.discard(h)
    return rep, ver, failed, counted_k


def call_one(req, key, tries=5):
    """Exactly the Phase 1j transport, writing into $K/ledger.jsonl."""
    sysx, user, gcfg, h, variant, item_id = req
    body = {'systemInstruction': {'parts': [{'text': sysx}]},
            'contents': [{'role': 'user', 'parts': [{'text': user}]}],
            'generationConfig': gcfg}
    url = P.API % P.MODEL
    delay, row = 1.0, None
    for attempt in range(1, tries + 1):
        t0 = time.time()
        code, js, raw = P._http(url, body, key)
        lat = int((time.time() - t0) * 1000)
        if code == 200:
            cands = (js or {}).get('candidates') or []
            txt = ''.join(pp.get('text', '') or '' for c in cands
                          for pp in ((c.get('content') or {}).get('parts') or []))
            um = (js or {}).get('usageMetadata') or {}
            row = {'ts': time.time(), 'model': P.MODEL, 'variant': variant, 'item_id': item_id,
                   'req_hash': h, 'http': 200, 'counted': True,
                   'verdict': P.parse_reply(txt, 'P-E4b') or 'PARSE_FAIL', 'reply': txt,
                   'finish': cands[0].get('finishReason') if cands else None,
                   'empty': (not cands) or txt.strip() == '', 'latency_ms': lat, 'try': attempt,
                   'prompt_tokens': um.get('promptTokenCount'),
                   'candidates_tokens': um.get('candidatesTokenCount'),
                   'thoughts_tokens': um.get('thoughtsTokenCount'),
                   'cached_tokens': um.get('cachedContentTokenCount'),
                   'thinking': '{"thinkingBudget": 0}', 'max_output': gcfg['maxOutputTokens']}
            P.ledger_append(LEDGER_K, row)
            return row
        row = {'ts': time.time(), 'model': P.MODEL, 'variant': variant, 'item_id': item_id,
               'req_hash': h, 'http': code, 'counted': False, 'verdict': None, 'reply': '',
               'latency_ms': lat, 'try': attempt, 'error': P._redact(raw or js, key),
               'transport_retry': True}
        P.ledger_append(LEDGER_K, row)
        if attempt == tries:
            return row
        time.sleep(delay * (1.0 + random.random() * 0.3))
        delay = min(delay * 2, 16.0)
    return row


def token_spend():
    tin = tout = n200 = nempty = nretry = 0
    for row in R.ledger_rows(LEDGER_K):
        if row.get('http') != 200:
            nretry += 1
            continue
        n200 += 1
        tin += row.get('prompt_tokens') or 0
        tout += (row.get('candidates_tokens') or 0) + (row.get('thoughts_tokens') or 0)
        if row.get('verdict') == 'PARSE_FAIL':
            nempty += 1
    return {'counted_calls_http200': n200, 'failed_empty_200': nempty,
            'non200_attempts': nretry, 'tokens_in': tin, 'tokens_out': tout,
            'spend_usd': round(tin * PRICE_IN + tout * PRICE_OUT, 5)}


# ================================================================== labels (blind judge, §0)
def judge_labels(source, purpose):
    """{item_id: (label, type)} for ONE source. The key is filtered on source BEFORE any join."""
    key = [json.loads(l) for l in open(os.path.join(JUDGE, 'key.jsonl'), encoding='utf-8') if l.strip()]
    rows = [r for r in key if r.get('source') == source]                 # filter first
    want = {r['j'] for r in rows}
    files = ['out_5.tsv'] if source == 'holdout1j' else ['out_1.tsv', 'out_2.tsv', 'out_3.tsv',
                                                         'out_4.tsv']
    verd = {}
    for f in files:
        p = os.path.join(JUDGE, f)
        if not os.path.exists(p):
            continue
        for ln in open(p, encoding='utf-8'):
            ln = ln.rstrip('\n')
            if not ln.strip():
                continue
            parts = ln.split('\t')
            j = parts[0].strip()
            if j not in want:
                continue
            if parts[1].strip().upper().startswith('C'):
                verd[j] = ('correct', None)
            else:
                t = (parts[2].strip().upper() if len(parts) > 2 and parts[2].strip() else 'E')
                verd[j] = ('wrong', t if t in TYPES else 'E')
    out = {r['id']: verd[r['j']] for r in rows if r['j'] in verd}
    L._log('1k:judge', 'judge labels source=%s' % source, len(out), purpose)
    return out, rows, verd


def control_noise(purpose):
    """Judge noise from the 60 controls: control j vs its dup_of original."""
    key = [json.loads(l) for l in open(os.path.join(JUDGE, 'key.jsonl'), encoding='utf-8') if l.strip()]
    ctrl = [r for r in key if r.get('source') == 'control']
    need = {r['j'] for r in ctrl} | {r.get('dup_of') for r in ctrl if r.get('dup_of')}
    verd = {}
    for f in ('out_1.tsv', 'out_2.tsv', 'out_3.tsv', 'out_4.tsv'):
        p = os.path.join(JUDGE, f)
        if not os.path.exists(p):
            continue
        for ln in open(p, encoding='utf-8'):
            parts = ln.rstrip('\n').split('\t')
            if not parts or parts[0].strip() not in need:
                continue
            verd[parts[0].strip()] = ('correct' if parts[1].strip().upper().startswith('C')
                                      else 'wrong')
    n = cw = wc = agree = 0
    for r in ctrl:
        a, b = verd.get(r.get('dup_of')), verd.get(r['j'])
        if a is None or b is None:
            continue
        n += 1
        if a == b:
            agree += 1
        elif a == 'correct':
            cw += 1
        else:
            wc += 1
    L._log('1k:judge', 'control noise', n, purpose)
    return {'n': n, 'agree': agree, 'correct_to_wrong': P.rate(cw, n),
            'wrong_to_correct': P.rate(wc, n), 'any_flip': P.rate(cw + wc, n)}


# ================================================================== the layers
def locktip_decide(base_decide):
    """§0: a lock mismatch no longer rejects — it attaches a TIP and the item goes on to L3.

    Implemented by re-deciding the item with the lock satisfied, so the whole frozen stack (F3/F5/
    F4v2/F4v3, L1, the model layer) runs exactly as before. A mistake-pattern L2 rejection
    (it['step'] == 'mistake') is NOT a lock and keeps rejecting.
    """
    def dec(it, flags, vm):
        d = base_decide(it, flags, vm)
        if d.get('layer') == 'L2' and not d.get('accepted') and it.get('step') != 'mistake' \
                and it.get('locks'):
            it2 = dict(it, locks=[], lock_ok=True)
            d2 = base_decide(it2, flags, vm)
            if d2.get('layer') == 'L2':
                return d
            d2 = dict(d2)
            d2['lock_tip'] = 'use the target structure: %s' % (it['locks'][0] if it['locks'] else '?')
            d2['released_from_lock'] = True
            return d2
        return d
    return dec


def guard_readouts(recs, ann, strict):
    """{item_id: {'f8':…, 'f9':…}} — pure offline, identical for every prompt. 0 calls."""
    old = f9.REPORTED_STRICT
    f9.REPORTED_STRICT = strict
    out = {}
    for r in recs:
        a = ann.get(str(r['sid']))
        try:
            r8 = f8.check(r['sk'], a, r['answer'])
        except Exception as e:
            r8 = {'verdict': 'abstain', 'reason': 'F8 error %s' % type(e).__name__}
        try:
            r9 = f9.check(r['sk'], a, r['answer'])
        except Exception as e:
            r9 = {'verdict': 'abstain', 'reason': 'F9 error %s' % type(e).__name__}
        out[r['item_id']] = {'f8': r8, 'f9': r9}
    f9.REPORTED_STRICT = old
    return out


def apply_guards(res, guards, f8_on, f9_on):
    """A guard may only turn an acceptance into a rejection (readout on top of the stored L3 verdict)."""
    out = {}
    for i, d in res.items():
        d = dict(d)
        if d['accepted']:
            g = guards.get(i) or {}
            if f8_on and (g.get('f8') or {}).get('verdict') == 'reject':
                d['accepted'], d['layer'] = False, 'F8'
            elif f9_on and (g.get('f9') or {}).get('verdict') == 'reject':
                d['accepted'], d['layer'] = False, 'F9'
        out[i] = d
    return out


# ================================================================== scoring
def score(recs, res, labels):
    """Coverage denominator = ALL items judged correct; FA denominator = all items judged wrong."""
    by = {r['item_id']: r for r in recs}
    lab = {i: labels.get(i, (by[i]['judged'], by[i]['wrong_type'])) for i in by}
    corr = [i for i in by if lab[i][0] == 'correct']
    corrC = [i for i in corr if by[i]['kind'] == 'C']
    wrong = [i for i in by if lab[i][0] == 'wrong']
    acc = {i for i in by if res[i]['accepted']}
    m = {'coverage': P.rate(len(set(corr) & acc), len(corr)),
         'coverage_kindC': P.rate(len(set(corrC) & acc), len(corrC)),
         'fa': P.rate(len([i for i in wrong if i in acc]), len(wrong)),
         'fa_by_type': {}, 'fa_by_layer': {}, 'fr_by_layer': {},
         'fa_items': [], 'false_rejections': []}
    for t in TYPES:
        n = [i for i in wrong if lab[i][1] == t]
        m['fa_by_type'][t] = P.rate(len([i for i in n if i in acc]), len(n))
    for i in sorted(i for i in wrong if i in acc):
        lay = res[i]['layer']
        m['fa_by_layer'][lay] = m['fa_by_layer'].get(lay, 0) + 1
        m['fa_items'].append({'id': i, 'type': lab[i][1], 'layer': lay, 'model': res[i]['model']})
    for i in sorted(set(corr) - acc):
        lay = res[i]['layer']
        m['fr_by_layer'][lay] = m['fr_by_layer'].get(lay, 0) + 1
        m['false_rejections'].append({'id': i, 'layer': lay, 'model': res[i]['model']})
    return m


def _r(d):
    return '%d/%d = %.2f%% [%.2f, %.2f]' % (d['k'], d['n'], d['pct'] or 0.0, d['ci'][0], d['ci'][1])


# ================================================================== sides (one shared code path)
def build_side(side, purpose):
    """-> (st_base, recs, ann, by_id). DEV and replay1j use the frozen Phase 1j arm-B builder."""
    if side in ('dev', 'replay1j'):
        s = 'dev' if side == 'dev' else 'holdout'
        old = os.environ.get('PHASE1J_FINAL')
        os.environ['PHASE1J_FINAL'] = '1'
        try:
            data = R.load_side(s, purpose)
        finally:
            if old is None:
                os.environ.pop('PHASE1J_FINAL', None)
            else:
                os.environ['PHASE1J_FINAL'] = old
        L._log('1j:%s' % s, 'items+annotations (arm B, via runner_1j.load_side)', len(data[0]), purpose)
        st, recs, pm = R.prep_arm('B', s, data)
        ann = data[2]
        return st, recs, ann, {r['item_id']: r for r in recs}
    if side == 'fresh':
        os.environ['PHASE1K_OPEN_FRESH'] = '1'
        sents = {int(s['sid']): s for s in L.load_fresh_sentences(purpose=purpose)}
        ann = L.load_fresh_annotations(purpose=purpose)
        items = L.load_fresh_items(purpose=purpose)
        C = R._C
        recs = []
        for it in items:
            sid = int(it['sid'])
            s = sents[sid]
            a = (ann.get(str(sid)) or {})
            hy = a.get('hygienised', a)
            lk = []
            for x in (hy.get('lk') or []):
                if isinstance(x, str):
                    lk.append(x)
                elif isinstance(x, (list, tuple)):
                    lk += [y for y in x if isinstance(y, str)]
            r = {'item_id': it['id'], 'kind': it['id'].split(':')[0], 'sid': sid, 'n': 1,
                 'level': s.get('level'), 'topic': s.get('topic'), 'sk': s['sk'],
                 'band': s.get('band'), 'reference': s['reference'], 'refs': list(s['refs']),
                 'answer': it['text'], 'judged': 'wrong' if it['id'].startswith('W') else 'correct',
                 'wrong_type': None, 'half': 'NEW', 'locks': lk, 'intent': it.get('intent'),
                 'chk': {'verdict': 'correct', 'step': 'L1', 'feedback': ''}, 'chk_missing': True,
                 'rows': [], 'lock_ok': True, 'lock_released_2_1': None}
            try:
                nrm = C.base.norm
                r['lock_ok'] = (not lk) or any(nrm(x).strip() in nrm(r['answer']) for x in lk)
                if not r['lock_ok']:
                    ok, tr = C.lock_equivalent_ok(P.to_item(r))
                    if ok:
                        r['lock_ok'], r['lock_released_2_1'] = True, tr
            except Exception:
                pass
            recs.append(r)
        st = R.make_state(recs, ann, ('F4v3',), side_tag='fresh1k')
        return st, recs, ann, {r['item_id']: r for r in recs}
    raise ValueError(side)


def collect_verdicts(st, recs, l3_ids, prompts, max_calls, allow_calls, tag):
    """Build the requests for every L3-eligible item under every prompt, reuse, then call. -> vms."""
    by = {r['item_id']: r for r in recs}
    req, hashes = {}, {p: {} for p in prompts}
    for p in prompts:
        for i in l3_ids:
            s, u, g, h = build_req(st, by[i], p)
            hashes[p][i] = h
            req[h] = (s, u, g, h, 'J-B' if p == 'P-FROZEN' else 'K-1K', i)
            SYS_TEXT_CACHE['sys'] = s
    rep, ver, failed, counted_k = ledger_state()
    need = [h for h in req if h not in ver and h not in failed]
    print('[%s] L3-eligible %d  unique prompts %d  reused %d  NEW needed %d  (counted in $K so far %d)'
          % (tag, len(l3_ids), len(req), len(req) - len(need), len(need), counted_k))
    made = {'ok': 0, 'bad': 0}
    if need and allow_calls:
        if counted_k + len(need) > max_calls:
            raise SystemExit('REFUSED: %d counted + %d new > --max-calls %d'
                             % (counted_k, len(need), max_calls))
        todo = [req[h] for h in need]
        random.Random(1).shuffle(todo)                  # an outage damages all variants equally
        key = P.load_key()

        def work(q):
            row = call_one(q, key)
            made['ok' if row.get('http') == 200 else 'bad'] += 1
            return row
        with ThreadPoolExecutor(max_workers=6) as pool:
            for _ in pool.map(work, todo):
                pass
        print('[%s] calls made: http200 %d  transport-dead %d' % (tag, made['ok'], made['bad']))
        rep, ver, failed, counted_k = ledger_state()
    elif need:
        raise SystemExit('FAIL: %d prompts are missing from the ledgers and calls are not allowed here'
                         % len(need))
    vms = {p: {i: ver[h] for i, h in hashes[p].items() if h in ver} for p in prompts}
    return vms, hashes, rep, {'reused': len(req) - len(need), 'new': len(need), 'made': made,
                              'counted_k': counted_k, 'no_verdict': {p: [i for i in l3_ids
                                                                        if i not in vms[p]]
                                                                     for p in prompts}}


def configure_row(st, recs, vm, locktip, guards, f8_on, f9_on, tip_reject):
    stx = dict(st)
    if locktip:
        stx['decide'] = locktip_decide(st['decide'])
    res = P.run_pipeline(stx, vm, tip_reject=tip_reject)
    return apply_guards(res, guards, f8_on, f9_on)


ROWDEF = []
for _p in PROMPTS:
    ROWDEF += [('BASE', _p, False, False, False, False),
               ('BASE+F8', _p, False, True, False, False),
               ('BASE+F9', _p, False, False, True, False),
               ('LOCKTIP', _p, True, False, False, False),
               ('LOCKTIP+F8', _p, True, True, False, False),
               ('LOCKTIP+F9', _p, True, False, True, False),
               ('LOCKTIP+F8+F9 (ALL)', _p, True, True, True, False),
               ('LOCKTIP+F9 strict', _p, True, False, True, True),
               ('LOCKTIP+F8+F9 strict (ALL)', _p, True, True, True, True)]


def all_rows(st, recs, vms, guards_by_strict, labels):
    rows, resmap = [], {}
    for name, prompt, locktip, f8_on, f9_on, strict in ROWDEF:
        for tip in (True, False):
            g = guards_by_strict[strict]
            res = configure_row(st, recs, vms[prompt], locktip, g, f8_on, f9_on, tip)
            m = score(recs, res, labels)
            parts = int(locktip) + int(f8_on) + int(f9_on) + int(strict) + int(prompt == 'P-1K')
            row = {'name': name, 'prompt': prompt, 'locktip': locktip, 'f8': f8_on, 'f9': f9_on,
                   'f9_strict': strict, 'tip_reject': tip, 'moving_parts': parts,
                   'coverage': m['coverage'], 'coverage_kindC': m['coverage_kindC'], 'fa': m['fa'],
                   'fa_by_type': m['fa_by_type'], 'fa_by_layer': m['fa_by_layer'],
                   'fr_by_layer': m['fr_by_layer'], 'fa_items': m['fa_items']}
            rows.append(row)
            resmap[(name, prompt, tip)] = res
    return rows, resmap


def select(rows):
    trace = []
    trace.append('candidates: %d rows (9 configurations x 2 prompts x TIP on/off)' % len(rows))
    ok = [r for r in rows if (r['fa']['pct'] or 0) < 5.0 and (r['fa_by_type']['T']['pct'] or 0) < 5.0]
    trace.append('gate FA < 5%% AND type-T FA < 5%%: %d rows pass' % len(ok))
    if ok:
        ok.sort(key=lambda r: (-(r['coverage']['pct'] or 0), r['moving_parts'],
                               0 if r['prompt'] == 'P-FROZEN' else 1))
        pick = ok[0]
        trace.append('top 5 by coverage among the survivors: %s'
                     % [('%s/%s/tip=%s cov %.2f FA %.2f T %.2f'
                         % (r['name'], r['prompt'], r['tip_reject'], r['coverage']['pct'] or 0,
                            r['fa']['pct'] or 0, r['fa_by_type']['T']['pct'] or 0)) for r in ok[:5]])
        trace.append('-> highest coverage (ties: fewer moving parts, then P-FROZEN): %s / %s / tip=%s'
                     % (pick['name'], pick['prompt'], pick['tip_reject']))
    else:
        trace.append('NO configuration meets both FA targets — the coverage target is NOT reachable; '
                     'falling back to the LOWEST FA point estimate.')
        pool = sorted(rows, key=lambda r: ((r['fa']['pct'] or 0), -(r['coverage']['pct'] or 0),
                                           r['moving_parts'], 0 if r['prompt'] == 'P-FROZEN' else 1))
        pick = pool[0]
        trace.append('-> lowest FA: %s / %s / tip=%s (FA %.2f %%, coverage %.2f %%)'
                     % (pick['name'], pick['prompt'], pick['tip_reject'], pick['fa']['pct'] or 0,
                        pick['coverage']['pct'] or 0))
    return pick, trace


# ================================================================== TASK A
def task_a(recs, new_labels, base_res):
    old = R.label_sets(recs, 'dev')[0]                      # Phase 1j arm-B PRIMARY labels
    by = {r['item_id']: r for r in recs}
    mv = {'n': 0, 'unchanged': 0, 'correct_to_wrong': collections.Counter(),
          'wrong_to_correct_by_old_type': collections.Counter(),
          'wrong_to_correct_by_1j_layer': collections.Counter(),
          'wrong_to_wrong_matrix': collections.Counter(), 'missing_judge_label': 0}
    for i, r in by.items():
        o = old.get(i, (r['judged'], r['wrong_type']))
        if i not in new_labels:
            mv['missing_judge_label'] += 1
            continue
        n = new_labels[i]
        mv['n'] += 1
        if o[0] == 'correct' and n[0] == 'wrong':
            mv['correct_to_wrong'][n[1] or '?'] += 1
        elif o[0] == 'wrong' and n[0] == 'correct':
            mv['wrong_to_correct_by_old_type'][o[1] or '?'] += 1
            lay = base_res[i]['layer'] if base_res[i] and not base_res[i]['accepted'] else 'accepted'
            grp = ('L2 lock' if lay == 'L2' else ('L3' if str(lay).startswith('L3')
                                                  else ('accepted' if lay == 'accepted'
                                                        else 'guard %s' % lay)))
            mv['wrong_to_correct_by_1j_layer'][grp] += 1
        elif o[0] == 'wrong' and n[0] == 'wrong' and o[1] != n[1]:
            mv['wrong_to_wrong_matrix']['%s->%s' % (o[1], n[1])] += 1
        else:
            mv['unchanged'] += 1
    cells_old = collections.Counter('correct' if v[0] == 'correct' else 'wrong:%s' % v[1]
                                    for v in old.values())
    cells_new = collections.Counter('correct' if v[0] == 'correct' else 'wrong:%s' % v[1]
                                    for v in new_labels.values())
    return {'movement': {k: (dict(v) if isinstance(v, collections.Counter) else v)
                         for k, v in mv.items()},
            'old_cells_1j_primary': dict(cells_old), 'new_cells_1k_judge': dict(cells_new),
            'conventions': {
                'labels': 'the blind judge\'s §0 verdicts adopted IN FULL (label AND type) for all 490 '
                          'DEV items',
                'coverage_denominator': 'ALL items judged correct (any id kind); the kind-C-only figure '
                                        'is printed as a secondary line for continuity with 1j',
                'fa_denominator': 'all items judged wrong',
                'types': 'T / W / M / S / V (voice, new) / E'}}


# ================================================================== extra analyses
def extras(recs, resmap, guards, labels, sel_key):
    by = {r['item_id']: r for r in recs}
    lab = {i: labels.get(i, (by[i]['judged'], by[i]['wrong_type'])) for i in by}
    base = resmap[('BASE', 'P-FROZEN', True)]
    lock = resmap[('LOCKTIP', 'P-FROZEN', True)]
    rel = {'lock_rejected_total': 0, 'released_correct_now_accepted': 0,
           'released_wrong_now_accepted_by_type': collections.Counter(),
           'released_total': 0, 'still_rejected_after_release': 0}
    for i in by:
        if base[i]['layer'] == 'L2' and not base[i]['accepted']:
            rel['lock_rejected_total'] += 1
            if lock[i]['accepted']:
                rel['released_total'] += 1
                if lab[i][0] == 'correct':
                    rel['released_correct_now_accepted'] += 1
                else:
                    rel['released_wrong_now_accepted_by_type'][lab[i][1] or '?'] += 1
            else:
                rel['still_rejected_after_release'] += 1
    rel['released_wrong_now_accepted_by_type'] = dict(rel['released_wrong_now_accepted_by_type'])

    def guard_cost(base_row, gname):
        res = resmap[base_row]
        caught, caught_unique, cost = [], [], []
        other = 'f9' if gname == 'f8' else 'f8'
        for i in by:
            if not res[i]['accepted']:
                continue
            if (guards[i][gname] or {}).get('verdict') != 'reject':
                continue
            if lab[i][0] == 'wrong':
                caught.append(i)
                if (guards[i][other] or {}).get('verdict') != 'reject':
                    caught_unique.append(i)
            else:
                cost.append(i)
        return {'caught_wrong': len(caught), 'caught_wrong_only_this_guard': len(caught_unique),
                'cost_correct_rejected': len(cost), 'cost_ids': cost[:20], 'caught_ids': caught[:20]}
    guardstats = {}
    for bn in (('LOCKTIP', 'P-FROZEN', True), ('BASE', 'P-FROZEN', True)):
        for g in ('f8', 'f9'):
            guardstats['%s|%s|tip=%s|%s' % (bn[0], bn[1], bn[2], g.upper())] = guard_cost(bn, g)

    sel = resmap[sel_key]
    b3 = {}
    for v in ('tip', 'abstain'):
        ids = [i for i in by if (guards[i]['f9'] or {}).get('verdict') == v]
        b3[v] = {'n': len(ids),
                 'judged_correct': sum(1 for i in ids if lab[i][0] == 'correct'),
                 'judged_wrong': sum(1 for i in ids if lab[i][0] == 'wrong'),
                 'cost_type_T_wrong_accepted_by_selected':
                     sum(1 for i in ids if lab[i][0] == 'wrong' and lab[i][1] == 'T'
                         and sel[i]['accepted'])}
    b3['f9_distribution'] = dict(collections.Counter((guards[i]['f9'] or {}).get('verdict')
                                                     for i in by))
    b3['f8_distribution'] = dict(collections.Counter((guards[i]['f8'] or {}).get('verdict')
                                                     for i in by))
    return {'lock_released': rel, 'guards': guardstats, 'b3': b3}


def task_c(recs, vms, resmap, labels):
    by = {r['item_id']: r for r in recs}
    lab = {i: labels.get(i, (by[i]['judged'], by[i]['wrong_type'])) for i in by}
    both = [i for i in vms['P-FROZEN'] if i in vms['P-1K']]
    disc = collections.Counter()
    ex = []
    for i in both:
        a, b = vms['P-FROZEN'][i], vms['P-1K'][i]
        if a != b:
            disc['%s->%s' % (a, b)] += 1
            if len(ex) < 25:
                ex.append({'id': i, 'frozen': a, 'p1k': b, 'label': lab[i][0], 'type': lab[i][1],
                           'sk': by[i]['sk'], 'answer': by[i]['answer']})
    out = {'items_with_both_verdicts': len(both), 'discordant': dict(disc), 'examples': ex,
           'tip_switch': {}}
    for p in PROMPTS:
        for name in ('LOCKTIP', 'LOCKTIP+F8+F9 (ALL)'):
            for tip in (True, False):
                res = resmap[(name, p, tip)]
                m = score(recs, res, labels)
                out['tip_switch']['%s|%s|tip=%s' % (name, p, tip)] = {
                    'coverage': m['coverage'], 'fa': m['fa'],
                    'fa_T': m['fa_by_type']['T']}
    return out


# ================================================================== reports
def md_table(rows):
    L2 = ['| configuration | prompt | TIP-as-rejection | coverage | coverage (kind C) | FA | '
          'FA T | FA W | FA M | FA S | FA V | FA E |',
          '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for r in rows:
        L2.append('| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |'
                  % (r['name'], r['prompt'], 'on' if r['tip_reject'] else 'off',
                     _r(r['coverage']), _r(r['coverage_kindC']), _r(r['fa']),
                     _r(r['fa_by_type']['T']), _r(r['fa_by_type']['W']), _r(r['fa_by_type']['M']),
                     _r(r['fa_by_type']['S']), _r(r['fa_by_type']['V']), _r(r['fa_by_type']['E'])))
    return L2


def write_measure_reports(A, rows, pick, trace, ext, tc, calls, sel_row, prompt_shas):
    os.makedirs(TASKA, exist_ok=True)
    os.makedirs(TASKD, exist_ok=True)
    json.dump(A, open(os.path.join(TASKA, 'TASK_A_RELABEL.json'), 'w'), indent=1, ensure_ascii=False)
    mv = A['movement']
    a = ['# Phase 1k — Task A: the relabelling, DEV (agent R)', '',
         'New DEV labels = the blind judge\'s §0 verdicts, **adopted in full (label AND type)** for all '
         '490 DEV items. Movement is measured against the Phase 1j arm-B **primary** labels. Large '
         'movement is expected: §0 changed what "correct" means. No number below may be compared with a '
         'Phase 1j number that used the old definition.', '',
         '## Conventions declared for this phase', '']
    for k, v in A['conventions'].items():
        a.append('- **%s** — %s' % (k, v))
    a += ['', '## Movement, Phase 1j arm-B primary -> Phase 1k judge', '',
          '| direction | n |', '|---|---|',
          '| items compared | %d |' % mv['n'],
          '| unchanged | %d |' % mv['unchanged'],
          '| correct -> wrong | %d |' % sum(mv['correct_to_wrong'].values()),
          '| wrong -> correct | %d |' % sum(mv['wrong_to_correct_by_old_type'].values()),
          '| wrong -> wrong, type changed | %d |' % sum(mv['wrong_to_wrong_matrix'].values()),
          '| DEV items without a judge verdict | %d |' % mv['missing_judge_label'], '',
          '**correct -> wrong, by NEW type:** `%s`' % json.dumps(mv['correct_to_wrong']), '',
          '**wrong -> correct, by OLD type:** `%s`' % json.dumps(mv['wrong_to_correct_by_old_type']), '',
          '**wrong -> correct, by the layer that rejected them in the frozen 1j arm-B run (TIP on):** '
          '`%s`' % json.dumps(mv['wrong_to_correct_by_1j_layer']), '',
          '**wrong -> wrong type matrix (old -> new):** `%s`' % json.dumps(mv['wrong_to_wrong_matrix']),
          '', '## Cell sizes', '',
          '- Phase 1j arm-B primary: `%s`' % json.dumps(A['old_cells_1j_primary']),
          '- Phase 1k judge (new): `%s`' % json.dumps(A['new_cells_1k_judge']), '']
    open(os.path.join(TASKA, 'TASK_A_RELABEL.md'), 'w', encoding='utf-8').write('\n'.join(a) + '\n')

    dev = {'conventions': A['conventions'], 'task_a': A, 'rows': rows, 'selection': trace,
           'selected': {k: pick[k] for k in ('name', 'prompt', 'locktip', 'f8', 'f9', 'f9_strict',
                                             'tip_reject', 'moving_parts')},
           'selected_numbers': {'coverage': pick['coverage'], 'coverage_kindC': pick['coverage_kindC'],
                                'fa': pick['fa'], 'fa_by_type': pick['fa_by_type'],
                                'fa_by_layer': pick['fa_by_layer'], 'fr_by_layer': pick['fr_by_layer']},
           'extras': ext, 'task_c': tc, 'calls': calls, 'prompt_shas': prompt_shas}
    json.dump(dev, open(os.path.join(TASKD, 'dev_results.json'), 'w'), indent=1, ensure_ascii=False)
    return dev


# ================================================================== main: measure
def measure(max_calls):
    purpose = 'Phase 1k agent R: DEV measurement (Tasks A-D)'
    st, recs, ann, by = build_side('dev', purpose)
    labels, _k, _v = judge_labels('dev', purpose)
    print('judge DEV labels: %d of %d items' % (len(labels), len(recs)))

    st_lock = dict(st, decide=locktip_decide(st['decide']))
    l3 = sorted(i for i, v in P.run_pipeline(st_lock, {}).items() if v['reached_l3'])
    l3_base = sorted(i for i, v in P.run_pipeline(st, {}).items() if v['reached_l3'])
    print('L3-eligible under LOCKTIP: %d (frozen 1j arm B reached L3 on %d)' % (len(l3), len(l3_base)))

    vms, hashes, rep, cstat = collect_verdicts(st, recs, l3, PROMPTS, max_calls, True, 'DEV')
    guards_by_strict = {False: guard_readouts(recs, ann, False),
                        True: guard_readouts(recs, ann, True)}
    rows, resmap = all_rows(st, recs, vms, guards_by_strict, labels)
    A = task_a(recs, labels, resmap[('BASE', 'P-FROZEN', True)])
    pick, trace = select(rows)
    sel_key = (pick['name'], pick['prompt'], pick['tip_reject'])
    ext = extras(recs, resmap, guards_by_strict[pick['f9_strict']], labels, sel_key)
    tc = task_c(recs, vms, resmap, labels)
    calls = token_spend()
    calls.update({'reused_prompts': cstat['reused'], 'new_this_run': cstat['new'],
                  'no_verdict_items': {p: len(v) for p, v in cstat['no_verdict'].items()},
                  'phase_budget_remaining': PHASE_CAP - calls['counted_calls_http200']})
    prompt_shas = {p: prompt_template_sha(p) for p in PROMPTS}
    dev = write_measure_reports(A, rows, pick, trace, ext, tc, calls, pick, prompt_shas)

    cfg = {'phase': '1k', 'side_measured': 'dev', 'model': P.MODEL,
           'generationConfig': P.GEN_CFG,
           'selected': dev['selected'],
           'prompt_id': pick['prompt'], 'prompt_template_sha256': prompt_shas[pick['prompt']],
           'prompt': {'base': 'the frozen P-B lines of checker_1i.prompt(it, "P-B")',
                      'extra_lines_in_order': ['gender line (only when the annotation still has g)',
                                               'ground line', 'wording line']
                      + (['P-1K rule: judge against the Slovak', 'P-1K rule: voice (B1)',
                          'P-1K rule: time frame (B2/B3)'] if pick['prompt'] == 'P-1K' else []),
                      'gender_template': P.GENDER_TMPL, 'ground_line': P.GROUND_LINE,
                      'wording_line': P.WORDING_LINE,
                      'new_rules_verbatim': list(NEW_RULES) if pick['prompt'] == 'P-1K' else [],
                      'tail': 'SAME, TIP or DIFF?'},
           'system_instruction': SYS_TEXT_CACHE.get('sys', ''),
           'switches': {'l2_lock_rejects': not pick['locktip'],
                        'lock_mismatch_becomes_tip': pick['locktip'],
                        'F8': pick['f8'], 'F9': pick['f9'],
                        'f9_REPORTED_STRICT': pick['f9_strict'],
                        'tip_as_rejection': pick['tip_reject'],
                        'old_guards': ['F3', 'F5', 'F4v2', 'F4v3', 'F2B'],
                        'F2B_not_applied_to_lock_released_items': True},
           'guard_sha256': {'f8.py': fsha(os.path.join(K, 'taskB', 'f8.py')),
                            'f9.py': fsha(os.path.join(K, 'taskB', 'f9.py'))},
           'label_conventions': A['conventions'],
           'selection_trace': trace,
           'selected_dev_numbers': {'coverage': pick['coverage'],
                                    'coverage_kindC': pick['coverage_kindC'], 'fa': pick['fa'],
                                    'fa_by_type': pick['fa_by_type']},
           'data': 'Phase 1j arm-B Slovak/refs/annotations for dev+replay1j; phase1k/fresh/* for fresh'}
    json.dump(cfg, open(FROZEN, 'w'), indent=1, ensure_ascii=False)

    # ---- markdown
    M = ['# Phase 1k — Task B/C/D: the DEV measurement (agent R)', '',
         'Model **gemini-3.1-flash-lite**, temperature 0, thinkingBudget 0. Labels = the blind judge\'s '
         '§0 verdicts, adopted in full. Coverage denominator = all items judged correct; FA denominator '
         '= all items judged wrong. Every L3-eligible item has a verdict under BOTH prompts, so every '
         'guard and switch below is a zero-call readout on the same stored verdicts.', '',
         '## 1 The table', ''] + md_table(rows) + ['',
         '## 2 What the lock released', '', '```', json.dumps(ext['lock_released'], indent=1), '```', '',
         '## 3 F8 / F9 caught and cost', '', '```', json.dumps(ext['guards'], indent=1), '```', '',
         '## 4 B3 line (F9 tip / abstain)', '', '```', json.dumps(ext['b3'], indent=1), '```', '',
         '## 5 Task C — P-1K vs P-FROZEN on identical items', '', '```',
         json.dumps({k: v for k, v in tc.items() if k != 'examples'}, indent=1)[:6000], '```', '',
         '## 6 Selection', ''] + ['- %s' % t for t in trace] + ['',
         '## 7 Calls', '', '```', json.dumps(calls, indent=1), '```', '']
    open(os.path.join(TASKD, 'TASK_D_DEV.md'), 'w', encoding='utf-8').write('\n'.join(M) + '\n')

    print('\n== ROWS ==')
    for r in rows:
        print('%-28s %-9s tip=%-5s cov %-24s FA %-24s T %s'
              % (r['name'], r['prompt'], r['tip_reject'], _r(r['coverage']), _r(r['fa']),
                 _r(r['fa_by_type']['T'])))
    print('\n== SELECTION ==')
    for t in trace:
        print('  ' + t)
    print('lock released: %s' % json.dumps(ext['lock_released']))
    print('guards: %s' % json.dumps(ext['guards']))
    print('B3: %s' % json.dumps(ext['b3']))
    print('task C: %s' % json.dumps({k: v for k, v in tc.items() if k != 'examples'}))
    print('calls: %s' % json.dumps(calls))
    print('task A: %s' % json.dumps(A['movement']))
    return dev, cfg


# ================================================================== main: final
def final(side, max_calls):
    cfg = json.load(open(FROZEN, encoding='utf-8'))
    sel = cfg['selected']
    if side == 'fresh':
        if os.path.exists(DONE):
            raise SystemExit('REFUSED: %s exists — the fresh side is measured once.' % DONE)
        os.environ['PHASE1K_OPEN_FRESH'] = '1'
    purpose = 'Phase 1k FINAL run of the frozen config, side %s' % side
    st, recs, ann, by = build_side(side, purpose)
    src = {'dev': 'dev', 'fresh': 'fresh', 'replay1j': 'holdout1j'}[side]
    labels, keyrows, _v = judge_labels(src, purpose)
    for r in recs:                                   # adopt the judge label+type in full
        if r['item_id'] in labels:
            r['judged'], r['wrong_type'] = labels[r['item_id']]
    stx = dict(st, decide=locktip_decide(st['decide'])) if sel['locktip'] else st
    l3 = sorted(i for i, v in P.run_pipeline(stx, {}).items() if v['reached_l3'])
    vms, hashes, rep, cstat = collect_verdicts(st, recs, l3, (sel['prompt'],), max_calls,
                                               side != 'dev', side.upper())
    guards = guard_readouts(recs, ann, sel['f9_strict'])
    res = configure_row(st, recs, vms[sel['prompt']], sel['locktip'], guards, sel['f8'], sel['f9'],
                        sel['tip_reject'])
    m = score(recs, res, labels)
    lab = {i: labels.get(i, (by[i]['judged'], by[i]['wrong_type'])) for i in by}

    def itemise(ids):
        out = []
        for i in ids:
            r = by[i]
            out.append({'id': i, 'layer': res[i]['layer'], 'model_reply':
                        rep.get(hashes[sel['prompt']].get(i), ''), 'model': res[i]['model'],
                        'slovak': r['sk'], 'answer': r['answer'], 'reference': r.get('reference'),
                        'judge_label': lab[i][0], 'judge_type': lab[i][1],
                        'intent': r.get('intent'),
                        'f8': (guards[i]['f8'] or {}).get('verdict'),
                        'f9': (guards[i]['f9'] or {}).get('verdict')})
        return out
    out = {'side': side, 'frozen': cfg, 'coverage': m['coverage'],
           'coverage_kindC': m['coverage_kindC'], 'fa': m['fa'], 'fa_by_type': m['fa_by_type'],
           'fa_by_layer': m['fa_by_layer'], 'fr_by_layer': m['fr_by_layer'],
           'false_acceptances': itemise([f['id'] for f in m['fa_items']]),
           'false_rejections': itemise([f['id'] for f in m['false_rejections']]),
           'b3': {v: {'n': sum(1 for i in by if (guards[i]['f9'] or {}).get('verdict') == v),
                      'judged_correct': sum(1 for i in by
                                            if (guards[i]['f9'] or {}).get('verdict') == v
                                            and lab[i][0] == 'correct'),
                      'judged_wrong': sum(1 for i in by
                                          if (guards[i]['f9'] or {}).get('verdict') == v
                                          and lab[i][0] == 'wrong'),
                      'cost_type_T_wrong_accepted': sum(1 for i in by
                                                        if (guards[i]['f9'] or {}).get('verdict') == v
                                                        and lab[i] == ('wrong', 'T')
                                                        and res[i]['accepted'])}
                  for v in ('tip', 'abstain')},
           'calls': token_spend(), 'reused_prompts': cstat['reused'], 'new_this_run': cstat['new'],
           'no_verdict_items': cstat['no_verdict']}
    out['calls']['phase_budget_remaining'] = PHASE_CAP - out['calls']['counted_calls_http200']

    if side == 'fresh':
        out['judge_noise_controls'] = control_noise(purpose)
        cells = collections.Counter()
        for r in recs:
            cells['%s|%s' % (r.get('intent'), '%s:%s' % lab[r['item_id']])] += 1
        out['intent_x_label'] = dict(cells)
        for nm, intent in (('active_to_passive_cell', 'V'), ('time_frame_shift_cell', 'TF')):
            ids = [i for i in by if by[i].get('intent') == intent and lab[i][0] == 'wrong']
            acc = [i for i in ids if res[i]['accepted']]
            out[nm] = {'intent': intent, 'judged_wrong': len(ids), 'accepted': len(acc),
                       'rate': P.rate(len(acc), len(ids)),
                       'rejecting_layers': dict(collections.Counter(res[i]['layer'] for i in ids
                                                                    if not res[i]['accepted'])),
                       'accepted_items': itemise(acc)}
        # out-of-sample F9 check, reporting only
        chk = {'agree': 0, 'conservative': 0, 'error': 0, 'errors': []}
        for s in L.load_fresh_sentences(purpose=purpose):
            g = s.get('tf_gold')
            try:
                fr = f9.sk_frame(s['sk'])
            except Exception as e:
                fr = {'frames': None, 'reason': 'error %s' % type(e).__name__}
            frames = fr.get('frames')
            if g == 'mixed' or not frames:
                chk['conservative'] += 1
            elif list(frames) == [g]:
                chk['agree'] += 1
            elif g in frames:
                chk['conservative'] += 1
            else:
                chk['error'] += 1
                chk['errors'].append({'sid': s['sid'], 'sk': s['sk'], 'tf_gold': g,
                                      'script': list(frames), 'reason': fr.get('reason')})
        chk['error_rate'] = P.rate(chk['error'], 70)
        out['f9_out_of_sample_tf_check'] = chk

    os.makedirs(TASKD, exist_ok=True)
    name = {'dev': 'dev_reproduction', 'fresh': 'fresh_results', 'replay1j': 'replay1j_results'}[side]
    json.dump(out, open(os.path.join(TASKD, '%s.json' % name), 'w'), indent=1, ensure_ascii=False)

    T = ['# Phase 1k — %s' % {'dev': 'DEV reproduction of the frozen config (zero calls)',
                              'fresh': 'FRESH results — the one measurement of the frozen config',
                              'replay1j': 'ALREADY-SEEN DATA — not the headline (Phase 1j holdout '
                                          'replay)'}[side], '',
         'Frozen config: **%s / %s / TIP-as-rejection %s** (F8 %s, F9 %s, REPORTED_STRICT %s).'
         % (sel['name'], sel['prompt'], 'on' if sel['tip_reject'] else 'off', sel['f8'], sel['f9'],
            sel['f9_strict']), '',
         '| metric | value |', '|---|---|',
         '| coverage | %s |' % _r(out['coverage']),
         '| coverage (kind C only) | %s |' % _r(out['coverage_kindC']),
         '| FA | %s |' % _r(out['fa'])]
    for t in TYPES:
        T.append('| FA type %s | %s |' % (t, _r(out['fa_by_type'][t])))
    if side == 'fresh':
        T += ['| ACTIVE->PASSIVE cell (intent V, judged wrong) | %s accepted of %d, layers %s |'
              % (out['active_to_passive_cell']['accepted'], out['active_to_passive_cell']['judged_wrong'],
                 json.dumps(out['active_to_passive_cell']['rejecting_layers'])),
              '| TIME-FRAME-SHIFT cell (intent TF, judged wrong) | %s accepted of %d, layers %s |'
              % (out['time_frame_shift_cell']['accepted'],
                 out['time_frame_shift_cell']['judged_wrong'],
                 json.dumps(out['time_frame_shift_cell']['rejecting_layers']))]
        T += ['', '## Judge noise (60 controls)', '', '```',
              json.dumps(out['judge_noise_controls'], indent=1), '```', '',
              '## Writer intent x judge label', '', '```', json.dumps(out['intent_x_label'], indent=1),
              '```', '', '## F9 out-of-sample time-frame check (reporting only)', '', '```',
              json.dumps(out['f9_out_of_sample_tf_check'], indent=1), '```']
    T += ['', '## B3 line', '', '```', json.dumps(out['b3'], indent=1), '```', '',
          '## Every false acceptance', ''] + ['- `%s`' % json.dumps(x, ensure_ascii=False)
                                              for x in out['false_acceptances']] + \
        ['', '## Every false rejection', ''] + ['- `%s`' % json.dumps(x, ensure_ascii=False)
                                                for x in out['false_rejections']] + \
        ['', '## Calls', '', '```', json.dumps(out['calls'], indent=1), '```', '']
    fn = {'dev': 'DEV_REPRODUCTION.md', 'fresh': 'FRESH_TABLES.md',
          'replay1j': 'REPLAY1J_TABLES.md'}[side]
    open(os.path.join(TASKD, fn), 'w', encoding='utf-8').write('\n'.join(T) + '\n')

    print('side=%s  coverage %s  FA %s' % (side, _r(out['coverage']), _r(out['fa'])))
    for t in TYPES:
        print('  FA %s %s' % (t, _r(out['fa_by_type'][t])))
    print('  layers FA %s  FR %s' % (json.dumps(out['fa_by_layer']), json.dumps(out['fr_by_layer'])))
    print('  calls %s' % json.dumps(out['calls']))
    if side == 'dev':
        exp = cfg['selected_dev_numbers']
        ok = (out['coverage']['k'] == exp['coverage']['k'] and out['coverage']['n'] == exp['coverage']['n']
              and out['fa']['k'] == exp['fa']['k'] and out['fa']['n'] == exp['fa']['n']
              and cstat['new'] == 0)
        print('DEV reproduction with ZERO new calls: %s' % ('OK' if ok else 'MISMATCH'))
    if side == 'fresh':
        open(DONE, 'w').write(json.dumps({'coverage': out['coverage'], 'fa': out['fa']}) + '\n')
        print('FINAL_RUN_DONE written — the fresh side is closed.')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=('measure', 'final'))
    ap.add_argument('--side', choices=('dev', 'fresh', 'replay1j'), default='dev')
    ap.add_argument('--max-calls', type=int, default=MY_CAP)
    a = ap.parse_args()
    if a.max_calls > MY_CAP and a.mode == 'measure':
        raise SystemExit('REFUSED: agent R may use at most %d counted calls' % MY_CAP)
    if a.mode == 'measure':
        measure(a.max_calls)
    else:
        final(a.side, a.max_calls)


if __name__ == '__main__':
    main()
