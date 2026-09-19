# Phase 1N — the new set under P-FROZEN-1N, measured once

Freeze commit `9446b09469567bcc37e05f55b28c96428f2bb3bb`. Config **LOCKTIP+F8-READOUT-ONLY (TIP-as-rejection on) / P-FROZEN-1N** (F8 decides NOTHING), model `gemini-3.1-flash-lite`, temperature 0, thinkingBudget 0. Every figure is numerator/denominator, point and exact 95 % Clopper-Pearson interval; columns are never averaged.

## Headline

| metric | value |
|---|---|
| items | 900 over 100 sentences |
| coverage | 350/426 = 82.16% [78.19, 85.68] |
| coverage (kind C) | 338/399 = 84.71% [80.80, 88.10] |
| false accepts | 14/474 = 2.95% [1.62, 4.91] |

## FA by type

| type | FA |
|---|---|
| T | 4/188 = 2.13% [0.58, 5.36] |
| W | 4/94 = 4.26% [1.17, 10.54] |
| M | 3/95 = 3.16% [0.66, 8.95] |
| S | 3/97 = 3.09% [0.64, 8.77] |

## FA and false rejections by layer

| layer | FA | false rejections |
|---|---|---|
| F2B | — | 1/426 = 0.23% [0.01, 1.30] |
| F4v2 | — | 7/426 = 1.64% [0.66, 3.36] |
| F5 | — | 13/426 = 3.05% [1.63, 5.16] |
| L3 | 14/474 = 2.95% [1.62, 4.91] | 39/426 = 9.15% [6.59, 12.30] |
| L3:TIPrej | — | 16/426 = 3.76% [2.16, 6.03] |

## Targets

| target | on the point | on the interval |
|---|---|---|
| coverage >= 90% | missed | missed |
| FA < 5% | MET | MET |
| type-T FA < 5% | MET | missed |

## The named cells

**TIME-FRAME (writer intent TF, judged wrong)** — accepted 3 of 170 judged wrong = 3/170 = 1.76% [0.37, 5.07]; rejecting layers `{"F5": 1, "L3": 164, "L3:TIPrej": 2}`

* floor: the cell needs n >= 150 judged-wrong TF items — n = 170, MET

## PASSIVE cells (judged-correct items only)

**by_writer_tag** (the writer key `passive` on the item), 426 judged-correct items

| tag | n | accepted | rejected | rejected by layer | TIP fired (model / any) |
|---|---|---|---|---|---|
| by | 83 | 78/83 = 93.98% [86.50, 98.02] | 5 | `{"F4v2": 5}` | 0 / 0 |
| agentless | 22 | 6/22 = 27.27% [10.73, 50.22] | 16 | `{"F4v2": 2, "L3": 14}` | 0 / 0 |
| untagged | 321 | 266/321 = 82.87% [78.29, 86.82] | 55 | `{"F2B": 1, "F5": 13, "L3": 25, "L3:TIPrej": 16}` | 16 / 20 |

* coverage, all judged correct: 350/426 = 82.16% [78.19, 85.68]
* coverage WITHOUT the passive items: 266/321 = 82.87% [78.29, 86.82]
* coverage of the passive items only: 84/105 = 80.00% [71.07, 87.17]

**by_judge_tag** (the judge row key `passive`), 426 judged-correct items

| tag | n | accepted | rejected | rejected by layer | TIP fired (model / any) |
|---|---|---|---|---|---|
| by | 83 | 78/83 = 93.98% [86.50, 98.02] | 5 | `{"F4v2": 5}` | 0 / 0 |
| agentless | 22 | 6/22 = 27.27% [10.73, 50.22] | 16 | `{"F4v2": 2, "L3": 14}` | 0 / 0 |
| untagged | 321 | 266/321 = 82.87% [78.29, 86.82] | 55 | `{"F2B": 1, "F5": 13, "L3": 25, "L3:TIPrej": 16}` | 16 / 20 |

* coverage, all judged correct: 350/426 = 82.16% [78.19, 85.68]
* coverage WITHOUT the passive items: 266/321 = 82.87% [78.29, 86.82]
* coverage of the passive items only: 84/105 = 80.00% [71.07, 87.17]

## §5.1 the counter fix (routing, not verdicts)

* rejected at L2 under BASE: **205**; L3-eligible under LOCKTIP: **834**
* released (both): **205**, of which accepted **63**, judged correct 68, judged wrong by type `{"M": 5, "S": 20, "T": 105, "W": 7}`
* the OLD inert counter `released_by_LOCKTIP_total`, carried UNPATCHED: **0**

## Carried bugs (counted, NOT patched)

* `released_by_LOCKTIP_total` (inert accept-flip): **0**, beside the fixed routing counter **205**.
* F2B never sees the lock-released items — counter A (routing proxy) **205**, counter B (section5 bug3, inert accept-flip) **{"still_fires": false, "count": 0, "sids": [], "ids": [], "measured_as": "items LOCKTIP released, which F2B never sees"}**; the two disagree and both are carried.
* 0 records whose chk step is "mistake" are rejected at L2 and not released.
* reference hygiene: NOT applied (phase1n/hygiene present: False) — chk before == chk after, `{"correct/match": 33, "wrong/auto": 867}`.

## The builder limit (§2.1)

* 28 L1 near-misses (6 of them token-count mismatches), 10 judged correct, 1 of those rejected downstream = coverage understatement 1/426 = 0.23% [0.01, 1.30].
* the production checker accepts spelling_variant and fuzzy matches; neither tolerance is reproducible offline, so compute_chk never makes those L1 accepts and offline coverage UNDERSTATES production coverage by up to the figure above
* 18 near-misses are judged wrong (an L1 accept there would be a false accept).

## Judge noise (controls vs the part labels)

* 80 control comparisons; judged disagreements 3/80 = 3.75% [0.78, 10.57]; type disagreements 2/40 = 5.00% [0.61, 16.92].

## Shadow readouts (they decide nothing)

* **F8v1-on**: COST 57 judged-correct items it would reject, CATCHES 0 judged-wrong, of which UNIQUE 0 (rejected by no other layer incl. L3); headline under it coverage 301/426 = 70.66% [66.08, 74.94], FA 14/474 = 2.95% [1.62, 4.91].
* **F8v2-on**: COST 35 judged-correct items it would reject, CATCHES 0 judged-wrong, of which UNIQUE 0 (rejected by no other layer incl. L3); headline under it coverage 321/426 = 75.35% [70.97, 79.37], FA 14/474 = 2.95% [1.62, 4.91].
* **F9-on**: caught uniquely 2 wrong, cost 19 correct; coverage 331/426 = 77.70% [73.44, 81.57], FA 12/474 = 2.53% [1.31, 4.38].
* **TIP-off** (TIP-as-rejection off): coverage 366/426 = 85.92% [82.25, 89.08], FA 81/474 = 17.09% [13.81, 20.79].

## Calls

* unique requests 834, reused 0, new 834; counted calls in phase1n 954 of cap 1200; items without a verdict 0 (a counted failure is never guessed).
* spend at $0.25 in / $1.50 out per 1M tokens: `{"spend_usd": 0.07015, "tokens_in": 274881, "tokens_out": 954}`
