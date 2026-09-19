# Phase 2C production annotation — the plan, printed before the run starts

20 September 2026. Runner: `phase2c/run_2c.py`. Selection: `phase2c/selection_2c.jsonl` = **8,128 rows**
(sk 4,064 + cz 4,064; 56 rows per language carry an empty `correct_answer_*` and are annotated anyway with the
flag `empty_correct_answer`). 0 Gemini calls, 0 DB access, writes only inside `phase2c/`, nothing pushed.

## 1. Pipeline, per sentence

| step | who | what |
|---|---|---|
| 1 | SCRIPT `derive_2c.derive(row, mode="after")` | `person`, `number`, `perfective_present` — **the only three fields GATE 1 passed** (sk 4.29 / 1.37 / 7.41 %, cz 8.82 / 2.94 / 5.45 %). Also the arm-B rewrite and the AG v4 / reader_nom / g4 voice paths, which are carried on the row for GATE 3 and are **not** used as annotation. |
| 2 | SCRIPT, model fallback | arm-B rewrite (`U`/`R` + machine check). Where the reader ABSTAINs, a `*_rw` session runs 2B's REWRITE prompt verbatim (sk+cz widened, the 2B assert kept). Model `R` is applied only if the token machine check passes. |
| 3 | MODEL, one session per 100 rows | `v`, the **lk correction**, `voice`, `subject`, `agent_nom`, `embedded_agents`, `gender`, `tf`, `tense_open`, `fragment`, `main_sentence_index`, plus `person`/`number`/`perfective_present` on the rows where the script abstained. |
| 4 | SCRIPT | `alt`: every content token of `en` classified `mapped` / `propose_new` / `unmapped` against the phase1b group table (`table.json` + `forms.json` + `ng_phase1c.json`), alt_map_2b.py's classifier reused. |

**lk is corrected, not copied.** 2B SCORE #5: the v session returned lk[0] unchanged on 100/100 sk rows —
including the 41 the lk judge marked *adjust* — and Czech did the same (`vcz_2c.json`: `lk0_copied_unchanged` 100).
So the v prompt now states that `lk_supplied` is often wrong, forbids copying by default, and **requires per row**
`lk_verdict ∈ {exact, adjusted}`, the corrected span, and a one-clause `lk_reason`. Per batch the adjust rate goes
into `gates_2c.json`; **below 5 % it writes a DEFECT line and the run continues** (never a stop).

**voice and agent_nom are authored by the model on every row** even though the script also computes them: they
failed GATE 1 (voice sk 14.29 / cz 11.36 %, agent_nom sk 11.63 / cz 21.05 %), and GATE 3 needs an independent
annotation to score the script paths against.

## 2. Session and batch layout

* N = **100 rows per session**, **4 sessions in parallel** (`--par`), model `opus`, bundled CLI 2.1.275,
  `--output-format json --max-turns 12`. OAuth token read via `zsh -ic` into the env; never printed, never logged.
* Batches of 1,000 rows, one language each: `sk_0001..sk_0004` (1,000) + `sk_0005` (64), same for `cz`.
* Per batch: 10 `*_v` sessions + up to 10 `*_rw` sessions (only for chunks that have ABSTAIN rows).
  Whole run: **82 v-sessions + ≤ 82 rw-sessions**.
* After each batch: `out/annotations_{lang}_{NNNN}.jsonl` → git commit → GATE 3 → `gates_2c.json` → `DONE_<batch>`.
* First completed batch only: both upload candidates into `out/` and committed —
  **A** `upload_candidate_A_<batch>.xlsx` (exercise_id, language_code, level, src, en, **the whole structure as JSON in one cell**),
  **B** `upload_candidate_B_<batch>.csv` (flat, keyed `exercise_id` + `language_code`, 30 columns).

## 3. Projected cost

**(a) A-priori, from 2B/GATE 2 components** (the base the brief names): v 493.4 (mean of measured v_sk 476.7 and
v_cz 510.1) + 5.93 extra model-authored fields/row × 13.5 output tok = 80.1 + lk correction folded into v ≈ 40.5
− the separate lk pass 245.6 (folded, not run) + rewrite fallback 268.5 over all rows = **882.5 tok/sentence**
→ 8,128 × 882.5 = **7.17 M**. (The 1,050.1 tok/sent re-extrapolation = 8.54 M includes the separate lk pass.)

**(b) Revised with the smoke session actually measured** (sk_0001_s01_v, 100 rows): **91,375 tokens = 913.75
tok/sentence** for the v session (in 2, cache_creation 21,630, cache_read 22,462, output 47,281 = 473 out/row).

| component | rows | tok/row | total |
|---|---|---|---|
| v + lk + all model fields | 8,128 | 913.75 (M) | 7.43 M |
| rewrite fallback (2B: 553.6/row, 40–48.5 % of rows) | 3,250–3,942 | 553.6 (M, 2B) | 1.80–2.18 M |
| **projected total** | | | **9.2 – 9.6 M** |

