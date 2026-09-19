#!/usr/bin/env python3
"""Phase 1W stack entry point = "1V round 2 + §2" (0 extra model calls).
1V round 2 = phase1v/trackA_loop/stack_1v.py: AG v4 + v5 refsubj rs_nom + TIP determiner rule.
§2 = phase1w/reader_nom.py: the agent reader v6 (variant from phase1w/s2_result.json 'chosen_variant';
None there = the 1V reader is left in place).
  decide(sk, ann, wtags, answer, reference, variant='primary', flags=None, extra=('rs_nom',))  -> AG verdict
  final_accept(row, extra=('rs_nom',), tip=True)  -> (accept, layer); row['ag'] must come from decide()."""
import os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(HERE)
for p in (HERE, os.path.join(TO, 'phase1v', 'trackA_loop')):
    if p not in sys.path:
        sys.path.insert(0, p)
import stack_1v as S                                                           # noqa: E402
import reader_nom as R                                                         # noqa: E402
EXTRA = ('rs_nom',)
READER_VARIANT = R._default()


def decide(sk, ann, wtags, answer, reference, variant='primary', flags=None, extra=EXTRA):
    with R.installed(S.V3.V2, 'sk', READER_VARIANT):
        return S.decide(sk, ann, wtags, answer, reference, variant, flags, extra)


def final_accept(row, extra=EXTRA, tip=True):
    return S.final_accept(row, extra, tip)
