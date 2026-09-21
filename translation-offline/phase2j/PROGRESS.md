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

## S2c — F4v3 extension of Part A (21.9.2026)
- A1: F4v3 (phase1i/taskC/guards_c.py:339 -> sk_features_v3 :323 -> C.sk_features :328) = SAME sk_features misreading; all 27
  fire on the A1 false signals, extra number signal used 0x; F4v3 sits in the guards_c wrapper after L3 (:127-142).
- A2: f4fix.build_fixed_v3 / v3_patch / sweep3 (P2J_F4V3FIX, default 1). T14 + T15 added; test_2j 14/14 PASS (T8 now takes
  the 44 from 2I results, NEW_L3_CALLS_S2.json holds the 43 needed jids). Catches 21, cost 1 (A:250:m), 5 move to L3:TIPrej.
- A3 closed-set re-score: 443/497 = 89.13 % [86.06, 91.73] -> 464/497 = 93.36 % [90.80, 95.39]; FA 19/403 = 4.71 % [2.86, 7.26]
  -> 20/403 = 4.96 % [3.06, 7.56]. run_S2c: 843 requests all seeded (partA/seed_2I_S2.jsonl = 2I + run_S2 ledgers), 0 new calls.
- A4: 1W 900 / 1S rows 1,080 / 1S packet 183: 0 F4v3 fire changes -> PASS, 0 calls. A5: Czech path has no F4v3.
- Freeze d9b806d1c06093d7a360b82b84d97a787eec164f. Honest note: a zsh word-split bug ($G) skipped the pre-run commit; the 0-call run used exactly the files hashed
  in FROZEN_SHA.txt before it (shasum -c after = 0 mismatches), committed as the freeze immediately after.
- Files: f4fix.py, test_2j.py, partA/{gate_f4v3.py, GATE_F4V3.json, a3_final_s2c.py, A3_FINAL_S2c.{md,json}, seed_2I_S2.jsonl},
  run_S2c/, SHA_after_S2c.txt, SHA_diff_S2c.txt.
- Gemini calls: S2c 0, cumulative 43 of 1,200 (GEMINI_LEDGER.json {"S1": 0, "S2": 43, "S2c": 0}). Headless tokens 0.
- SHA check S2c: S1 generator, 3,256 files, diff empty.
- NEXT (S3): Part C; the one new FA (A:250:m, dropped adjective) belongs to C's dropped-content-word class.

## S3 — Part C (21.9.2026; 0 Gemini calls, 0 headless tokens; closed-set analysis on run_S2c)
- C1: current FAs 20/403 = 2I's 19 + A:250:m; dropped content word 16 (2I 15 + A:250:m), grammar 2, wrong word 1, doubtful 1.
  ONE path for all 20: F5 needs an order-preserving subsequence; `_subseq_positions` returns None at checker_1i.py:669,
  loop `continue` :719, trace "not a subsequence of any accepted variant"; span_information (:683) never reached. Causes:
  every FA sentence has exactly 1 reference (closed set 873/900 single-ref) AND every M answer also swaps >=1 token
  (must/has to, put on/wore, incredible/unbelievable ...). Secondary: now/today/totally sit in FUNCTION/INFO_FUNC.
