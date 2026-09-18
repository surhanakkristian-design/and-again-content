# Phase 1f — four offline fixes x {P-B, P-C}, gemini-3.1-flash-lite

Baseline reproduced: P-B no flags = 177/235.

| row | variant | flags | coverage /235 | correct / with tip | FA raw | FA REAL | FA by type (raw) | L1/L2/L3 correct | F3/F4 kills | failed |
|---|---|---|---|---|---|---|---|---|---|---|
| Phase 1e baseline (P-B, no flags) | P-B | - | 177 (75.3 %) | 169 / 8 | 22 | 13 (12.4 %) | {"M": 13, "T": 6, "S": 3} | 100/48/87 | 0/0 | 0 |
| +F1 | P-B | F1 | 203 (86.4 %) | 193 / 10 | 24 | 14 (13.3 %) | {"M": 13, "T": 6, "W": 2, "S": 3} | 100/18/117 | 0/0 | 0 |
| +F2 | P-B | F2 | 193 (82.1 %) | 169 / 24 | 22 | 13 (12.4 %) | {"M": 13, "T": 6, "S": 3} | 100/31/104 | 0/0 | 0 |
| +F3 | P-B | F3 | 177 (75.3 %) | 169 / 8 | 15 | 7 (6.7 %) | {"M": 6, "T": 6, "S": 3} | 100/48/87 | 0/0 | 0 |
| +F4 | P-B | F4 | 176 (74.9 %) | 169 / 7 | 20 | 11 (10.5 %) | {"M": 13, "T": 6, "S": 1} | 100/46/86 | 0/3 | 0 |
| F1+F2 | P-B | F1F2 | 217 (92.3 %) | 193 / 24 | 24 | 14 (13.3 %) | {"M": 13, "T": 6, "W": 2, "S": 3} | 100/3/132 | 0/0 | 0 |
| all four | P-B | F1F2F3F4 | 214 (91.1 %) | 193 / 21 | 15 | 6 (5.7 %) | {"M": 6, "T": 6, "W": 2, "S": 1} | 100/3/129 | 0/3 | 0 |
| all four with P-C | P-C | F1F2F3F4 | 219 (93.2 %) | 204 / 15 | 17 | 8 (7.6 %) | {"M": 7, "T": 6, "W": 2, "S": 2} | 100/3/129 | 0/3 | 0 |
| best found (NONE qualifies at <=2 real FA; lowest-FA row shown) | P-B | F2F3F4 | 190 (80.9 %) | 169 / 21 | 13 | 5 (4.8 %) | {"M": 6, "T": 6, "S": 1} | 100/31/101 | 0/3 | 0 |

## F3 / F4 offline cost and savings
```
{
 "F3": {
  "cost_on_235": {
   "total": 0,
   "would_otherwise_be_accepted": 0,
   "rejected_anyway": 0
  },
  "savings_on_105": {
   "total": 14,
   "real_savings_was_accepted": 7,
   "already_rejected": 7
  }
 },
 "F4": {
  "cost_on_235": {
   "total": 3,
   "would_otherwise_be_accepted": 3,
   "rejected_anyway": 0
  },
  "savings_on_105": {
   "total": 13,
   "real_savings_was_accepted": 2,
   "already_rejected": 11
  }
 }
}
```

## Cost
```
{
 "calls_1f": 252,
 "lat_median_ms": 865,
 "lat_p95_ms": 1193,
 "tokens_avg": {
  "in": 177.12301587301587,
  "out": 1.0,
  "thoughts": 0.0,
  "cached": 0.0
 },
 "measured_spend_usd": null,
 "measured_spend_note": "free tier: $0 billed; the figures below are list-price equivalents",
 "list_price_per_call_usd": 4.5780753968253965e-05,
 "price": {
  "in": 0.25,
  "out": 1.5,
  "cached": 0.025,
  "src": "task brief"
 },
 "best_row_L3_share_of_correct": 0.43,
 "usd_per_active_user_per_month": 0.01180559017223911,
 "cost_assumptions": "1e cost_block: 20 exercises/day x 30 days x the best row's L3 share of the correct-answer distribution; Flash-Lite $0.25 in / $1.50 out / $0.025 cached per 1M"
}
```

## Best row
```
{"F1": false, "F2": true, "F3": true, "F4": true}
```
190/235 = 80.9 %, real FA 5

Remaining false rejections of the best row: 45 (ids and text in the json).
