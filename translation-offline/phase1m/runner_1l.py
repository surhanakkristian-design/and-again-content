#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1L — the corrected fresh measurement of the FROZEN Phase 1k configuration.

    PYTHONDONTWRITEBYTECODE=1 python3 -B phase1l/runner_1l.py dev
    PYTHONDONTWRITEBYTECODE=1 python3 -B phase1l/runner_1l.py fresh --max-calls 1200

Frozen rule set (unchanged, imported from phase1k): arm B, Slovak-anchored acceptance, LOCKTIP
(the L2 structure lock is a TIP source, not a rejector), F8, F9, prompt P-FROZEN, TIP-as-rejection
ON, f9.REPORTED_STRICT False. Model gemini-3.1-flash-lite, temperature 0, thinkingBudget 0.

Three changes only, all from the owner's brief:
  2.1  the fresh builder computes `chk` with the deterministic checker instead of asserting
       {'verdict': 'correct', 'step': 'L1'} (the Phase 1k defect that sent every fresh item to L1
       and produced 0 model calls);
  2.2  F9's negated-present fix (phase1l/f9.py, rebound over runner_1k.f9);
  2.3  the reference-hygiene pass (phase1l/hygiene/out_<side>_*.json) applied to the accepted
       reference lists, measured before AND after.

