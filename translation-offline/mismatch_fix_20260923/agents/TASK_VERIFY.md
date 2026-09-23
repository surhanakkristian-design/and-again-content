# Task: independently verify proposed fixes (read-only, no database)

Context: in the And Again app a native speaker READS the native sentence and must translate it into English; the
English row is the reference answer. Someone else proposed a new native row for each item because a review found a
mismatch with the English. You judge each proposal on your own.

Input blocks: `@@ <key> <exercise_id> <lang> ...` with the English row, the OLD native row, the ISSUE that was found,
the PROPOSED NEW native row (full sentence, gap = correct_answer, distractors, mode, proposer note), and sometimes the
other natives as context. English items (lang en) show the OLD and NEW English row plus all natives; judge whether
the new English now says what the natives say and still works as a gap-fill (and as a chunk build where chunks are shown).

Answer AGREE only if ALL hold:
1. The new sentence says what the English says: same person/number/gender where the language marks them, same time
   frame, same concrete nouns/verbs/places, no added or dropped content clause (an interjection is fine). A reader
   translating it would arrive at the English reference.
2. It is grammatical and natural for a native speaker (agreement with a corrected pronoun included).
3. The gap (correct_answer) is still the word(s) that correspond to the English gap and appear in the sentence;
   the distractors are wrong in this sentence and differ from the correct answer.
4. Mode PATCH changed nothing beyond what the issue needed (compare OLD and NEW). Spanish P1 items keep an explicit
   subject pronoun; only the pronoun (and agreement it forces, or the rephrased "Ojalá" wish) may change.
   Mode RETRANSLATE is acceptable when the old row said something entirely different.
   Mode NOCHANGE: agree only if the OLD row already matches the English.
Otherwise DISAGREE and say exactly what is wrong (and the fix you would make).

Write `<OUT>` as TSV: header `key<TAB>verdict<TAB>reason`, one line per item, verdict = AGREE | DISAGREE. No tabs
inside fields. Do not modify any other file, no network, no database. Reply with one line: `<n> items, <a> AGREE`.
