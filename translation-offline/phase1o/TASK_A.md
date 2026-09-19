# Phase 1O Task A — diagnostic re-run on a closed set, not a new measurement

Closed Phase 1N set (900 items, 100 sentences), ORIGINAL 1N judge labels, identical frozen stack (LOCKTIP+F8-READOUT-ONLY (TIP-as-rejection on), arm B, `gemini-3.1-flash-lite`, temperature 0, thinkingBudget 0). The ONLY difference between the two columns is the prompt: `P-FROZEN-1N` (the 1N run, stored verdicts) versus `P-FROZEN` (the 1M prompt, no voice line).

**Status: COVERAGE-ONLY (judged-wrong items not called; FA not measured).** Run commit `20c82082781be986e552fa0bfb3ad4da25f9fd03`.

## Fidelity pre-flight (0 calls)

* `P-FROZEN-1N` re-scored by this module from stored verdicts: coverage 350/426 = 82.16% [78.19, 85.68], FA 14/474 = 2.95% [1.62, 4.91] — expected 350/426 and 14/474: **MATCH** (FA and FR id lists identical to `results_1n.json`: True).

## Plan (0 calls)

| scope | L3 items | unique requests | already stored | NEW calls |
|---|---|---|---|---|
| all | 834 | 834 | 0 | 834 |
| correct | 373 | 373 | 0 | 373 |

* hard cap for the whole phase: 600 counted calls; counted in `phase1o/calls.jsonl` when planned: 0.

## Side by side

| metric | 1N run (`P-FROZEN-1N`) | old prompt (`P-FROZEN`) |
|---|---|---|
| coverage | 350/426 = 82.16% [78.19, 85.68] | 345/426 = 80.99% [76.93, 84.60] |
| FA overall | 14/474 = 2.95% [1.62, 4.91] | not measured |
| FA type T | 4/188 = 2.13% [0.58, 5.36] | not measured |
| FA type W | 4/94 = 4.26% [1.17, 10.54] | not measured |
| FA type M | 3/95 = 3.16% [0.66, 8.95] | not measured |
| FA type S | 3/97 = 3.09% [0.64, 8.77] | not measured |
| FR at F2B | 1/426 = 0.23% [0.01, 1.30] | 1/426 = 0.23% [0.01, 1.30] |
| FR at F4v2 | 7/426 = 1.64% [0.66, 3.36] | 7/426 = 1.64% [0.66, 3.36] |
| FR at F5 | 13/426 = 3.05% [1.63, 5.16] | 13/426 = 3.05% [1.63, 5.16] |
| FR at L3 | 39/426 = 9.15% [6.59, 12.30] | 43/426 = 10.09% [7.40, 13.36] |
| FR at L3:TIPrej | 16/426 = 3.76% [2.16, 6.03] | 17/426 = 3.99% [2.34, 6.31] |
| FA at L3 | 14/474 = 2.95% [1.62, 4.91] | not measured |
| coverage, passive tag None | 266/321 = 82.87% [78.29, 86.82] | 268/321 = 83.49% [78.97, 87.38] |
| coverage, passive tag by | 78/83 = 93.98% [86.50, 98.02] | 74/83 = 89.16% [80.41, 94.92] |
| coverage, passive tag agentless | 6/22 = 27.27% [10.73, 50.22] | 3/22 = 13.64% [2.91, 34.91] |

All intervals are exact 95 % Clopper-Pearson. Same items, same labels in both columns: the intervals describe each column, the paired flips below describe the difference.

## L3 verdict transitions, `P-FROZEN-1N` -> `P-FROZEN`

**judged correct**: `{"DIFF->DIFF": 35, "DIFF->SAME": 1, "DIFF->TIP": 3, "SAME->DIFF": 8, "SAME->SAME": 307, "SAME->TIP": 2, "TIP->SAME": 4, "TIP->TIP": 13}`

**judged wrong**: `{}`

### Items whose final accept/reject flipped

