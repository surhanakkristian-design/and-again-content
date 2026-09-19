# Phase 1N — runner handoff (label `runner-build`)

## Files written in `phase1n/`

| file | what |
|---|---|
| `runner_1l.py`, `loader_1l.py`, `f8.py`, `f8v2.py`, `f9.py` | byte-for-byte copies of the executed 1M modules (`cp`, then `chmod u+w`) |
| `runner_1n.py` | the 1N runner (written from `phase1m/runner_1m.py`; every 1M block kept, the changed blocks named below) |
| `loader_1n.py` | the 1N loader (from `loader_1m.py`); TYPES `('T','W','M','S')`, sids 160001..160100, judge `passive` key, `data_dir` / `judge_dir` / `types` parameters so the CLOSED 1M data can be re-scored WITHOUT writing into `phase1m` |
| `FROZEN_CONFIG_1N.json` | locktip true, `f8_module "none"`, `f8_decides false`, f9_decides false, tip_reject true, arm B, prompt `P-FROZEN-1N` |
| `FREEZE_FILES` | exhaustive; executed block first, then `prep_1n.py` |
| `PROMPT_DIFF_1N.md` | verbatim before / after of the one prompt line |
| `DEPENDENCY_READS.md` | appended: the two earlier-phase files the import chain forced (`phase1k/runner_1k.py`, `phase1i/pipeline_1i.py`) |

## TESTED (0 model calls in every test)

* `python3 -m py_compile runner_1n.py loader_1n.py` — OK.
* `--dev --f8 f8v2` on `fresh1m`: **coverage 547/614 = 89.09 % [86.35, 91.44]**, **FA 69/646 =
  10.68 % [8.41, 13.32]**, L2 249 / L3-eligible 1115, 1115 stored verdicts reused, 0 calls →
  **MATCH**, i.e. the copied stack is faithful.
* `--dev --f8 none` (the 1N headline configuration) on `fresh1m`: coverage 553/614 = 90.07 %,
  FA 94/646 = 14.55 % — the cost of F8 not deciding, as expected; MISMATCH against the 1M numbers
  is correct here.
* `--dev` sides `dev` / `replay1j` / `fresh1l` run and are reported; `DEV_EXP` / `REPLAY_EXP` are
  1L targets valid ONLY with `--f8 f8 --f9 on --tip reject` (the runner says so in
  `reproduction_scope`), so their MISMATCH under `--f8 f8v2` is expected, not a defect.
* `--selftest-final`: the ENTIRE post-transport path executed over fresh1m + stored verdicts —
  label merge, metrics, TIME-FRAME cell, PASSIVE cells (writer and judge tag), §5.1, the carried
  counters, the F8v1-on / F8v2-on / F9-on / TIP-off shadows, builder limit (29 near-misses),
  judge noise, section5, `selftest/results_selftest.json` + `.md`. Missing passive tags are
  tolerated (the 1M judge rows carry none: `judge passive tags 0`).
* `--dry` refuses cleanly with `REFUSED: .../data/annotations.json does not exist` — the data side
  has not delivered `annotations.json` / `items.json` yet.

## NOT TESTED (cannot be, yet)

* `--dry` / `--final` end to end — they need `data/annotations.json`, `data/items.json`
  (`sentences.json` is already there) and, for `--final`, `judge/` + `FREEZE_HASH`.
* `--probe` — it would spend counted calls; the code path is identical to `--final`'s transport.
* the real transport (unchanged 1M code: 6 workers, seed-1 shuffle, MIN_INTERVAL 0.30, 5 tries,
  counted = HTTP 200 only, empty 200 = counted failure never retried, streak-5 quota wall →
  `RUN_PAUSED.txt` before any label is read).

## Decisions taken

1. **The prompt.** `P-FROZEN` contains NO voice line at all (the voice rule lives in
   `runner_1k.NEW_RULES[1]`, appended only for `P-1K`). "Replace the voice line by the opposite"
   is therefore implemented as: take the finished `P-FROZEN` body from the original builder and
   insert exactly ONE line, `VOICE_SAME_LINE`, directly after `WORDING_LINE` — the inverted
   `NEW_RULES[1]` (`DIFF` → `SAME, provided the meaning is preserved`; its second sentence is
   already SAME and is kept word for word). Building on top of the original body guarantees every
   other byte is identical. Both readings are documented in `PROMPT_DIFF_1N.md`.
2. **F8 never decides.** `load_cfg` refuses `f8_decides true` / `f8_module != "none"`; the headline
   guards are `{'f8': None, 'f9': …}` and `apply_guards` is called with `f8_on=False`. Both modules
   are still read out per item; `f8_shadow()` reports headline-under-guard, COST (judged-correct it
   would reject), CATCHES (judged-wrong it would reject) and UNIQUE (of those, the ones the headline
   stack incl. L3 accepts), each with ids, plus the routing delta.
3. **`--dev` / `--selftest-final` / `--probe` use prompt `P-FROZEN`** for the stored sides —
   otherwise every stored verdict is a cache miss. `--probe` calls the NEW prompt and compares it
   with the stored old-prompt verdict per item.
