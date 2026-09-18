# Phase 1k — HANDOFF from agent R (DEV measurement, selection, FREEZE)

Read `CONTEXT_1K.md` (§0 verbatim) first. Everything here is DEV only. **The fresh side was never
opened**: `PHASE1K_OPEN_FRESH` was never set by me, `fresh/items_fresh.jsonl`, `writer_output*` and the
fresh judge rows were never read. Files: `taskA/TASK_A_RELABEL.{md,json}`, `taskD/dev_results.json`,
`taskD/TASK_D_DEV.md`, `taskD/dev_reproduction.json`, `taskD/DEV_REPRODUCTION.md`,
`FROZEN_CONFIG_1K.json`, `runner_1k.py`, `ledger.jsonl`, `access_log.jsonl`.

## 1 Task A — the relabelling (new labels = the blind judge's §0 verdicts, adopted IN FULL)

Conventions declared **before** the measurement: coverage denominator = **all items judged correct**
(any id kind; the kind-C-only figure is printed as a secondary line for continuity with 1j); FA
denominator = **all items judged wrong**; types **T / W / M / S / V (voice, new) / E**.

Movement against the Phase 1j arm-B **primary** labels, all 490 DEV items (0 items lack a judge verdict):

| direction | n | detail |
|---|---|---|
| unchanged | 452 | |
| correct -> wrong | 5 | by NEW type: `M 1, V 3, W 1` |
| wrong -> correct | 5 | by OLD type: `T 2, M 2, S 1`; by the 1j layer that had rejected them: `L2 lock 2, L3 1, (already accepted in 1j, i.e. it was a 1j false acceptance) 2` |
| wrong -> wrong, type changed | 28 | `S->W 7, S->M 5, T->W 5, T->M 2, T->S 2, T->V 1, S->V 1, M->V 1, W->T 1, S->T 1, M->T 1, T->E 1` |

New cell sizes (the denominators of every number below): **189 judged correct** (180 of them kind C),
**301 judged wrong** — T 54, W 76, M 66, S 98, **V 6**, E 1. In Phase 1j the arm-B primary coverage
denominator was 185 kind-C-correct items. **The movement is large enough that no coverage or FA number
in this file may be compared with a Phase 1j number**: the definition of "correct" changed. Old cell
sizes are in `taskA/TASK_A_RELABEL.json`.

## 2 Tasks B/C/D — the DEV rows

Design: an item's L3 verdict under a given prompt is computed once; guards and switches are readouts on
top, so all 36 rows share the same 636 stored verdicts. 318 items are L3-eligible under LOCKTIP (the
frozen 1j arm B reached L3 on 256 of them; the other 62 were stopped by the L2 lock and needed new
P-FROZEN calls). Every L3-eligible item has a verdict under **both** prompts. 0 items ended without a
verdict (no empty 200s).

