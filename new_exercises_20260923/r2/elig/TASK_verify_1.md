Task: independent eligibility verifier, part 1.
Folder: ~/Projects/and-again-content/new_exercises_20260923/r2/elig/
1. Read RULE.md in that folder — it is the full standard. Do NOT read any other judge/verify output files in the folder.
2. Read verify_input_1.json (a JSON array of {id, sentences}).
3. Judge EVERY item yourself by reading it (no keyword scripts deciding for you; you may use a script only to assemble/validate the JSON).
4. Write verify_output_1.json: a JSON array, same order and same length as the input, each {"id", "full", "sentence"}.
5. Validate: same ids in the same order, every "full" boolean, "sentence" copied exactly from the item's sentences when full=true, null otherwise.
Reply with one line: the item count and how many are full=true.
