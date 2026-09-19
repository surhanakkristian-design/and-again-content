# Phase 2B plan (printed and committed before any work) — measurement only
Budget 800,000 harness tokens (headless runner hard cap 420,000; sub-agents ~380,000). Gemini calls 0. DB SELECT only.
Main session <= 16 tool calls, each agent <= 12. Earlier phase dirs (phase1*, phase2a) read-only; all output in phase2b/.

1. DATA agent (0 sessions): define + run the 7,200 selection rule (3,600 concepts x 2: A -> one A1 + one A2, B -> one B1 + one B2;
   topic chosen by lowest md5(concept_id||exercise_id||'phase2b'), ties by exercise_id), relate it to 39,498 (1W Track B SQL)
   and to "5,895". Draw 200 (100 sk, 100 cz; 25 per level each) from the selection, deterministically
   (md5(exercise_id||'phase2b-sample')), excluding every test-set id and every phase2a id. Pull: source sentence, en reference,
   en/sk/cz correct_answer, exercise_type title/level, alt-group mapping from the existing synonym-group table.
2. DERIVE agent (0 sessions): frozen reader_nom (variant full) + existing guards -> voice, agent_nom, person, number, gender,
   tense_open, perfective_present where a deterministic source exists; arm-B rewrite as a SCRIPT (pronoun from reader
   person/number/gender), abstain list for the model; g4_v2/g4_v3 AND the frozen stack's own AG v4 voice path on the same 200.
3. RUN + SCORE agent (headless, bundled claude 2.1.275 --model opus, token via zsh -ic, never printed):
   blind gold (source only, 2 sessions x 100), lk judge (1 session), v-only cost with all other fields supplied
   (4 sessions x 50), model rewrite fallback for reader abstains only (1 session). ~8 sessions, ~360k tokens.
   Score every field vs the blind gold, exact 95 % Clopper-Pearson.
4. REPORT agent: docs/features/reports/TRANSLATION_PRODUCTION_PHASE2B_REPORT.md (per-field table first) + extrapolations
   for 14,400 / 20,400 / 57,600.
Stop rule: if headless spawning fails, STOP at 0 cost and quote the error. If cumulative tokens would pass 800k, STOP.
Build nothing for production, annotate no batch, change no checker rule; defects are recorded, not fixed.
