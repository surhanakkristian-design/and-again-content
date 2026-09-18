# Phase 1i — TASK A: an L3 "TIP" counted as a rejection (zero model calls)

Whole Phase 1h fresh set, **DEV + HOLDOUT together** (this is a re-scoring of an already-made
measurement, not a design decision taken on the holdout). Headline row = **row 7 (P-B)**, the row
that produced the 82.1 % coverage and 12.0 % false acceptance of the Phase 1h report; row 8 (P-C) is
shown because it is free, but it stays **void** (report §5 D3: 311 empty replies).

**This flips an existing switch — it adds no rule.** `checker_1h.decide()` (lines 853-855) maps a
model reply of `TIP` to `verdict='correct_with_tip', accepted=True`. Task A asks only what the frozen
measurement would have said if that single branch rejected instead. Nothing else is changed; no prompt,
threshold, layer, word list or annotation is touched and no call was made.

## HEADLINE

**The 66 real false acceptances of row 7 were accepted by:**

| accepted by | n |
|---|---|
| L3 model reply **TIP** | 42 |
| L3 model reply **SAME** | 23 |
| an **offline** layer (L1) | 1 |
| **total** | 66 |

**The 345 accepted correct answers of row 7 were accepted by:**

| accepted by | n |
|---|---|
| L3 model reply **TIP** | 21 |
| L3 model reply **SAME** | 189 |
| an **offline** layer (L1) | 135 |
| **total** | 345 |

(of the L3 SAME accepts, 5 carried an F2-released tip, i.e. `correct_with_tip` without a model TIP; they are NOT touched by this switch.)

## Before / after, row 7 (P-B)

| figure | before | after (TIP = reject) | change |
|---|---|---|---|
| coverage (n = 420 judged really correct) | 345/420 = 82.1 % [78.1–85.7] | 324/420 = 77.1 % [72.8–81.1] | -5.0 pp |
| real false acceptance (n = 550 judged really wrong) | 66/550 = 12.0 % [9.4–15.0] | 24/550 = 4.4 % [2.8–6.4] | -7.6 pp |

### By wrong type (false acceptance, row 7)

| type | before | after |
|---|---|---|
| T | 2/137 = 1.5 % [0.2–5.2] | 1/137 = 0.7 % [0.0–4.0] |
| W | 17/138 = 12.3 % [7.3–19.0] | 4/138 = 2.9 % [0.8–7.3] |
| M | 27/135 = 20.0 % [13.6–27.8] | 8/135 = 5.9 % [2.6–11.3] |
| S | 20/140 = 14.3 % [8.9–21.2] | 11/140 = 7.9 % [4.0–13.6] |

### By sentence half (row 7)

| half | coverage before | coverage after | FA before | FA after |
|---|---|---|---|---|
| OLD (the 80 in-sample sentences) | 185/240 = 77.1 % [71.2–82.2] | 177/240 = 73.8 % [67.7–79.2] | 37/317 = 11.7 % [8.3–15.7] | 15/317 = 4.7 % [2.7–7.7] |
| NEW (the 60 fresh sentences) | 160/180 = 88.9 % [83.4–93.1] | 147/180 = 81.7 % [75.2–87.0] | 29/233 = 12.4 % [8.5–17.4] | 9/233 = 3.9 % [1.8–7.2] |

### DEV / HOLDOUT aggregates (row 7, counts only — no item is listed)

| side | coverage before | coverage after | FA before | FA after |
|---|---|---|---|---|
| dev | 160/203 = 78.8 % [72.5–84.2] | 149/203 = 73.4 % [66.8–79.3] | 30/260 = 11.5 % [7.9–16.1] | 8/260 = 3.1 % [1.3–6.0] |
| holdout | 185/217 = 85.3 % [79.8–89.7] | 175/217 = 80.6 % [74.8–85.7] | 36/290 = 12.4 % [8.8–16.8] | 16/290 = 5.5 % [3.2–8.8] |

## Row 8 (P-C) — VOID, quoted for completeness only

| figure | before | after |
|---|---|---|
| coverage | 350/420 = 83.3 % [79.4–86.8] | 343/420 = 81.7 % [77.6–85.2] |
| real false acceptance | 8/550 = 1.5 % [0.6–2.9] | 3/550 = 0.5 % [0.1–1.6] |

Row 8 has 310 failed calls and 277 items with no parsed verdict (report §5 D3); its numbers are artefacts of missing verdicts and must not be quoted.

## Sanity

- row 7 before reproduces Phase 1h exactly: coverage 345/420 = 82.1 %, real FA 66/550 = 12.0 %
- row 7 failed calls 0, items reaching L3 without a parsed verdict 23 (Phase 1h reported 23 fresh items without a verdict).
- intervals: exact Clopper-Pearson, `scipy.stats.beta` when importable, otherwise a pure-python bisection on the binomial CDF (both implemented in this script; the numbers above say which ran: the values are identical to 2 decimals either way).

## Reading

- The TIP branch is the single cheapest lever in the whole checker: it removes 42 of the 66 false acceptances (7.6 pp) at a cost of 21 of the 345 accepted correct answers (5.0 pp of coverage).
- It is a pure trade, not a free win: judge it against the product decision (assistive hint layer vs autonomous gate), not against one number.

