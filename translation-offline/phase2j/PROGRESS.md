# Phase 2J PROGRESS

## PLAN (written by S1, 21.9.2026)
Budget: Claude 4,000,000 tokens (harness). Gemini: HARD CAP 1,200 counted calls (A3+B4+D), $1.00; ledger GEMINI_LEDGER.json.
| stage | work | headless tok (proj.) | agent tok (proj.) | Gemini calls (proj.) |
|---|---|---|---|---|
| S1 | setup, SHA_before, stack copy, Part A deterministic (A1-A5) | 0 | ~150k | 0 |
| S2 | run_2j.py + test_2j.py, freeze, A3/A4 new L3 calls only | 0 | ~200k | 44 |
| S3 | Part C (F5 misses, C2 build if 0 cost, A2-level FA) | 0 | ~150k | 0 |
| S4 | B1 deterministic ref audit; B2 Slovak ref model audit (waves of 4 x N=100) | sized after wave 1 (<= remainder) | ~150k | 0 |
| S5 | B3 corrections -> phase2j/upload/; B4 closed-set re-score | 0 | ~150k | <= ~150 |
| S6 | Part D set + 4 blind writers | ~390k | ~100k | 0 |
| S7 | Part D judge (1 prompt, 4 sessions, 80 duplicates) | ~275k | ~100k | 0 |
| S8 | Part D run, opened once | 0 | ~100k | ~800 (cap 1,200 total) |
| S9 | analysis + report + SHA after | 0 | ~150k | 0 |
Reserve: D ~700k headless + ~400k orchestration. Fixed projection without B2: ~665k headless + ~1.25M agent = ~1.9M;
B2 gets at most 4.0M - 1.9M - 0.4M reserve = ~1.7M, measured on wave 1 before launching more.

## S1 — setup + Part A deterministic (0 Gemini calls, 0 headless tokens)
- SHA_before.txt: 3,256 files (phase2i/sha_tree.sh, phase2j excluded; phase1p dirty pair in the baseline).
- Copied 2I TRANSLATION-ONLY stack: stack_tonly.py (+ A2 hook, P2J_F4FIX), stack_frozen.py, adapter_2f.py, write_guard.py, tonly/.
- A1: cause = checker_1i.sk_features ending heuristics (checker_1i.py:552-563) reading nouns/adverbs as verbs; `after_prep`
  looks one token back (542-544): `po vidieckej ceste`, `v celom jeho živote`, `pri tomto plote` (-te -> 2pl), `príliš`
  (-š -> 2sg), `samozrejme` (-me -> 1pl). Path: decide 815-820 -> f4v2_subject_mismatch 608 -> sk_features 536. Not reported speech.
  All 44 F4v2 rejections of 2I are on the 5 sentences; the 20 judge-wrong ones are m/s/t/w variants, not subject errors.
- A2: phase2j/f4fix.py (PP prepositional-NP shadow + NV closed non-verb list), F4v2 only. 9/9 unit checks.
- A3: see partA/PART_A.md "A3 CORRECTION": 44 items un-fire (24 correct, 20 wrong), 0 new fires; **44 new L3 calls** needed
  (partA/NEW_L3_CALLS_S2.json). Stored-reply replay machinery validated (fix OFF: 800 requests, 0 missing, 0 diffs).
  DEFECT for S2: the stack hook patched the wrong checker_1i instance (fix ON replay = 2I); fix the hook, re-run partA.py.
- A4: 0 F4v2 decision changes on the 1W test set and on all phase1t/1u/1w item files (1S packet = closed 1Q set as re-used there);
  PASS, 0 new calls. (No phase1q/phase1s items.json with sentences.json exists; 1S labels live elsewhere - S2 may confirm.)
- A5: Czech reader (phase1v/trackC/cz_reader.py) has the SAME defect (`příliš` -> 2sg, x15 in the CZ upload); fix
  f4fix.build_fixed(CK, 'cz') changes 21/4,064 CZ rows (SK 128/4,064). Cost candidates to inspect: SK potrebuješ, bola; CZ byla, mluvila, dala.
- Files: f4fix.py, stack_tonly.py, partA/{partA.py, make_report.py, PART_A.md, partA_result.json, NEW_L3_CALLS_S2.json, *_stdout.txt, _run/}.
- Gemini calls: S1 0, cumulative 0. Headless tokens 0.
- SHA check S1: identical (3,256 files), diff empty
