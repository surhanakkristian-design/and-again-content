# Phase 1L — HANDOFF from agent A (build)

Work tree `~/Projects/and-again-content/translation-offline/phase1l/`. `phase1k/` is INPUT ONLY —
never edit it. I hit the 12-call harness cap; this file is the exact state.

## DONE

* **2.2 F9 negated-present fix — DONE and validated.** `phase1l/f9.py` is a copy of
  `phase1k/taskB/f9.py` with one change (four textual patches, all asserted at build time):
  a new `_pres_la(w)` helper (`(ne)` + `-iela|-ieľa|-iel|-ieľ`, plus a small lexicon
  `posiela / vysiela / zasiela / …`) is consulted in `_is_l_part` (such a token is NOT an
  l-participle) and in `_looks_present` (it IS a finite present verb), and `'iela'/'ieľa'` were
  added to `IMPF_SUF` so `aspect()` calls it imperfective and the frame comes out `present`
  rather than `{present, future}`. Nothing else in F9 is touched.
  `phase1l/f8.py` is a byte-for-byte copy (F8 unchanged) — it does `import f9`, so keep
  `phase1l/` first on `sys.path` OR rebind `runner_1k.f8/.f9` after import (see below).
* **F9 re-validation over the 140 existing DEV+holdout sentences — DONE**:
  `validate_f9_1l.py` → `F9_REVALIDATION_1L.md` + `f9_revalidation_1l.json`, Phase 1k §4 format
  (agree / conservative / error + every error listed), plus the unit test on the brief's sentence
  string and a diff of which sentences moved. Run it with
  `PYTHONDONTWRITEBYTECODE=1 python3 -B phase1l/validate_f9_1l.py` (0 calls, no fresh data).
* **2.3 hygiene export — DONE for dev**: `export_hygiene.py --side dev` wrote
  `hygiene/in_dev_*.json` ({sid, slovak, v} only, pretty, ≤ 1100 lines/file). Reads go through
  `loader_1l.py`, which redirects `loader_1k._log` into `phase1l/access_log.jsonl` (phase1k is
  read-only now).
* `RECORDED_NOT_MADE.md` written.

## NOT DONE — what remains

1. **`runner_1l.py` does not exist yet.** Everything in the brief's "Runner requirements",
   §5 accounting and `results_fresh.{json,md}` is open.
2. **The freeze** (`FREEZE_HASH`) — do it only once the runner reproduces the DEV replay.
3. **`export_hygiene.py --side fresh`** — must run AFTER the freeze commit (it is otherwise ready;
   it reads only the answer-free `sentences_fresh.jsonl`, which the loader allows ungated, and it
   logs the read).

## How to build `runner_1l.py` (all the recon I paid for)

Import, do not copy, the frozen machinery — this keeps the rule set literally identical:

```python
import sys, os
L1 = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1l')
sys.path.insert(0, L1)
import loader_1l as L                      # logs into phase1l/access_log.jsonl
sys.path.insert(0, os.path.join(os.path.dirname(L1), 'phase1k'))
import runner_1k as R1K                    # reads phase1k FROZEN_CONFIG_1K.json, judge labels, prompts
import f9 as f9_1l, f8 as f8_1l            # the phase1l copies
R1K.f9, R1K.f8 = f9_1l, f8_1l              # rebind: runner_1k prepends phase1k/taskB to sys.path
assert L1 in R1K.f9.__file__
```

Reusable as-is from `runner_1k`: `build_req`, `prompt_template_sha`, `judge_labels`,
`control_noise`, `locktip_decide`, `guard_readouts`, `apply_guards`, `score`, `configure_row`,
`_r`, `TYPES`, and the sub-modules `R1K.R` (= `phase1j/taskC/runner_1j.py`),
`R1K.P` (= `phase1i/pipeline_1i.py`, which holds `run_pipeline`, `to_item`, `rate` (Clopper-Pearson),
`ledger_append`, `load_key`, `_http`, `parse_reply`, `MODEL`, `API`).
**Copy, do not reuse, `ledger_state()` / `call_one()`**: they write into `phase1k/ledger.jsonl`.
In 1L they must APPEND to `phase1l/calls.jsonl` and READ (for reuse) all three of
`phase1j/ledger.jsonl`, `phase1k/ledger.jsonl`, `phase1l/calls.jsonl`. Same transport rules
(counted = http 200 only; 0/429/5xx retried with backoff, `counted:false`; empty 200 = failed,
counted, never retried, never guessed). Resume = replay `calls.jsonl` by `req_hash`.

