Task: write listening questions, part 3.
Folder: ~/Projects/and-again-content/new_exercises_20260923/r2/lq/
1. Read GEN_RULES.md in that folder — the full standard. Do not read any other output files.
2. Read gen_input_3.json (JSON array of videos).
3. Work through EVERY video yourself: read its speech and what_is_seen, decide how many fair NEW audio-only questions it carries
   (0..max_new, never repeating existing_questions), and write them. Scripts only to assemble/validate JSON, never to write questions.
4. Write gen_output_3.json: JSON array, same order and length as the input, each
   {"media_id", "questions": [{"question","correct_answer","accepted_answers"}], "skip", "reason"}.
5. Validate: same media_ids in order; len(questions) <= max_new; 2-5 accepted_answers each, none equal to correct_answer
   (case-insensitive); the question text does not contain the correct_answer; skip=true iff questions is empty (with a reason).
Reply with one line: videos, questions written, videos skipped.
