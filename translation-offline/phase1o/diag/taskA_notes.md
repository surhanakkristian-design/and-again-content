## Why it stopped, and what the owner can choose

* The brief expected about 450 new requests. The real number is **834**: every one of the 834 L3-eligible 1N items needs a fresh verdict under `P-FROZEN`, because no `P-FROZEN` verdict for a 1N item exists in any ledger (the 1N probe used 1M items). 834 > the 600-call phase cap, so the module stopped with **0 model calls**, nothing trimmed.
* Two ways forward, both already built into the module (`phase1o/diag/taskA_oldprompt.py`, guarded by `phase1o/RUN_COMMIT`):
  1. `--run --scope all` after raising the cap to >= 834 (edit `CAP`, recommit, rewrite `RUN_COMMIT`): coverage AND FA under the old prompt. List price about $0.06.
  2. `--run --scope correct`: only the **373** L3-eligible items the 1N judge called correct. Fits under the cap as it stands. It answers the one question of Task A completely (coverage under the old prompt, the passive split, the transition matrix for judged-correct items, the points of the 6.93-point gap the prompt explains); FA under the old prompt stays unmeasured and the report says so. It selects items by judge label, which is acceptable only because the set is closed and this is a diagnosis.
* After either run, `--report` rewrites `TASK_A.md`, `TASK_D.md` and `taskA_results.json` in one invocation.
