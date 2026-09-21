## Stage 1 (context, SHA baseline, Part 0) — 21.9.2026
- Wrote CONTEXT.md (frozen 1W map, lk sites, the quoted "ALREADY VERIFIED" line lib_prev.py:234-235, 2H headless recipe, data/exclusions, uploads), SHA_before.txt (3,256 files, generator sha_tree.sh), part0.py -> upload/ (SK 0 / CZ 50 v fixes, CZ exercise_id -> int), PART0_RESULT.md, upload/UPLOAD_README.md.
- 0 Gemini calls, 0 headless sessions. Claude tokens this stage ≈130k (estimate; harness figure authoritative). Cumulative ≈130k of 3,000,000; projection stays within budget.
- Note: phase1p/access_log.jsonl and run_1p.log were already modified in the working tree since 19.9 (pre-2I); SHA_before captures that state.
## Stage 2 (build both stacks, runner, tests, freeze) - 21.9.2026 - STOPPED
- Built: make_tonly.py -> tonly/ (3 copies, 11 edits + __file__ pins), tonly.diff, TONLY_CHANGES.md, stack_frozen.py,
  stack_tonly.py, run_2i.py, test_2i.py, DEFECTS.md (9 items).
- STOP_stage2.md: the frozen chain crashes on production annotations (alt is a list; 1W needs the 2F adapter shape).
  Suite did not complete; nothing frozen. 0 Gemini calls, 0 headless sessions.
- Claude tokens this stage ~160k (estimate; harness figure authoritative). Cumulative ~290k of 3,000,000.
## Stage 2b (2F adapter, write isolation, tests, freeze) - 21.9.2026
- adapter_2f.py (verbatim p3_probe.py 55, 121-128, 286-294, 297-322 + convert) wired into stack_frozen.from_2i; stack_tonly.strip_row; write_guard.py; test_2i (k)(w)(z sha tree) added; harness fix (SHA_before newline parse).
- test_2i: 32/32 PASS, 0 model calls; probe data reproduced byte-identical 60/60; 0 chain writes outside phase2i.
- FROZEN_SHA.txt + FREEZE_COMMIT.txt. Claude tokens this stage ~90k (estimate). Cumulative ~380k of 3,000,000.
