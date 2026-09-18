#!/usr/bin/env python3
"""Phase 1j agent R — the DEV runner for every arm (BASE, A, B, A+B, C) and the shared library
that `phase1j/run_final.py` reuses for the one holdout run.

    PYTHONDONTWRITEBYTECODE=1 python3 runner_1j.py --plan          # budget plan, ZERO calls
    PYTHONDONTWRITEBYTECODE=1 python3 runner_1j.py --run           # make the missing calls, then score
    PYTHONDONTWRITEBYTECODE=1 python3 runner_1j.py --score         # score from the ledger only, 0 calls

Model is decided: gemini-3.1-flash-lite, temperature 0, thinkingBudget 0.
The API key is read only inside pipeline_1i.load_key(), never printed and never put on a command line.
Every counted call goes through the ONE shared ledger phase1j/ledger.jsonl (HTTP 200 = counted).
"""
import argparse
import collections
import copy
import hashlib
import importlib
import json
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))            # phase1j/taskC
P1J = os.path.dirname(HERE)
TOFF = os.path.dirname(P1J)
P1I = os.path.join(TOFF, 'phase1i')
for _p in (P1I, os.path.join(P1I, 'taskB'), os.path.join(P1I, 'taskC'), P1J,
           os.path.join(P1J, 'taskA')):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import pipeline_1i as P                                                      # noqa: E402
import p_chain as PC                                                         # noqa: E402
import guards_c as G                                                         # noqa: E402
from loader_1j import load_items, load_annotations                           # noqa: E402

LEDGER = os.path.join(P1J, 'ledger.jsonl')
TASKB = os.path.join(P1J, 'taskB')
TASKD = os.path.join(P1J, 'taskD')
CAP_TOTAL = 1400
RESERVE_FINAL = 330
CAP_DEV = CAP_TOTAL - RESERVE_FINAL                      # 1070
PRICE_IN, PRICE_OUT = 0.25 / 1e6, 1.50 / 1e6

# ------------------------------------------------------------------ the TAG CONTRACT (arm C)
TAG_SYS = (
    'You check English translations of Slovak. Reply with TAGS ONLY, no prose, no explanation, at most '
    '8 tokens. Use one or more of these tags, separated by a space: '
    'OK | MISS:<word> | ADD:<word> | SWAP:<answer>~<reference> | SUBJ:<answer>~<expected>. '
    'OK = the learner sentence means the same as the Slovak and is correct English. '
    'MISS:<word> = something the Slovak says is missing from the learner sentence. '
    'ADD:<word> = the learner sentence adds information the Slovak does not have. '
    'SWAP:<a>~<b> = the learner wrote <a> where the Slovak means <b> (a different thing, person, place, '
    'time, quantity or time reference). '
    'SUBJ:<a>~<b> = the learner subject is <a> but the Slovak subject is <b>. '
    'If nothing is wrong, reply exactly OK.')
TAG_TAIL = 'Tags?'
TAG_CFG = {'temperature': 0, 'maxOutputTokens': 32, 'thinkingConfig': {'thinkingBudget': 0}}
TAG_RE = re.compile(r'\b(OK|MISS|ADD|SWAP|SUBJ)\b(?::([^\s]+))?')

ARMS = {
    # name           data     p_prompt f4p    contract labels
    'BASE': dict(data='orig', p_prompt=False, f4p=False, contract=False, labels='orig'),
    'A': dict(data='orig', p_prompt=True, f4p=True, contract=False, labels='orig'),
    'A:f4p-only': dict(data='orig', p_prompt=False, f4p=True, contract=False, labels='orig'),
    'A:p_prompt-only': dict(data='orig', p_prompt=True, f4p=False, contract=False, labels='orig'),
    'B': dict(data='b', p_prompt=False, f4p=False, contract=False, labels='b'),
    'A+B': dict(data='b', p_prompt=True, f4p=True, contract=False, labels='b'),
    'C': dict(data='b', p_prompt=True, f4p=True, contract=True, labels='b'),
}
ARM_ORDER = ['BASE', 'A', 'A:f4p-only', 'A:p_prompt-only', 'B', 'A+B', 'C']
VARIANT_OF = {'BASE': 'P-E4b', 'A': 'J-A', 'A:f4p-only': 'P-E4b', 'A:p_prompt-only': 'J-A',
              'B': 'J-B', 'A+B': 'J-AB', 'C': 'J-C'}


# ================================================================== data
def parse_tags(txt):
    return [(m.group(1), m.group(2) or '') for m in TAG_RE.finditer(txt or '')]


