# Task: final source/reference check of the changed exercises (read-only, no database)

Context: in the And Again app a native speaker READS the native sentence and must translate it into English; the
English sentence is the reference answer. In gap exercises the native gap must correspond to the English gap.
Some rows of these exercises were just corrected. You check them again with fresh eyes.

Input: blocks `### <exercise_id> <level>` with the English row (`en:`) and the 8 native rows (de, ua, es, fr, tr, hu,
sk, cz); each row = full sentence + [gap: …]. Rows marked `*` were changed today (the English row too, where marked).
Judge EVERY row marked `*` (and, for an exercise whose English is marked `*`, every native row) against the English.
Flag ONLY a REAL mismatch that would make the exercise unanswerable or misleading:
- a different concrete noun, verb or place;
- a different number, person or gender that the language marks (a language that does not mark it is fine);
- a different time frame (a tense the language lacks, rendered by its normal equivalent, is fine);
- a missing or added clause (a dropped/added interjection like "Wow"/"Bro" is fine);
- the gap word not matching (different word/meaning, or not present in the sentence). An EMPTY native gap and a
  structural gap difference (English article, many/much, do-support, auxiliary, copula, relative pronoun that the
  language has no word for) are NOT mismatches;
- a native sentence that is ungrammatical so that its meaning changes.
NOT mismatches: wording, register, word order, idiom, natural paraphrase, synonyms, articles, punctuation.
When unsure, do not flag.

Write `<OUT>` as TSV: header `exercise_id<TAB>lang<TAB>category<TAB>what_differs<TAB>proposed_fix`, one line per flagged
row, nothing else. category ∈ noun_verb_place | number_person_gender | time_frame | clause | gap | grammar.
No tabs inside fields. Do not modify any other file, no network, no database.
Reply with one line: `<n> exercises, <r> rows judged, <m> flagged`.
