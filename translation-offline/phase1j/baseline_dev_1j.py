#!/usr/bin/env python3
"""Phase 1j — apparatus check: replay the FROZEN Phase 1i configuration on the NEW DEV side.

ZERO model calls. The frozen config is P-E4b + TIP counted as a rejection + Task B fixes
(backfill_s_ids, lock_fix syn/gender/contraction) + Task C guard {F4v3} (phase1i/FROZEN_CONFIG.json).
Every L3 verdict is taken from the stored Phase 1i ledgers (taskE/calls.jsonl for the 1i DEV items,
taskF/holdout_calls.jsonl for the 1i HOLDOUT items) — both were produced with the identical P-E4b prompt
builder and the identical per-item inputs, so the prompt text is byte-identical and nothing is called.

usage: PYTHONDONTWRITEBYTECODE=1 python3 phase1j/baseline_dev_1j.py
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(HERE)
P1I = os.path.join(TO, 'phase1i')
sys.path.insert(0, P1I)
sys.path.insert(0, HERE)

import pipeline_1i as P                                                     # noqa: E402
from loader_1j import load_items, load_annotations                          # noqa: E402

PURPOSE = 'Phase 1j apparatus check: replay the frozen 1i config on the new DEV side, 0 calls'
recs = load_items('dev', purpose=PURPOSE)
ann = load_annotations('dev', purpose=PURPOSE)

import checker_1i as C                                                      # noqa: E402
for s, a in ann.items():
    C._ANN[int(s)] = a.get('hygienised', a)
for r in recs:
    C.SK_OF[r['sid']] = r['sk']

P._ST = {'C': C, 'recs': recs, 'ann': ann, 'side': 'dev1j', 'base_decide': C.decide,
         'decide': C.decide, 'b_fix': False, 'guards': (), 'reports': {}}
cfg = json.load(open(os.path.join(P1I, 'FROZEN_CONFIG.json'), encoding='utf-8'))
VARIANT = cfg['prompt_variant']
st = P.configure(b_fix=True, guards=tuple(cfg['c_guards']), side='dev1j')

# ---------------------------------------------------------------- stored P-E4b verdicts (no calls)
LEDGERS = [os.path.join(P1I, 'taskE', 'calls.jsonl'),
           os.path.join(P1I, 'taskF', 'holdout_calls.jsonl'),
           os.path.join(P1I, 'taskF', 'dev_calls.jsonl')]
have, fails, src = {}, set(), collections.Counter()
for p in LEDGERS:
    if not os.path.exists(p):
        continue
    h, f, _ = P.ledger_verdicts(p)
    for (v, i), val in h.items():
        if v == VARIANT:
            have[i] = val
            src[os.path.basename(p)] += 1
    for (v, i) in f:
        if v == VARIANT and i not in have:
            fails.add(i)

l3 = sorted(i for i, v in P.run_pipeline(st, {}).items() if v['reached_l3'])
misses = sorted(i for i in l3 if i not in have and i not in fails)
vm = {i: have[i] for i in l3 if i in have}
res = P.run_pipeline(st, vm, tip_reject=(cfg['tip_scoring'] == 'tip_reject'))
m = P.metrics(st, res)

out = {'side': 'phase1j DEV (70 sentences)', 'config': {k: cfg[k] for k in
       ('prompt_variant', 'tip_scoring', 'c_guards', 'b_flags', 'model', 'generationConfig')},
       'n_items': len(recs), 'l3_items': len(l3), 'model_calls_made': 0,
       'cache_misses_l3_without_stored_verdict': len(misses), 'cache_miss_ids': misses[:20],
       'stored_failed_calls_at_l3': len([i for i in l3 if i in fails]),
       'verdict_source_rows': dict(src),
       'coverage': m['coverage'], 'fa': m['fa'], 'fa_by_type': m['fa_by_type'],
       'fa_by_layer': m['fa_by_layer'], 'fa_by_half': m['fa_by_half'],
       'model_verdict_split_at_l3': dict(collections.Counter(vm.get(i) or 'none' for i in l3)),
       'failed_items_no_verdict': m['failed_items'],
       'false_acceptances': m['fa_items'], 'fr_by_layer': m['fr_by_layer'],
       'items_from_1i_dev': sum(1 for r in recs if r.get('side_1i') == 'dev'),
       'phase1i_dev_reference': cfg['dev_numbers']}
json.dump(out, open(os.path.join(HERE, 'split', 'baseline_dev.json'), 'w', encoding='utf-8'),
          indent=1, ensure_ascii=False)

print('items %d  L3 %d  cache misses %d  failed-call items at L3 %d'
      % (len(recs), len(l3), len(misses), out['stored_failed_calls_at_l3']))
print('coverage %(k)d/%(n)d = %(pct)s %% CI %(ci)s' % m['coverage'])
print('FA       %(k)d/%(n)d = %(pct)s %% CI %(ci)s' % m['fa'])
print('FA by type', {t: '%d/%d' % (m['fa_by_type'][t]['k'], m['fa_by_type'][t]['n'])
                     for t in ('T', 'W', 'M', 'S')})
print('FA by layer', m['fa_by_layer'], ' FR by layer', m['fr_by_layer'])
print('verdict rows reused from', dict(src))
