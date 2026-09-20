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
2026-09-20 16:15 DEFECT (inherited, FIXED as 2E change 4): the throughput guard counted a 429 back-off sleep as
zero throughput. cz_0002_s04_v's five-step ladder (60+120+240+480+960 s) is ~31 min of legitimate waiting; the
20-minute floor read it as a dead run and SOFT-STOPped at 15:11, so cz_0003, cz_0004 and cz_0005 were never
attempted. Floor raised to 45 min, which still catches 2C's hours-long throttling.
2026-09-20 16:15 DEFECT (recorded, NOT fixed): cz_0002_s04_v has now been refused with 429 on nine consecutive
attempts across two phases (2D: 4 attempts, 364,431 tok; 2E: 6 attempts, 555,531 tok = 919,962 tokens for zero
rows). Every other session of that batch passed first time, and 2D's give-ups were also s04 of cz_0002, cz_0003
and cz_0004. A per-chunk cause is more likely than the rate limiter. Not retried again in 2E: its 100 rows
(n 5365-5464) stay missing, which is precisely what the 2E assemble-what-is-complete rule exists to tolerate.
2026-09-20 16:35 prior session NOT adoptable -> treated as MISSING and re-run: phase2d/cz_0001_s07_v (rows is not a list (unparsable result))
2026-09-20 17:52 batch cz_0003 incomplete: sessions cz_0003_s04_v missing; 100 rows (6365-6464) not written, 900 rows written
