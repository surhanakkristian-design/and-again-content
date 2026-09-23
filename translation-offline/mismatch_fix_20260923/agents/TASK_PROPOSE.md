# Task: propose fixes for confirmed source/reference mismatches (propose only, no database)

Context: in the And Again app a native speaker READS the native sentence and must translate it into English; the
English row is the reference answer and is NOT changed here. Gap-fill exercises show `intro_text` (the sentence with
`...` where the gap is) and the options correct_answer / distractor_1 / distractor_2. The full sentence is derived
mechanically: full = intro_text with `...` replaced by correct_answer (spaces collapsed, a final "." added if the intro
ends on the gap, first letter capitalised if the gap opens the sentence). So you only give intro_text and the options.

Your input file (given below) has blocks `@@ <key> <exercise_id> <lang> level-type: ...` with the English row, the
CURRENT native row, one or more ISSUE lines (what a two-pass review found and a suggested fix; the suggestion can be
imperfect, fix the real problem), and sometimes the other natives as context.

For every block decide the new native row:
- PATCH: change only what the issue needs (a word, a pronoun, a clause, a case, a tense). Everything else stays
  byte-identical to the CURRENT row (same wording, punctuation, interjections, explicit subject).
- RETRANSLATE: only when the native sentence says something entirely different from the English (e.g. the Hungarian A1
  series "the X is on the table" instead of "the X is thick and white"). Translate the English sentence again into
  that language, in the style of the current row and the other natives: same register (slang/interjection kept),
  same kind of gap (the gap covers the word that corresponds to the English gap word, same grammatical role), and
  keep an explicit subject pronoun if the current row has one.
- NOCHANGE: only if the current row already matches the English (say why in the note).
Rules:
- The new sentence must say what the English says: same person, number and gender where the language marks them,
  same time frame, same concrete nouns/verbs/places, no added or dropped clause (an interjection like "Bro"/"Tío" is fine).
- intro_text has exactly ONE `...`. correct_answer is the words that fill it, and the gap must still correspond to the
  English gap. Keep the current correct_answer unless the fix touches the gap itself. If an empty current
  correct_answer exists, keep it empty (then intro_text has `...` where nothing is inserted, as now).
- Distractors: keep the current ones unless the gap changed; if it changed, give two wrong options of the same kind
  (like the current ones / the English distractors), grammatical as words but wrong in this sentence, and never equal
  to the correct answer.
- Grammar must be native-correct (agreement of adjectives/participles with the corrected pronoun, e.g. es
  "ella está cansada", verb person with the new subject).
- Spanish pronoun items (keys P1-...): Spanish keeps the explicit subject pronoun; set it to the person/gender the
  English requires (él / ella / ellos / ellas / tú / yo / usted / nosotros ...) and adjust only what agreement needs.
  The "Ojalá yo ..." wish rows whose English is "He/She wishes he/she ...": rephrase the wish to the English person,
  e.g. "Él desearía haber empujado un poco más fuerte ..." with the gap on the verb form that corresponds to the
  English gap (e.g. gap "haber empujado", distractors of the same kind such as "empujar" / "empujaría"). Keep the rest
  of the sentence unchanged.
- Hungarian/Turkish do not mark gender; do not add gender. Slovak/Czech/Ukrainian mark gender in past tense and adjectives.

Output: write `<OUT>` as TSV with this header and one line per block, in input order:
`key<TAB>exercise_id<TAB>lang<TAB>mode<TAB>intro_text<TAB>correct_answer<TAB>distractor_1<TAB>distractor_2<TAB>note`
mode ∈ PATCH | RETRANSLATE | NOCHANGE. For NOCHANGE copy the current values. note = one short English line saying
what you changed. No tabs or newlines inside fields. Do not modify any other file, no network, no database.
Reply with one line only: `<n> blocks, <p> PATCH, <r> RETRANSLATE, <k> NOCHANGE`.

## Round 2 addendum
Round-2 blocks also show the EARLIER PROPOSAL and a REVIEWER OBJECTION. Produce a corrected proposal that fixes the
objection (typically a distractor that can also be read as correct: replace it with an option that is clearly wrong in
this sentence but of the same kind). If you think the objection is wrong, still make the row safe (a distractor must be
unambiguously wrong). If there is no objection, re-check the earlier proposal and keep or fix it.
