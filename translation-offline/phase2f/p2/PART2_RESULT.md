# Phase 2F Part 2 result: Czech coverage and false acceptance, fresh set NOT OPENED

- Status: STOP: the judge did not deliver all verdict files; 0 Gemini calls
- Method: Phase 1W §4, language changed to Czech; Slovak 1W figures are quoted beside every Czech one below.
- Part 1: {"PART1_DONE": true, "PART1_STOP.md": true, "status": "STOPPED EARLY: ['STOP_token_cap.md']; 2850 rows assembled, 1466116 headless tokens", "waited_s": 0}
- Note: PART 1 STOPPED EARLY (PART1_STOP.md present); Part 2 ran anyway as the brief instructs.
- Note: judge continuation session 2 for parts [4]

## Deviations from 1W (declared before the set was opened)

1. The 100 sentences are PRODUCTION Czech, drawn read-only from the full Czech production corpus and annotated by the frozen 2E pipeline inside this driver; 1V/1W had the writers invent the sentences AND the annotation.  Consequence: the assembler, packet builder, label join and floor check are written in this driver against the same contracts instead of copied byte-identically from phase1v/trackA_set.
2. STATED DEVIATION - the set source was WIDENED before the set was opened.  The first reading of "100 NEW Czech sentences from PRODUCTION" was narrow: the pool was 2C's own 4,064-row Czech selection minus every row 2C, 2D or 2E had already annotated, and the annotation was adopted from phase2f/out/annotations_cz_final.jsonl.  That pool was empty in practice.  Part 1 failed twice to annotate cz_0004 and cz_0005, so the adoptable residue was A1 17 / A2 18 / B1 8 / B2 7 against the 25 per level the design requires, and the driver correctly refused twice at 0 Gemini calls rather than open a short set.  Part 1 will NOT be re-attempted: cz_0004 is 429-limited and cost 875,000 headless tokens for zero rows.  The pool is therefore the WHOLE Czech production corpus - 39,498 grammar-topic exercises with a Czech full_sentence (A1 9,999 / A2 13,591 / B1 8,906 / B2 7,002), read with a SELECT-only query and never written to.  This is the same source 2C's selection was itself drawn from.  The widening makes the set MORE production-representative, not less: 2C's selection was a concept-capped, md5-ranked ONE-ROW-PER-(concept, level) sample of this corpus, so drawing straight from the corpus removes that sampling filter instead of adding one.  The 100 are annotated by this driver with the frozen 2E pipeline - the 2C/2E v prompt verbatim, the arm-B rewrite pass, and the dedicated lk pass (prompt sha16 5fa910459c078539, asserted in code) - which replaces the adoption path the narrow reading depended on.  Declared here BEFORE the set was opened.
3. The writers therefore write ONLY the 4 correct + 5 wrong answers per sentence, seeing only the Czech sentence, its level and its topic - never the English reference, never the annotation.  The answer-slot contract is conditional on what the writer sees (a sentence that names no doer gets time-frame shifts in w1/w2 instead of agent drops).
4. Floors F1a/F1b/F4 cannot be controlled on production text (the sentence shape is given, not commissioned).  They are COMPUTED and REPORTED but declared with min 0; the runner gate requires the seven 1U key names to be present, so they are present.  F7 (T/W/M/S each >= 60) is added for "T/W/M/S otherwise balanced".
5. sentences.json carries the CZECH sentence under the key "slovak" because loader_1u.py requires that key and phase1p/runner_1p.py reads it; a duplicate "czech" key carries the same string.  Renaming it would have meant editing read-only phase1p code.
6. The L3 prompt is P-FROZEN-1U, unchanged, including its sentence that names Slovak.  Editing it would have been a stack change and would have broken the article_line hash assertion; the brief says to tune nothing.  Recorded as a defect instead (see DEFECTS).

## Defects RECORDED, not fixed

- skp_heavy: SKP (no named doer) is 52 of 100 production sentences; the agent-drop floor F1 >= 120 may not be reachable

## Headless sessions (bundled binary, --output-format json, --max-turns 12, opus)

