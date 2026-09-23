# Task: independent re-check of candidate mismatches (read-only)

You get `recheck/rNN.txt`. Each item is `@@ <item_no> <exercise_id> <lang>` followed by the English row (`en:`), the
native row under review (`<lang>:`) and, for context, the other native rows. Each row = full sentence + `[gap: …]`
(the correct_answer cut out of the sentence).

A native speaker READS the native sentence and must translate it into English; the English sentence is the reference.
Decide for each item, on your own, whether the native row under review has a REAL mismatch with the English that
would make the exercise unanswerable or misleading:
- a different concrete noun, verb or place (en "milkshakes" vs ua «коктейлі» = cocktails);
- a different number, person or gender that the language marks (a language that does not mark it is fine);
- a different time frame (a tense the language lacks, rendered by its normal equivalent, is fine);
- a missing or added clause (a dropped/added interjection like "Wow"/"Bro" is fine);
- the gap word not matching (different word/meaning, or not present in the native sentence).
An EMPTY native gap (`[gap: ]`) by itself is NOT counted here (those rows are listed separately); judge only
whether the native SENTENCE says something different from the English, or whether a non-empty native gap is a
different word. A native sentence that is broken so that its meaning differs (e.g. a verb left in the infinitive so
the tense/person is lost) IS a mismatch.
A STRUCTURAL gap difference is NOT a mismatch: when the English gap is a grammar word the native language has no
word for (article a/an/the, quantifier many/much, do-support, an auxiliary such as is/has/will/is going to, copula,
relative pronoun), a different or empty native gap is expected. Answer NO for those.
If the row under review is `en`, judge whether the English row differs from what the natives consistently say.
NOT mismatches: wording, register, word order, idiom, natural paraphrase, synonyms, a hypernym/hyponym a learner would
still render the same way, articles, punctuation. When unsure, answer NO.

Write `recheck/rNN.out.tsv` with header `item_no<TAB>exercise_id<TAB>lang<TAB>verdict<TAB>category<TAB>what_differs<TAB>proposed_fix`,
one line per item. verdict = YES (real mismatch) or NO. For NO leave category/what_differs/proposed_fix as `-`.
category ∈ noun_verb_place | number_person_gender | time_frame | clause | gap. proposed_fix = which side to change and
how (e.g. `change ua: коктейлі → молочні коктейлі`). No tabs inside fields. Do not modify any other file, no network,
no database. Reply with one line: `rNN: <n items>, <y> YES`.
