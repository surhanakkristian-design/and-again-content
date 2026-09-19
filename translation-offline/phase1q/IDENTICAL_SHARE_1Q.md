# Phase 1Q - identical-to-reference share, asserted BEFORE the 1P set is opened

Definition, one definition for both sets: an item counts if it is **judged correct** and its
sentence carries at least one stored rendering. The answer is normalised (NFKC, lowercase, every
punctuation character -> space, whitespace collapsed) and compared for equality with `v[0]` (the
reference) and, separately, with ANY stored rendering. 0 model calls, labels unchanged.

| set | n (judged correct) | == v[0] | pct | == any rendering | pct |
|---|---|---|---|---|---|
| 1P fresh | 599 | 65 | 10.85 | 83 | 13.86 |
| 1N closed | 426 | 25 | 5.87 | 33 | 7.75 |

1P's report quoted "29 of 400" for 1N's v[0] share. Recomputed on the definition above the 1N
denominator is **426 judged-correct items** (1N: 900 items, 426 judged correct, all with a
reference), not 400, and the v[0] count is **25** (5.87 pct), 33 (7.75 pct) against any
rendering. The 1P set is about twice as literal as 1N on this measure.

Raw: [{"set": "1P fresh", "n_judged_correct_with_reference": 599, "identical_to_v0": 65, "pct_v0": 10.85, "identical_to_any_rendering": 83, "pct_any": 13.86}, {"set": "1N closed", "n_judged_correct_with_reference": 426, "identical_to_v0": 25, "pct_v0": 5.87, "identical_to_any_rendering": 33, "pct_any": 7.75}]
