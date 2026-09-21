# Phase 2K - final Slovak upload

Files: `upload_sk_final.xlsx` (sheet `sk`; columns exercise_id, language_code, level, src, en, structure_json) + `annotations_sk_final.jsonl` (structure_json = the jsonl row).
4,064 rows; `exercise_id` is an integer on every row; `v[0] == en` on every row.

Source: `phase2j/upload/annotations_sk_fixed.jsonl` (B3-corrected) with the 4 references B3 truncated (exercise_id 927, 22385, 35040, 41408) restored to their value before B3 (`phase2i/upload`); detail in `RESTORE_4.json`.

**`v` is display-only and no longer grades.** Since Phase 2K the checker is SOURCE-ONLY: it judges the answer against the Slovak sentence. The stored English reference (`en`, `v`) stays in the data and is shown to the learner as the correct answer when they are wrong; it is never used to grade.

Reference-ending scan (preposition or article, SK final + CZ): `../analysis/ref_endings.json` (219 hits: SK 117, CZ 102).
