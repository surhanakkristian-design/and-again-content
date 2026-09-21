# Translation production — Phase 2K report (21.9.2026)

Working directory: `~/Projects/and-again-content/translation-offline/phase2k/` (below: `P2K/`).
Brief + stage plan: `P2K/BRIEF_2K.md`. Stage log: `P2K/PROGRESS.md`.

## 0. Headline: Czech was NOT measured

The SAFETY STOP in Part 3 fired: pooled SOURCE-ONLY FA on the two closed Slovak sets = 73/805 = **9.07 %** [7.18, 11.27] > 8.0 %
(`P2K/STOP_part3.md`). Following the brief, Parts 4 and 5 did not run: no Czech checker was assembled, no Czech set was
written or judged, no headless Claude session was started, and no Czech upload file was written. **0 Claude tokens were spent on Czech.**

| Czech target | point | 95 % CP interval |
|---|---|---|
| coverage >= 90 % | NOT MEASURED | NOT MEASURED |
| FA < 5 % | NOT MEASURED | NOT MEASURED |

## 1. Part 3 — Slovak closed-set re-score, SOURCE-ONLY beside the reference-based stacks

**This is a closed-set, in-sample re-score**, not a fresh measurement: the 2I set (900 items) and the 2J Part D set (900 items)
with their EXISTING judge labels; no new writers, no new judges. Both sets were seen while the reference-based stacks were built,
and the SOURCE-ONLY prompt was written after reading their failures, so these numbers are optimistic.
Stack = frozen S1 SOURCE-ONLY (`P2K/stack_source.py`, freeze commit e394bc2, `P2K/FROZEN_SHA_S1.txt`), gemini-3.1-flash-lite,
temperature 0, thinkingBudget 0, SAME/TIP/DIFF, TIP-as-rejection ON. Reference-based column = the stored per-item results of the
2I translation-only stack (`phase2i/run/results.jsonl`, stack tonly) and the 2J fixed stack (`phase2j/partD/run/results.jsonl`),
reproduced exactly (2I 89.13 % / 4.71 %, 2J 90.36 % / 5.97 %). Full tables and all 182 changed items: `P2K/analysis/part3.md`, `P2K/analysis/part3.json`.

Exact 95 % Clopper-Pearson:

| set | level | coverage ref-based | coverage SOURCE-ONLY | FA ref-based | FA SOURCE-ONLY |
|---|---|---|---|---|---|
| 2I | all | 443/497 = 89.13 % [86.06, 91.73] | 477/497 = 95.98 % [93.85, 97.52] | 19/403 = 4.71 % [2.86, 7.26] | 37/403 = 9.18 % [6.55, 12.43] |
| 2I | A1 | 120/124 = 96.77 % [91.95, 99.11] | 116/124 = 93.55 % [87.68, 97.17] | 2/101 = 1.98 % [0.24, 6.97] | 3/101 = 2.97 % [0.62, 8.44] |
| 2I | A2 | 117/125 = 93.60 % [87.78, 97.20] | 119/125 = 95.20 % [89.85, 98.22] | 8/100 = 8.00 % [3.52, 15.16] | 8/100 = 8.00 % [3.52, 15.16] |
| 2I | B1 | 103/123 = 83.74 % [76.01, 89.78] | 117/123 = 95.12 % [89.68, 98.19] | 6/102 = 5.88 % [2.19, 12.36] | 14/102 = 13.73 % [7.71, 21.96] |
| 2I | B2 | 103/125 = 82.40 % [74.57, 88.63] | 125/125 = 100.00 % [97.09, 100.00] | 3/100 = 3.00 % [0.62, 8.52] | 12/100 = 12.00 % [6.36, 20.02] |
| 2J | all | 450/498 = 90.36 % [87.42, 92.81] | 474/498 = 95.18 % [92.91, 96.89] | 24/402 = 5.97 % [3.86, 8.75] | 36/402 = 8.96 % [6.35, 12.18] |
| 2J | A1 | 109/124 = 87.90 % [80.83, 93.07] | 115/124 = 92.74 % [86.67, 96.63] | 3/101 = 2.97 % [0.62, 8.44] | 4/101 = 3.96 % [1.09, 9.83] |
| 2J | A2 | 119/125 = 95.20 % [89.85, 98.22] | 121/125 = 96.80 % [92.01, 99.12] | 7/100 = 7.00 % [2.86, 13.89] | 8/100 = 8.00 % [3.52, 15.16] |
| 2J | B1 | 103/124 = 83.06 % [75.28, 89.20] | 120/124 = 96.77 % [91.95, 99.11] | 7/101 = 6.93 % [2.83, 13.76] | 11/101 = 10.89 % [5.56, 18.65] |
| 2J | B2 | 119/125 = 95.20 % [89.85, 98.22] | 118/125 = 94.40 % [88.80, 97.72] | 7/100 = 7.00 % [2.86, 13.89] | 13/100 = 13.00 % [7.11, 21.20] |
| pooled | all | 893/995 = 89.75 % [87.69, 91.56] | **951/995 = 95.58 % [94.11, 96.77]** | 43/805 = 5.34 % [3.89, 7.13] | **73/805 = 9.07 % [7.18, 11.27]** |
| pooled | A1 | 229/248 = 92.34 % [88.29, 95.32] | 231/248 = 93.15 % [89.25, 95.96] | 5/202 = 2.48 % [0.81, 5.68] | 7/202 = 3.47 % [1.40, 7.01] |
| pooled | A2 | 236/250 = 94.40 % [90.78, 96.90] | 240/250 = 96.00 % [92.77, 98.07] | 15/200 = 7.50 % [4.26, 12.07] | 16/200 = 8.00 % [4.64, 12.67] |
| pooled | B1 | 206/247 = 83.40 % [78.16, 87.82] | 237/247 = 95.95 % [92.68, 98.04] | 13/203 = 6.40 % [3.45, 10.70] | 25/203 = 12.32 % [8.13, 17.64] |
| pooled | B2 | 222/250 = 88.80 % [84.22, 92.43] | 243/250 = 97.20 % [94.32, 98.87] | 10/200 = 5.00 % [2.42, 9.00] | 25/200 = 12.50 % [8.26, 17.90] |