| configuration | prompt | TIP-rej | coverage | FA | FA T |
|---|---|---|---|---|---|
| BASE (= frozen arm B of 1j, new labels) | P-FROZEN | on | 175/189 = 92.59 % [87.88, 95.89] | 12/301 = 3.99 % [2.08, 6.86] | 0/54 = 0.00 % [0.00, 6.60] |
| BASE | P-FROZEN | off | 177/189 = 93.65 % | 26/301 = 8.64 % | 0/54 = 0.00 % |
| BASE+F8 | P-FROZEN | on | 175/189 = 92.59 % | 11/301 = 3.65 % | 0/54 = 0.00 % |
| BASE+F9 | P-FROZEN | on | 175/189 = 92.59 % | 12/301 = 3.99 % | 0/54 = 0.00 % |
| **LOCKTIP** | **P-FROZEN** | **on** | **182/189 = 96.30 % [92.52, 98.50]** | **13/301 = 4.32 % [2.32, 7.27]** | **0/54 = 0.00 % [0.00, 6.60]** |
| LOCKTIP | P-FROZEN | off | 184/189 = 97.35 % | 30/301 = 9.97 % | 1/54 = 1.85 % |
| LOCKTIP+F8 | P-FROZEN | on | 182/189 = 96.30 % | 12/301 = 3.99 % | 0/54 = 0.00 % |
| LOCKTIP+F9 | P-FROZEN | on | 182/189 = 96.30 % | 13/301 = 4.32 % | 0/54 = 0.00 % |
| LOCKTIP+F8+F9 (ALL) | P-FROZEN | on | 182/189 = 96.30 % | 12/301 = 3.99 % | 0/54 = 0.00 % |
| LOCKTIP+F8+F9 (ALL) | P-FROZEN | off | 184/189 = 97.35 % | 29/301 = 9.63 % | 1/54 = 1.85 % |
| BASE | P-1K | on | 173/189 = 91.53 % | 12/301 = 3.99 % | 0/54 = 0.00 % |
| BASE | P-1K | off | 176/189 = 93.12 % | 21/301 = 6.98 % | 0/54 = 0.00 % |
| LOCKTIP | P-1K | on | 180/189 = 95.24 % | 12/301 = 3.99 % | 0/54 = 0.00 % |
| LOCKTIP | P-1K | off | 183/189 = 96.83 % | 24/301 = 7.97 % | 1/54 = 1.85 % |
| LOCKTIP+F8 | P-1K | on | 180/189 = 95.24 % | 11/301 = 3.65 % | 0/54 = 0.00 % |
| LOCKTIP+F8+F9 (ALL) | P-1K | on | 180/189 = 95.24 % | 11/301 = 3.65 % | 0/54 = 0.00 % |
| LOCKTIP+F8+F9 (ALL) | P-1K | off | 183/189 = 96.83 % | 23/301 = 7.64 % | 1/54 = 1.85 % |

The `f9.REPORTED_STRICT = True` rows are identical to their non-strict twins on DEV (the switch changes
no DEV item). All 36 rows with FA by type T/W/M/S/V/E and exact CP intervals: `taskD/dev_results.json`,
rendered in `taskD/TASK_D_DEV.md`.

**Selected row, itemised (LOCKTIP / P-FROZEN / TIP on):** coverage 182/189 = 96.30 % [92.52, 98.50],
kind-C-only 176/180 = 97.78 %; FA 13/301 = 4.32 % [2.32, 7.27]; FA by type T 0/54 = 0.00 %,
W 2/76 = 2.63 %, M 3/66 = 4.55 %, S 6/98 = 6.12 %, **V 2/6 = 33.33 % [4.33, 77.72]**, E 0/1.
FA by layer: L1 5, L3 8 (five wrong answers are exact matches of an accepted reference — no layer above
L1 can see them). FR by layer: L3 5, L3:TIPrej 2.

### What the L2 lock released

The lock rejected **65** DEV items in the frozen 1j configuration. Under LOCKTIP: **8** of them end up
accepted — **7 judged correct** (this is the whole coverage gain, 175 -> 182) and **1 judged wrong**
(type S). The other 57 are still rejected, now by the model or by a guard, so releasing the lock cost
almost nothing in FA (+1 item, 12 -> 13).

### F8 / F9 caught and cost (on top of LOCKTIP / P-FROZEN / TIP on)

- **F8** (voice): distribution over the 490 DEV answers `accept 460, reject 1, abstain 29`. Caught
  **1** judged-wrong answer that the configuration otherwise accepts (`C:23360:1881410199`), and it is
  the only layer that catches it. **Own cost: 0** judged-correct answers.
- **F9** (time frame): distribution `tip 168, accept 253, abstain 35, reject 34`. Caught **0**
  additional judged-wrong answers (every item it rejects is already rejected by L1/L3/a guard) and its
  **own cost is 0**. On DEV, F9 is inert — that is not evidence that it is useless, only that the DEV
  answers do not contain a time-frame error that survives the model layer.

