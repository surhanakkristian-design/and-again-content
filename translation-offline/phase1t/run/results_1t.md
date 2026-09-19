# Phase 1T — the fresh set, frozen stack minus lever 1, AG v3 before L3

* items **900**, planned model calls **570**, AG rejections before L3 **128**
* coverage k/n **[389, 421]**, false accepts k/n **[16, 479]** (intervals: score_1t.py)

## AG v3 and its shadows

```
{
 "abstain_agentless_passive": 161,
 "errors": 0,
 "fired_v2": 67,
 "fired_v2_not_v3": 15,
 "fired_v3": 128,
 "fired_v3_by": 67,
 "fired_v3_clause": 125,
 "fired_v3_not_v2": 76,
 "fired_v3_subj": 94,
 "items": 900
}
```

## accept table

```
{
 "accept/correct": 389,
 "accept/wrong": 16,
 "reject/correct": 32,
 "reject/wrong": 463
}
```

Rows: `results_1t.json`.  Every figure with intervals: `python3 score_1t.py`.
