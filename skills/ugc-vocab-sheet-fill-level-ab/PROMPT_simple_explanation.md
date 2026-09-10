# Claude Code — Simple Explanation (type 74 / 75)

Driven by `run_part.sh`:

    PROMPT_FILE=./PROMPT_simple_explanation.md GATE_SCRIPT=scripts/translation_status.py \
    CONCEPTS_PER_PASS=60 UNIT=exercises \
    caffeinate -dimsu bash ./scripts/run_part.sh "<workbook>.xlsx" 2>&1 | tee -a logs/simple.log

---

Use the skill `ugc-vocab-sheet-fill-level-ab`. Read its SKILL.md first — the typography
rules and the validator gates still apply.

## Token discipline

Open the workbook only with `openpyxl` inside a script, a handful of exercises at a time.
Never `cat` it, never print a sheet. Report counts, not contents.

## What this pass does

**Simple Explanation is the easiest exercise in the app: name the asset in at most four
words.** It is not written from scratch — it is the Label exercise, shortened.

Every new exercise (type **74** at A level, **75** at B) has a partner Label exercise
(type **27** / **68**) on the same media. The mapping is in
`<workbook> — simple_explanation.csv`: `exercise_id`, `derived_from_exercise_id`,
`media_id`, `concept_id`, `word`.

For each row: read the nine language rows of the Label exercise, shorten each of them,
and write the result into the nine rows of the new exercise.

## The shortening rule

**Keep the shortest phrase that still contains the target word — at most four words.**
Shorten `correct_answer`, `distractor_1` and `distractor_2` the same way, so all three
options come out in the same shape.

| word | Label answer | Simple Explanation |
|---|---|---|
| blender | to make a smoothie in a blender | a blender |
| smoothie | to make a smoothie in a blender | to make a smoothie |
| athletics competition | an athletics competition | an athletics competition (already short) |

- The target word must survive. That is the whole point of the exercise.
- Keep the article the Label answer used (`a blender`, not `blender`).
- If the Label answer is a verb phrase and the word is the verb, keep the verb phrase
  (`to make a smoothie`). If the word is a noun inside it, drop to the noun phrase.
- If the Label answer is already four words or fewer, copy it as it is.
- **The three options must stay mutually exclusive.** If shortening makes two options
  identical, back off one step and keep the shorter distinguishing phrase instead.
- `intro_text` stays **empty** in all nine languages, like the Label exercise.

## The other eight languages

Shorten each language from **its own** Label row, never by translating the English
result. This matters more than it sounds:

- Slavic languages have no articles and inflect: `robí smoothie v mixéri` → `mixér`,
  in the nominative, not the `v mixéri` that appears in the sentence.
- Hungarian and Turkish carry suffixes on the word: `turmixgépben` → `turmixgép`,
  `blenderda` → `blender`.
- German keeps its article and case: `in einem Mixer` → `ein Mixer`.

The four-word budget is an English-level guide, not a hard count for the others — a
natural short phrase in the target language wins over hitting a number.

## Typography — unchanged

`sk cz de` `„ … “` · `hu` `„ … ”` · `fr` `« … »` with spaces · `es ua` `« … »` without ·
`en tr` `“ … ”`. Spanish opens with `¿` / `¡`, French spaces before `? ! ; :`.
Most of these answers are bare phrases with no punctuation at all.

## Rhythm

- Work in `exercise_id` order from the CSV, all nine languages of one exercise at once.
- **Save after every 10 exercises.**
- Every 60 exercises run:
  ```bash
  python3 scripts/validate_part.py "<workbook>.xlsx" --loanwords ./loanwords.json
  ```
  and fix what it names.

## Finish condition — then STOP

`translation_status.py` shows every exercise fully translated and `validate_part.py`
exits 0. Then stop and wait for confirmation.

## Final report

Exercises written; any where the target word could not survive a four-word phrase; any
where shortening made two options collide and how you resolved it; anything you guessed.
