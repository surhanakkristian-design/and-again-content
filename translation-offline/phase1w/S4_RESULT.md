# Phase 1W §4 result: fresh set A4 OPENED once, run completed (did not crash), 600/600 calls counted

## History (kept): the two pre-run preflight stops, 0 model calls each, set unopened

- Stop 1 (22:09:01, previous driver): `ModuleNotFoundError: No module named 'runner_1t'` at a4/run/runner_1u.py line 42. Cause: the copied 1U runner (and score_1u.py) computed TOFF = dirname(P1U), which in the copy is phase1w, not translation-offline, so phase1t/run, phase1p, phase1s, phase1u/taskA were never put on sys.path. article_line_1u.py had the same shape and would have looked for phase1w/a4/stack/L3_PROMPT_1U.txt.
- Fix 1 (§4 completion worker, pre-run): TOFF = dirname(dirname(P1U)) in runner_1u.py and score_1u.py; article_line_1u.py repointed to read phase1u/stack/L3_PROMPT_1U.txt and phase1u/RULING_ARTICLE.txt in place (prompt P-FROZEN-1U unchanged, its byte-identity check still runs). Dry import of runner_1u, score_1u, article_line_1u, loader_1u: OK, 36 modules resolved (phase1i..phase1w).
- Stop 2 (22:11:39): `REFUSED: sid 200001 outside the agreed range 190001..190100` (loader_1u.py carried 1U's sid range). This is the "preflight stop output" line further down.
- Fix 2 (pre-run): loader_1u.py SID_LO, SID_HI = 200001, 200100 (brief §4 sids). P1/P2 split = sid parity in score_1u.py, unaffected.
- Nothing in stage A was re-run: writers, judge, assembly, packets, label join and floors are the previous driver's outputs untouched. Both fixes are in the FREEZE commit. No code change after the run started.
- chmod: phase1b..phase1v (20 dirs; phase1a and phase1d do not exist) were already a-w; find found no user-writable path; test writes `touch phase1t/WT` and `touch phase1b/WT` -> Permission denied; the driver's own write test into phase1v -> PermissionError. All before the run.
- Floors F1-F6 on JUDGED counts: all pass (see below).
- Preflight after the fixes: L3-eligible 743, chk {correct/match 155, wrong/auto 745} (not all-accepting), AG errors 0, planned 600 <= cap 800 -> PASS, 0 calls.

## Commits and run summary

- FREEZE hash: 79f76f12cb3cb0751703e17d83c8c539ebdf11ae
- RUN commit: 553b865bd64338289f04fcb887458f189f18b289
- --final run ONCE, 22:16:04 -> exit 0, FINAL_RUN_DONE written, did NOT crash (no recompute needed)
- calls: 600 counted (http 200), 0 uncounted retries, 0 failed (empty/unparsable 200); gemini-3.1-flash-lite, temp 0, thinkingBudget 0
- tokens in 326,015 / out 600; spend $0.03284 at list price
- session total counted: 194 (§3) + 600 = 794 of the 1,200 hard cap
- access log (verbatim): phase1w/a4/run/access_log.jsonl; calls: phase1w/a4/run/calls.jsonl; score: phase1w/a4/run/score_1u.json + SCORE_1U.md
- headline pooled coverage 392/401 = 97.76 % [95.78, 98.97]: point MET, interval MET; pooled FA 16/499 = 3.21 % [1.84, 5.15]: point MET, interval MISSED

- Status: stage B complete
- Note: pre-run fix (0 calls, set unopened): the copied runner/scorer computed TOFF one level short (P1U = phase1w/a4), so runner_1t was not on sys.path; TOFF fixed in runner_1u.py + score_1u.py, and article_line_1u.py repointed to read phase1u/stack + phase1u/RULING_ARTICLE.txt in place; dry import of every module OK; stage A NOT re-run (writers/judge/assemble/join/floors untouched); stage B resumed
- Note: pre-run fix (0 calls, set unopened): the copied runner/scorer computed TOFF one level short (P1U = phase1w/a4), so runner_1t was not on sys.path; TOFF fixed in runner_1u.py + score_1u.py, and article_line_1u.py repointed to read phase1u/stack + phase1u/RULING_ARTICLE.txt in place; dry import of every module OK; stage A NOT re-run (writers/judge/assemble/join/floors untouched); stage B resumed
- Stack: phase1w/stack_1w.py = 1V round 2 + §2 (reader_nom, variant full); §3 REVERTED, L3 prompt P-FROZEN-1U unchanged
- Tooling: phase1v/trackA_set copied to phase1w/a4/set (.py byte-identical; .md paths repointed); 1U runner/loader/scorer copied to phase1w/a4/run with one stack patch (AG primary = stack_1w.decide, rows re-scored with stack_1w.final_accept, cap 800), TASKA path -> phase1u/taskA, and S7 added to the scorer (declared in 1V)
- selftest_1v (on a throwaway copy): {"exit": 0, "tail": ["SELFTEST OK \u2014 0 failure(s)"]}

## Headless sessions (harness usage, bundled binary, --output-format json, --max-turns 12, --model opus)

- writer_A1_try1: exit 0, is_error False, turns 4, input 8, cache_creation 66197, cache_read 124670, output 58846, cost_usd 2.195495, duration_ms 524563, permission_denials 0, models ['claude-opus-5']
- writer_A2_try1: exit 0, is_error False, turns 4, input 8, cache_creation 68163, cache_read 125421, output 60814, cost_usd 2.2647305, duration_ms 552937, permission_denials 0, models ['claude-opus-5']
- writer_B1_try1: exit 0, is_error False, turns 4, input 8, cache_creation 63083, cache_read 133924, output 63437, cost_usd 2.283757, duration_ms 565352, permission_denials 0, models ['claude-opus-5']
- writer_B2_try1: exit 0, is_error False, turns 4, input 8, cache_creation 70988, cache_read 126614, output 63755, cost_usd 2.367102, duration_ms 609726, permission_denials 0, models ['claude-opus-5']
- judge_s1: exit 0, is_error False, turns 10, input 20, cache_creation 193938, cache_read 835390, output 107871, cost_usd 5.0539499999999995, duration_ms 860760, permission_denials 0, models ['claude-opus-5']
- judge sessions used: 1

## Set build

- assemble sentences_read: 116
- assemble sentences_kept: 100
- assemble items: 900
- assemble levels: {"A1": 25, "A2": 25, "B1": 25, "B2": 25}
- assemble halves: {"P1": 50, "P2": 50}
- assemble kinds: {"FR": 32, "MC": 24, "MN": 24, "SKP": 20}
- assemble earlier_sentences_checked_against: 0
- assemble overlaps_total: 1
- assemble violations_total: 0
- assemble hard_violations: 0
- assemble hard_violations_by_kind: {}
- assemble floor_counts_by_construction: {"F1_agent_drops": 160, "F1a_drop_fronted": 64, "F1b_drop_misaligned": 48, "F2_time_frame": 120, "F3_by_passive": 80, "F4_skp_passive": 72, "F5_missing_article": 97, "F6_determiner": 94}
- assemble loud: []
- assemble answer_kinds: {"C": 400, "W": 500}
- assemble wrong_types: {"M": 160, "T": 120, "S": 100, "W": 120}
- assemble exit: 0
- packets items: 900
- packets duplicate_controls: 80
- packets duplicates_per_level: {"A1": 20, "A2": 20, "B1": 20, "B2": 20}
- packets total_qids: 980
- packets parts: 4
- packets seed: 20260923
- packets packet_fields_clean: true
- packets levels_per_part: [{"A2": 62, "B1": 54, "B2": 65, "A1": 64}, {"B1": 61, "A1": 60, "A2": 67, "B2": 57}, {"A2": 55, "B2": 60, "A1": 59, "B1": 71}, {"B2": 63, "A1": 62, "A2": 61, "B1": 59}]
- join key_entries: 980
- join verdict_rows: 980
- join items_labelled: 900
- join unlabelled_items: 0
- join judged: {"wrong": 499, "correct": 401}
- join types: {"T": 119, "M": 160, "W": 120, "S": 100}
- join confidence: {"5": 793, "4": 97, "3": 10}
- join borderline: 12
- join duplicate_controls: 80
- join duplicate_controls_judged: 80
- join label_disagreements: 0
- join judge_noise_pct: 0.0
- join type_only_disagreements: 0
- join REFUSED: null
- join exit: 0

## Floors on JUDGED counts (F1-F6)

- F1_agent_drops_wrong: {"n": 160, "min": 120, "pass": true}
- F1a_fronted_wrong: {"n": 64, "min": 40, "pass": true}
- F1b_misaligned_wrong: {"n": 48, "min": 30, "pass": true}
- F2_time_frame_wrong: {"n": 119, "min": 100, "pass": true}
- F3_by_passive_correct: {"n": 80, "min": 60, "pass": true}
- F4_skp_correct: {"n": 72, "min": 40, "pass": true}
- F5_missing_article_wrong: {"n": 97, "min": 40, "pass": true}
- F6_determiner_correct: {"n": 94, "min": 60, "pass": true}
- missing_article_judged_correct: 0
- determiner_judged_wrong: 0
- T_W_M_S_wrong: {"T": 119, "W": 120, "M": 160, "S": 100}
- judged_correct: 401
- judged_wrong: 499
- all_pass: true
- items: 900
- items_labelled: 900
- drop_cells: {"drop-fronted": {"wrong": 64, "correct": 0}, "drop-misaligned": {"wrong": 48, "correct": 0}, "drop-main": {"wrong": 48, "correct": 0}, "drop-other": {"wrong": 0, "correct": 0}}

## Freeze / chmod / preflight

- FREEZE hash: 79f76f12cb3cb0751703e17d83c8c539ebdf11ae
- RUN commit: 553b865bd64338289f04fcb887458f189f18b289
- chmod: 20 dirs made read-only BEFORE the run; write test into phase1v refused: PermissionError
- chmod stat: dr-xr-xr-x phase1b
- chmod stat: dr-xr-xr-x phase1c
- chmod stat: dr-xr-xr-x phase1e
- chmod stat: dr-xr-xr-x phase1f
- chmod stat: dr-xr-xr-x phase1g
- chmod stat: dr-xr-xr-x phase1h
- chmod stat: dr-xr-xr-x phase1i
- chmod stat: dr-xr-xr-x phase1j
- chmod stat: dr-xr-xr-x phase1k
- chmod stat: dr-xr-xr-x phase1l
- chmod stat: dr-xr-xr-x phase1m
- chmod stat: dr-xr-xr-x phase1n
- chmod stat: dr-xr-xr-x phase1o
- chmod stat: dr-xr-xr-x phase1p
- chmod stat: dr-xr-xr-x phase1q
- chmod stat: dr-xr-xr-x phase1r
- chmod stat: dr-xr-xr-x phase1s
- chmod stat: dr-xr-xr-x phase1t
- chmod stat: dr-xr-xr-x phase1u
- chmod stat: dr-xr-xr-x phase1v
- preflight n_items: 900
- preflight l2_firings: 137
- preflight l3_eligible: 743
- preflight ag_rejected_before_l3: 143
- preflight reach_l3_planned_calls: 600
- preflight unique_requests: 600
- preflight PLANNED_CALLS: 600
- preflight counted_ledger_dev: 0
- preflight cap: 800
- preflight chk: {"correct/match": 155, "wrong/auto": 745}
- preflight ag: {"items": 900, "errors": 0, "fired_primary": 144, "fired_v2": 92, "fired_v3": 110, "fired_guarded_union": 115, "fired_v4_full": 142, "fired_v4_not_v3": 34, "fired_v3_not_v4": 0, "abstain_agentless_passive": 119}
- preflight exit: 0
- preflight stop output: REFUSED: sid 200001 outside the agreed range 190001..190100 | 

## Model calls (gemini-3.1-flash-lite, temperature 0, thinkingBudget 0)

- final started: 2026-09-19T22:16:04; runner exit 0; FINAL_RUN_DONE True
- lines: 600
- counted_http200: 600
- uncounted_retries: 0
- uncounted_by_http: {}
- failed_empty_or_unparsable_200: 0
- tokens_in: 326015
- tokens_out: 600
- models: {"gemini-3.1-flash-lite": 600}
- spend_usd_list_price: 0.03284
- phase total counted (194 §3 + this run): 794 of the 1,200 hard cap
- access log (verbatim): phase1w/a4/run/access_log.jsonl; call log: phase1w/a4/run/calls.jsonl
- runner tail: [PROMPT] P-FROZEN-1U = P-FROZEN-1P + 1 line at index 9; sys identical; hash 81a21eff8840 -> 77c3cd5246d9
- runner tail: [PREFLIGHT] L2 lock firings under BASE: 137   L3-eligible under LOCKTIP: 743   AG v4 rejects before L3: 143   reach L3: 600
- runner tail: [PREFLIGHT] unique requests 600   reusable 0   PLANNED NEW CALLS 600   counted here 0   failed(200, unparsable) 0
- runner tail: [CAP] preflight: counted in ledger_dev 0 + planned 600 = 600   (hard cap 800)
- runner tail: [CALLS] http200 600 (empty replies 0)  transport-dead 0  skipped after the wall 0
- runner tail: -- FINAL_RUN_DONE written: /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1w/a4/run/FINAL_RUN_DONE

## Headline and sensitivities S1-S7 (pooled / P1 / P2, exact Clopper-Pearson 95 %; coverage >= 90 %, FA < 5 %)

- headline pooled coverage: 392/401 = 97.76 % [95.78, 98.97] - target coverage >= 90 %: point MET, interval MET
- headline pooled fa: 16/499 = 3.21 % [1.84, 5.15] - target FA < 5 %: point MET, interval MISSED
- headline P1 coverage: 195/200 = 97.50 % [94.26, 99.18] - target coverage >= 90 %: point MET, interval MET
- headline P1 fa: 5/250 = 2.00 % [0.65, 4.61] - target FA < 5 %: point MET, interval MET
- headline P2 coverage: 197/201 = 98.01 % [94.98, 99.46] - target coverage >= 90 %: point MET, interval MET
- headline P2 fa: 11/249 = 4.42 % [2.23, 7.77] - target FA < 5 %: point MET, interval MISSED
- headline Fisher P1 vs P2 coverage: p = 0.7508
- headline Fisher P1 vs P2 fa: p = 0.1366
- S1_writer_intent pooled coverage: 391/400 = 97.75 % [95.77, 98.97] - target coverage >= 90 %: point MET, interval MET
- S1_writer_intent pooled fa: 17/500 = 3.40 % [1.99, 5.39] - target FA < 5 %: point MET, interval MISSED
- S1_writer_intent P1 coverage: 195/200 = 97.50 % [94.26, 99.18] - target coverage >= 90 %: point MET, interval MET
- S1_writer_intent P1 fa: 5/250 = 2.00 % [0.65, 4.61] - target FA < 5 %: point MET, interval MET
- S1_writer_intent P2 coverage: 196/200 = 98.00 % [94.96, 99.45] - target coverage >= 90 %: point MET, interval MET
- S1_writer_intent P2 fa: 12/250 = 4.80 % [2.50, 8.23] - target FA < 5 %: point MET, interval MISSED
- S1_writer_intent Fisher P1 vs P2 coverage: p = 1.0
- S1_writer_intent Fisher P1 vs P2 fa: p = 0.1366
- S1_writer_intent items moved: 1
- S2_wrong_borderline_correct pooled coverage: 397/421 = 94.30 % [91.64, 96.31] - target coverage >= 90 %: point MET, interval MET
- S2_wrong_borderline_correct pooled fa: 11/479 = 2.30 % [1.15, 4.07] - target FA < 5 %: point MET, interval MET
- S2_wrong_borderline_correct P1 coverage: 196/207 = 94.69 % [90.69, 97.32] - target coverage >= 90 %: point MET, interval MET
- S2_wrong_borderline_correct P1 fa: 4/243 = 1.65 % [0.45, 4.16] - target FA < 5 %: point MET, interval MET
- S2_wrong_borderline_correct P2 coverage: 201/214 = 93.93 % [89.84, 96.73] - target coverage >= 90 %: point MET, interval MISSED
- S2_wrong_borderline_correct P2 fa: 7/236 = 2.97 % [1.20, 6.02] - target FA < 5 %: point MET, interval MISSED
- S2_wrong_borderline_correct Fisher P1 vs P2 coverage: p = 0.8346
- S2_wrong_borderline_correct Fisher P1 vs P2 fa: p = 0.3759
- S2_wrong_borderline_correct items moved: 20
- S3_correct_borderline_wrong pooled coverage: 375/381 = 98.43 % [96.60, 99.42] - target coverage >= 90 %: point MET, interval MET
- S3_correct_borderline_wrong pooled fa: 33/519 = 6.36 % [4.42, 8.81] - target FA < 5 %: point MISSED, interval MISSED
- S3_correct_borderline_wrong P1 coverage: 187/191 = 97.91 % [94.72, 99.43] - target coverage >= 90 %: point MET, interval MET
- S3_correct_borderline_wrong P1 fa: 13/259 = 5.02 % [2.70, 8.43] - target FA < 5 %: point MISSED, interval MISSED
- S3_correct_borderline_wrong P2 coverage: 188/190 = 98.95 % [96.25, 99.87] - target coverage >= 90 %: point MET, interval MET
- S3_correct_borderline_wrong P2 fa: 20/260 = 7.69 % [4.76, 11.63] - target FA < 5 %: point MISSED, interval MISSED
- S3_correct_borderline_wrong Fisher P1 vs P2 coverage: p = 0.685
- S3_correct_borderline_wrong Fisher P1 vs P2 fa: p = 0.2803
- S3_correct_borderline_wrong items moved: 20
- S4_exclude_S2_S3 pooled coverage: 375/381 = 98.43 % [96.60, 99.42] - target coverage >= 90 %: point MET, interval MET
- S4_exclude_S2_S3 pooled fa: 11/479 = 2.30 % [1.15, 4.07] - target FA < 5 %: point MET, interval MET
- S4_exclude_S2_S3 P1 coverage: 187/191 = 97.91 % [94.72, 99.43] - target coverage >= 90 %: point MET, interval MET
- S4_exclude_S2_S3 P1 fa: 4/243 = 1.65 % [0.45, 4.16] - target FA < 5 %: point MET, interval MET
- S4_exclude_S2_S3 P2 coverage: 188/190 = 98.95 % [96.25, 99.87] - target coverage >= 90 %: point MET, interval MET
- S4_exclude_S2_S3 P2 fa: 7/236 = 2.97 % [1.20, 6.02] - target FA < 5 %: point MET, interval MISSED
- S4_exclude_S2_S3 Fisher P1 vs P2 coverage: p = 0.685
- S4_exclude_S2_S3 Fisher P1 vs P2 fa: p = 0.3759
- S4_exclude_S2_S3 items moved: 40
- S5_article_pre_ruling pooled coverage: 395/498 = 79.32 % [75.49, 82.79] - target coverage >= 90 %: point MISSED, interval MISSED
- S5_article_pre_ruling pooled fa: 13/402 = 3.23 % [1.73, 5.47] - target FA < 5 %: point MET, interval MISSED
- S5_article_pre_ruling P1 coverage: 196/247 = 79.35 % [73.76, 84.22] - target coverage >= 90 %: point MISSED, interval MISSED
- S5_article_pre_ruling P1 fa: 4/203 = 1.97 % [0.54, 4.97] - target FA < 5 %: point MET, interval MET
- S5_article_pre_ruling P2 coverage: 199/251 = 79.28 % [73.74, 84.12] - target coverage >= 90 %: point MISSED, interval MISSED
- S5_article_pre_ruling P2 fa: 9/199 = 4.52 % [2.09, 8.41] - target FA < 5 %: point MET, interval MISSED
- S5_article_pre_ruling Fisher P1 vs P2 coverage: p = 1.0
- S5_article_pre_ruling Fisher P1 vs P2 fa: p = 0.1689
- S5_article_pre_ruling items moved: 97
- S6_leave_out_A1 pooled coverage: 294/301 = 97.67 % [95.27, 99.06] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_A1 pooled fa: 16/374 = 4.28 % [2.46, 6.85] - target FA < 5 %: point MET, interval MISSED
- S6_leave_out_A1 P1 coverage: 143/148 = 96.62 % [92.29, 98.89] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_A1 P1 fa: 5/185 = 2.70 % [0.88, 6.19] - target FA < 5 %: point MET, interval MISSED
- S6_leave_out_A1 P2 coverage: 151/153 = 98.69 % [95.36, 99.84] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_A1 P2 fa: 11/189 = 5.82 % [2.94, 10.17] - target FA < 5 %: point MISSED, interval MISSED
- S6_leave_out_A1 Fisher P1 vs P2 coverage: p = 0.2762
- S6_leave_out_A1 Fisher P1 vs P2 fa: p = 0.2006
- S6_leave_out_A1 items moved: 225
- S6_leave_out_A2 pooled coverage: 297/301 = 98.67 % [96.63, 99.64] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_A2 pooled fa: 11/374 = 2.94 % [1.48, 5.20] - target FA < 5 %: point MET, interval MISSED
- S6_leave_out_A2 P1 coverage: 151/152 = 99.34 % [96.39, 99.98] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_A2 P1 fa: 2/190 = 1.05 % [0.13, 3.75] - target FA < 5 %: point MET, interval MET
- S6_leave_out_A2 P2 coverage: 146/149 = 97.99 % [94.23, 99.58] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_A2 P2 fa: 9/184 = 4.89 % [2.26, 9.08] - target FA < 5 %: point MET, interval MISSED
- S6_leave_out_A2 Fisher P1 vs P2 coverage: p = 0.3675
- S6_leave_out_A2 Fisher P1 vs P2 fa: p = 0.0334
- S6_leave_out_A2 items moved: 225
- S6_leave_out_B1 pooled coverage: 293/301 = 97.34 % [94.83, 98.85] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_B1 pooled fa: 11/374 = 2.94 % [1.48, 5.20] - target FA < 5 %: point MET, interval MISSED
- S6_leave_out_B1 P1 coverage: 144/148 = 97.30 % [93.22, 99.26] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_B1 P1 fa: 4/185 = 2.16 % [0.59, 5.44] - target FA < 5 %: point MET, interval MISSED
- S6_leave_out_B1 P2 coverage: 149/153 = 97.39 % [93.44, 99.28] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_B1 P2 fa: 7/189 = 3.70 % [1.50, 7.48] - target FA < 5 %: point MET, interval MISSED
- S6_leave_out_B1 Fisher P1 vs P2 coverage: p = 1.0
- S6_leave_out_B1 Fisher P1 vs P2 fa: p = 0.5429
- S6_leave_out_B1 items moved: 225
- S6_leave_out_B2 pooled coverage: 292/300 = 97.33 % [94.81, 98.84] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_B2 pooled fa: 10/375 = 2.67 % [1.29, 4.85] - target FA < 5 %: point MET, interval MET
- S6_leave_out_B2 P1 coverage: 147/152 = 96.71 % [92.49, 98.92] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_B2 P1 fa: 4/190 = 2.11 % [0.58, 5.30] - target FA < 5 %: point MET, interval MISSED
- S6_leave_out_B2 P2 coverage: 145/148 = 97.97 % [94.19, 99.58] - target coverage >= 90 %: point MET, interval MET
- S6_leave_out_B2 P2 fa: 6/185 = 3.24 % [1.20, 6.93] - target FA < 5 %: point MET, interval MISSED
- S6_leave_out_B2 Fisher P1 vs P2 coverage: p = 0.723
- S6_leave_out_B2 Fisher P1 vs P2 fa: p = 0.5385
- S6_leave_out_B2 items moved: 225
- S7_determiner_correct_as_wrong pooled coverage: 302/307 = 98.37 % [96.24, 99.47] - target coverage >= 90 %: point MET, interval MET
- S7_determiner_correct_as_wrong pooled fa: 106/593 = 17.88 % [14.87, 21.20] - target FA < 5 %: point MISSED, interval MISSED
- S7_determiner_correct_as_wrong P1 coverage: 150/153 = 98.04 % [94.38, 99.59] - target coverage >= 90 %: point MET, interval MET
- S7_determiner_correct_as_wrong P1 fa: 50/297 = 16.84 % [12.76, 21.59] - target FA < 5 %: point MISSED, interval MISSED
- S7_determiner_correct_as_wrong P2 coverage: 152/154 = 98.70 % [95.39, 99.84] - target coverage >= 90 %: point MET, interval MET
- S7_determiner_correct_as_wrong P2 fa: 56/296 = 18.92 % [14.62, 23.85] - target FA < 5 %: point MISSED, interval MISSED
- S7_determiner_correct_as_wrong Fisher P1 vs P2 coverage: p = 0.6844
- S7_determiner_correct_as_wrong Fisher P1 vs P2 fa: p = 0.5219
- S7_determiner_correct_as_wrong items moved: 94

## Every cell, one per line (headline labels)

- cell agent_drop_fa all: 10/160 = 6.25 % [3.04, 11.19]
- cell agent_drop_fa fronted: 7/64 = 10.94 % [4.51, 21.25]
- cell agent_drop_fa main: 0/48 = 0.00 % [0.00, 7.40]
- cell agent_drop_fa misaligned: 3/48 = 6.25 % [1.31, 17.20]
- cell agent_drop_fa other: n = 0
- cell by_passive_coverage: 79/80 = 98.75 % [93.23, 99.97]
- cell missing_article coverage: n = 0
- cell missing_article fa: 3/97 = 3.09 % [0.64, 8.77]
- cell missing_article judged_correct_n: 0
- cell missing_article judged_wrong_n: 97
- cell missing_article rejected_by_layer AG: 1
- cell missing_article rejected_by_layer L3: 66
- cell missing_article rejected_by_layer L3:TIPrej: 27
- cell skp_coverage: 70/72 = 97.22 % [90.32, 99.66]
- cell time_frame_fa: 2/119 = 1.68 % [0.20, 5.94]

## AG block

- ag primary_v4 catches_judged_wrong: 141
- ag primary_v4 fired: 144
- ag primary_v4 measured_cost_judged_correct: 3
- ag shadows_offline guarded_union catches_judged_wrong: 114
- ag shadows_offline guarded_union cost_judged_correct: 1
- ag shadows_offline guarded_union fired: 115
- ag shadows_offline guarded_union fired_where_v4_did_not: 0
- ag shadows_offline guarded_union v4_fires_where_it_did_not: 29
- ag shadows_offline v2 catches_judged_wrong: 92
- ag shadows_offline v2 cost_judged_correct: 0
- ag shadows_offline v2 fired: 92
- ag shadows_offline v2 fired_where_v4_did_not: 5
- ag shadows_offline v2 v4_fires_where_it_did_not: 57
- ag shadows_offline v3 catches_judged_wrong: 110
- ag shadows_offline v3 cost_judged_correct: 0
- ag shadows_offline v3 fired: 110
- ag shadows_offline v3 fired_where_v4_did_not: 0
- ag shadows_offline v3 v4_fires_where_it_did_not: 34
- ag shadows_offline v4_full catches_judged_wrong: 139
- ag shadows_offline v4_full cost_judged_correct: 3
- ag shadows_offline v4_full fired: 142
- ag shadows_offline v4_full fired_where_v4_did_not: 0
- ag shadows_offline v4_full v4_fires_where_it_did_not: 2

## Model block

- model counted_calls: 600
- model failed_calls: 0
- model latency_ms_mean: 659.8
- model latency_ms_total: 395879
- model model_replies DIFF: 311
- model model_replies SAME: 252
- model model_replies TIP: 37
- model price_note: UPPER BOUND at the published flash-lite list price ($0.10/1M in, $0.40/1M out); free-tier calls cost 0
- model spend_usd_upper_bound: 0.0326
- model tokens_in: 326015
- model tokens_out: 0
- failed calls (detail): []
