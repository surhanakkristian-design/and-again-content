# Phase 1i — DEV / HOLDOUT split of the Phase 1h fresh set

Produced by `phase1i/make_split.py` (zero model calls). Source: the Phase 1h fresh set as read by
the frozen loader through `phase1h/fresh_io_fix.py` — 420 correct + 560 wrong written answers over
140 sentences (80 OLD in-sample sentences + 60 NEW), judgements from `phase1h/fresh/judgements.jsonl`.

## Rule

```
side = int(sha256(item_id.encode("utf-8")).hexdigest(), 16) % 2      # 0 = DEV, 1 = HOLDOUT
```

Deterministic, id-only, no randomness, no stratification. `item_id` is the frozen Phase 1h id
`C|W:<sid>:<int(md5(answer)[:8],16)>` (`checker_1h._iid`).

## Counts

| figure | DEV | HOLDOUT | total |
|---|---|---|---|
| items | 467 | 513 | 980 |
| correct answers written | 203 | 217 | 420 |
| wrong answers written | 264 | 296 | 560 |
| correct, judged really correct (coverage denominator) | 203 | 217 | 420 |
| wrong, judged really wrong (FA denominator) | 260 | 290 | 550 |
| wrong, judged really CORRECT (excluded from FA) | 4 | 6 | 10 |
| unjudged | 0 | 0 | 0 |

### Wrong answers by type (written / judged really wrong)

| type | DEV | HOLDOUT |
|---|---|---|
| T | 69 / 67 | 71 / 70 |
| W | 70 / 69 | 70 / 69 |
| M | 57 / 56 | 83 / 79 |
| S | 68 / 68 | 72 / 72 |

### Old (the 80 in-sample sentences) vs new (the 60 fresh sentences)

| half | DEV items (C / W) | HOLDOUT items (C / W) |
|---|---|---|
| OLD | 256 (117 / 139) | 304 (123 / 181) |
| NEW | 211 (86 / 125) | 209 (94 / 115) |

## Leakage caveat — RECORDED, NOT FIXED

The split is per ANSWER, not per sentence. **138 of the 140 Slovak sentences (sid) have items on both sides** (1 DEV-only, 1 HOLDOUT-only).
Anything learned on DEV about a particular Slovak sentence, its reference wording or its annotation
therefore transfers to HOLDOUT items of the same sentence. A per-sid split was not used because it
would have made the per-type cells (T/W/M/S) too small to measure; the consequence is that the
HOLDOUT number is an optimistic bound whenever a change is sentence-specific. Any change that is
per-sentence (a hand edit of an annotation, a reference rewrite, a word list keyed to a sid) is
therefore NOT measurable on this holdout and must be declared as such.

sids on both sides: 103, 119, 224, 381, 1018, 1452, 2121, 2389, 2783, 2874, 2929, 3084, 3332, 3494, 3603, 3937, 4449, 4571, 4612, 5595, 5959, 5966, 5971, 6265, 6275, 6353, 6365, 6790, 6830, 6883, 6884, 6971, 6985, 7037, 7238, 7444, 7458, 7465, 7533, 7558, 7687, 7708, 7716, 7752, 7910, 7928, 7998, 8017, 8020, 8039, 8209, 8293, 8465, 8491, 8507, 8618, 8756, 8799, 8812, 8824, 8920, 9007, 9038, 9244, 9495, 9498, 9552, 9584, 9602, 9607, 9687, 9907, 9913, 9966, 9992, 10013, 10043, 10107, 10116, 10124, 10138, 10167, 10179, 10243, 10366, 10574, 10734, 10866, 10959, 11216, 11348, 11540, 11610, 11980, 12831, 13034, 13175, 13395, 14182, 14266, 14697, 14779, 14806, 15437, 15954, 16009, 16261, 16403, 18251, 18789, 18966, 20298, 20435, 20702, 21124, 21467, 21510, 21750, 22427, 23026, 23360, 23669, 23878, 24101, 24733, 24741, 25921, 25981, 26084, 27097, 27628, 28006, 29143, 29691, 31648, 32141, 32342, 32539

## Files

- `split/dev_ids.json`, `split/holdout_ids.json` — sorted id lists
- `split/split_counts.json` — every count above as JSON
- `dev/items.jsonl`, `holdout/items.jsonl` — one line per item (schema in `phase1i/CONTEXT.md`)
- `dev/annotations.json`, `holdout/annotations.json` — sid -> {hygienised, raw} annotation
- `dev/l2_false_rejections.json`, `dev/false_acceptances.json` — row-7 error lists on DEV
- `taskA/scoring_rows.jsonl` — verdict-only rows for both sides (no Slovak, no answers)

