# Task: propose fixes for 5 broken native source sentences (And Again language app)

Read `work/items.json` (relative to /Users/kristiansurhanak/Projects/and-again-content/translation-offline/source_fix_20260923).
Each item is one gapped exercise row: `intro_text` holds exactly one gap marker `...`; `correct_answer` fills it;
`full_sentence` = intro_text with the gap replaced by correct_answer (a sentence-final mark is appended only if the
intro ends at the gap). Learners are natives of that language learning English; the native row is the source they
translate / the gloss of the English sentence.

For each item write a corrected native row that:
- says what the English row says, naturally, as a native speaker would (register of the English: casual stays casual);
- keeps the GAP WORD ROLE: the gap covers the native word/phrase that corresponds to the English gap word's function
  (e.g. English gap "at" in "ends ... sunset" → the Turkish locative time phrase; English "Can" → the ability verb form);
- keeps any explicit subject pronoun already present (e.g. tr "Sen");
- has exactly ONE `...` in intro_text, a non-empty correct_answer, and two plausible WRONG distractors of the same
  word class (distinct from the answer and from each other);
- ends with the same sentence-final mark as the English sentence;
- changes as little as needed.

Write `work/proposals.json`: a list of {exercise_id, lang, intro_text, correct_answer, distractor_1, distractor_2,
full_sentence, rationale (one line)}. Nothing else; do not touch any database.
