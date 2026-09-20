2026-09-20 14:42 prior session NOT adoptable -> treated as MISSING and re-run: phase2d/cz_0001_s07_v (rows is not a list (unparsable result))
2026-09-20 14:49 DEFECT (inherited from 2C/2D, FIXED here as 2E change 3): the per-batch projection gate
extrapolated this process's tok/row over EVERY remaining row, including the 2,964 rows already paid for by
adopted 2D sessions. After cz_0001 (1 session run, 90,322 tok, 903.2 tok/row over 100 paid rows) it projected
2,857,788 tokens for the 3,064 "remaining" rows and issued STOP projection_budget against the 1,400,000 cap --
a false stop: the true remainder is 8 v sessions + <=7 rw sessions, about 1.1 M. The gate now extrapolates only
over rows whose v session is not complete on disk, plus an upper bound of EST['rw'] per absent rw session.
STOP_projection_budget.md is renamed .RESOLVED.md and the run resumed with --ignore-stop-file.
2026-09-20 14:50 prior session NOT adoptable -> treated as MISSING and re-run: phase2d/cz_0001_s07_v (rows is not a list (unparsable result))
2026-09-20 16:12 batch cz_0002 incomplete: sessions cz_0002_s04_v missing; 100 rows (5365-5464) not written, 900 rows written
