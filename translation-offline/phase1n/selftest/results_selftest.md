# Phase 1N SELFTEST of the --final path (closed 1M side, 0 calls)

Freeze commit `(selftest — no freeze)`. Config **LOCKTIP+F8-READOUT-ONLY (TIP-as-rejection on) / P-FROZEN-1N** (F8 decides NOTHING), model `gemini-3.1-flash-lite`, temperature 0, thinkingBudget 0. Every figure is numerator/denominator, point and exact 95 % Clopper-Pearson interval; columns are never averaged.

## Headline

| metric | value |
|---|---|
| items | 1260 over 140 sentences |
| coverage | 553/614 = 90.07% [87.42, 92.32] |
| coverage (kind C) | 533/559 = 95.35% [93.26, 96.94] |
| false accepts | 94/646 = 14.55% [11.92, 17.51] |

## FA by type

| type | FA |
|---|---|
| T | 11/242 = 4.55% [2.29, 7.99] |
| W | 0/89 = 0.00% [0.00, 4.06] |
| M | 1/62 = 1.61% [0.04, 8.66] |
| S | 2/82 = 2.44% [0.30, 8.53] |

## FA and false rejections by layer

| layer | FA | false rejections |
|---|---|---|
| F2B | — | 3/614 = 0.49% [0.10, 1.42] |
| F4v2 | — | 9/614 = 1.47% [0.67, 2.76] |
| F5 | — | 5/614 = 0.81% [0.26, 1.89] |
| L3 | 94/646 = 14.55% [11.92, 17.51] | 27/614 = 4.40% [2.92, 6.33] |
| L3:TIPrej | — | 17/614 = 2.77% [1.62, 4.40] |

## Targets

| target | on the point | on the interval |
|---|---|---|
| coverage >= 90% | MET | missed |
| FA < 5% | missed | missed |
| type-T FA < 5% | MET | missed |

## The named cells

**TIME-FRAME (writer intent TF, judged wrong)** — accepted 7 of 189 judged wrong = 7/189 = 3.70% [1.50, 7.48]; rejecting layers `{"L3": 173, "L3:TIPrej": 9}`

* floor: the cell needs n >= 150 judged-wrong TF items — n = 189, MET

**AGENT-DEMOTION (writer intent V, judged wrong)** — accepted 79 of 176 judged wrong = 79/176 = 44.89% [37.40, 52.55]; rejecting layers `{"F4v2": 20, "L3": 72, "L3:TIPrej": 5}`

| form | accepted / judged wrong | rate | rejecting layers |
|---|---|---|---|
| passive | 51/66 | 51/66 = 77.27% [65.30, 86.69] | `{"F4v2": 8, "L3": 5, "L3:TIPrej": 2}` |
| cleft | 1/12 | 1/12 = 8.33% [0.21, 38.48] | `{"F4v2": 4, "L3": 6, "L3:TIPrej": 1}` |
| reported | 14/31 | 14/31 = 45.16% [27.32, 63.97] | `{"F4v2": 4, "L3": 12, "L3:TIPrej": 1}` |
| dropped | 13/67 | 13/67 = 19.40% [10.76, 30.89] | `{"F4v2": 4, "L3": 49, "L3:TIPrej": 1}` |

## PASSIVE cells (judged-correct items only)

**by_writer_tag** (the writer key `passive` on the item), 614 judged-correct items

| tag | n | accepted | rejected | rejected by layer | TIP fired (model / any) |
|---|---|---|---|---|---|
| by | 0 | 0/0 = 0.00% [0.00, 0.00] | 0 | `{}` | 0 / 0 |
| agentless | 0 | 0/0 = 0.00% [0.00, 0.00] | 0 | `{}` | 0 / 0 |
| untagged | 614 | 553/614 = 90.07% [87.42, 92.32] | 61 | `{"F2B": 3, "F4v2": 9, "F5": 5, "L3": 27, "L3:TIPrej": 17}` | 17 / 29 |

* coverage, all judged correct: 553/614 = 90.07% [87.42, 92.32]
* coverage WITHOUT the passive items: 553/614 = 90.07% [87.42, 92.32]
* coverage of the passive items only: 0/0 = 0.00% [0.00, 0.00]

