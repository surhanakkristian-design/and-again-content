# Phase 1O - Task B: blind re-judge of the closed 1N set with `topic` restored

0 model calls, no network. Script `phase1o/diag/taskB_rejudge.py`, numbers `phase1o/taskB_results.json`. Intervals: exact Clopper-Pearson 95 %. The apparatus was pre-flighted: with the ORIGINAL labels it reproduces 350/426 and 14/474 and both published intervals exactly; old K-vs-J control disagreement reproduces 3/80 = 3.75 % [0.78, 10.57] (1N reported 3/80).

## 0. The bad news first

1. **The labels explain +1.45 of the 6.93 points** (coverage under the re-judged labels 347/415 = 83.61 % [79.70, 87.05] against 1N 350/426 = 82.16 % [78.19, 85.68]; paired sentence bootstrap of the difference [+0.31, +2.70], 2000 draws, 100 sentences). The bootstrap interval excludes 0.
2. **The hypothesis (a topic-less judge passed marginal answers, depressing coverage and flattering FA together) is SUPPORTED by this data.** It needs movement that is predominantly correct->wrong AND concentrated on stack-rejected items. Movement: correct->wrong 12, wrong->correct 1 (two-sided sign test p = 0.0034) - predominance holds. Concentration: 9/12 = 75.00 % [42.81, 94.51] of the correct->wrong items were stack-rejected, against a base rate of 76/426 = 17.84 % [14.32, 21.81] among all 1N judged-correct items - concentration holds (lower bound above the base rate).
3. **FA is worse under the new labels, which is what the hypothesis predicts: 17/485 = 3.51 % [2.05, 5.55] against 1N 14/474 = 2.95 % [1.62, 4.91].** 3 of the 12 correct->wrong items were stack-ACCEPTED and become new false accepts; 1 of the 1 wrong->correct items were stack-rejected (new false rejections), 0 were stack-accepted.
4. **The AMOUNT of movement (13/900 = 1.44 % [0.77, 2.46] of items) is no larger than the noise yardsticks; only its DIRECTION (item 2) stands out, and its effect on coverage is small (item 1).** New controls K vs their J twins under the new labels 2/80 = 2.50 % [0.30, 8.74] (same session, twins in parts 4-5: 0/27 = 0.00 % [0.00, 12.77]; across the two sessions, twins in parts 1-3: 2/53 = 3.77 % [0.46, 12.98]); new K vs old K 1/80 = 1.25 % [0.03, 6.77]; 1N baselines 3/80 = 3.75 % (same-session verdict disagreement) and 2/80 = 2.5 % (cross-session filler drift). A single re-judge cannot separate "topic" from ordinary re-judging noise except through asymmetry and these yardsticks.
5. **Task E cross-check: of the 11 1N false rejections Task E called E4 ("answer really wrong, judge generous"), the blind re-judge flipped 6 to wrong.**

## 1. Movement

| direction | n | stack-accepted | stack-rejected | by writer intent (id prefix) | by type | judge passive tag old>new | by packet |
|---|---|---|---|---|---|---|---|
| correct -> wrong | 12 | 3 | 9 | {'W': 10, 'C': 2} | new type: {'M': 6, 'T': 6} | {'None>None': 12} | {1: 2, 2: 1, 3: 2, 4: 3, 5: 4} |
| wrong -> correct | 1 | 0 | 1 | {'W': 1} | old type: {'S': 1} | {'None>None': 1} | {3: 1} |

Totals: old correct 426, new correct 415, correct under both 414, wrong under both 473. 1N layer of the correct->wrong items: {'F5': 5, 'L3:TIPrej': 1, 'None': 3, 'L3': 3}. The layer of 1N judged-wrong items is not stored per item in the files this task used. Moved by session: parts 1-3 6/540 = 1.11 % [0.41, 2.40] (c2w, w2c = [5, 1]), parts 4-5 7/360 = 1.94 % [0.79, 3.97] (c2w, w2c = [7, 0]). Type disagreement on items wrong under both: 3/473 = 0.63 % [0.13, 1.84].

Concentration: of the 76 false rejections 9/76 = 11.84 % [5.56, 21.29] flipped to wrong; of the 350 accepted-correct 3/350 = 0.86 % [0.18, 2.48] flipped to wrong; of the 14 false accepts 0/14 = 0.00 % [0.00, 23.16] flipped to correct; of the 460 true rejections 1/460 = 0.22 % [0.01, 1.21] flipped to correct.

