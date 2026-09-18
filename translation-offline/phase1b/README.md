# Phase 1b – pattern-based offline translation check

FORMAT_SPEC.md is the source of truth for the data. Node ≥ 22.18 runs the `.ts` files directly (type stripping).

## File map

| Path | What |
|---|---|
| `FORMAT_SPEC.md` | data format: synonym table, mistake library, per-sentence annotation, checker order |
| `synonyms/table.json`, `synonyms/annotator.json`, `synonyms/*.json` | global synonym groups (all files merged; `annotator.json` = `ng` proposals from `merge_batches.ts`) |
| `synonyms/forms.json` | generated inflected forms per group and form tag (`build_forms.ts`) |
| `synonyms/forms_dropped.txt` | rule-generated forms that are not in `../wordlist/en_words.txt` |
| `mistakes/<type_id>.json` | mistake library per topic |
| `annotated/batch_*.json` → `annotated/<id>.json` | annotator batches → one annotation per sentence |
| `selection/all230.json`, `selection/sets.json` | the 230 sentences (reference, level, `new_long`) and the measurement sets |
| `review/lint.json` | lint gate output |
| `measure/` | measurement outputs; `measure/test_output.txt` = unit test run |
| `../checker/v2/match.ts` | compile(annotation, forms, library) → slot graphs; exact matcher; weighted-edit closest path |
| `../checker/v2/check.ts` | check(answer, compiled, {native, level}) → {verdict, step, feedback, unmatched, closest} |
| `../checker/v2/forms.ts` | forms generation (rules + irregular tables), used by `build_forms.ts` and the tests |
| `../checker/v2/v2.test.ts` | unit tests with synthetic fixtures |
| `scripts/data.ts` | shared loaders (work on whatever files exist) |
| `scripts/build_forms.ts`, `merge_batches.ts`, `lint.ts`, `measure.ts` | tooling (below) |
| `~/Projects/and-again/supabase/migrations/20260918120000_translation_offline_check_v2.sql` | DB proposal, NOT applied; supersedes the Phase 1 proposal |

Phase 1 files (`../checker/offlineCheck.ts`, `typedAnswer.ts`, `slots.ts`, `../pilot/`) are unchanged; v2 imports their normalisation,
typo, BrE/AmE, tip-template and feedback-language helpers.

## How to run (from `translation-offline/`)

```sh
node --test checker/offlineCheck.test.ts checker/v2/v2.test.ts   # full suite (Phase 1c: 78 tests, 78 pass)
node phase1b/scripts/merge_batches.ts                # batches → annotated/<id>.json, ng → synonyms/annotator.json (idempotent)
node phase1b/scripts/build_forms.ts                  # synonyms → synonyms/forms.json (+ forms_dropped.txt)
node phase1b/scripts/lint.ts                         # → review/lint.json, one summary line per error class
node phase1b/scripts/measure.ts coverage <translations.json> phase1b/measure/coverage.json
node phase1b/scripts/measure.ts fa <fa_translations.json> phase1b/measure/fa.json
node phase1b/scripts/measure.ts regression phase1b/measure/regression.json
node phase1b/scripts/measure.ts timing phase1b/measure/timing.json
node phase1b/scripts/measure.ts sizes phase1b/measure/sizes.json
```

Order after new data arrives: merge_batches → build_forms → lint → measure. Translations input:
`[{exercise_id, translations: [string | {text}]}]`; native language sk.

## Matching in one paragraph

Each variant becomes a graph over its word boundaries. Plain words carry their Phase 1 readings (contractions, numbers, noun + 's).
Slots replace words: `s` (group members in the anchor's form, from forms.json), safe groups (everywhere outside the lock),
`o`, `d` (on a determiner: replace; on a bare noun: insert before it), flipped `g` chains (one graph per gender assignment, so a
chain flips consistently). Optional words are insertion edges with a bit (each used once); `-anchor` is an ε edge. Locked words are
literal and take no insertion inside a lock piece. Mistakes are the variant with the lock (or anchor) replaced by the wrong text,
compiled with the same freedoms. The closest path for the tip is a weighted edit distance over the same graph (a typo substitution
costs 0.5, so a single typo is found on the best path), so the tip never asks to replace an allowed alternative.

## Known limits

- (Phase 1c) A multi-form verb anchor is narrowed by the preceding words only (no parser): with no auxiliary before it, `cut`
  still accepts the members in base AND past form (never pp).
- (Phase 1c) `her` flipped to masculine: `his` before a word, `him` before a non-noun or after a listed object verb
  (give/show/tell/let/make/help/see/…); "had her car" style exceptions outside that list are read as possessive.
- The closest-path search ignores the "optional word at most once" bit; an answer that only repeats an optional word gets the
  generic tip.
