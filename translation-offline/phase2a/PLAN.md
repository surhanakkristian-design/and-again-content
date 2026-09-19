# Phase 2A plan (printed and committed before any session)
- Input: selection.json (commit 91a14d6): 1,000 ids, A1 253 / A2 344 / B1 226 / B2 177, gold 100 (25/34/23/18).
  SCOPE DEFECT: the live in-scope query (1W Track B SQL) returns 39,498 sentences, not 5,895; the 5,895 figure is not defined
  in any 1V/1W file (1V assumed equal quarters). Proportions are taken from the 39,498 population. Recorded, not resolved.
- Pipeline: phase1w/trackB/run_s5.py prompts VERBATIM (sha REWRITE fa61a15bc34ed6b3, ANNOT 46c5fe84210419ad, GOLD 524b89b7aa4caebd),
  bundled claude 2.1.275, --model opus, N = 30, 4 parallel. Checker/guards/prompts/rules untouched (frozen stack_1w + reader_nom full).
- Stage 1: 34 rewrite sessions (1,000) + 4 blind-gold sessions (100, Slovak only).  Stage 2: 4 annotation sessions (the 100 gold rows).
- §4.2 gate on the 100, before (raw SK, blind gold) and after (rewritten SK, gold_after): g1, g2, g3_v2, g3_v3, g4_v2, g4_v3 with
  reader_nom full installed + reader_nom direct. Any gated ERROR > 10 % => STOP, stage 3 not run. 1V first-word reader reported, not gated.
- Stage 3 (PASS only): 30 annotation sessions (900).  Total 72 sessions.
- Budget: projected 34x37k + 34x40.5k + 4x33k = ~2.77M harness tokens; runner hard cap 2,850,000 (pre-launch check, 45k/session),
  150k reserved for sub-agents; phase cap 3,000,000. Every session file committed on arrival. 0 Gemini calls, 0 DB access.
- Known gap: the 1W annotation prompt has no `p`/`g` chain fields; they are not added (that would change the measured pipeline).