**Under the 10,500,000 cap, but at 88–92 % of it.** There is no headroom for retries or for a second pass over a
failed batch. This is stated, not hidden: if the cap would be breached the runner stops cleanly (§5) with every
completed batch already written and committed, and the remainder can be run later under a raised cap by decision.
The 91,375 tokens of the smoke session are in `ledger_2c.json` and count toward the cap; the full run **reuses**
that session and does not redo it.

## 4. Projected wall clock

Measured: the smoke v session took **450.7 s for 100 rows = 4.51 s/sentence serial** (2B's v_sk was 0.54 s/sent,
v_cz 0.99; the extra authored fields quadruple the output and so the time). Rewrite fallback 1.14 s/row (2B).

* serial: 8,128 × 4.51 + ~3,900 × 1.14 = 36,655 + 4,450 = 41,105 s
* **at 4 parallel: ≈ 10,280 s = 2.85 h** (a-priori (a) would have been ≈ 0.8–1.5 h)

Under the 5 h cap, with about 2 h of margin for contention between the four parallel sessions. The runner does not
trust this estimate: after batch 1 it projects the total from the real elapsed time and stops if it exceeds 5 h.

## 5. Caps and STOP conditions

| guard | bar | on breach |
|---|---|---|
| headless tokens | 10,500,000, all tokens incl. cache reads, across resumes (`ledger_2c.json`) | in-flight pre-check before **every** spawn (spent + in-flight × EST + this session's projected cost from the running mean); breach → `STOP_token_cap.md`, exit 3 |
| wall clock | 5 h, projected from batch 1 (elapsed/row × 8,128) | `STOP_wall_projection.md`, exit 3 |
| GATE 3 AG v4 | ERROR-of-decided > 12 % on the batch's 50 scored rows | `STOP_gate3_agv4_<batch>.md`, exit 3 |
| GATE 3 reader_nom (fixed, P1–P3) | ERROR-of-decided > 12 % | `STOP_gate3_reader_nom_<batch>.md`, exit 3 |
| g4 harness guard | — | **DIAGNOSTIC ONLY, never gates.** 2B settled it: g4 is built over AG v2/v3 and 20 of its 23–28 raw errors are the one reflexive `si`/`sa`/`se` pattern the arm-B rewrite amplifies by construction. |
| lk adjust rate | < 5 % per batch | DEFECT line in `DEFECTS_run_2c.md`, **run continues** |
| OAuth token missing | — | `STOP_no_oauth_token.md` at 0 cost |
| unknown argv | — | exit 2 before anything runs; `--only` ids that match no session are exit 2 at the end |

A stop file is a decision, not a hiccup: while one exists the runner refuses to start and says so; `--ignore-stop-file`
is the explicit override.

GATE 3 scores **50 deterministic rows per batch** (`random.Random(sha256(batch_id))`), the script's AG v4 voice path
(`agv4_main_passive|agv4_main_reflex`) and the fixed reader_nom agent against **that batch's own model annotation**
(2B's `g3cls` word-overlap rule; script abstention = CONSERVATIVE, not an error). Numbers land in `gates_2c.json`
as each batch finishes.

## 6. Idempotency and resume

* Launch: `nohup python3 run_2c.py --all > /dev/null 2>&1 &` — resume with the **same command**.
* A batch with `out/DONE_<batch>` **and** its annotations file is skipped whole, before any derivation or spawn.
* A session is skipped when `out/sessions/<sid>.json` exists, parses, has `exit 0` and contains every row of its
  chunk; otherwise it is re-run. Nothing else can trigger a re-run — this is the 2B failure mode (a failed resume
  silently re-ran five finished sessions and breached the cap) and it is now impossible by construction.
* Annotations are written only when **every** session of the batch is complete on disk; otherwise the batch logs
  PARTIAL and writes nothing.
* Every artefact is committed the moment it is written (session file, ledger, annotations, gates, uploads, log),
  `git add <path>` only, never `git add -A`.

## 7. Smoke test (done before this plan was finalised)

* Dry run (`--dry-run`, 0 model calls, isolated `out_dry/` + `*_dry` artefacts): prompt construction, selection
  loading, derivation, assembly, GATE 3 arithmetic, the STOP path, both upload writers, and the batch-level
  idempotent skip all exercised; unknown argv rejected with exit 2.
* One real session, `sk_0001_s01_v`, the first 100 rows of batch sk_0001: **exit 0, 100/100 rows returned,
  0 missing fields, 91,375 tokens, 450.7 s**, v[0] = the reference on 100/100, two variants on 4,
  `lk_verdict` adjusted on **48/100** (2B's v session changed 0/100; the 2B judge said 20.5 % need it — 48 % is
  the diagnostic to watch, the opposite failure of 2B's), voice 52 active_agent / 39 active_prodrop / 6 passive /
  3 impersonal, model-authored residual nulls on 35 person / 34 number / 27 perfective_present rows.
  Re-running the same command printed `SKIP-DONE` and spent 0 tokens.
* That session's output stays on disk and is reused by the full run.
