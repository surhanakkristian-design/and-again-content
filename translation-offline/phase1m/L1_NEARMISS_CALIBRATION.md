# Phase 1M — carry-check 2: `l1_nearmiss` calibrated against production L1 on DEV

Label `carry`. Generated 2026-09-19T07:11:43Z by `phase1m/l1_nearmiss_calibration.py`. **0 model calls.** Predicate: imported from runner_1m.l1_nearmiss.

Side: `build_side('dev', hyg_on=False)` — **490 records / 70 sentences**, the only side whose records carry the *stored production* checker verdict.

## 1. Stored production `chk` vs the offline builder

Stored step (with the stored accept/reject decision):

| stored step / decision | n | share |
|---|---|---|
| auto/reject | 415 | 84.7 % |
| match/accept | 67 | 13.7 % |
| mistake/reject | 4 | 0.8 % |
| mistake/accept | 3 | 0.6 % |
| spelling_variant/accept | 1 | 0.2 % |

Crosstab stored -> computed (`compute_chk`):

| stored step / decision | computed step | n |
|---|---|---|
| auto/reject | auto | 415 |
| match/accept | auto | 42 |
| match/accept | match | 25 |
| mistake/accept | auto | 3 |
| mistake/reject | auto | 4 |
| spelling_variant/accept | auto | 1 |

Accept/reject disagreements between stored and computed: **46 / 490** (9.39 %).

`spelling_variant` rows present in this DEV side: **1** — the step the offline builder structurally cannot produce.

## 2. `l1_nearmiss` against both

Near-misses flagged: **9 / 490** (1.84 %), of which 2 have the same token count and 7 are length-mismatch candidates.

By **stored** production verdict:

| stored step / decision | near-misses | rows | rate |
|---|---|---|---|
| match/accept | 7 | 67 | 10.4 % |
| auto/reject | 1 | 415 | 0.2 % |
| spelling_variant/accept | 1 | 1 | 100.0 % |
| mistake/accept | 0 | 3 | 0.0 % |
| mistake/reject | 0 | 4 | 0.0 % |

By **computed** builder step:

| computed step | near-misses |
|---|---|
| auto | 9 |

## 3. How well does the near-miss count approximate production L1 beyond the builder?

Gap set **G** = items production accepted at L1 (`verdict` accepted and `step` in `match`/`spelling_variant`) that the offline builder does **not** call `match`: **|G| = 43**.

| quantity | value |
|---|---|
| near-miss ∧ G (true positive) | 8 |
| near-miss ∧ ¬G (over-count) | 1 |
| G ∧ ¬near-miss (missed) | 35 |
| precision (share of near-misses that production really accepted at L1) | 88.9 % |
| recall (share of G the proxy finds) | 18.6 % |

Composition of G, by stored step -> computed step:

| stored | computed | n | flagged near-miss |
|---|---|---|---|
| match | auto | 42 | 7 |
| spelling_variant | auto | 1 | 1 |

**Reading — and the caveat that decides how to use this number.** Taken at face value the proxy has **88.9 % precision** (8 of 9 flagged rows were really accepted by production at L1) but only **18.6 % recall** (8 of 43 gap rows found). The recall figure is, however, **not** a measurement of the offline builder's L1 leniency gap, because G is contaminated: 42 of its 43 rows have stored step `match`, i.e. production made an *exact* L1 match that the builder now misses. Those rows are production/offline **normalisation and reference-set drift**, not fuzzy acceptance: the stored `chk` was captured against the production reference set under production's own normaliser, while `build_side('dev')` matches against the arm-B annotations (`ann_b0`). The sample below makes the dominant mechanism visible — every `match` near-miss differs from its nearest reference only by a contraction (`she's` / `there's` / `wouldn't` vs the spelled-out form), i.e. production's normaliser expands contractions and `checker_1i.base.norm` does not.

The part of G that really is "production accepts at L1 beyond what the offline builder can reproduce" is the `spelling_variant` step, and on DEV that is **1 row(s)**, of which the near-miss predicate flags **1**. So:

* as an **estimator of the size** of the unreproducible-L1 gap, the near-miss count is a loose **upper bound**: 9 flagged vs 1 true `spelling_variant` accepts on DEV (~9x over-count);
* as a **filter**, it is accurate: 8 of 9 flagged rows (88.9 %) are answers production did accept at L1, so items it flags deserve to be read as "production-plausible accepts the offline pipeline will reject", not as noise;
* it is **not** a substitute for the missing `spelling_variant` step. DEV carries only 1 such row in 490, so DEV cannot calibrate that step at all — any Phase 1M claim about production L1 leniency has to be stated as a bound, not an estimate.

Caveats: (a) DEV is the calibration set *and* the set the frozen config was tuned on, so these rates are optimistic for a fresh side; (b) the stored DEV verdicts come from the production checker at capture time — a later production change to the spelling-variant step would invalidate the mapping; (c) the near-miss predicate is a pure string rule and knows nothing of the annotation mistake patterns, so a near-miss can coexist with a legitimate `mistake` rejection (see the crosstab).

### Sample near-misses (up to 12)

| item | stored | computed | dist | len_mm | answer | nearest ref |
|---|---|---|---|---|---|---|
| C:10138:885817230 | match | auto | 2 | True | `If she hadn't found this room, she would still be crying alone.` | `If she had not found this room, she would still be crying alone.` |
| C:10734:680124368 | auto | auto | 1 | False | `She should have drawn it farther from the water.` | `She should have drawn it further from the water.` |
| C:13175:1686822603 | match | auto | 2 | True | `There's a lot of yellow cheese on the board.` | `There is a lot of yellow cheese on the board.` |
| C:14779:960497277 | match | auto | 2 | True | `She's going to wipe the dust off the top edge of the door.` | `She is going to wipe the dust off the top edge of the door.` |
| C:15954:3303144406 | match | auto | 2 | True | `Look! The vendor's lowering the basket into the oil.` | `Look! The vendor is lowering the basket into the oil.` |
| C:16261:3147452768 | match | auto | 2 | True | `He has a plan. He's going to walk her home.` | `He has a plan. He is going to walk her home.` |
| C:6275:803370492 | match | auto | 2 | True | `Look — right now they're posing in front of the waterfall.` | `Look — right now they are posing in front of the waterfall.` |
| C:6971:2024863593 | match | auto | 2 | True | `If she were a robot, the requests wouldn't bother her.` | `If she were a robot, the requests would not bother her.` |
| C:8756:735046139 | spelling_variant | auto | 1 | False | `He said the puck traveled faster on cold ice.` | `He said the puck travelled faster on cold ice.` |

