# CHANGES_2G - Phase 2G Part B (finish Czech annotation)

All code is a COPY of phase2f/ (read only), produced by `make_2g.py` with asserted replacements. No checker rule, no prompt text and no gate bar changed.

## B1 - throughput guard REMOVED ENTIRELY (removed code lines below)

Kept: token cap with in-flight accounting (cap 2,900,000 for all Part B headless sessions: annotation `--cap 2900000`, lk `--cap 2900000 - annotation spend`; the reservation `spent + inflight x 95,000 + estimate` is checked before every launch), the per-session circuit breaker (wall floor 900 s, token floor 200,000, 3x running mean), and the projection gate (4 h wall, cap tokens) - the projection is now session-based (see below).

## run_2g_cz.py

* docstring marks the copy
* BASE = translation-offline from phase2g/partB
* F2 = phase2f (input, read only)
* B1: throughput-guard constants REMOVED

  Removed / replaced code:

```python
TP_WINDOW_S = 300                # change 4
TP_MIN_TOK_S = 60.0
TP_MIN_SAMPLES = 20              # 2F change 1: the floor is back at 60 tok/s over 20 minutes because the
                                 # guard's clock now EXCLUDES back-off sleep ENTIRELY (SLEEPS /
                                 # sleep_overlap below).  2E raised this to 45 min to try to outlast one
                                 # ladder and was soft-stopped anyway by two ladders in one run: the
                                 # defect was measuring the sleep, not the length of the floor.
```

* B2 constants: PIECE_ROWS 10, PIECE_MAX_RETRY 2, PIECED ranges, EST['vp']
* --no-spawn (assemble-only, 0 model calls) for the post-usage-stop pass
* --no-spawn parsed
* file name "ledger_2f_cz%s.json" -> "ledger_2g_cz%s.json"
* file name "gates_2f_cz%s.json" -> "gates_2g_cz%s.json"
* file name "run_2f_cz%s.log" -> "run_2g_cz%s.log"
* DEFECTS renamed; TIMELINE / PIECES_JSON / REFUSED_MD / PROGRESS paths
* stop() writes the piece log before exiting
* stop-file header
* commit messages say Phase 2G Part B
* B1: ledger no longer records guard settings

  Removed / replaced code:

```python
         "throughput_guard": {"window_s": TP_WINDOW_S, "min_tok_per_s": TP_MIN_TOK_S, "min_minutes": TP_MIN_SAMPLES},
```

* B1: ThroughputGuard class, GUARD and monitor_loop REMOVED

  Removed / replaced code:

```python
# ---------------------------------------------------------------- change 4: throughput guard
class ThroughputGuard(object):
    def __init__(self, window_s=TP_WINDOW_S, min_rate=TP_MIN_TOK_S, need=TP_MIN_SAMPLES):
        self.window_s, self.min_rate, self.need = window_s, min_rate, need
        self.samples = collections.deque(); self.low = 0; self.reason = None; self.rate = None; self.dt = None
        self.unmeasurable = 0                              # 2F change 3: windows with no completion in flight
    def sample(self, t, tok):
        self.samples.append((t, tok))
        while len(self.samples) > 1 and t - self.samples[0][0] > self.window_s:
            self.samples.popleft()
        t0, k0 = self.samples[0]
        dt = (t - t0) - sleep_overlap(t0, t)               # 2F change 1: sleep is not measured at all
        self.dt = dt
        if dt <= 0:                                        # window was entirely back-off sleep (or worse,
            return self.reason                             # rounding); the guard CANNOT fire on it
        self.rate = (tok - k0) / dt
        # 2F change 3: a window with NO session completion while work is IN FLIGHT is UNMEASURABLE.
        # STATE["tok"] only moves when a session RETURNS, so one long-running session reads as 0.0 tok/s
        # while the pool is in fact working - that is what soft-stopped 2F Part 1 at 00:13:25 with
        # cz_0003_s04_v still out.  A pool that is genuinely STUCK is the CIRCUIT BREAKER's job
        # (per-session wall and token floors, 3x the running mean).  This guard exists to catch a pool
        # that IS returning work far too slowly - 2C's five hours at 25 tok/s - and that case still
        # fires, because there tok rises.  Do not increment the streak, do not reset it, do not fire.
        if (tok - k0) <= 0 and STATE["inflight"] > 0:
            self.unmeasurable += 1
            return self.reason
        self.low = self.low + 1 if self.rate < self.min_rate else 0
        if self.low >= self.need and not self.reason:
            self.reason = ("measured throughput %.1f tok/s stayed under %.0f tok/s for %d consecutive minutes "
                           "(trailing %d s window)" % (self.rate, self.min_rate, self.low, self.window_s))
        return self.reason
GUARD = ThroughputGuard()
def monitor_loop():
    while not STATE.get("finished"):
        time.sleep(60)
        if STATE.get("finished"):
            return
        with LOCK:
            tok = STATE["tok"]
        r = GUARD.sample(time.time(), tok)
        log("THROUGHPUT", "rate %.1f tok/s" % (GUARD.rate or 0.0), "low_streak", GUARD.low, "cum_tok", tok,
            "inflight", STATE["inflight"], "measured_window_s %.0f" % (GUARD.dt if GUARD.dt is not None else -1),
            "unmeasurable_windows", GUARD.unmeasurable,
            "backoff_sleep_excluded:true")
        if r:
            soft_stop("throughput_guard", r + ".\n\n2C ran five hours at 25 tok/s because nothing checked; this run "
                                              "stops spawning instead. In-flight sessions finish or hit the circuit "
                                              "breaker, everything complete is committed, resume with the same command.")
            return
```

