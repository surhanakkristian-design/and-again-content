# Phase 1T — runner handoff (the fresh 100-sentence set)

Python: the system `python3`, no venv, no third-party package.  Always `PYTHONDONTWRITEBYTECODE=1`.
Model `gemini-3.1-flash-lite`, temperature 0, thinkingBudget 0; keys and transport are
runner_1n/runner_1l's (the key is never printed).  Everything is written under `phase1t/run/`.

| file | what |
|---|---|
| `runner_1t.py` | `--dry-run` (stubbed model, 0 calls) · `--preflight` (0 calls) · `--final` (once) |
| `loader_1t.py` | the ONLY door to `phase1t/set/data` and to `data/labels.json`; one access-log line per read |
| `score_1t.py` | all figures, twice (primary + S2), 0 calls, run after `--final` |
| `FROZEN_CONFIG_1T.json` `FREEZE_FILES` `CALL_PLAN_1T.md` `TOOLING_EDITS_1T.md` | frozen state |
| `DRY_RUN_1T.json` `PREFLIGHT_1T.json` `MODULES_1T.txt` | the 0-call evidence |

The stack is the frozen 1Q/1P one, imported not copied: prompt P-FROZEN-1P, LOCKTIP,
TIP-as-rejection, F2B/F3/F4v2/F5, levers 2 and 3, arm B, hygiene absent, F8/F9 do not decide.
Differences: **lever 1 removed**, **rule AG v3 before L3** (a rejection is final and costs 0 calls;
AG v2 and each v3 flag alone are recorded as 0-call shadows), **RUNNER_PATCH_1S applied in full**.

## Commands, in order

    cd ~/Projects/and-again-content/translation-offline/phase1t/run
    export PYTHONDONTWRITEBYTECODE=1

    # 1. the set (other side): assemble_1t.py, then the judge, then the labels + the floors
    python3 ../set/assemble_1t.py --report
    python3 ../set/assemble_1t.py --labels          # writes set/data/labels.json
    python3 ../set/floor_check_1t.py                # must print FLOORS PASS (all five)

    # 2. 0-call checks (repeat after ANY edit)
    python3 runner_1t.py --dry-run                  # 13/13 checks, stubbed model
    python3 runner_1t.py --preflight                # plan + MODULES_1T.txt + PREFLIGHT_1T.json

    # 3. the owner fixes the cap, then freeze
    #    edit FROZEN_CONFIG_1T.json: "call_cap": <number>   (null = --final REFUSES)
    #    append any new .py to FREEZE_FILES (paths relative to the repo root)
    git add -A && git commit -m "phase 1T: freeze the runner"
    git rev-parse HEAD > FREEZE_HASH

    # 4. ONCE
    python3 runner_1t.py --final                    # exit 3 + RUN_PAUSED.txt = quota wall; rerun to resume
    python3 score_1t.py                             # SCORE_1T.json + SCORE_1T.md

## Guarantees

* `--preflight` counts the plan by a 0-call pass, asserts **L2 firings > 0**, writes
  `STOP_PREFLIGHT.txt` and stops on **L3-eligible 0** (or "nothing reaches L3"), and writes
  `STOP_PLAN.txt` when counted + planned > cap − 10.  With `call_cap: null` it only prints.
* `--final` refuses if `FINAL_RUN_DONE` exists, unless every `FREEZE_FILES` entry matches
  `FREEZE_HASH` **and** every imported `.py` is listed, unless `../set/FLOOR_CHECK_1T.json` says all
  five floors hold, and while `call_cap` is null.
* Labels are read **once, last**: after every planned verdict exists.  A quota wall or a missing
  verdict writes `RUN_PAUSED.txt` and exits 3 **before any label is read**; rerunning `--final`
  resumes from `calls.jsonl` without repeating a call.
* Every reply is appended to `calls.jsonl` **before** any aggregation, so a crash is replayed
  offline with 0 calls; `guarded_run` leaves `FINAL_RUN_DONE.attempt` with DONE or CRASHED +
  traceback; every write is `safe_json.safe_dump` (serialise first, then atomic replace).
* AG-rejected items never reach L3 and nothing else depends on them: their verdict is absent by
  construction and their layer is attributed `AG` (or the earlier deterministic layer).

## Rough edges

* The three data reads are logged with caller `runner_1p.py`: the frozen `build_side()` does them.
* `phase1p/lever1.py` is imported (runner_1p imports it at module level) but never called — the
  levers list is `[2, 3]` and `lever1_side()` is not part of the 1T path.
* `--dry-run` writes only under `phase1t/run/selftest/`; its fixture is synthetic and its labels
  are synthetic.  `results_1t.json` in `selftest/run_*/` is never a measurement.
