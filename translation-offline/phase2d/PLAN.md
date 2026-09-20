# Phase 2D plan (printed before starting)

Budget 8,000,000 harness tokens. Gemini calls 0. DB SELECT only. Nothing written to the database.
`phase2c/out/` is INPUT and stays byte-identical (SHA baseline: `SHA_phase2c_out_before.txt`).

## Task A — the lk defect (~1.0 M)
A1 DONE BEFORE ANY SPEND (see report §1). The 41 Slovak v-session prompts share ONE byte-identical fixed
   prefix (sha256[:16] = 63abade8fac1971a, 3,122 chars); the lone session's prefix equals the four-up
   session's byte for byte; the runner sets no temperature and passes no concurrency-dependent flag.
   2C's "lone vs four-up" statistic is an artefact: its "smoke session" IS `sk_0001_s01_v`, reused by the
   full run (`SKIP-DONE`), so its 48/100 was compared against a batch mean that already contains it.
A2 Dedicated lk pass, 2B's judge method (`LK` prompt from `phase2b/run_2b.py`), extended by one field so the
   pass also returns the corrected span. N = 100/session, **fixed concurrency 2 for every session**, 41 sessions.
A3 Rates per batch + pooled with exact Clopper-Pearson; count of changed values; write
   `out/lk_corrected_sk.jsonl` and `out/annotations_sk_final.jsonl` (2C output, only `lk`/`lk_verdict`/`lk_reason` replaced).
A4 GATE 3 on a random 250 of the merged output (AG v4 + reader_nom, bar 12 %), 0 model calls.

## Task B — Czech (~5.5 M), only after A
Reuse the 13 finished `cz_0001` sessions (assert before spawning, log every skip). PAR = 2. 429 -> exponential
back-off from 60 s with jitter, max 3 retries then give up on the session. Mid-run throughput check: abort and
report if measured throughput stays under 60 tok/s for 20 min. After every batch: recompute projected finish,
STOP if > 4 h; print cumulative tokens, STOP if the projection exceeds the budget.

## Task C — upload package
One .xlsx per language (format A: structure as JSON in one cell) + `UPLOAD_README.md`. Nothing uploaded.

## Order
A2/A3 -> A4 -> B (sequential; A and B must not share the rate-limit window) -> C -> report.
