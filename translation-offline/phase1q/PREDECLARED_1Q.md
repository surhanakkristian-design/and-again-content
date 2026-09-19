# Phase 1Q — pre-declaration, written BEFORE the 1P set is opened

Nothing below may be changed after the first `--final` call. The set is measured once.

## Primary analysis

* Stack: the **frozen stack, commit 0e0961b** — `runner_1p.py`, `lever1.py`, `lever2.py`,
  `lever3.py`, `loader_1p.py`, the guards, the prompts, `FROZEN_CONFIG_1P.json`; prompt
  `P-FROZEN-1P` (= P-FROZEN + VOICE_SAME_LINE + the per-record lever 2 / lever 3 lines), arm B,
  LOCKTIP on, **TIP-as-rejection ON**, F8 readout-only, F9 off, model `gemini-3.1-flash-lite`,
  temperature 0, thinkingBudget 0.
* **F5 is UNCHANGED.** Its boundary is not decided and is not touched by this phase.
* **Labels = the 1P judged labels, unchanged.** Task A moved 0 labels (all 9 M3 additions were
  already judged wrong), Task B1 moves 0 labels. `data/annotations.json` is the blind annotation
  delivery, normalised, nothing else.
* Headline: **coverage** = accepted share of the judged-correct items, **FA** = accepted share of
  the judged-wrong items, reported for **P1 (odd sids)**, **P2 (even sids)** and **pooled**, each
  with an exact **Clopper-Pearson 95 %** interval (`P.cp`).

## Cells, each on its own line

| cell | definition |
|---|---|
| agentless | items carrying the writer tag `agentless` (coverage on judged correct, FA on judged wrong) |
| time-frame | items carrying the writer tag `timeframe` |
| determiner | items carrying the writer tag `determiner` |
| M1 | the writer-type-M triage bucket M1 (phase1q/taskA/triage.json) |
| M2 | the writer-type-M triage bucket M2 |
| M3 | the writer-type-M triage bucket M3 |

M1 / M2 / M3 are reported as accept rates inside their bucket, split by judged side; they are
descriptive, they do not enter the headline.

## Secondary, pre-declared

* **Coverage on the 480 writer-intended-correct items** (writer intent C), accepted / 480.
* **Accept rate in the cell "writer-M, judged correct", n = 119.**

## F6 (addition guard, variant C) — post hoc, reported on its own line

`phase1q/f6.py` is **not wired into the runner** and does not influence any decision. After the
run it is applied offline to the per-item results:

* **cost** = judged-correct items the stack ACCEPTS and F6 would REJECT;
* **catches** = judged-wrong items the stack ACCEPTS and F6 would REJECT.

Both are reported as their own line, never folded into F5, never folded into a lever, never added
to the headline coverage or FA. Its 1N measured cost was 2/426 = 0.47 %.

## Ablation, pre-declared

Baseline `P-FROZEN-1N` with the levers OFF, leftover calls only (cap - 10 = 1,390):
**lever 1 alone, lever 2 alone, lever 3 alone, and all three together**. For each arm the
**gain** (judged-correct items it converts from reject to accept) and the **FA cost**
(judged-wrong items it converts from reject to accept) are reported **separately**, never netted.
The runner's pre-declared item order is judged-correct determiner-tag L3-eligible items first,
then judged-correct agentless items, in SID order.

## Stopping rules

* Phase cap **1,400** counted calls, 225 already spent on dev; `--preflight` STOPS (writes
  `STOP_PLAN.txt`, 0 calls) if `dev_used + planned > 1,390`.
* A quota wall or a missing verdict writes `RUN_PAUSED.txt` and exits 3 **before any label is
  read**; rerunning `--final` reuses every stored verdict by request hash.
* `FINAL_RUN_DONE` makes a second `--final` refuse.
