---
name: ugc-vocab-sheet-fill-level-ab
description: "Fill the Supabase-ready vocabulary workbook in the NEW template schema ('UGC - Claude x Higgsfield_new_template.xlsx': Instructions, All Words, media, media_categories, word_concepts, word_localizations, concept_media, exercises, sentence_translations, categories, styles, ALIAS - exercise_types, EXAMPLE - B level). Two modes: (A) fill the rows of a just-finished generation batch, (B) partition an existing curated word list into N import-ready part workbooks and fill them. Trigger on 'fill in the sheet', 'fill the Excel', 'update the tracking file', 'align the file with the generated videos', 'split the B words into parts', 'generate part1..part6'. Every id is a deterministic function of the input; every part is gated by validate_part.py before delivery. Never touches rows outside the window, never overwrites filled cells without asking, never invents an asset."
---

# UGC Vocab — Fill the Supabase workbook (new template schema, 2026-08)

The workbook feeds Supabase directly. Ids and foreign keys must be exact, spellings verbatim,
every language row genuinely in its language, and every uncertain cell flagged in the summary
instead of silently guessed. **Nothing ships until `scripts/validate_part.py` exits 0.**

## Two modes

| Mode | When | What it does |
|---|---|---|
| **A — batch fill** | The user attaches folders of freshly generated media | Step 1 QC on every clip → then Steps 2–5 for that window only |
| **B — bulk partition** | The user points at a curated source workbook + an assets folder and asks for `part1..partN` | Media already passed QC: verify assets EXIST, skip re-watching → scaffold with `build_parts.py`, then Steps 3–5 per part |

Mode B is the default for the B-level export (source: `UGC - Claude x Higgsfield - Vocabulary_update.xlsx`,
assets: `…/And Again/UGC Videos/Checked Videos`).

## Workbook map — NEW schema (this replaces the old dictionary_*/sentences layout)

| Sheet | Role |
|---|---|
| **Instructions** | AUTHORITATIVE. Read FIRST at runtime; where it conflicts with this skill, it wins. |
| **All Words** | Master rows, key `media_id`: media_id, word (article included), part of speech, Level (A/B), Irony, meaning, Recommended category, Voiceover, Explanation. |
| **media** | id = media_id, title = `<slug(word incl. article)>_<media_id>`, media_url, thumbnail_url, style_id, media_type (`video`/`image`). |
| **media_categories** | media_id ↔ category_id. **Exactly one row per media item.** |
| **word_concepts** | **One row per UNIQUE word**: id, word (article STRIPPED, lowercase), part_of_speech. No language column — this sheet stays **English only** (user decision, Aug 2026): the word is translated in `word_localizations`, `part_of_speech` is never translated, and `meaning_context` / `category` no longer exist as per-language fields. Never add columns to this sheet. |
| **word_localizations** | id, concept_id, language_code, translation. **Exactly 9 rows per concept**, one per language. This is the only place the word itself is translated. |
| **concept_media** | id, concept_id, media_id. **Exactly one row per media item** — this is how several media share one concept. |
| **exercises** | id, concept_id, media_id, exercise_type_id, options_count. **Structure only — no text.** |
| **sentence_translations** | id, exercise_id, language_code, intro_text, correct_answer, distractor_1, distractor_2. **Exactly 9 rows per exercise.** All exercise TEXT lives here, including the English original (`en` row). |
| **categories** | Categories_ID 1–40 + names EN/SK/CZ/DE. |
| **styles** | 1 Ilustrácie, 2 Fotky, 3 Videá, 4 Disney, 5 Anime, 6 Rozprávky 80tky. |
| **ALIAS - exercise_types** | id, title, level, focus_category — **69 ids, no language_code column, POV DEPRECATED**. |
| **EXAMPLE - B level** | The 39-row blueprint (format only — its content was written without videos, never imitate it). |

**Languages (9, fixed order):** `sk, en, de, cz, fr, es, ua, tr, hu`.
The old 14-language set, the 4 learning languages, `dictionary_words`, `dictionary_translations`,
`sentences`, `dictionary_word_media`, `translated_text`, `unlock_tier` and the human-readable
`Exercises` sheet **no longer exist**. Never recreate them.

**Authority hierarchy:** (1) Instructions sheet + the user's direct answers, (2) the instruction
row inside each sheet, (3) the EXAMPLE tab (format only), (4) existing data rows — LAST and never
a precedent (the old workbook is 57% blank in `dictionary_translations` and 98% blank in
`sentence_translations`; it is the defect, not the model).

## The exercise contract — non-negotiable counts

Derived from the Instructions sheet and confirmed against the blueprint and ALIAS:

- **media_type = `video` → exactly 39 exercises**, in this exercise_type_id order:
  `31…49` (19 × B1) + `50…67` (18 × B2) + `68` Label the video + `69` Meaning of the word.
