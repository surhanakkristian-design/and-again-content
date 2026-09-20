# DEFECTS — phase 2F Czech run (run_2f_cz.py)

Same convention as 2E: one timestamped line per defect, appended by the runner itself (`defect()`), plus
anything found by hand. A defect recorded and NOT fixed says so explicitly.

2026-09-20 23:40 DEFECT (mine, FIXED): I concluded twice that `nohup` and a double-fork/setsid daemon were
being reaped by the tool sandbox, because `ps -o pid,command | grep halves.py` printed nothing. The check was
wrong, not the launch: `ps` without `ax` lists only this session's own processes. Both launches were alive the
whole time, and by the time I had also started a third chain from the user's Terminal, THREE halves.py runs
were annotating cz_0002_s04_v against the same account at once. That contention is a plausible cause of the
429s on the second half (both duplicates logged their own "attempt 1 of 3" at 23:30:07 and 23:31:53). The two
duplicate chains were killed at 23:40; the Terminal chain (the one the user can see and stop) was kept. Seventh
occurrence of the same lesson: when a check fails, suspect the measuring apparatus first.
2026-09-20 23:26 DEFECT (recorded, NOT fixed): session() charges retry tokens to `retry_tokens_not_counted_
as_session` only when the CLI returns; a session killed from outside leaves its tokens uncounted in
ledger_2f_cz.json, so the tripwire under-reads real spend by that amount.
2026-09-20 23:52 batch cz_0002 incomplete: sessions cz_0002_s04_v missing; 100 rows (5365-5464) not written, 900 rows written
2026-09-21 00:28 batch cz_0003 incomplete: sessions cz_0003_s04_v missing; 100 rows (6365-6464) not written, 900 rows written

## D-2F-07 — the throughput guard measured a window with no session completion (FIXED, 2F change 3)

2026-09-21 00:13:25 the guard soft-stopped Part 1 with `STATE["tok"]` frozen at 285,312 while
`cz_0003_s04_v` was still in flight and had not returned.  `STATE["tok"]` only moves when a session
RETURNS, so one long session reads as 0.0 tok/s; the guard counted 20 consecutive "zero throughput"
minutes that were 20 minutes of legitimate work.  2F change 1 had excluded back-off SLEEP from the
clock but not IN-FLIGHT WORK THAT HAS NOT RETURNED.  Cost: 591,139 tokens in Part 1 for 0 new rows;
cz_0004 (1,000 rows) and cz_0005 (64 rows) were never attempted for the second phase running, and
Part 2's driver then found an empty measurement pool.

FIX (2F change 3, `ThroughputGuard.sample`): if `tok - k0 <= 0` and `STATE["inflight"] > 0` the window
is UNMEASURABLE — the streak is neither incremented nor reset and the guard cannot fire.  A pool that
is genuinely stuck is the circuit breaker's job (per-session wall and token floors, 3x the running
mean).  The guard still catches a pool that IS returning work far too slowly — 2C's five hours at
25 tok/s — because there `tok` rises.  Floor unchanged at 60 tok/s / 20 minutes; change 1 untouched.

## D-2F-08 — 50 paid-for rows could not enter the assembly (FIXED, 2F change 4)

`cz_0002_s04_v_h1` (n 5365-5414, 50 valid rows, 66,724 tokens) was unusable because the assembler
worked at whole-chunk granularity.  FIX: a half-chunk session `<sid>_h1`/`_h2` whose rows are a
contiguous sub-range of the chunk is accepted for its own rows; the chunk still counts as missing, so
`row_ranges_present` / `row_ranges_missing` in the meta record the partial coverage honestly.

## D-2F-09 — the lk comparison report died on a missing file (FIXED)

`out/REPORT_2f_lk.json` is never written when the lk stage has no new rows; step 5 of `run_part1.py`
then logged a `FileNotFoundError`.  It now writes `REPORT_2f_lk_compare.md` with an explicit
"no new rows" note in that case.

## D-2F-10 — a stale STOP file silently downgraded the lk stage (FIXED by procedure)

`run_part1.py` step 4 skips the paid lk pass when ANY `STOP_*.md` exists in the phase directory, so
the previous run's stop file would have downgraded this run too.  `STOP_throughput_guard.md` is moved
to `archive/STOP_throughput_guard_20260921_0013.md` before the relaunch.
