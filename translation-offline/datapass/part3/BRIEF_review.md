# Part 3 — independent reviewer brief (de, ua, es, fr, tr, hu)

Another translator translated English grammar exercises into `de ua es fr tr hu` (ua = Ukrainian). You review EVERY
row of your review file on your own, as a native-level reviewer of all six languages, and correct the rows that are
wrong. You write ONE output file and touch nothing else. Run no scripts.

## The review file
```
MEDIA <id> | meaning: <sense of the headword>
E <exercise_id> | <level> type <n> <type name> | style <style> | options <2|3> [| SEL]
en|<intro_text with the gap ...>|<correct_answer>|<distractor_1>|<distractor_2>
de|…
  !HARD: <machine failure — this row CANNOT be written as it is; you must correct it or empty it>
  ~soft: <machine warning — look at it; it may be fine>
ua|… es|… fr|… tr|… hu|…
```

## What the rows must be (the project's rules — judge against these, not your taste)
- The exercise is English; the row only lets a speaker understand it. The row translates the English sentence (same
  meaning, same details, nothing added or dropped) and, with correct_answer in the gap, reads as natural native speech.
- **Options in position**: correct_answer translates the English correct_answer, distractor_1 translates distractor_1,
  distractor_2 translates distractor_2. **Identical options are CORRECT** (two English forms landing on one word). A
  distractor that happens to be correct in the language is NOT a defect. **An EMPTY option cell is CORRECT** where the
  English option has no equivalent word: articles in ua (all empty) and `the` in tr (`a/an` = `bir`), do/does/did as a
  whole option (all six), tr present copula / case-ending prepositions, hu unwritten 3rd-person copula, fr/es bare
  `will`. de, fr, es, hu translate articles. `options 2` -> distractor_2 empty.
- The gap `...` appears exactly once, and holds exactly what correct_answer holds (the sentence with correct_answer
  inserted must be grammatical and must not repeat or lose a word). A sentence-final gap ends intro_text on `...` with
  nothing after it (`...?`, `...!`, fr `... ?` allowed); otherwise intro_text ends with its final punctuation.
- Grammar, agreement, case, diacritics, spelling correct. Typography: de `„…“`, hu `„…”`, fr `« … »` + space before
  `? ! ; :`, es/ua `«…»`, tr `“…”`; Spanish `¿…?` `¡…!` (a tag question `…, ¿verdad?` has ONE `¿`). ua is Ukrainian
  (never Russian words or letters ы э ъ ё).
- Register: same Gen-Z tone as the English; slang/idioms rendered by a natural equivalent, never word for word.
- **SEL** exercises: the es, ua, tr and hu intro_text carries ONE explicit nominative subject pronoun where the language
  would drop the subject (not needed when the subject is a noun/pronoun already); the pronoun is never inside the gap or
  an option, and it agrees with the verb. de/fr need nothing extra.

## What to correct
A row is wrong when it: mistranslates or changes the meaning; is ungrammatical or misspelled; puts the gap in the wrong
place or makes the filled sentence wrong; swaps/drops/fabricates an option; writes a label/category name/bracket in a
cell; breaks typography; misses the SEL pronoun; or carries a !HARD flag. **Do NOT correct style preferences**, a
freer-but-correct wording, identical options, or empty option cells that the rules require.

## Output — only the rows you correct, nothing else in the file
```
<exercise_id>|<lang>|<intro_text>|<correct_answer>|<distractor_1>|<distractor_2>|<short reason in English>
```
All four fields given in full (empty fields stay empty between the pipes). If a row is wrong and you cannot make it
right, write `<exercise_id>|<lang>|EMPTY|<reason>` instead. If nothing needs correcting, write the single line `NONE`.
When done, reply with ONE line: the number of rows corrected and the number emptied.
