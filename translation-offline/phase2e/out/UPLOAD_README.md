# Upload package — Phase 2D

**Nothing here has been uploaded and nothing was written to the database.** These files are for the owner to
upload himself.

## Files

| file | language | rows | status |
|---|---|---|---|
| `upload_sk_final.xlsx` | Slovak (`sk`) | 4,064 | complete, gated, ready |
| — | Czech (`cz`) | 0 | **no file**: Phase 2D completed no Czech batch (see the report, §3) |

Czech has 3,200 rows of raw session output banked in `phase2d/out/sessions/`, but no batch reached all 20
sessions, so by the phase rule nothing was assembled and there is nothing to upload.

## Column map — `upload_sk_final.xlsx`, sheet `sk`

| column | content | database |
|---|---|---|
| `exercise_id` | integer | `exercise_localizations.exercise_id` — the row key |
| `language_code` | always `sk` | `exercise_localizations.language_code` — the second half of the row key |
| `level` | A1 / A2 / B1 / B2 | from `exercise_types.level`; carried for filtering only, **do not write it** |
| `src` | the Slovak sentence as it is stored today | equals `exercise_localizations.full_sentence` for that (`exercise_id`, `sk`) row — carried so the uploader can assert it still matches before writing |
| `en` | the English reference as it is stored today | equals `exercise_localizations.full_sentence` for that (`exercise_id`, `en`) row — same purpose |
| `structure_json` | the whole 34-field annotation as one JSON object | the payload |

**Each line updates exactly one row: `exercise_localizations WHERE exercise_id = <exercise_id> AND
language_code = 'sk'`.** `src` and `en` are there to be compared, not written.

### One thing the owner must decide before writing anything

`structure_json.lk` is the key phrase of the **English** sentence, and `structure_json.lk_supplied` is the value
currently stored in `exercise_localizations.correct_answer` for the **`en`** row, not the `sk` row. So a `lk`
correction, if it is applied at all, lands on the English localization, while everything else in
`structure_json` describes the Slovak row. The upload therefore touches two rows per exercise, or one row plus a
separate English correction list. Phase 2D did not determine which column the annotation structure itself
belongs in — that is a schema decision, not a measurement, and it was deliberately left to the owner.

### Fields inside `structure_json`

`exercise_id`, `language_code`, `n`, `concept_id`, `headword`, `level`, `exercise_type_id`, `type_title`, `src`,
`en`, `correct_answer_src`, `lk_supplied`, `v`, `lk`, `lk_verdict`, `lk_reason`, `person`, `number`,
`perfective_present`, `voice`, `agent_nom`, `gender`, `tense_open`, `tf`, `subject`, `embedded_agents`,
`fragment`, `main_sentence_index`, `alt`, `rewrite`, `script_voice_paths`, `script_reader_agent`,
`field_sources`, `flags`.

Largest `structure_json` cell over the sheet: **2,937 characters against Excel's 32,767 limit** — 11× headroom,
nothing is near truncation. The canonical artefact stays `phase2d/out/annotations_sk_final.jsonl`; the .xlsx is
a faithful container for it. If the import path can read JSONL, use the JSONL.

## Check these on the first ten rows before running the upload

1. **The row key resolves.** `exercise_id` + `language_code = 'sk'` hits exactly one `exercise_localizations` row.
2. **The source has not moved.** Column `src` still equals that row's `full_sentence`, character for character.
   These sentences were read on 19–20 September 2026; if one has been edited since, its annotation is stale.
3. **`structure_json` parses** and its `exercise_id` equals the `exercise_id` column.
4. **`v[0]` equals `en` verbatim.** That is an invariant of the annotation pass; a row where it fails is corrupt.
5. **`lk[0]` is a verbatim, case-sensitive substring of `en`.** True on 4,064/4,064 here — re-assert it after any
   spreadsheet round-trip, because Excel will silently strip a leading apostrophe or convert a lone `-`.
6. **`lk[0]` vs `lk_supplied`.** They differ on **2,076 of 4,064 rows (51.1 %)**. That is the point of this phase,
   not an error — but look at ten of them and satisfy yourself the new span is the better one before overwriting
   anything. Row `n = 3661` is the single known bad one: it kept the old value because the model's correction was
   not contiguous in `en`.
7. **`lk_verdict`.** The .xlsx carries the two-way value (`exact` / `adjusted`). The **three-way** class
   (`exact` 48.87 % / `adjust` 24.75 % / `unusable` 26.38 %) is in `phase2d/out/lk_corrected_sk.jsonl`. The
   `unusable` rows are the ones whose stored answer is a numeral, conjunction or pronoun rather than a verb
   phrase — decide whether those are data defects or legitimate non-verb exercises before touching them.
8. **Excel type coercion.** Open the file and confirm `exercise_id` is still an integer and that no sentence has
   been reinterpreted as a date or a number.
9. **Nulls are meaningful.** `subject` null = pro-drop, `gender` null = not marked, `script_reader_agent` null =
   the reader abstained. Do not coalesce them to empty strings.
10. **`lk` is the only field re-judged in Phase 2D.** Everything else is Phase 2C's output, unchanged and
    byte-verified.


---

# ADDENDUM — Czech (Phase 2E)

`upload_cz_final.xlsx` — sheet **`cz`**, **1,900 rows**, the same six columns as the Slovak file
(`exercise_id`, `language_code`, `level`, `src`, `en`, `structure_json`), the whole 34-field annotation as
JSON in the one `structure_json` cell. Lossless; nothing was uploaded.

* **Largest `structure_json` cell: 2,936 characters against Excel's 32,767-character limit** (11.2x headroom).
  Largest row: `exercise_id` 36878.
* Each line updates exactly one row: `exercise_localizations WHERE exercise_id = <exercise_id> AND
  language_code = 'cz'`.
* **`lk` is the Phase 2E dedicated pass, not the v session.** Czech `lk[0]`, `lk_verdict` and `lk_reason` come
  from `run_2e_lk.py` (prompt sha16 `5fa910459c078539`, the model sees only `en` and `correct_answer_en`);
  every other field is byte-identical to the batch annotations, asserted row by row on merge.
* **The same two open questions as Slovak apply unchanged**, and neither was settled here:
  1. `lk` / `lk_supplied` describe the **English** localization row (`correct_answer` for
     `language_code = 'en'`), while the rest of the structure describes the Czech row. The upload touches two
     rows per exercise, or needs a separate English correction list. That is a schema decision for the owner.
  2. Stored answers that are numerals, conjunctions or relative pronouns are labelled `unusable` by the judge.
     Either the data is wrong on those rows or the judge's scope is too narrow. Nothing was overwritten.
* **Rows that are missing, and why**, are recorded per batch in `annotations_cz_NNNN.meta.json`
  (`row_ranges_present`, `row_ranges_missing`, `sessions_missing`) and in `PARTIAL_cz_NNNN.json`.
