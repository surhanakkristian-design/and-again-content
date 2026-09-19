#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1Q Task B2/B3 part 2.  0 model calls, 0 DB.

PART 1  F6 (as frozen, VARIANT C) against the hand gold over the 120 NEW
        sentences 170001-170120 (phase1q/f6_gold_1p.json).  The 1P annotation
        record is flat {v, lk, alt, ...}; the 1N pipeline nests it under
        "hygienised", so it is wrapped HERE (never inside f6.py).
PART 2  F5 (frozen, phase1i/checker_1i.f5_adjunct_deletion) measured on the
        CLOSED 1N set, on its own lines: cost = judged-CORRECT answers F5
        rejects, catches = judged-WRONG answers F5 rejects by wrong-type, plus
        the overlap with F6's rejected items (from phase1q/f6_eval_1n.json).
        The 1N records are built through phase1n/runner_1n.build_side_1n, so
        they carry exercise_id / item_id and the HYGIENE registry entries -
        the earlier attempt hand-rolled the record and every call raised
        KeyError 'exercise_id'.
"""
import collections
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import f6                                                             # noqa: E402
import f6_eval_1n as E                                                # noqa: E402

P1P = os.path.join(ROOT, 'phase1p')
P1N = os.path.join(ROOT, 'phase1n')


def alog(what, n):
    line = {'ts': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
            'side': '1q:taskB2', 'what': what, 'caller': 'phase1q_f6_gold_120', 'n': n,
            'purpose': '1Q B2 F6 hand gold, sentences+annotation only'}
    with open(os.path.join(P1P, 'access_log.jsonl'), 'a') as fh:
        fh.write(json.dumps(line, ensure_ascii=False) + '\n')


# ------------------------------------------------------------------ PART 1 --
def part1(variants=('C', 'A', 'B')):
    S = {str(x['sid']): x for x in json.load(open(os.path.join(P1P, 'data/sentences.json')))}
    alog('data/sentences.json', len(S))
    Asrc = json.load(open(os.path.join(P1P, 'data/annotations_src.json')))
    alog('data/annotations_src.json', len(Asrc))
    # mirror the 1N container: {"<sid>": {"hygienised": {v, lk, alt, ...}}}
    A = {str(k): {'hygienised': v} for k, v in Asrc.items()}
    gold = json.load(open(os.path.join(HERE, 'f6_gold_1p.json')))
    out = {}
    for v in variants:
        out[v] = E.run_gold(gold, A, S, v)
    return out, gold


# ------------------------------------------------------------------ PART 2 --
def f5_on_1n():
    sys.path.insert(0, P1N)
    os.chdir(P1N)
    import runner_1n as RN                                            # noqa: E402
    import runner_1l as RL                                            # noqa: E402
    C = RL.C
    fn = C.f5_adjunct_deletion
    st, recs, ann, by, info = RN.build_side_1n('1Q B3: F5 measurement on the closed 1N set')
    os.chdir(HERE)
    S, A, I, lab = E.load_set(P1N)
    rec_by_id = {}
    for r in recs:
        rec_by_id[r.get('item_id') or r.get('exercise_id')] = r
    diag = {'n_recs': len(recs), 'rec_keys': sorted(recs[0].keys()),
            'call_shape': None, 'errors': collections.Counter()}

    def call(rec):
        def _tail(r):
            try:
                return int(str(r.get('item_id', '')).split(':')[-1])
            except Exception:
                return 0
        shapes = [
            ('as built', lambda r: dict(r)),
            ('+exercise_id=item_id', lambda r: dict(r, exercise_id=r.get('item_id'))),
            ('+exercise_id=sid(int)', lambda r: dict(r, exercise_id=int(r['sid']))),
            ('+exercise_id=id tail(int)', lambda r: dict(r, exercise_id=_tail(r))),
            ('+exercise_id=sid+id=sid', lambda r: dict(r, exercise_id=int(r['sid']), id=int(r['sid']))),
            ('+exercise_id=sid+answer+reference',
             lambda r: dict(r, exercise_id=int(r['sid']), id=int(r['sid']),
                            answer=r.get('answer') or r.get('ans'),
                            reference=r.get('reference') or (r.get('refs') or [''])[0])),
        ]
        last = None
        for name, f in shapes:
            try:
                res = fn(f(rec))
            except Exception as ex:
                import traceback as _tb
                fr = _tb.extract_tb(ex.__traceback__)[-1]
                last = '%s: %s [%s @ %s:%d]' % (type(ex).__name__, ex, name,
                                                fr.name, fr.lineno)
                continue
            if diag['call_shape'] is None:
                diag['call_shape'] = name
            return res, None
        return None, last

    cost, catches, rejset = [], collections.defaultdict(list), set()
    n_corr = n_wrong = n_fail = 0
    for it in I:
        L = lab.get(it['id'])
        if not L or L['judged'] not in ('correct', 'wrong'):
            continue
        rec = rec_by_id.get(it['id'])
        if rec is None:
            diag['errors']['no record for %s' % it['id']] += 1
            continue
        res, err = call(rec)
        if err:
            n_fail += 1
            diag['errors'][err] += 1
            rej = False
        else:
            rej = E.f5_rejects(res)
        if L['judged'] == 'correct':
            n_corr += 1
            if rej:
                cost.append({'id': it['id'], 'answer': it['answer'], 'why': _why(res)})
        else:
            n_wrong += 1
            if rej:
                catches[L['type'] or '?'].append({'id': it['id'], 'answer': it['answer'],
                                                  'why': _why(res)})
        if rej:
            rejset.add(it['id'])
    diag['errors'] = dict(diag['errors'])
    return {'n_correct': n_corr, 'n_wrong': n_wrong, 'n_call_failures': n_fail,
            'cost': cost, 'catches': dict(catches), 'rejset': sorted(rejset),
            'diag': diag}


def _why(res):
    if isinstance(res, dict):
        for k in ('why', 'reason', 'reasons', 'spans', 'deleted', 'detail'):
            if res.get(k):
                return res[k]
        return {k: v for k, v in res.items() if k in ('verdict', 'fires', 'layer')}
    return str(res)[:160]


# --------------------------------------------------------------------- md ---
def write_md(path, g, f5, overlap, gold_n):
    W = []
    A = W.append
    A('# Phase 1Q Task B2/B3 part 2 - F6 hand gold on the 120 NEW sentences, F5 measured on 1N')
    A('')
    A('0 model calls, 0 DB. `f6.py` was NOT touched (VARIANT C, as frozen).')
    A('')
    A('## PART 1 - F6 hand gold, 120 new sentences (sids 170001-170120)')
    A('')
    A('Source of the gold: `phase1p/data/sentences.json` + `phase1p/data/annotations_src.json`')
    A('(the blind reference annotation: `v`, `lk`, `alt`). No `items.json`, no writer answers, no')
    A('labels were opened; both reads are logged in `phase1p/access_log.jsonl`.')
    A('The flat 1P record is wrapped as `{"hygienised": {...}}` in this script, mirroring the 1N')
    A('container that `f6._ann` unwraps.')
    A('')
    A('`faithful` = a correct natural English answer, not identical to `v[0]`; gold = must NOT be')
    A('rejected. `added` = the same answer plus exactly one content addition the Slovak lacks; gold')
    A('= should be rejected. agree = addition rejected. conservative = addition not rejected')
    A('(harmless miss). ERROR = a faithful answer rejected.')
    A('')
    A('| variant | agree | conservative | ERROR |')
    A('|---|---|---|---|')
    for v, d in g.items():
        A('| %s%s | %d/%d | %d | %d |' % (v, ' (selected)' if v == 'C' else '', d['agree'], d['n'],
                                          d['conservative'], len(d['errors'])))
    A('')
    A('### Variant C - every ERROR (faithful answer rejected)')
    A('')
    if not g['C']['errors']:
        A('none.')
    for e in g['C']['errors']:
        A('- **%s** - "%s" -> F6 blamed `%s` (%s)' % (e['sid'], e['answer'], e['blamed'], e['reason']))
    A('')
    A('### Variant C - conservative items (planted addition NOT rejected)')
    A('')
    if not g['C']['missed']:
        A('none.')
    for m in g['C']['missed']:
        A('- %s - added "%s" -> %s (%s)' % (m['sid'], m['add'], m['verdict'], m['reason']))
    A('')
    A('### 1N gold (closed set, reported separately - never pooled with the 120)')
    A('')
    A('| set | agree | conservative | ERROR |')
    A('|---|---|---|---|')
    A('| 1N (100 sentences) | 63/100 | 37 | 0 |')
    A('| 1P new (120 sentences) | %d/%d | %d | %d |' % (g['C']['agree'], g['C']['n'],
                                                        g['C']['conservative'], len(g['C']['errors'])))
    A('')
    A('No measured cost on the 1P items is reported here: the 1P answers and labels stay unopened.')
    A('')
    A('## PART 2 - F5 (frozen omission guard) on the CLOSED 1N set')
    A('')
    A('The earlier attempt called `phase1i/checker_1i.f5_adjunct_deletion` with a hand-rolled dict;')
    A('every call raised `KeyError: exercise_id` and its 0/426 figure is VOID. Here the 1N records')
    A('are built by `phase1n/runner_1n.build_side_1n(...)` (the real builder: `item_id`,')
    A('`exercise_id`, refs, chk, the HYGIENE registry) and F5 is called on those records.')
    A('')
    A('- record shape handed to F5: `%s`' % f5['diag']['call_shape'])
    A('- records built: %d; call failures: %d' % (f5['diag']['n_recs'], f5['n_call_failures']))
    if f5['diag']['errors']:
        A('- call errors: `%s`' % json.dumps(f5['diag']['errors'])[:400])
    A('')
    A('| | k/n | %% |')
    A('|---|---|---|')
    A('| **F5 cost** (judged-CORRECT answers F5 rejects) | %d/%d | %.2f |'
      % (len(f5['cost']), f5['n_correct'], 100.0 * len(f5['cost']) / max(1, f5['n_correct'])))
    nc = sum(len(x) for x in f5['catches'].values())
    A('| **F5 catches** (judged-WRONG answers F5 rejects) | %d/%d | %.2f |'
      % (nc, f5['n_wrong'], 100.0 * nc / max(1, f5['n_wrong'])))
    A('')
    A('Catches by wrong type:')
    A('')
    A('| wrong type | F5 rejects |')
    A('|---|---|')
    for t, xs in sorted(f5['catches'].items()):
        A('| %s | %d/%d |' % (t, len(xs), f5['n_wrong']))
    if not f5['catches']:
        A('| - | 0 |')
    A('')
    A('### F5 cost items (judged CORRECT, F5 rejected)')
    A('')
    if not f5['cost']:
        A('none.')
    for c in f5['cost']:
        A('- `%s` - "%s" -> %s' % (c['id'], c['answer'], str(c['why'])[:200]))
    A('')
    A('### F5 catches (judged WRONG, F5 rejected)')
    A('')
    if not nc:
        A('none.')
    for t, xs in sorted(f5['catches'].items()):
        for c in xs:
            A('- [%s] `%s` - "%s" -> %s' % (t, c['id'], c['answer'], str(c['why'])[:160]))
    A('')
    A('### Overlap F5 / F6[C] on 1N')
    A('')
    A('F5 and F6 numbers are NEVER added together. Items both guards reject: **%d**.' % len(overlap))
    for i in overlap:
        A('- `%s`' % i)
    A('')
    A('## Files')
    A('')
    A('- `phase1q/f6_gold_1p.json` - the 120 x 2 hand gold (new sentences)')
    A('- `phase1q/f6_gold_eval_1p.py` - this measurement (re-runnable, 0 calls)')
    A('- `phase1q/f6_gold_1p_eval.json` - raw numbers')
    A('- `phase1q/F6_VALIDATION_1N.md` - earlier file; its F5 lines are VOID (notice appended there)')
    open(path, 'w').write('\n'.join(W) + '\n')


def main():
    g, gold = part1()
    for v, d in g.items():
        print('[1P gold %s] agree %d/%d conservative %d ERROR %d'
              % (v, d['agree'], d['n'], d['conservative'], len(d['errors'])))
    for e in g['C']['errors']:
        print('  ERROR C %s "%s" blamed %s' % (e['sid'], e['answer'], e['blamed']))
    f5 = f5_on_1n()
    nc = sum(len(x) for x in f5['catches'].values())
    print('[F5 on 1N] cost %d/%d  catches %d/%d  by type %s  failures %d  shape %s'
          % (len(f5['cost']), f5['n_correct'], nc, f5['n_wrong'],
             {t: len(x) for t, x in f5['catches'].items()}, f5['n_call_failures'],
             f5['diag']['call_shape']))
    if f5['diag']['errors']:
        print('  F5 call errors:', json.dumps(f5['diag']['errors'])[:400])
    ev = json.load(open(os.path.join(HERE, 'f6_eval_1n.json')))
    f6rej = set((ev.get('variants', {}).get('C', {}).get('measured', {}) or {}).get('rejset') or [])
    overlap = sorted(set(f5['rejset']) & f6rej)
    print('overlap F5 & F6[C] on 1N: %d (F6[C] rejected %d)' % (len(overlap), len(f6rej)))
    json.dump({'gold_1p': g, 'f5_1n': f5, 'overlap_f5_f6C_1n': overlap,
               'f6_C_rejset_1n': sorted(f6rej)},
              open(os.path.join(HERE, 'f6_gold_1p_eval.json'), 'w'), ensure_ascii=False, indent=1)
    write_md(os.path.join(HERE, 'F6_GOLD_1P_AND_F5_1N.md'), g, f5, overlap, len(gold['items']))
    print('wrote F6_GOLD_1P_AND_F5_1N.md')
    return 0


if __name__ == '__main__':
    sys.exit(main())
