# Phase 1g — builder state (18 Sept 2026)

## Done
- `run_phase1g.py` (+ `lib_prev.py`, a verbatim copy of phase1e/run_phase1e.py; no previous-phase runner is
  imported, all writes go to phase1g/). Selftest PASSES.
- Row 0 (Phase 1f all four x P-B) reproduces 1f exactly: 214/235, FA raw 15, FA real 6, 193/21.
- F5, F4v2 and the F2 tip boundary implemented and measured; 9 ablation rows, lenient + strict false
  acceptance with exact Clopper-Pearson intervals, sample-size computation.
- 0 new model calls: all 2 x 198 needed verdicts were reused byte-identically from the phase1e/phase1f
  ledgers. `calls.jsonl` is therefore empty (no new call was made), `call_counts.json` records new/reused/
  failed/cap.
- Outputs in phase1g/: results_<ts>.json/.md (the LATEST timestamp is authoritative), decisions.jsonl,
  f5_cost_235.json, f4v2_verification.json, f2_boundary_disputed.json, remaining_errors.json,
  sample_size.json, call_counts.json, run_<ts>.log (three runs: two pre-fix, the last one authoritative).

## Fixed during the run (apparatus first)
1. F4v2 read the noun `škola` as a feminine l-participle -> l-participles are now only read when the
   sentence carries a past/conditional marker.
2. `si` was read as the 2sg past auxiliary although it is the reflexive/dative clitic -> no person is
   derived from `si` any more.
3. `vyťahovaním` (instrumental verbal noun) was read as a 1sg `-m` form -> `-ním/-tím` excluded.
4. English `it`/`you` object pronouns were treated as subjects -> the guard abstains when ANY pronoun of
   the answer fits the Slovak.

## Left for the next agents
- Judgement pass: `remaining_errors.json` has `"judgement": "TO BE ADDED BY THE NEXT AGENT"` on every
  remaining false acceptance and false rejection of rows 7 and 8.
- The report (not written here, by instruction).

## Exact next command
    cd /Users/kristiansurhanak/Projects/and-again-content/translation-offline
    python3 phase1g/run_phase1g.py --selftest && python3 phase1g/run_phase1g.py --tabulate
(re-runnable offline; it never calls the model when the ledgers already hold the verdicts)
