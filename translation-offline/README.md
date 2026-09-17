# Offline translation check – Phase 1 pilot

"Translate the sentence" without AI at runtime: every exercise gets stored acceptable English
translations and typical mistakes with prepared feedback; the phone checks the answer offline.
Report: `~/Projects/and-again/docs/features/reports/TRANSLATION_OFFLINE_PHASE1_REPORT.md`.
Migration proposal (not applied): `~/Projects/and-again/supabase/migrations/20260917160000_translation_offline_check.sql`.

| path | what |
|---|---|
| `GENERATION_SPEC.md`, `REVIEW_SPEC.md` | the instructions the generation and review passes followed |
| `scripts/dump_rows.py` | read-only dump of the grammar rows (en/sk/cz `full_sentence`) → `data/grammar_rows.json` (git-ignored, 10 MB) |
| `scripts/allocation.py` | Part A: tiers, eligibility, allocation table → `measurements/allocation_table.json` |
| `scripts/select_pilot.py` | the 200 pilot sentences (bench cases included) → `pilot/selection.json` |
| `pilot/batches/` | generation input, 10 batches by level |
| `pilot/generated_pre_review/` | generation output as written (slot syntax) |
| `pilot/generated/` | the same files after the review pass |
| `pilot/review/` | review lists and change logs |
| `pilot/expanded/` | database shape: slots expanded + normalised form, `_lint.json`, `_stats.json` (`node scripts/build_pilot.ts`) |
| `checker/` | pure TypeScript checker + tests (`node --test checker/*.test.ts`); `typedAnswer.ts` is a byte copy of the app's `lib/typedAnswer.ts` (asserted by a test) |
| `wordlist/` | SCOWL en_US (size 60) expanded to 99,756 lower-case forms + build script + licence |
| `measurements/` | allocation, lint before review, coverage and bench runs (`node scripts/run_measurements.ts`), timings |
