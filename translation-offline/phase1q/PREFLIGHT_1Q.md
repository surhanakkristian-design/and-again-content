# Phase 1Q - preflight and dry run, 0 counted model calls

Both were run on 2026-09-19 against the frozen stack (FREEZE_HASH
255ef142625a14434f82758ea733cc5cf7c2fe79). Ledger `phase1p/calls.jsonl`: 225 rows, 225 counted - unchanged
by this step.

## `python3 runner_1p.py --preflight` - PASS

```
[BUILD fresh1p] 1080 items / 120 sentences   chk {"correct/match": 83, "wrong/auto": 997}   passive {"None": 768, "agentless": 270, "by": 42}
levers {"l1:answer_is_agentless_passive": 276, "l1:fired": 239, "l2:aspect": 828, "l2:definiteness": 1000, "l2:number": 207, "l3:items_with_a_variant": 1026, "l3:removed": 72, "l3:shown": 1080}
L2 lock firings under BASE: 272   L3-eligible under LOCKTIP: 925
[PREFLIGHT] unique requests 925   reusable 0   PLANNED NEW CALLS 925   counted so far 225
[PREFLIGHT] dev_used + planned = 225 + 925 = 1150   (stop threshold 1390, phase cap 1400)
[PREFLIGHT] PASS
```

The L2 > 0 assertion holds (272 lock firings) and L3-eligible is 925, not 0, so no
`STOP_PREFLIGHT.txt` and no `STOP_PLAN.txt` was written.

## Planned calls

| step | planned counted calls |
|---|---|
| dev already spent | 225 |
| `--final`, main side (L3-eligible items, prompt P-FROZEN-1P) | 925 |
| `--final`, lever-1 side (rewritten answers, computed here with the runner's own `lever1_side` / `l3_eligible` / `plan`; preflight does NOT show this) | 239 |
| **total after `--final`** | **1389** |
| leftover under the phase cap 1,400 | 11 |
| leftover the ablation may use (`cap - 10 - counted`) | **1** |

Arithmetic: 225 + 925 + 239 = 1389; 1,400 - 10 - 1389 = 1.
Preflight only compares `225 + 925 = 1150` against its 1,390 threshold, so the lever-1
side is NOT inside the number it prints; `run_calls()` re-checks the hard 1,400 cap before every
batch, and 1389 <= 1,400, so `--final` fits.

## How the ablation fits, and what happens when the leftover is too small

`--ablation` is pre-declared and narrows by **truncation only**, never by redesign: it builds the
baseline side (levers OFF, prompt P-FROZEN-1N), takes the judged-correct determiner-tag L3-eligible
items in SID order, then the judged-correct agentless ones, sets `budget = max(0, 1390 - counted)`
and stops adding requests at `len(need) >= budget`. With 1 calls left it therefore measures the
first ~1 determiner items only; the tail and the agentless block are simply not measured. With a
budget of 0 it makes 0 calls and writes `ablation_1p.json` with whatever verdicts already exist
(effectively nothing). The four pre-declared ablation arms (lever 1 / 2 / 3 alone, all three) cannot
be bought from this leftover - that has to be said plainly in the readout rather than papered over.

## `python3 runner_1p.py --dry-run` - PASS, 0 counted calls

```
[BUILD synthetic] 6 items / 2 sentences   chk {"correct/match": 1, "wrong/auto": 5}
[DRY-RUN] L2 0   L3-eligible 5
[DRY-RUN] {"n_items": 6, "unique_requests": 5, "l2": 0, "l3_eligible": 5}
[DRY-RUN] lever1 {"fired": 2, "gain": 0, "fa_cost": 0, "shadow_accept": 2}
[DRY-RUN] written selftest/dry_run_1p.json - 0 model calls
```

Two guarantees re-verified in the source:

* `build_side()` **computes** `chk` with `RL.compute_chk(r)` per record and never asserts it
  (runner_1p.py: `r['chk'], h = RL.compute_chk(r)   # COMPUTED, never asserted`). On the real side
  the distribution is `{"correct/match": 83, "wrong/auto": 997}` - not degenerate.
* The degenerate all-accepting STOP exists: if the chk distribution has one value and every record
  is accepting, `STOP_CHK.txt` is written and the run exits with 0 model calls made.

No `STOP_*.txt`, no `RUN_PAUSED.txt`, no `FINAL_RUN_DONE` is present, so `--final` is free to run.

## Pace and expected duration

`calls.jsonl` carries no wall-clock field (keys: cached_tokens, candidates_tokens, counted, empty, finish, http, item_id, latency_ms, max_output, model, prompt_tokens, reply, req_hash, thinking, thoughts_tokens, try, ts, variant, verdict), so the dev run gives no measured rate. The
free-tier `gemini-3.1-flash-lite` key is the binding constraint: at the free-tier ~15 requests/min
the 1,164 run calls take about **1 h 20 min**, at 10/min about **2 h**, plus the backoff the
transport adds on every 429. Plan for two to three hours and do not interrupt the shell.
