# Phase 1M — DRY RUN (no judge label was read, no model call was made)

* config: **LOCKTIP+F8V2 (TIP-as-rejection on) / P-FROZEN**, model `gemini-3.1-flash-lite`, temperature 0, thinkingBudget 0
* items 1260 over 140 sentences
* chk distribution (COMPUTED, never asserted): `{"correct/match": 110, "wrong/auto": 1150}`
* chk steps: `{"auto": 1150, "match": 110}`
* L2 lock firings under BASE: **249**   L3-eligible under LOCKTIP: **1115**
* unique requests **1115**, reusable from a ledger 0, NEW **1115**
* counted calls already in phase1m/calls.jsonl: 0; cap 1600; headroom 485
* level spread: `{"A1": 162, "A2": 261, "B1": 450, "B2": 387}`
* writer intents: `{"C": 560, "M": 61, "S": 83, "T": 61, "TF": 192, "V": 220, "W": 83}`
* writer forms: `{"None": 1040, "cleft": 54, "dropped": 68, "passive": 66, "reported": 32}`

## Verbatim output (`python3 runner_1m.py --dry`, label `freeze`, FINAL frozen config)

```
== Phase 1M DRY RUN — LOCKTIP+F8V2 (TIP-as-rejection on) / P-FROZEN
[BUILD] 1260 items / 140 sentences   chk distribution {"correct/match": 110, "wrong/auto": 1150}
L2 lock firings under BASE: 249   L3-eligible under LOCKTIP: 1115
[PREFLIGHT FRESH1M] (reference numbers: DEV 65/318, 1j replay 310/336, 1L fresh side non-zero)
[DRY] unique requests 1115   reused 0   NEW 1115   already counted in phase1m 0   cap 1600
-- written phase1m/DRY_RUN.md
```

* config read from `FROZEN_CONFIG_1M.json`: f8_module `f8v2`, f9_decides `false`, tip_reject `true`, locktip `true`, prompt `P-FROZEN`.
* gates: L2 lock firings under BASE 249 (non-zero), L3-eligible under LOCKTIP 1115 (non-zero), planned calls 1115 <= 1600 hard cap (headroom 485). Nothing trimmed.
* `phase1m/calls.jsonl` does not exist, so 0 counted calls; no `_smoke/` directory, no `STOP_*`, `RUN_PAUSED.txt` or `FINAL_RUN_DONE` artefact is left in `phase1m`.
* end-to-end synthetic smoke: run earlier in a `_smoke` copy with SYNTHETIC verdicts/labels and 0 model calls (`access_log.jsonl`, caller `smoke/driver_smoke.py`, 4 rows, 2026-09-19T07:15:41Z); the copy was removed and left no artefact.
* 0 model calls, 0 judge labels read.