- **media_type = `image` → exactly 2 exercises**: `68` + `69` (vocabulary only). Trim anything else.
- **`media_type` decides, not `style_id`** (styles 4/5/6 contain both videos and images).
- **POV is gone.** A legacy POV exercise maps to **`68` Label the video**, keeping its context:
  the POV caption becomes the correct label phrase (`POV: Providing VIP service.` → `to provide
  VIP service`), the two POV distractors become same-shape label distractors. Never emit id ≥ 70.
- **No skipping — confirmed by the user (Aug 2026): 39 exercises for every video, 2 for every
  photo/illustration, no exceptions.** If the target word resists a topic, the
  sentence stays in the video's world and the topic is carried by the sentence around the word
  rather than forced onto it — a grammatically wrong or absurd exercise is still never acceptable.
  If a topic truly cannot be built, flag it in the summary and ask; do not silently drop the row.
- **options_count** = 3 with two distractors, 2 with one. It must agree with all 9 language rows.
- **English length budget (Instructions sheet, Aug 2026):** in the `en` row only —
  `intro_text` ≤ 90 characters, `correct_answer` / `distractor_1` / `distractor_2` ≤ 50.
  The other 8 languages carry NO limit: they are shown briefly as a translation aid, so natural
  phrasing wins over squeezing under a count. `validate_part.py` enforces this as `E13`.

## Id algebra — every id a pure function (idempotent, collision-free)

| Sheet | Rule |
|---|---|
| media_id | **Never renumbered** — taken from the source. |
| word_concepts.id | Continues from the last delivered part — part1 holds 1–150, so part2 starts at **151** (user decision, Aug 2026: no offset, ids simply run on). `word_localizations.id` then also continues seamlessly, since it is derived from the concept id. |
| word_localizations.id | `(concept_id − 1) × 9 + language_index + 1` |
| concept_media.id | Running integer across the whole export, in (concept, media_id) order. |
| exercises.id | Running integer across the whole export, in part → concept → media → type order. |
| sentence_translations.id | `(exercise_id − 1) × 9 + language_index + 1` |

Because ids derive from position, re-running the scaffolder reproduces the same file byte-for-byte
in the structural columns — a crashed run resumes without renumbering anything.

**Cross-level collision:** some B words also appear as A-level rows.
before an A-level export, load the B `word_concepts` as a registry and REUSE the existing
concept_id for any word already there. Never let one word get two concept ids.

**Continuation offsets.** `exercises.id` and `concept_media.id` run continuously across parts. When
a part was delivered before this rule existed, do NOT renumber it mid-flight: read its max ids and
pass them to the scaffolder for the next part
(`--exercise-id-start`, `--concept-media-id-start`, `--concept-id-start`). Renumbering an in-progress
workbook is never worth the risk; if a uniform shift is needed later, it is one mechanical pass
after the content is finished and validated.

## Step 1 — QC (Mode A only)
Unchanged from v1 and mandatory when the media is new: Pass A cut map → Pass B 10 fps contact
sheets → Pass C forensic zoom only where something looks wrong; the 1c story-audit ledger (object
counts start → cuts → end, action-completion criterion, scene constancy, static world, behaviour
logic) written into the log; 1d blind-transcription voiceover check; 1f salvage-by-trim before any
`Error`. A `Yes` without a written ledger is invalid. An `Error` word gets NO rows in ANY sheet.

