# Phase 1O Task A/D — dependency reads

Imported in-process (forced by the chain `taskA_oldprompt -> runner_1n -> runner_1l -> runner_1k -> ...`); nothing was written into any of these directories:

* `phase1i/checker_1i.py`
* `phase1i/lib_prev.py`
* `phase1i/pipeline_1i.py`
* `phase1i/reference_hygiene.py`
* `phase1i/taskB/backfill_s_ids.py`
* `phase1i/taskB/lock_fix.py`
* `phase1i/taskC/guards_c.py`
* `phase1j/loader_1j.py`
* `phase1j/taskA/p_chain.py`
* `phase1j/taskC/runner_1j.py`
* `phase1k/loader_1k.py`
* `phase1k/runner_1k.py`
* `phase1n/f8.py`
* `phase1n/f8v2.py`
* `phase1n/f9.py`
* `phase1n/loader_1l.py`
* `phase1n/loader_1n.py`
* `phase1n/runner_1l.py`
* `phase1n/runner_1n.py`
* `phase1o/diag/taskA_oldprompt.py`

Read by hand (source text): `phase1n/runner_1n.py` (whole), `phase1n/HANDOFF_RUNNER_1N.md`, `phase1n/FROZEN_CONFIG_1N.json`, `phase1n/DEPENDENCY_READS.md` (tail); via `inspect.getsource` only the functions the module calls: `runner_1l.call_one / ledger_state / token_spend / load_keys / plan_requests / hashes_for / col_metrics / _r`, `pipeline_1i.rate / run_pipeline / ledger_append`, `runner_1k.configure_row / apply_guards / locktip_decide`, `runner_1j.ledger_rows`, `loader_1n._log / load_labels`.
