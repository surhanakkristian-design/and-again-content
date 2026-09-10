# Claude Code — A-level part, full translation pass (English + 8 languages)

Driven by `run_part.sh`:

    PROMPT_FILE=./PROMPT_A_translations.md CONCEPTS_PER_PASS=40 \
    caffeinate -dimsu bash ./scripts/run_part.sh "UGC - Claude x Higgsfield_A-level_partN.xlsx" \
      2>&1 | tee -a logs/overnight.log

---

Use the skill `ugc-vocab-sheet-fill-level-ab`. Read its SKILL.md first — Step 3 (English content),
Step 4 (the language pass), the loanword rule and the validator gates are binding.

## Token discipline

- The workbook is **never loaded into the conversation.** Open it only with `openpyxl` inside a
  script, one concept at a time. Never `cat` it, never print a sheet, never dump rows "to check".
- Use `translation_status.py` for progress — its output is a few lines.
- Report counts, not contents. If you must inspect, print at most the 9 rows of one exercise.

## Scope

Target: the A-level part workbook named in the opening message.

**This is A level (CEFR A1/A2) — a different exercise contract from B:**

- **video → exactly 27 exercises**, in this `exercise_type_id` order:
  `1…11` (11 × A1) + `12…26` (15 × A2) + `27` Label the video.
- **image → exactly 1 exercise**: `27` Label the video.
- **There is no "Meaning of the word" at A level.** Type 69 is B-only; never emit it here,
  and never emit anything above 27.
- Every A video gets all 26 grammar types regardless of whether its word feels A1 or A2.

The three parts: part1 395 concepts (ids 978–1372), part2 393 (1373–1765), part3 416
(1766–2181). Nothing is written yet: `word_localizations` is empty, every `en` row is empty.

**This pass writes all 9 languages** — English first, then the other eight. Order per concept:
1. `word_localizations` — all 9 rows.
2. For each exercise: the `en` row, then `sk, de, cz, fr, es, ua, tr, hu`.

Never touch: `All Words`, `media`, `media_categories`, `word_concepts`, `concept_media`,
`exercises`, or any id column. Never renumber anything.

Start with:
```bash
python3 scripts/translation_status.py "./UGC - Claude x Higgsfield_new_template_part2.xlsx"
```
and resume from the first unfinished concept. Never from the top.

## HARD LIMITS — these failed part 1 and had to be reworked. Get them right the first time.

**1. English length budget** (Instructions sheet). In the `en` row ONLY:
- `intro_text` ≤ **90** characters
- `correct_answer` / `distractor_1` / `distractor_2` ≤ **50** characters each

The other 8 languages have **no limit** — they are shown briefly as a translation aid, so natural
phrasing beats squeezing under a count. Never truncate or abbreviate a translation to hit a number.

Write English short from the start; do not write a full sentence and then trim it. If an option
runs long, the content has leaked out of the sentence into the answer — move it back into
`intro_text` and leave only the tested contrast in the options. `validate_part.py` fails on `E13`.

**2. Typography, per language** — apply while writing, do not rely on a later fix:

| | quotes | notes |
|---|---|---|
| sk cz de | `„ … “` | |
| hu | `„ … ”` | |
| fr | `« … »` | space inside both marks, and a space before `? ! ; :` |
| es ua | `« … »` | no inner spaces |
| en tr | `“ … ”` | |

Spanish opens every question with `¿` and every exclamation with `¡`.
The gap marker is exactly three dots `...` — never four.

**3. Translate the sentence; never invent a new scene.** Where English uses a structure the target
language lacks (`So do I` / `Neither do I`, question tags, continuous aspect in de/hu), keep the
English SENTENCE and test the closest native device. Rebuilding it as a different situation — for
example turning a statement into a two-turn dialogue so the tag fits — is a defect even when the
result reads well.

## Writing the English row

- **intro_text** — the sentence with the gap marked `...`. Empty on type 68.
- **correct_answer / distractor_1 / distractor_2** — exactly one option is truly correct;
  distractors are plausible level-typical learner errors, never defensible alternatives.
- **Video alignment is the crucial rule:** every sentence lives inside THAT media item's world —
  its subject, setting, props, plot and mood, from the All Words `Explanation of the video`.
  Never a generic shop/window/box sentence.
- B1 rows stay B1; B2 rows may use the advanced structures. One sentence where possible, two max.
  Gen Z (15–25) contexts, irony welcome where the clip earns it.
- **Type 27 Label the video** — `intro_text` empty in every language; options are short phrases
  naming what the media shows (`to open a door`), plus two same-shape wrong phrases. This is the
  only vocabulary type at A level, and it is the ONLY exercise a still image gets, so it has to
  carry the word on its own: the correct phrase must be unmistakably what the asset shows, and the
  two wrong phrases must be plausible but clearly not it.
- **Keep the English at A1/A2.** Short sentences, everyday words, present tenses unless the type
  demands otherwise. A B1 sentence with an A1 gap is still a defect. The `EXAMPLE - A level` tab in
  the template shows the intended register for all 27 types — read one row of the same type before
  writing, and match its shape, not its content.
