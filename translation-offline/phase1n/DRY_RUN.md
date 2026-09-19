# Phase 1N — DRY RUN (label `dry-run`)

19 Sept 2026. `python3 runner_1n.py --dry` in `phase1n/`. **No judge label was read, no model call was
made.** Exit code **0**. Run twice; the second run produced a byte-identical `DRY_RUN_1N.md` (md5
unchanged) and left `calls.jsonl` at 120 rows, so the plan is deterministic.

## 1. Verbatim console output

```
== Phase 1N DRY RUN — LOCKTIP+F8-READOUT-ONLY (TIP-as-rejection on) / P-FROZEN-1N
[BUILD fresh1n] 900 items / 100 sentences   chk distribution {"correct/match": 33, "wrong/auto": 867}   passive tags {"None": 795, "agentless": 22, "by": 83}
L2 lock firings under BASE: 205   L3-eligible under LOCKTIP: 834
[PREFLIGHT FRESH1N] (reference numbers: DEV 65/318, 1j replay 310/336, 1M fresh 249/1115)
[DRY] unique requests 834   reused 0   NEW 834   already counted in phase1n 120   cap 1200
-- written phase1n/DRY_RUN_1N.md
```

The runner's own file `DRY_RUN_1N.md` (written by the run, verbatim):

```
# Phase 1N — DRY RUN (no judge label was read, no model call was made)

* config: **LOCKTIP+F8-READOUT-ONLY (TIP-as-rejection on) / P-FROZEN-1N**, model `gemini-3.1-flash-lite`, temperature 0, thinkingBudget 0; F8 decides NOTHING, F9 off, TIP-as-rejection on, arm B
* items 900 over 100 sentences
* chk distribution (COMPUTED, never asserted): `{"correct/match": 33, "wrong/auto": 867}`
* chk steps: `{"auto": 867, "match": 33}`
* L2 lock firings under BASE: **205**   L3-eligible under LOCKTIP: **834**
* unique requests **834**, reusable from a ledger 0, NEW **834**
* counted calls already in phase1n/calls.jsonl: 120; cap 1200; headroom 246
* level spread: `{"A1": 117, "A2": 189, "B1": 324, "B2": 270}`
* writer intents: `{"C": 400, "M": 100, "S": 100, "T": 25, "TF": 175, "W": 100}`
* writer forms: `{"None": 900}`
* writer passive tags: `{"None": 795, "agentless": 22, "by": 83}`
* hygiene: OFF (phase1n/hygiene present: False)
```

## 2. The five numbers the task asks for

| quantity | value |
|---|---|
| COMPUTED chk distribution | `{"correct/match": 33, "wrong/auto": 867}` (steps `{"auto": 867, "match": 33}`) |
| L2 lock firings under BASE | **205** |
| L3-eligible under LOCKTIP | **834** |
| planned unique requests | **834** (reusable from a ledger 0, NEW 834) |
| counted calls so far in `phase1n/calls.jsonl` | **120** (the `dev-readout` probe) |

## 3. Against the HARD CAP

```
planned 834 + counted 120 = 954   <=   1200
headroom 246
```

**Under the cap.** Nothing was trimmed and nothing needed to be; status is not "blocked".

## 4. Preflight

Both preflight conditions hold: L2 firings 205 > 0 and L3-eligible 834 > 0, so no
`STOP_PREFLIGHT.txt` was written. No `STOP_PLAN.txt`, no `RUN_PAUSED.txt` exists.

The build ratios sit next to the 1M reference rather than drifting, which is the sanity argument
that the new loader is reading the new data correctly:

| ratio | 1N fresh (900 items) | 1M fresh (~1260 items) |
|---|---|---|
| L3-eligible / items | 834 = 92.7 % | 1115 = 88.5 % |
| L2 lock firings / items | 205 = 22.8 % | 249 = 19.8 % |

The low `correct/match` count (33 of the 400 writer-C items) is **not** a defect: `match` is the
cheap exact-match short-circuit, and `assemble_1n.py` writes paraphrased correct answers, so almost
every correct item is routed on as `auto` and gets decided downstream. The floor check reads 426 of
900 judged correct, which is the labelled truth and has no reason to equal the pre-label `match`
count. chk is COMPUTED and never asserted, per the runner's own note.

## 5. Bugs hit and fixes made

**None.** The runner and loader ran the new data end to end on the first attempt. No loader or
runner bug was hit, so no pre-freeze fix was made, `HANDOFF_RUNNER_1N.md` lists no new fix under
this label, and — since the task ties the `--selftest-final` re-run to "after any fix" — no re-run
was owed and none was made. `runner_1n.py`, `loader_1n.py`, `FROZEN_CONFIG_1N.json`, `FREEZE_FILES`
and the prompt are byte-for-byte as `dev-readout` left them. No new `.py` file, so `FREEZE_FILES`
needs no edit.

## 6. Blind integrity

The three `access_log.jsonl` rows the dry run appended are `data/sentences.json`,
`data/annotations.json`, `data/items.json` only — no `judge/*` file was opened, confirming the
"no label read" contract. `calls.jsonl` stayed at 120 rows across both runs, confirming "no model
call".

## 7. Exact next step

`--probe` is optional and already spent (120 calls, `dev-readout`). The next step is: commit
`phase1n`, write `FREEZE_HASH` with that commit, then run `--final` ONCE against the remaining
**1080** counted calls, of which the plan needs **834**.

No DB write, no app code change, nothing deployed, no migration, no git push, no commit was made by
this label.
