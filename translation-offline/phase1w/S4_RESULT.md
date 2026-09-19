# Phase 1W §4 result: fresh set A4 NOT OPENED

- Status: STOP: preflight refused/stopped (0 model calls): ['REFUSED: sid 200001 outside the agreed range 190001..190100']
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

- FREEZE hash: None
- RUN commit: None
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
- preflight stop output: REFUSED: sid 200001 outside the agreed range 190001..190100 | 

## Model calls (gemini-3.1-flash-lite, temperature 0, thinkingBudget 0)

- final started: None; runner exit None; FINAL_RUN_DONE False
- lines: 0
- counted_http200: 0
- uncounted_retries: 0
- uncounted_by_http: {}
- failed_empty_or_unparsable_200: 0
- tokens_in: 0
- tokens_out: 0
- models: {}
- spend_usd_list_price: 0.0
- phase total counted (194 §3 + this run): 194 of the 1,200 hard cap
- access log (verbatim): phase1w/a4/run/access_log.jsonl; call log: phase1w/a4/run/calls.jsonl
