# Phase 1M — the new 140-sentence set, measured once

Freeze commit `22cba45596e4df755eb42bd0b13b063aaddd7610`. Config **LOCKTIP+F8V2 (TIP-as-rejection on) / P-FROZEN**, model `gemini-3.1-flash-lite`, temperature 0, thinkingBudget 0. Every figure is numerator/denominator, point and exact 95 % Clopper-Pearson interval; columns are never averaged.

## Headline

| metric | value |
|---|---|
| items | 1260 over 140 sentences |
| coverage | 547/614 = 89.09% [86.35, 91.44] |
| coverage (kind C) | 530/559 = 94.81% [92.63, 96.50] |
| false accepts | 69/646 = 10.68% [8.41, 13.32] |

## FA by type

| type | FA |
|---|---|
| T | 11/242 = 4.55% [2.29, 7.99] |
| W | 0/89 = 0.00% [0.00, 4.06] |
| M | 1/62 = 1.61% [0.04, 8.66] |
| S | 2/82 = 2.44% [0.30, 8.53] |
| V | 55/171 = 32.16% [25.24, 39.72] |
| E | 0/0 = 0.00% [0.00, 0.00] |

## FA and false rejections by layer

| layer | FA | false rejections |
|---|---|---|
| F2B | — | 3/614 = 0.49% [0.10, 1.42] |
| F4v2 | — | 9/614 = 1.47% [0.67, 2.76] |
| F5 | — | 5/614 = 0.81% [0.26, 1.89] |
| F8 | — | 6/614 = 0.98% [0.36, 2.11] |
| L3 | 69/646 = 10.68% [8.41, 13.32] | 27/614 = 4.40% [2.92, 6.33] |
| L3:TIPrej | — | 17/614 = 2.77% [1.62, 4.40] |

## Targets

| target | on the point | on the interval |
|---|---|---|
| coverage >= 90% | missed | missed |
| FA < 5% | missed | missed |
| type-T FA < 5% | MET | missed |

## The two named cells

**AGENT-DEMOTION (writer intent V, judged wrong)** — accepted 54 of 176 judged wrong = 54/176 = 30.68% [23.96, 38.06]; rejecting layers `{"F4v2": 20, "F8": 25, "L3": 72, "L3:TIPrej": 5}`

| form | accepted / judged wrong | rate | rejecting layers |
|---|---|---|---|
| passive | 30/66 | 30/66 = 45.45% [33.14, 58.19] | `{"F4v2": 8, "F8": 21, "L3": 5, "L3:TIPrej": 2}` |
| cleft | 1/12 | 1/12 = 8.33% [0.21, 38.48] | `{"F4v2": 4, "L3": 6, "L3:TIPrej": 1}` |
| reported | 12/31 | 12/31 = 38.71% [21.85, 57.81] | `{"F4v2": 4, "F8": 2, "L3": 12, "L3:TIPrej": 1}` |
| dropped | 11/67 | 11/67 = 16.42% [8.49, 27.48] | `{"F4v2": 4, "F8": 2, "L3": 49, "L3:TIPrej": 1}` |

**TIME-FRAME-SHIFT (writer intent TF, judged wrong)** — accepted 7 of 189 judged wrong = 7/189 = 3.70% [1.50, 7.48]; rejecting layers `{"L3": 173, "L3:TIPrej": 9}`

## §5.1 the counter fix (routing, not verdicts)

* rejected at L2 under BASE: **249**; L3-eligible under LOCKTIP: **1115**
* released (both): **249**, of which accepted **55**, judged correct 46, judged wrong by type `{"M": 6, "S": 9, "T": 165, "V": 20, "W": 3}`
* the OLD inert counter, for continuity: **0**

## Carried bugs (counted, NOT patched)

* F2B never sees the 249 lock-released items.
* 0 records whose chk step is "mistake" are rejected at L2 and not released.

## The builder limit (§2.1)

* 29 L1 near-misses (13 of them token-count mismatches), 11 judged correct, 0 of those rejected downstream = coverage understatement 0/614 = 0.00% [0.00, 0.60].
* 18 near-misses are judged wrong (an L1 accept there would be a false accept).

## Judge noise (controls vs the part labels)

* judged disagreements 2/100 = 2.00% [0.24, 7.04]; type disagreements 0/45 = 0.00% [0.00, 7.87].

## Shadow readouts (they decide nothing)

* **F9 had it stayed on**: caught uniquely 9 wrong, cost 23 correct; coverage 524/614 = 85.34% [82.29, 88.05], FA 60/646 = 9.29% [7.16, 11.79].
* **the other TIP setting** (TIP-as-rejection off): coverage 563/614 = 91.69% [89.22, 93.75], FA 156/646 = 24.15% [20.90, 27.64].
* **f8v2**: caught uniquely 25 wrong, cost 6 correct.

## Calls

* unique requests 1115, reused 0, new 1115; counted calls in phase1m 1115 of cap 1600; items without a verdict 0 (a counted failure is never guessed).
* spend at $0.25 in / $1.50 out per 1M tokens: `{"tokens_in": 244757, "tokens_out": 1115}`
