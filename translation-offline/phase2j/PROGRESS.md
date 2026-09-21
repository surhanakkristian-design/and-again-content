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

## S2 — hook fix + verb-loss narrowing + runner/tests; STOPPED at 0 cost (test_2j 11/12)
- Hook defect found: the decide the stack runs is the guards_c wrapper (pipeline_1i.configure -> guards_c.apply), whose
  globals are NOT checker_1i.__dict__ (probe: 0 calls reached the patched C.f4v2_subject_mismatch). Fix = f4fix.sweep():
  gc walk replacing the original f4v2_subject_mismatch in every namespace dict + closure cell; run after load, in
  post_build and before every pipeline_1i.run_pipeline (stack_tonly.py hook; POISON post_build chained).
- PROOF (partA.py re-run over the real stack path, 900 items): fix OFF = 2I exactly (800 reach L3, 0 missing, 0 diffs);
  fix ON: 843 reach L3, **43 new requests** (44 items un-fire; one of them shares a request hash with a stored 2I
  reply), changed = exactly the 44 (24 judge-correct, 20 judge-wrong), 0 other items changed. Bounds unchanged:
  coverage 443/497 (all rejected) .. 466/497 = 93.76 % [91.26, 95.72] with 23 pending correct; FA 19/403 .. 39/403.
- Verb-loss (S1 candidates): real. f4fix.is_verb_head(): the PP head is not shadowed when it is an l-participle
  (-l/-la/-lo/-li/-ly), a 2sg -š form or byt/mat -> returns to the 2I reading (can never add a signal). Upload scan:
  SK 125/4,064 rows change (was 128), CZ 18/4,064 (was 21); every potrebuješ/bola/byla/mluvila/dala signal kept, no
  removed signal is verb-like (partA/T11_verbloss.json). 9/9 unit cases still pass; A4 1W + 1T/1U/1W files 0 changes.
- A4 1S packet: phase1s/taskA/rows_1s.json (1,080 rows, all with Slovak) + phase1s/taskC/judge/packet.json (183):
  F4v2 fire changes 0, verdict changes 0 -> PASS, 0 calls (partA/GATE_1S.json, partA/gate1s.py).
- Built: run_2j.py (gemini transport = run_2i_base.py byte copy of 2I run_2i.py, one stack, phase ledger cap
  1,200 - other stages, spend $1.00, --seed-ledger, --expect-needed, abspath everywhere; claude spawner = 2H recipe,
  usage-limit STOP file, envelope-only rate limit, resume, token-cap reservation), test_2j.py (13 checks), s2_chain.sh.
- STOP: the second suite run (inside s2_chain.sh, before freeze) ended 11/12 -> STOP_S2.md, 0 model calls, no freeze,
  no run_S2. First run failed only T8 (subset-only artefact: A:250:c3 already reaches L3 with fix OFF in the 45-item
  subset); T8 was relaxed to "the 44 all reach L3, nothing else changes". Failing check of the second run:
    FAIL  T8 A2 hook on the REAL stack path: fix ON vs OFF prepare on the 5 sids -> exactly the 44 new L3 requests
          AssertionError(['A:250:c3']) Traceback (most recent call last):
      File "/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j/test_2j.py", line 21, in deco
        fn(); RES.append((name, 'PASS', ''))
  Agent tool budget (12) exhausted, so not re-run. NEXT (S2 resume): fix that check, run
  zsh /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j/s2_chain.sh (tests -> freeze -> run_2j --expect-needed 43 -> partA/a3_final.py -> SHA).
- Gemini calls: S2 0, cumulative 0 (GEMINI_LEDGER.json {"S1": 0}). Headless tokens 0.
- SHA check S2: diff lines 122 (SHA_after_S2.txt, SHA_diff_S2.txt)

## S2b — resume of S2 (21.9.2026)
- SHA question: NO real write to any earlier phase. SHA_diff_S2's 122 lines were a generator mismatch (the chain's own find
  included the 121 phase2i files that S1's sha_tree.sh prunes). S1 generator re-run: 3,256 files, diff empty; phase2i git-clean;
  no __pycache__ outside phase2j; nothing restored. partA/SHA_INCIDENT_S2.md. s2_chain.sh now uses
  `zsh phase2i/sha_tree.sh | grep -v '  phase2j/'` and literal git -C calls (e5db040 committed all uncommitted S2 files).
- T8 compares request hashes: 44 items -> 43 unique requests (A:250:c3 decided by AG before L3), none existed with fix OFF,
  fix-ON subset requests = fix-OFF + exactly those. test_2j 12/12 PASS.
- s2_chain.sh under nohup: tests 12/12 -> freeze (ce8b28e, FREEZE_COMMIT 583eced) -> run_S2: 843 requests, 800 seeded 2I
  replies, 43 counted calls, $0.0057, 0 uncounted -> a3_final.py. Results commit 496fc75.
- A3 FINAL (closed-set re-score, labelled): coverage 443/497 = 89.13 % [86.06, 91.73], FA 19/403 = 4.71 % [2.86, 7.26],
  both UNCHANGED. The 44 un-fire F4v2 but are all rejected again: F4v3 27 (22 correct, 5 wrong), L3 DIFF 16 (15 wrong, 1 correct),
  AG 1 (correct). => F4v3 very likely carries the same sk_features misreading; f4fix does not patch it. NEXT: F4v3 reasons on
  the 27, extend f4fix + tests + re-freeze; re-score reuses run_S2 replies at 0 cost (ceiling 465/497 = 93.56 %, FA risk +5).
- Gemini calls: S2 43, cumulative 43 of 1,200 (GEMINI_LEDGER.json {"S1": 0, "S2": 43}). Headless tokens 0.
- SHA check S2b: S1 generator, 3,256 files, diff empty (SHA_after_S2.txt; SHA_diff_S2.txt 0 lines).