**Mode B skips the watching pass** (the source folder is `Checked Videos` — already QC'd) but MUST
still verify that every media title has a real file of the right type (`build_parts.py --assets`,
`validate_part.py --assets`). A row whose asset is missing is dropped from the part and reported —
never write a row pointing at a file that does not exist.

## Step 2 — All Words, media, media_categories, concept_media (mechanical)
Run `scripts/build_parts.py --strip-examples` (user decision: the template's Example rows are
deleted from the part workbooks; the per-sheet **instruction row is kept** — it is the runtime spec,
and every script skips it by testing whether column A parses as an integer). It copies All Words and media verbatim, resolves the category name to
`category_id`, writes one `media_categories` and one `concept_media` row per media item, creates the
deduplicated `word_concepts`, the 9 empty `word_localizations` rows per concept, all `exercises`
rows, and the 9 `sentence_translations` skeleton rows per exercise. **Do not hand-write any of this.**

Canonical spelling rules: All Words keeps `a/an` (`A break`, `An alley`); `word_concepts.word`
strips it and lowercases (`break`, `alley`); `media.title` keeps it (`a_break_1`, `an_alley_1673`)
because the file on disk is named that way.

## Step 3 — The English content pass (per concept, save after every concept)
For each exercise, write the `en` row of `sentence_translations`:
- **intro_text** — the sentence with the gap (`...`); empty on type 68, a `"<word>" means...` stem on type 69.
- **correct_answer / distractor_1 / distractor_2** — the option set. Exactly one option is truly
  correct; distractors are plausible level-typical learner errors, never defensible alternatives.
- **Video alignment is the crucial rule:** every sentence lives inside THAT media item's world —
  its subject, setting, props, plot and mood, from the All Words `Explanation of the video` (and
  the clip itself in Mode A). Never a generic shop/window/box sentence.
- Level rules bind: B1 rows stay B1, B2 rows may use the advanced structures. Max 2 sentences,
  ideally 1. Gen Z (15–25) contexts, irony welcome where the clip earns it.
- **68 Label the video** — `intro_text` stays EMPTY in every language; the options are short phrases
  naming what the media shows (`showing off her framed certificates`) + two same-shape wrong phrases.
- **69 Meaning of the word** — `intro_text` is the stem `"<english word>" means...`, localized per
  language while the quoted word stays English (`"certificate" znamená...`, `"certificate"
  bedeutet...`); the options are meaning phrases aligned with the All Words `meaning of the word`
  + two plausible wrong meanings.
- Every other type (31–67) carries the gapped sentence in `intro_text`, gap marked `...`.
- Grammar audit as an English teacher before moving on: correct, natural, idiomatic, genuinely
  testing its topic.

## Step 4 — The language pass (8 languages, per concept)
Then fill `sk, de, cz, fr, es, ua, tr, hu` for every exercise, and the 9 `word_localizations` rows.

- **A language_code row is ENTIRELY in that language** (Instructions sheet). No English fallback,
  no half-translated row, no copy of the `en` row. `E10` fails the part for this.
- **Distractors — the hierarchy:** (1) **mirror the error** — reproduce the equivalent mistake in
  the target language (EN `2 cats.` / `2 cat.` → SK `2 mačky.` / `2 mačka.`); the distractor is
  SUPPOSED to be wrong in the target language. (2) **Bracket gloss (max 3 words)** only when the
  contrast has no equivalent and two options would otherwise be identical. (3) **Never fabricate**
  a fake form — translate the sense plainly and flag the row.
- **Loanword rule (food & cultural terms).** When no clean 1:1 equivalent exists, use ONE agreed
  loanword per language, identically in `word_localizations` and in every `sentence_translations`
  row of that concept (`dumplings` → `dumplingy`, never `pirôžok` in one row and `raviole` in the
  next). The lock file is `loanwords.json`; extend it the moment a new such term appears, and never
  substitute a local dish name for a foreign concept.
- **No two language rows of one exercise may be byte-identical** (`E11`). sk/cz coinciding on a
  short loanword answer is a `W1` warning to eyeball, not an automatic pass.

## Step 5 — Validate, then deliver
1. `python scripts/translation_status.py <part>.xlsx` to see where the file stands and what is next
   (read-only; it is also how a resumed run finds its place).
   Then `python scripts/fix_typography.py <part>.xlsx --apply` for the mechanical repairs, and
   `python scripts/rework_list.py <part>.xlsx` for rows whose English breaks the length budget or
   whose translations re-invented the scene; `sample_check.py` prints a readable sample for the
   human review that no script can replace.
2. `python scripts/validate_part.py <part>.xlsx --assets <dir> --loanwords loanwords.json` after
   **every 25 concepts** and again before delivery. Exit 0 or it does not ship.
3. Fix what it names; never silence a check.
4. Report per part: concepts / media / videos / images / exercises / translation rows, assets
   verified, dropped rows and why, POV rows remapped, loanword decisions, `W1`/`W2` warnings with a
   one-line judgement each, and every cell the user must still decide on.

## Single-phase runs (the user may ask for one phase only)
The user often runs ONE phase per session — e.g. "only continue the translations in part 1, then
stop". In that case: touch nothing outside that phase's columns, do not re-open QC, do not
renumber, do not start the next part, and **stop at the phase boundary with a short report instead
of continuing into the next phase.** Waiting for the user's confirmation is the deliverable.

## Chunking & resumability
Generate **one concept at a time and save**; an interruption loses at most one concept. The scaffold
already contains every id, so a resumed run finds its place by looking for the first
`sentence_translations` row with an empty `correct_answer`. Never renumber to "tidy up".

## Never
- Never write a row for a media item whose asset does not exist.
- Never emit exercise_type_id ≥ 70, or the 14-language set, or the removed sheets.
- Never leave `translation`, `correct_answer` or `distractor_1` empty.
- Never overwrite a filled cell without asking; collect and ask once at the end.
- Never let the old workbook's existing rows serve as a model for anything.

## No silent fallback

If a step cannot find its input or an external tool fails, print the failure and stop.
Never write a substitute file, never fall back to copying the raw source, never
regenerate something that was supposed to be looked up. A script that produces a
plausible-looking wrong result is worse than one that crashes.