- Audit as an English teacher before moving on: correct, natural, idiomatic, genuinely testing its
  topic, and within budget.

## Writing the 8 translations

- **A `language_code` row is ENTIRELY in that language.** No English left over, no half-translated
  cell, no copy of the `en` row.
- Translate the **whole exercise as a unit**: the gapped sentence and its options must still work
  together, and the correct option must remain the only correct one in that language.
- **Distractors — strict hierarchy:**
  1. **Mirror the error.** Reproduce the equivalent mistake in the target language (EN `2 cats.` /
     `2 cat.` → SK `2 mačky.` / `2 mačka.`). The distractor is *supposed* to be wrong.
  2. **Bracket gloss, max 3 words** — only when the contrast has no equivalent and two options
     would otherwise be identical.
  3. **Never fabricate** a fake form. Translate the sense plainly and flag the id.
- **Loanwords:** food and cultural terms use ONE agreed rendering per language, identical in
  `word_localizations` and in every exercise of that concept. `./loanwords.json` is the lock file —
  read it before you start, append to it before using a new term.
- **No two language rows of one exercise may be byte-identical.** If sk and cz genuinely coincide
  on a short loanword answer, keep it and list it in the report.
- Register: Gen Z, same tone as the `en` row. Established anglicisms stay untranslated (Mood, Glow
  Up, Chill, Nerd Mode).
- `options_count` is fixed at 3: `distractor_2` filled in all 9 languages.

## Style carries over by translation — with one named exception (Kristian, 10 September 2026)

The rule, verbatim:

> The humour comes from the content, not from the sentence structure, so for most styles a
> normal translation carries the style over intact. The exceptions are slang, flirt, and idioms
> wherever they appear: those must not be translated literally. There the translator finds the
> target language's own equivalent, keeping the content, the correct answer and the grammar
> point identical.

What this means in practice:

- **Default: translate.** Whatever voice the `en` row has — a dry ironic comment, a telenovela
  line, a corporate memo, an empty-headed "because" — translate it as a sentence. The joke is in
  what is said about the clip; a faithful translation keeps it. Do not "localise" the sentence,
  do not rebuild the scene, do not add markers the English row does not have. This pass is
  translation, not localisation (SPEC_AMENDMENTS §6).
- **The exception is decided per sentence, not per style.** Three things must never be rendered
  word for word: **slang** (reduced forms, Gen Z lexis, address words such as *bro, no cap,
  kinda*), **flirt** (compliment markers such as *not gonna lie, low-key, smooth*), and **an
  idiom wherever it appears**, under any of the nine styles — *the end of the world, over the
  top, no notes, love that for him, kind of a situation*. For these, find the target language's
  own way of saying the same thing to the same audience, and keep three things identical: the
  content (what is being said about the clip), the correct answer, and the grammar point of the
  gap. If the target language has no equivalent, say it plainly in that language and list the
  id in the report; never invent slang, never translate an idiom literally.
- **How to spot an idiom:** read the English sentence literally, in your head, as a picture. If
  the literal picture is wrong for the clip (nobody's world is ending, nothing is on top of
  anything, there are no notes), the phrase is an idiom and takes the exception. A second test:
  if you had to explain the phrase to a learner, would you explain the words or the meaning?
  Meaning → idiom. The `en` row's style (a `# style:` line where present) is a hint, not the
  rule — a chill sentence can carry an idiom and a slang sentence can be idiom-free.
- **This sits beside `loanwords.json`, not on top of it.** That file locks the WORD-level
  renderings of food and cultural terms (one agreed word per language, identical in
  `word_localizations` and every exercise; the validator warns on drift, W2). This section is
  about PHRASE-level figurative language. A loanword inside a slang sentence still follows the
  lock file; a slang phrase around a loanword follows this section. Nothing here changes the
  loanword rule, and nothing here needs adding to that file.

## Rhythm

- Work **concept by concept in `concept_id` order**; inside a concept, exercise by exercise, all 9
  languages at once. Never sweep one language across the file.
- **Save the workbook after every concept.**
- Every 25 concepts run:
  ```bash
  python3 scripts/validate_part.py "./UGC - Claude x Higgsfield_new_template_part2.xlsx" --loanwords ./loanwords.json
  ```
  Fix what it names before continuing. `E13` (length) must stay at zero — if it appears, you are
  writing English too long and the next concepts must be tighter.

## Block mode

If the opening message says "do the next N concepts", do exactly that, then run the validator,
report briefly and stop. The workbook is the progress record; the next session resumes from it.

## Finish condition — then STOP

```bash
python3 scripts/validate_part.py "./UGC - Claude x Higgsfield_new_template_part2.xlsx" --loanwords ./loanwords.json
python3 scripts/rework_list.py   "./UGC - Claude x Higgsfield_new_template_part2.xlsx" --gate
```
The first exits 0, the second prints `GATE: DONE`, and `translation_status.py` shows 5761/5761.
Then **stop and wait for my confirmation.**

## Final report — short

- concepts and exercises written, validator result, each warning judged in one line;
- loanwords appended to `loanwords.json`;
- exercises where the English point has no target-language equivalent and how you solved it;
- any concept where the 90/50 budget cost something real;
- anything you had to guess.
