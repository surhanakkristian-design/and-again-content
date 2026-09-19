# TOOLING_EDITS_1T — every diff-hunk category against the frozen 1P runner

`runner_1t.py` does not copy `runner_1p.py`: it **imports** it (and through it runner_1n /
runner_1l / runner_1k / the checker), so the prompt, the transport, the pacing, the quota wall, the
layers, LOCKTIP, TIP-as-rejection, `compute_chk`, `lock_counts`, `plan()` and `decide()` are the
frozen code, byte for byte.  `MODULES_1T.txt` lists the 28 imported files; `FREEZE_FILES` freezes
them.  The categories below are the complete list of what 1T does differently.

## A. The three differences the task asked for

1. **lever 1 removed** — `LEVERS = (2, 3)`; `FROZEN_CONFIG_1T.json` refuses any other list;
   `lever1_side()` / the rewritten request set / the `suppress_f4v2` path are never entered, so the
   run has one request set and no lever-1 call.  (`phase1p/lever1.py` is still imported because
   `runner_1p` imports it at module level; it is never called.)
2. **rule AG v3 before L3** — `ag_map()` runs `agent_drop_v3.decide(..., flags=('clause','subj','by'))`
   per item (source side only: Slovak, annotation, writer_tags, reference, answer) plus the 0-call
   shadows `v2`, `v3_clause`, `v3_subj`, `v3_by`.  `plan_ids()` removes every AG-fired item from the
   L3 list, so it costs 0 calls and never reaches L3; `ag_layer()` attributes the outcome exactly as
   `rescore_1s_c.build()` did for K3 (an earlier non-L3 deterministic rejection keeps its layer,
   otherwise the layer is `AG`).  Nothing downstream reads an AG-rejected item's model verdict.
3. **RUNNER_PATCH_1S in full** — `safe_json.safe_dump` at every write site (results, markers, STOP /
   PAUSED files, dry-run report), serialise-before-truncate, `write_done_marker`, `guarded_run`
   around the paid-for entry point, and every reply appended to `calls.jsonl` by the frozen
   transport **before** any aggregation (the dry run proves the offline replay is identical).

## B. Consequences of running a different set (not stack changes)

4. `loader_1t.py` instead of `loader_1p.py`: sid range 180001–180100, the 1T tag vocabulary
   (`agentdrop-main`, `agentdrop-embedded`, `skp-passive`, `by-passive-embedded`, …), `writer_tags`
   kept on the sentence, and a single label door `set/data/labels.json` in assemble_1t's schema
   (`judged, type, passive, agent_drop, tip, borderline`).  Access log: `phase1t/run/access_log.jsonl`,
   1N convention.  The three data reads carry caller `runner_1p.py` because the frozen
   `build_side()` performs them.
5. `FINAL_ITEMS_EXPECTED = 900`, side tag `fresh1t`, halves by SPLIT_1T.md (odd sid → P1) — the same
   `half_of()` function as 1P.
6. `set_run_dir()` re-points every write site of the imported stack (calls.jsonl, access log, run
   log, STOP/PAUSED/DONE markers, `runner_1p.HERE`, `runner_1p.CFG_PATH`) into `phase1t/run`, so the
   run cannot write into phase1p / phase1n; the dry run re-points them again into `selftest/`.

## C. Gates that 1P did not have or could not express

7. **cap from the config**: `call_cap` is read from `FROZEN_CONFIG_1T.json`; `null` makes `--final`
   and `run_calls()` refuse, and `--preflight` stops with `STOP_PLAN.txt` at cap − 10 (1P hard-wired
   1400 / 1390).
8. **check_freeze rewritten**: entries are paths relative to the repository root, so the AG rule
   (`phase1t/taskA/agent_drop_v3.py`), `agent_drop_v2.py` and `safe_json.py` can be frozen — the 1P
   version could not name a file outside its own directory (see the note in `phase1p/FREEZE_FILES`).
   It also refuses if any `.py` the process imported is missing from the list.
9. **floor gate**: `--final` refuses unless `set/FLOOR_CHECK_1T.json` reports all five 1T floors.
10. **the pause is not a crash**: the quota wall returns `status: PAUSED` (RUN_PAUSED.txt already
    written, no label read) and the exit 3 happens outside `guarded_run`, so the marker does not
    claim CRASHED.
11. **scoring is a separate file**: 1P scored inline; 1T's runner writes rows + a headline k/n only,
    and `score_1t.py` produces every figure twice (primary and S2) with exact Clopper-Pearson
    intervals and Fisher's exact test, from the rows, with 0 calls.
12. **modes**: `--dev` and `--ablation` do not exist in 1T; `--dry-run` runs the real `--final` code
    path against a stubbed model (13 checks).

Nothing in this list touches a prompt, a layer, a threshold, a lever's logic, the checker, the
transport or the label path.
