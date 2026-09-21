# Phase 2J S5 - corrected upload files (B3)

Generator: `phase2j/partB/b3.py build` (0 model calls). Sources: phase2i/upload/ (unchanged) + partB/audit/AUDIT_RESULTS.jsonl (B2) + partB/B1_flags_*.jsonl (B1).
Same format as phase2i/upload/ (xlsx sheet sk/cz, columns exercise_id, language_code, level, src, en, structure_json; jsonl one annotation per row, same key order and serialisation). `v[0] == en` holds on every row.

Rules: only B2-flagged SK references on the 3200 audited rows are touched (B2 coverage incomplete: packets p032, p033, p034, p035, p036, p037, p038, p039, p040 not audited).
- adds content (A): the added span is removed in place (exactly one occurrence, article a/an repaired, time frame must stay the same, else listed).
- narrows (N): the flagged reference stays; the span replaced by the broader word is ADDED as a further variant.
- wrong person or gender (W): only he/she-family pairs on sentences with one gender only; other gender ADDED (source open), or the flagged ref REPLACED where B1 read a fixed contradicting gender; person/number W are listed, not changed.
- other (O): listed, not changed. Faithful references are never touched. Added variants pass the 1P lever-3 tense filter against v[0].
- Czech: 0 changes; every B1 CZ flag listed (reader noise, no model audit).

Rows changed: SK 577, CZ 0. v[0] changed on 58 rows (all flagged v[0]; en updated with it).

| lang/class | replaced | added | removed | listed |
|---|---|---|---|---|
| cz/B1_gender_contradiction | 0 | 0 | 0 | 15 |
| cz/B1_gender_fixed_open | 0 | 0 | 0 | 10 |
| cz/B1_neuter_as_he_she | 0 | 0 | 0 | 13 |
| cz/B1_number | 0 | 0 | 0 | 16 |
| cz/B1_person | 0 | 0 | 0 | 53 |
| sk/A | 60 | 0 | 0 | 5 |
| sk/N | 0 | 164 | 0 | 8 |
| sk/O | 0 | 0 | 0 | 141 |
| sk/W | 0 | 385 | 0 | 84 |
| sk/dedup | 0 | 0 | 1 | 0 |

Per-reference detail: `B3_diff.jsonl` (action replaced / added / removed / listed + reason). Hashes: `partB/B3_result.json` b3.out_sha256.