Transport: counted = HTTP 200 only. 0/429/5xx are retried with backoff and logged counted:false.
An empty 200 is a FAILED call: counted, never retried, never guessed. Every call goes to
phase1l/calls.jsonl. phase1j/ and phase1k/ are read-only: their ledgers are read for reuse, never
written. Every read of fresh data is logged to phase1l/access_log.jsonl through loader_1l.
"""
import sys
sys.dont_write_bytecode = True

import argparse                                                           # noqa: E402
import collections                                                        # noqa: E402
import copy                                                               # noqa: E402
import glob                                                               # noqa: E402
import json                                                               # noqa: E402
import os                                                                 # noqa: E402
import random                                                             # noqa: E402
import subprocess                                                         # noqa: E402
import threading                                                          # noqa: E402
import time                                                               # noqa: E402
from concurrent.futures import ThreadPoolExecutor                         # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
P1J = os.path.join(TOFF, 'phase1j')
P1K = os.path.join(TOFF, 'phase1k')
REPO = os.path.dirname(TOFF)
for _p in (HERE, P1K, os.path.join(P1K, 'taskB'), os.path.join(P1J, 'taskC')):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import loader_1l as L                                                     # noqa: E402
import runner_1k as R1K                                                   # noqa: E402

# runner_1k prepends phase1k/taskB to sys.path, so a plain `import f9` would bind the PHASE 1K copy.
# Put phase1l first again, drop the phase1k modules, and import f9 BEFORE f8 (f8 does `import f9`
# and must see the phase1l one).
sys.path.insert(0, HERE)
for _m in ('f8', 'f9'):
    sys.modules.pop(_m, None)
import f9 as f9_1l                                                        # noqa: E402
import f8 as f8_1l                                                        # noqa: E402

R1K.f8, R1K.f9 = f8_1l, f9_1l                     # 2.2: the phase1l copies, not phase1k/taskB
assert os.path.dirname(os.path.abspath(R1K.f9.__file__)) == HERE, 'F9 rebind failed'
assert os.path.dirname(os.path.abspath(R1K.f8.__file__)) == HERE, 'F8 rebind failed'

R = R1K.R                                         # phase1j/taskC/runner_1j
P = R1K.P                                         # phase1i/pipeline_1i
C = R._C                                          # phase1i/checker_1i

LEDGERS_RO = [os.path.join(P1J, 'ledger.jsonl'), os.path.join(P1K, 'ledger.jsonl')]
CALLS = os.path.join(HERE, 'calls.jsonl')
ACCESS = os.path.join(HERE, 'access_log.jsonl')
HYG = os.path.join(HERE, 'hygiene')
FREEZE_HASH = os.path.join(HERE, 'FREEZE_HASH')
DONE = os.path.join(HERE, 'FINAL_RUN_DONE')
STOP_PRE = os.path.join(HERE, 'STOP_PREFLIGHT.txt')
STOP_PLAN = os.path.join(HERE, 'STOP_PLAN.txt')
FROZEN = os.path.join(P1K, 'FROZEN_CONFIG_1K.json')
TYPES = R1K.TYPES
PRICE_IN, PRICE_OUT = 0.25 / 1e6, 1.50 / 1e6
PLAN_CAP = 1200
PHASE_CAP = 2000
EXCLUDE_SID = 140006
DEV_TARGET = {'coverage': (182, 189), 'fa': (12, 301)}
REPLAY_TARGET = {'coverage_pct': 90.82, 'fa_pct': 5.10, 'faT_pct': 3.39}


def alog(side, what, n, purpose):
    L._log(side, what, n, purpose, caller='runner_1l.py')


# ================================================================== 2.1 the builder
def compute_chk(r):
    """The deterministic checker's own verdict for one record — never asserted.

    Exactly the two offline-decidable branches of `lib_prev.route`'s input:
      * `verdict='correct', step='match'`  when the normalised answer equals one of the accepted
        references `checker_1i.refs_of(it)` = [reference] + annotation `v` (+ the 2.3 gender
        variants), i.e. the same L1 test the DEV records carry;
      * `verdict='wrong', step='mistake'`  when an annotation mistake pattern matches;
      * otherwise `verdict='wrong', step='auto'` -> the item is routed to L2/L3 like any DEV item.
    The production checker's `spelling_variant` step is NOT reproducible offline and is therefore
    never produced (recorded in RECORDED_NOT_MADE.md).
    """
    it = {'exercise_id': r['sid'], 'reference': r['reference'], 'answer': r['answer'],
          'item_id': r['item_id'], 'sk': r['sk']}
    n = C.base.norm(r['answer'])
    try:
        refs = C.refs_of(it)
    except Exception:
        refs = [r['reference']] + list(r.get('refs') or [])
    for x in refs:
        if isinstance(x, str) and C.base.norm(x) == n:
            return {'verdict': 'correct', 'step': 'match', 'feedback': ''}, 'match'
    try:
        a = C.annot(r['sid']) or {}
        for pat in (a.get('m') or []):
            if isinstance(pat, str) and C.pattern_match(C.parse_lock(pat), r['answer']):
                return {'verdict': 'wrong', 'step': 'mistake', 'feedback': pat}, 'mistake'
    except Exception:
        pass
    return {'verdict': 'wrong', 'step': 'auto', 'feedback': ''}, 'auto'


def hygiene_patches(side, purpose):
    """{sid: patch} from phase1l/hygiene/out_<side>_*.json. Missing files = no hygiene."""
    out, files = {}, sorted(glob.glob(os.path.join(HYG, 'out_%s_*.json' % side)))
    for p in files:
        rows = json.load(open(p, encoding='utf-8'))
        for x in rows:
            out[int(x['sid'])] = x
    alog('1l:hygiene', 'hygiene patches side=%s files=%s' % (side, [os.path.basename(f) for f in files]),
         len(out), purpose)
    return out, files


def apply_hygiene(recs, ann, patches):
    """Apply {remove, replace} to the accepted reference set of each sid, in memory only.

    The accepted set is [reference] + annotation `v`. `replace` rewrites a string wherever it
    occurs; `remove` drops it. If the DISPLAYED reference is itself removed, the first surviving
    `v` entry is promoted to reference (the reference is only the first member of the accepted
    set); if nothing survives, the reference is kept and the sid is reported as `ref_kept`.
    """
    st = {'sids_touched': set(), 'removed': 0, 'replaced': 0, 'ref_changed': 0, 'ref_kept': [],
          'examples': []}
    byd = collections.defaultdict(list)
    for r in recs:
        byd[int(r['sid'])].append(r)
    for sid, p in patches.items():
        rows = byd.get(sid)
        if not rows:
            continue
        rem = {str(x).strip() for x in (p.get('remove') or []) if str(x).strip()}
        rep = {str(x['from']).strip(): str(x['to']) for x in (p.get('replace') or [])
               if str(x.get('from', '')).strip()}
        a = ann.get(str(sid))
        hy = (a.get('hygienised') if isinstance(a, dict) and 'hygienised' in a else a) or {}
        v0 = [x for x in (hy.get('v') or []) if isinstance(x, str)]
        ref0 = rows[0]['reference']
        ref = rep.get(str(ref0).strip(), ref0)
        v = []
        for x in v0:
            xs = x.strip()
            if xs in rem:
                st['removed'] += 1
                continue
            if xs in rep:
                st['replaced'] += 1
                v.append(rep[xs])
            else:
                v.append(x)
        if str(ref0).strip() in rem:
            st['removed'] += 1
            if v:
                ref, v = v[0], v[1:]
            else:
                ref = ref0
                st['ref_kept'].append(sid)
        elif ref != ref0:
            st['replaced'] += 1
        if ref != ref0:
            st['ref_changed'] += 1
        if (v != v0) or (ref != ref0):
            st['sids_touched'].add(sid)
            if len(st['examples']) < 10:
                st['examples'].append({'sid': sid, 'reference_before': ref0, 'reference_after': ref,
                                       'v_before': v0, 'v_after': v,
                                       'reason': p.get('reason', '')})
        hy['v'] = v
        if isinstance(a, dict) and 'hygienised' not in a:
            a['v'] = v
        for r in rows:
            r['reference'] = ref
            r['refs'] = [ref] + v
    st['sids_touched'] = sorted(st['sids_touched'])
    return st


def build_side(side, hyg_on, purpose):
    """-> (st, recs, ann, by, info). Rebuilds the whole checker state; call it once per variant."""
    patches, hfiles = hygiene_patches('dev' if side in ('dev', 'replay1j') else 'fresh', purpose) \
        if hyg_on else ({}, [])
    info = {'hygiene_files': [os.path.basename(f) for f in hfiles]}
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
        alog('1j:%s' % s, 'items+annotations (arm B, runner_1j.load_side)', len(data[0]), purpose)
        recs0, ann0, ann_b0, sk_new, rew = copy.deepcopy(data)
        if patches:
            info['hygiene'] = apply_hygiene(recs0, ann_b0, patches)
        st, recs, pm = R.prep_arm('B', s, (recs0, ann0, ann_b0, sk_new, rew))
        ann = ann_b0
        if patches:                       # the references the DEV rows were matched against moved
            info['hygiene']['dev_chk_recomputed'] = []
            for r in recs:
                if int(r['sid']) in patches and r['chk']['verdict'] in ('correct', 'correct_with_tip'):
                    new, how = compute_chk(r)
                    if how != 'match':
                        info['hygiene']['dev_chk_recomputed'].append(r['item_id'])
                        r['chk'] = new
        return st, recs, ann, {r['item_id']: r for r in recs}, info

    if side != 'fresh':
        raise ValueError(side)
    os.environ['PHASE1K_OPEN_FRESH'] = '1'
    sents = {int(s['sid']): s for s in L.load_fresh_sentences(purpose=purpose)}
    ann = L.load_fresh_annotations(purpose=purpose)
    items = L.load_fresh_items(purpose=purpose)
    if patches:
        pass                                     # applied below, once the recs exist
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
             'chk': {'verdict': 'wrong', 'step': 'auto', 'feedback': ''}, 'chk_missing': False,
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
    if patches:
        info['hygiene'] = apply_hygiene(recs, ann, patches)
    st = R.make_state(recs, ann, ('F4v3',), side_tag='fresh1k')
    # ---- 2.1: the chk every fresh record carries is COMPUTED here, after the annotations are in
    how = collections.Counter()
    for r in recs:
        r['chk'], h = compute_chk(r)
        r['chk_missing'] = False
        how[h] += 1
    info['chk_computed'] = dict(how)
    return st, recs, ann, {r['item_id']: r for r in recs}, info


def dev_chk_calibration():
    """Does compute_chk() reproduce the stored DEV checker verdicts? (validation of 2.1, 0 calls)"""
    purpose = 'Phase 1L validation of the 2.1 builder against the stored DEV checker verdicts'
    st, recs, ann, by, _i = build_side('dev', False, purpose)
    agree = collections.Counter()
    mism = []
    for r in recs:
        got, how = compute_chk(r)
        a = (r['chk']['verdict'] in ('correct', 'correct_with_tip'))
        b = (got['verdict'] in ('correct', 'correct_with_tip'))
        agree['%s->%s' % (r['chk']['step'], how)] += 1
        if a != b:
            mism.append({'id': r['item_id'], 'stored': r['chk'], 'computed': got})
    return {'n': len(recs), 'step_transitions': dict(agree),
            'accept_disagreements': len(mism), 'examples': mism[:10]}


# ================================================================== layers / preflight
def l3_ids(st, locktip):
    stx = dict(st, decide=R1K.locktip_decide(st['decide'])) if locktip else st
    return sorted(i for i, v in P.run_pipeline(stx, {}).items() if v['reached_l3'])


def lock_counts(st, recs):
    """(L2 lock firings/rejections under BASE, L3-eligible under LOCKTIP)."""
    base = P.run_pipeline(st, {})
    lock_rej = [i for i, v in base.items() if v['layer'] == 'L2' and not v['accepted']]
    return lock_rej, l3_ids(st, True)


def preflight(st, recs, tag):
    lock_rej, l3 = lock_counts(st, recs)
    print('[PREFLIGHT %s] L2 lock firings/rejections under BASE: %d   L3-eligible under LOCKTIP: %d'
          % (tag, len(lock_rej), len(l3)))
    print('[PREFLIGHT %s] (DEV reference: 65 lock rejections / 318 L3-eligible; 1j replay 310/336)'
          % tag)
    if not lock_rej or not l3:
        open(STOP_PRE, 'w', encoding='utf-8').write(json.dumps(
            {'tag': tag, 'lock_rejections': len(lock_rej), 'l3_eligible': len(l3),
             'why': 'the builder produced a degenerate side (the Phase 1k defect); no model call was '
                    'made'}, indent=1) + '\n')
        raise SystemExit('STOP: preflight failed, %s written, 0 model calls made' % STOP_PRE)
    return lock_rej, l3


# ================================================================== transport
def ledger_state():
    """Verdicts + replies from phase1j, phase1k (read-only) and phase1l/calls.jsonl (ours)."""
    rep, ver, failed, counted_l = {}, {}, set(), 0
    for path, mine in [(p, False) for p in LEDGERS_RO] + [(CALLS, True)]:
        for row in R.ledger_rows(path):
            if row.get('http') != 200:
                continue
            if mine:
                counted_l += 1
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
    return rep, ver, failed, counted_l


_PACE = threading.Lock()
_LAST = [0.0]
MIN_INTERVAL = 0.30                               # free-tier pacing, as Phase 1k ran it (6 workers)


def pace():
    with _PACE:
        dt = time.time() - _LAST[0]
        if dt < MIN_INTERVAL:
            time.sleep(MIN_INTERVAL - dt)
        _LAST[0] = time.time()


def load_keys():
    """Free-tier key first, then the default key. Same file and same redaction as Phase 1k."""
    keys = []
    try:
        env = P.ENV
        if os.path.exists(env):
            for ln in open(env, encoding='utf-8'):
                ln = ln.strip()
                for name in ('GEMINI_API_KEY_FREE', 'GEMINI_API_KEY_FREETIER'):
                    if ln.startswith(name):
                        v = ln.split('=', 1)[1].strip().strip('"').strip("'")
                        if v:
                            keys.append(v)
    except Exception:
        pass
    k = P.load_key()
    if k not in keys:
        keys.append(k)
    return keys


def call_one(req, key, tries=5):
    """Phase 1k transport verbatim, writing into phase1l/calls.jsonl."""
    sysx, user, gcfg, h, variant, item_id = req
    body = {'systemInstruction': {'parts': [{'text': sysx}]},
            'contents': [{'role': 'user', 'parts': [{'text': user}]}],
            'generationConfig': gcfg}
    url = P.API % P.MODEL
    delay, row = 1.0, None
    for attempt in range(1, tries + 1):
        pace()
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
            P.ledger_append(CALLS, row)           # an EMPTY 200 stops here: counted, not retried
            return row
        row = {'ts': time.time(), 'model': P.MODEL, 'variant': variant, 'item_id': item_id,
               'req_hash': h, 'http': code, 'counted': False, 'verdict': None, 'reply': '',
               'latency_ms': lat, 'try': attempt, 'error': P._redact(raw or js, key),
               'transport_retry': True}
        P.ledger_append(CALLS, row)
        if attempt == tries:
            return row
        time.sleep(delay * (1.0 + random.random() * 0.3))
        delay = min(delay * 2, 16.0)
    return row


def token_spend():
    tin = tout = n200 = nempty = nretry = 0
    for row in R.ledger_rows(CALLS):
        if row.get('http') != 200:
            nretry += 1
            continue
        n200 += 1
        tin += row.get('prompt_tokens') or 0
        tout += (row.get('candidates_tokens') or 0) + (row.get('thoughts_tokens') or 0)
        if row.get('verdict') == 'PARSE_FAIL' or row.get('empty'):
            nempty += 1
    return {'counted_calls_http200': n200, 'failed_empty_200': nempty, 'non200_attempts': nretry,
            'tokens_in': tin, 'tokens_out': tout,
            'spend_usd': round(tin * PRICE_IN + tout * PRICE_OUT, 5),
            'phase_budget_remaining_estimate': PHASE_CAP - 667 - n200,
            'caveat': 'billed versus free-tier is NOT detectable from the response body; these are '
                      'list-price figures for the tokens the API reported.'}


# ================================================================== scoring
def col_metrics(recs, res, labels, drop_sid=None):
    by = {r['item_id']: r for r in recs if drop_sid is None or int(r['sid']) != drop_sid}
    lab = {i: labels.get(i, (by[i]['judged'], by[i]['wrong_type'])) for i in by}
    corr = [i for i in by if lab[i][0] == 'correct']
    corrC = [i for i in corr if by[i]['kind'] == 'C']
    wrong = [i for i in by if lab[i][0] == 'wrong']
    acc = {i for i in by if res[i]['accepted']}
    fa = [i for i in wrong if i in acc]
    fr = sorted(set(corr) - acc)
    m = {'n_items': len(by), 'coverage': P.rate(len(set(corr) & acc), len(corr)),
         'coverage_kindC': P.rate(len(set(corrC) & acc), len(corrC)),
         'fa': P.rate(len(fa), len(wrong)), 'fa_by_type': {}, 'fa_by_layer': {},
         'fr_by_layer': {}, 'fa_ids': sorted(fa), 'fr_ids': fr}
    for t in TYPES:
        n = [i for i in wrong if lab[i][1] == t]
        m['fa_by_type'][t] = P.rate(len([i for i in n if i in acc]), len(n))
    cfa = collections.Counter(res[i]['layer'] for i in fa)
    for layer, k in sorted(cfa.items(), key=lambda x: str(x[0])):
        m['fa_by_layer'][str(layer)] = P.rate(k, len(wrong))
    cfr = collections.Counter(res[i]['layer'] for i in fr)
    for layer, k in sorted(cfr.items(), key=lambda x: str(x[0])):
        m['fr_by_layer'][str(layer)] = P.rate(k, len(corr))
    m['targets'] = {
        'coverage >= 90%': {'point': (m['coverage']['pct'] or 0.0) >= 90.0,
                            'interval': m['coverage']['ci'][0] >= 90.0},
        'FA < 5%': {'point': (m['fa']['pct'] or 0.0) < 5.0, 'interval': m['fa']['ci'][1] < 5.0},
        'type-T FA < 5%': {'point': (m['fa_by_type']['T']['pct'] or 0.0) < 5.0,
                           'interval': m['fa_by_type']['T']['ci'][1] < 5.0}}
    return m


def _r(d):
    return '%d/%d = %.2f%% [%.2f, %.2f]' % (d['k'], d['n'], d['pct'] or 0.0, d['ci'][0], d['ci'][1])


# ================================================================== requests
def plan_requests(st, recs, ids, prompt_id, tag):
    by = {r['item_id']: r for r in recs}
    out = {}
    for i in ids:
        s, u, g, h = R1K.build_req(st, by[i], prompt_id)
        R1K.SYS_TEXT_CACHE['sys'] = s
        out[h] = (s, u, g, h, 'L-1L:%s' % tag, i)
    return out


def hashes_for(st, recs, ids, prompt_id):
    by = {r['item_id']: r for r in recs}
    return {i: R1K.build_req(st, by[i], prompt_id)[3] for i in ids}


# ================================================================== §5 accounting
def section5(side, st, recs, ann, by, res, guards, labels, sel, lock_rej, info_before, info_after):
    lab = {i: labels.get(i, (by[i]['judged'], by[i]['wrong_type'])) for i in by}
    base_res = R1K.configure_row(st, recs, {}, False, guards, False, False, sel['tip_reject'])
    sec = {}

    # --- what the L2 lock released
    lock_r = R1K.configure_row(st, recs, {}, True, guards, False, False, sel['tip_reject'])
    rel = {'rejected_at_L2_under_BASE': len(lock_rej),
           'released_by_LOCKTIP_total': 0, 'released_judged_correct': 0,
           'released_judged_wrong_by_type': {}}
    wr = collections.Counter()
    for i in by:
        if lock_r[i]['accepted'] and not base_res[i]['accepted']:
            rel['released_by_LOCKTIP_total'] += 1
            if lab[i][0] == 'correct':
                rel['released_judged_correct'] += 1
            else:
                wr[lab[i][1] or '?'] += 1
    rel['released_judged_wrong_by_type'] = dict(wr)
    sec['lock_released'] = rel

    # --- F8 / F9: caught, caught uniquely, own cost, with the model layer present
    lt = R1K.configure_row(st, recs, RES_VM[0], True, guards, False, False, sel['tip_reject'])
    gc = {}
    for g in ('f8', 'f9'):
        other = 'f9' if g == 'f8' else 'f8'
        caught, uniq, cost = [], [], []
        for i in by:
            if not lt[i]['accepted']:
                continue
            if (guards[i][g] or {}).get('verdict') != 'reject':
                continue
            (caught if lab[i][0] == 'wrong' else cost).append(i)
            if lab[i][0] == 'wrong' and (guards[i][other] or {}).get('verdict') != 'reject':
                uniq.append(i)
        gc[g.upper()] = {'caught_wrong': len(caught), 'caught_wrong_only_this_guard': len(uniq),
                         'own_cost_correct_rejected': len(cost),
                         'caught_ids': sorted(caught), 'cost_ids': sorted(cost),
                         'basis': 'on top of LOCKTIP with the model layer present'}
    sec['guard_cost'] = gc

    # --- the B3 tip / abstain line and its type-T cost
    sec['b3_tip_abstain'] = {
        v: {'n': sum(1 for i in by if (guards[i]['f9'] or {}).get('verdict') == v),
            'judged_correct': sum(1 for i in by if (guards[i]['f9'] or {}).get('verdict') == v
                                  and lab[i][0] == 'correct'),
            'judged_wrong': sum(1 for i in by if (guards[i]['f9'] or {}).get('verdict') == v
                                and lab[i][0] == 'wrong'),
            'cost_type_T_wrong_accepted': sum(1 for i in by
                                              if (guards[i]['f9'] or {}).get('verdict') == v
                                              and lab[i] == ('wrong', 'T') and res[i]['accepted'])}
        for v in ('tip', 'abstain')}

    # --- the four unpatched §5.4 guard bugs: does each still FIRE on this side? (patch NONE)
    strict = R1K.guard_readouts(recs, ann, True)
    bug1 = [i for i in by if lab[i][0] == 'wrong' and res[i]['accepted']
            and by[i].get('intent') == 'V' and (guards[i]['f8'] or {}).get('verdict') != 'reject']
    bug2 = [i for i in by if (strict[i]['f9'] or {}).get('verdict')
            != (guards[i]['f9'] or {}).get('verdict')]
    bug3 = [i for i in by if res[i].get('layer') and lock_r[i]['accepted']
            and not base_res[i]['accepted']]
    bug4 = [i for i in by if by[i]['chk']['step'] == 'mistake']
    sec['unpatched_guard_bugs_5_4'] = {
        '1 F8 fires only on an English passive main clause': {
            'still_fires': bool(bug1), 'count': len(bug1),
            'sids': sorted({by[i]['sid'] for i in bug1}), 'ids': sorted(bug1),
            'measured_as': 'items judged wrong with writer intent V that the frozen stack accepted '
                           'and F8 did not reject'},
        '2 F9 inert on DEV, REPORTED_STRICT frozen untested': {
            'still_fires': not bool(bug2), 'items_where_strict_changes_F9': len(bug2),
            'ids': sorted(bug2),
            'measured_as': 'F9 readout with REPORTED_STRICT True vs the frozen False; 0 = the switch '
                           'is still untested on this side'},
        '3 F2B not applied to lock-released items': {
            'still_fires': bool(bug3), 'count': len(bug3),
            'sids': sorted({by[i]['sid'] for i in bug3}), 'ids': sorted(bug3),
            'measured_as': 'items LOCKTIP released, which F2B never sees'},
        '4 an L2 step=="mistake" rejection is not released': {
            'still_fires': bool(bug4), 'count': len(bug4),
            'sids': sorted({by[i]['sid'] for i in bug4}), 'ids': sorted(bug4),
            'measured_as': 'items whose computed chk step is "mistake"'}}
    sec['patched'] = 'NONE — all four are recorded and deliberately left unpatched.'

    # --- hygiene
    hb = (info_after or {}).get('hygiene') or {}
    sec['hygiene'] = {'files': (info_after or {}).get('hygiene_files') or [],
                      'sids_touched': hb.get('sids_touched', []),
                      'references_removed': hb.get('removed', 0),
                      'references_replaced': hb.get('replaced', 0),
                      'display_reference_changed': hb.get('ref_changed', 0),
                      'reference_kept_because_nothing_survived': hb.get('ref_kept', []),
                      'examples': hb.get('examples', [])}
    sec['builder_2_1'] = {'chk_computed_fresh': (info_after or {}).get('chk_computed'),
                          'chk_computed_before_hygiene': (info_before or {}).get('chk_computed')}
    return sec


def f9_fresh_validation(purpose):
    """F9 sk_frame vs the stored tf_gold on the 70 fresh sentences (agree/conservative/error)."""
    chk = {'agree': 0, 'conservative': 0, 'error': 0, 'errors': [], 'rows': []}
    sents = L.load_fresh_sentences(purpose=purpose)
    for s in sents:
        g = s.get('tf_gold')
        try:
            fr = f9_1l.sk_frame(s['sk'])
        except Exception as e:
            fr = {'frames': None, 'reason': 'error %s' % type(e).__name__}
        frames = fr.get('frames')
        if g == 'mixed' or not frames:
            v = 'conservative'
        elif list(frames) == [g]:
            v = 'agree'
        elif g in frames:
            v = 'conservative'
        else:
            v = 'error'
            chk['errors'].append({'sid': s['sid'], 'sk': s['sk'], 'tf_gold': g,
                                  'script': list(frames), 'reason': fr.get('reason')})
        chk[v] += 1
        chk['rows'].append({'sid': s['sid'], 'tf_gold': g, 'script': list(frames or []),
                            'verdict': v})
    chk['n'] = len(sents)
    chk['error_rate'] = P.rate(chk['error'], len(sents))
    return chk


RES_VM = [{}]                                     # the verdict map the §5 block scores against


# ================================================================== modes
def run_dev(args):
    cfg = json.load(open(FROZEN, encoding='utf-8'))
    sel = cfg['selected']
    print('== Phase 1L DEV regression — frozen config %s / %s / TIP %s (F8 %s, F9 %s, strict %s)'
          % (sel['name'], sel['prompt'], sel['tip_reject'], sel['f8'], sel['f9'], sel['f9_strict']))
    cal = dev_chk_calibration()
    print('-- 2.1 builder calibration on DEV: %d items, accept-disagreements %d, transitions %s'
          % (cal['n'], cal['accept_disagreements'], json.dumps(cal['step_transitions'])))
    out = {'mode': 'dev', 'builder_calibration': cal, 'sides': {}}
    for side in ('dev', 'replay1j'):
        purpose = 'Phase 1L DEV-mode regression of the frozen config, side %s (zero new calls)' % side
        st, recs, ann, by, info = build_side(side, False, purpose)
        src = {'dev': 'dev', 'replay1j': 'holdout1j'}[side]
        labels, _kr, _v = R1K.judge_labels(src, purpose)
        for r in recs:
            if r['item_id'] in labels:
                r['judged'], r['wrong_type'] = labels[r['item_id']]
        lock_rej, l3 = lock_counts(st, recs)
        print('[%s] L2 lock firings/rejections under BASE %d   L3-eligible under LOCKTIP %d'
              % (side.upper(), len(lock_rej), len(l3)))
        req = plan_requests(st, recs, l3, sel['prompt'], side)
        hmap = hashes_for(st, recs, l3, sel['prompt'])
        rep, ver, failed, counted_l = ledger_state()
        miss = [h for h in req if h not in ver and h not in failed]
        if miss:
            print('[%s] CACHE MISS %d prompts — reported, NOT called (dev mode makes no call)'
                  % (side.upper(), len(miss)))
        vm = {i: ver[h] for i, h in hmap.items() if h in ver}
        guards = R1K.guard_readouts(recs, ann, sel['f9_strict'])
        res = R1K.configure_row(st, recs, vm, sel['locktip'], guards, sel['f8'], sel['f9'],
                                sel['tip_reject'])
        m = col_metrics(recs, res, labels)
        print('[%s] coverage %s' % (side.upper(), _r(m['coverage'])))
        print('[%s] FA       %s' % (side.upper(), _r(m['fa'])))
        print('[%s] FA T     %s' % (side.upper(), _r(m['fa_by_type']['T'])))
        print('[%s] FA layers %s' % (side.upper(), json.dumps({k: v['k'] for k, v
                                                               in m['fa_by_layer'].items()})))
        out['sides'][side] = {'coverage': m['coverage'], 'fa': m['fa'],
                              'fa_by_type': m['fa_by_type'],
                              'fa_by_layer': {k: v['k'] for k, v in m['fa_by_layer'].items()},
                              'fr_by_layer': {k: v['k'] for k, v in m['fr_by_layer'].items()},
                              'lock_rejections_BASE': len(lock_rej), 'l3_eligible': len(l3),
                              'cache_misses_not_called': len(miss)}
        if side == 'dev':
            e = DEV_TARGET
            out['sides'][side]['delta_vs_phase1k'] = {
                'coverage_phase1k': '%d/%d' % e['coverage'], 'fa_phase1k': '%d/%d' % e['fa'],
                'coverage_delta_k': m['coverage']['k'] - e['coverage'][0],
                'fa_delta_k': m['fa']['k'] - e['fa'][0]}
            print('[DEV] Phase 1k frozen DEV numbers: coverage %d/%d, FA %d/%d  -> delta %+d / %+d'
                  % (e['coverage'][0], e['coverage'][1], e['fa'][0], e['fa'][1],
                     m['coverage']['k'] - e['coverage'][0], m['fa']['k'] - e['fa'][0]))
        else:
            e = REPLAY_TARGET
            out['sides'][side]['delta_vs_phase1k'] = {
                'coverage_phase1k_pct': e['coverage_pct'], 'fa_phase1k_pct': e['fa_pct'],
                'faT_phase1k_pct': e['faT_pct'],
                'coverage_delta_pct': round((m['coverage']['pct'] or 0) - e['coverage_pct'], 2),
                'fa_delta_pct': round((m['fa']['pct'] or 0) - e['fa_pct'], 2),
                'faT_delta_pct': round((m['fa_by_type']['T']['pct'] or 0) - e['faT_pct'], 2)}
            print('[REPLAY1J] Phase 1k replay: 90.82 / 5.10 / 3.39  -> now %.2f / %.2f / %.2f'
                  % (m['coverage']['pct'] or 0, m['fa']['pct'] or 0,
                     m['fa_by_type']['T']['pct'] or 0))
        # ---- F9-fix cause analysis: which items move when F9 is the phase1l copy
        g_old = {}
        R1K.f9 = _F9_OLD
        try:
            g_old = R1K.guard_readouts(recs, ann, sel['f9_strict'])
        finally:
            R1K.f9 = f9_1l
        moved = [i for i in by if (g_old[i]['f9'] or {}).get('verdict')
                 != (guards[i]['f9'] or {}).get('verdict')]
        res_old = R1K.configure_row(st, recs, vm, sel['locktip'], g_old, sel['f8'], sel['f9'],
                                    sel['tip_reject'])
        m_old = col_metrics(recs, res_old, labels)
        out['sides'][side]['f9_fix_effect'] = {
            'items_whose_F9_readout_moved': len(moved), 'ids': sorted(moved)[:40],
            'coverage_with_phase1k_F9': m_old['coverage'], 'fa_with_phase1k_F9': m_old['fa'],
            'faT_with_phase1k_F9': m_old['fa_by_type']['T']}
        print('[%s] F9 fix: %d readouts moved; with the OLD F9 coverage %s FA %s'
              % (side.upper(), len(moved), _r(m_old['coverage']), _r(m_old['fa'])))

        # ---- dev before/after hygiene for the deterministic layers
        pat, files = hygiene_patches('dev', purpose)
        if pat and side == 'dev':
            st2, recs2, ann2, by2, info2 = build_side(side, True, purpose)
            for r in recs2:
                if r['item_id'] in labels:
                    r['judged'], r['wrong_type'] = labels[r['item_id']]
            l3b = l3_ids(st2, sel['locktip'])
            hm2 = hashes_for(st2, recs2, l3b, sel['prompt'])
            rep2, ver2, failed2, _c = ledger_state()
            need = [i for i, h in hm2.items() if h not in ver2 and h not in failed2]
            vm2 = {i: ver2[h] for i, h in hm2.items() if h in ver2}
            g2 = R1K.guard_readouts(recs2, ann2, sel['f9_strict'])
            res2 = R1K.configure_row(st2, recs2, vm2, sel['locktip'], g2, sel['f8'], sel['f9'],
                                     sel['tip_reject'])
            m2 = col_metrics(recs2, res2, labels)
            print('[DEV hygiene] before coverage %s FA %s' % (_r(m['coverage']), _r(m['fa'])))
            print('[DEV hygiene] after  coverage %s FA %s' % (_r(m2['coverage']), _r(m2['fa'])))
            print('[DEV hygiene] %d items would need a call (changed reference) — NOT called'
                  % len(need))
            out['dev_hygiene'] = {'files': [os.path.basename(f) for f in files],
                                  'before': {'coverage': m['coverage'], 'fa': m['fa']},
                                  'after': {'coverage': m2['coverage'], 'fa': m2['fa']},
                                  'would_need_a_call': sorted(need),
                                  'hygiene_stats': info2.get('hygiene')}
        elif side == 'dev':
            print('[DEV hygiene] no phase1l/hygiene/out_dev_*.json present — before/after not run')
            out['dev_hygiene'] = None
    json.dump(out, open(os.path.join(HERE, 'dev_regression.json'), 'w'), indent=1,
              ensure_ascii=False)
    print('-- written phase1l/dev_regression.json  (0 new model calls)')
    return out


def check_freeze():
    if not os.path.exists(FREEZE_HASH):
        raise SystemExit('REFUSED: %s does not exist — freeze the code first.' % FREEZE_HASH)
    h = open(FREEZE_HASH, encoding='utf-8').read().strip().split()[0]
    files = sorted(f for f in os.listdir(HERE) if f.endswith('.py'))
    bad = []
    for f in files:
        cur = subprocess.check_output(['git', 'hash-object', os.path.join(HERE, f)],
                                      cwd=REPO).decode().strip()
        try:
            was = subprocess.check_output(
                ['git', 'rev-parse', '%s:translation-offline/phase1l/%s' % (h, f)],
                cwd=REPO, stderr=subprocess.DEVNULL).decode().strip()
        except subprocess.CalledProcessError:
            was = None
        if cur != was:
            bad.append({'file': f, 'now': cur[:12], 'at_freeze': (was or 'ABSENT')[:12]})
    if bad:
        raise SystemExit('REFUSED: phase1l code differs from FREEZE_HASH %s: %s'
                         % (h, json.dumps(bad)))
    # FREEZE_HASH itself is excluded by construction: only *.py files are compared, and FREEZE_HASH
    # is not a .py file (it is also committed AFTER the code commit it names, so it cannot be inside
    # the tree it points at).
    print('[FREEZE] %d python files identical to commit %s' % (len(files), h))
    return h


def run_fresh(args):
    if os.path.exists(DONE):
        raise SystemExit('REFUSED: %s exists — the fresh side is measured once.' % DONE)
    fh = check_freeze()
    cfg = json.load(open(FROZEN, encoding='utf-8'))
    sel = cfg['selected']
    purpose = 'Phase 1L FINAL fresh run of the frozen Phase 1k configuration (the one measurement)'
    os.environ['PHASE1K_OPEN_FRESH'] = '1'

    # ---------------- build both reference variants
    st_b, recs_b, ann_b, by_b, info_b = build_side('fresh', False, purpose)
    lock_rej_b, l3_b = preflight(st_b, recs_b, 'FRESH/before-hygiene')
    req_b = plan_requests(st_b, recs_b, l3_b, sel['prompt'], 'before')
    hm_b = hashes_for(st_b, recs_b, l3_b, sel['prompt'])

    st_a, recs_a, ann_a, by_a, info_a = build_side('fresh', True, purpose)
    lock_rej_a, l3_a = preflight(st_a, recs_a, 'FRESH/after-hygiene')
    req_a = plan_requests(st_a, recs_a, l3_a, sel['prompt'], 'after')
    hm_a = hashes_for(st_a, recs_a, l3_a, sel['prompt'])

    req = dict(req_b)
    req.update(req_a)                              # dedupe by request hash: unchanged item = 1 call
    rep, ver, failed, counted_l = ledger_state()
    need = [h for h in req if h not in ver and h not in failed]
    print('[FRESH] L3-eligible before %d / after %d   unique requests %d   reused %d   NEW %d'
          % (len(l3_b), len(l3_a), len(req), len(req) - len(need), len(need)))
    if len(need) > min(PLAN_CAP, args.max_calls):
        open(STOP_PLAN, 'w', encoding='utf-8').write(json.dumps(
            {'planned_new_calls': len(need), 'cap': min(PLAN_CAP, args.max_calls),
             'why': 'the plan exceeds the cap; nothing was trimmed and no call was made'},
            indent=1) + '\n')
        raise SystemExit('STOP: planned %d new calls > cap %d — %s written, 0 calls made'
                         % (len(need), min(PLAN_CAP, args.max_calls), STOP_PLAN))

    made = {'ok': 0, 'bad': 0}
    if need:
        keys = load_keys()
        key = keys[0]

        def work(h):
            row = call_one(req[h], key)
            made['ok' if row.get('http') == 200 else 'bad'] += 1
            return row
        todo = list(need)
        random.Random(1).shuffle(todo)
        with ThreadPoolExecutor(max_workers=6) as pool:
            for _ in pool.map(work, todo):
                pass
        print('[FRESH] calls made: http200 %d  transport-dead %d' % (made['ok'], made['bad']))
        rep, ver, failed, counted_l = ledger_state()

    # ---------------- score both variants (each rebuilds its own checker state)
    labels, _kr, _v = R1K.judge_labels('fresh', purpose)
    cols, keep = {}, {}
    for tag, hm, side_st in (('before', hm_b, 'before'), ('after', hm_a, 'after')):
        st, recs, ann, by, info = build_side('fresh', tag == 'after', purpose)
        for r in recs:
            if r['item_id'] in labels:
                r['judged'], r['wrong_type'] = labels[r['item_id']]
        hmx = hashes_for(st, recs, l3_ids(st, sel['locktip']), sel['prompt'])
        vm = {i: ver[h] for i, h in hmx.items() if h in ver}
        guards = R1K.guard_readouts(recs, ann, sel['f9_strict'])
        res = R1K.configure_row(st, recs, vm, sel['locktip'], guards, sel['f8'], sel['f9'],
                                sel['tip_reject'])
        RES_VM[0] = vm
        cols['all_600_%s_hygiene' % tag] = col_metrics(recs, res, labels)
        cols['excl_%d_%s_hygiene' % (EXCLUDE_SID, tag)] = col_metrics(recs, res, labels,
                                                                      drop_sid=EXCLUDE_SID)
        keep[tag] = {'st': st, 'recs': recs, 'ann': ann, 'by': by, 'res': res, 'guards': guards,
                     'vm': vm, 'info': info, 'hm': hmx,
                     'no_verdict': sorted(i for i in hmx if i not in vm)}

    K = keep['after']
    RES_VM[0] = K['vm']
    sec5 = section5('fresh', K['st'], K['recs'], K['ann'], K['by'], K['res'], K['guards'], labels,
                    sel, lock_rej_a, info_b, K['info'])
    f9v = f9_fresh_validation(purpose)

    lab = {i: labels.get(i, (K['by'][i]['judged'], K['by'][i]['wrong_type'])) for i in K['by']}
    cells = {}
    for nm, intent in (('ACTIVE->PASSIVE (intent V)', 'V'), ('TIME-FRAME-SHIFT (intent TF)', 'TF')):
        ids = [i for i in K['by'] if K['by'][i].get('intent') == intent and lab[i][0] == 'wrong']
        acc = [i for i in ids if K['res'][i]['accepted']]
        cells[nm] = {'judged_wrong': len(ids), 'accepted': len(acc), 'rate': P.rate(len(acc), len(ids)),
                     'rejecting_layers': dict(collections.Counter(
                         str(K['res'][i]['layer']) for i in ids if not K['res'][i]['accepted'])),
                     'accepted_ids': sorted(acc)}

    out = {'phase': '1L', 'side': 'fresh', 'freeze_commit': fh, 'frozen_config': cfg['selected'],
           'preflight': {'lock_rejections_BASE_before': len(lock_rej_b),
                         'lock_rejections_BASE_after': len(lock_rej_a),
                         'l3_eligible_before': len(l3_b), 'l3_eligible_after': len(l3_a)},
           'builder_2_1': {'before': info_b.get('chk_computed'),
                           'after': K['info'].get('chk_computed')},
           'columns': cols, 'cells': cells, 'section5': sec5,
           'f9_out_of_sample_validation': f9v,
           'no_verdict_items': {t: keep[t]['no_verdict'] for t in keep},
           'calls': dict(token_spend(), planned_new=len(need), made=made,
                         reused=len(req) - len(need), unique_requests=len(req))}
    json.dump(out, open(os.path.join(HERE, 'results_fresh.json'), 'w'), indent=1, ensure_ascii=False)

    # ---------------- markdown
    order = ['all_600_after_hygiene', 'excl_%d_after_hygiene' % EXCLUDE_SID,
             'all_600_before_hygiene', 'excl_%d_before_hygiene' % EXCLUDE_SID]
    head = ['(a) all 600, after hygiene', '(b) excl. sid %d, after hygiene' % EXCLUDE_SID,
            '(c) all 600, BEFORE hygiene', '(d) excl. sid %d, before hygiene' % EXCLUDE_SID]
    T = ['# Phase 1L — FRESH results (the one measurement of the frozen Phase 1k configuration)', '',
         'Freeze commit `%s`. Frozen config: **%s / %s / TIP-as-rejection %s** (F8 %s, F9 %s, '
         'REPORTED_STRICT %s). Every figure is numerator/denominator, point, exact 95 %% '
         'Clopper-Pearson interval. Columns are never averaged.'
         % (fh, sel['name'], sel['prompt'], 'on' if sel['tip_reject'] else 'off', sel['f8'],
            sel['f9'], sel['f9_strict']), '',
         '| metric | %s |' % ' | '.join(head), '|---|---|---|---|---|']
    rows = [('coverage', lambda m: _r(m['coverage'])),
            ('coverage (kind C)', lambda m: _r(m['coverage_kindC'])),
            ('FA', lambda m: _r(m['fa']))]
    for t in TYPES:
        rows.append(('FA type %s' % t, (lambda t: lambda m: _r(m['fa_by_type'][t]))(t)))
    for nm, fn in rows:
        T.append('| %s | %s |' % (nm, ' | '.join(fn(cols[c]) for c in order)))
    T += ['', '## FA by layer (denominator = all items judged wrong)', '']
    for c, h in zip(order, head):
        T += ['**%s**' % h, '', '```', json.dumps({k: _r(v) for k, v in cols[c]['fa_by_layer'].items()},
                                                  indent=1), '```', '']
    T += ['## False rejections by layer (denominator = all items judged correct)', '']
    for c, h in zip(order, head):
        T += ['**%s**' % h, '', '```', json.dumps({k: _r(v) for k, v in cols[c]['fr_by_layer'].items()},
                                                  indent=1), '```', '']
    T += ['## The two named cells', '', '```', json.dumps(cells, indent=1, ensure_ascii=False), '```',
          '', '## Targets — per column, on the point and on the interval (never averaged)', '',
          '| target | %s |' % ' | '.join(head), '|---|---|---|---|---|']
    for tgt in ('coverage >= 90%', 'FA < 5%', 'type-T FA < 5%'):
        T.append('| %s | %s |' % (tgt, ' | '.join(
            'point %s / interval %s' % ('MET' if cols[c]['targets'][tgt]['point'] else 'not met',
                                        'MET' if cols[c]['targets'][tgt]['interval'] else 'not met')
            for c in order)))
    T += ['', '## §5 accounting', '', '```',
          json.dumps(sec5, indent=1, ensure_ascii=False)[:60000], '```', '',
          '## F9 hand-check on the 70 fresh sentences (against the stored tf_gold)', '', '```',
          json.dumps({k: v for k, v in f9v.items() if k != 'rows'}, indent=1, ensure_ascii=False),
          '```', '', '## Model calls', '', '```', json.dumps(out['calls'], indent=1), '```', '',
          '## Preflight', '', '```', json.dumps(out['preflight'], indent=1), '```', '']
    open(os.path.join(HERE, 'results_fresh.md'), 'w', encoding='utf-8').write('\n'.join(T) + '\n')

    with open(os.path.join(HERE, 'F9_REVALIDATION_1L.md'), 'a', encoding='utf-8') as fh2:
        fh2.write('\n\n## Out-of-sample: the 70 FRESH sentences vs the stored `tf_gold` '
                  '(Phase 1L final run)\n\n')
        fh2.write('agree %d / conservative %d / error %d of %d — error rate %s\n\n'
                  % (f9v['agree'], f9v['conservative'], f9v['error'], f9v['n'],
                     _r(f9v['error_rate'])))
        if f9v['errors']:
            for e in f9v['errors']:
                fh2.write('- `%s`\n' % json.dumps(e, ensure_ascii=False))
        else:
            fh2.write('No errors: F9 never named a time frame the hand-check contradicts.\n')

    for c, h in zip(order, head):
        m = cols[c]
        print('%s  coverage %s  FA %s  FA T %s' % (h, _r(m['coverage']), _r(m['fa']),
                                                   _r(m['fa_by_type']['T'])))
    print('calls %s' % json.dumps(out['calls']))
    open(DONE, 'w', encoding='utf-8').write(json.dumps(
        {'freeze_commit': fh, 'coverage': cols[order[0]]['coverage'], 'fa': cols[order[0]]['fa']}) + '\n')
    print('FINAL_RUN_DONE written — the fresh side is closed.')
    return out


_F9_OLD = None


def main():
    global _F9_OLD
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=('dev', 'fresh'))
    ap.add_argument('--max-calls', type=int, default=PLAN_CAP)
    a = ap.parse_args()
    sys.path.insert(0, os.path.join(P1K, 'taskB'))
    import importlib.util
    spec = importlib.util.spec_from_file_location('f9_1k', os.path.join(P1K, 'taskB', 'f9.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    _F9_OLD = mod
    if a.mode == 'dev':
        run_dev(a)
    else:
        run_fresh(a)


if __name__ == '__main__':
    main()
