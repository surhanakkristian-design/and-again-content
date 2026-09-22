# Claude Code — part 1 of batch 6.9.2026, translation pass (eight languages; the English is done)

Status, 11 September 2026: **translations only.** The English rows of this part are written,
verified and accepted (reports REPORT_2026-09-10_11 and _13). This pass writes no English sentence.

How it is driven: by the caller, batch by batch. Each translator subagent writes a sidecar file,
the batch is gated with `check_lang.py` and `scripts/apply_lang.py --check`, and the caller applies
it with `scripts/apply_lang.py`. Not by `run_part.sh`, whose loop depends on `translation_status.py`,
a script that is not present on this machine.

---

Use the skill `ugc-vocab-sheet-fill-level-ab`. Read its SKILL.md first — Step 3 (English content),
Step 4 (the language pass), the loanword rule and the validator gates are binding.

## Token discipline

- The workbook is **never loaded into the conversation.** Open it only with `openpyxl` inside a
  script, one concept at a time. Never `cat` it, never print a sheet, never dump rows "to check".
- Use `translation_status.py` for progress — its output is a few lines.
- Report counts, not contents. If you must inspect, print at most the 9 rows of one exercise.

## Scope

Target: `Excels/Claude/6.9.2026-part1-translations/partsA/6.9.2026_A_part1.xlsx` — A level,
**237 concepts, one per media; 237 media (211 videos, 26 images); 5,723 exercises.** Parts 2 and 3
of batch 6.9.2026 are separate workbooks and are not in this pass.

**This is A level (CEFR A1/A2):** a video has exactly 27 exercises, types 1…26 then 27 Label the
video; an image has exactly 1, type 27. No type 69 and nothing above 27 at A level.

**Already written — read it, never edit it:**
- every `en` row of `sentence_translations`, all 5,723. It is the source you translate from. The
  section "Writing the English row" below does not apply to this pass.
- `All Words`, `media`, `media_categories`, `word_concepts`, `concept_media`, `exercises`, and every
  id column. Never renumber anything.

**What this pass writes:**
1. `sentence_translations`, the eight non-English rows of every exercise — `sk, de, cz, fr, es, ua,
   tr, hu` — 5,723 × 8 = **45,784 rows**, all empty today. Only `intro_text`, `correct_answer`,
   `distractor_1` and `distractor_2`; `full_sentence`, `chunks` and `correct_alternative` stay empty.
2. `word_localizations`, all nine rows of every concept, **the English row included** — 237 × 9 =
   **2,133 rows**, all empty today.

Simple Explanations (type 74) are not in this pass: they are not yet scaffolded into this workbook.

**Your SOURCE file is produced by `scripts/dump_lang_source.py`** — that script owns the MEDIA / W / E
block format, and it is what regenerates your input if a batch has to be re-run. Do not hand-edit a
SOURCE file and do not reformat one.

**The gate order, and it is not interchangeable:** run `check_lang.py` over the **combined** batch —
all eight languages at once — and then `apply_lang.py` over **each four-language half separately**.
Handing `check_lang.py` one half gives `missing ['fr','es','tr','hu']`, and handing `apply_lang.py`
the two halves concatenated gives `block E 28132 given twice`; both are the wrong-shaped input, not a
defect in the batch.

**Sections below that describe the old driver and do not apply here:** the `translation_status.py`
line under Token discipline; "Writing the English row"; "Rhythm", because the caller writes the
workbook and you never save it; "Block mode"; and "Finish condition", because `rework_list.py` is not
present either. Everything else — the hard limits, typography, "Translate the sentence; never invent
a new scene", the translation rules, the option hierarchy of section 10 of the spec, loanwords, and
the style section — is binding.

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
English SENTENCE and translate its options per section 10 of the spec: the closest native wording.
Never test a native device of your own in its place. Rebuilding it as a different situation — for
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

## The MEDIA block, and what each field is for (15 September 2026)

Every word in your SOURCE file opens with a block describing the clip that word came from. It is
there once per word, not once per exercise. Read it before the word's first exercise and keep it in
mind for all of them.

- **`meaning of the word`** — the definition. It decides **which sense** of the English word this
  word's exercises are about, and it is **binding**. `bank` is the sloping land beside a river or a
  financial institution, `cold` is the absence of heat or the infection; the definition says which,
  and your translation must be that sense in every one of the word's exercises.
- **`explanation of the video`**, **`props`**, **`actions`** — the scene. They decide **which
  reading** of an ambiguous English sentence is the right one. They are **context only**. "The tongs
  are out" with `props: metal tongs; round table grill` is a hand holding tongs at a grill, not tongs
  left outdoors. "He opened a difficult book" with `props: heavy leather-bound law books` is a law
  book.
- **`irony: Yes`** — the row is **meant to be funny**. Keep it funny. A translation that is accurate
  and flat has lost the thing the row exists for. `irony: No` means play it straight.
- `All Words word (as displayed)`, `category` and `voiceover` are background. Use them if they help;
  nothing depends on them.

