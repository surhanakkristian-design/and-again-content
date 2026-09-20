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
