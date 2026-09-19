# Phase 1P — runner handoff

Python: the system `python3` on this Mac (3.9+), no venv, no third-party package.  Always
`PYTHONDONTWRITEBYTECODE=1`.  Keys: `runner_1l.load_keys()` reads
`~/Projects/and-again/.env.local` and takes `GEMINI_API_KEY_FREE*` **first**, the default key
second; no key is ever printed (the transport redacts it).  Model `gemini-3.1-flash-lite`,
temperature 0, thinkingBudget 0.

## Files

| file | what |
|---|---|
| `runner_1p.py` | the runner: `--preflight`, `--dry-run`, `--final`, `--ablation`, `--dev --lever N [--go]` |
| `loader_1p.py` | the ONLY door to `data/`, `judge/` and (read-only) the closed sets; every read is one line in `access_log.jsonl` |
| `lever1.py` `lever2.py` `lever3.py` | the three levers, all deterministic, 0 model calls |
| `assemble_1p.py` | writer files -> `data/{sentences,annotations,items}.json` + `--labels` |
| `floor_check_1p.py` | the four floors + `--make-fixture` |
| `FROZEN_CONFIG_1P.json` `FREEZE_FILES` `SPLIT_1P.md` `CALL_PLAN_1P.md` `DEV_READOUT_1P.md` | frozen state |
| `dev/dev_lever{1,2,3}.json` | the dev measurement, 225 counted calls |
| `selftest/` | the synthetic dry run and the writer/verdict fixture run |

`access_log.jsonl` convention is 1N's: one JSON line per read,
`{ts, side, what, caller, n, purpose}`; closed sets are logged with side `1p:ext:<phase>` /
`1p:judge:ext` and are **never** written to.

## Commands, in order

    cd ~/Projects/and-again-content/translation-offline/phase1p
    export PYTHONDONTWRITEBYTECODE=1

    # 1. writers deliver data/writer_A.json + data/writer_B.json
    python3 assemble_1p.py                 # REFUSES on overlap / duplicates / bad tags / not 4+5
    # 2. judge delivers judge/{blind_map.json,_key.json,out_part*.json|verdicts_*.json}
    python3 assemble_1p.py --labels        # joins labels + judge noise -> assemble_1p.json
    python3 floor_check_1p.py              # exit 2 + STOP_FLOOR.txt unless all four floors hold
    # 3. 0-call checks
    python3 runner_1p.py --dry-run         # synthetic rows, 0 calls, writes selftest/dry_run_1p.json
    python3 runner_1p.py --preflight       # asserts L2 > 0, STOPS on L3-eligible 0, prints the plan
    # 4. freeze: commit phase1p, then
    git rev-parse HEAD > FREEZE_HASH
    # 5. ONCE
    python3 runner_1p.py --final
    # 6. leftover calls only, pre-declared
    python3 runner_1p.py --ablation

Any new `.py` in `phase1p/` must be appended to `FREEZE_FILES`, otherwise `check_freeze()` refuses
the run.

## Guarantees built into the runner

* `build_side()` **computes** `chk` with `runner_1l.compute_chk` and never asserts it; a degenerate
  all-accepting `chk` writes `STOP_CHK.txt` and exits with 0 calls made (the Phase 1k defect).
* `--preflight` asserts **L2 firings > 0**, writes `STOP_PREFLIGHT.txt` and exits on
  **L3-eligible 0**, and prints `dev_used + planned`; over **1,390** it writes `STOP_PLAN.txt` and
  makes 0 calls.  `run_calls()` re-checks the 1,400 cap before every batch.
* `--final` refuses if `FINAL_RUN_DONE` exists, refuses unless every frozen file matches
  `FREEZE_HASH`, reads the judge labels **only after** every planned verdict exists, and writes
  `results_1p.json`, `results_1p.md`, `calls.jsonl`, `access_log.jsonl`, then `FINAL_RUN_DONE`.
  A quota wall or a missing verdict writes `RUN_PAUSED.txt` and exits 3 **before any label is read**.
* `results_1p.json` carries, per item: `sid`, `half`, `level`, `judged`, `judged_type`, `tags`,
  `layers` (main layer / verdict / model reply / reached_l3), `lever1` (fired, agent, rewritten,
  rewritten layer + accept, **shadow** unrewritten accept + layer), `lever2_fired`, `lever3`
  (variants shown / removed + the removed detail), `final_accept`, `tip`.
* `--ablation` is pre-declared: the baseline `P-FROZEN-1N` stack with the levers OFF, on
  judged-correct determiner-tag L3-eligible items first, then judged-correct agentless items, in
  SID order, with leftover calls only, up to cap - 10.

## Known rough edges

* `assemble_1p.py --labels` looks for the judge files in `phase1p/judge/`; the self-test ran the
  judge side through `floor_check_1p.py --judge-dir`, so the `--labels` path is exercised only by
  its absent-file branch.  Check its output on the first real judge delivery.
* The synthetic fixture is in `selftest/fx/`; `data/` is empty on purpose and must stay that way
  until the writers deliver.