**NEVER TRANSLATE FROM THE SCENE.** The row you translate is the **English sentence**, and only the
English sentence. The scene chooses between readings of it; it never adds a detail, never removes
one, and never corrects the English. If the scene and the English sentence disagree, translate the
English sentence as written and say so in your report — do not quietly fix it.

## Writing the 8 translations

- **The exercise is English; your row translates it.** Ruling of 11 September 2026, recorded as
  section 10 of `/Users/kristian/Meine Ablage/And Again/Claude Krasty/1.Step - Exercises/EXERCISE_AUTHORING_SPEC.md`
  — **read section 10 in full; it is binding and wins over anything in this prompt.** English is the
  learning language; sk, de, cz, fr, es, ua, tr and hu only translate. The learner chooses among the
  English options and reads your row to understand the exercise. Nobody learns your language from it,
  so your row never has to work as an exercise in your language.
- **A `language_code` row is ENTIRELY in that language.** No English left over, no half-translated
  cell, no copy of the `en` row.
- Translate the **whole exercise as a unit**: with the translated correct option in the gap, the
  sentence reads as a native speaker would say it.
- **Options — the hierarchy (section 10):**
  1. **Translate each option in its position**, as well as your language's grammar allows: the
     `correct_answer` translates the English `correct_answer`, `distractor_1` translates `distractor_1`,
     `distractor_2` translates `distractor_2` (EN `2 cats.` / `2 cat.` → SK `2 mačky.` / `2 mačka.`).
     A translated distractor that happens to make a correct sentence in your language is not a defect.
  2. **The answer is the natural form, always** (brief §0a). **There are no brackets and no labels.**
     When two English options collapse onto one word in your language, keep the word and write it in
     both cells: `musieť` / `musieť` for *must* against *have to*, `jeho` / `jeho` for *his* against
     *its*. Identical options are the accepted outcome, not an error — the learner answers in English
     and reads your row only to understand the sentence. **Articles** (§0e): translate the article
     where your language has one; leave the cell **empty** where it does not — sk, cz and ua leave all
     three empty, tr writes `bir` for *a*/*an* and leaves the definite cell empty, de, fr, es and hu
     translate the forms. Never a bracket, never a category name, never a parenthetical.
  3. **Never rebuild the exercise and never fabricate a form.** No grammatical contrast of your language
     in place of the English one; no option dropped, merged or swapped because your language lacks the
     category; no invented wrong form of your language.
- **Loanwords:** food and cultural terms use ONE agreed rendering per language, identical in
  `word_localizations` and in every exercise of that concept. `./loanwords.json` is the lock file —
  read it before you start, append to it before using a new term.
- **No two language rows of one exercise may be byte-identical.** If sk and cz genuinely coincide
  on a short loanword answer, keep it and list it in the report.
- Register: Gen Z, same tone as the `en` row. Established anglicisms stay untranslated (Mood, Glow
  Up, Chill, Nerd Mode).
- `options_count` is **3 for most types and 2 for types 13, 15 and 18** (ruling of 15 September 2026,
  brief §0h.3). Where it is 2, `distractor_2` is empty in all nine languages and you write nothing
  there. Where it is 3, fill `distractor_2` — unless §0e leaves that cell empty.

## Per-language rules files — binding

Each language has a rules file, one block per exercise type 1–26:
`Excels/Claude/6.9.2026-part1-translations/partsA/work/lang/rules/RULES_<lang>.md`
for `sk, cz, de, hu, fr, es, ua, tr`. **Read the file for every language you translate, in full.**

Each file says, per type, which form of your language renders each English form — tense, aspect, case,
gender, number, word order, typography — with worked rows.

Earlier versions of these files are kept in `rules/v1_cancelled_by_ruling0_11sep/` and
`rules/v2_as_measured_11sep/` for the record only; never use them.

## Sentence-final gaps (11 September 2026)

When the gap ends the sentence, `intro_text` ends on the three dots, `...`, and on nothing else.

- **No full stop after it.** `....` is a four-dot gap; both checkers refuse it.
- **No `... .`** with a space, and **no words added after the gap** to make room for a stop. Adding
  words changes the sentence.
- The import appends the final full stop itself when it builds `full_sentence`: step 4 of the
  recorded convention, `interleave` in `validate_part.py`, adds `.` where the intro ends on `...` and
  the sentence does not already end in `.`, `?` or `!`.
- A question mark or an exclamation mark may follow the gap directly: `...?`, `...!`; in French, with
  its space, `... ?`, `... !`.
- The correct answer carries no trailing stop.

## Loanword lock — the sense, not the spelling (11 September 2026)

A lock entry binds **the concept it names, in that concept's sense.**

- In that concept's word row and in every exercise of that concept, use the locked rendering.
- In a sentence of another concept, use the locked rendering only when the English word carries the
  same sense. When it carries a different sense — "gate" meaning a garden gate, "cool" meaning to
  lower a temperature — translate the word normally, and name the exercise id in your report.
- Never bend a sentence to fit a lock.

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
