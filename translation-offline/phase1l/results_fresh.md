# Phase 1L — FRESH results (the one measurement of the frozen Phase 1k configuration)

Freeze commit `994e045d01dc0930df0415581ca29449c093bfa1`. Frozen config: **LOCKTIP+F8+F9 (ALL) / P-FROZEN / TIP-as-rejection on** (F8 True, F9 True, REPORTED_STRICT False). Every figure is numerator/denominator, point, exact 95 % Clopper-Pearson interval. Columns are never averaged.

| metric | (a) all 600, after hygiene | (b) excl. sid 140006, after hygiene | (c) all 600, BEFORE hygiene | (d) excl. sid 140006, before hygiene |
|---|---|---|---|---|
| coverage | 191/217 = 88.02% [82.94, 92.02] | 188/214 = 87.85% [82.71, 91.91] | 191/217 = 88.02% [82.94, 92.02] | 188/214 = 87.85% [82.71, 91.91] |
| coverage (kind C) | 189/209 = 90.43% [85.61, 94.06] | 186/206 = 90.29% [85.40, 93.97] | 189/209 = 90.43% [85.61, 94.06] | 186/206 = 90.29% [85.40, 93.97] |
| FA | 15/383 = 3.92% [2.21, 6.38] | 14/377 = 3.71% [2.04, 6.15] | 15/383 = 3.92% [2.21, 6.38] | 14/377 = 3.71% [2.04, 6.15] |
| FA type T | 3/130 = 2.31% [0.48, 6.60] | 3/128 = 2.34% [0.49, 6.70] | 3/130 = 2.31% [0.48, 6.60] | 3/128 = 2.34% [0.49, 6.70] |
| FA type W | 1/70 = 1.43% [0.04, 7.70] | 1/69 = 1.45% [0.04, 7.81] | 1/70 = 1.43% [0.04, 7.70] | 1/69 = 1.45% [0.04, 7.81] |
| FA type M | 2/68 = 2.94% [0.36, 10.22] | 2/67 = 2.99% [0.36, 10.37] | 2/68 = 2.94% [0.36, 10.22] | 2/67 = 2.99% [0.36, 10.37] |
| FA type S | 1/70 = 1.43% [0.04, 7.70] | 1/69 = 1.45% [0.04, 7.81] | 1/70 = 1.43% [0.04, 7.70] | 1/69 = 1.45% [0.04, 7.81] |
| FA type V | 8/44 = 18.18% [8.19, 32.71] | 7/43 = 16.28% [6.81, 30.70] | 8/44 = 18.18% [8.19, 32.71] | 7/43 = 16.28% [6.81, 30.70] |
| FA type E | 0/1 = 0.00% [0.00, 97.50] | 0/1 = 0.00% [0.00, 97.50] | 0/1 = 0.00% [0.00, 97.50] | 0/1 = 0.00% [0.00, 97.50] |

## FA by layer (denominator = all items judged wrong)

**(a) all 600, after hygiene**

```
{
 "L3": "15/383 = 3.92% [2.21, 6.38]"
}
```

**(b) excl. sid 140006, after hygiene**

```
{
 "L3": "14/377 = 3.71% [2.04, 6.15]"
}
```

**(c) all 600, BEFORE hygiene**

```
{
 "L3": "15/383 = 3.92% [2.21, 6.38]"
}
```

**(d) excl. sid 140006, before hygiene**

```
{
 "L3": "14/377 = 3.71% [2.04, 6.15]"
}
```

## False rejections by layer (denominator = all items judged correct)

**(a) all 600, after hygiene**

```
{
 "F2B": "2/217 = 0.92% [0.11, 3.29]",
 "F4v2": "1/217 = 0.46% [0.01, 2.54]",
 "F9": "3/217 = 1.38% [0.29, 3.99]",
 "L3": "11/217 = 5.07% [2.56, 8.89]",
 "L3:TIPrej": "9/217 = 4.15% [1.91, 7.73]"
}
```

**(b) excl. sid 140006, after hygiene**

```
{
 "F2B": "2/214 = 0.93% [0.11, 3.34]",
 "F4v2": "1/214 = 0.47% [0.01, 2.58]",
 "F9": "3/214 = 1.40% [0.29, 4.04]",
 "L3": "11/214 = 5.14% [2.59, 9.01]",
 "L3:TIPrej": "9/214 = 4.21% [1.94, 7.83]"
}
```

**(c) all 600, BEFORE hygiene**

