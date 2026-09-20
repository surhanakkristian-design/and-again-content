# Phase 2E plan — printed before any tokens are spent

20 September 2026. Budget **4,000,000** harness tokens. **Gemini calls 0. DB SELECT only — nothing is written
to the database.** No deploy, no migration, no push, no checker rule change, no rebase. `phase2c/out/` and
`phase2d/out/` are INPUT and stay byte-identical (baseline `SHA_inputs_before.txt`, 224 files). Everything is
written under `phase2e/` and committed as it is produced.

## §1 — the brief defect that caused 2D's zero, fixed first

2D annotated 3,200 Czech rows and wrote **zero** batches: each of four batches lost exactly one v session to a
429 give-up, and the rule was "a batch is written only when all 20 of its sessions are complete".

**New rule, implemented in `run_2e_cz.py` (`2E change 1`): assemble whatever is complete.** A batch's rows are
written as soon as *their own* sessions are done. A missing v session costs its 100-row chunk; a missing rw
session costs only that chunk's rewrite-fallback rows; **nothing else in the batch is affected.** Every batch
carries `annotations_cz_NNNN.meta.json` recording `row_ranges_present`, `row_ranges_missing`,
`sessions_present`, `sessions_missing`. A complete batch gets `DONE_cz_NNNN`; an incomplete one gets
`PARTIAL_cz_NNNN.json` and is re-assembled, not skipped, on any later run.

## Task A — the nine missing v sessions plus the missing rw sessions (≈ 1.08 M)

* Every finished session in `phase2d/out/sessions/` (and `phase2c/out/sessions/`) is **COPIED**, never moved,
  into `phase2e/out/sessions/`, logged `ADOPT` and `SKIP-DONE … 0 tokens`. Adoption **rejects** any file that
  does not parse, did not exit 0, or does not cover its whole chunk — which is how `cz_0001_s07_v`
  (2D: exit 0, unparsable, 81,602 tok) comes back as missing and is re-run.
* To run: `cz_0001_s07_v`, `cz_0002_s04_v`, `cz_0003_s04_v`, `cz_0004_s04_v`, `cz_0004_s07_v`,
  `cz_0004_s08_v`, `cz_0004_s09_v`, `cz_0004_s10_v`, `cz_0005_s01_v` + the missing rw sessions
  (`cz_0004_s04/s06..s10_rw`, `cz_0005_s01_rw`).
* Runner = 2D's Czech runner unchanged except §1 and one constant: **PAR = 2**, 429 back-off from 60 s with
  jitter, circuit breaker (3× running mean, floors 900 s / 200,000 tok), 60 s throughput monitor (60 tok/s
  floor over 20 min), per-batch projection gate. 2D measured 399–480 tok/s with the monitor never firing, so
  the pacing is right. **`MAX_RETRY` 3 → 5** (`2E change 2`): 2D's four give-ups burned 1.26 M tokens for zero
  rows; a fifth attempt is cheaper than a lost batch. Every retry is logged `counted:false`.
* Then `annotations_cz_0001..0005.jsonl`, `DONE_cz_NNNN`, and **GATE 3 per batch** — random 50, AG v4 and
  `reader_nom`, bar 12 %, g4 diagnostic only, never gated.
* Cap `--cap 1,400,000`.

## Task B — the dedicated lk pass for Czech (≈ 1.9 M)

`run_2e_lk.py` = `run_2d_lk.py`'s method, reading Phase 2E's own Czech batches: the model sees **only** `en`
and `correct_answer_en`, prompt sha16 **`5fa910459c078539`** (asserted in code), fixed **PAR = 2**, N = 100.
2D measured 473.5 tok/sentence. Reports the non-exact rate per batch with exact 95 % Clopper–Pearson against
Slovak's **51.13 % [49.58, 52.68]**, how many values changed, and every span rejected for not being a
contiguous substring of `en` (Slovak: exactly 1). Writes `out/lk_corrected_cz.jsonl` and merges into
`out/annotations_cz_final.jsonl`, replacing **only** `lk[0]`, `lk_verdict`, `lk_reason`, with a round-trip
assert that every other field is byte-identical. **Low-mode watch:** any session under **30 %** non-exact is
archived to `out/sessions_lowmode/<sid>.attempt1.json` and re-run exactly once. Cap `--cap 2,100,000`.

## Task C — the upload package

`out/upload_cz_final.xlsx`, sheet `cz`, columns `exercise_id`, `language_code`, `level`, `src`, `en`,
`structure_json` — the same format as 2D's Slovak file — plus a Czech addendum to `UPLOAD_README.md` stating
the largest `structure_json` cell against Excel's 32,767 limit. **Nothing is uploaded.**

## Budget arithmetic

| item | tokens |
|---|---|
| Task A (9 v × 83,422 + ~7 rw × 46,606, measured 2D means) | ≈ 1,077,000 |
| Task B (4,064 rows × 473.5, measured 2D) | ≈ 1,924,000 |
| main session + any agents | ≈ 250,000 |
| **projected total** | **≈ 3,251,000 of 4,000,000** |

Cumulative tokens and the projected total are printed after every session; the run STOPS if the projection
exceeds the budget. Launched under `nohup`, so a closed window does not kill it.

## Self-test (0 model calls, before launch)

`run_2e_cz.py --all --self-test --dry-run` exercised prompt construction, adoption (including the rejection of
`cz_0001_s07_v`), the back-off ladder at the new ceiling of 5, the circuit breaker, the throughput guard, the
projection gate, partial and complete assembly, GATE 3 arithmetic and its STOP path, and both upload writers,
in an isolated `out_dry/`.
