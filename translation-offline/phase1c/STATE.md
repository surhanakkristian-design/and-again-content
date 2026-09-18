# Phase 1c STATE (handover; each agent appends a terse section)

## prep (18.9.2026)
Paths relative to `~/Projects/and-again-content/translation-offline/`. Nothing committed yet.

**§0 counts** → `phase1c/counts_s0.json`. Correct 510 (measure 210 = 70 ids × 3 in `phase1b/measure/coverage_translations.json`;
supp 300 = 60 ids × 5 in `phase1b/supp/translations.json`), wrong 210 (70 ids × 3 in `phase1b/measure/fa_translations.json`,
T53/W53/M52/S52). 130 distinct ids (A1 17, A2 23, B1 48, B2 42); measure ids and supp ids are DISJOINT (measure 70 incl. all 30
long; supp 60, 0 long). `*_b3.json` files are subsets. New translations needed: none (0 tokens).

**§1 checker v2 patches** (in place): `checker/v2/match.ts` (verbContext + groupAlternatives narrowing for multi-form verb anchors;
flipPronoun "her"→his|him single reading with HER_OBJECT_AFTER verbs), `checker/v2/check.ts` (spellingReadings: BrE/AmE as a
normal substitution in steps 1b–4; tip shows learner's number words), `checker/v2/v2.test.ts` (+4 tests, fixture group cut_chop).
Full suite: `node --test checker/offlineCheck.test.ts checker/v2/v2.test.ts` → **78 tests, 78 pass, 0 fail** (was 74: 44 Phase 1
+ 30 v2). The 4 new tests fail on the unpatched code (verified). `phase1b/synonyms/table.json` +end_finish (v) → 863 groups,
safe still 30; forms rebuilt (`phase1b/synonyms/forms.json`). FORMAT_SPEC.md: have_to NOT safe recorded (§1), example fixed,
patch summary in §4. README known limits updated.
Tooling (not checker): `phase1b/scripts/data.ts` honours `ANN_DIR` (default phase1b/annotated); `lint.ts` honours `LINT_DIR`.

**§2 selection** → `phase1c/selection.json` (seed 20260918; S/L split seed+1). Plan A1 12 / A2 16 / B1 28 / B2 24 (= all230
proportion), S = ¼ of each level, L = ¾.
- S (20): A1 3, A2 4, B1 7, B2 6; long 3; sources measure 8 / supp 12; b3 3.
- L (60): A1 9, A2 12, B1 21, B2 18; long 9; sources measure 27 / supp 33; b3 9.
- All 80 have blind translations; needs_translation: none. b3 used only for B1 (non-b3 B1 pool = 16): 12 ids.
- Long ids: 1018 3603 9907 (S); 3084 4449 1452 5595 9244 3494 2955 2874 103 (L).

**§3 tasks**: `phase1c/tasks/batchS.md` (33.8 k chars, 18 topics), `phase1c/tasks/batchL.md` (69.5 k chars, 38 topics); built by
`phase1c/scripts/build_tasks.py`. Self-contained (rules + sentences + library index of the batch topics; no synonym index, no
Phase 1 mistakes). Annotator writes `phase1c/annotated/batchS.json` / `batchL.json` (array; §3 format with `alt` instead of `s`/`ng`).

**Mapping** `phase1c/scripts/map_alts.ts` (zero tokens):
`node phase1c/scripts/map_alts.ts phase1c/annotated/batchS.json` (then batchL) → `phase1c/annotated/<id>.json` (checker format,
`alt` kept), ng groups → `phase1b/synonyms/ng_phase1c.json` (ids ng1c_N, dedup by pos+members, `ok`/`bad` EMPTY → lint flags
syn_missing_ok_bad until review-syn fills them; `basis` = nearest existing group), report `phase1c/annotated/map_batchS.json`
(`stats`: alternatives, alt_mapped_existing, alt_new, anchors_to_existing_group, anchors_to_ng, ng_new_groups, ng_reused_groups
= the §5 numbers; run S before L so L's "reused" counts ng from S). Anchors inside a lock are skipped (listed). Then
`node phase1b/scripts/build_forms.ts`. Tested on `phase1c/scripts/map_alts_fixture.json` (3 sentences: 7 anchors, 3 alts → existing
groups, 5 ng incl. spine/thorn/prickle n, has no idea/doesn't know x) + e2e compile/check: the thorns/night/dial/doesn't-know
answers → correct. Limits: pos by heuristics (prev word, inflection); multi-word items without a covering group → pos x (surfaces).

**Running the checker on phase1c** (from translation-offline/):
`ANN_DIR=$PWD/phase1c/annotated LINT_DIR=$PWD/phase1c/review node phase1b/scripts/lint.ts`
`ANN_DIR=$PWD/phase1c/annotated node phase1b/scripts/measure.ts coverage phase1c/inputs/cov_heldout.json phase1c/measure/cov_before.json`
(same for `fa phase1c/inputs/fa.json …`, `timing`, `sizes`). IMPORTANT: always set ANN_DIR, otherwise it reads phase1b/annotated
(which holds Phase 1b annotations for 12 of our ids). lint's p1_mistake_* checks compare against Phase 1 mistakes (pilot/generated) — informational.
Coverage in Phase 1b = measure.ts `coverage` rows; verdict correct or correct_with_tip = accepted; denominator = translations
judged correct by hand (rejected rows are read and judged; Phase 1b: 11/(63−3)). measure.ts totals split by level and new_long,
not by batch — split by `batch` from the input file / selection.json.

**Inputs** `phase1c/inputs/` (from selection): `cov_heldout.json` 240 (measure ids: their 3 coverage translations; supp ids:
supp translations #0,#2,#4), `supp_fix.json` 90 (supp ids: #1,#3 — for the §4.5 fix pass), `supp_all.json` 225, `fa.json` 105
wrong (measure ids only). DECISION FOR ORCHESTRATOR: measure ids have no supp translations and supp ids have no wrong/
coverage translations, so the held-out split above keeps "after" coverage honest; FA can only be measured on the 35 measure ids.

## postannot (18.9.2026)
**FLAG id 103**: its Slovak ("O jeho promócii sa hovorí…") does NOT match its English ("He was handed his diploma…"); batch-L annotator annotated
the English only. Excluded from the coverage denominator (3 rows) and from the sample; needs a source fix before production.
`phase1c/annotated/batchS.json` was one-object-per-line without commas → rewritten as valid JSON (raw kept: `phase1c/batchS.raw.json`).

**Mapping (§5)** → `phase1c/mapping_stats.json` (+ `annotated/map_batch{S,L}.json`, ng store `phase1b/synonyms/ng_phase1c.json`, forms rebuilt, 971 groups).
S: 67 alts, 32 → existing groups (47.8 %), 29 new ng = 145 / 100 sent. L: 215 alts, 77 existing (35.8 %), 79 new ng (+5 reused) = 131.7 / 100 sent.
Total 108 distinct ng (135 / 100 sent; pos x 67, n 26, v 14, a 1). L proposes slightly fewer per sentence than S (−9 %) — weak saturation signal only.

**Lint (§4.4)** → `phase1c/lint.json` (raw `phase1c/review/lint.json`). 182 issues = 108 syn_missing_ok_bad (the ng, pending review-syn) + 57 p1_mistake_verdict_changed
(informational) + 17 real. Phase 1b 44 = 27 p1 info + 17. By type 1b→1c: ann_anchor_in_lock 8→2, ann_anchor_not_a_member_form 2→0, compile_note 2→3,
feedback_too_long 0→4 (3084), lib_translated_grammar_name 4→4 (library-wide), mistake_accepted_as_correct 1→2 (4571, 7458), variant_is_freedom_swap 0→2 (10107).

**Coverage BEFORE (§6.1)** → `phase1c/measure_before.json` (raw `phase1c/measure/cov_before.json`, `fa_before.json`). Raw 95/240; denominator 235
(−3 id 103, −2 judged wrong: 1018 "She's poured", 5595 "She's finally stamped" — sk masculine) → **95/235 = 40.4 %** (1b: 18.3 %).
A1 50.0 · A2 45.8 · B1 42.7 · B2 29.0 · long 41.9 (13/31) · short 40.2 · batch S 37.3 · L 41.5. False rejections 140 (139 auto, 1 mistake), each with reason in the file.
**FA**: 9/105 accepted (3 silent `correct`: 14266 variant, 1452 sk genderless, 5595 "at last" dropped — sk has one "Konečne"; 6 correct_with_tip via library soft
items: tense nuance / dropped will). Real = 0 by the 1b convention; 6/105 if tip-accepts count.
Fix split (`inputs/supp_fix.json`, 90) checked now → `phase1c/measure/supp_fix_before.json`: 25 accepted, 65 rejected (all into supp.md).

**Review tasks** (built by `phase1c/scripts/build_review_tasks.py`, manifest `phase1c/tasks/review_manifest.json`; common change schema target syn|lib|ann):
- `tasks/review_syn_1.md` (~19.8 k tok) + `review_syn_2.md` (~2.6 k) → `review/syn_1.json`, `syn_2.json`: 56 existing groups + 108 ng = 164 groups.
- `tasks/review_lib_1.md` … `review_lib_6.md` (~12–20 k tok each, ~107 k total) → `review/lib_1..6.json`: 48 topics, 953 items (SPLIT INTO 6, not 2).
- `tasks/review_sample.md` (~4 k tok) → `review/sample.json`: seed 20260920, ids 7716 25921 (S) · 25981 13034 8293 2955(long) 119 7037 (L).
- `tasks/supp.md` (~9.5 k tok) → `review/supp.json`: 65 rejections R1–R65 in the fix split (step-3 held-out rejections are not in the fix split by design → 0).

**Apply** `python3 phase1c/scripts/apply_reviews.py` (reads review/{syn,lib,sample,supp}*.json incl. parts) → `phase1c/synonyms/` (table/annotator/ng/review_added + forms),
`phase1c/annotated_after/<id>.json`, `phase1c/overlay/library.json`, log `phase1c/review/applied.json` (op counts, supp fix types by type, errors). Never writes phase1b/.
Tooling: `phase1b/scripts/data.ts` now honours `SYN_DIR` (synonym files + forms.json) and `LIB_OVERLAY`; `build_forms.ts` writes to SYN_DIR. Defaults unchanged (before-numbers reproduce).
Tested on a synthetic review set (scratchpad): add_group mist/fog + ann merge on 6884 → 0/3 → 1/3 accepted; remove_group drops the anchor; lib overlay read back; 0 errors.
AFTER: `ANN_DIR=$PWD/phase1c/annotated_after SYN_DIR=$PWD/phase1c/synonyms LIB_OVERLAY=$PWD/phase1c/overlay/library.json node phase1b/scripts/measure.ts coverage phase1c/inputs/cov_heldout.json phase1c/measure/cov_after.json` (same for fa).

## measure (18.9.2026)
**Apply**: `phase1c/scripts/apply_reviews.py` already read split parts; added `norm_irr`: syn review wrote `irr` as `{lemma:{past,pp,ing}}`, FORMAT_SPEC wants
`{lemma:[3sg,past,pp,ing]}` (the dict form made forms.ts emit NO past/pp forms). 19 entries in 12 ng groups normalised → dropped (none had all 4 forms; every
head is in forms.ts' built-in irregular table, same output). 4 apply errors, all harmless no-ops on groups syn already merged/removed (sample ng1c_35/39,
supp ng1c_71; supp ng1c_27 add "were putting together…" not applied → R14 stays rejected). 971 groups (863 table + 88 ng + 20 review_added). phase1b/ untouched.
**Coverage AFTER** → `phase1c/measure_after.json` (script `phase1c/scripts/measure_after.py [norev_dir]`; raw `phase1c/measure/*_after.json`). Same split/denominator
as before: **100/235 = 42.6 %** (before 40.4). A1 47.2 · A2 47.9 · B1 41.5 · B2 37.7 · long 41.9 (13/31) · short 42.6 · batch S 37.3 · L 44.3.
+9 gained, −4 regressions (8756, 20298 via supp lock changes; 11216, 9498 via review-syn merges that dropped "don't like"/"counter" — both valid for the Slovak).
Effect split (held-out): syn+lib+sample alone 94/235 (40.0 %, net −1); + supp → 100. Fix split (IN-SAMPLE, supp saw it): 25/77 → 64/77 correct accepted (83.1 %),
41/52 targeted fixed, 0/13 wrong accepted, 2 regressions (11216, 9498). Still rejected: R1 R2 R10 R14 R20 R31 R32 R36 R41 R42 R58.
**FA**: 9/105, identical rows to before (3 valid readings, 6 tip-accepts) → **0 real**; 6/105 if tip-accepts count. Review-only also 9.
**False rejections** 135, each with category+cause in the file: synonym_missing 37, paraphrase 26, extra_word 16, determiner 12, tense_aspect 11, dropped_word 8,
clause_reorder 5, word_order 4, review_regression 4, gender_pronoun 4, lock_blocks_swap 4 (at the moment→right now inside lock), optional_that 3, library_false_hit 1
(categories auto-derived from checker feedback; primary = first issue).
**Checker fixes recorded, NOT done**: (a) R20 — g chain dropped when "his" is d-swapped to "that"; (b) id 119 — gender swap inside a locked span (sample appended
g [["she"]], ineffective); (c) R2 — `p` cannot insert before a sentence-initial word; (d) optional "that" after said/wishes.
**§6.4**: `phase1c/scripts/timing_all.ts` — all 80 exercises × (real + 600 synthetic answers) × 5 runs = 242,850 checks: mean 0.25 ms, p99 1.16 ms, **max 11.3 ms**
(9038, 80-token junk; warm runs max 9.6). Per-exercise download (`measure/sizes_after.json`): raw mean 3,232 / max 4,639 B; **gzip mean 970 / max 1,329 B**.
**§7 tokens** → `phase1c/tokens.json` (`python3 phase1c/scripts/tokens.py`; re-run at the end, measure+main are partial). METHOD BUG FOUND: Phase 1b's
token_usage.py keeps the FIRST streamed record per message id, whose output_tokens is a stub (7 vs 11,204). tokens.py default = max per field ("corrected");
`--method first` reproduces 1b (`phase1c/tokens_phase1b_method.json`). Only output differs (cache fields identical). Phase 1b's 11,590 is therefore understated;
to compare like for like, re-run phase1b with the corrected method (its session e836e9e1…, no STEP tags).
Corrected: batchS 88,519 (3 calls) · batchL 193,727 (4 calls) → v=(193,727−88,519)/40=2,630.2 · F=88,519−20·2,630.2=35,915 (1b-method: S 77,322, L 165,208, v 2,197, F 33,379).
Startup context ≈10.6 k per subagent; main 73.5 k. review-syn 275,447 (1,680/group) · review-lib 1,015,601 (21,158/topic, 1,066/item) · review-sample 55,201
(6,900/sentence) · supp 115,917 (1,783/rejection, 2,229/fix). prep 4.11 M, postannot 2.04 M. Total so far 10.60 M (cache read 90.1 %).