- ann_v_A1_r0_try0: exit 0, is_error False, turns 1, input 2, cache_creation 19927, cache_read 0, output 15018, cost_usd 0.57473, duration_ms 154071
- ann_v_A2_r0_try0: exit 0, is_error False, turns 1, input 2, cache_creation 20149, cache_read 0, output 12954, cost_usd 0.52535, duration_ms 129853
- ann_v_B1_r0_try0: exit 0, is_error False, turns 1, input 2, cache_creation 9786, cache_read 10672, output 14639, cost_usd 0.469181, duration_ms 144629
- ann_v_B2_r0_try0: exit 0, is_error False, turns 1, input 2, cache_creation 9707, cache_read 10672, output 11550, cost_usd 0.391166, duration_ms 113622
- ann_rw_A1_r0_try0: exit 0, is_error False, turns 1, input 2, cache_creation 6512, cache_read 10672, output 4415, cost_usd 0.18084099999999997, duration_ms 51269
- ann_rw_A2_r0_try0: exit 0, is_error False, turns 1, input 2, cache_creation 6390, cache_read 10672, output 3807, cost_usd 0.16442099999999998, duration_ms 43214
- ann_rw_B1_r0_try0: exit 0, is_error False, turns 1, input 2, cache_creation 6895, cache_read 10672, output 4052, cost_usd 0.17559599999999997, duration_ms 40971
- ann_rw_B2_r0_try0: exit 0, is_error False, turns 1, input 2, cache_creation 7210, cache_read 10672, output 9953, cost_usd 0.326271, duration_ms 108420
- ann_lk_A1_try0: exit 0, is_error False, turns 1, input 2, cache_creation 6825, cache_read 10672, output 3775, cost_usd 0.16797099999999998, duration_ms 36162
- ann_lk_A2_try0: exit 0, is_error False, turns 1, input 2, cache_creation 6920, cache_read 10672, output 2655, cost_usd 0.14092099999999996, duration_ms 25255
- ann_lk_B1_try0: exit 0, is_error False, turns 1, input 2, cache_creation 7077, cache_read 10672, output 3510, cost_usd 0.163866, duration_ms 37686
- ann_lk_B2_try0: exit 0, is_error False, turns 1, input 2, cache_creation 7049, cache_read 10672, output 2615, cost_usd 0.14121099999999998, duration_ms 23559
- writer_A1_try1: exit 0, is_error False, turns 2, input 4, cache_creation 35796, cache_read 29160, output 28106, cost_usd 1.07521, duration_ms 265412
- writer_A2_try1: exit 0, is_error False, turns 2, input 4, cache_creation 37083, cache_read 29261, output 29288, cost_usd 1.1176805, duration_ms 273521
- writer_B1_try1: exit 0, is_error False, turns 2, input 4, cache_creation 47518, cache_read 29427, output 39560, cost_usd 1.4789135, duration_ms 382516
- writer_B2_try1: exit 0, is_error False, turns 2, input 4, cache_creation 40809, cache_read 29376, output 32854, cost_usd 1.244148, duration_ms 310451
- judge_s1: exit 1, is_error True, turns 13, input 24, cache_creation 197017, cache_read 1266632, output 83513, cost_usd 4.691431000000001, duration_ms 759548
- headless tokens spent in Part 2 (input + output + cache): 2265574

## Set selection

