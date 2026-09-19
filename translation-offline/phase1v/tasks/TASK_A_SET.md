Track A, item A4 SET BUILD ONLY (no stack, no model checking calls). Dir: TO/phase1v/trackA_set.
Replicate exactly how the 1U fresh set was built (TO/phase1u/set/ and its briefs/scripts; the 1U report
appendix describes it): 100 new sentences, arm-B, 25 per level (A1/A2/B1/B2 as in 1U), sid 200001-200100,
no overlap with the 770 existing sentences (check text + normalized), 4 correct + 5 wrong answers per
sentence, blind writers ONE PER LEVEL (Read+Write only, no sight of the stack or of each other),
ONE blind judge for all packets, items shuffled across levels (new seed, record it), 80 hidden
duplicates, 4 packets. Writer and judge briefs = the 1U briefs adapted; ADD to the writer brief that
each writer must produce enough determiner-difference answers that are CORRECT (owner rule: determiner
free when the Slovak has no demonstrative), so the new floor can pass.
Spawning writers/judge: you cannot use the Agent tool. Use the claude CLI headless, e.g.
  claude -p "<brief path + instructions>" --model sonnet --allowedTools "Read,Write" 
  (run the 4 writers in parallel with & and wait; then the single judge over all 4 packets in one session).
Check `which claude` first. If the CLI is unavailable or fails, STOP after writing the briefs and return
"NEED_SPAWN" with the exact brief paths and output paths so the main session spawns them.
Floors on JUDGED counts (write floors_1v.json + FLOOR_CHECK_1V.json): agent drops judged wrong >=120
(fronted >=40, misaligned >=30); determiner-difference judged CORRECT >=60; missing-article judged wrong
>=40; time-frame >=100; by-passive correct >=60; SKP correct >=40. If a floor fails, you may commission
ONE top-up round of writers (then re-judge only the new items with the same judge brief); if still
failing, STOP and report — do not lower floors.
Pre-declare sensitivities S1..S6 as in 1U plus S7 = determiner-difference correct items rescored as wrong;
write SENSITIVITIES_1V.json; each must be unable to move 0 items (top-up rule as 1U).
Do NOT run the stack on the set. Do not read TO/phase1v/trackA_loop. Deliver set/ ready for the run agent.