4. **Judge type V retired** by `RL.TYPES = ('T','W','M','S')` (col_metrics reads the module global)
   and the same tuple in `loader_1n.py`; `R1K.TYPES` is left alone (it only feeds the 1J/1K replay).
   The 1M labels are re-scored with `types=TYPES_1M` so the reproduction stays exact. Writer intent
   `V` is still honoured: the AGENT-DEMOTION cell is emitted only when some item carries it.
5. **Cap 1200** counted calls for the whole phase, enforced over `phase1n/calls.jsonl` by
   `cap_or_stop()` in `--final` AND `--probe`; over the cap → `STOP_PLAN.txt`, exit, nothing trimmed.
6. **Carried, not patched**: the inert `released_by_LOCKTIP_total` beside the fixed routing counter,
   the two disagreeing F2B counters under `counter_A_routing_proxy_carried_bugs` /
   `counter_B_section5_bug3_inert_accept_flip`, `step=="mistake"` not released, and the
   reference-hygiene null (hygiene dir absent ⇒ off; chk before == chk after, both printed).
7. `RL.token_spend`'s hard-wired `PHASE_CAP - 667` estimate is dropped from `spend()`.
8. Ledgers: `LEDGERS_RO` gains `phase1l/calls.jsonl` AND `phase1m/calls.jsonl`, so the 1115 stored
   1M verdicts are visible (verdicts are mapped by `req_hash`, never by the ledger row's item id).

## Next steps for whoever runs it

1. Data side delivers `data/annotations.json`, `data/items.json` (with `passive`: null | by |
   agentless) and `judge/` (`blind_map.json`, `out_part*.json` incl. a possible `out_part9.json`,
   `controls_map.json`, `out_controls.json`, judge rows carrying `passive`).
2. `--dry` → check the chk distribution, the preflight (L2 > 0 and L3-eligible > 0; L3-eligible 0
   writes `STOP_PREFLIGHT.txt` and exits non-zero) and the plan against the 1200 cap.
3. Optional `--probe` (≤120 calls) before freezing.
4. Commit phase1n, write `FREEZE_HASH` with that commit, then `--final` ONCE.
   **Any new `.py` added to `phase1n/` must be appended to `FREEZE_FILES`**, otherwise
   `check_freeze_1n()` refuses the run.

---

## `dev-readout` (design readouts + hardening) — 19 Sept 2026

Ran, each once, 0 model calls: `--dev --f8 none`, `--dev --f8 f8v2`, `--selftest-final` (all exit
0; the self-test needed no fix, it was already clean end to end). Then `--probe` once, 120 counted
calls (cap 1200, 1080 left). Written: `DEV_READOUT_1N.md`, `PROBE_1N.md`, `probe_1n.json`,
`dev_regression_1n_{none,f8v2}.json`, `selftest/results_selftest.*`, `calls.jsonl` (120 rows).

### Fixes made to `runner_1n.py` (pre-freeze; `loader_1n.py` untouched)

1. **`run_dev` now emits per-side F8 shadow readouts.** It only ever reported the headline
   coverage/FA per side, so COST / CATCHES / UNIQUE existed for `fresh1m` in `--selftest-final`
   and for no other side. `run_dev` now rebinds each module in turn (`select_f8('f8')`,
   `select_f8('f8v2')`), recomputes `guard_readouts` / `configure_row` / `col_metrics`, and stores
   `row['f8_shadow_readouts']` (+ `row['labelled_items_in_shadow']`), printing one line per module
   per side. Insert point: immediately before the `exp = {...}` expectation block in `run_dev`.
2. **`select_f8('none')` does not rebind `R1K.f8`** — it returns the module that happens to be
   bound. Iterating the shadows would therefore have left F8v2 bound for every following side and
   silently changed their readouts. `run_dev` now captures `R1K.f8` before the shadow loop and
   restores it afterwards (falling back to `select_f8(sel['f8_module'])` when nothing was bound).
   The `--f8 f8v2` run still reproduces the 1M headline exactly after the change, which is the
   proof the restore works.
3. The shadow loop is fed only `ids_sh = [i for i in by if i in labels and i in res]`, so an
   unlabelled or verdict-less item can no longer raise a `KeyError` inside `f8_shadow` /
   `guard_delta` on a side whose judge file is incomplete.

Nothing else was touched: no guard added or tuned, no config change, `FROZEN_CONFIG_1N.json`,
`FREEZE_FILES` and the prompt are as `runner-build` left them. No new `.py` file, so `FREEZE_FILES`
needs no edit. No earlier-phase file was read, so `DEPENDENCY_READS.md` is unchanged.

### State for the next runner

* `--dev` (both settings), `--selftest-final` and `--probe` are now all exercised. Still untested:
  `--dry` / `--final`, which need `data/annotations.json`, `data/items.json`, `judge/` and
  `FREEZE_HASH`.
* The probe spent 120 of the 1200 counted calls; `--final` must be planned against the remaining
  **1080**.
* Selection rule recorded in `DEV_READOUT_1N.md` §3 (TASK B): guards are chosen on measured COST
  and measured catches; gold-assertion accuracy is a report-only diagnostic and never a gate.