### B3 line (F9 tip / abstain)

| F9 verdict | n | judged correct | judged wrong | cost = judged-wrong type-T items the SELECTED config accepts |
|---|---|---|---|---|
| tip | 168 | 66 | 102 | **0** |
| abstain | 35 | 19 | 16 | **0** |

### Task C — P-1K versus P-FROZEN on identical items (318 items, both verdicts)

Discordant model verdicts: `SAME->DIFF 1, TIP->DIFF 8, SAME->TIP 3, TIP->SAME 1, DIFF->TIP 1` (14 of
318 = 4.4 %). P-1K is strictly **stricter**: at TIP-on it loses 2 correct items (182 -> 180) and gains
nothing on FA (13 -> 12, and 12 -> 11 with F8); at TIP-off it is better on FA (30 -> 24) at the cost of
coverage (184 -> 183). The new rule text did **not** improve the voice or time-frame classes on DEV —
DEV contains only 6 voice items and no surviving time-frame errors, so Task C is under-powered here and
the fresh 70 (>= 30 V and >= 30 TF probes) is where it can actually be judged.

TIP switch re-measured under the new labels, both prompts: switching TIP-as-rejection **off** buys
+1.05 pt coverage for +5.65 pt FA (P-FROZEN) and +1.59 pt for +3.98 pt (P-1K). Every full row is in
`taskD/dev_results.json` -> `task_c.tip_switch`.

## 3 Selection trace (applied mechanically by `select()` over the stored rows)

1. 36 candidate rows (9 configurations x 2 prompts x TIP on/off).
2. Gate `FA point estimate < 5 % AND type-T FA point estimate < 5 %`: **18 rows pass**.
3. Highest coverage among the survivors: 96.30 % — a four-way tie (LOCKTIP, LOCKTIP+F8, LOCKTIP+F9,
   LOCKTIP+F8+F9, all P-FROZEN / TIP on).
4. Tie-break as pre-declared: fewer moving parts wins -> **LOCKTIP**, then P-FROZEN.

**-> FROZEN: LOCKTIP / P-FROZEN / TIP-as-rejection ON, F8 off, F9 off** (`FROZEN_CONFIG_1K.json`,
prompt sha256 `def440d1…`, f8.py `bb4662b5a0f74da7`, f9.py `0aa46d60cc9c64b0`).

