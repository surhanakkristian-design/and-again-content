# CHANGES_2F.md — `phase2e/run_2e_cz.py` -> `phase2f/run_2f_cz.py`

Exactly two behavioural changes, plus the mechanical repointing of artefact paths at 2F (`ledger/gates/log/DEFECTS` 2e -> 2f, output under `phase2f/out/`, adoption source `phase2e/out/sessions/` first). Line numbers are 1-based; OLD = `phase2e/run_2e_cz.py`, NEW = `phase2f/run_2f_cz.py`.

| # | OLD lines | NEW lines | what |
|---|---|---|---|
| insert | 56-55 | 56-56 | `E2 = os.path.join(BASE, "phase2e")                          ` |
| replace | 71-71 | 72-74 | `MAX_RETRY = 5                    # 2E change 2: ceiling rais` |
| replace | 77-80 | 80-84 | `TP_MIN_SAMPLES = 45              # 2E change 4: a full 5-ste` |
| replace | 114-117 | 118-121 | `LEDGER = os.path.join(H, "ledger_2e_cz%s.json" % DRY)` |
| replace | 159-159 | 163-163 | `commit([fn, LEDGER, GATES, LOGP], "Phase 2E: STOP %s" % reas` |
| replace | 170-170 | 174-174 | `commit([fn, LOGP], "Phase 2E: soft stop %s" % reason)` |
| insert | 407-406 | 411-439 | `# ----------------------------------------------------------` |
| replace | 411-411 | 444-444 | `self.samples = collections.deque(); self.low = 0; self.reaso` |
| replace | 417-419 | 450-453 | `dt = t - t0` |
| replace | 436-436 | 470-471 | `"inflight", STATE["inflight"])` |
| replace | 495-495 | 530-531 | `srcs = [("phase2d", os.path.join(D2, "out", "sessions")), ("` |
| replace | 537-537 | 573-573 | `"Phase 2E: adopt %d finished prior Czech sessions (copied; p` |
| replace | 581-581 | 617-617 | `commit([LEDGER], "Phase 2E: GIVEUP %s (%s)" % (sid, why))` |
| insert | 633-632 | 669-669 | `_sl0 = time.time()` |
| insert | 634-633 | 671-671 | `record_sleep(_sl0, time.time())        # 2F change 1: exclud` |
| replace | 695-695 | 733-733 | `commit([sess_path(sid), LEDGER], "Phase 2E: session %s (%d t` |
| replace | 903-903 | 941-941 | `commit([xp, cp], "Phase 2E: upload format candidates from ba` |
| replace | 974-974 | 1012-1012 | `save_ledger(); commit([LOGP, LEDGER, DEFECTS], "Phase 2E: ba` |
| replace | 995-995 | 1033-1033 | `commit([ann_path, side, DEFECTS], "Phase 2E: annotations %s ` |
| replace | 1011-1011 | 1049-1049 | `"Phase 2E: batch %s %s + GATE 3" % (bid, "complete" if not m` |
| replace | 1039-1039 | 1077-1077 | `ck("backoff:at_most_5_retries_2E", MAX_RETRY == 5)` |
| insert | 1080-1079 | 1118-1152 | `# 2F change 1: the guard's clock excludes back-off sleep ent` |
| replace | 1219-1219 | 1292-1292 | `commit([LOGP, LEDGER, GATES, DEFECTS], "Phase 2E: run segmen` |

