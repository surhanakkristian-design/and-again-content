# Phase 1P — call plan

Hard cap for the WHOLE phase: **1,400 counted calls** (`runner_1p.PHASE_CAP_1P`, enforced in
`run_calls()` before any request leaves). counted = HTTP 200 only; http 0 / 429 / 5xx is retried
with backoff and logged `counted:false`; an empty 200 is a counted failure, never retried, never
guessed.  Free-tier key first (`runner_1l.load_keys()[0]`).

## Planned before any call was made (printed by `--dev --lever N` without `--go`)

| step | items | planned counted calls |
|---|---|---|
| baseline reproduction of 1N on the closed side | 900 | **0** (834 stored verdicts reused) |
| lever 1 — 35 detector hits (26 judged-correct + 9 judged-wrong exposure), rewritten answers | 35 | 33 |
| lever 2 — 41 non-agentless L3 false rejections + 55 judged-wrong (38 time-frame, 17 other) | 96 | 96 |
| lever 3 — the same two sets | 96 | 96 |
| **dev total** | | **225** (cap 300) |

Cut from the suggested plan to stay under 300: the FA sample is **55 per lever, not ~70**
(70 % weighted to the time frame), and the lever-1 exposure cap is 40 (only 9 items exist).  No
lever was ever measured in combination with another.

## Spent

* dev: **225 counted calls** (`phase1p/calls.jsonl`, 225 rows, 225 http 200, 0 empty, 0 transport-dead).
* remaining under the phase cap: **1175**.

## Expected final run (1,080 items, 120 sentences)

* main requests = the L3-eligible items.  On 1N that was 834/900 = 92.7 %, so **~1,000** for 1,080
  items.
* lever-1 rewritten records: the detector fired on 35/900 = 3.9 % of 1N answers, and the 1P set is
  built to carry far more agentless passives (floor: 60 judged-correct + 60 judged-wrong), so
  budget **~150**.
* expected total **~1,150**, i.e. 225 + 1,150 = **1,375 <= 1,400**.  `--preflight` prints
  `dev_used + planned` and **STOPS** (writes `STOP_PLAN.txt`, 0 calls) if it exceeds **1,390**.
* `--ablation` is pre-declared and runs on the leftover only, up to cap - 10 = 1,390.