* B1: guard self-tests REMOVED (they also exercised the 2F sleep ledger, which stays but no longer feeds anything)

  Removed / replaced code:

```python
    # change 4: throughput guard
    g = ThroughputGuard()
    t0, res, trip_at = 1000.0, None, None
    for i in range(1, 40):                                     # minutes at 0 tok/s
        res = g.sample(t0 + 60 * i, 0)
        if res:
            trip_at = i; break
    ck("guard:trips_at_20_low_minutes",
       res is not None and g.low == TP_MIN_SAMPLES and trip_at == TP_MIN_SAMPLES + 1,
       "low=%d, tripped at minute %s (sample 1 has no trailing window yet)" % (g.low, trip_at))
    g2 = ThroughputGuard()
    tok = 0
    for i in range(1, 60):                                     # 100 tok/s forever
        tok += 6000
        ck2 = g2.sample(t0 + 60 * i, tok)
    ck("guard:healthy_run_never_trips", ck2 is None and g2.low == 0, "rate=%.1f tok/s" % (g2.rate or 0))
    g3 = ThroughputGuard()
    tok = 0
    for i in range(1, 15):
        g3.sample(t0 + 60 * i, tok)
    streak_before = g3.low
    for i in range(15, 25):
        tok += 6000
        g3.sample(t0 + 60 * i, tok)
    ck("guard:recovery_resets_streak", streak_before >= 13 and g3.low == 0, "%d -> %d" % (streak_before, g3.low))
    # 2F change 1: the guard's clock excludes back-off sleep entirely
    ck("guard:floor_restored_to_20_min_60_toks", TP_MIN_SAMPLES == 20 and TP_MIN_TOK_S == 60.0 and TP_WINDOW_S == 300)
    del SLEEPS[:]
    ck("sleep:no_intervals_no_subtraction", sleep_overlap(0.0, 100.0) == 0.0)
    SLEEPS.extend([(10.0, 40.0), (20.0, 50.0)])                # two PAR=2 sessions asleep at once
    ck("sleep:overlapping_intervals_merged_not_double_counted", sleep_overlap(0.0, 100.0) == 40.0,
       "%.1f s" % sleep_overlap(0.0, 100.0))
    ck("sleep:clipped_to_the_window", sleep_overlap(30.0, 45.0) == 15.0, "%.1f s" % sleep_overlap(30.0, 45.0))
    del SLEEPS[:]
    tz = 1000.0
    g4 = ThroughputGuard(); SLEEPS.append((tz, tz + 60 * 40))   # a whole 40-minute ladder, 0 tokens
    res4 = None
    for i in range(1, 41):
        res4 = g4.sample(tz + 60 * i, 0)
    ck("guard:a_40_min_backoff_ladder_never_trips_it", res4 is None and g4.low == 0 and g4.dt == 0.0,
       "low=%d corrected_window=%.0f s" % (g4.low, g4.dt if g4.dt is not None else -1))
    del SLEEPS[:]
    g5 = ThroughputGuard(); SLEEPS.append((tz, tz + 60 * 31))   # 2E's ladder, then REAL dead time
    trip5 = None
    for i in range(1, 32):
        g5.sample(tz + 60 * i, 0)
    ck("guard:streak_stays_0_while_asleep", g5.low == 0, "low=%d" % g5.low)
    for i in range(32, 80):
        if g5.sample(tz + 60 * i, 0):
            trip5 = i; break
    ck("guard:trips_20_measured_minutes_after_the_ladder", trip5 == 31 + TP_MIN_SAMPLES,
       "tripped at minute %s (ladder ended at 31)" % trip5)
    g6 = ThroughputGuard(); del SLEEPS[:]
    SLEEPS.append((tz, tz + 60 * 31))
    tok6 = 0
    for i in range(1, 60):                                     # healthy 100 tok/s after the ladder
        tok6 += 6000 if i > 31 else 0
        r6 = g6.sample(tz + 60 * i, tok6)
    ck("guard:healthy_after_a_ladder_never_trips", r6 is None and g6.low == 0, "low=%d" % g6.low)
    del SLEEPS[:]
    # 2F change 3: an UNMEASURABLE window (no completion while work is in flight) neither counts nor fires
    del SLEEPS[:]
    g7 = ThroughputGuard(); STATE["inflight"] = 1
    res7 = None
    for i in range(1, 41):                                     # 40 minutes, one session still out, tok frozen
        res7 = g7.sample(tz + 60 * i, 285312)
    ck("guard:inflight_zero_delta_is_unmeasurable_never_fires",
       res7 is None and g7.low == 0 and g7.unmeasurable >= 39,
       "low=%d unmeasurable=%d (the 2F Part 1 stop at 00:13:25)" % (g7.low, g7.unmeasurable))
    g7b = ThroughputGuard()                                    # ... and it does not RESET a real streak either
    for i in range(1, 11):
        STATE["inflight"] = 0; g7b.sample(tz + 60 * i, 0)      # 10 genuinely idle minutes, nothing in flight
    pre = g7b.low
    STATE["inflight"] = 1
    for i in range(11, 21):
        g7b.sample(tz + 60 * i, 0)
    ck("guard:unmeasurable_does_not_reset_a_real_streak", pre == 9 and g7b.low == 9,
       "%d -> %d" % (pre, g7b.low))
    g8 = ThroughputGuard(); STATE["inflight"] = 2              # 2C: 25 tok/s WITH sessions returning
    tok8, trip8 = 0, None
    for i in range(1, 60):
        tok8 += 1500                                           # 25 tok/s * 60 s
        if g8.sample(tz + 60 * i, tok8):
            trip8 = i; break
    ck("guard:2C_25_toks_with_returns_still_fires_at_20_min",
       trip8 == TP_MIN_SAMPLES + 1 and g8.low == TP_MIN_SAMPLES,
       "tripped at minute %s, rate %.1f tok/s" % (trip8, g8.rate or 0))
    g9 = ThroughputGuard(); SLEEPS.append((tz, tz + 60 * 31))  # change 1 still behaves, now with inflight > 0
    for i in range(1, 32):
        g9.sample(tz + 60 * i, 0)
    ck("guard:change1_sleep_exclusion_intact_under_change3", g9.low == 0 and g9.dt == 0.0,
       "low=%d corrected_window=%.0f s" % (g9.low, g9.dt if g9.dt is not None else -1))
    del SLEEPS[:]; STATE["inflight"] = 0
```