## Full diff
```diff
--- phase2e/run_2e_cz.py
+++ phase2f/run_2f_cz.py
@@ -54,4 +54,5 @@
 C2 = os.path.join(BASE, "phase2c")                             # INPUT, read only
 D2 = os.path.join(BASE, "phase2d")                             # INPUT, read only
+E2 = os.path.join(BASE, "phase2e")                             # INPUT, read only (2F adopts from here)
 B2 = os.path.join(BASE, "phase2b")
 for p in (C2, B2):
@@ -69,5 +70,7 @@
 LK_ADJUST_FLOOR = 5.0
 LK_NEEDS_DEDICATED_PASS = True   # change 6
-MAX_RETRY = 5                    # 2E change 2: ceiling raised 3 -> 5 (four give-ups cost four batches)
+MAX_RETRY = 3                    # 2F change 2: ceiling 5 -> 3 (2E defect 2).  With the SS1 batch rule a
+                                 # give-up costs 100 rows, so attempts 4 and 5 bought nothing and cost
+                                 # about 190,000 tokens across the two refused s04 chunks.
 CB_WALL_FLOOR_S = 900            # change 3
 CB_TOK_FLOOR = 200_000
@@ -75,8 +78,9 @@
 TP_WINDOW_S = 300                # change 4
 TP_MIN_TOK_S = 60.0
-TP_MIN_SAMPLES = 45              # 2E change 4: a full 5-step back-off ladder is 60+120+240+480+960 =
-                                 # ~31 min of legitimate waiting; a 20-min floor read that as a dead
-                                 # run and soft-stopped cz_0003..cz_0005. 45 min still catches 2C's
-                                 # throttling, which lasted hours.
+TP_MIN_SAMPLES = 20              # 2F change 1: the floor is back at 60 tok/s over 20 minutes because the
+                                 # guard's clock now EXCLUDES back-off sleep ENTIRELY (SLEEPS /
+                                 # sleep_overlap below).  2E raised this to 45 min to try to outlast one
+                                 # ladder and was soft-stopped anyway by two ladders in one run: the
+                                 # defect was measuring the sleep, not the length of the floor.
 LANGS = ("cz",)
 
@@ -112,8 +116,8 @@
 DRY = "_dry" if A["dry"] else ""
 STOPPFX = "STOPDRY" if A["dry"] else "STOP"
-LEDGER = os.path.join(H, "ledger_2e_cz%s.json" % DRY)
-GATES = os.path.join(H, "gates_2e_cz%s.json" % DRY)
-LOGP = os.path.join(H, "run_2e_cz%s.log" % DRY)
-DEFECTS = os.path.join(H, "DEFECTS_run_2e_cz%s.md" % DRY)
+LEDGER = os.path.join(H, "ledger_2f_cz%s.json" % DRY)
+GATES = os.path.join(H, "gates_2f_cz%s.json" % DRY)
+LOGP = os.path.join(H, "run_2f_cz%s.log" % DRY)
+DEFECTS = os.path.join(H, "DEFECTS_run_2f_cz%s.md" % DRY)
 
 LOG = open(LOGP, "a", buffering=1, encoding="utf-8")
@@ -157,5 +161,5 @@
     log("STOP", reason, detail)
     save_ledger()
-    commit([fn, LEDGER, GATES, LOGP], "Phase 2E: STOP %s" % reason)
+    commit([fn, LEDGER, GATES, LOGP], "Phase 2F: STOP %s" % reason)
     sys.exit(3)
 
@@ -168,5 +172,5 @@
     fn = write_stop_file(reason, detail)
     log("SOFT-STOP", reason, detail, "- no further sessions will be spawned; in-flight sessions may finish")
-    commit([fn, LOGP], "Phase 2E: soft stop %s" % reason)
+    commit([fn, LOGP], "Phase 2F: soft stop %s" % reason)
 
 # ---------------------------------------------------------------- prompts (2C text, reused verbatim)
@@ -405,9 +409,38 @@
     return wall, tok
 
+# ---------------------------------------------------------------- 2F change 1: the back-off sleep ledger
+# Every `counted:false` back-off sleep is recorded as an interval (t0, t1).  The throughput guard
+# subtracts the part of those intervals that falls inside its trailing window from elapsed seconds
+# BEFORE computing tok/s, so time spent asleep is not measured as throughput at all.  Intervals are
+# MERGED before summing: at PAR = 2 two sessions can sleep at once, and double counting could drive the
+# corrected clock negative.
+SLEEPS = []
+SLEEPLOCK = threading.Lock()
+def record_sleep(t0, t1):
+    if t1 > t0:
+        with SLEEPLOCK:
+            SLEEPS.append((t0, t1))
+def sleep_overlap(a, b):
+    """Seconds of recorded back-off sleep inside [a, b], overlapping intervals counted once."""
+    with SLEEPLOCK:
+        iv = sorted(SLEEPS)
+    tot, cur0, cur1 = 0.0, None, None
+    for s0, s1 in iv:
+        lo, hi = max(a, s0), min(b, s1)
+        if hi <= lo:
+            continue
+        if cur1 is None or lo > cur1:
+            if cur1 is not None: tot += cur1 - cur0
+            cur0, cur1 = lo, hi
+        else:
+            cur1 = max(cur1, hi)
+    if cur1 is not None: tot += cur1 - cur0
+    return tot
+
 # ---------------------------------------------------------------- change 4: throughput guard
 class ThroughputGuard(object):
     def __init__(self, window_s=TP_WINDOW_S, min_rate=TP_MIN_TOK_S, need=TP_MIN_SAMPLES):
         self.window_s, self.min_rate, self.need = window_s, min_rate, need
-        self.samples = collections.deque(); self.low = 0; self.reason = None; self.rate = None
+        self.samples = collections.deque(); self.low = 0; self.reason = None; self.rate = None; self.dt = None
     def sample(self, t, tok):
         self.samples.append((t, tok))
@@ -415,7 +448,8 @@
             self.samples.popleft()
         t0, k0 = self.samples[0]
-        dt = t - t0
-        if dt <= 0:
-            return None
+        dt = (t - t0) - sleep_overlap(t0, t)               # 2F change 1: sleep is not measured at all
+        self.dt = dt
+        if dt <= 0:                                        # window was entirely back-off sleep (or worse,
+            return self.reason                             # rounding); the guard CANNOT fire on it
         self.rate = (tok - k0) / dt
         self.low = self.low + 1 if self.rate < self.min_rate else 0
@@ -434,5 +468,6 @@
         r = GUARD.sample(time.time(), tok)
         log("THROUGHPUT", "rate %.1f tok/s" % (GUARD.rate or 0.0), "low_streak", GUARD.low, "cum_tok", tok,
-            "inflight", STATE["inflight"])
+            "inflight", STATE["inflight"], "measured_window_s %.0f" % (GUARD.dt if GUARD.dt is not None else -1),
+            "backoff_sleep_excluded:true")
         if r:
             soft_stop("throughput_guard", r + ".\n\n2C ran five hours at 25 tok/s because nothing checked; this run "
@@ -493,5 +528,6 @@
     does not parse, did not exit 0, or does not cover its whole chunk is NOT adopted: it is treated as
     MISSING and re-run.  That is how cz_0001_s07_v (exit 0, unparsable, 81,602 tok in 2E) comes back."""
-    srcs = [("phase2d", os.path.join(D2, "out", "sessions")), ("phase2c", os.path.join(C2, "out", "sessions"))]
+    srcs = [("phase2e", os.path.join(E2, "out", "sessions")), ("phase2d", os.path.join(D2, "out", "sessions")),
+            ("phase2c", os.path.join(C2, "out", "sessions"))]
     got, rejected, per_src, seen = [], [], collections.Counter(), set()
     for tag, src in srcs:
@@ -535,5 +571,5 @@
         log("ADOPT-REJECTED", len(rejected), "session file(s) NOT adoptable, will be re-run:", " | ".join(rejected))
     commit([LEDGER] + [sess_path(x) for x in got],
-           "Phase 2E: adopt %d finished prior Czech sessions (copied; phase2c/phase2e untouched)" % len(got))
+           "Phase 2F: adopt %d finished prior Czech sessions (copied; phase2c/phase2e untouched)" % len(got))
     return got
 
@@ -579,5 +615,5 @@
         save_ledger()
     log("GIVEUP", sid, kind, why, "tok", tok, "wall", round(wall, 1), "- moving on, the run never hangs")
-    commit([LEDGER], "Phase 2E: GIVEUP %s (%s)" % (sid, why))
+    commit([LEDGER], "Phase 2F: GIVEUP %s (%s)" % (sid, why))
 
 def session(sid, kind, prompt, rows):
@@ -631,5 +667,7 @@
                     log("RETRY", sid, kind, "attempt", attempt + 1, "of", MAX_RETRY, "reason", why,
                         "sleep %.1fs" % d, "counted:false")
+                    _sl0 = time.time()
                     time.sleep(d)
+                    record_sleep(_sl0, time.time())        # 2F change 1: excluded from the guard's clock
                     continue
                 record_giveup(sid, kind, "retries_exhausted after %d retries (%s)" % (MAX_RETRY, why),
@@ -693,5 +731,5 @@
             defect("%s burned %d tokens > ceiling %.0f (change 3): marked GIVEUP-TOKENS, never retried, excluded "
                    "from the running means; its rows are kept because they are already paid for" % (sid, tok, tok_cap))
-        commit([sess_path(sid), LEDGER], "Phase 2E: session %s (%d tok)" % (sid, tok))
+        commit([sess_path(sid), LEDGER], "Phase 2F: session %s (%d tok)" % (sid, tok))
         if out is None:
             return sid, ("FAIL", sid, "unparsable/exit %d" % p.returncode)
@@ -901,5 +939,5 @@
         for a in anns: w.writerow(csv_row(a))
     log("UPLOAD-FORMATS", os.path.basename(xp), os.path.getsize(xp), os.path.basename(cp), os.path.getsize(cp))
-    commit([xp, cp], "Phase 2E: upload format candidates from batch %s" % bid)
+    commit([xp, cp], "Phase 2F: upload format candidates from batch %s" % bid)
 
 # ---------------------------------------------------------------- batch driver
@@ -972,5 +1010,5 @@
     if not write_rows:
         log("EMPTY", bid, "no session of this batch is complete; nothing written")
-        save_ledger(); commit([LOGP, LEDGER, DEFECTS], "Phase 2E: batch %s has no complete session" % bid)
+        save_ledger(); commit([LOGP, LEDGER, DEFECTS], "Phase 2F: batch %s has no complete session" % bid)
         return "partial"
     anns = [assemble(r, drv[r["n"]], MV.get(r["n"]), RW.get(r["n"])) for r in write_rows]
@@ -993,5 +1031,5 @@
                "written": time.strftime("%Y-%m-%dT%H:%M:%S")},
               open(side, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
-    commit([ann_path, side, DEFECTS], "Phase 2E: annotations %s (%d of %d rows%s)"
+    commit([ann_path, side, DEFECTS], "Phase 2F: annotations %s (%d of %d rows%s)"
             % (bid, len(anns), len(rows), "" if not missing else ", PARTIAL"))
     g = gate3(bid, lang, anns)
@@ -1009,5 +1047,5 @@
     save_ledger()
     commit([GATES, done_marker if not missing else os.path.join(OUT, "PARTIAL_%s.json" % bid), LOGP, LEDGER, DEFECTS],
-           "Phase 2E: batch %s %s + GATE 3" % (bid, "complete" if not missing else "partial"))
+           "Phase 2F: batch %s %s + GATE 3" % (bid, "complete" if not missing else "partial"))
     for k in ("agv4", "reader_nom"):
         p = g[k]["ERROR_of_decided_pct"]
@@ -1037,5 +1075,5 @@
     ck("backoff:60/120/240_plus_jitter", all(60 * 2 ** i <= ds[i] < 60 * 2 ** i + 30 for i in range(MAX_RETRY)),
        "[%s]" % ", ".join("%.1f" % d for d in ds))
-    ck("backoff:at_most_5_retries_2E", MAX_RETRY == 5)
+    ck("backoff:at_most_3_retries_2F", MAX_RETRY == 3, "MAX_RETRY=%d" % MAX_RETRY)
     # change 3: circuit breaker
     STATE["kind"]["v"] = [0, 0, 0.0]
@@ -1078,4 +1116,39 @@
         g3.sample(t0 + 60 * i, tok)
     ck("guard:recovery_resets_streak", streak_before >= 13 and g3.low == 0, "%d -> %d" % (streak_before, g3.low))
+    # 2F change 1: the guard's clock excludes back-off sleep entirely
+    ck("guard:floor_restored_to_20_min_60_toks", TP_MIN_SAMPLES == 20 and TP_MIN_TOK_S == 60.0 and TP_WINDOW_S == 300)
+    del SLEEPS[:]
+    ck("sleep:no_intervals_no_subtraction", sleep_overlap(0.0, 100.0) == 0.0)
+    SLEEPS.extend([(10.0, 40.0), (20.0, 50.0)])                # two PAR=2 sessions asleep at once
+    ck("sleep:overlapping_intervals_merged_not_double_counted", sleep_overlap(0.0, 100.0) == 40.0,
+       "%.1f s" % sleep_overlap(0.0, 100.0))
+    ck("sleep:clipped_to_the_window", sleep_overlap(30.0, 45.0) == 15.0, "%.1f s" % sleep_overlap(30.0, 45.0))
+    del SLEEPS[:]
+    tz = 1000.0
+    g4 = ThroughputGuard(); SLEEPS.append((tz, tz + 60 * 40))   # a whole 40-minute ladder, 0 tokens
+    res4 = None
+    for i in range(1, 41):
+        res4 = g4.sample(tz + 60 * i, 0)
+    ck("guard:a_40_min_backoff_ladder_never_trips_it", res4 is None and g4.low == 0 and g4.dt == 0.0,
+       "low=%d corrected_window=%.0f s" % (g4.low, g4.dt if g4.dt is not None else -1))
+    del SLEEPS[:]
+    g5 = ThroughputGuard(); SLEEPS.append((tz, tz + 60 * 31))   # 2E's ladder, then REAL dead time
+    trip5 = None
+    for i in range(1, 32):
+        g5.sample(tz + 60 * i, 0)
+    ck("guard:streak_stays_0_while_asleep", g5.low == 0, "low=%d" % g5.low)
+    for i in range(32, 80):
+        if g5.sample(tz + 60 * i, 0):
+            trip5 = i; break
+    ck("guard:trips_20_measured_minutes_after_the_ladder", trip5 == 31 + TP_MIN_SAMPLES,
+       "tripped at minute %s (ladder ended at 31)" % trip5)
+    g6 = ThroughputGuard(); del SLEEPS[:]
+    SLEEPS.append((tz, tz + 60 * 31))
+    tok6 = 0
+    for i in range(1, 60):                                     # healthy 100 tok/s after the ladder
+        tok6 += 6000 if i > 31 else 0
+        r6 = g6.sample(tz + 60 * i, tok6)
+    ck("guard:healthy_after_a_ladder_never_trips", r6 is None and g6.low == 0, "low=%d" % g6.low)
+    del SLEEPS[:]
     # change 5: projection gate
     p = projection(rows_paid=700, rows_left=3364, tok=966_000, elapsed=7000.0)
@@ -1217,5 +1290,5 @@
                          % sorted(set(A["only"]) - MATCHED)); sys.exit(2)
     save_ledger()
-    commit([LOGP, LEDGER, GATES, DEFECTS], "Phase 2E: run segment finished (%d tokens cumulative)" % STATE["tok"])
+    commit([LOGP, LEDGER, GATES, DEFECTS], "Phase 2F: run segment finished (%d tokens cumulative)" % STATE["tok"])
     log("END", "tokens", STATE["tok"], "wall_s", round(time.time() - STATE["t0"], 1), "batches_done", done_batches,
         "retries", STATE["retries"], "giveups", len(STATE["giveups"]),
```