def req_hash(sysx, user, gcfg):
    blob = json.dumps([sysx, user, gcfg], sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(blob.encode('utf-8')).hexdigest()[:32]


def load_side(side, purpose):
    recs = load_items(side, purpose=purpose)
    ann = load_annotations(side, purpose=purpose)
    ann_b = json.load(open(os.path.join(TASKB, 'annotations_b_%s.json' % side), encoding='utf-8'))
    sk_new = json.load(open(os.path.join(TASKB, 'sk_new.json'), encoding='utf-8'))
    rew = {}
    for ln in open(os.path.join(TASKB, 'rewrites.jsonl'), encoding='utf-8'):
        if ln.strip():
            r = json.loads(ln)
            rew[str(r['sid'])] = r
    return recs, ann, ann_b, sk_new, rew


def b_recs(recs, sk_new, rew):
    """Task B data: new Slovak + aligned refs (README_B §'which fields')."""
    out = copy.deepcopy(recs)
    for r in out:
        s = str(r['sid'])
        if s in sk_new:
            r['sk'] = sk_new[s]
            if rew.get(s, {}).get('refs_new'):
                r['refs'] = list(rew[s]['refs_new'])
    return out


def build_pmap(recs, ann, rew, use_fallback):
    """sid(str) -> p | None; also stores it on the annotation entry so f4p / p_of see it."""
    sk_of = {}
    for r in recs:
        sk_of[str(r['sid'])] = r['sk']
    pm, nfall = {}, 0
    for sid, sk in sk_of.items():
        try:
            p = PC.derive_p(sk, ann.get(sid))
        except Exception:
            p = None
        if p is None and use_fallback and rew.get(sid, {}).get('status') == 'rewritten':
            rw = rew[sid]
            per = rw['person'][0] if rw.get('person') else None
            num = rw['number'][0] if rw.get('number') else None
            if per or num:
                p = {'person': per, 'number': num, 'gender': None, 'subject': 'explicit',
                     'en_subjects': [], 'signals': ['taskB_inserted_pronoun'], 'has_g': False,
                     'evidence': 'inserted pronoun "%s" (Task B rewrite) -> person %s, number %s'
                                 % (rw['pronoun'][0] if rw.get('pronoun') else '?', per, num),
                     'from_taskB_pronoun': True}
                try:
                    p['en_subjects'] = PC.licensed_subjects(p)
                except Exception:
                    pass
                nfall += 1
        pm[sid] = p
        if sid in ann:
            ann[sid]['p_chain'] = p
    return pm, nfall


_PMAP_ACTIVE = {}


def _f4p(it):
    sid = str(it.get('sid') or it.get('exercise_id'))
    p = _PMAP_ACTIVE.get(sid)
    if not p:
        return False, 'no p'
    ann = {'p_chain': p, 'hygienised': {}}
    try:
        return PC.f4p_subject_mismatch(dict(it, sk=it.get('sk'), sid=sid), ann)
    except Exception as e:
        return False, 'f4p error %s' % type(e).__name__


import checker_1i as _C                                                    # noqa: E402
# snapshot the PRISTINE checker callables before any Task B / Task C patch is applied; restoring them
# before each arm undoes every monkeypatch (reload() cannot be used: checker_1i.prompt would self-wrap).
_PRISTINE = {k: v for k, v in _C.__dict__.items() if callable(v)}


def make_state(recs, ann, guards, side_tag):
    C = _C
    C.__dict__.update(_PRISTINE)
    C._ANN.clear()
    C.SK_OF.clear()
    for s, a in ann.items():
        C._ANN[int(s)] = a.get('hygienised', a)
    for r in recs:
        C.SK_OF[r['sid']] = r['sk']
    P._ST = {'C': C, 'recs': recs, 'ann': ann, 'side': side_tag, 'base_decide': C.decide,
             'decide': C.decide, 'b_fix': False, 'guards': (), 'reports': {}}
    return P.configure(b_fix=True, guards=tuple(guards), side=side_tag)


def prep_arm(arm_name, side, data):
    """-> (st, recs, pmap). Sets the module-global pmap the f4p guard reads."""
    global _PMAP_ACTIVE
    a = ARMS[arm_name]
    recs, ann, ann_b, sk_new, rew = data
    if a['data'] == 'b':
        rr = b_recs(recs, sk_new, rew)
        an = copy.deepcopy(ann_b)
        pm, _ = build_pmap(rr, an, rew, use_fallback=True)
    else:
        rr = copy.deepcopy(recs)
        an = copy.deepcopy(ann)
        pm, _ = build_pmap(rr, an, rew, use_fallback=False)
    _PMAP_ACTIVE = pm
    st = make_state(rr, an, ('F4v3',), side_tag='%s1j' % side)
    if a['f4p']:
        # f4p is applied as its own wrapper, not through guards_c.GUARDS: guards_c.decide carries a
        # hard-coded reason table and raises KeyError on an unknown guard name. Same semantics as a
        # Task C guard — it can only turn an acceptance into a rejection. `pm` is bound per arm.
        def dec(it, flags, vm, _base=st['decide'], _pm=pm):
            d = _base(it, flags, vm)
            if d.get('accepted'):
                sid = str(it.get('sid') or it.get('exercise_id'))
                p = _pm.get(sid)
                if p:
                    try:
                        hit, trace = PC.f4p_subject_mismatch(dict(it, sid=sid),
                                                             {'p_chain': p, 'hygienised': {}})
                    except Exception as e:
                        hit, trace = False, 'f4p error %s' % type(e).__name__
                    if hit:
                        d = dict(d, accepted=False, layer='f4p', verdict='rejected', why=trace)
            return d
        st['decide'] = dec
    return st, rr, pm


# ================================================================== prompts
def build_request(st, r, arm_name, pm):
    """(system, user, generationConfig, hash) for one item under one arm."""
    a = ARMS[arm_name]
    it = P.to_item(r)
    lines = P.pb_lines(st, it)
    head, tail = lines[:-1], lines[-1]
    g = P.gender_chain(st, r['sid'])
    gline = P.GENDER_TMPL.format(words=', '.join('"%s"' % w for w in g)) if g else None
    pline = ''
    if a['p_prompt']:
        p = pm.get(str(r['sid']))
        if p:
            try:
                pline = PC.p_prompt_line(p) or ''
            except Exception:
                pline = ''
    extra = ([gline] if gline else []) + ([pline] if pline else []) + [P.GROUND_LINE, P.WORDING_LINE]
    if a['contract']:
        tail = TAG_TAIL
        sysx, gcfg = TAG_SYS, TAG_CFG
    else:
        sysx, gcfg = P.sys_text(st, 'P-E4b'), P.GEN_CFG
    user = '\n'.join(head + extra + [tail])
    return sysx, user, gcfg, req_hash(sysx, user, gcfg)


# ================================================================== ledger
def ledger_rows(path=LEDGER):
    if not os.path.exists(path):
        return []
    out = []
    for ln in open(path, encoding='utf-8'):
        ln = ln.strip()
        if not ln:
            continue
        try:
            out.append(json.loads(ln))
        except Exception:
            pass
    return out


def ledger_state(path=LEDGER):
    """(replies {hash: reply}, verdicts {hash: verdict}, counted, failed, retries)"""
    rep, ver, counted, failed, retries = {}, {}, 0, set(), 0
    for row in ledger_rows(path):
        if row.get('http') != 200:
            retries += 1
            continue
        counted += 1
        h = row.get('req_hash')
        if not h:
            continue
        rep[h] = row.get('reply', '')
        v = row.get('verdict')
        if v == 'PARSE_FAIL':
            failed.add(h)
            ver.pop(h, None)
        else:
            ver[h] = v
            failed.discard(h)
    return rep, ver, counted, failed, retries


def phase1i_reuse(st, recs, pm):
    """{hash of the canonical P-E4b request: verdict} from the two frozen Phase 1i ledgers."""
    have = {}
    for p in (os.path.join(P1I, 'taskE', 'calls.jsonl'),
              os.path.join(P1I, 'taskF', 'holdout_calls.jsonl'),
              os.path.join(P1I, 'taskF', 'dev_calls.jsonl')):
        if not os.path.exists(p):
            continue
        h, _f, _r = P.ledger_verdicts(p)
        for (v, i), val in h.items():
            if v == 'P-E4b':
                have[i] = val
    out = {}
    for r in recs:
        if r['item_id'] in have:
            _s, _u, _g, hh = build_request(st, r, 'BASE', pm)
            out[hh] = have[r['item_id']]
    return out


def call_one(req, key, tries=5):
    sysx, user, gcfg, h, variant, item_id = req
    body = {'systemInstruction': {'parts': [{'text': sysx}]},
            'contents': [{'role': 'user', 'parts': [{'text': user}]}],
            'generationConfig': gcfg}
    url = P.API % P.MODEL
    delay = 1.0
    row = None
    for attempt in range(1, tries + 1):
        t0 = time.time()
        code, js, raw = P._http(url, body, key)
        lat = int((time.time() - t0) * 1000)
        if code == 200:
            cands = (js or {}).get('candidates') or []
            txt = ''.join(pp.get('text', '') or '' for c in cands
                          for pp in ((c.get('content') or {}).get('parts') or []))
            finish = cands[0].get('finishReason') if cands else None
            empty = (not cands) or txt.strip() == ''
            if variant == 'J-C':
                v = 'TAGS' if parse_tags(txt) else 'PARSE_FAIL'
            else:
                v = P.parse_reply(txt, 'P-E4b') or 'PARSE_FAIL'
            um = (js or {}).get('usageMetadata') or {}
            row = {'ts': time.time(), 'model': P.MODEL, 'variant': variant, 'item_id': item_id,
                   'req_hash': h, 'http': 200, 'counted': True, 'verdict': v, 'reply': txt,
                   'finish': finish, 'empty': empty, 'latency_ms': lat, 'try': attempt,
                   'prompt_tokens': um.get('promptTokenCount'),
                   'candidates_tokens': um.get('candidatesTokenCount'),
                   'thoughts_tokens': um.get('thoughtsTokenCount'),
                   'cached_tokens': um.get('cachedContentTokenCount'),
                   'thinking': '{"thinkingBudget": 0}', 'max_output': gcfg['maxOutputTokens']}
            P.ledger_append(LEDGER, row)
            return row
        row = {'ts': time.time(), 'model': P.MODEL, 'variant': variant, 'item_id': item_id,
               'req_hash': h, 'http': code, 'counted': False, 'verdict': None, 'reply': '',
               'finish': None, 'empty': None, 'latency_ms': lat, 'try': attempt,
               'error': P._redact(raw or js, key), 'transport_retry': True}
        P.ledger_append(LEDGER, row)
        if attempt == tries:
            return row
        time.sleep(delay * (1.0 + random.random() * 0.3))
        delay = min(delay * 2, 16.0)
    return row


# ================================================================== labels
def judge_data():
    km = json.load(open(os.path.join(TASKB, 'judge_keymap.json'), encoding='utf-8'))
    ju = {}
    for i in (1, 2, 3):
        p = os.path.join(TASKB, 'judge_output_part%d.jsonl' % i)
        for ln in open(p, encoding='utf-8'):
            if ln.strip():
                j = json.loads(ln)
                ju[j['k']] = j
    return km, ju


def label_sets(recs, side):
    """-> primary {id:(label,type)}, sensitivity {id:(label,type)}, relabel report dict."""
    km, ju = judge_data()
    orig = {r['item_id']: (r['judged'], r['wrong_type']) for r in recs}
    prim, sens = dict(orig), dict(orig)
    cnt = {'dev': collections.Counter(), 'both': collections.Counter()}
    ctrl = {'dev': collections.Counter(), 'both': collections.Counter()}
    examples = []
    for k, meta in km.items():
        j = ju.get(k)
        if not j:
            continue
        sc = ['both'] + (['dev'] if meta['side'] == 'dev' else [])
        old_l, old_t = meta['old_label'], meta['old_type']
        new_l, new_t = j['label'], j.get('type')
        subj_ok = j.get('subj_ok')
        if meta.get('control'):
            for s in sc:
                ctrl[s]['n'] += 1
                if old_l == 'correct' and new_l == 'wrong':
                    ctrl[s]['correct_to_wrong'] += 1
                elif old_l == 'wrong' and new_l == 'correct':
                    ctrl[s]['wrong_to_correct'] += 1
                elif old_l == new_l:
                    ctrl[s]['agree'] += 1
            continue
        for s in sc:
            cnt[s]['n_rejudged'] += 1
            if old_l == 'correct' and new_l == 'wrong':
                cnt[s]['correct_to_wrong_subject' if subj_ok is False
                       else 'correct_to_wrong_other'] += 1
            elif old_l == 'wrong' and new_l == 'correct':
                cnt[s]['wrong_to_correct'] += 1
            elif old_l == 'wrong' and new_l == 'wrong' and old_t != new_t:
                cnt[s]['wrong_to_wrong_type_change'] += 1
            else:
                cnt[s]['unchanged'] += 1
        iid = meta['item_id']
        if iid in prim:
            if new_l == 'wrong' and subj_ok is False:
                prim[iid] = ('wrong', 'S')
                if old_l == 'correct' and len(examples) < 40:
                    examples.append({'id': iid, 'old': old_l, 'note': j.get('note', '')})
            sens[iid] = ('wrong', new_t) if new_l == 'wrong' else ('correct', None)
    rep = {'dev': dict(cnt['dev']), 'both_sides': dict(cnt['both']),
           'control_dev': dict(ctrl['dev']), 'control_both': dict(ctrl['both']),
           'primary_overrides_dev': sum(1 for i in prim if i in orig and prim[i] != orig[i]),
           'sensitivity_overrides_dev': sum(1 for i in sens if i in orig and sens[i] != orig[i]),
           'primary_override_examples': examples[:10]}
    nc = ctrl['both']['n'] or 1
    rep['control_noise'] = {
        'n': ctrl['both']['n'],
        'correct_to_wrong': P.rate(ctrl['both']['correct_to_wrong'], ctrl['both']['n']),
        'wrong_to_correct': P.rate(ctrl['both']['wrong_to_correct'], ctrl['both']['n']),
        'any_flip': P.rate(ctrl['both']['correct_to_wrong'] + ctrl['both']['wrong_to_correct'],
                           ctrl['both']['n'])}
    return prim, sens, rep


def relabel(recs, labels):
    out = copy.deepcopy(recs)
    for r in out:
        l, t = labels.get(r['item_id'], (r['judged'], r['wrong_type']))
        r['judged'] = l
        r['wrong_type'] = t if l == 'wrong' else None
    return out


# ================================================================== scoring
def score(recs_labeled, res):
    return P.metrics({'recs': recs_labeled}, res)


def arm_verdict_map(arm_name, hashes, rep, ver, switch_on):
    """{item_id: SAME|TIP|DIFF}. For arm C the tag table is applied here (zero calls)."""
    vm, tags_of = {}, {}
    contract = ARMS[arm_name]['contract']
    for iid, h in hashes.items():
        if contract:
            if h not in rep:
                continue
            tg = parse_tags(rep[h])
            tags_of[iid] = tg
            if not tg:
                continue                       # PARSE_FAIL -> no verdict -> scored rejected
            names = {t for t, _ in tg}
            if names & {'SUBJ', 'SWAP', 'ADD'}:
                vm[iid] = 'DIFF'
            elif 'MISS' in names:
                vm[iid] = 'DIFF' if switch_on else 'SAME'
            elif 'OK' in names:
                vm[iid] = 'SAME'
        elif h in ver:
            vm[iid] = ver[h]
    return vm, tags_of


# ================================================================== main
def build_all(side, data, purpose_tag):
    """-> {arm: {'st','recs','pm','l3','hashes','req'}} — zero calls."""
    out = {}
    base_st = base_recs = base_pm = None
    for name in ARM_ORDER:
        st, rr, pm = prep_arm(name, side, data)
        l3 = sorted(i for i, v in P.run_pipeline(st, {}).items() if v['reached_l3'])
        by_id = {r['item_id']: r for r in rr}
        hashes, req = {}, {}
        for i in l3:
            s, u, g, h = build_request(st, by_id[i], name, pm)
            hashes[i] = h
            req[h] = (s, u, g, h, VARIANT_OF[name], i)
        out[name] = {'st': st, 'recs': rr, 'pm': pm, 'l3': l3, 'hashes': hashes, 'req': req,
                     'by_id': by_id}
        if name == 'BASE':
            base_st, base_recs, base_pm = st, rr, pm
    out['_reuse'] = phase1i_reuse(base_st, base_recs, base_pm)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--plan', action='store_true')
    ap.add_argument('--run', action='store_true')
    ap.add_argument('--score', action='store_true')
    ap.add_argument('--workers', type=int, default=6)
    a = ap.parse_args()
    os.makedirs(TASKD, exist_ok=True)
    side = 'dev'
    purpose = 'Phase 1j agent R: DEV measurement of arms BASE/A/B/A+B/C'
    data = load_side(side, purpose)
    recs0 = data[0]
    prim, sens, rel = label_sets(recs0, side)
    ALL = build_all(side, data, purpose)
    reuse_1i = ALL['_reuse']
    rep, ver, counted, failed_h, retries = ledger_state()
    ver = dict(ver)
    ver.update({h: v for h, v in reuse_1i.items() if h not in ver})
    rep = dict(rep)

    # ---- budget plan (dedupe byte-identical prompts across arms)
    known = set(ver) | set(rep) | set(failed_h)
    plan, todo_h, seen = {}, [], set()
    for name in ARM_ORDER:
        req = ALL[name]['req']
        new = [h for h in req if h not in known and h not in seen]
        plan[name] = {'l3': len(ALL[name]['l3']), 'unique_prompts': len(req),
                      'already_have': sum(1 for h in req if h in known),
                      'new_after_dedupe': len(new)}
        for h in new:
            seen.add(h)
            todo_h.append(h)
    subsample_note = 'none'
    if len(todo_h) > CAP_DEV - counted:
        keep = CAP_DEV - counted
        c_new = [h for h in ALL['C']['req'] if h in set(todo_h)]
        other = [h for h in todo_h if h not in set(c_new)]
        room = keep - len(other)
        sids = sorted({ALL['C']['by_id'][ALL['C']['req'][h][5]]['sid'] for h in c_new})
        random.Random(1).shuffle(sids)
        chosen, cur = set(), 0
        per_sid = collections.defaultdict(list)
        for h in c_new:
            per_sid[ALL['C']['by_id'][ALL['C']['req'][h][5]]['sid']].append(h)
        for s in sids:
            if cur + len(per_sid[s]) > room:
                continue
            chosen.add(s)
            cur += len(per_sid[s])
        todo_h = other + [h for s in chosen for h in per_sid[s]]
        subsample_note = ('arm C cut to a random by-SENTENCE subsample (seed 1): %d of %d DEV sentences, '
                          '%d of %d new calls' % (len(chosen), len(sids), cur, len(c_new)))
    print('== BUDGET PLAN (dedupe + reuse) ==')
    for name in ARM_ORDER:
        print('  %-16s L3 %3d  unique %3d  have %3d  NEW %3d'
              % (name, plan[name]['l3'], plan[name]['unique_prompts'],
                 plan[name]['already_have'], plan[name]['new_after_dedupe']))
    print('  reused from phase1i ledgers: %d hashes' % len(reuse_1i))
    print('  ledger counted so far: %d   NEW planned: %d   DEV cap %d   total cap %d (reserve %d)'
          % (counted, len(todo_h), CAP_DEV, CAP_TOTAL, RESERVE_FINAL))
    print('  subsample: %s' % subsample_note)
    if a.plan:
        json.dump({'plan': plan, 'new_total': len(todo_h), 'counted_before': counted,
                   'subsample': subsample_note, 'relabel': rel},
                  open(os.path.join(TASKD, 'budget_plan.json'), 'w'), indent=1, ensure_ascii=False)
        return

    # ---- calls
    made = {'ok': 0, 'bad': 0}
    if a.run and todo_h:
        if counted + len(todo_h) > CAP_DEV:
            raise SystemExit('REFUSED: %d + %d > DEV cap %d' % (counted, len(todo_h), CAP_DEV))
        allreq = {}
        for name in ARM_ORDER:
            allreq.update(ALL[name]['req'])
        todo = [allreq[h] for h in todo_h]
        random.Random(1).shuffle(todo)
        key = P.load_key()

        def work(rq):
            row = call_one(rq, key)
            if row.get('http') == 200:
                made['ok'] += 1
            else:
                made['bad'] += 1
            return row

        with ThreadPoolExecutor(max_workers=a.workers) as pool:
            for _ in pool.map(work, todo):
                pass
        print('calls made: http200 %d  transport-dead %d' % (made['ok'], made['bad']))
        rep, ver, counted, failed_h, retries = ledger_state()
        ver = dict(ver)
        ver.update({h: v for h, v in reuse_1i.items() if h not in ver})

    # ---- score everything
    rows, details = [], {}
    labelsets = {'primary': prim, 'sensitivity': sens}
    for name in ARM_ORDER:
        A = ALL[name]
        for switch in (True, False):
            if name in ('BASE',) and switch is False:
                pass
            vm, tags_of = arm_verdict_map(name, A['hashes'], rep, ver, switch)
            if ARMS[name]['contract']:
                res = P.run_pipeline(A['st'], vm, tip_reject=False)
            else:
                res = P.run_pipeline(A['st'], vm, tip_reject=switch)
            nofail = [i for i in A['l3'] if i not in vm]
            entry = {'arm': name, 'switch': 'on' if switch else 'off',
                     'l3': len(A['l3']), 'no_verdict': len(nofail),
                     'no_verdict_ids': nofail[:20], 'model_calls_unique': len(A['req'])}
            for lname, lab in labelsets.items():
                use = lab if ARMS[name]['labels'] == 'b' else \
                    {r['item_id']: (r['judged'], r['wrong_type']) for r in recs0}
                m = score(relabel(A['recs'], use), res)
                entry[lname] = {'coverage': m['coverage'], 'fa': m['fa'],
                                'fa_by_type': m['fa_by_type'], 'fa_by_layer': m['fa_by_layer'],
                                'fa_items': m['fa_items'], 'fr_by_layer': m['fr_by_layer'],
                                'false_rejections': m['false_rejections']}
            rows.append(entry)
            details[(name, switch)] = {'res': res, 'vm': vm, 'tags': tags_of}
    json.dump({'rows': rows}, open(os.path.join(TASKD, '_rows_raw.json'), 'w'), indent=1,
              ensure_ascii=False)
    return {'ALL': ALL, 'rows': rows, 'details': details, 'rel': rel, 'prim': prim, 'sens': sens,
            'recs0': recs0, 'plan': plan, 'counted': counted, 'made': made,
            'subsample': subsample_note, 'reuse_1i': reuse_1i, 'rep': rep, 'ver': ver,
            'failed_h': failed_h, 'retries': retries}


def _r(d):
    return '%d/%d = %.2f%% [%.2f, %.2f]' % (d['k'], d['n'], d['pct'] or 0.0, d['ci'][0], d['ci'][1])


def _row_of(rows, arm, switch):
    for e in rows:
        if e['arm'] == arm and e['switch'] == ('on' if switch else 'off'):
            return e
    return None


EXPECTED_TAG = {'correct': {'OK'}, 'M': {'MISS', 'ADD'}, 'W': {'SWAP'}, 'S': {'SUBJ'}}


def tag_accuracy(R):
    """Tag-level accuracy of the TAG CONTRACT on the DEV items that reached the model."""
    ALL, prim = R['ALL'], R['prim']
    A = ALL['C']
    rep = R['rep']
    by_id = A['by_id']
    conf_first, conf_set = collections.Counter(), collections.Counter()
    per_class = collections.defaultdict(lambda: [0, 0])
    tdist = collections.Counter()
    unparsable, mismatches, n_reached = 0, [], 0
    for iid in A['l3']:
        h = A['hashes'][iid]
        if h not in rep:
            continue
        n_reached += 1
        tags = parse_tags(rep[h])
        names = [t for t, _ in tags]
        if not tags:
            unparsable += 1
        lab, typ = prim.get(iid, (by_id[iid]['judged'], by_id[iid]['wrong_type']))
        cls = 'correct' if lab == 'correct' else typ
        first = names[0] if names else 'UNPARSABLE'
        nameset = '+'.join(sorted(set(names))) or 'UNPARSABLE'
        if cls == 'T':
            tdist[nameset] += 1
            conf_first[('T', first)] += 1
            conf_set[('T', nameset)] += 1
            continue
        exp = EXPECTED_TAG.get(cls)
        if exp is None:
            continue
        conf_first[(cls, first)] += 1
        conf_set[(cls, nameset)] += 1
        ok = bool(names) and names[0] in exp
        per_class[cls][1] += 1
        per_class[cls][0] += int(ok)
        if not ok and len(mismatches) < 10:
            r = by_id[iid]
            mismatches.append({'id': iid, 'class': cls, 'expected': sorted(exp),
                               'returned': rep[h].strip()[:80], 'sk': r['sk'],
                               'reference': r['reference'], 'answer': r['answer']})
    tot = [sum(v[0] for v in per_class.values()), sum(v[1] for v in per_class.values())]
    return {'n_reached_model': n_reached, 'unparsable': unparsable,
            'overall': P.rate(tot[0], tot[1]),
            'per_class': {c: P.rate(v[0], v[1]) for c, v in per_class.items()},
            'confusion_first': {'%s|%s' % k: v for k, v in sorted(conf_first.items())},
            'confusion_set': {'%s|%s' % k: v for k, v in sorted(conf_set.items())},
            'type_T_tags': dict(tdist), 'mismatch_examples': mismatches}


def token_spend():
    tin = tout = n200 = nfail = nretry = 0
    for row in ledger_rows():
        if row.get('http') != 200:
            nretry += 1
            continue
        n200 += 1
        tin += row.get('prompt_tokens') or 0
        tout += (row.get('candidates_tokens') or 0) + (row.get('thoughts_tokens') or 0)
        if row.get('verdict') == 'PARSE_FAIL':
            nfail += 1
    return {'counted_calls_http200': n200, 'failed_calls_parse': nfail,
            'transport_rows_not_counted': nretry, 'tokens_in': tin, 'tokens_out': tout,
            'spend_usd': round(tin * PRICE_IN + tout * PRICE_OUT, 5)}


def select(rows):
    cands = []
    for arm in ('A', 'B', 'A+B', 'C'):
        for sw in (True, False):
            e = _row_of(rows, arm, sw)
            p = e['primary']
            cands.append({'arm': arm, 'switch': 'on' if sw else 'off',
                          'cov_pct': p['coverage']['pct'], 'cov': p['coverage'],
                          'fa_pct': p['fa']['pct'], 'fa': p['fa'],
                          'T_pct': p['fa_by_type']['T']['pct'], 'T': p['fa_by_type']['T'],
                          'calls': e['model_calls_unique']})
    work = []
    gate = [c for c in cands if (c['T_pct'] or 0) <= 1.5]
    work.append('type-T FA <= 1.5%% gate: %d of 8 rows pass -> %s'
                % (len(gate), [('%s/%s' % (c['arm'], c['switch'])) for c in gate]))
    under5 = [c for c in gate if (c['fa_pct'] or 0) < 5.0]
    if under5:
        under5.sort(key=lambda c: (-(c['cov_pct'] or 0), c['calls']))
        pick = under5[0]
        work.append('rows with FA point estimate < 5%%: %s'
                    % [('%s/%s cov %.2f FA %.2f' % (c['arm'], c['switch'], c['cov_pct'], c['fa_pct']))
                       for c in under5])
        work.append('-> highest coverage among them: %s / switch %s' % (pick['arm'], pick['switch']))
    else:
        work.append('NO row passing the T gate has an FA point estimate under 5% — '
                    'falling back to the LOWEST FA among the gate survivors.')
        pool = gate or cands
        pool = sorted(pool, key=lambda c: ((c['fa_pct'] or 0), -(c['cov_pct'] or 0), c['calls']))
        pick = pool[0]
        work.append('-> lowest FA: %s / switch %s (FA %.2f%%, coverage %.2f%%)'
                    % (pick['arm'], pick['switch'], pick['fa_pct'], pick['cov_pct']))
    return pick, cands, work


RUN_FINAL_SRC = '''#!/usr/bin/env python3
"""Phase 1j — the ONE final run (agent F) and the zero-call DEV reproduction of the selected row.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1j/run_final.py --side dev        # 0 new calls, reproduces DEV
    PHASE1J_FINAL=1 PYTHONDONTWRITEBYTECODE=1 python3 phase1j/run_final.py --side holdout

Everything comes from phase1j/FROZEN_CONFIG_1J.json; the logic is the shared library
phase1j/taskC/runner_1j.py, so the holdout requests are built by exactly the code that built the DEV
requests. The holdout is read ONLY through loader_1j. The API key is read only inside
pipeline_1i.load_key(). Counted calls (HTTP 200) go to the ONE shared ledger phase1j/ledger.jsonl and
are also mirrored into taskD/final_calls.jsonl.
"""
import argparse, collections, json, os, random, sys
from concurrent.futures import ThreadPoolExecutor

P1J = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(P1J, 'taskC'))
import runner_1j as R                                                       # noqa: E402
import pipeline_1i as P                                                     # noqa: E402

CFG = json.load(open(os.path.join(P1J, 'FROZEN_CONFIG_1J.json'), encoding='utf-8'))
DONE = os.path.join(P1J, 'FINAL_RUN_DONE')
TASKD = os.path.join(P1J, 'taskD')
ARM, SWITCH = CFG['arm'], CFG['switch'] == 'on'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--side', required=True, choices=('dev', 'holdout'))
    a = ap.parse_args()
    if a.side == 'holdout':
        if os.environ.get('PHASE1J_FINAL') != '1':
            raise SystemExit('REFUSED: the holdout run needs PHASE1J_FINAL=1.')
        if os.path.exists(DONE):
            raise SystemExit('REFUSED: %s exists — the holdout is measured once.' % DONE)
    os.makedirs(TASKD, exist_ok=True)
    purpose = 'Phase 1j FINAL run of the frozen 1j config' if a.side == 'holdout' \\
        else 'Phase 1j: zero-call reproduction of the selected DEV row'
    data = R.load_side(a.side, purpose)
    recs0 = data[0]
    prim, sens, rel = R.label_sets(recs0, a.side)
    ALL = R.build_all(a.side, data, purpose)
    reuse_1i = ALL['_reuse']
    rep, ver, counted, failed_h, retries = R.ledger_state()
    ver = dict(ver); ver.update({h: v for h, v in reuse_1i.items() if h not in ver})

    need = [h for h in ALL[ARM]['req'] if h not in ver and h not in rep and h not in failed_h]
    print('side=%s arm=%s switch=%s  L3=%d  unique prompts=%d  reused=%d  NEW calls needed=%d'
          % (a.side, ARM, CFG['switch'], len(ALL[ARM]['l3']), len(ALL[ARM]['req']),
             len(ALL[ARM]['req']) - len(need), len(need)))
    if a.side == 'dev':
        if need:
            raise SystemExit('FAIL: --side dev must need ZERO new calls, needs %d' % len(need))
    else:
        if counted + len(need) > R.CAP_TOTAL:
            raise SystemExit('REFUSED: %d + %d > hard cap %d' % (counted, len(need), R.CAP_TOTAL))
        if need:
            todo = [ALL[ARM]['req'][h] for h in need]
            random.Random(1).shuffle(todo)
            key = P.load_key()
            with ThreadPoolExecutor(max_workers=6) as pool:
                for _ in pool.map(lambda q: R.call_one(q, key), todo):
                    pass
            rep, ver, counted, failed_h, retries = R.ledger_state()
            ver = dict(ver); ver.update({h: v for h, v in reuse_1i.items() if h not in ver})

    out = {'side': a.side, 'frozen': CFG, 'relabel': rel, 'rows': {}}
    A = ALL[ARM]
    for lname, lab in (('primary', prim), ('sensitivity', sens)):
        use = lab if R.ARMS[ARM]['labels'] == 'b' else \\
            {r['item_id']: (r['judged'], r['wrong_type']) for r in recs0}
        vm, tags = R.arm_verdict_map(ARM, A['hashes'], rep, ver, SWITCH)
        res = P.run_pipeline(A['st'], vm,
                             tip_reject=(False if R.ARMS[ARM]['contract'] else SWITCH))
        m = R.score(R.relabel(A['recs'], use), res)
        fa_full = []
        for f in m['fa_items']:
            r = A['by_id'][f['id']]
            fa_full.append(dict(f, model_reply=rep.get(A['hashes'].get(f['id']), ''),
                                slovak_used=r['sk'], reference=r['reference'], answer=r['answer']))
        out['rows'][lname] = {'coverage': m['coverage'], 'fa': m['fa'],
                              'fa_by_type': m['fa_by_type'], 'fa_by_layer': m['fa_by_layer'],
                              'fr_by_layer': m['fr_by_layer'],
                              'false_rejections': m['false_rejections'],
                              'false_acceptances': fa_full,
                              'no_verdict_items': [i for i in A['l3'] if i not in vm]}
        if lname == 'primary':
            with open(os.path.join(TASKD, 'final_verdicts.jsonl'), 'w', encoding='utf-8') as fh:
                for i in sorted(res):
                    fh.write(json.dumps(dict(res[i], model_reply=rep.get(A['hashes'].get(i), '')),
                                        ensure_ascii=False) + '\\n')
    # zero-call BASE replay (the frozen Phase 1i config) on the same items
    vmb, _ = R.arm_verdict_map('BASE', ALL['BASE']['hashes'], rep, ver, True)
    resb = P.run_pipeline(ALL['BASE']['st'], vmb, tip_reject=True)
    mb = R.score(R.relabel(ALL['BASE']['recs'],
                           {r['item_id']: (r['judged'], r['wrong_type']) for r in recs0}), resb)
    out['base_1i_replay_same_items'] = {'coverage': mb['coverage'], 'fa': mb['fa'],
                                        'fa_by_type': mb['fa_by_type'],
                                        'fa_by_layer': mb['fa_by_layer'],
                                        'fr_by_layer': mb['fr_by_layer'],
                                        'new_calls': 0}
    out['calls'] = R.token_spend()
    out['calls']['transport_retries'] = retries
    out['calls']['reused_prompts'] = len(A['req']) - len(need)
    out['calls']['new_this_run'] = len(need)
    if a.side == 'holdout':
        rows = [r for r in R.ledger_rows() if r.get('http') == 200]
        with open(os.path.join(TASKD, 'final_calls.jsonl'), 'w', encoding='utf-8') as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + '\\n')
        json.dump(out, open(os.path.join(TASKD, 'final_summary.json'), 'w'), indent=1,
                  ensure_ascii=False)
        open(DONE, 'w').write(json.dumps({'coverage': out['rows']['primary']['coverage'],
                                          'fa': out['rows']['primary']['fa']}) + '\\n')
    else:
        json.dump(out, open(os.path.join(TASKD, 'dev_reproduction.json'), 'w'), indent=1,
                  ensure_ascii=False)
    pr = out['rows']['primary']
    print('coverage %s' % R._r(pr['coverage']))
    print('FA       %s' % R._r(pr['fa']))
    for t in ('T', 'W', 'M', 'S'):
        print('  FA %s  %s' % (t, R._r(pr['fa_by_type'][t])))
    print('FA by layer %s   FR by layer %s' % (pr['fa_by_layer'], pr['fr_by_layer']))
    print('sensitivity: coverage %s  FA %s'
          % (R._r(out['rows']['sensitivity']['coverage']), R._r(out['rows']['sensitivity']['fa'])))
    print('BASE 1i replay (0 calls): coverage %s  FA %s'
          % (R._r(out['base_1i_replay_same_items']['coverage']),
             R._r(out['base_1i_replay_same_items']['fa'])))
    print('calls %s' % json.dumps(out['calls']))
    if a.side == 'holdout':
        print('false acceptances, itemised:')
        for f in pr['false_acceptances']:
            print(json.dumps(f, ensure_ascii=False))
        print('FINAL_RUN_DONE written — the holdout is closed.')
    if a.side == 'dev':
        exp = CFG['selected_dev_numbers']
        ok = (pr['coverage']['k'] == exp['coverage']['k'] and pr['fa']['k'] == exp['fa']['k']
              and len(need) == 0)
        print('DEV reproduction with ZERO new calls: %s' % ('OK' if ok else 'MISMATCH'))


if __name__ == '__main__':
    main()
'''


def write_outputs(R):
    rows, ALL, prim, sens = R['rows'], R['ALL'], R['prim'], R['sens']
    rel, recs0 = R['rel'], R['recs0']
    pick, cands, work = select(rows)
    tags = tag_accuracy(R)
    spend = token_spend()
    orig_lab = {r['item_id']: (r['judged'], r['wrong_type']) for r in recs0}

    # ---- subject analysis: BASE type-S false acceptances vs each arm
    base = _row_of(rows, 'BASE', True)
    base_S = [f for f in base['primary']['fa_items'] if f['type'] == 'S']
    base_res = R['details'][('BASE', True)]['res']
    subj = {'base_type_S_fa': [], 'correct_answers_lost': {}}
    for f in base_S:
        r0 = ALL['BASE']['by_id'][f['id']]
        e = {'id': f['id'], 'layer': f['layer'], 'model': f['model'], 'sk': r0['sk'],
             'reference': r0['reference'], 'answer': r0['answer'], 'removed_by': {}}
        for arm in ('A', 'B', 'A+B', 'C'):
            res = R['details'][(arm, True)]['res']
            if f['id'] in res:
                lab = (prim if ARMS[arm]['labels'] == 'b' else orig_lab).get(f['id'], ('wrong', 'S'))
                e['removed_by'][arm] = ('still accepted' if res[f['id']]['accepted']
                                        else 'REMOVED (%s)' % res[f['id']]['layer'])
                e['removed_by'][arm] += '' if lab[0] == 'wrong' else ' [now labelled correct]'
        subj['base_type_S_fa'].append(e)
    base_ok = {i for i in base_res if base_res[i]['accepted']}
    for arm in ('A', 'B', 'A+B', 'C'):
        res = R['details'][(arm, True)]['res']
        lab = prim if ARMS[arm]['labels'] == 'b' else orig_lab
        lost = []
        for i, l in lab.items():
            if l[0] == 'correct' and i in base_ok and i in res and not res[i]['accepted']:
                r0 = ALL[arm]['by_id'].get(i)
                lost.append({'id': i, 'layer': res[i]['layer'], 'model': res[i]['model'],
                             'sk': r0['sk'] if r0 else '', 'answer': r0['answer'] if r0 else ''})
        subj['correct_answers_lost'][arm] = lost

    sel = _row_of(rows, pick['arm'], pick['switch'] == 'on')
    sel_fa = []
    for f in sel['primary']['fa_items']:
        r0 = ALL[pick['arm']]['by_id'][f['id']]
        sel_fa.append(dict(f, model_reply=R['rep'].get(ALL[pick['arm']]['hashes'].get(f['id']), ''),
                           sk=r0['sk'], reference=r0['reference'], answer=r0['answer']))

    dev = {'label_rules': {
        'arm_A_and_BASE': 'existing labels on the original Slovak (items.jsonl judged / wrong_type)',
        'arms_B_A+B_C_primary': 'existing label/type, overridden to (wrong, type S) exactly where the '
                                'blind judge says label=wrong AND subj_ok=false, for items of REWRITTEN '
                                'sentences only; every other judge disagreement counted, not adopted',
        'arms_B_A+B_C_sensitivity': 'judge label AND type adopted for every rewritten-sentence item',
        'controls': 'the 60 CONTROL items (unchanged Slovak) never change a label; they measure judge '
                    'noise only'},
        'relabel': rel, 'budget_plan': R['plan'], 'subsample': R['subsample'],
        'rows': rows, 'subject_analysis': subj, 'tag_accuracy': tags,
        'selection': {'candidates': cands, 'working': work, 'picked': pick},
        'selected_false_acceptances': sel_fa, 'calls': spend}
    json.dump(dev, open(os.path.join(TASKD, 'dev_results.json'), 'w'), indent=1, ensure_ascii=False)

    cfg = {'phase': '1j', 'side_measured': 'dev', 'arm': pick['arm'], 'switch': pick['switch'],
           'model': P.MODEL, 'generationConfig': TAG_CFG if ARMS[pick['arm']]['contract']
           else P.GEN_CFG,
           'flags': dict(ARMS[pick['arm']]),
           'guards': list(('F4v3', 'f4p') if ARMS[pick['arm']]['f4p'] else ('F4v3',)),
           'b_fix': True,
           'system_instruction': (TAG_SYS if ARMS[pick['arm']]['contract']
                                  else P.sys_text(ALL['BASE']['st'], 'P-E4b')),
           'prompt': {'base': 'the frozen P-B lines of checker_1i.prompt(it, "P-B")',
                      'extra_lines_in_order': ['gender line (only when the annotation still has g)',
                                               'p line (p_chain.p_prompt_line) when p_prompt is on',
                                               'ground line', 'wording line'],
                      'gender_template': P.GENDER_TMPL, 'ground_line': P.GROUND_LINE,
                      'wording_line': P.WORDING_LINE,
                      'tail': TAG_TAIL if ARMS[pick['arm']]['contract'] else 'SAME, TIP or DIFF?'},
           'verdict_rule': ('TAG CONTRACT: any SUBJ/SWAP/ADD -> wrong; MISS -> %s; OK -> accepted; '
                            'no parsable tag -> no verdict -> rejected'
                            % ('rejected' if pick['switch'] == 'on' else 'accepted'))
           if ARMS[pick['arm']]['contract'] else
           ('one word SAME/TIP/DIFF; TIP -> %s' % ('rejected' if pick['switch'] == 'on'
                                                   else 'accepted')),
           'label_rule': dev['label_rules'],
           'data': ('Task B rewritten Slovak (taskB/sk_new.json), refs_new, '
                    'annotations_b_<side>.json (g=null on rewritten sids)')
           if ARMS[pick['arm']]['data'] == 'b' else 'original Slovak and annotations',
           'p_chain': ('derive_p(new Slovak); when None on a rewritten sentence, person/number taken '
                       'from the inserted pronoun in taskB/rewrites.jsonl')
           if ARMS[pick['arm']]['p_prompt'] else 'not used',
           'selected_dev_numbers': {'coverage': sel['primary']['coverage'],
                                    'fa': sel['primary']['fa'],
                                    'fa_by_type': sel['primary']['fa_by_type']}}
    json.dump(cfg, open(os.path.join(P1J, 'FROZEN_CONFIG_1J.json'), 'w'), indent=1,
              ensure_ascii=False)
    open(os.path.join(P1J, 'run_final.py'), 'w', encoding='utf-8').write(RUN_FINAL_SRC)
    os.chmod(os.path.join(P1J, 'run_final.py'), 0o755)

    # ---------------------------------------------------------------- markdown
    L = []
    w = L.append
    w('# Phase 1j — Task D, the DEV measurement (agent R)')
    w('')
    w('Model **gemini-3.1-flash-lite**, temperature 0, thinkingBudget 0 — decided, not tested. '
      'DEV only. Every counted call is an HTTP-200 row in the one shared ledger `phase1j/ledger.jsonl`.')
    w('')
    w('## 1 Label rules (declared before the results)')
    w('')
    for k, v in dev['label_rules'].items():
        w('- **%s** — %s' % (k, v))
    w('- Type **M** in CONTEXT_1J §6 is *"meaning added **or** dropped"*, so under the tag contract the '
      'expected tag for an M item is **MISS or ADD** (either counts as correct).')
    w('')
    w('## 2 Relabelling counts and judge noise')
    w('')
    w('DEV (rewritten-sentence items only, controls excluded): `%s`' % json.dumps(rel['dev']))
    w('')
    w('Both sides together (counts only, taken from the key map; no holdout row was opened): `%s`'
      % json.dumps(rel['both_sides']))
    w('')
    w('Primary overrides actually applied on DEV: **%d** items. Sensitivity overrides on DEV: **%d**.'
      % (rel['primary_overrides_dev'], rel['sensitivity_overrides_dev']))
    w('')
    w('**Judge noise, 60 CONTROL items** (unchanged Slovak, judged blind a second time):')
    w('')
    cn = rel['control_noise']
    w('| direction | rate | exact 95 %% CP |')
    w('|---|---|---|')
    for k in ('correct_to_wrong', 'wrong_to_correct', 'any_flip'):
        w('| %s | %d/%d = %.2f %% | [%.2f, %.2f] |'
          % (k, cn[k]['k'], cn[k]['n'], cn[k]['pct'] or 0.0, cn[k]['ci'][0], cn[k]['ci'][1]))
    w('')
    w('## 3 Budget plan (printed before any call, zero calls)')
    w('')
    w('| arm | items at L3 | unique prompts | already stored | NEW calls after dedupe |')
    w('|---|---|---|---|---|')
    for name in ARM_ORDER:
        p = R['plan'][name]
        w('| %s | %d | %d | %d | %d |' % (name, p['l3'], p['unique_prompts'], p['already_have'],
                                          p['new_after_dedupe']))
    w('')
    w('Total NEW planned: **%d** (DEV allowance 1,070 = 1,400 hard cap − 330 reserved for the final '
      'holdout run). Subsample: **%s**. All (item, arm) pairs were built first, byte-identical prompts '
      'deduped, then shuffled with seed 1 so an outage damages every arm equally.'
      % (sum(R['plan'][n]['new_after_dedupe'] for n in ARM_ORDER), R['subsample']))
    w('')
    w('## 4 The table')
    w('')
    w('*switch* = TIP-as-rejection for A / B / A+B. **For arm C there is no TIP**; its analogue is the '
      'MISS row of the tag table — switch **on** = `MISS -> rejected`, switch **off** = '
      '`MISS -> accepted`. Coverage denominators differ between arms because the B-labels move items '
      'between the correct and the wrong set; read the percentages, not the counts, across arms.')
    for lname in ('primary', 'sensitivity'):
        w('')
        w('### 4.%d %s labels' % (1 if lname == 'primary' else 2, lname))
        w('')
        w('| arm | switch | coverage | FA | FA T | FA W | FA M | FA S | failed calls | FR by layer |')
        w('|---|---|---|---|---|---|---|---|---|---|')
        for name in ARM_ORDER:
            for sw in ('on', 'off'):
                e = _row_of(rows, name, sw == 'on')
                d = e[lname]
                w('| %s | %s | %s | %s | %s | %s | %s | %s | %d | %s |'
                  % (name, sw, _r(d['coverage']), _r(d['fa']),
                     _r(d['fa_by_type']['T']), _r(d['fa_by_type']['W']),
                     _r(d['fa_by_type']['M']), _r(d['fa_by_type']['S']),
                     e['no_verdict'], json.dumps(d['fr_by_layer'])))
    w('')
    w('"failed calls" = items that reached L3 and have **no** verdict (an empty or unparsable HTTP-200 '
      'reply, counted, never retried, never guessed); they are scored as rejected.')
    w('')
    w('## 5 A vs B on the subject problem')
    w('')
    w('BASE has %d type-S false acceptances on DEV. Per item, under switch **on**:' % len(base_S))
    w('')
    w('| item | A | B | A+B | C |')
    w('|---|---|---|---|---|')
    for e in subj['base_type_S_fa']:
        w('| `%s` | %s | %s | %s | %s |' % (e['id'], e['removed_by'].get('A', '—'),
                                            e['removed_by'].get('B', '—'),
                                            e['removed_by'].get('A+B', '—'),
                                            e['removed_by'].get('C', '—')))
    w('')
    for e in subj['base_type_S_fa']:
        w('- `%s` — SK: %s | ref: %s | answer: **%s**' % (e['id'], e['sk'], e['reference'],
                                                          e['answer']))
    w('')
    w('**Correct answers each arm loses that BASE accepted** (label in force for that arm, switch on):')
    for arm in ('A', 'B', 'A+B', 'C'):
        lost = subj['correct_answers_lost'][arm]
        w('')
        w('- **%s** — %d lost' % (arm, len(lost)))
        for x in lost[:25]:
            w('  - `%s` at %s (model %s) — %s' % (x['id'], x['layer'], x['model'], x['answer']))
    w('')
    w('## 6 Task C — tag-level accuracy of the contract')
    w('')
    w('Expected tag from the label in force: correct -> `OK`, M -> `MISS` or `ADD`, W -> `SWAP`, '
      'S -> `SUBJ`. Type **T** has no tag in the contract and is reported separately. Scored on the '
      'first tag returned.')
    w('')
    w('- items that reached the model: **%d**, unparsable replies: **%d**'
      % (tags['n_reached_model'], tags['unparsable']))
    w('- overall tag accuracy (excluding T): **%s**' % _r(tags['overall']))
    w('')
    w('| expected class | tag accuracy | exact 95 %% CP |')
    w('|---|---|---|')
    for c in ('correct', 'M', 'W', 'S'):
        if c in tags['per_class']:
            d = tags['per_class'][c]
            w('| %s | %d/%d = %.2f %% | [%.2f, %.2f] |' % (c, d['k'], d['n'], d['pct'] or 0.0,
                                                           d['ci'][0], d['ci'][1]))
    w('')
    w('Tags the model gave **type-T** items: `%s`' % json.dumps(tags['type_T_tags']))
    w('')
    w('Confusion, expected x first tag returned: `%s`' % json.dumps(tags['confusion_first']))
    w('')
    w('Confusion, expected x full tag SET: `%s`' % json.dumps(tags['confusion_set']))
    w('')
    w('Ten example mismatches:')
    w('')
    for m in tags['mismatch_examples']:
        w('- `%s` expected %s, returned `%s` — SK: %s | ref: %s | answer: **%s**'
          % (m['id'], '/'.join(m['expected']), m['returned'], m['sk'], m['reference'], m['answer']))
    w('')
    w('## 7 Selection')
    w('')
    w('| arm | switch | coverage | FA | FA type T | unique calls |')
    w('|---|---|---|---|---|---|')
    for c in cands:
        w('| %s | %s | %s | %s | %s | %d |' % (c['arm'], c['switch'], _r(c['cov']), _r(c['fa']),
                                               _r(c['T']), c['calls']))
    w('')
    for line in work:
        w('- %s' % line)
    w('')
    w('**Frozen choice: arm `%s`, switch `%s`** — written to `phase1j/FROZEN_CONFIG_1J.json`; '
      '`phase1j/run_final.py` rebuilds exactly these requests.' % (pick['arm'], pick['switch']))
    w('')
    w('### DEV false acceptances of the selected configuration, itemised')
    w('')
    for f in sel_fa:
        w('- `%s` type %s at %s — model reply `%s` | SK: %s | ref: %s | answer: **%s**'
          % (f['id'], f['type'], f['layer'], (f.get('model_reply') or '').strip(), f['sk'],
             f['reference'], f['answer']))
    w('')
    w('## 8 Calls, tokens, spend')
    w('')
    w('`%s`' % json.dumps(spend))
    w('')
    w('Transport retries (non-200 rows, never counted): %d. Prompts reused byte-identically from the '
      'Phase 1i ledgers: %d. Spend at $0.25 / 1M input and $1.50 / 1M output tokens: **$%.5f**. '
      '**Whether these calls were billed or served from a free tier is not detectable from the '
      'response body** — the figure is the list price of the tokens actually reported by '
      '`usageMetadata`.' % (spend['transport_rows_not_counted'], len(R['reuse_1i']),
                            spend['spend_usd']))
    open(os.path.join(TASKD, 'TASK_D_DEV.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('\n== SELECTED: arm %s switch %s ==' % (pick['arm'], pick['switch']))
    for line in work:
        print('  ' + line)
    print('  coverage %s   FA %s' % (_r(sel['primary']['coverage']), _r(sel['primary']['fa'])))
    print('  tag accuracy overall %s (unparsable %d)' % (_r(tags['overall']), tags['unparsable']))
    print('  calls %s' % json.dumps(spend))
    for name in ARM_ORDER:
        for sw in ('on', 'off'):
            e = _row_of(rows, name, sw == 'on')
            print('  %-16s %-3s cov %-22s FA %-22s T %s  fail %d'
                  % (name, sw, _r(e['primary']['coverage']), _r(e['primary']['fa']),
                     _r(e['primary']['fa_by_type']['T']), e['no_verdict']))


if __name__ == '__main__':
    r = main()
    if r:
        write_outputs(r)
