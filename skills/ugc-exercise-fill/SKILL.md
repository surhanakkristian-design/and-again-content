---
name: ugc-exercise-fill
description: Fill the And Again exercise workbook from an intake snapshot — build a part, write the English exercises, translate into nine languages, validate, and hand it over for review. Use this whenever the user mentions building a part, filling exercises, the translation pass, run_part, validate_part, chunks, correct_alternative, or an intake snapshot, and whenever they ask to turn assigned vocabulary assets into exercises, even if they do not name a script. Also use it when a part has come back failing validation and needs repair.
---

# And Again — exercise fill

Turns a snapshot of assigned vocabulary assets into workbook rows: one concept per word
sense, its media row, its exercises, and those exercises in nine languages.

Read `HANDOFF.md` and `EXERCISE_AUTHORING_SPEC.md` in the project folder before using this.
The spec is the authority on what a row must contain; this file is the authority on the
order of operations.

## Before anything

`SETUP.md` must be done. If any required file is missing or more than one copy of
`build_parts.py` exists on the machine, stop and say so. Do not proceed on a guess.

Never take id numbers from a document. Read the live maxima from Supabase every time.

## Step 1 — Build the part

One part is about 250 assets, not the whole snapshot. Six parts for this batch. A
validation failure at the end of a 1,486-asset part means repairing a file with half a
million rows.

```bash
python3 ~/.claude/skills/ugc-vocab-sheet-fill-level-ab/scripts/build_parts.py \
  --source "<snapshot>.xlsx" --template "<template>.xlsx" \
  --out partN-exercises --parts 1 --one-asset-per-concept --strip-examples \
  --exclude <every earlier part> \
  --concept-id-start <next> --exercise-id-start <next> --concept-media-id-start <next>
```

`--exclude` filters by `media_id` only. If you find a copy that also filters by word, it is
the wrong copy — it silently drops legitimate rows, because one word may legitimately
appear across several assets.

Words that already exist live with the same everyday sense reuse the live `concept_id`.
Judge that by what the live concept teaches, not by whether the coverage file puts the two
on different rows.

Pictures need a style id. The build refuses an empty style, so decide the style before
building a part that contains pictures.

## Step 2 — Write the English exercises

Follow `EXERCISE_AUTHORING_SPEC.md` section 8, in that order:

1. Write `intro_text`, `correct_answer`, both distractors.
2. Check the sentence is natural in the target language.
3. Fix punctuation and spacing — **per language, never in one sweep**.
4. Build `full_sentence`.
5. Only then produce `chunks` and `correct_alternative`.

Chunking before the sentence is final means chunking twice: the join-back check compares
against `full_sentence`, so every later fix invalidates the pieces.

Type 69's correct answer is the media's meaning column copied character for character.
That is why the meaning is capped at 50 characters. Never write your own text there.

Type 68 has no `intro_text`. Types 33, 34, 37 and 42 are two-option by design — leave
`distractor_2` empty rather than inventing a third option.

English budgets: `intro_text` ≤ 90 characters, options ≤ 50. Other languages uncapped.

Stop here and hand the English rows to Kristian before translating. Fixing one English
sentence is cheap; fixing its nine versions is not.

## Step 3 — Translate

```bash
cd partN-exercises
PROMPT_FILE=~/.claude/skills/ugc-vocab-sheet-fill-level-ab/PROMPT_translations.md \
CONCEPTS_PER_PASS=40 caffeinate -dimsu \
bash ~/.claude/skills/ugc-vocab-sheet-fill-level-ab/scripts/run_part.sh "<workbook>.xlsx" \
  2>&1 | tee -a logs/overnight.log
```

This chains fresh sessions until the gate says DONE. The workbook is the progress record,
so interrupting and rerunning the same command resumes.

If you start a long run, **detach it from the session**. A run started as a child of the
chat window dies when the window closes. Use a double-fork and `setsid`, verify the parent
pid is 1, and show that line rather than asserting it.

Alive is not enough. If the committed row count does not move across two consecutive
passes, that is a fault — say so loudly. A process that runs and writes nothing is worse
than one that dies.

Quotes per language: `sk cz de` use `„ … “` · `hu` uses `„ … ”` · `fr` uses `« … »` with
spaces · `es ua` use `« … »` without · `en tr` use `“ … ”`. Spanish opens with `¿` `¡`.
French keeps its spaces before `? ! ; :`. The gap between quote marks is exactly three
dots.

Translate the sentence. Never invent a new scene to make an English structure fit.

## Step 4 — Validate

The part is machine-clean when the validator exits 0.

```bash
python3 ~/.claude/skills/ugc-vocab-sheet-fill-level-ab/scripts/fix_typography.py "<wb>.xlsx" --apply
python3 ~/.claude/skills/ugc-vocab-sheet-fill-level-ab/scripts/sample_check.py   "<wb>.xlsx" --n 15
python3 ~/.claude/skills/ugc-vocab-sheet-fill-level-ab/scripts/sample_check.py   "<wb>.xlsx" --flags-only
```

Run the spec's section 9 checklist over the finished file and **report every failing row
rather than fixing it silently**.

The validator must enforce, in code and not in a prompt:

- `...` is a blank and nothing else; a pause is `…`
- a split unit gets two blanks, and both distractors carry the same two-part shape
- the blank count in `correct_answer` is exactly one less than in `intro_text`
- `chunks` join back to `full_sentence` character for character
- every `correct_alternative` is a permutation that keeps the capitalised piece first and
  the punctuated piece last
- the chunk exemption fires under 1% per language

## Step 5 — Hand it over

Then the part is Kristian's to check. Look hardest yourself at type 69, at Hungarian and
Turkish, and at any grammar type whose English structure the target language lacks.

## After a part is finished

Fold the newest scripts and prompt back into the skill so the part folder holds only data:

```bash
S=~/.claude/skills/ugc-vocab-sheet-fill-level-ab
P="<part folder>"
cp "$P/scripts/"*.py "$P/scripts/run_part.sh" "$S/scripts/"
cp "$P/loanwords.json" "$S/loanwords.json"
chmod +x "$S/scripts/run_part.sh"
```

Then copy the skill back to the Drive folder as the master. Never edit both copies.

## What never happens

- No silent fallback. A script that cannot find what it needs prints the failure and stops.
  It never writes a substitute, never guesses a path, never pairs a file to a row by
  filename similarity.
- No hand-correcting a file that a script rebuilds. Fix the source the script reads.
- No punctuation fix across several languages at once.
- No id taken from a document instead of the database.
