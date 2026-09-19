# Phase 1N — reads outside phase1n / phase1m / the 1M report

Format: `path | why the import chain forced it | label`

| phase1k/runner_1k.py | grep + sed ranges: `build_req` (the P-FROZEN request builder), `NEW_RULES` / `PROMPTS`, `judge_labels`, `guard_readouts`, `apply_guards`, `locktip_decide`, `TYPES`. It executes at run time as `R1K` (runner_1l.py:50) and holds the prompt assembly the task asked to quote | recon-code |
| phase1i/pipeline_1i.py | grep + sed ranges: `MODEL/GEN_CFG/API/ENV`, `GROUND_LINE`, `WORDING_LINE`, `pb_lines`, `sys_text`, `run_pipeline`, `rate`, `cp`. Executes as `P` (runner_1l.py:66) and carries the prompt lines and the CP-interval helper | recon-code |
| phase1i/lib_prev.py | grep: `SYS` and `prompt(it,'P-B')` — the verbatim system text and P-B lines of P-FROZEN, imported lazily inside `P.sys_text` / `P.pb_lines` at run time | recon-code |
| phase1i/checker_1i.py | grep: `prompt()` — confirms `C.prompt(it,'P-B')` delegates to `lib_prev._orig_prompt` and adds no voice rule. Executes as `C` (runner_1l.py:67) | recon-code |

No data file of any earlier phase was opened; no model call was made; nothing was written outside
`translation-offline/phase1n`.

## runner-build (Phase 1N runner)

* `phase1k/runner_1k.py` lines 40-120 / 180-310 / 430-460 — FORCED by the import chain:
  `runner_1n.py` rebinds `R1K.build_req` (prompt P-FROZEN-1N) and calls `R1K.guard_readouts`,
  `R1K.configure_row`, `R1K.judge_labels`, `R1K.locktip_decide`; their exact signatures and the
  `apply_guards` semantics (a guard may only turn an accept into a reject) had to be read.
* `phase1i/pipeline_1i.py` lines 25-60 / 125-200 — FORCED: `P.WORDING_LINE` is the insertion
  anchor of the 1N prompt line, and `P.run_pipeline` / `P.rate` / `P.GEN_CFG` are used directly.
* nothing was written to either directory; both are read-only.

* `phase1k/runner_1k.py` — read by `rescore-1m` (grep of `configure_row` / `guard_readouts` / `apply_guards`); forced by the import chain `runner_1n -> runner_1l -> runner_1k`, which supplies the pipeline configuration used by `rescore_1m.py`. 19 Sept 2026.