**by_judge_tag** (the judge row key `passive`), 614 judged-correct items

| tag | n | accepted | rejected | rejected by layer | TIP fired (model / any) |
|---|---|---|---|---|---|
| by | 0 | 0/0 = 0.00% [0.00, 0.00] | 0 | `{}` | 0 / 0 |
| agentless | 0 | 0/0 = 0.00% [0.00, 0.00] | 0 | `{}` | 0 / 0 |
| untagged | 614 | 553/614 = 90.07% [87.42, 92.32] | 61 | `{"F2B": 3, "F4v2": 9, "F5": 5, "L3": 27, "L3:TIPrej": 17}` | 17 / 29 |

* coverage, all judged correct: 553/614 = 90.07% [87.42, 92.32]
* coverage WITHOUT the passive items: 553/614 = 90.07% [87.42, 92.32]
* coverage of the passive items only: 0/0 = 0.00% [0.00, 0.00]

## §5.1 the counter fix (routing, not verdicts)

* rejected at L2 under BASE: **249**; L3-eligible under LOCKTIP: **1115**
* released (both): **249**, of which accepted **58**, judged correct 46, judged wrong by type `{"M": 6, "S": 9, "T": 165, "V": 20, "W": 3}`
* the OLD inert counter `released_by_LOCKTIP_total`, carried UNPATCHED: **0**

## Carried bugs (counted, NOT patched)

* `released_by_LOCKTIP_total` (inert accept-flip): **0**, beside the fixed routing counter **249**.
* F2B never sees the lock-released items — counter A (routing proxy) **249**, counter B (section5 bug3, inert accept-flip) **{"still_fires": false, "count": 0, "sids": [], "ids": [], "measured_as": "items LOCKTIP released, which F2B never sees"}**; the two disagree and both are carried.
* 0 records whose chk step is "mistake" are rejected at L2 and not released.
* reference hygiene: NOT applied (phase1n/hygiene present: False) — chk before == chk after, `{"correct/match": 110, "wrong/auto": 1150}`.

## The builder limit (§2.1)

* 29 L1 near-misses (13 of them token-count mismatches), 11 judged correct, 0 of those rejected downstream = coverage understatement 0/614 = 0.00% [0.00, 0.60].
* the production checker accepts spelling_variant and fuzzy matches; neither tolerance is reproducible offline, so compute_chk never makes those L1 accepts and offline coverage UNDERSTATES production coverage by up to the figure above
* 18 near-misses are judged wrong (an L1 accept there would be a false accept).

## Judge noise (controls vs the part labels)

* 100 control comparisons; judged disagreements 2/100 = 2.00% [0.24, 7.04]; type disagreements 0/45 = 0.00% [0.00, 7.87].

## Shadow readouts (they decide nothing)

* **F8v1-on**: COST 0 judged-correct items it would reject, CATCHES 69 judged-wrong, of which UNIQUE 33 (rejected by no other layer incl. L3); headline under it coverage 553/614 = 90.07% [87.42, 92.32], FA 61/646 = 9.44% [7.30, 11.96].
* **F8v2-on**: COST 20 judged-correct items it would reject, CATCHES 78 judged-wrong, of which UNIQUE 25 (rejected by no other layer incl. L3); headline under it coverage 547/614 = 89.09% [86.35, 91.44], FA 69/646 = 10.68% [8.41, 13.32].
* **F9-on**: caught uniquely 10 wrong, cost 23 correct; coverage 530/614 = 86.32% [83.34, 88.94], FA 84/646 = 13.00% [10.51, 15.84].
* **TIP-off** (TIP-as-rejection off): coverage 570/614 = 92.83% [90.50, 94.75], FA 182/646 = 28.17% [24.73, 31.81].

## Calls

* unique requests 1115, reused 1115, new 0; counted calls in phase1n 0 of cap 1200; items without a verdict 0 (a counted failure is never guessed).
* spend at $0.25 in / $1.50 out per 1M tokens: `{"spend_usd": 0.0, "tokens_in": 0, "tokens_out": 0}`