## 2. Coverage and FA against the new labels

| metric | 1N labels | re-judged labels |
|---|---|---|
| coverage | 350/426 = 82.16 % [78.19, 85.68] | 347/415 = 83.61 % [79.70, 87.05] |
| FA | 14/474 = 2.95 % [1.62, 4.91] | 17/485 = 3.51 % [2.05, 5.55] |
| coverage, items correct under BOTH labelings | - | 347/414 = 83.82 % [79.91, 87.23] |
| FA, items wrong under BOTH labelings | - | 14/473 = 2.96 % [1.63, 4.92] |
| coverage, new-correct items without a new-judge passive tag | - | 263/310 = 84.84 % [80.35, 88.64] |

| FA by type | 1N labels (old type) | re-judged labels (new type) |
|---|---|---|
| M | 3/95 = 3.16 % [0.66, 8.95] | 4/102 = 3.92 % [1.08, 9.74] |
| S | 3/97 = 3.09 % [0.64, 8.77] | 3/97 = 3.09 % [0.64, 8.77] |
| T | 4/188 = 2.13 % [0.58, 5.36] | 6/191 = 3.14 % [1.16, 6.71] |
| W | 4/94 = 4.26 % [1.17, 10.54] | 4/95 = 4.21 % [1.16, 10.43] |

## 3. Noise yardsticks

* preflight_old_K_vs_old_J (1N reported 3/80): 3/80 = 3.75 % [0.78, 10.57]
* new_K_vs_new_J_all: 2/80 = 2.50 % [0.30, 8.74]
* new_K_vs_new_J_same_session(parts4-5): 0/27 = 0.00 % [0.00, 12.77]
* new_K_vs_new_J_cross_session(parts1-3): 2/53 = 3.77 % [0.46, 12.98]
* new_K_vs_old_K: 1/80 = 1.25 % [0.03, 6.77]
* new_J_vs_old_J_on_the_80_twins: 0/80 = 0.00 % [0.00, 4.51]
* type_disagreement_both_wrong: 3/473 = 0.63 % [0.13, 1.84]
* direction new K vs old K (correct->wrong, wrong->correct): [1, 0]
* 1N `judge_noise` block verbatim: `{"controls_compared": 80, "judged_disagreements": {"k": 3, "n": 80, "pct": 3.75, "ci": [0.78, 10.57]}, "type_comparisons": 40, "type_disagreements": {"k": 2, "n": 40, "pct": 5.0, "ci": [0.61, 16.92]}, "judged_disagreement_ids": ["W:160066:3107568222", "W:160088:1164202144", "W:160088:148507747"], "type_disagreement_ids": ["W:160008:1985746104", "W:160012:1057727893"], "caveat": "same-session duplicates bound within-session inconsistency only"}`

## 4. Task E cross-check

Flipped to wrong by the blind re-judge, per Task E bucket of the 76 1N false rejections: {"E1": {"flipped": 0, "n": 3}, "E2": {"flipped": 0, "n": 35}, "E3": {"flipped": 0, "n": 18}, "E4": {"flipped": 6, "n": 11}, "E5": {"flipped": 3, "n": 9}}. E4 ids flipped: ['W:160021:356150325', 'W:160042:2501266784', 'W:160053:337807729', 'W:160072:3478128531', 'W:160079:812730797', 'W:160096:962295857']. E4 ids kept correct: ['C:160035:1168408523', 'C:160053:703629798', 'W:160013:1795021316', 'W:160066:3107568222', 'W:160076:167794355'].

## 5. Caveats

* The judge agent/model of 1N and of 1M is recorded nowhere we could find; judge identity is an uncontrolled difference between the labelings.
* 2 judge sessions here (parts 1-3; parts 4-5 + controls) against 5 packets in 1N; the controls sat in the second session, so K-vs-J is within-session only for twins in parts 4-5.
* One judge revised part 1 once (J0081 and J0152 re-levelled, both now correct).
* A single re-judge cannot separate "topic" from ordinary re-judging noise except through the asymmetry of the movement and the yardsticks above.
* Stack verdicts are the STORED 1N verdicts (results_1n.json `fr_ids` / `fa_ids`); nothing was re-run. Writer intent is the id prefix. The passive tag shown is the judge tag (old>new); the writer passive key was not read.
* The sign test and Clopper-Pearson intervals treat items as independent; items cluster in 100 sentences (the bootstrap line resamples sentences).
