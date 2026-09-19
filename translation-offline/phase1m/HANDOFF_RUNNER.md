# Phase 1M — runner handoff (label `runner-build`)

Files written: `loader_1m.py`, `runner_1m.py`, `FROZEN_CONFIG_1M.json`, `FREEZE_FILES`
(+ generated `run_1m.log`, `dev_regression_1m.json`).

## What is TESTED

* `--dev --f8 f8 --f9 on --tip reject` **reproduces Phase 1L exactly**, 0 model calls:
  * dev coverage 182/189 (96.30 %), FA 12/301 (3.99 %), FA-T 0/54; lock 65 / L3 318
  * replay1j 178/196 (90.82 %), 15/294 (5.10 %), FA-T 2/59 (3.39 %); lock 93 / L3 336
  * fresh1l 191/217 (88.02 %), 15/383 (3.92 %), FA-T 3/130 (2.31 %) — the 1L report numbers
  Stored verdicts come from phase1j + phase1k ledgers **plus `phase1l/calls.jsonl`**, which
  `runner_1m` appends to `RL.LEDGERS_RO` at import (the 1L ledger is invisible otherwise).
  0 cache misses on all three sides.
* Both files compile; `--dry` and `--final` refuse cleanly (F8 module absent / no FREEZE_HASH /
  overrides outside `--dev`).
* Every data read is logged to `access_log.jsonl` (loader_1m writes the same
  `{ts, side, what, caller, n, purpose}` line as `loader_1l._log`).

## What is NOT tested (no data existed yet)

1. **Everything that touches `data/*.json`**: `build_side_1m`, the chk distribution/abort,
   `preflight_1m`, the plan, `l1_nearmiss`. `--dry` is the first thing to run the moment
   `data/` and an F8 module exist.
2. **`f8v2`**: selected by name from the config, loaded by file path via importlib and bound to
   `R1K.f8`. It must expose `check(slovak, annotation, answer) -> {'verdict': ...}` like `f8.py`.
   Only `--f8 f8` has actually run.
3. The whole `--final` body after the plan: transport, quota-wall pause, label merge, metrics,
   cells, shadows, markdown. Never executed.
4. `judge/*` parsing: no file existed. `load_labels` merges `out_part*.json` via `blind_map.json`
   and validates judged/type; unknown jids and wrong-without-type land in `meta['rejected_rows']`.

## Decisions a later agent must know

* `FROZEN_CONFIG_1M.json` carries the brief's keys with defaults `f8_module f8v2`,
  `f9_decides false`, `tip_reject true`, `locktip true`, `prompt P-FROZEN`. **The values of
  f8_module / f9_decides / tip_reject are the orchestrator's**, not mine — set them before the
  freeze commit. `--dry`/`--final` refuse any CLI override; `--dev` takes `--f8/--f9/--tip`.
* `FREEZE_FILES` lists all 10 `.py` in `phase1m` incl. the not-yet-written `f8v2.py`.
  `check_freeze_1m` compares each against `<FREEZE_HASH>:translation-offline/phase1m/<f>` and
  additionally refuses if a `.py` exists in the directory but is missing from the list.
* Cap: **1600 counted calls for the phase**, counting `counted:true` rows already in
  `phase1m/calls.jsonl`. Over cap ⇒ `STOP_PLAN.txt`, exit, nothing trimmed.
* Quota wall = 5 consecutive requests that exhaust their retries ⇒ remaining requests are skipped,
  `RUN_PAUSED.txt`, exit 3, **no label is read and no FINAL_RUN_DONE is written**. Rerunning
  `--final` resumes: stored verdicts are reused by request hash.
* An empty HTTP 200 is a counted failure: the request lands in `ledger_state`'s `failed`, the item
  keeps no verdict, is absent from `vm`, cannot be accepted at L3, and is reported in
  `no_verdict_items`.
* `make_state(..., side_tag='fresh1m')` is used; if the tag is rejected the runner says so and
  falls back to `'fresh1k'` — check `run_1m.log` for that line.
* `reference`/`refs` are derived from the annotation `v` (first entry = displayed reference), the
  way `apply_hygiene` promotes them. Sentences are natively arm B: **no `prep_arm` anywhere**.
* Hygiene is off unless `phase1m/hygiene/out_fresh1m_*.json` appears (`RL.HYG` = `phase1m/hygiene`).
* §13 near-miss: the per-token rule (<= 1 edit/token) applies to equal token counts; answers whose
  token count differs are matched on whole-string Levenshtein <= 2 and reported separately as
  `len_mismatch_subset`.
* §12 F2B: F2B is not separately callable offline, so — exactly as Phase 1L did — the carried bug is
  counted as "every lock-released item is an item F2B never sees". Stated as such in the output.
* `RL.section5` (the 1L §5 block) is called for continuity inside a `try`; if the new side breaks
  it, the error string is stored under `section5_1L_block` and nothing else is affected. The §11
  fixed counter and the §12 bugs are computed independently of it.
