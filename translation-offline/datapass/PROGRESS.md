# Data pass progress (resume file)
- Part 1 (sk/cz grammar): DONE — 430 written, 8 reverted (gap moved), net 422; the 4 verifier-refused comma rows fixed in the resume run (part1/fix_clitic.py).
- Part 2 (punctuation): DONE — 142 rows written (backups/part2/part2_all.jsonl).
- Part 3 (translate 10,283 x 6): DONE — s001-s069 written (10,283 exercises; resume run 22.9 wrote s046-s069, 21,888 cells, 0 empty). 2 first-run cells empty (39286 hu, 40497 tr).
- Part 4 (explicit subject): DONE — es 629, ua 86, tr 266, hu 490 written (backups/part4/).
- Part 5 (import safeguard): DONE — and-again-content fd95c82.
Resume: re-run the step for the first slice whose state is not "written"; writer.run is idempotent (guards on old values).
