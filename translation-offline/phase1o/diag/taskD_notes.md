## Plain answer

**Yes — the stack rejects the agentless passive outright; it is never "tolerated with a tip".** The deciding layer is **L3, the model's one-word verdict**: 14 of the 16 rejections are a raw `DIFF` reply from `gemini-3.1-flash-lite` under `P-FROZEN-1N`. The other 2 never reached the model: the **F4v2 subject-mismatch guard** rejected them before L3. **0 of the 16 are TIP-turned-rejection** (`model_tip` false on every row, no item carries a tip) — so switching TIP-as-rejection OFF would rescue none of them.

## What machinery exists for a dropped agent / missing meaning, and whether it fired

Read from the routing code the runner executes (`pipeline_1i.run_pipeline`, `runner_1k.configure_row / apply_guards / locktip_decide`, the guard docstrings of `checker_1i` / `guards_c`):

* **There is no "type M, accept with a tip" path at all.** `M` exists only as a JUDGE label on items judged wrong. Nothing in the stack classifies an accepted answer as "meaning dropped but tolerable".
* The only tip sources are (a) the model replying `TIP` ("same meaning and acceptable, but with a small slip" — the system text says nothing about a dropped agent), (b) a `correct_with_tip` chk from the checker, (c) the LOCKTIP lock tip. None fired on the 16. With TIP-as-rejection ON a model `TIP` would have been a rejection anyway.
* The missing-meaning guards are **rejecting** guards, not tolerating ones: `F5` (adjunct deletion — fires only when the answer is an order-preserving subsequence of a reference/variant and the deleted span carries information), `F5t` (diff-based deletion, not in the 1N guard set), `F2B` (a with-tip acceptance downgraded when the Slovak carries a duration the answer lost). **None of them fired on the 16** (layers are `L3` x14 and `F4v2` x2). A passive is not a subsequence of the active reference, so F5 cannot see a dropped agent by construction.
* `F4v2` (answer subject pronoun contradicts a feature the Slovak determines) fired on 2 — a subject guard misreading the passive's new subject, not a meaning guard. The pipeline row keeps no guard trace, so the exact clash is not stored.
* F8v1 / F8v2 / F9 are readouts only in 1N and decide nothing; their per-item readouts are listed below.
* The stored model reply is the bare word (`maxOutputTokens` 24, "No explanation"): **no reason text exists** for any of the 14 DIFFs.

## What this means for the owner's expectation

The owner expected: agentless passive = dropped agent = type M, tolerated with a tip. The stack does neither. The 1N voice line tells the model that dropping the agent "is SAME, provided the meaning is preserved", and the model still answers DIFF on 14 of the 22 agentless items judged correct (6 accepted, 2 stopped earlier by F4v2) — while the `by`-passives, which keep the agent, pass 78 of 83 with 0 L3 rejections. The model is treating the lost agent as lost meaning (DIFF), which is the prompt's own wording line at work ("a word that changes which thing, person ... the Slovak names is DIFF"), and no layer downstream can turn a DIFF into an accept-with-tip. The reply under `P-FROZEN` is in the per-item list once Task A has run; until then it reads "not run".
