# Task: checker v2 + tooling (Opus). Budget: at most ~35 tool calls.
Read: phase1b/FORMAT_SPEC.md (authoritative), ../checker/offlineCheck.ts, ../checker/typedAnswer.ts, ../checker/slots.ts,
../checker/offlineCheck.test.ts (skim), ../scripts/build_pilot.ts, ../scripts/run_measurements.ts,
~/Projects/and-again/supabase/migrations/20260917160000_translation_offline_check.sql, ../measurements/bench_comparison.json (shape only).
Phase 1 files stay untouched (import their helpers). Node runs .ts directly (type stripping), tests with `node --test`.
The real data (synonyms/table.json, mistakes/*.json, annotated/*.json) is being written by other agents IN PARALLEL — do not
wait for it; build against the spec and synthetic fixtures; every script must work on whatever files exist.

Deliverables (all new files):
1. `../checker/v2/match.ts` — compile(annotation, synForms, library) → per variant a slot graph: plain tokens; contextual-synonym
   slots (same form of every member, forms from synonyms/forms.json); safe groups applied everywhere outside locked spans
   (multi-word members too); gender chains (run the match once per gender assignment so a chain flips consistently);
   `o` alternatives; determiner slots (codes A/P/Z or explicit, ∅ allowed where listed, a≡an); optional words (+w anywhere
   outside the lock, +w@anchor, -anchor). Locked tokens are literal. Mistake patterns = the variant with the lock (or
   anchor) replaced by the wrong text, compiled with the same freedoms. Match = DP over the slot graph; readings from the
   Phase 1 normalisation (contractions, numbers, 's) are each tried. Also a weighted-edit DP (insert/delete/substitute cost 1)
   that returns the closest path and the aligned differences.
2. `../checker/v2/check.ts` — check(answer, compiled, {native, level}) → {verdict, step, feedback, unmatched, closest}.
   Steps exactly as FORMAT_SPEC §4 (keep Phase 1 BrE/AmE step, typo rule with the real-word and word-form exclusions via
   ../wordlist/en_words.txt or a per-exercise neighbour list, Phase 1 §3.2 normalisation additions, Phase 1 tip templates
   and language rules, 150-char cap). Library feedback: fill {right}/{wrong} from the matched variant/answer + per-sentence
   slots. The automatic tip is built from the closest path INCLUDING all freedoms, so it never says "write X instead of Y"
   when X is allowed there.
3. `scripts/build_forms.ts` — synonyms/*.json (except forms.json) → synonyms/forms.json: per group, per form tag, the surface
   strings of every member. Regular forms by rule (verbs: -s/-es/-ies, -ed with doubling/-e/-y rules, -ing; nouns: plural;
   adjectives: -er/-est) KEPT ONLY IF in ../wordlist/en_words.txt (log dropped ones to synonyms/forms_dropped.txt), irregular
   forms from the group's `irr`; include a built-in irregular-verb table (~150 common A1–B2 verbs) as fallback.
4. `scripts/merge_batches.ts` — annotated/batch_*.json (JSON arrays) → annotated/<id>.json (one per sentence); move `ng`
   groups into synonyms/annotator.json with ids `ng_<exercise>_<k>` and rewrite the `s` references. Idempotent.
5. `scripts/lint.ts` — the lint gate (no tokens): required keys; v[0] == reference from selection/all230.json; ≤4 variants;
   lk found in each variant; anchors found in ≥1 variant, not inside a lock; group ids exist and the anchor is a form of a
   member; g anchors are personal/possessive pronouns; d/o values valid; library ids exist for that topic and extra slots
   supplied; filled feedback ≤150 chars; no mistake pattern is accepted as correct by the sentence's own matcher; no variant is
   accepted by another variant's matcher (i.e. it is a mere freedom swap); every Phase 1 stored mistake of that exercise
   (../pilot/generated/<id>.json, expanded with ../checker/slots.ts) still gets its Phase 1 verdict; library file checks
   (≤150 chars with long plausible fills, no praise words, gendered-form list from Phase 1 lint). Output review/lint.json +
   one summary line per error class.
6. `scripts/measure.ts` with subcommands:
   `coverage <translations.json> <out.json>` (input [{exercise_id, translations:[...]}] or items [{text}]; native sk; writes
   verdict/step/feedback/closest per answer and totals by level and new_long flag from selection/all230.json);
   `fa <fa_translations.json> <out.json>` (same, reports accepted ones); `regression <out.json>` (the 20 bench answers of
   ../measurements/bench_comparison.json and every Phase 1 stored mistake expansion vs its Phase 1 verdict; list changes);
   `timing <out.json>` (most complex compiled sentence: 2,000 answers incl. adversarial long/near-miss ones; max and p99 ms);
   `sizes <out.json>` (bytes raw+gzip of table, forms, library all/per topic, annotation per sentence mean/max, and per-exercise
   download = annotation + its applicable library items in ONE language + forms of referenced groups + typo neighbour list).
7. `../checker/v2/v2.test.ts` — unit tests with SYNTHETIC fixtures for: every annotation type (s, g, o, d codes+explicit, +w,
   +w@, -w), lock (no freedom and no safe synonym inside), inflection (lift→raised ok for lifted; "raise" for "lifted" rejected;
   irregular), safe multi-word, typo exclusions (real word, word form), library slots + language rules (sk/cz/en B, null A) +
   150 cap, auto tip never names an allowed alternative, BrE/AmE, mistake beats step 4. Run; save output to measure/test_output.txt.
8. `~/Projects/and-again/supabase/migrations/20260918120000_translation_offline_check_v2.sql` — PROPOSAL, NOT APPLIED (say so
   in the header). Supersedes the Phase 1 proposal: global synonym groups table (kind, pos, members, irregular forms, ok/bad
   examples), per-topic mistake library (verdict, pattern, slots, feedback per language), per-exercise annotation jsonb +
   content_version, keep Phase 1's unmatched-answer log. RLS read-only for authenticated like Phase 1. Do not apply.
9. `phase1b/README.md` — file map + how to run.
Final message ≤4 lines: files, test pass/fail count, anything that doesn't meet the spec.