### 2.1 — the builder (the whole point of Phase 1L)

`runner_1k.build_side('fresh')` (runner_1k.py ~line 339) builds each fresh record with
`'chk': {'verdict': 'correct', 'step': 'L1', 'feedback': ''}, 'chk_missing': True`. That single
line is the defect. The DEV path does `R.load_side(side, purpose)` → `R.prep_arm('B', side, data)`
(`phase1j/taskC/runner_1j.py`), and the real `chk` comes out of there. **I ran out of calls before
reading `prep_arm`'s body — read it first** (`awk 'NR>=x&&NR<=y'`, the `awk '/^def …/,/^def …/'`
range collapses on one-line matches; use `grep -n '^def ' runner_1j.py` and slice by line numbers).
Reproduce exactly what `prep_arm` does to fill `chk` — the deterministic checker is
`phase1i/checker_1i.py`, reachable as `R1K.R._C` (already used in `build_side` as `C.base.norm`
and `C.lock_equivalent_ok(P.to_item(r))`) — and drop `chk_missing`.
Fresh records otherwise stay exactly as `build_side` builds them (sentences_fresh + annotations
`hygienised` → `lk`/`locks`, `lock_ok`, `R.make_state(recs, ann, ('F4v3',), side_tag='fresh1k')`).

**PREFLIGHT (mandatory, before any model call):** print, for the fresh side, (a) the number of L2
lock firings/rejections under BASE and (b) the number of L3-eligible items
(`sorted(i for i, v in P.run_pipeline(stx, {}).items() if v['reached_l3'])` with
`stx = dict(st, decide=R1K.locktip_decide(st['decide']))`). Assert both non-zero; if either is 0,
write `phase1l/STOP_PREFLIGHT.txt`, exit non-zero, make no call. Phase 1k printed
`[FRESH] L3-eligible 0 … NEW needed 0` — that is the exact symptom to catch. DEV had 65 lock
rejections / 318 L3-eligible, the 1j replay 310 / 336, so a healthy fresh side should show lock
rejections in the tens and L3-eligible in the low hundreds.

### Expected call volume

Not knowable without opening fresh (I did not open it). Bound: ≤ 600 L3-eligible items × 2
reference variants (before / after hygiene), deduplicated by `req_hash` — only sentences the
hygiene pass actually touches produce a second distinct prompt, so the brief's ≈ 300–400 is
plausible and the 1,200 STOP ceiling is the hard gate. Phase cap 2,000 counted calls for the whole
phase; 667 were spent in 1k (1,333 left). Price $0.25/1M in, $1.50/1M out.

### Other runner requirements not to forget

`dev` mode with zero new calls (the P-FROZEN prompts for DEV are already in
`phase1j/ledger.jsonl` + `phase1k/ledger.jsonl`; `collect_verdicts(..., allow_calls=False)` raises
if anything is missing) and compare against the 1k replay numbers 90.82 % / 5.10 % / 3.39 % type-T
— note those are the **1j-holdout replay** figures (`--side replay1j`), the DEV reproduction target
is 182/189 coverage and 12/301 FA; state which you regress against and the F9-fix delta.
Refuse `fresh` if `phase1l/FINAL_RUN_DONE` exists or if the phase1l code files differ from
`FREEZE_HASH`. Three result columns (a) all 600 after hygiene, (b) excluding sid 140006 after
hygiene, (c) all 600 before hygiene (+ the same excluding 140006); coverage, FA, FA by type
T/W/M/S/V/E, FA by layer, false rejections by layer, all with exact Clopper-Pearson
(`R1K.P.rate(k, n)` returns `{k, n, pct, ci}`); the ACTIVE→PASSIVE and TIME-FRAME-SHIFT cells;
targets on the point AND on the interval; never average. §5 accounting as listed in the brief.
Build the fresh F9 hand-check validation INTO the runner in the same agree/conservative/error
format — the gold is `tf_gold` in `sentences_fresh.jsonl` (70/70 present; `runner_1k.final()` already
has a cruder version of this check, extend it, do not re-use its shape blindly).

## Budget note

phase1k was left writable by the previous session (`drwxr-xr-x`); I did not chmod it, and I wrote
nothing into it. Consider `chmod -R a-w phase1k` before the fresh run so the guarantee is
mechanical — `loader_1l` already keeps every write out of phase1k.
