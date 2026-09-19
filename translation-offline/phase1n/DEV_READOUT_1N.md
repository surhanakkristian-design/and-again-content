# Phase 1N — DEV readout on the CLOSED sides (0 model calls)

Commands, each run once, zero new model calls (every L3 verdict came from the stored ledgers
`phase1j/1k/1l/1m/calls.jsonl`; cache misses would have been reported, there were none):

```
python3 runner_1n.py --dev --f8 none     ->  dev_regression_1n_none.json   (the 1N headline config)
python3 runner_1n.py --dev --f8 f8v2     ->  dev_regression_1n_f8v2.json   (the 1M config, control)
```

**All four sides are CLOSED sets.** `dev` and `replay1j` were used to build and tune the stack,
`fresh1l` and `fresh1m` have been measured and reported. Nothing below is a measurement of the
checker: it is a design readout used to choose what the frozen stack carries into the one fresh 1N
run. No target may be claimed from any number on this page.

## 1. Headline coverage and FA per side, under both settings

`--f8 none` = F8 decides nothing (the 1N frozen configuration). `--f8 f8v2` = F8v2 decides, the
Phase 1M frozen configuration. LOCKTIP on, F9 off, TIP-as-rejection on, prompt `P-FROZEN` in both
(the stored verdicts are P-FROZEN verdicts; the 1N prompt is only exercised by `--probe`).

| side | n items | coverage — F8 none | coverage — F8v2 | FA — F8 none | FA — F8v2 | FA type T — none / F8v2 |
|---|---|---|---|---|---|---|
| dev | 490 | 182/189 = 96.30 % [92.52, 98.50] | 182/189 = 96.30 % | 13/301 = 4.32 % [2.32, 7.27] | 11/301 = 3.65 % [1.84, 6.44] | 0/54 / 0/54 |
| replay1j | 490 | 182/196 = 92.86 % [88.31, 96.04] | 182/196 = 92.86 % | 18/294 = 6.12 % [3.67, 9.50] | 17/294 = 5.78 % [3.40, 9.10] | 3/59 / 3/59 |
| fresh1l | — | 194/217 = 89.40 % [84.52, 93.16] | 194/217 = 89.40 % | 26/383 = 6.79 % [4.48, 9.79] | 12/383 = 3.13 % [1.63, 5.41] | 3/130 / 3/130 |
| fresh1m | 1260 | 553/614 = 90.07 % [87.42, 92.32] | 547/614 = 89.09 % [86.35, 91.44] | 94/646 = 14.55 % [11.92, 17.51] | 69/646 = 10.68 % [8.41, 13.32] | 11/242 / 11/242 |

Reproduction: under `--f8 f8v2` the fresh1m row reproduces the published Phase 1M headline
(547/614 and 69/646) exactly — `PHASE 1M REPRODUCED: True`. The `dev` / `replay1j` expectations are
Phase **1L** targets and are valid only with `--f8 f8 --f9 on --tip reject`; their MISMATCH here is
the configuration, not a defect (the runner prints that scope itself). Under `--f8 none` the
fresh1m MISMATCH is likewise correct and is exactly the price of F8 not deciding: coverage +6
items, FA +25 items.

## 2. COST and CATCHES of the two F8 modules — under the OLD labels

**Stated as such: every COST / CATCH / UNIQUE below is counted against the labels of the closed set
it sits on — the 1M (and 1L / 1J) judge labels that the guards were built against.** They are not
independent evidence; a guard that looks free here can still cost on fresh data.

* **COST** = items the module would reject that the judge called **correct** (lost coverage).
* **CATCHES** = items it would reject that the judge called **wrong**.
* **UNIQUE** = of those catches, the ones the headline stack (every other layer incl. L3) accepts —
  i.e. the catches that actually remove a false accept. This is the only part of CATCHES that
  moves FA.

