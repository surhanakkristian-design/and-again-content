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
## Stage 3 (item set + blind writers) - 21.9.2026
- make_set.py: seed 20260921 (per level seed+index), 25/25/25/25 from unique src, 2F probe 60 excluded by Slovak text (all 60 found); set/sentences.jsonl sha 20d62acfec9222a47f8626ad4352e804b668fff4f4b8207dd49b32ad3c1167aa. Not opened by run_2i.py.
- writers/run_writers.py: 4 headless opus sessions (2H recipe: zsh -ic token, nohup, --output-format json), one per level, identical template (sha 68105f3dc611894e..., writers/PROMPTS.sha256), writers saw wid/slovak/level/topic only.
- Validator bug (sorted(types) compared to unsorted TYPES) rejected every valid output, so each session was retried once (8 sessions spawned, all rc 0, 1 turn). Fixed; stored attempt-1 outputs re-validated at 0 cost and used (attempt 2 also valid, unused). DEFECTS 14.
- set/answers.jsonl: 900 answers (500 correct, 400 wrong: T/W/M/S 100 each), 0 dedupes, agent-drop natural 5; sha 37f81c61d57d07ac... No labels.
- Writer tokens (8 sessions): input 16, output 128772, cache read 169812, cache creation 90526, total 389,126 (used attempts 194,337). Agent ~60k est. 0 Gemini calls.
- Cumulative ~829,126 of 3,000,000. Projection: judge 4 x ~245 items, cap 400k each (expected ~150-250k each, ~0.8M; worst 1.6M) + run (0 Claude, orchestration ~50k) + analysis/report ~200k -> expected ~1,879,126, worst ~2,679,126 (within 3,000,000).