> **Flag for the owner, not a deviation:** `LOCKTIP+F8` has the *same* coverage (182/189) with a
> *lower* FA (3.99 % vs 4.32 %) and zero measured cost; the pre-declared tie-break ("fewer moving
> parts") is what excluded it. If the owner prefers dominance over parsimony, switching `F8` to true in
> `FROZEN_CONFIG_1K.json` is a one-line change and needs **0 new calls** — but it must be decided
> before the fresh run, not after.

## 4 The runner

`runner_1k.py` executes the frozen config on three sides through **one** shared code path
(`build_side()` differs, `collect_verdicts()` / `configure_row()` / `score()` are identical):

```
cd ~/Projects/and-again-content/translation-offline
PYTHONDONTWRITEBYTECODE=1 python3 -B phase1k/runner_1k.py final --side dev                  # 0 calls, done, OK
PYTHONDONTWRITEBYTECODE=1 python3 -B phase1k/runner_1k.py final --side fresh    --max-calls 600
PYTHONDONTWRITEBYTECODE=1 python3 -B phase1k/runner_1k.py final --side replay1j --max-calls 400
```

- `--side dev` re-ran now and reproduced the selected row **exactly with zero new calls** (182/189,
  13/301) — printed `DEV reproduction with ZERO new calls: OK`.
- `--side fresh` sets `PHASE1K_OPEN_FRESH=1` itself, refuses if `FINAL_RUN_DONE` exists, adopts the
  judge labels for `source=="fresh"` (label + type in full), computes judge noise from the 60 controls
  (any flip / correct->wrong / wrong->correct with CP intervals), writes `taskD/fresh_results.json` +
  `taskD/FRESH_TABLES.md` (coverage, FA, FA by type with CP; the ACTIVE->PASSIVE cell and the
  TIME-FRAME-SHIFT cell each on its own line with the rejecting layers; writer-intent x judge-label
  table; every FA and FR itemised with layer, model reply, Slovak, answer, judge type, F8/F9 verdicts;
  the B3 tip/abstain line; the out-of-sample `f9.sk_frame` vs `tf_gold` check on the 70 fresh
  sentences), then writes `FINAL_RUN_DONE`. **It is the one measurement — run it once.**
- `--side replay1j` scores the 490 Phase 1j holdout items with `source=="holdout1j"` labels; its tables
  are titled *ALREADY-SEEN DATA — not the headline*.
- The fresh item records are built from `sentences_fresh.jsonl` + `annotations_fresh.json` (`lk` ->
  `locks`, `lock_ok` computed exactly as `checker_1i` does, `chk` synthesised); since the frozen config
  never rejects on the lock, a wrong `locks` value can only change the tip text.
- Budget: `--max-calls N` is hard — the runner counts `counted:true` rows in `phase1k/ledger.jsonl`
  and refuses before calling if `counted + new > N`.

## 5 Calls, tokens, spend, budget

`counted (HTTP 200) 466 · reused byte-identical prompts 170 · failed (empty 200) calls 0 ·
non-200 attempts 0 · tokens in 163,561 · tokens out 466 · spend $0.04159`
(at $0.25/1M in and $1.50/1M out; whether the calls were billed or free-tier is not visible in the
response body). **Phase budget left: 2,000 − 466 = 1,534 counted calls.** The fresh run needs about one
call per L3-eligible fresh item (<= 600 items, so <= 600 calls); `replay1j` needs about 150–250 new
ones (the 1j holdout arm-B calls are reused from `phase1j/ledger.jsonl`).

## 6 Known guard bugs / limitations (recorded, NOT patched — no calls left to re-validate)

1. **F8 fires only on an English passive main clause** (agent G's own note). The DEV set has 6 voice
   items and the selected config accepts 2 of them (FA V 33 %, CI [4, 78]). Both are voice failures the
   *model* waved through and F8 did not see. This is the single biggest risk for the fresh run, where
   >= 30 answers are V probes. Nothing was changed on DEV evidence.
2. **F9 is inert on DEV** (0 caught, 0 cost). `REPORTED_STRICT` changes no DEV item, so the switch is
   untested on real data; it is frozen at `False`.
3. **F2B is not applied to lock-released items.** In the frozen stack F2B can withdraw a tip granted by
   F2; a LOCKTIP release is a §0 tip and is deliberately not exposed to F2B (recorded in
   `FROZEN_CONFIG_1K.json.switches`). It affects at most the 8 released items.
4. **A mistake-pattern rejection at L2 (`step == "mistake"`) is not released** — only the structure lock
   is. Fresh sentences carry no `m` patterns, so this cannot fire there.
5. Five of the 13 false acceptances are **L1 exact matches** of an accepted reference: the judge calls
   them wrong, the annotation calls them right. No layer above L1 can ever catch those; if the owner
   wants them, the `v` lists of those sentences have to change, not the checker.

## 7 Freeze

`git commit` of `translation-offline/phase1k` — short hash in `FREEZE_COMMIT.txt` (left uncommitted;
the next agent commits it together with the fresh results). Nothing was pushed, no DB was touched, no
app code and no edge function were changed, and `$J` was not written to (the loader logs into
`phase1k/access_log.jsonl`).

## 8 Agent R self-count

11 harness tool calls: 1 context dump, 2 reads of that dump + `runner_1j.py`, 2 targeted inspections
(pipeline/checker/judge/ledger), 1 write of `runner_1k.py`, 1 measurement run, 1 DEV reproduction,
1 write of this hand-off, 1 commit. Cap was 12.