| id | judged | type | passive | direction | L3 1N -> old | layer 1N -> old |
|---|---|---|---|---|---|---|
| C:160003:3732307761 | correct | None | None | reject->accept | DIFF -> SAME | L3 -> L3 |
| C:160012:4258150073 | correct | None | by | accept->reject | SAME -> DIFF | L3 -> L3 |
| C:160013:2228538754 | correct | None | None | reject->accept | TIP -> SAME | L3:TIPrej -> L3 |
| C:160016:687924368 | correct | None | agentless | accept->reject | SAME -> DIFF | L3 -> L3 |
| C:160017:1584049848 | correct | None | None | reject->accept | TIP -> SAME | L3:TIPrej -> L3 |
| C:160031:1866579597 | correct | None | by | accept->reject | SAME -> TIP | L3 -> L3:TIPrej |
| C:160035:1168408523 | correct | None | None | reject->accept | TIP -> SAME | L3:TIPrej -> L3 |
| C:160044:2250578659 | correct | None | by | accept->reject | SAME -> DIFF | L3 -> L3 |
| C:160051:1573843600 | correct | None | None | accept->reject | SAME -> DIFF | L3 -> L3 |
| C:160051:415479675 | correct | None | None | accept->reject | SAME -> DIFF | L3 -> L3 |
| C:160056:2304988526 | correct | None | agentless | accept->reject | SAME -> DIFF | L3 -> L3 |
| C:160065:390080876 | correct | None | None | reject->accept | TIP -> SAME | L3:TIPrej -> L3 |
| C:160084:3341454354 | correct | None | by | accept->reject | SAME -> TIP | L3 -> L3:TIPrej |
| C:160089:2138348670 | correct | None | None | accept->reject | SAME -> DIFF | L3 -> L3 |
| C:160092:3845336042 | correct | None | agentless | accept->reject | SAME -> DIFF | L3 -> L3 |

## How much of the gap is the prompt

The 1M -> 1N coverage gap is 89.09 - 82.16 = **6.93 points**. Under the old prompt the same 1N items score **345/426 = 80.99% [76.93, 84.60]**, i.e. -1.17 points against 82.16: the prompt explains **NONE** of the gap (-1.17 of 6.93 points); the remaining 8.10 points are NOT the prompt (the set, the items, the labels).

## Why it stopped, and what the owner can choose

* The brief expected about 450 new requests. The real number is **834**: every one of the 834 L3-eligible 1N items needs a fresh verdict under `P-FROZEN`, because no `P-FROZEN` verdict for a 1N item exists in any ledger (the 1N probe used 1M items). 834 > the 600-call phase cap, so the module stopped with **0 model calls**, nothing trimmed.
* Two ways forward, both already built into the module (`phase1o/diag/taskA_oldprompt.py`, guarded by `phase1o/RUN_COMMIT`):
  1. `--run --scope all` after raising the cap to >= 834 (edit `CAP`, recommit, rewrite `RUN_COMMIT`): coverage AND FA under the old prompt. List price about $0.06.
  2. `--run --scope correct`: only the **373** L3-eligible items the 1N judge called correct. Fits under the cap as it stands. It answers the one question of Task A completely (coverage under the old prompt, the passive split, the transition matrix for judged-correct items, the points of the 6.93-point gap the prompt explains); FA under the old prompt stays unmeasured and the report says so. It selects items by judge label, which is acceptable only because the set is closed and this is a diagnosis.
* After either run, `--report` rewrites `TASK_A.md`, `TASK_D.md` and `taskA_results.json` in one invocation.

## Calls

* counted calls (HTTP 200) in `phase1o/calls.jsonl`: **373**; uncounted retries (http 0/429/5xx): 0; empty-200 / parse failures (counted, never retried, never guessed): 0.
* items without an old-prompt verdict: 461 (0 of them counted failures). never guessed: the pipeline gets no verdict for the item and does not accept it at L3.
* tokens in 84394, out 373; list-price spend at $0.25 in / $1.50 out per 1M tokens: **$0.02166**.
* `phase1n/calls.jsonl` byte-unchanged: True.

## Addendum (closing worker, 19 September 2026)

The section "Why it stopped, and what the owner can choose" above is generated text that describes the state BEFORE the reduced run (0 calls). The main session then chose option 2, `--run --scope correct`: 373 counted calls, cap 600 not raised, FA under the old prompt NOT MEASURED. The figures in "Side by side", the transitions and "Calls" are the result of that run. The module was not edited after `RUN_COMMIT`.