## 2F change 3 — the throughput guard cannot measure a window with no completion

`run_2f_cz.py`, `ThroughputGuard`: `__init__` 444 -> 444-445 (`self.unmeasurable`), `sample`'s streak
update 455 -> 463-474 (the guard now returns early when `tok - k0 <= 0` and `STATE["inflight"] > 0`),
`monitor_loop`'s THROUGHPUT log 470 -> 481-482 (`unmeasurable_windows`).  Self-tests added at
1195-1223: `guard:inflight_zero_delta_is_unmeasurable_never_fires` (40 minutes, tok frozen at 285,312,
one session out — no fire, streak 0), `guard:unmeasurable_does_not_reset_a_real_streak`,
`guard:2C_25_toks_with_returns_still_fires_at_20_min` (fires at exactly 20 low minutes),
`guard:change1_sleep_exclusion_intact_under_change3`.  Floor unchanged (60 tok/s, 20 min, 300 s window).

## 2F change 4 — the assembler accepts a contiguous half-chunk session

`run_2f_cz.py` 995-1001 -> 1009-1032: a missing whole chunk now tries `<sid>_h1` / `<sid>_h2` over the
chunk's two contiguous halves and keeps whatever they cover; the chunk still counts as missing so the
meta stays honest.  This recovers `cz_0002_s04_v_h1` (n 5365-5414, 50 rows, already paid for).

## run_part1.py

`finish()` 60-67 -> 60-81: deletes a stale `PART1_STOP.md` on a clean finish and relaunches Part 2's
driver (`nohup python3 p2_driver.py`) as the last step in every outcome.  Step 2 (refused chunks)
154-160 -> 168-175: both `cz_0002_s04_v` and `cz_0003_s04_v` are closed, `halves.py` is not run.
Step 3 176-180 -> 191-196: the run is confined to `cz_0004` and `cz_0005`.  Step 5 232-233 -> 248-259:
the lk comparison degrades to a written "no new rows" note instead of a `FileNotFoundError`.