- C2: no SK->EN lemma/bilingual resource in the repo (only annotation `alt`). Sized V1-V5 (content missing / net deficit /
  pure deletion mod synonyms / word in all refs / F5 relaxed): closed-2I cost min 16 (V3/V4 catch 3), V5 catch 5 cost 34;
  1W V4 3/0 but 2I 16 -> NOT BUILT, no test, no re-freeze. 1S packet (183) has no refs/labels and no overlap with rows_1s
  -> not sizable. Needed: a per-sentence Slovak content-word -> English map (Part B's audit could supply it).
- C3: A2 FA = the same 8/100 = 8.00 % [3.52, 15.16] on 2I and current stack: 7 dropped (now, today, totally, Look!, off the
  plant, hot, in the room) + 1 doubtful (honestly); all M, L3 SAME, single-ref, non-subsequence. Levels now A1 2/101,
  A2 8/100, B1 7/102, B2 3/100.
- Files: partC/{partC.py, partC_result.json, PART_C.md}, SHA_after_S3.txt, SHA_diff_S3.txt.
- Gemini calls: S3 0, cumulative 43 of 1,200 (GEMINI_LEDGER.json S3: 0). Headless tokens 0.
- SHA check S3: S1 generator, 3,256 files, diff empty.
- NEXT (S4): Part B; B's reference audit is the only route to a deterministic dropped-word rule (C2).

## S4 — Part B1 + B2 launch (21.9.2026; 0 Gemini calls)
- B1 (partB/b1_audit.py, 0 calls): reader_nom.read (variant from phase1w s2_result) with f4fix.build_fixed sk_features swapped
  into the reader's CK; Czech = cz_reader.build() + f4fix.build_fixed(CK,'cz'). English = subject pronoun of the aligned sentence
  (discourse words / punctuation before it only; leading subordinate clause skipped to its comma; quotes ignored).
  Rules: person, number (`you` never number), gender_contradiction (3sg m/f), gender_fixed_open (3sg, gender open, no explicit
  subject, he/she) -> B3 adds other gender, neuter_as_he_she = REVIEW only. 1sg/2sg/1pl/2pl past: gender is on the participle
  only and English I/you/we carry none -> never flagged. 3sg m/f + it not flagged.
- Two reader defects found (measuring apparatus) and repaired IN THE AUDIT ONLY: R1 reader leaves gender None on 3sg past
  (Povedal -> 3/sg/None) -> gender from the l-participle (753 SK / 730 CZ rows); R2 CZ bys/jsi/bych/jsem/bychom/jsme/byste/jste
  not read (-> 3sg; 49 rows overridden), SK `si` beside an l-participle (`mal by si`) -> person open (57). Before repairs 356/302
  flags (gender_fixed_open 253/184, mostly false).
- Result: SK rows read 1,824/4,064 (2,240 reader abstain = not compared), refs compared 1,169/4,341; flags 92 on 83 rows:
  person 44, number 19, neuter_as_he_she 15, gender_fixed_open 9, gender_contradiction 5.
  CZ read 1,782, refs compared 1,097/4,313; flags 107 on 99 rows: person 53, number 16, gender_contradiction 15,
  neuter_as_he_she 13, gender_fixed_open 10. Residual reader noise remains in the flags (e.g. `Udrie ho` read 1sg,
  `ťa ... netrafila` object read as subject, CZ `Kdybych měl` still 3sg when the clause is split) -> S5: treat B1 flags as
  candidates; act on SK only where B2 agrees; CZ flags need a per-item look before any B3 change.
  Files: partB/{b1_audit.py, B1.md, B1_result.json, B1_flags_sk.jsonl, B1_flags_cz.jsonl}.
- B2 (partB/audit/audit_2j.py): 41 packets of N=100 (seed 20260921, all levels mixed, items = id + Slovak + stored refs only),
  PROMPT.txt sha256 ccf78e156ec1f6fb914f88731992469a3b7ec85e76af40dbae357a2332f0eea4 (PROMPT.sha256, PACKETS.json has per-packet
  prompt sha); classes F/A/N/W/O with span, alt for N/W; validator hard (JSON, packet id, ids in order, refs count, class, alt)
  vs soft (span not verbatim); invalid -> one retry <pid>_r1. Waves of 4 threads, run_2j.run_session (2H recipe, opus,
  max_turns 3, zsh -ic token), usage-limit = STOP_usage_limit.md hard stop, cap 1,500,000 by reservation
  (spent + #todo x max packet cost). test_2j T16 added; suite 15/15 PASS (test_2j_output_S4.txt) before any spawn.
- Driver launched under nohup (pid 23767, cwd partB/audit, log partB/audit/driver.log). WAVE 1 (partB/audit/WAVE1.json):
  4/4 valid, per session p000 43,755 / p001 44,441 / p002 45,494 / p003 43,921; spent 177,611; mean 44,403, max 45,494.
  Projection all 41 = 1,860,889 (> cap) -> full audit does NOT fit; estimate 7 further waves fit = 8 waves = 32 packets =
  3,200 sentences, stop before wave 9 (~1.46M). Czech sized, not run: 41 packets, 707,178 prompt chars (SK 710,993),
  ~1.81M (mean) - 1.86M (max) tokens.
- NEXT (S5): wait for partB/audit/DRIVER_DONE.json; COVERAGE.json lists exactly the audited exercise_ids (D samples only
  from those); AUDIT_RESULTS.jsonl = one row per reference. Commit partB/audit after the driver ends.
- Gemini calls: S4 0, cumulative 43 of 1,200. Headless tokens S4: 177,611 at return (wave 1), final <= 1,500,000.
- SHA check S4: S1 generator, see SHA_diff_S4.txt (line count printed at the commit).

## S5 - B2 summary, B3 corrections, B4 closed-set re-score (21.9.2026)
- B2 driver ended on the token cap before wave 9: 3200/4,064 SK rows audited (3413 refs), packets p032-p040 not audited; COVERAGE.json = the audited ids (Part D samples only from these). Per ref all: {"W": 469, "F": 2566, "O": 141, "N": 172, "A": 65}.
- B1 agreement: B1 SK flags 92, audited 70, B2=W 21, any B2 flag 26; B2 W refs 469 of which B1-flagged 21.
- B3 (partB/b3.py, T17 in test_2j): SK rows changed 577, v[0] changed 58 (en = v[0] kept), CZ 0 (all B1 CZ flags listed). Counts: {"sk/W": {"added": 385, "listed": 84}, "sk/O": {"listed": 141}, "sk/N": {"listed": 8, "added": 164}, "sk/A": {"listed": 5, "replaced": 60}, "sk/dedup": {"removed": 1}, "cz/B1_neuter_as_he_she": {"listed": 13}, "cz/B1_gender_contradiction": {"listed": 15}, "cz/B1_number": {"listed": 16}, "cz/B1_gender_fixed_open": {"listed": 10}, "cz/B1_person": {"listed": 53}}. Upload: phase2j/upload/ (+ B3_diff.jsonl, UPLOAD_README.md). Re-freeze: FROZEN_SHA_S5.txt, FREEZE_COMMIT_S5.txt (stack code unchanged; test_2j + b3 added).
- B4 CLOSED-SET RE-SCORE A+B: coverage 474/497 = 95.37 % [93.14, 97.04], FA 21/403 = 5.21 % [3.25, 7.86] (A3 464/497 = 93.36 % [90.80, 95.39] / 20/403 = 4.96 % [3.06, 7.56]; 2I 443/497 = 89.13 % [86.06, 91.73] / 19/403 = 4.71 % [2.86, 7.26]); changed vs A3 22, vs 2I 63; run {"status": "COMPLETE", "requests": 837, "needed": 101, "seeded_used": 736, "calls_made": 101, "counted_total": 101, "spend_usd": 0.012708, "uncounted_attempts": 0}. Detail partB/PART_B.md, partB/b4/B4.json.
- Gemini calls: S5 101, cumulative 144 of 1,200 (GEMINI_LEDGER.json {"S1": 0, "S2": 43, "S2c": 0, "S3": 0, "S5": 101, "S5probe": 0}).
- Headless tokens: B2 total 1414860 (S4 recorded 177,611 at return; S5 adds 1237249 from the driver); S5 itself 0; cumulative headless 1414860.
- SHA check S5: SHA_diff_S5.txt 0 lines.
- NEXT (S6): Part D samples from the CORRECTED phase2j/upload/annotations_sk_fixed.jsonl, only audited ids (COVERAGE.json), excluding 2F-probe 60 + 2I 100.
