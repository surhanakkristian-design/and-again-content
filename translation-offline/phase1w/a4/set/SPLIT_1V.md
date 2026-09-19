# Phase 1V — SPLIT, SIDs, floors and pre-declared sensitivities
**Declared 19 Sept 2026, BEFORE any 1V sentence exists.** Same build as 1U (phase1u/set/SPLIT_1U.md), changes marked NEW.

- 4 blind writers, one per level (A1/A2/B1/B2), 29 sentences each; assembler keeps 25 per level: 8 FR + 6 MC + 6 MN + 5 SKP.
- Public ids 1V001-1V100, **sid 200001-200100** (A1 001-025, A2 026-050, B1 051-075, B2 076-100). 9 answers each -> 900 items.
- Arm-B Slovak (explicit subject pronouns). No overlap with the 770 existing sentences (exact normalised text + Jaccard, assemble_1v.earlier_slovak()).
- Odd sid -> P1, even -> P2; pooled headline; Fisher P1 vs P2; exact Clopper-Pearson; targets on point AND interval.
- ONE blind judge (judge/JUDGE_BRIEF_1V.md) for all packets; shuffled across levels, **NEW seed 20260923** (1U used 20260920); 80 hidden duplicate controls (20 per level); 4 packets (build_packets_1v.py, N<=5 if token budget forces).
- Floors on JUDGED counts before the run (FLOORS_DECLARED_1V.json): F1 agent drops wrong >=120 (F1a fronted >=40, F1b misaligned >=30), F2 time-frame wrong >=100, F3 by-passive correct >=60, F4 SKP correct >=40, F5 missing-article wrong >=40, **NEW F6 determiner-difference judged CORRECT >=60**.
  By construction: 20 FR/MC/MN x 4 levels = 80 determiner c2 + >=12 SKP c4 -> ~92 written (F6 headroom ~35 %).
- Sensitivities S1-S6 exactly as 1U, **NEW S7** = determiner-difference correct items rescored as wrong (SENSITIVITIES_1V.json).
- One top-up writer round allowed if a floor fails; still failing -> STOP, floors never lowered.
