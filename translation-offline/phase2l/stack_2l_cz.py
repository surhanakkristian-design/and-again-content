#!/usr/bin/env python3
"""Phase 2L Part D FROZEN Czech configuration (22.9.2026): the mirror of stack_2l.py (SOURCE-ONLY + B, TIP rejected).
Layers, in order (identical to Slovak): AG (stack_1w.decide = AG v4 + reader_nom v6, extra=(), reading the Czech V2/V3
bound by cz_assemble) -> F4v2 -> F4v3 (f4fix.build_fixed_v3(guards_c, Czech CK, 'cz'), input {sk: CZECH sentence,
answer}) -> L3 gemini-3.1-flash-lite judged against the CZECH sentence only (phase2k/spec/l3_system_cz.txt +
l3_user_cz.txt; SAME accept, TIP reject, DIFF reject) -> content check (content_check.py, language 'Czech', the CZECH
sentence + answer) on every L3-accepted answer; MISSING -> reject; a failed check call keeps the L3 verdict.
stack_source_cz.py = stack_source.py with only load() changed (cz_assemble.SUBS, tested).  No reference field is read."""
import os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import run_2l as R  # noqa: E402
import stack_source_cz as SCZ  # noqa: E402
R.K.S = SCZ                     # run_2k.run_items resolves S at call time -> the Czech stack
R.S = SCZ
SCZ_FILE = os.path.abspath(SCZ.__file__)
TIP_ACCEPT = False
LANG = 'cz'


def run(items, run_dir, stage, ledger_path=R.LEDGER, key=None, spend_dirs=()):
    assert R.K.S is SCZ
    return R.run_full(items, run_dir, stage, LANG, TIP_ACCEPT, ledger_path, key, spend_dirs)
