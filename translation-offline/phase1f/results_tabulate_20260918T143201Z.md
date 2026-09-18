# Phase 1f — four offline fixes x {P-B, P-C}, gemini-3.1-flash-lite

Baseline reproduced: P-B no flags = 177/235.

| row | variant | flags | coverage /235 | correct / with tip | FA raw | FA REAL | FA by type (raw) | L1/L2/L3 correct | F3/F4 kills | failed |
|---|---|---|---|---|---|---|---|---|---|---|
| Phase 1e baseline (P-B, no flags) | P-B | - | 177 (75.3 %) | 169 / 8 | 22 | 13 (12.4 %) | {"M": 13, "T": 6, "S": 3} | 100/48/87 | 0/0 | 0 |
| +F1 | P-B | F1 | 177 (75.3 %) | 169 / 8 | 22 | 13 (12.4 %) | {"M": 13, "T": 6, "S": 3} | 100/18/117 | 0/0 | 39 |
| +F2 | P-B | F2 | 177 (75.3 %) | 169 / 8 | 22 | 13 (12.4 %) | {"M": 13, "T": 6, "S": 3} | 100/31/104 | 0/0 | 17 |
| +F3 | P-B | F3 | 177 (75.3 %) | 169 / 8 | 15 | 7 (6.7 %) | {"M": 6, "T": 6, "S": 3} | 100/48/87 | 0/0 | 0 |
| +F4 | P-B | F4 | 176 (74.9 %) | 169 / 7 | 21 | 12 (11.4 %) | {"M": 13, "T": 6, "S": 2} | 100/46/86 | 0/3 | 0 |
| F1+F2 | P-B | F1F2 | 177 (75.3 %) | 169 / 8 | 22 | 13 (12.4 %) | {"M": 13, "T": 6, "S": 3} | 100/3/132 | 0/0 | 54 |
| all four | P-B | F1F2F3F4 | 176 (74.9 %) | 169 / 7 | 14 | 6 (5.7 %) | {"M": 6, "T": 6, "S": 2} | 100/3/129 | 0/3 | 52 |
| all four with P-C | P-C | F1F2F3F4 | 100 (42.6 %) | 97 / 3 | 8 | 0 (0.0 %) | {"M": 1, "T": 6, "S": 1} | 100/3/129 | 0/3 | 175 |
| best found | P-C | - | 100 (42.6 %) | 97 / 3 | 9 | 0 (0.0 %) | {"M": 2, "T": 6, "S": 1} | 100/48/87 | 0/0 | 144 |

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
   "would_otherwise_be_accepted": 1,
   "rejected_anyway": 2
  },
  "savings_on_105": {
   "total": 8,
   "real_savings_was_accepted": 1,
   "already_rejected": 7
  }
 }
}
```

## Cost
```
{
 "calls_1f": 0,
 "lat_median_ms": null,
 "lat_p95_ms": null,
 "tokens_avg": {
  "in": 0,
  "out": 0,
  "thoughts": 0,
  "cached": 0
 },
 "measured_spend_usd": 0.0,
 "measured_spend_note": "free tier: $0 billed; the figures below are list-price equivalents",
 "list_price_per_call_usd": 0.0,
 "price": {
  "in": 0.25,
  "out": 1.5,
  "cached": 0.025,
  "src": "task brief"
 },
 "best_row_L3_share_of_correct": 0.37,
 "usd_per_active_user_per_month": null,
 "cost_assumptions": "1e cost_block: 20 exercises/day x 30 days x the best row's L3 share of the correct-answer distribution; Flash-Lite $0.25 in / $1.50 out / $0.025 cached per 1M"
}
```

## Best row
```
{"F1": false, "F2": false, "F3": false, "F4": false}
```
100/235 = 42.6 %, real FA 0

Remaining false rejections of the best row: 135 (ids and text in the json).
