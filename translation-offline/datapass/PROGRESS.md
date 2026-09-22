# Data pass progress (resume file)
- Part 1 (sk/cz grammar): DONE — 426 fixes written (backups/part1/part1_all.jsonl), 4 rejected by the verifier.
- Part 2 (punctuation): DONE — 142 rows written (backups/part2/part2_all.jsonl).
- Part 3 (translate 10,283 x 6): STOPPED at budget — s001-s045 written (6,635 exercises); resume at s046 (part3/state.json, done.sh).
- Part 4 (explicit subject): DONE — es 629, ua 86, tr 266, hu 490 written (backups/part4/).
- Part 5 (import safeguard): DONE — and-again-content fd95c82.
Resume: re-run the step for the first slice whose state is not "written"; writer.run is idempotent (guards on old values).
