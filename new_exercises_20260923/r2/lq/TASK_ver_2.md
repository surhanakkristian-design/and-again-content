Task: independent verifier for listening questions, part 2.
Folder: ~/Projects/and-again-content/new_exercises_20260923/r2/lq/
1. Read VERIFY_RULES.md and GEN_RULES.md in that folder. Do NOT read gen_output_* or any other output file.
2. Read ver_input_2.json (JSON array; each item is ONE proposed question with its video context and a "key").
3. Check EVERY item yourself against A-E; be strict on A (answerable with sound off from what_is_seen, the situation or
   world knowledge = REJECT) and on E. Scripts only to assemble/validate JSON, never to decide.
4. Write ver_output_2.json: JSON array, same order and length, each {"key","verdict","reason","drop_variants"}.
5. Validate keys/order; drop_variants must be exact strings from that item's accepted_answers.
Reply with one line: items, AGREE count, REJECT count.
