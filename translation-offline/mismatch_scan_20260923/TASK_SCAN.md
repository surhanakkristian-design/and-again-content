# Task: source/reference mismatch scan (read-only, report only)

You get ONE slice file: `slices/sNN.txt` (about 150 exercises). Each exercise block is
`### <exercise_id> <level>`, then the English row (`en:`) and 8 native rows (de, ua, es, fr, tr, hu, sk, cz).
Each row is the full sentence plus `[gap: …]` = the correct_answer (the word(s) cut out of the sentence);
sometimes `[intro: …]` = the sentence as shown with the gap.

In the app a native speaker READS the native sentence and must translate it into English; the English sentence is
the reference answer. In gap exercises the gap word in the native row must correspond to the English gap.

For every exercise, compare EACH native row with the English row and flag ONLY real mismatches that would make the
exercise unanswerable or misleading:
- a different concrete noun, verb or place (e.g. en "milkshakes" vs ua «коктейлі» = cocktails; ua would need «молочні коктейлі»);
- a different number, person or gender that the language marks (en "he" vs es "ella"; singular vs plural noun;
  "we" vs "they"). Languages that do not mark it (dropped pronoun, genderless tr/hu pronoun) are NOT mismatches;
- a different time frame (past vs future, "yesterday" vs "tomorrow"; a tense the language lacks rendered by its
  normal equivalent is NOT a mismatch, e.g. Slavic perfective future for English future perfect);
- a missing or added clause (a whole piece of content dropped or added; a dropped/added interjection like
  "Wow"/"Bro" is NOT a mismatch);
- the gap word not matching (the native gap is a different word/meaning than the English gap, or the gap is not in
  the native sentence at all).

NOT mismatches: wording differences, register, word order, idiom, natural paraphrase, synonyms, a reasonable
hypernym/hyponym that a learner would still render the same way, article/determiner choices, punctuation.
When unsure, DO NOT flag. Expect most exercises to be clean.

Output: write `flags/sNN.tsv` (same NN) with a header line and one line per flagged (exercise, language):
`exercise_id<TAB>lang<TAB>category<TAB>what_differs<TAB>proposed_fix`
- category ∈ noun_verb_place | number_person_gender | time_frame | clause | gap
- what_differs: short, quote both words (e.g. `en "milkshakes" vs ua «коктейлі» (cocktails)`)
- proposed_fix: which side to change and how, e.g. `change ua: коктейлі → молочні коктейлі` or `change en: …` (change
  en only when the English is the odd one out against most natives).
No tabs inside fields. If nothing is flagged, write only the header. Do not modify any other file, do not use the
network, do not run any database command. Reply with one line: `sNN: <n exercises> scanned, <m> flags`.