| side | module | rejects | COST (judged correct) | CATCHES (judged wrong) | UNIQUE (headline would accept) | headline if it decided: coverage / FA |
|---|---|---|---|---|---|---|
| dev | F8v1 | 1 | 0 | 1 | 1 | 182/189 / 12/301 = 3.99 % |
| dev | F8v2 | 25 | 0 | 25 | 2 | 182/189 / 11/301 = 3.65 % |
| replay1j | F8v1 | 1 | **1** | 0 | 0 | 181/196 = 92.35 % / 18/294 = 6.12 % |
| replay1j | F8v2 | 20 | 0 | 20 | 1 | 182/196 / 17/294 = 5.78 % |
| fresh1l | F8v1 | 23 | 0 | 23 | 11 | 194/217 / 15/383 = 3.92 % |
| fresh1l | F8v2 | 46 | 0 | 46 | 14 | 194/217 / 12/383 = 3.13 % |
| fresh1m | F8v1 | 69 | 0 | 69 | **33** | 553/614 = 90.07 % / 61/646 = 9.44 % |
| fresh1m | F8v2 | 98 | **20** | 78 | **25** | 547/614 = 89.09 % / 69/646 = 10.68 % |

UNIQUE is measured against the `--f8 none` headline (the 1N configuration); the per-item ids are in
`dev_regression_1n_*.json` under `sides.<side>.f8_shadow_readouts.<module>` (`cost_ids`,
`catch_ids`, `unique_ids`). The `--f8 f8v2` file reports UNIQUE against its own headline, where
F8v2's own catches are already spent — that is why UNIQUE collapses to 0 there; the cost/catch
counts themselves are identical in both files, as they must be.

### What the table says

1. On the largest and most recent closed set (fresh1m) **F8v2 is dominated by F8v1 on both axes**:
   F8v2 pays 20 judged-correct rejections (6 of them visible as lost coverage, 553 -> 547) and
   removes 25 false accepts, while F8v1 pays 0 and removes 33 (FA 9.44 % versus 10.68 %). F8v2
   rejects more items in total (98 vs 69) yet fixes fewer false accepts, because its extra
   rejections land on items another layer already rejects.
2. That is the same direction the 1M report recorded ("the F8v1 shadow beat the fixed F8v2") and it
   is now stated in the units a guard decision needs: measured cost and unique catches, per side.
3. On dev and fresh1l F8v2 looks better (more catches, no cost). The two readings disagree, which
   is exactly why neither set may decide anything: dev is the set both modules were written on.
4. `replay1j` shows F8v1's only measured COST (1 item) — one lost judged-correct answer.

## 3. TASK B — how a guard is selected from now on

**A guard is selected on MEASURED COST and MEASURED CATCHES.**

* COST = the number of judged-correct answers the guard rejects. It is the primary cost and it is
  counted, not argued.
* CATCHES = the number of judged-wrong answers it rejects, reported together with UNIQUE — the
  catches that the rest of the stack does not already make. A guard whose UNIQUE is 0 buys nothing.
* Both are read per side, with the set named and its status (closed / fresh) stated beside them.
* **Gold-assertion accuracy is a report-only diagnostic. It is never a gate.** No guard is
  accepted, rejected, tuned or ranked by how well it agrees with a gold assertion set; that number
  may appear in a report, labelled as a diagnostic, and nowhere else.
* Numbers taken on a set the guard was built or tuned on are never sufficient for selection; they
  are reported as such and a fresh set decides.

**No guard is added or tuned in this phase.** The frozen stack is the one the owner fixed:
LOCKTIP on, F8 decides nothing (both modules read out only), F9 off, TIP-as-rejection on, arm B,
prompt `P-FROZEN-1N`, gemini-3.1-flash-lite / temperature 0 / thinkingBudget 0. This document
changes no configuration; it records the readouts the next selection will be held to.

## 4. Self-test

`python3 runner_1n.py --selftest-final` runs clean end to end (exit 0, 0 model calls): fresh1m
build (1260 items / 140 sentences), preflight, 1115 of 1115 L3 verdicts reused, label merge,
metrics, TIME-FRAME / PASSIVE cells, the fixed §5.1 counter (249 of 249 released, old inert counter
0), the carried-bug counters, the four shadows, the §2.1 builder limit (29 L1 near-misses, 11
judged correct, 0 rejected downstream), judge noise, and it writes
`selftest/results_selftest.json` + `.md`. Headline 553/614 = 90.07 %, FA 94/646 = 14.55 % — the 1M
headline is deliberately NOT expected here, because F8 decides nothing under the 1N config.