* B1: monitor thread start REMOVED

  Removed / replaced code:

```python
    if not A["dry"]:
        threading.Thread(target=monitor_loop, daemon=True).start()
```

* --no-spawn: never loads the token, never spawns
* --no-spawn still assembles every batch
* progress.log line after every batch
* piece log at the end of every run
* projection gate KEPT, but session-based: remaining sessions x running per-kind mean (pieces have their own kind, so 10-row overhead does not inflate the per-row extrapolation)

  Removed / replaced code:

```python
            p = projection(STATE["rows_paid"], _vr, STATE["tok"], time.time() - STATE["t0"])
```

* rw sessions are inside projection_2g now

  Removed / replaced code:

```python
                p["projected_total_tokens"] += _rwn * EST["rw"]
```

* adopt (COPY) finished sessions from phase2f first
* adopt 2F half-chunk sessions (cz_0002_s04_v_h1)
* B2/B3/stop helpers; pieces get their own stats kind 'vp'
* reservation estimate per stats kind
* B3: cap refusal logged
* B3: launch record (time, index, concurrency)
* B2: pieces MAX_RETRY 2
* circuit breaker per stats kind (floors unchanged)
* B3 http-error log + usage-limit / first-session hard stop
* retry ceiling per session type
* retry log
* give-up text
* token breaker per stats kind
* running means per stats kind
* B3: end record
* B3: give-up record
* B2: s04 v chunks replaced by their 10-row pieces
* B4: 2F half-chunk assembler extended to 10-row pieces
* a chunk fully recovered from halves/pieces is not 'missing'
* GATE 3 stops only live runs (dry / assemble-only record it)
* no per-batch upload candidates
* 2G self-tests
* F2_ROWS = the 2,850 rows 2F already gated
* GATE 3 (2F code unchanged, bar 12 %) scores 50 random rows of the rows NEW in this batch; the whole re-assembled batch is scored as <bid>_all_rows_DIAGNOSTIC and never gates (the dry run showed the resampled cz_0002 at 14.58 % over rows 2E/2F had already gated and passed)

  Removed / replaced code:

```python
    g = gate3(bid, lang, anns)
```


## run_2g_lk.py

* BASE from partB
* lk input/output dir = partB/lk
* file name "ledger_2f_lk.json" -> "ledger_2g_lk.json"
* file name "run_2f_lk.log" -> "run_2g_lk.log"
* file name "defects_2f_lk.txt" -> "defects_2g_lk.txt"
* input-hash baseline = phase2g/SHA_inputs_before.txt
* commit messages
* sample helper
* GATE sample tolerates < 250 rows
* B5: prompt sha16 asserted at import
* timeline + usage-limit helpers
* B3: lk launch record
* B3 + usage-limit check after every lk CLI call

## build_upload_2g.py

* BASE from partB
* README = 2F's README + 2G addendum, written to partB/
* addendum header
* commit message

## B5 - chain logic: a STOP file blocks only the stage that wrote it

2F's `run_part1.py` downgraded the lk pass to `--merge-only` whenever ANY `STOP_*.md` existed (D-2F-10, D-2F-12). Removed logic:

```python
    stops = [f for f in os.listdir(H) if f.startswith("STOP_") and f.endswith(".md")]
    over = spend() > TRIPWIRE

    # ------------------------------------------------ 4. dedicated lk pass over the NEW rows only
    lk_rc = None
    if stops or over:
        log("LK-SKIPPED", "stop files", stops, "over_tripwire", over, "-> merge-only, no new tokens")
        adopt_lk()
        lk_rc = run([sys.executable, "run_2f_lk.py", "--merge-only"], "run_2f_lk")
    else:
        adopt_lk()
        lk_rc = run([sys.executable, "run_2f_lk.py", "--cap", str(max(0, TRIPWIRE - spend()))], "run_2f_lk")
```

`chain_2g.sh` runs the paid lk pass after annotation regardless of any annotation-stage STOP file (token_cap, projection_*, gate3_*). The only exception is the brief's critical stop rule: after `STOP_usage_limit.md` or `STOP_first_session_failed.md` no further headless Claude session is started anywhere; B6 (0 Claude sessions) still runs and DONE is written.

## Deviations to note

* Finished 2F sessions (cz_0004 s01-s03, s05-s08 v+rw, cz_0002_s04_v_h1, everything of cz_0001-0003) are ADOPTED by COPY at 0 tokens instead of re-run; only missing sessions are paid for.
* Projection gate kept, formula changed to remaining sessions x running per-kind mean (pieces are their own kind `vp`); the 2F per-row extrapolation would have extrapolated 10-row-piece overhead onto full chunks.
* GATE 3 gates only rows new in 2G (50 random of them per batch); the full re-assembled batch is a never-gating diagnostic.
* Gemini: Part B makes 0 Gemini calls (GATE 3 and lk use no Gemini).

