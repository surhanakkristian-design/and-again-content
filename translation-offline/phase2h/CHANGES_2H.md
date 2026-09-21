# Phase 2H - changes vs Phase 2G Part B

One runner, `run_2h.py` (subcommands `annotate`, `lk`, `merge`, `upload`, flag `--dry`, `--cap`, `--no-spawn`), replaces
run_2g_cz.py + run_2g_lk.py + prep_lk.py + final_merge.py + build_upload_2g.py. The prompts (VPROMPT, REWRITE, LK_2D),
the 2C derivation call, row assembly and the alt mapping are copied byte for byte from 2G by `make_2h.py` (ast line
ranges, sources' sha256 recorded in the block header). Everything below is new or fixed.

1. **False 429 (defect 1).** `should_retry`/`post_call`/`_post_call_lk` looked for the substring "429" in stdout+stderr;
   rows n=5429/6429/7429 echo it in successful output. Replaced by ONE `classify(rc, stdout, stderr)`: a
   `{"type":"result","is_error":false}` envelope with exit 0 is SUCCESS, full stop. Rate limit = HTTP status FIELD
   429/529 (`api_error_status`, `http_status`, `status_code`, `status`, nested `error.status`) or API error type
   `rate_limit_error`/`overloaded_error`; auth = 401/403 or `authentication_error`/`permission_error` (no retry);
   5xx field -> retry; non-zero exit -> retry. Usage limit/quota = `is_error: true` + USAGE_RE on the error
   envelope's own message only. Result text and stderr are never searched.
2. **`_samp` recursion (defect 2).** `rnd.sample(pop, min(k, len(pop)))`; one definition for both gates.
3. **Rows stranded by GATE 3 (defect 3).** A batch's rows are assembled, written and committed BEFORE its gate. A
   GATE 3 STOP no longer stops the run: it writes `STOP_gate3_<metric>_<bid>.md`, marks that batch's rows
   `gate3: "STOP"` (annotations file, meta and final jsonl) and excludes them from the upload xlsx only. Every other
   batch continues.
4. **Stop-file scoping (defect 4).** Only `STOP_usage_limit.md`, `STOP_first_session_failed.md`, `STOP_token_cap.md`
   stop further headless sessions (either stage). Gate STOP/FLAG files and 2G-style `STOP_rows_missing` never block.
5. **Chunks (defect 5).** 10-row pieces removed; N=100, PAR=2. The 20 still-missing gap rows (5425-5434, 6425-6434)
   run as ONE chunk `cz_gap_s04_v` (their rewrite rows come from the adopted cz_0002/0003_s04_rw sessions).
6. **README heading (defect 6).** `UPLOAD_README.md` starts with "Phase 2H"; 2F's README is appended with demoted
   headings.
7. **GATE 3 decision.** 50 random rows (seed sha256(bid), as 2G) of the rows new to 2H per batch (cz_gap: its 20,
   cz_0004 / cz_0005: all rows), on AG v4 and reader_nom, bar 12 %, g4 recorded only. Exact two-sided 95 %
   Clopper-Pearson on ERROR-of-decided: decided < 40 -> FLAG only (never STOP, even at 0 decided); CP lower > 12 %
   -> STOP that batch; point > 12 % -> FLAG; else PASS. 2G stopped on the point estimate.
8. **Token budget.** One ledger (`ledger_2h.json`) and one `--cap` for both stages. Before every launch:
   `spent + sum(estimates in flight) + next estimate <= cap`, else STOP_token_cap.md. After every session: cumulative
   tokens + projection to completion in run_2h.log, progress.log, session_timeline_2h.jsonl. Plans with per-session
   estimates are written first (`PLAN_annotate.json`, `PLAN_lk.json`). Estimates: 2F's measured per-row means of its
   full-chunk sessions (floors 40k v / 20k rw); lk 440 tok/row-run; 1,379 tok/row shown as the reference.
9. **Adoption.** 2E's check (parses, rows list, exit 0, non-empty, v chunk fully covered), COPY only, from
   phase2f/out/sessions then phase2g/partB/out/sessions; 2G's annotations_cz_0001..0003 copied as present rows.
   Resume: a complete session file is skipped at 0 tokens; a finished chunk never re-runs.
10. **Hard stops.** First headless session of a process fails (spawn/auth/exit, anything but a rate-limit envelope)
    -> STOP_first_session_failed.md; usage-limit envelope -> STOP_usage_limit.md; both raise and end the process after
    what exists is assembled and committed (2G used os._exit).
11. **lk stage.** Same prompt (sha16 asserted at import) and argv. Targets: the 280 rows 2G judged + every row new in
    2H (1,084), sessions of 100, PAR 2. Acceptance: run 1 >= 30 % non-exact -> accepted; else run 2; runs differ by
    > 15 points -> run 3 and per-row majority (tie -> unusable > adjust > exact); else run 2 >= 30 % accepted, below ->
    `accepted_below_bar`. A failed run 2 keeps run 1 (`accepted_below_bar_run2_failed`); a failed run 3 keeps run 2.
    Every run logged with rate and exact CP95 in `lk_sessions_2h.json`. lk GATE 3 (250 rows, seed 20260920) computed
    and recorded; its FLAG/STOP files block nothing.
12. **merge / upload.** `out/annotations_cz_final.jsonl` over every present row (unique n, sorted): 2H lk judgement
    applied where present, else 2G's final row, else the annotation row; `out/upload_cz_final.xlsx` (sheet cz, same six
    columns) without gate-STOPPED batches.
13. **Commits.** Only `translation-offline/phase2h` is added and committed (`git commit -- <path>`), after every
    session, gate, stage.
14. **Chain.** `chain_2h.sh`: input SHA before, FROZEN_SHA check, tests (abort at 0 spend on any FAIL), annotate, lk,
    merge+upload, SHA after + diff, DONE. No setsid, no daemonize.py.
