# Data pass progress (resume file)
- Part 1 (sk/cz grammar): DONE — 426 fixes written (backups/part1/part1_all.jsonl), 4 rejected by the verifier.
- Part 2 (punctuation): DONE — 142 rows written (backups/part2/part2_all.jsonl).
- Part 3 (translate 10,283 x 6): per-slice state in part3/state.json (slice -> translated / reviewed / written).
- Part 4 (explicit subject es/ua/tr/hu on the 2,049): not started.
- Part 5 (import safeguard): not started.
Resume: re-run the step for the first slice whose state is not "written"; writer.run is idempotent (guards on old values).
