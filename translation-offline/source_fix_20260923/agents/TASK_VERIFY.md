# Task: independently verify 5 proposed native source-sentence fixes (And Again language app)

Folder: /Users/kristiansurhanak/Projects/and-again-content/translation-offline/source_fix_20260923.
Read `work/items.json` (the broken rows, the English rows, the problem) and `work/proposals.json` (someone else's fix).
You are an independent native-level reviewer of Turkish and Hungarian. Do NOT trust the proposal.

For each proposal decide AGREE or DISAGREE. AGREE only if ALL hold:
1. it is grammatical and natural for a native speaker, in the English row's register;
2. it means what the English says (same subject, tense, question/statement, number, the same content words);
3. the gap covers the native counterpart of the English gap word's role; exactly one `...` in intro_text;
   correct_answer non-empty; distractors are wrong, plausible, same word class, distinct;
4. full_sentence == intro_text with `...` replaced by correct_answer (spacing exact), ending with the English mark;
5. it fixes the stated problem and keeps any explicit subject pronoun.
If you DISAGREE, give the reason and your own corrected row.

Write `work/verdicts.json`: list of {exercise_id, lang, verdict: "AGREE"|"DISAGREE", reason, alternative (row or null)}.
Do not touch any database.
