# SCORE_1T — the fresh set (primary labels and S2), 0 model calls

| figure | primary | S2 |
| --- | --- | --- |
| coverage (pooled) | 389/421 = 92.40 % [89.44, 94.74] | 389/421 = 92.40 % [89.44, 94.74] |
| FA (pooled) | 16/479 = 3.34 % [1.92, 5.37] | 16/479 = 3.34 % [1.92, 5.37] |
| coverage P1 | 195/210 = 92.86 % [88.49, 95.95] | 195/210 = 92.86 % [88.49, 95.95] |
| coverage P2 | 194/211 = 91.94 % [87.41, 95.24] | 194/211 = 91.94 % [87.41, 95.24] |
| FA P1 | 5/240 = 2.08 % [0.68, 4.79] | 5/240 = 2.08 % [0.68, 4.79] |
| FA P2 | 11/239 = 4.60 % [2.32, 8.09] | 11/239 = 4.60 % [2.32, 8.09] |
| Fisher P1 vs P2 (coverage) | 0.8544 | 0.8544 |
| Fisher P1 vs P2 (FA) | 0.1363 | 0.1363 |

## cells (primary / S2)

| cell | primary | S2 |
| --- | --- | --- |
| agent_drop_all — false accepts | 13/161 = 8.07 % [4.37, 13.41] | 13/161 = 8.07 % [4.37, 13.41] |
| agent_drop_main — false accepts | 2/65 = 3.08 % [0.37, 10.68] | 2/65 = 3.08 % [0.37, 10.68] |
| agent_drop_embedded — false accepts | 11/96 = 11.46 % [5.86, 19.58] | 11/96 = 11.46 % [5.86, 19.58] |
| by-passive coverage | 80/80 = 100.00 % [95.49, 100.00] | 80/80 = 100.00 % [95.49, 100.00] |
| SKP-sentence coverage | 72/72 = 100.00 % [95.01, 100.00] | 72/72 = 100.00 % [95.01, 100.00] |
| time-frame FA | 1/119 = 0.84 % [0.02, 4.59] | 1/119 = 0.84 % [0.02, 4.59] |

## per level (coverage / FA, primary)

| level | coverage | FA |
| --- | --- | --- |
| A1 | 98/103 = 95.15 % [89.03, 98.41] | 2/122 = 1.64 % [0.20, 5.80] |
| A2 | 95/105 = 90.48 % [83.18, 95.34] | 3/120 = 2.50 % [0.52, 7.13] |
| B1 | 96/107 = 89.72 % [82.35, 94.76] | 6/118 = 5.08 % [1.89, 10.74] |
| B2 | 100/106 = 94.34 % [88.09, 97.89] | 5/119 = 4.20 % [1.38, 9.53] |

## FA by judged type (primary)

| type | FA |
| --- | --- |
| T | 1/119 = 0.84 % [0.02, 4.59] |
| W | 0/72 = 0.00 % [0.00, 4.99] |
| M | 13/209 = 6.22 % [3.35, 10.40] |
| S | 2/79 = 2.53 % [0.31, 8.85] |

## AG v3

```
{
 "fired": 128,
 "catches_judged_wrong": 128,
 "measured_cost_judged_correct": 0,
 "measured_cost_items": [],
 "fired_on_unlabelled": 0
}
```

## AG shadows (v2 and each v3 flag alone)

```
{
 "v2": {
  "fired": 67,
  "catches_judged_wrong": 67,
  "cost_judged_correct": 0,
  "fired_where_v3_did_not": 15,
  "v3_fires_where_it_did_not": 76
 },
 "v3_by": {
  "fired": 67,
  "catches_judged_wrong": 67,
  "cost_judged_correct": 0,
  "fired_where_v3_did_not": 15,
  "v3_fires_where_it_did_not": 76
 },
 "v3_clause": {
  "fired": 125,
  "catches_judged_wrong": 125,
  "cost_judged_correct": 0,
  "fired_where_v3_did_not": 1,
  "v3_fires_where_it_did_not": 4
 },
 "v3_subj": {
  "fired": 94,
  "catches_judged_wrong": 94,
  "cost_judged_correct": 0,
  "fired_where_v3_did_not": 18,
  "v3_fires_where_it_did_not": 52
 }
}
```

## layers

```
{
 "false_rejections_by_layer": {
  "L3:TIPrej": 28,
  "L3": 4
 },
 "false_accepts_by_layer": {
  "L3": 16
 },
 "true_rejections_by_layer": {
  "L3": 238,
  "AG": 128,
  "F5": 45,
  "L3:TIPrej": 49,
  "F3": 3
 }
}
```

## judge noise (the 80 duplicate controls)

```
{
 "key": "judge/_private/_key.json",
 "verdict_files": 4,
 "verdict_rows": 980,
 "items_labelled": 900,
 "unlabelled_items": 0,
 "missing_verdicts": 0,
 "duplicate_controls": 80,
 "duplicate_controls_judged": 80,
 "label_disagreements": 0,
 "judge_noise_pct": 0.0,
 "type_only_disagreements": 0,
 "judged": {
  "wrong": 479,
  "correct": 421
 },
 "types": {
  "T": 119,
  "M": 209,
  "S": 79,
  "W": 72
 }
}
```