- source: the FULL Czech production corpus, read with a SELECT-only query (never 2C's 4,064-row sample of it, and nothing was ever written)
- corpus total: 39498 (expected 39498); by level: {"B1": 8906, "B2": 7002, "A1": 9999, "A2": 13591} (expected {"A1": 9999, "A2": 13591, "B1": 8906, "B2": 7002})
- exclusion set sizes: annotated-by-2C/2D/2E/2F-Part-1 exercise ids 4064, selection_2c rows those phases touched 4064, phase1*/pilot/measurements exercise ids 488, union of id sets 4552, normalised sentence texts 10595, 2C row numbers (n) 8128
- candidates after exclusion: 34966 total, by level {"A1": 8733, "A2": 12269, "B1": 7874, "B2": 6090}
- reserve queue built: {"A1": 40, "A2": 40, "B1": 40, "B2": 40}; reserve used: {"A1": 0, "A2": 0, "B1": 0, "B2": 0}; replacements made: []
- overlap count: 0; violation count: 0
- annotation token spend (headless, this driver): 310134 of the 1800000 cap; refused chunks []; v prompt sha16 4f9d486477084793; lk prompt sha16 5fa910459c078539; PAR 2; MAX_RETRY 3

- selection source: "FULL Czech production corpus (read-only SELECT), not phase2c/selection_2c.jsonl"
- selection corpus_total: 39498
- selection corpus_by_level: {"B1": 8906, "B2": 7002, "A1": 9999, "A2": 13591}
- selection corpus_expected: 39498
- selection corpus_expected_by_level: {"A1": 9999, "A2": 13591, "B1": 8906, "B2": 7002}
- selection exclusion_ex_annotated: 4064
- selection exclusion_ex_selection: 4064
- selection exclusion_ex_phase1: 488
- selection exclusion_ex_ids_union: 4552
- selection exclusion_ex_text: 10595
- selection exclusion_used_n: 8128
- selection exclusion_detail: {"ex_annotated": 4064, "ex_selection": 4064, "ex_phase1": 488, "ex_text": 10595, "used_n": 8128, "ex_ids_union": 4552, "selection_2c_rows": 8128, "sources_checked": [{"file": "phase2c/out/annotations_sk_0001.jsonl", "new_n": 1000, "new_exercise_ids": 1000}, {"file": "phase2c/out/annotations_sk_0002.jsonl", "new_n": 1000, "new_exercise_ids": 1000}, {"file": "phase2c/out/annotations_sk_0003.jsonl", "new_n": 1000, "new_exercise_ids": 1000}, {"file": "phase2c/out/annotations_sk_0004.jsonl", "new_n": 1000, "new_exercise_ids": 1000}, {"file": "phase2c/out/annotations_sk_0005.jsonl", "new_n": 64, "new_exercise_ids": 64}, {"file": "phase2d/out/annotations_sk_final.jsonl", "new_n": 0, "new_exercise_ids": 0}, {"file": "phase2e/out/annotations_cz_0001.jsonl", "new_n": 1000, "new_exercise_ids": 0}, {"file": "phase2e/out/annotations_cz_0002.jsonl", "new_n": 900, "new_exercise_ids": 0}, {"file": "phase2e/out/annotations_cz_0003.jsonl", "new_n": 900, "new_exercise_ids": 0}, {"file": "phase2e/out/annotations_cz_final.jsonl", "new_n": 0, "new_exercise_ids": 0}, {"file": "phase2f/out/annotations_cz_0001.jsonl", "new_n": 0, "new_exercise_ids": 0}, {"file": "phase2f/out/annotations_cz_0002.jsonl", "ne
- selection candidates: 34966
- selection candidates_by_level: {"A1": 8733, "A2": 12269, "B1": 7874, "B2": 6090}
- selection reserve_by_level: {"A1": 40, "A2": 40, "B1": 40, "B2": 40}
- selection reserve_used: {"A1": 0, "A2": 0, "B1": 0, "B2": 0}
- selection replacements_made: []
- selection annotation: {"method": "frozen 2E pipeline run by this driver: v (2C prompt verbatim) + arm-B rewrite + the dedicated lk pass", "v_prompt_sha16": "4f9d486477084793", "lk_prompt_sha16": "5fa910459c078539", "par": 2, "max_retry": 3, "rounds": 3, "headless_tokens_annotation": 310134, "headless_tokens_part2_total": 310134, "token_cap": 1800000, "token_estimate": 190000, "sessions": ["ann_v_A1_r0_try0", "ann_v_A2_r0_try0", "ann_v_B1_r0_try0", "ann_v_B2_r0_try0", "ann_rw_A1_r0_try0", "ann_rw_A2_r0_try0", "ann_rw_B1_r0_try0", "ann_rw_B2_r0_try0", "ann_lk_A1_try0", "ann_lk_A2_try0", "ann_lk_B1_try0", "ann_lk_B2_try0"], "refused_chunks": [], "replacements": [], "reserve_used": {"A1": 0, "A2": 0, "B1": 0, "B2": 0}, "rows_paid": 100, "lk_merge": {"corrected": 52, "class_unusable": 23, "class_adjust": 29, "exact": 48, "class_exact": 48}, "unmeasurable_windows": 1, "derive_2c": true, "annotated": 100}
- selection picked: 100
- selection by_level: {"A1": 25, "A2": 25, "B1": 25, "B2": 25}
- selection halves: {"P1": 50, "P2": 50}
- selection kinds: {"SKP": 52, "MN": 23, "FR": 6, "MC": 19}
- selection sid_range: [210001, 210100]
- selection seed: 20260921
- selection earlier_n_checked_against: 8128
- selection earlier_sentences_checked_against: 10595
- selection sources_checked: [{"file": "phase2c/out/annotations_sk_0001.jsonl", "new_n": 1000, "new_exercise_ids": 1000}, {"file": "phase2c/out/annotations_sk_0002.jsonl", "new_n": 1000, "new_exercise_ids": 1000}, {"file": "phase2c/out/annotations_sk_0003.jsonl", "new_n": 1000, "new_exercise_ids": 1000}, {"file": "phase2c/out/annotations_sk_0004.jsonl", "new_n": 1000, "new_exercise_ids": 1000}, {"file": "phase2c/out/annotations_sk_0005.jsonl", "new_n": 64, "new_exercise_ids": 64}, {"file": "phase2d/out/annotations_sk_final.jsonl", "new_n": 0, "new_exercise_ids": 0}, {"file": "phase2e/out/annotations_cz_0001.jsonl", "new_n": 1000, "new_exercise_ids": 0}, {"file": "phase2e/out/annotations_cz_0002.jsonl", "new_n": 900, "new_exercise_ids": 0}, {"file": "phase2e/out/annotations_cz_0003.jsonl", "new_n": 900, "new_exercise_ids": 0}, {"file": "phase2e/out/annotations_cz_final.jsonl", "new_n": 0, "new_exercise_ids": 0}, {"file": "phase2f/out/annotations_cz_0001.jsonl", "new_n": 0, "new_exercise_ids": 0}, {"file": "phase2f/out/annotations_cz_0002.jsonl", "new_n": 50, "new_exercise_ids": 0}, {"file": "phase2f/out/annotations_cz_0003.jsonl", "new_n": 0, "new_exercise_ids": 0}, {"file": "phase2f/out/annotations_cz_final.js
- selection overlaps_total: 0
- selection violations_total: 0
- selection lk_prompt_sha16: "5fa910459c078539"
- selection lk_verdicts: {"adjusted": 52, "exact": 48}
- selection v_prompt_sha16: ["4f9d486477084793"]

## Assemble

- assemble items: 900
- assemble sentences: 100
- assemble hard: []
- assemble hard_n: 0
- assemble soft_n: 0
- assemble soft: []
- assemble answer_tags: {"plain": 100, "determiner": 100, "by-passive": 78, "paraphrase": 100, "drop-main": 164, "time-frame": 136, "missing-article": 100, "wrong-word": 100, "skp-passive": 22}
- assemble wrong_types: {"M": 164, "T": 136, "S": 100, "W": 100}

## Packets

- packets items: 900
- packets duplicate_controls: 80
- packets duplicates_per_level: 20
- packets total_qids: 980
- packets parts: 4
- packets part_sizes: [254, 256, 257, 213]
- packets seed: 20260921
- packets packet_fields_clean: true
- packets topic_present: true
- packets levels_per_part: [["A1", "A2", "B1", "B2"], ["A1", "A2", "B1", "B2"], ["A1", "A2", "B1", "B2"], ["A1", "A2", "B1", "B2"]]

## Label join

- join key_entries: 980
- join verdict_rows: 980
- join items_labelled: 900
- join unlabelled_items: 0
- join rejected_rows: []
- join rejected_n: 0
- join judged: {"correct": 406, "wrong": 494}
- join types: {"T": 146, "W": 102, "S": 99, "M": 147}
- join confidence: {"4": 900}
- join borderline: 47
- join duplicate_controls: 80
- join duplicate_controls_judged: 80
- join label_disagreements: 4
- join type_only_disagreements: 4
- join judge_noise_pct: 5.0

## Floors on JUDGED counts

- floors F1_agent_drops_wrong: {"n": 0, "min": 120, "pass": false}
- floors F1a_fronted_wrong: {"n": 0, "min": 0, "pass": true}
- floors F1b_misaligned_wrong: {"n": 0, "min": 0, "pass": true}
- floors F2_time_frame_wrong: {"n": 146, "min": 100, "pass": true}
- floors F3_by_passive_correct: {"n": 76, "min": 60, "pass": true}
- floors F4_skp_correct: {"n": 24, "min": 0, "pass": true}
- floors F5_missing_article_wrong: {"n": 99, "min": 40, "pass": true}
- floors F6_determiner_correct: {"n": 100, "min": 60, "pass": true}
- floors F7_T_wrong: {"n": 146, "min": 60, "pass": true}
- floors F7_W_wrong: {"n": 102, "min": 60, "pass": true}
- floors F7_M_wrong: {"n": 0, "min": 60, "pass": false}
- floors F7_S_wrong: {"n": 99, "min": 60, "pass": true}
- floors judged_correct: 553
- floors judged_wrong: 347
- floors items: 900
- floors items_labelled: 900
- floors missing_article_judged_correct: 1
- floors determiner_judged_wrong: 0
- floors all_pass: false
- floors sensitivity_nonempty: {"S1_writer_intent": 169, "S2_wrong_borderline_correct": 20, "S3_correct_borderline_wrong": 31, "S5_article_pre_ruling": 100, "S6_leave_one_level_out": 4, "S7_determiner_correct_as_wrong": 100}
- floors sensitivity_empty: []

## Freeze / preflight / calls

- FREEZE hash: None
- RUN commit: None
- final started: None; runner exit None; FINAL_RUN_DONE False
- lines: 0
- counted_http200: 0
- uncounted_retries: 0
- uncounted_by_http: {}
- failed_empty_or_unparsable_200: 0
- failure_rate_pct: null
- tokens_in: 0
- tokens_out: 0
- spend_usd_list_price: 0.0
- Gemini budget: 0 counted of Part 2's ceiling 588 (phase-wide cap 900 minus the 312 counted calls Part 3.1 already spent).  counted = http 200 only; http 0 / 429 / 5xx are retried with logged back-off as counted:false; an empty or unparsable 200 is a FAILED call - counted, never guessed, never silently retried.
- access log (verbatim) below; call log: p2/run/calls.jsonl

## Access log (verbatim)

```
(no access log: the data dir was never read by the runner)
```
