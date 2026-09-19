# Phase 1T — the fresh set, frozen stack minus lever 1, AG v3 before L3

* items **8**, planned model calls **6**, AG rejections before L3 **2**
* coverage k/n **[3, 3]**, false accepts k/n **[0, 5]** (intervals: score_1t.py)

## AG v3 and its shadows

```
{
 "abstain_agentless_passive": 1,
 "errors": 0,
 "fired_v2": 2,
 "fired_v2_not_v3": 0,
 "fired_v3": 2,
 "fired_v3_by": 2,
 "fired_v3_clause": 2,
 "fired_v3_not_v2": 0,
 "fired_v3_subj": 2,
 "items": 8
}
```

## accept table

```
{
 "accept/correct": 3,
 "reject/wrong": 5
}
```

Rows: `results_1t.json`.  Every figure with intervals: `python3 score_1t.py`.
