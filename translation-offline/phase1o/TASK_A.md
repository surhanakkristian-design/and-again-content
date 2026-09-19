# Phase 1O Task A — diagnostic re-run on a closed set, not a new measurement

Closed Phase 1N set (900 items, 100 sentences), ORIGINAL 1N judge labels, identical frozen stack (LOCKTIP+F8-READOUT-ONLY (TIP-as-rejection on), arm B, `gemini-3.1-flash-lite`, temperature 0, thinkingBudget 0). The ONLY difference between the two columns is the prompt: `P-FROZEN-1N` (the 1N run, stored verdicts) versus `P-FROZEN` (the 1M prompt, no voice line).

**Status: NOT RUN — old-prompt verdicts missing for 834 of 834 L3-eligible items.** Run commit `20c82082781be986e552fa0bfb3ad4da25f9fd03`.

## Fidelity pre-flight (0 calls)

* `P-FROZEN-1N` re-scored by this module from stored verdicts: coverage 350/426 = 82.16% [78.19, 85.68], FA 14/474 = 2.95% [1.62, 4.91] — expected 350/426 and 14/474: **MATCH** (FA and FR id lists identical to `results_1n.json`: True).

## Plan (0 calls)

| scope | L3 items | unique requests | already stored | NEW calls |
|---|---|---|---|---|
| all | 834 | 834 | 0 | 834 |
| correct | 373 | 373 | 0 | 373 |

* hard cap for the whole phase: 600 counted calls; counted in `phase1o/calls.jsonl` when planned: 0.

## Result

**No old-prompt figure exists.** NOT RUN — old-prompt verdicts missing for 834 of 834 L3-eligible items. No model call was made for a plan above the cap; nothing was trimmed and nothing was guessed.

## Why it stopped, and what the owner can choose

* The brief expected about 450 new requests. The real number is **834**: every one of the 834 L3-eligible 1N items needs a fresh verdict under `P-FROZEN`, because no `P-FROZEN` verdict for a 1N item exists in any ledger (the 1N probe used 1M items). 834 > the 600-call phase cap, so the module stopped with **0 model calls**, nothing trimmed.
* Two ways forward, both already built into the module (`phase1o/diag/taskA_oldprompt.py`, guarded by `phase1o/RUN_COMMIT`):
  1. `--run --scope all` after raising the cap to >= 834 (edit `CAP`, recommit, rewrite `RUN_COMMIT`): coverage AND FA under the old prompt. List price about $0.06.
  2. `--run --scope correct`: only the **373** L3-eligible items the 1N judge called correct. Fits under the cap as it stands. It answers the one question of Task A completely (coverage under the old prompt, the passive split, the transition matrix for judged-correct items, the points of the 6.93-point gap the prompt explains); FA under the old prompt stays unmeasured and the report says so. It selects items by judge label, which is acceptable only because the set is closed and this is a diagnosis.
* After either run, `--report` rewrites `TASK_A.md`, `TASK_D.md` and `taskA_results.json` in one invocation.

## Calls

* counted calls (HTTP 200) in `phase1o/calls.jsonl`: **0**; uncounted retries (http 0/429/5xx): 0; empty-200 / parse failures (counted, never retried, never guessed): 0.
* items without an old-prompt verdict: 834 (0 of them counted failures). never guessed: the pipeline gets no verdict for the item and does not accept it at L3.
* tokens in 0, out 0; list-price spend at $0.25 in / $1.50 out per 1M tokens: **$0.00000**.
* `phase1n/calls.jsonl` byte-unchanged: no run — not touched.