Pooled SOURCE-ONLY against the targets (closed set): coverage MET on the point and the interval; FA MISSED on the point and the interval.

**Reference-caused rejections:** all **25 of 25** of 2J's "reference wrong or too narrow" false rejections
(`phase2j/analysis/ANALYSIS.md`) are now accepted.

**What moved (182 changed verdicts):**

| set | FR removed | FR added | FA removed | FA added |
|---|---|---|---|---|
| 2I | 51 | 17 | 7 | 25 |
| 2J | 40 | 16 | 7 | 19 |
| pooled | 91 | 33 | 14 | 44 |

Net: coverage +58 items, FA +30 items. FA added by writer type: **M 35**, T 5, S 3, W 1 — the M (meaning / missing-word) items dominate.
FA removed (14): source-only L3 returned TIP (11) or DIFF (3) where the reference-based L3 had said SAME.
FR added (33): source-only L3 TIP where the reference-based L3 said SAME (20), DIFF where it said SAME (11), the source-only AG
firing without reference alignment (1, 2I A:262:c2), and one answer identical to the reference (2I A:1330:c1 "This is the heaviest
dictionary in the world!") that the removed L1 accept used to pass and L3 now calls DIFF.

**What drives the FA rise.** The 44 added FAs are overwhelmingly answers that DROP a content word or phrase the source carries —
adjectives, nouns and place phrases that the §1.1 ruling explicitly calls WRONG to drop, e.g. "A mushroom grows…" (Veľká huba),
"…the gavel came down" (obrovské kladivko), "These seats are completely empty!" (vzadu), "…had the pages laminated" (sprievodcu),
"…had been sent an hour before" (z laboratória), "He used to be a student, but…" (tu). Mechanically:
- 9 were caught before by removed deterministic reference layers: F3 deletion 6, F5 adjunct deletion 3;
- 3 by the reference-reading AG, 2 by F4v2 on the reference-based path;
- 30 by the reference-based L3 (DIFF 19 / TIP 11) — with the reference in the prompt the omission was visible as a diff; judging against
  the Slovak alone, flash-lite calls the same answer SAME.
The §1.1 ruling was in the L3 system text (`P2K/spec/l3_system_sk.txt`) throughout, so writing the rule down did not make the
model enforce it: the reference layers (F3/F5 and the reference comparison inside L3) were doing the dropped-content-word catching.

**Czech false rejections / false acceptances by cause:** not available (Part 5 not run).

## 2. Part 1 — close Slovak

**1.1 Ruling, verbatim** (in `P2K/spec/judge_prompt_{sk,cz}.txt`, `writer_template_{sk,cz}.txt`, `l3_system_{sk,cz}.txt`; asserted
equal to the brief text by test T10):

> Dropping a word is judged by its KIND. ACCEPTABLE to drop: time adverbs, degree adverbs and interjections — now, today, already,
> still, finally, then, totally, completely, just, Look! (Slovak: teraz, dnes, už, ešte, konečne, vtedy, úplne, práve, Pozri!; Czech:
> teď, dnes, už, ještě, konečně, tehdy, úplně, právě, Podívej!). WRONG to drop: nouns, adjectives, main verbs, and place or direction
> phrases — hot, in the room, off the plant. The owner's reason: where even the model does not treat it as a serious error, it is not
> counted as one.

**1.2 The 4 truncated references restored** to their pre-B3 value from `phase2i/upload` (`P2K/upload/RESTORE_4.json`; v[0] and en):

| exercise_id | B3 (truncated) | restored |
|---|---|---|
| 927 | "…before a." | "…before a trust fall." |
| 22385 | "…in front of." | "…in front of the happy man." |
| 35040 | "He shares his ice cream with." | "He shares his ice cream with his friend." |
| 41408 | "…slumped onto desk." | "…slumped onto her desk." |

Reference-ending test (`P2K/build_upload.py` scan_endings, test T8) over the final SK file and the CZ file from `phase2i/upload`.
**Split decision (flagged for the owner to overrule):** the asserted STRICT list (articles + of/onto/into/upon/among/between/beneath/
via/despite/during/than/toward(s)/to/from/with/at/by) has **2 hits**, both ex 4146 (SK + CZ) "…every move she is thinking of." — a
legitimate stranded preposition, recorded as a reviewed exception in `P2K/analysis/ref_endings_reviewed.json`; T8 fails on any other
strict hit. The looser list (particles / stranded prepositions: up, in, on, for, before, over, out …) has **219 hits** (SK 117, CZ 102),
all listed in `P2K/analysis/ref_endings.json` but NOT asserted, because they are mostly complete sentences ("the day before",
"It's over", "what the room is for"). If the owner wants the brief's "ending in a preposition" read literally, those 219 need review.

**1.3 Final Slovak file:** `P2K/upload/upload_sk_final.xlsx` (sheet `sk`) + `annotations_sk_final.jsonl` + `UPLOAD_README.md`:
4,064 rows, `exercise_id` integer, `v[0] == en` on every row (T9); the README states that `v` is display-only and no longer grades.

## 3. Part 2 — SOURCE-ONLY stack and every removed layer

`P2K/stack_source.py`: AG -> F4v2 -> F4v3 (source-side guards) pre-L3; everything else goes to L3 with ONLY {language, source,
answer}; SAME accept, TIP reject, DIFF reject. Test T6 feeds poison `v/alt/lk/en` objects that raise on access and asserts no
reference string appears in any L3 body (13/13 PASS, `P2K/test_2k_output.txt`, re-run `test_2k_output_S2.txt`).
Full grep with line numbers: `P2K/analysis/REMOVED_LAYERS_GREP.md`.

| removed layer | file:line (2J stack) | reads |
|---|---|---|
| L1 exact-reference accept | phase1i/checker_1i.py:822-824 (route: phase2j/tonly/lib_prev.py:121-124) | v / refs |
| F3 deletion | phase1i/checker_1i.py:799-803 | reference |
| F5 adjunct deletion / subsequence | phase1i/checker_1i.py:804-809 (_subseq_positions :669, loop :719) | v |
| L2 mistake / F1 / F2 + LOCKTIP | phase1i/checker_1i.py:827-840, 299-300, 319-372; phase1k/runner_1k.py:248-268 | lk (already stripped in 2I) |
| L3 verdict map | phase1i/checker_1i.py:841-850 (replaced by stack_source.finish) | — |
| F2B | phase1i/checker_1i.py:851-858 (f2_boundary_violation :773-795; en_span_tokens :1548-1568) | alt |
| reference-based L3 body | phase2j/tonly/lib_prev.py:223 ("same as the reference"), :230 ("Reference English:") + GROUND/WORDING/VOICE/lever/ARTICLE lines | reference, v[0] |
| record reference=v[0], refs=v | phase2j/tonly/runner_1p.py build_side (:153) | v |
| AGv5 refsubj rs_nom | phase1v/trackA_loop/stack_1v.py:43-99 (call :99), final_accept :137-144 | reference |
| TIPdet rule | phase1v/trackA_loop/stack_1v.py:122-134, applied :144 | reference |
| AG v4 clause alignment | runner_1u ag_map_1u -> agent_drop_v4.py:290 -> agent_drop_v3.py:386 / :442 / **:269 split_en(reference)** | reference |

**AG read the reference** on every call (poison probe: 900/900 reads per set, at `agent_drop_v3.py:269` split_en). Removed: AG is now
`stack_1w.decide` with `reference=''`, `extra=()`, annotation stripped of v/alt/en/lk*/headword/rewrite. Effect vs the 2J stack's own AG
on the same items: 8 disagreements on the 2I set (892/900 agree) and 5 on the 2J set (895/900); in Part 3 this gave 3 FAs added, 2 FRs
removed and 1 FR added (`P2K/analysis/s1_prep.json` ag_disagree, `part3.md`).
**F4v2/F4v3** (2J-fixed via f4fix.build_fixed_v3) read only {sk, answer}: no reference read (PoisonDict, 0 errors on 1,800 items).
F4v3 moved pre-L3 (label-only effect). Both F4 guards fired 0 times on either set.

## 4. Part 4 — Czech stack and gold validation: NOT RUN

Stopped by the Part 3 safety stop. No Czech reader / f4fix cz binding, no Czech tests, no 1T gold validation. `run_2k.py --lang cz`
is still REFUSED by design; only the Czech L3 text (`P2K/spec/l3_system_cz.txt`) exists.

## 5. Czech upload file: NOT WRITTEN

`P2K/upload/upload_cz_final.xlsx` does not exist. The CZ file in `phase2i/upload` was only scanned by the ending test (Part 1).

## 6. Gemini calls and spend

1,788 counted calls of the 3,000 cap (S1 0, S2_2i 896, S2_2j 892; `P2K/GEMINI_LEDGER.json`), 0 uncounted attempts, 0 rate-limit
retries needed; spend **$0.1816** of $1.00.

## 7. Claude tokens against 2,200,000

| stage | agent (harness) | headless |
|---|---|---|
| S1 setup + Part 1 + Part 2 | 201,462 | 0 |
| S2 Part 3 | 56,806 | 0 |
| S6 report agent | ~75,000 (estimate) | 0 |
| orchestrator | ~60,000 (estimate) | 0 |
| **total** | **~393,000 (17.9 % of budget)** | **0** |

Note: `P2K/TOKENS.jsonl` holds the agents' own pre-harness estimates (S1 350,000, S2 90,000); the harness counts above supersede them.

## 8. Judge noise

No new judging in this phase: Part 3 reused the existing 2I and 2J judge labels, so no new duplicate-agreement measurement exists.
The noise of those labels is as reported in 2I/2J.

## 9. Defects recorded, not fixed

1. SOURCE-ONLY lets dropped content words through (44 FA added, 35 of them M items) — the §1.1 ruling in the prompt does not enforce itself.
2. SOURCE-ONLY adds 33 FRs (L3 TIP/DIFF where the reference-based L3 said SAME), incl. an answer identical to the stored reference (2I A:1330:c1) now rejected.
3. The judge prompt (`P2K/spec/judge_prompt_{sk,cz}.txt`) still has the older line "a dropped function word is correct, a dropped content word is wrong" before the ruling (consistent, but redundant); relevant only when Czech judging runs.
4. The reference-ending test asserts only the strict list; 219 looser hits in `P2K/analysis/ref_endings.json` are unreviewed.
5. The Czech checker has still never been assembled or run (2J §3 A5 remains open).
6. Part 3 is in-sample: the SOURCE-ONLY prompt was written after reading these sets' failures.

## 10. Judgement

1. Judging against the source removes the reference-caused rejections (25/25 of 2J's accepted; pooled closed-set coverage 95.58 %).
2. But without the reference layers it lets dropped content words through: pooled FA 9.07 % [7.18, 11.27], so as specified it does not work yet.
3. Czech was not measured; neither Czech target has a number.
4. The Slovak file `P2K/upload/upload_sk_final.xlsx` is fit to upload as DISPLAY data (`v` display-only, 4 truncations repaired); grading should not switch to SOURCE-ONLY until a source-side dropped-content guard exists.
5. Owner's options: (a) build a deterministic source-side content-word guard (Slovak noun/adjective/place-phrase coverage check) and re-score, (b) accept ~9 % FA for the coverage gain, or (c) keep the reference-based 2J stack for grading and use SOURCE-ONLY only as a second opinion on reference-caused rejections.
