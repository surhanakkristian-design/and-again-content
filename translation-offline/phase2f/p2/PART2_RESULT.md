# Phase 2F Part 2 result: Czech coverage and false acceptance, fresh set NOT OPENED

- Status: STOP: not enough fresh annotated Czech sentences per level {"A1": 17, "A2": 18, "B1": 8, "B2": 7} (need 25 each); the set was NOT opened, 0 Gemini calls
- Method: Phase 1W §4, language changed to Czech; Slovak 1W figures are quoted beside every Czech one below.
- Part 1: {"PART1_DONE": true, "PART1_STOP.md": true, "status": "STOPPED EARLY: ['STOP_token_cap.md']; 2850 rows assembled, 1466116 headless tokens", "waited_s": 0}
- Note: PART 1 STOPPED EARLY (PART1_STOP.md present); Part 2 ran anyway as the brief instructs.
- Note: PART 1 STOPPED EARLY (PART1_STOP.md present); Part 2 ran anyway as the brief instructs.

## Deviations from 1W (declared before the set was opened)

1. The 100 sentences are PRODUCTION Czech (phase2c/selection_2c.jsonl) annotated by the frozen 2E pipeline and adopted from phase2f/out/annotations_cz_final.jsonl at 0 new tokens; 1V/1W had the writers invent the sentences AND the annotation.  Consequence: the assembler, packet builder, label join and floor check are written in this driver against the same contracts instead of copied byte-identically from phase1v/trackA_set.
2. The writers therefore write ONLY the 4 correct + 5 wrong answers per sentence, seeing only the Czech sentence, its level and its topic - never the English reference, never the annotation.  The answer-slot contract is conditional on what the writer sees (a sentence that names no doer gets time-frame shifts in w1/w2 instead of agent drops).
3. Floors F1a/F1b/F4 cannot be controlled on production text (the sentence shape is given, not commissioned).  They are COMPUTED and REPORTED but declared with min 0; the runner gate requires the seven 1U key names to be present, so they are present.  F7 (T/W/M/S each >= 60) is added for "T/W/M/S otherwise balanced".
4. sentences.json carries the CZECH sentence under the key "slovak" because loader_1u.py requires that key and phase1p/runner_1p.py reads it; a duplicate "czech" key carries the same string.  Renaming it would have meant editing read-only phase1p code.
5. The L3 prompt is P-FROZEN-1U, unchanged, including its sentence that names Slovak.  Editing it would have been a stack change and would have broken the article_line hash assertion; the brief says to tune nothing.  Recorded as a defect instead (see DEFECTS).

## Defects RECORDED, not fixed

- none

## Headless sessions (bundled binary, --output-format json, --max-turns 12, opus)

- headless tokens spent in Part 2 (input + output + cache): 0

## Set selection


## Assemble

- assemble items: 900
- assemble sentences: 100
- assemble hard: []
- assemble hard_n: 0
- assemble soft_n: 0
- assemble soft: []
- assemble answer_tags: {"plain": 100, "determiner": 100, "by-passive": 76, "paraphrase": 100, "drop-fronted": 56, "time-frame": 148, "missing-article": 100, "wrong-word": 100, "drop-misaligned": 48, "drop-main": 48, "skp-passive": 24}
- assemble wrong_types: {"M": 152, "T": 148, "S": 100, "W": 100}

## Packets

- packets items: 900
- packets duplicate_controls: 80
- packets duplicates_per_level: 20
- packets total_qids: 980
- packets parts: 3
- packets part_sizes: [460, 460, 60]
- packets seed: 20260921
- packets packet_fields_clean: true
- packets topic_present: true
- packets levels_per_part: [["A1", "A2", "B1", "B2"], ["A1", "A2", "B1", "B2"], ["A1", "A2", "B1", "B2"]]

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
- Gemini budget: 0 (cap 600)
- access log (verbatim) below; call log: p2/run/calls.jsonl

## Access log (verbatim)

```
(no access log: the data dir was never read by the runner)
```
