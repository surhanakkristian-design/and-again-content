# Phase 2B DATA defects (recorded, not fixed) — 19 Sept 2026

1. **No `sentence_translations` table live.** Sentences (full_sentence, correct_answer) live in `exercise_localizations`
   (9 languages x 48,572 rows). The selection uses that table.
2. **No concept level column.** `word_concepts` has id, word, part_of_speech, definition only. Level derived: level of the
   concept's vocabulary exercises (types 27/74/76 = A, 68/69/75/77 = B); 146 concepts have both -> family of their grammar
   exercises; 39 still ambiguous (34 with no grammar exercise, 5 with A and B grammar) -> A. Result A 1600 / B 1457.
3. **The 7,200 target (3,600 concepts x 2) is unattainable.** The live DB has 3,057 concepts in total, only
   2,286 have any grammar-topic sentence. Selection = 4,109
   (1,823 concepts x 2 + 463 x 1; 771 concepts get 0). Shortfall 3,091.
   463 concepts have only one level of their pair (A: 161, B: 302).
4. **The synonym-group table is not live.** `translation_synonym_groups` (migration 20260918120000) is not applied; the
   groups exist only as `phase1b/synonyms/table.json` = **863** groups (the "~862"; forms.json holds 971 = 863 + 108 1C
   contextual groups). The literal "862" in the Phase 1C report is "862 M" tokens, not a group count.
5. **Czech language_code is `cz`, not ISO `cs`.**
6. **"5,895" is still unreproducible.** 2,139 probed counts (concept/exercise/media/localization counts, distinct
   sentences, every level subset, every contiguous topic-id run): no exact hit. Only documented origin: PROJECT_HANDOFF_CHAT.md
   ("about 5,895 sentences", pointing at a Phase 1 §1.2 that does not define it) and 1C extrapolations.
7. **2A's excluded list was incomplete.** A fresh scan of phase1*/pilot/measurements found 488 ids
   (2A list: 470); union with 2A's 1,000 selected = 1,487. 2B used the union; overlap = 0.
8. **Topic imbalance in B2** (observation): per-topic selected 16 (type 54 Mixed Conditional) .. 106 (type 66 All Past Tenses);
   the 'All ... Tenses' types have more exercises per concept. Grammar type 'Random' (70-73) has no exercises; excluded by rule.
9. **Alt map is heuristic.** No lemmatizer/WordNet in the pipeline (nltk absent): suffix-strip + the generated forms of
   forms.json. "mapped" means a group exists for the surface word, not that the sense matches (e.g. ring -> call_phone_ring
   in "a ring of small fish"). propose_new uses the only thesauri on disk (1C ng groups + annotator alt maps):
   mapped 692 / propose_new 31 / unmapped 491 tokens.
