#!/usr/bin/env python3
"""Phase 2L FROZEN configuration (Part C, 22.9.2026): SOURCE-ONLY + B, TIP rejected.
= the 2K SOURCE-ONLY stack (stack_source.py, byte copy of phase2k/stack_source.py: AG / F4v2 / F4v3 source-side guards,
then L3 gemini-3.1-flash-lite judged against the SOURCE sentence only) + the Part B content check (content_check.py,
spec/content_check_prompt.txt) on every answer L3 accepted; MISSING -> reject; a failed check call keeps the L3 verdict.
TIP handling: L3 TIP is REJECTED.  Chosen on the CLOSED-SET, IN-SAMPLE Slovak re-score (partC/partC.md)."""
import os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import run_2l as R  # noqa: E402
TIP_ACCEPT = False


def run(items, run_dir, stage, lang, ledger_path=R.LEDGER, key=None, spend_dirs=()):
    return R.run_full(items, run_dir, stage, lang, TIP_ACCEPT, ledger_path, key, spend_dirs)
