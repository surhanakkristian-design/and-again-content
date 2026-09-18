#!/usr/bin/env python3
"""Phase 1j Task A — ZERO-CALL offline measurement of the F4p consultation on the Phase 1j DEV side.

Replays the frozen Phase 1i configuration (baseline_dev_1j.py) from the stored P-E4b verdicts, then asks
what f4p_guard would do to the items that baseline ACCEPTED.  A guard can only ever turn an acceptance into
a rejection, so the effect is exactly: FA caught (accepted & really wrong) and correct answers wrongly
rejected (accepted & really correct).  Writes results_offline.json + TASK_A_OFFLINE.md.
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P1J = os.path.dirname(HERE)
TO = os.path.dirname(P1J)
P1I = os.path.join(TO, 'phase1i')
sys.path.insert(0, P1I)
sys.path.insert(0, P1J)
sys.path.insert(0, HERE)

import pipeline_1i as P                                                    # noqa: E402
from loader_1j import load_items, load_annotations, load_sentences         # noqa: E402
import p_chain as PC                                                       # noqa: E402

PURPOSE = 'Task A offline F4p measurement on DEV (0 model calls)'
recs = load_items('dev', purpose=PURPOSE)
ann = load_annotations('dev', purpose=PURPOSE)
sents = load_sentences('dev', purpose=PURPOSE)

import checker_1i as C                                                     # noqa: E402
for s, a in ann.items():
    C._ANN[int(s)] = a.get('hygienised', a)
for r in recs:
    C.SK_OF[r['sid']] = r['sk']
P._ST = {'C': C, 'recs': recs, 'ann': ann, 'side': 'dev1j', 'base_decide': C.decide, 'decide': C.decide,
         'b_fix': False, 'guards': (), 'reports': {}}
cfg = json.load(open(os.path.join(P1I, 'FROZEN_CONFIG.json'), encoding='utf-8'))
st = P.configure(b_fix=True, guards=tuple(cfg['c_guards']), side='dev1j')
have = {}
for p in ('taskE/calls.jsonl', 'taskF/holdout_calls.jsonl', 'taskF/dev_calls.jsonl'):
    fp = os.path.join(P1I, p)
    if os.path.exists(fp):
        h, _f, _r = P.ledger_verdicts(fp)
        have.update({i: v for (var, i), v in h.items() if var == cfg['prompt_variant']})
l3 = sorted(i for i, v in P.run_pipeline(st, {}).items() if v['reached_l3'])
res = P.run_pipeline(st, {i: have[i] for i in l3 if i in have},
                     tip_reject=(cfg['tip_scoring'] == 'tip_reject'))
m = P.metrics(st, res)

# ---------------------------------------------------------------- p chains
pmap = PC.annotate(dict(ann), sents, out_path=os.path.join(HERE, 'annotations_p_dev.json'))
sk_of = {str(s['sid']): s['sk'] for s in sents}
ref_of = {str(s['sid']): s['reference'] for s in sents}
g_of = {str(s['sid']): s.get('g') for s in sents}
GOLD = {  # hand gold, read off the Slovak by the agent (main-clause subject). '?'= genuinely open.
 '224': '?sg', '1018': '3sg', '1452': '3sg', '2389': '3sg', '2783': '3sg', '3937': '3sg', '4449': '3sg',
 '5971': '3sg', '6265': '3sg', '6275': '3pl', '6365': '3sg', '6830': '3pl', '6884': '3sg', '6971': '3pl',
 '6985': '3sg', '7037': '3sg', '7444': '3sg', '7533': '3sg', '7687': '3pl', '7752': '3sg', '7910': '3sg',
 '8017': '3sg', '8020': '3sg', '8293': '3sg', '8465': '3pl', '8756': '3sg', '8799': '3sg', '8812': '3sg',
 '8824': '3sg', '8920': '3sg', '9007': '3sg', '9495': '3sg', '9498': '3sg', '9552': '3sg', '9602': '3sg',
 '9607': '3sg', '9687': '3sg', '9913': '?sg', '10013': '3sg', '10043': '3sg', '10116': '3sg',
 '10124': '3sg', '10138': '3sg', '10167': '3sg', '10179': '3sg', '10366': '3sg', '10574': '3sg',
 '10734': '3sg', '11610': '3sg', '13175': '3sg', '13395': '3sg', '14266': '3pl', '14779': '3sg',
 '15437': '1pl', '15954': '3sg', '16261': '3sg', '16403': '3sg', '20702': '3sg', '21124': '3sg',
 '21467': '2sg', '22427': '3sg', '23360': '2sg', '23878': '3sg', '24101': '3pl', '24733': '2sg',
 '25921': '3pl', '26084': '3sg', '27628': '3pl', '29691': '3sg', '31648': '3sg'}
print('--- per-sentence p (DEV) ---')
for s in sents:
    sid = str(s['sid'])
    p = pmap[sid]
    print('%-6s %-2s %s\n        p=%s | %s' % (
        sid, 'g' if g_of[sid] else '-', s['sk'],
        (('%s%s/%s' % (p['person'] or 'open', p['number'] or 'open', p['gender'] or '-')) if p else 'NONE'),
        (p['evidence'] if p else 'no usable signal / vetoed')))

n_chain = sum(1 for v in pmap.values() if v)
amb = sorted([sid for sid, v in pmap.items() if not v], key=int)
reasons = {str(s['sid']): PC.explain_p(s['sk'], ann.get(str(s['sid'])))[1] for s in sents}
hand = {'agree': [], 'conservative': [], 'error': []}
for sid, gold in GOLD.items():
    p = pmap[sid]
    gp, gn = (None if gold[0] == '?' else int(gold[0])), (None if gold[1:] == '?' else gold[1:])
    if not p:
        hand['conservative'].append((sid, gold, 'NONE'))
        continue
    got = '%s%s' % (p['person'] or '?', p['number'] or '?')
    if (p['person'] and gp and p['person'] != gp) or (p['number'] and gn and p['number'] != gn):
        hand['error'].append((sid, gold, got, p['evidence']))
    elif (gp and not p['person']) or (gn and not p['number']):
        hand['conservative'].append((sid, gold, got))
    else:
        hand['agree'].append((sid, gold, got))

# ---------------------------------------------------------------- F4p on the accepted items
by_id = {r['item_id']: r for r in recs}
caught, wrong_rej, untouched_fa = [], [], []
fa_ids = {x['id'] for x in m['fa_items']}
for iid, row in res.items():
    if not row.get('accepted'):
        continue
    r = by_id[iid]
    sid = str(r['sid'])
    p = pmap.get(sid)
    rej, reason = PC.f4p_guard(r['answer'], p, ann.get(sid))
    rec = {'id': iid, 'sid': r['sid'], 'type': r.get('wrong_type'), 'sk': r['sk'],
           'answer': r['answer'], 'p': p and {k: p[k] for k in ('person', 'number', 'gender', 'subject')},
           'evidence': p['evidence'] if p else None, 'reason': reason, 'layer': row.get('layer')}
    if rej and r['judged'] == 'wrong':
        caught.append(rec)
    elif rej and r['judged'] == 'correct':
        wrong_rej.append(rec)
    elif iid in fa_ids:
        untouched_fa.append(rec)

cov_k, cov_n = m['coverage']['k'], m['coverage']['n']
fa_k, fa_n = m['fa']['k'], m['fa']['n']
new_cov, new_fa = cov_k - len(wrong_rej), fa_k - len(caught)
by_type = collections.Counter(x['type'] for x in caught)
out = {'hand_check': {k: len(v) for k, v in hand.items()},
       'hand_check_errors': hand['error'], 'ambiguous_reasons': {s: reasons[s] for s in amb},
       'baseline': {'coverage': m['coverage'], 'fa': m['fa'], 'fa_by_type': m['fa_by_type']},
       'p_chain': {'dev_sentences': len(pmap), 'with_chain': n_chain, 'ambiguous': len(amb),
                   'ambiguous_sids': amb},
       'f4p_on_dev': {'fa_caught': len(caught), 'fa_caught_by_type': dict(by_type),
                      'correct_wrongly_rejected': len(wrong_rej),
                      'coverage_after': '%d/%d = %.2f %%' % (new_cov, cov_n, 100.0 * new_cov / cov_n),
                      'fa_after': '%d/%d = %.2f %%' % (new_fa, fa_n, 100.0 * new_fa / fa_n)},
       'caught_items': caught, 'wrongly_rejected_items': wrong_rej,
       'fa_not_caught': [{'id': x['id'], 'type': x['type'], 'reason': x['reason']} for x in untouched_fa]}
json.dump(out, open(os.path.join(HERE, 'results_offline.json'), 'w', encoding='utf-8'),
          indent=1, ensure_ascii=False)
print('\n=== p chains %d/%d, ambiguous %d' % (n_chain, len(pmap), len(amb)))
print('=== F4p: FA caught %d %s | correct wrongly rejected %d' % (len(caught), dict(by_type), len(wrong_rej)))
print('=== coverage %d/%d -> %d/%d | FA %d/%d -> %d/%d'
      % (cov_k, cov_n, new_cov, cov_n, fa_k, fa_n, new_fa, fa_n))
for x in caught:
    print('CAUGHT  ', x['id'], x['type'], '|', x['sk'], '|', x['answer'], '|', x['reason'])
for x in wrong_rej:
    print('FALSEREJ', x['id'], '|', x['sk'], '|', x['answer'], '|', x['reason'])
for x in untouched_fa:
    print('MISSED  ', x['id'], x['type'], '|', x['sk'], '|', x['answer'], '|', x['reason'])
print('=== hand-check: agree %d, conservative %d, ERRORS %d' % (len(hand['agree']), len(hand['conservative']), len(hand['error'])))
for e in hand['error']:
    print('  ERROR', e)

L = []
L.append('# Task A — the `p` (person / number) chain: offline DEV measurement\n')
L.append('Agent A, 18 Sept 2026. **Zero model calls** — the L3 verdicts are the stored Phase 1i P-E4b')
L.append('replies, exactly as `phase1j/baseline_dev_1j.py` uses them. DEV only; the holdout was touched')
L.append('once, COUNT ONLY (see `phase1j/access_log.jsonl`).\n')
L.append('## 1 Coverage of the chain\n')
L.append('| side | sentences | with a `p` chain | ambiguous (None) |')
L.append('|---|---|---|---|')
L.append('| DEV | %d | %d | %d |' % (len(pmap), n_chain, len(amb)))
L.append('| all 140 (count-only pass) | see ALL140 below | | |\n')
L.append('Distribution of the DEV chains: %s\n' % dict(collections.Counter(
    '%s%s' % (v['person'] or '?', v['number'] or '?') for v in pmap.values() if v)))
L.append('### The %d ambiguous DEV sentences and why\n' % len(amb))
L.append('| sid | reason |')
L.append('|---|---|')
for sid in amb:
    L.append('| %s | %s |' % (sid, reasons[sid]))
L.append('\n## 2 Hand-check (every DEV sentence read against the Slovak by the agent)\n')
L.append('Gold = the person/number of the MAIN-clause subject as the Slovak states it.')
L.append('`conservative` = the script asserts less than the gold (None, or an open feature) — no false claim.')
L.append('`error` = the script asserts a person or number the Slovak does not have.\n')
L.append('| outcome | n |')
L.append('|---|---|')
L.append('| agree | %d |' % len(hand['agree']))
L.append('| conservative (script says less) | %d |' % len(hand['conservative']))
L.append('| **error** | **%d** |' % len(hand['error']))
for e in hand['error']:
    L.append('\n- ERROR sid %s: gold %s, script %s — %s' % e)
L.append('\n## 3 The F4p consultation alone, on top of the frozen 1i baseline replay\n')
L.append('Baseline (unchanged apparatus): coverage %d/%d, FA %d/%d.' % (cov_k, cov_n, fa_k, fa_n))
L.append('F4p can only turn an acceptance into a rejection, so it is applied to the accepted items.\n')
L.append('| | baseline | + F4p |')
L.append('|---|---|---|')
L.append('| coverage | %d/%d = %.2f %% | %d/%d = %.2f %% |' % (cov_k, cov_n, 100.0*cov_k/cov_n, new_cov, cov_n, 100.0*new_cov/cov_n))
L.append('| FA | %d/%d = %.2f %% | %d/%d = %.2f %% |' % (fa_k, fa_n, 100.0*fa_k/fa_n, new_fa, fa_n, 100.0*new_fa/fa_n))
L.append('\nFA caught by type: %s (baseline FA by type T %d / W %d / M %d / S %d).' % (
    dict(by_type), m['fa_by_type']['T']['k'], m['fa_by_type']['W']['k'], m['fa_by_type']['M']['k'],
    m['fa_by_type']['S']['k']))
L.append('Correct answers wrongly rejected: **%d**.\n' % len(wrong_rej))
L.append('### False acceptances caught (id, type, Slovak, answer, p, reason)\n')
for x in caught:
    L.append('- `%s` **%s** — SK: *%s* — answer: *%s* — p = %s — %s' % (
        x['id'], x['type'], x['sk'], x['answer'], x['p'], x['reason']))
L.append('\n### Correct answers wrongly rejected\n')
L.append('- none' if not wrong_rej else '')
for x in wrong_rej:
    L.append('- `%s` — SK: *%s* — answer: *%s* — p = %s — %s' % (x['id'], x['sk'], x['answer'], x['p'], x['reason']))
L.append('\n### The %d baseline false acceptances F4p does NOT catch\n' % len(untouched_fa))
for x in untouched_fa:
    L.append('- `%s` %s — *%s* — %s' % (x['id'], x['type'], x['answer'], x['reason']))
L.append('\n## 4 Reading\n')
L.append('The DEV side contains only %d subject-recast false acceptances out of %d; the Phase 1i HOLDOUT'
         % (len(caught), fa_k))
L.append('had 10 of 23. F4p is therefore measured here mainly for its COST (correct answers rejected: %d),'
         % len(wrong_rej))
L.append('and that cost is what the DEV side can establish at this size. The prompt line `p_prompt` is not')
L.append('measurable offline at all — it needs the DEV run of agent R.\n')
open(os.path.join(HERE, 'TASK_A_OFFLINE.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('wrote TASK_A_OFFLINE.md')
