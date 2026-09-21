# Phase 2I Part 0 — clean upload copies (0 model calls)
Generator: `phase2i/part0.py` (originals untouched; SHA-256 of the originals asserted equal before/after).
| file | source | rows |
|---|---|---|
| upload_sk_final.xlsx (sheet sk) | phase2d/out/upload_sk_final.xlsx | 4,064 |
| annotations_sk_fixed.jsonl | phase2d/out/annotations_sk_final.jsonl | 4,064 |
| upload_cz_final.xlsx (sheet cz) | phase2h/out/upload_cz_final.xlsx | 4,064 |
| annotations_cz_fixed.jsonl | phase2h/out/annotations_cz_final.jsonl | 4,064 |
Columns: exercise_id (INTEGER), language_code, level, src, en, structure_json.
Corrections:
- `v = [en]` where v was empty: SK 0 rows; CZ 50 rows, n = 5365–5414 (all 50 consecutive).
- `exercise_id` written as integer: SK was already int (4,064); CZ was text on all 4,064 rows -> int.
- Asserted: round-trip of xlsx and jsonl, 4,064 + 4,064 rows, structure_json == jsonl row, `v[0] == en` on every row (0 exceptions; no row with non-empty v had v[0] != en).
- **`lk` stays in `structure_json` but is now UNUSED**: by the owner's decision of 21.9.2026 the checker no longer checks the practised grammar; the translation-only checker reads `lk` nowhere.
Per-row detail + output hashes: `part0_result.json`.