```
{
 "F2B": "2/217 = 0.92% [0.11, 3.29]",
 "F4v2": "1/217 = 0.46% [0.01, 2.54]",
 "F9": "3/217 = 1.38% [0.29, 3.99]",
 "L3": "11/217 = 5.07% [2.56, 8.89]",
 "L3:TIPrej": "9/217 = 4.15% [1.91, 7.73]"
}
```

**(d) excl. sid 140006, before hygiene**

```
{
 "F2B": "2/214 = 0.93% [0.11, 3.34]",
 "F4v2": "1/214 = 0.47% [0.01, 2.58]",
 "F9": "3/214 = 1.40% [0.29, 4.04]",
 "L3": "11/214 = 5.14% [2.59, 9.01]",
 "L3:TIPrej": "9/214 = 4.21% [1.94, 7.83]"
}
```

## The two named cells

```
{
 "ACTIVE->PASSIVE (intent V)": {
  "judged_wrong": 43,
  "accepted": 8,
  "rate": {
   "k": 8,
   "n": 43,
   "pct": 18.6,
   "ci": [
    8.39,
    33.4
   ]
  },
  "rejecting_layers": {
   "F8": 11,
   "L3": 20,
   "F4v2": 4
  },
  "accepted_ids": [
   "W:140006:98216243",
   "W:140014:1487151881",
   "W:140024:670820885",
   "W:140037:1538470541",
   "W:140041:1273097874",
   "W:140058:4156271032",
   "W:140060:2368276709",
   "W:140064:225979015"
  ]
 },
 "TIME-FRAME-SHIFT (intent TF)": {
  "judged_wrong": 66,
  "accepted": 0,
  "rate": {
   "k": 0,
   "n": 66,
   "pct": 0.0,
   "ci": [
    0.0,
    5.44
   ]
  },
  "rejecting_layers": {
   "L3": 64,
   "F5": 1,
   "L3:TIPrej": 1
  },
  "accepted_ids": []
 }
}
```

## Targets — per column, on the point and on the interval (never averaged)

| target | (a) all 600, after hygiene | (b) excl. sid 140006, after hygiene | (c) all 600, BEFORE hygiene | (d) excl. sid 140006, before hygiene |
|---|---|---|---|---|
| coverage >= 90% | point not met / interval not met | point not met / interval not met | point not met / interval not met | point not met / interval not met |
| FA < 5% | point MET / interval not met | point MET / interval not met | point MET / interval not met | point MET / interval not met |
| type-T FA < 5% | point MET / interval not met | point MET / interval not met | point MET / interval not met | point MET / interval not met |

## §5 accounting

