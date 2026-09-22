# Part 3 — translator brief: English grammar exercises -> de, ua, es, fr, tr, hu

You translate the English rows of one SLICE into six languages: `de ua es fr tr hu` (ua = Ukrainian). You write
output files only; you open no workbook, run no script, and touch no other file. These are the grammar exercises of
the 6.9.2026 batch whose six-language rows are blank; the sk and cz rows were translated by the project's pass and
are in your slice as a check of meaning and register.

## Read first
- This brief. Then your SLICE file in full.
- **A-level slices only (the task message says so):** the six rules files, in full, from
  `/Users/kristiansurhanak/Meine Ablage/And Again/Excels/Claude/6.9.2026-part1-translations/partsA/work/lang/rules/`
  `RULES_de.md RULES_ua.md RULES_es.md RULES_fr.md RULES_tr.md RULES_hu.md` — per exercise type 1–26, which form of
  the language renders each English form, with worked rows. They are binding, except any line telling you to write a
  category name or grammatical term in a cell: that line is stale and the cell is EMPTY (rule 3 below).
- B-level slices have no rules files; this brief is the whole rule set.

## The slice format
```
MEDIA <id> | word: … | meaning: <the sense of the word, binding> | irony: Yes/No
scene: <what the clip shows — context only>
E <exercise_id> | <level> type <n> <type name> | style <style> | options <2|3> [| SEL]
en|<intro_text with the gap ...>|<correct_answer>|<distractor_1>|<distractor_2>
sk|…   (Slovak row — meaning/register check only)
cz|…   (Czech row — meaning/register check only)
LOANWORD LOCK … (at the end, when present: one agreed rendering per language for those terms, in that sense)
```

## The rules (the project's translation pass, binding)
1. **The exercise is English; your row only lets a speaker of your language understand it.** The learner answers in
   English. Translate the WHOLE exercise as a unit: with your correct option in the gap, the sentence reads as a native
   speaker would say it. Translate the ENGLISH sentence — never translate from the scene, never add or drop a detail,
   never rebuild the exercise as a new situation. The MEDIA `meaning` decides which sense of an ambiguous word; the scene
   only decides which reading of an ambiguous sentence. `irony: Yes` = the row is meant to be funny; keep it funny.
2. **Options in position:** `correct_answer` translates the English correct_answer, `distractor_1` translates
   distractor_1, `distractor_2` translates distractor_2 — each as well as your grammar allows. Never swap, drop, merge
   an option; never substitute a contrast of your language for the English one; never fabricate a wrong form of your
   language (a malformed English form such as `runned`, `gooder`, `must to` takes the correct form of the intended
   word). **The answer is always the natural form. No brackets, no labels.** When two English options land on one word
   in your language, write that word in both cells — identical options are correct. A translated distractor that happens
   to make a correct sentence in your language is not a defect.
3. **THE EMPTY-CELL RULE (any word, not only articles).** Where an English option has no adequate equivalent in your
   language, the cell is EMPTY — never a category name, grammatical term, description or bracket:
   - articles: **ua** has none → all three cells empty; **tr** `a/an` → `bir`, `the` → empty; **de, fr, es, hu**
     translate the article forms;
   - auxiliary `do` / `does` / `did` when it is the whole option: empty in all six;
   - **tr**: the present copula `is/are/am` (a suffix) → empty; a preposition that is only a case ending → empty;
   - **hu**: the unwritten 3rd-person copula (predicate adjective/noun) → empty; location/existence still `van/vannak`;
   - **fr, es**: a bare `will` whose verb stays outside the gap → empty.
   A whole row may have all three cells empty; that is correct. When `options 2`, `distractor_2` is always empty.
4. **The gap** is exactly three dots `...`, exactly once in intro_text, at the place that corresponds to the English gap
   (your word order may move it inside the sentence; it must hold exactly what correct_answer holds). A sentence-final
   gap: intro_text ends on `...` and NOTHING after it (no full stop; `...?` and `...!` are allowed; French `... ?`,
   `... !`). correct_answer carries no trailing full stop. Every other intro_text ends with its final punctuation.
   Never four dots.
5. **Typography:** quotes de `„…“`, hu `„…”`, fr `« … »` (spaces inside, and a space before `? ! ; :`), es and ua `«…»`
   (no inner spaces), tr `“…”`. Spanish opens every question with `¿` and every exclamation with `¡` — a tag question
   is `…, ¿verdad?` with ONE `¿`. Correct diacritics always (ä ö ü ß; é è ê à ç; á é í ó ú ñ ü ¿ ¡; ç ğ ı İ ö ş ü;
   á é í ó ö ő ú ü ű). ua is Cyrillic only (a brand name may stay Latin), never Russian letters (ы э ъ ё).
6. **Structures the language lacks** (question tags, So do I / Neither do I, continuous or perfect aspects, future
   perfect, mixed conditionals, used to/would): keep the English sentence and write the closest natural wording of
   each option; identical options are fine.
7. **Register:** Gen Z (15–25), the same tone as the English row (`style` line: chill, gossip, flirt, dramatic, nerd,
   business, low iq…). Slang, flirt markers and idioms are NEVER translated word for word: use your language's own
   natural equivalent for the same audience, keeping the content, the correct answer and the grammar point. Established
   anglicisms stay (Mood, Glow Up, Chill). Never invent slang.
8. **Loanword lock:** the terms listed under LOANWORD LOCK use exactly that rendering when the English word has that sense.
9. **SEL exercises — explicit subject (es, ua, tr, hu only):** in a `SEL` exercise the es, ua, tr and hu sentence
   carries an explicit nominative subject pronoun where the language would normally drop it (es yo/tú/él/ella/usted/
   nosotros/nosotras/vosotros/vosotras/ellos/ellas/ustedes; ua я/ти/він/вона/воно/ми/ви/вони; tr ben/sen/o/biz/siz/
   onlar; hu én/te/ő/mi/ti/ők/ön/önök): one pronoun, in the main clause (else the first clause with a dropped subject),
   agreeing with the verb. The pronoun is in intro_text, never inside the gap and never in an option. Where the subject
   is already a noun or pronoun, add nothing. de and fr always have a subject anyway. Non-SEL exercises: write the
   natural sentence (subject pronoun only where the language uses one).
10. No `|` inside a field. No row identical to the English row, no two language rows byte-identical.

## Output — exactly this format, nothing else in the files
```
E <exercise_id>
de|<intro_text>|<correct_answer>|<distractor_1>|<distractor_2>
ua|…
es|…
fr|…
tr|…
hu|…
```
Language order exactly `de ua es fr tr hu`. Every E block of the slice, in slice order, each with all six lines.
Write the output in consecutive files named in your task message (`…_1.txt`, `…_2.txt`, …), **at most 50 E blocks per
file**, each file written once with one Write call. No headers, comments or blank lines.

When all files are written, reply with ONE line: the number of E blocks written, and any exercise where you had to guess
or where the English sentence itself looks wrong (ids only). Nothing else.