```
{
 "lock_released": {
  "rejected_at_L2_under_BASE": 150,
  "released_by_LOCKTIP_total": 0,
  "released_judged_correct": 0,
  "released_judged_wrong_by_type": {}
 },
 "guard_cost": {
  "F8": {
   "caught_wrong": 11,
   "caught_wrong_only_this_guard": 9,
   "own_cost_correct_rejected": 0,
   "caught_ids": [
    "W:140001:3226349339",
    "W:140003:312397117",
    "W:140005:3877298044",
    "W:140012:213263887",
    "W:140020:3008526410",
    "W:140021:1964329415",
    "W:140026:3932510212",
    "W:140028:954872054",
    "W:140029:1352870231",
    "W:140048:331087784",
    "W:140050:2745100486"
   ],
   "cost_ids": [],
   "basis": "on top of LOCKTIP with the model layer present"
  },
  "F9": {
   "caught_wrong": 2,
   "caught_wrong_only_this_guard": 0,
   "own_cost_correct_rejected": 3,
   "caught_ids": [
    "W:140020:3008526410",
    "W:140048:331087784"
   ],
   "cost_ids": [
    "C:140009:3398740870",
    "C:140048:2590293579",
    "C:140069:856625898"
   ],
   "basis": "on top of LOCKTIP with the model layer present"
  }
 },
 "b3_tip_abstain": {
  "tip": {
   "n": 199,
   "judged_correct": 102,
   "judged_wrong": 97,
   "cost_type_T_wrong_accepted": 3
  },
  "abstain": {
   "n": 54,
   "judged_correct": 17,
   "judged_wrong": 37,
   "cost_type_T_wrong_accepted": 0
  }
 },
 "unpatched_guard_bugs_5_4": {
  "1 F8 fires only on an English passive main clause": {
   "still_fires": true,
   "count": 8,
   "sids": [
    140006,
    140014,
    140024,
    140037,
    140041,
    140058,
    140060,
    140064
   ],
   "ids": [
    "W:140006:98216243",
    "W:140014:1487151881",
    "W:140024:670820885",
    "W:140037:1538470541",
    "W:140041:1273097874",
    "W:140058:4156271032",
    "W:140060:2368276709",
    "W:140064:225979015"
   ],
   "measured_as": "items judged wrong with writer intent V that the frozen stack accepted and F8 did not reject"
  },
  "2 F9 inert on DEV, REPORTED_STRICT frozen untested": {
   "still_fires": true,
   "items_where_strict_changes_F9": 0,
   "ids": [],
   "measured_as": "F9 readout with REPORTED_STRICT True vs the frozen False; 0 = the switch is still untested on this side"
  },
  "3 F2B not applied to lock-released items": {
   "still_fires": false,
   "count": 0,
   "sids": [],
   "ids": [],
   "measured_as": "items LOCKTIP released, which F2B never sees"
  },
  "4 an L2 step==\"mistake\" rejection is not released": {
   "still_fires": false,
   "count": 0,
   "sids": [],
   "ids": [],
   "measured_as": "items whose computed chk step is \"mistake\""
  }
 },
 "patched": "NONE — all four are recorded and deliberately left unpatched.",
 "hygiene": {
  "files": [
   "out_fresh_1.json"
  ],
  "sids_touched": [
   140022,
   140024,
   140032
  ],
  "references_removed": 2,
  "references_replaced": 1,
  "display_reference_changed": 0,
  "reference_kept_because_nothing_survived": [],
  "examples": [
   {
    "sid": 140022,
    "reference_before": "You were waiting on the platform when it started raining.",
    "reference_after": "You were waiting on the platform when it started raining.",
    "v_before": [
     "You were waiting on the platform when it started raining.",
     "You waited on the platform when it started raining."
    ],
    "v_after": [
     "You were waiting on the platform when it started raining."
    ],
    "reason": "Simple past with \"when\" reads as sequence (waited after the rain began), losing the interrupted ongoing action of the imperfective \"si čakal\"; the correct progressive variant is already stored."
   },
   {
    "sid": 140024,
    "reference_before": "He was fixing that lawnmower all afternoon and in the end he gave up.",
    "reference_after": "He was fixing that lawnmower all afternoon and in the end he gave up.",
    "v_before": [
     "He was fixing that lawnmower all afternoon and in the end he gave up.",
     "He fixed that lawnmower all afternoon and in the end he gave up."
    ],
    "v_after": [
     "He was fixing that lawnmower all afternoon and in the end he gave up."
    ],
    "reason": "\"fixed\" asserts a completed successful repair, which contradicts \"gave up\" and mistranslates the imperfective \"opravoval\"; the progressive variant is already stored."
   },
   {
    "sid": 140032,
    "reference_before": "She asked me whether I could use that program.",
    "reference_after": "She asked me whether I could use that program.",
    "v_before": [
     "She asked me whether I could use that program.",
     "She asked me if I knew that program."
    ],
    "v_after": [
     "She asked me whether I could use that program.",
     "She asked me if I knew how to use that program."
    ],
    "reason": "\"ovládam ten program\" means being able to operate the program, not merely being acquainted with it, so \"knew that program\" shifts the meaning."
   }
  ]
 },
 "builder_2_1": {
  "chk_computed_fresh": {
   "match": 39,
   "auto": 561
  },
  "chk_computed_before_hygiene": {
   "match": 39,
   "auto": 561
  }
 }
}
```

## F9 hand-check on the 70 fresh sentences (against the stored tf_gold)

```
{
 "agree": 51,
 "conservative": 19,
 "error": 0,
 "errors": [],
 "n": 70,
 "error_rate": {
  "k": 0,
  "n": 70,
  "pct": 0.0,
  "ci": [
   0.0,
   5.13
  ]
 }
}
```

## Model calls

```
{
 "counted_calls_http200": 460,
 "failed_empty_200": 0,
 "non200_attempts": 0,
 "tokens_in": 99509,
 "tokens_out": 460,
 "spend_usd": 0.02557,
 "phase_budget_remaining_estimate": 873,
 "caveat": "billed versus free-tier is NOT detectable from the response body; these are list-price figures for the tokens the API reported.",
 "planned_new": 460,
 "made": {
  "ok": 460,
  "bad": 0
 },
 "reused": 0,
 "unique_requests": 460
}
```

## Preflight

```
{
 "lock_rejections_BASE_before": 150,
 "lock_rejections_BASE_after": 150,
 "l3_eligible_before": 460,
 "l3_eligible_after": 460
}
```

