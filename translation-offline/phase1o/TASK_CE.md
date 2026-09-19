# Phase 1O — Task C (false rejections by cause) and Task E (reference quality)

Diagnosis only. 0 model calls, no network, no git, nothing under `phase1n/` or `phase1m/` changed (size + mtime snapshot before/after: identical). Intervals are exact Clopper-Pearson 95 %; bootstrap intervals resample SENTENCES (clusters), 600 draws, seed 1505.
Scripts: `phase1o/diag/ce_build.py` (per-item layer rebuild through the frozen stack with stored verdicts; reproduces 350/426 and 547/614 and both `fr_ids` lists exactly), `ce_analyse.py`, `ce_extra.py`. Data: `phase1o/diag/ce_dump.json`, `ce_numbers.json`, per-item table `phase1o/taskCE_items.json` (143 rows).

## 0. The bad news first

1. **The like-for-like gap is larger than the headline, not smaller.** 1M's 67 false rejections contain 32 it-clefts / pseudo-clefts ("It was her who ...") — writer-V items that the 1M judge called correct; clefts were accepted 9/41. 1N has no V writer class (1 cleft in 426). Without passives and clefts: **1M 536/571 = 93.87 % [91.58, 95.69] vs 1N 266/320 = 83.12 % [78.56, 87.06] — 10.75 points**, against 6.93 on the headline. Writer-C, non-passive only: 529/558 = 94.80 % vs 254/294 = 86.39 % (8.41 points).
2. **Distance to the reference does not explain it.** Re-weighting the distance mix explains about 1 point (0.94 [-0.17, 2.06] on non-passive non-cleft; 1.17 [0.02, 2.54] on all items). Coverage differs WITHIN bins, worst for answers CLOSE to the reference: distance (0, 0.2] 1M 183/205 = 89.27 % [84.20, 93.15] vs 1N 91/125 = 72.80 % [64.12, 80.37]. Adding the determiner swap as a second composition axis lifts the explained part to 2.24 points [0.17, 4.83] (0.8 to 3.7 depending on direction). At least ~7 of the 10.75 like-for-like points stay unexplained by anything measurable offline.
3. **The same kind of answer fares worse in 1N.** Answers whose only difference to the nearest stored variant is a determiner: 1M 51/56 = 91.07 % [80.38, 97.04], 1N 25/35 = 71.43 % [53.70, 85.36]. The prompt differs between the sets (P-FROZEN vs P-FROZEN-1N); the 120 probe items re-asked under the new prompt are all W-kind 1M items (18 judged correct, 16 of them clefts), so the ledger cannot say whether the new prompt is stricter on determiners. **Cannot be determined with zero calls.**
4. **The reference is a small lever.** E1 (reference carries content the Slovak lacks) is 3 of 76 in 1N and 0 of 67 in 1M. Ceilings: (a) +1 to +3, (b) +2 to +18, (c) +9 to +21 items; the optimistic UNION of all three is +28 = 88.73 % [85.34, 91.57], still under 90 % at the point.
5. **11 of 1N's 76 false rejections (14.5 %) are E4** — the answer is arguably wrong and the judge was generous (writer-T/TF/M/W items passed by the judge); 4 in 1M. 21 more are passives that none of the three reference levers touches.

## TASK C

### C.0 Buckets (same for both sets)
Layer as recorded. Cause (exclusive, primary difference to the nearest stored variant after alt-normalisation): DET (that/those -> the, a/the, number of a plurale tantum), TENSE (tense/aspect choice inside the right frame, incl. will / going to, no backshift, conditional type), PASS_AGENTLESS, PASS_BY, CLEFT (it-cleft, pseudo-cleft), LEX (synonym / preposition), STRUCT (reordering, impersonal or passive Slovak re-rendered, neg-raising), DROP (dropped or added minor element). No item needed OTHER.

### C.1 Cause x layer, rates of judged-correct (counts in brackets)

| cause | 1M all /614 | 1N all /426 | 1M non-passive /611 | 1N non-passive /321 | 1M non-pass non-cleft /571 | 1N non-pass non-cleft /320 | layers 1M | layers 1N |
|---|---|---|---|---|---|---|---|---|
| DET | 0.33 % (2) | 3.52 % (15) | 0.33 % | 4.67 % | 0.35 % [0.04, 1.26] | 4.69 % [2.65, 7.61] | L3 1, TIPrej 1 | L3 11, TIPrej 4 |
| TENSE | 1.95 % (12) | 2.11 % (9) | 1.96 % | 2.80 % | 2.10 % [1.09, 3.64] | 2.81 % [1.29, 5.27] | L3 5, TIPrej 4, F2B 3 | L3 4, TIPrej 4, F2B 1 |
| PASS_AGENTLESS | 0 | 3.76 % (16) | 0 | 0 | 0 | 0 | — | L3 14, F4v2 2 |
| PASS_BY | 0 | 1.17 % (5) | 0 | 0 | 0 | 0 | — | F4v2 5 |
| CLEFT | 5.21 % (32) | 0.23 % (1) | 5.24 % | 0.31 % | 0 | 0 | L3 17, TIPrej 3, F4v2 9, F8 3 | L3 1 |
| LEX | 1.47 % (9) | 2.11 % (9) | 1.47 % | 2.80 % | 1.58 % [0.72, 2.97] | 2.81 % [1.29, 5.27] | L3 1, TIPrej 7, F8 1 | L3 4, TIPrej 5 |
| STRUCT | 0.81 % (5) | 1.64 % (7) | 0.82 % | 2.18 % | 0.88 % [0.28, 2.03] | 2.19 % [0.88, 4.45] | L3 2, TIPrej 2, F8 1 | L3 5, TIPrej 2 |
| DROP | 1.14 % (7) | 3.29 % (14) | 1.15 % | 4.36 % | 1.23 % [0.49, 2.51] | 4.38 % [2.41, 7.23] | L3 1, F5 5, F8 1 | TIPrej 1, F5 13 |
| **total FR** | 10.91 % (67) | 17.84 % (76) | 10.97 % (67) | 17.13 % (55) | 6.13 % (35) | 16.88 % (54) | | |

By layer, non-passive non-cleft: L3 DIFF 1M 10/571 = 1.75 % [0.84, 3.20] vs 1N 24/320 = 7.50 % [4.86, 10.95]; L3:TIPrej 2.45 % [1.35, 4.08] vs 5.00 % [2.88, 7.99]; F5 0.88 % [0.28, 2.03] vs 4.06 % [2.18, 6.85]; F2B 0.53 % vs 0.31 %; F8 0.53 % vs 0 (removed); F4v2 0 vs 0 (F4v2 fires only on clefts in 1M and only on passives in 1N).
The 1M "non-passive" flag is a regex (3 items); 1N uses the writer/judge tags.

### C.2 Answer 1 — why L3's own false-rejection rate doubled (27/614 = 4.40 % -> 39/426 = 9.15 %)
The doubling hides a swap of classes. 1M's 27: CLEFT 17, TENSE 5, STRUCT 2, DET 1, LEX 1, DROP 1. 1N's 39: PASS_AGENTLESS 14, DET 11, STRUCT 5, TENSE 4, LEX 4, CLEFT 1. Contribution to the +4.75 points (rate 1N minus rate 1M, all-item denominators): agentless passive +3.29, DET +2.42, STRUCT +0.85, LEX +0.78, TENSE +0.12, DROP -0.16, CLEFT -2.53.
On NON-PASSIVE items: 27/611 = 4.42 % -> 25/321 = 7.79 %. On non-passive non-cleft items the rate more than quadruples, **10/571 = 1.75 % [0.84, 3.20] -> 24/320 = 7.50 % [4.86, 10.95]**, intervals disjoint. DET alone: 1/571 = 0.18 % [0.00, 0.97] -> 11/320 = 3.44 % [1.73, 6.07]. Everything except DET: 9/571 = 1.58 % [0.72, 2.97] -> 13/320 = 4.06 % [2.18, 6.85].
What DET is: Slovak `ten / tie / tú` rendered "the" where the first stored reference says "that / those" (12 items, 7 of them with NO other difference, e.g. "Dad carried the old magazines up to the attic" -> DIFF), plus `hodiny` (plurale tantum) rendered "clock" (3 DET items + 1 STRUCT). Exposure: 1N's judged-correct answers drop a reference demonstrative in 137/320 = 42.8 % of non-passive non-cleft items, 1M's in 57/571 = 10.0 % (Slovak demonstrative present in 72/100 vs 73/140 sentences). Acceptance with the swap: 1N 105/137 = 76.64 % [68.66, 83.44], 1M 52/57 = 91.23 % [80.70, 97.09]; without it 87.98 % [82.37, 92.31] vs 94.16 % [91.77, 96.03]. So 1N has four times the exposure AND a lower rate at equal exposure. Model layer alone (non-passive non-cleft items that reached L3): SAME 1M 430/457 = 94.09 % [91.52, 96.07], 1N 233/274 = 85.04 % [80.25, 89.04]; excluding every determiner-swap item 94.51 % [91.81, 96.53] vs 88.08 % [81.82, 92.78].

### C.3 Answer 2 — why F5 roughly quadrupled (5/614 = 0.81 % -> 13/426 = 3.05 %; non-passive non-cleft 0.88 % -> 4.06 %)
What F5 checks (from the docstrings of `phase1i/taskC/guards_c.py`, surfaced through the import; F5's own body sits in `phase1i/checker_1i.py`, outside the directories this task may read): F5 fires only when the answer is a pure order-preserving SUBSEQUENCE of an accepted rendering (optional tokens stripped) and the deleted span carries information (`span_information`); one substituted word anywhere makes it abstain. It runs before the model, so a fired F5 never reaches L3.
What the 13 have in common: all are cause DROP, all are a stored variant minus 1–5 tokens. Deleted spans: "to us" x3 (`nám` in reporting frames: confirmed / explained / claimed to us), "up" / "all the way (up)" x2, "out", "sheet of", "right now", "already", "only", "parquet" x2 (one also "straight"), "in the". 9 are writer-C, **4 are writer-M items** (deliberately missing element, judged correct by the 1N judge); 1M's judged-correct set contains no M item at all (1M judged-correct intents: C 559, V 44, S 4, TF 3, T 4; 1N: C 399, W 7, T 7, M 5, TF 5, S 3). By E bucket: E1 3, E5b 5 (minor Slovak element omitted; judge tolerates, F5 does not), E4 3, E2 1, E5a 1. 1M's five: "back", "played", "number", "reading" (a stored alt), "tower".
Exposure did not rise: answers that are a pure token subsequence of a stored variant are 21/614 = 3.4 % in 1M and 13/426 = 3.1 % in 1N (own proxy; it misses 6 of 1N's 13 and 1 of 1M's 5 because F5 also strips optional tokens). The firing rate rose: 4/21 = 19.05 % [5.45, 41.91] vs 7/13 = 53.85 % [25.13, 80.78]. 1N's deletions are content-bearing (pronoun objects, adverbs, a noun), 1M's exposed answers mostly dropped optional material.

### C.4 Answer 3 — do 1N's judged-correct answers differ from 1M's?
All judged-correct items; distance = token Levenshtein to the NEAREST stored variant after alt-normalisation and contraction expansion, divided by the longer length. "Absent content" = answer tokens outside a function-word list and (crudely stemmed) not in the nearest variant. Structural-paraphrase proxy = distance >= 0.35 OR voice mismatch (regex) OR first two tokens differ. Mean | median; difference of means 1N - 1M with bootstrap interval.

| metric | 1M all (614) | 1N all (426) | diff | 1M non-pass non-cleft (571) | 1N non-pass non-cleft (320) | diff |
|---|---|---|---|---|---|---|
| tokens | 11.29 / 11 | 12.55 / 12 | +1.26 [+0.68, +1.81] | 11.11 / 11 | 12.06 / 12 | +0.96 [+0.40, +1.51] |
| distance | 0.168 / 0.111 | 0.275 / 0.214 | +0.107 [+0.083, +0.132] | 0.158 / 0.100 | 0.183 / 0.138 | +0.024 [-0.002, +0.054] |
| token edits | 1.97 / 1 | 3.61 / 3 | +1.65 [+1.35, +1.93] | 1.82 / 1 | 2.28 / 2 | +0.46 [+0.10, +0.78] |
| absent content words | 0.37 / 0 | 0.48 / 0 | +0.11 [+0.01, +0.21] | 0.40 / 0 | 0.47 / 0 | +0.07 [-0.02, +0.18] |
| structural proxy | 31.9 % | 45.1 % | +13.1 [+8.6, +18.6] | 27.0 % | 27.2 % | +0.2 [-6.2, +7.2] |
| distance >= 0.35 | 13.8 % | 34.5 % | +20.7 [+15.9, +25.4] | 13.5 % | 14.7 % | +1.2 [-4.1, +6.3] |
| L1 match | 17.9 % | 7.7 % | -10.2 [-13.7, -6.7] | 19.1 % | 10.3 % | -8.8 [-12.8, -4.5] |

Builder figure asked for: writer-C items on the exact `match` path — 1M 110/560 = 19.6 %, 1N 33/400 = 8.25 %. So yes, 1M's correct answers sat closer to the reference by construction; but once passives are set aside the difference is small (median distance 0.100 vs 0.138) and it is NOT where the coverage goes.

Acceptance by distance bin, non-passive non-cleft (mix % | accepted):

| bin | 1M mix | 1M accepted | 1N mix | 1N accepted |
|---|---|---|---|---|
| d = 0 | 35.6 % | 200/203 = 98.52 % [95.74, 99.69] | 26.9 % | 82/86 = 95.35 % [88.52, 98.72] |
| (0, .1] | 17.5 % | 91/100 = 91.00 % [83.60, 95.80] | 17.5 % | 41/56 = 73.21 % [59.70, 84.17] |
| (.1, .2] | 18.4 % | 92/105 = 87.62 % [79.76, 93.24] | 21.6 % | 50/69 = 72.46 % [60.38, 82.54] |
| (.2, .3] | 11.4 % | 61/65 = 93.85 % [84.99, 98.30] | 15.9 % | 44/51 = 86.27 % [73.74, 94.30] |
| (.3, .45] | 8.2 % | 44/47 = 93.62 % [82.46, 98.66] | 7.8 % | 22/25 = 88.00 % [68.78, 97.45] |
| > .45 | 8.9 % | 48/51 = 94.12 % [83.76, 98.77] | 10.3 % | 27/33 = 81.82 % [64.54, 93.02] |

Decomposition (A = 1N's bin rates at 1M's mix; B = 1M's bin rates at 1N's mix):

| subset | gap | composition A / B | composition, bootstrap | within-bin, bootstrap |
|---|---|---|---|---|
| all items | 6.93 | 1.57 / 0.71 | 1.17 [0.02, 2.54] | 5.93 [1.16, 10.73] |
| non-passive | 6.17 | 1.31 / 0.55 | 0.93 [-0.20, 2.21] | 4.88 [-0.16, 9.80] |
| non-passive non-cleft | 10.75 | 1.29 / 0.60 | 0.94 [-0.17, 2.06] | 9.77 [5.14, 14.93] |
| writer-C non-passive | 8.41 | 1.33 / 0.36 | 0.85 [-0.12, 1.88] | 7.70 [3.27, 12.94] |
| non-pass non-cleft, cells = determiner swap x distance | 10.75 | 3.66 [0.14, 7.89] / 0.82 [-1.45, 4.23] | 2.24 [0.17, 4.83] | remainder ~8.5 |

**C3 verdict.** Coverage differs WITHIN bins; that points away from difficulty-as-distance. Of the ~7 headline points, distance composition explains about 1 (1.17 [0.02, 2.54]); with the determiner swap added as a composition axis about 2.2 [0.2, 4.8], and the two directions disagree (3.7 vs 0.8) because 1N also punishes the swap harder. The headline comparison is itself not like for like: 1M's figure carries -4.8 points of cleft rejections that 1N cannot have, 1N's carries the passives. What produces the within-bin difference (prompt P-FROZEN-1N, the sentences, model noise) **cannot be determined offline.**

## TASK E

### E.0 Direction
Making the SLOVAK more explicit narrows the set of acceptable English answers: it helps FA (already settled) and costs coverage. The coverage-positive lever is the ENGLISH reference side: what the reference says, how many equally ranked renderings the model sees, and what the model is told the Slovak leaves open.

### E.1 Buckets, both sets (single rater, every item read: Slovak, stored variants, alts, locks, answer, layer, model reply)

| bucket | 1M (67) | % of 614 | 1N (76) | % of 426 | 1M non-pass non-cleft (35) | % of 571 | 1N non-pass non-cleft (54) | % of 320 |
|---|---|---|---|---|---|---|---|---|
| E1 reference carries content the Slovak lacks | 0 | 0 | 3 | 0.70 % | 0 | 0 | 3 | 0.94 % |
| E2 another equally valid rendering | 41 (32 clefts) | 6.68 % | 35 (21 passives) | 8.22 % | 9 | 1.58 % | 13 | 4.06 % |
| E3 Slovak underdetermines, stack picked a side | 13 | 2.12 % | 18 | 4.23 % | 13 | 2.28 % | 18 | 5.63 % |
| E4 answer really wrong, judge generous | 4 | 0.65 % | 11 | 2.58 % | 4 | 0.70 % | 11 | 3.44 % |
| E5 other | 9 | 1.47 % | 9 | 2.11 % | 9 | 1.58 % | 9 | 2.81 % |

E5 split: E5a answer lies INSIDE the stored annotation (recombination of stored variants + stored alts) and the model or a guard rejected it anyway — 1M 6 (3 of them F8 misfires after the model said SAME), 1N 4; E5b a minor Slovak element omitted (`nám`, `už`, `až`, `ešte`, `číslo`), judge tolerates, F5 does not — 1M 2, 1N 5; E5c the single reference OMITS a Slovak element (`ešte`) that the answer renders — 1M 1.
E3 content: 1N = 12 determiner + 4 `hodiny` number + 2 tense (1 behind F2B); 1M = 2 determiner + 11 tense/aspect (3 behind F2B; 3 conditionals where `keby + by` leaves present vs past unreal open).
E x layer, 1N: E1 {F5 3}; E2 {L3 21, TIPrej 6, F5 1, F4v2 7}; E3 {L3 12, TIPrej 5, F2B 1}; E4 {L3 4, TIPrej 4, F5 3}; E5a {L3 2, TIPrej 1, F5 1}; E5b {F5 5}.
The three E1 items: "all the way UP to / right up to" for `až k`; "take ... OUT to the container" for `odniesť`; "sheet of / piece of paper" for `papier` — all three rejected by F5 because the faithful answer is the reference minus the extra word.

### E.2 Ceilings for 1N's 76 (sizing only; base 350/426 = 82.16 %)

| lever | conservative | optimistic |
|---|---|---|
| **(a) E1 references corrected** | **+1 -> 351/426 = 82.39 % [78.44, 85.89]** | **+3 -> 353/426 = 82.86 % [78.94, 86.32]** |
| **(b) model shown the 2–3 stored variants, equally ranked** | **+2 -> 352/426 = 82.63 % [78.69, 86.11]** | **+18 -> 368/426 = 86.38 % [82.76, 89.50]** (central +11 -> 84.74 % [80.97, 88.02]) |
| **(c) "the Slovak does not fix X" annotation** | **+9 -> 359/426 = 84.27 % [80.46, 87.60]** | **+21 -> 371/426 = 87.09 % [83.53, 90.12]** |
| union a or b or c | +11 -> 361/426 = 84.74 % [80.97, 88.02] | +28 -> 378/426 = 88.73 % [85.34, 91.57] |

b and c overlap on 14 items in the optimistic reading (the determiner items); the three numbers must not be added. Layers inside the optimistic union: L3 14, L3:TIPrej 11, F5 3.

Assumptions.
- A ceiling assumes the model then answers SAME; none of these was tested.
- (a) counts only E1. Conservative = the corrected variant equals the answer exactly (L1 match, 1 item); the other two would clear F5 and still face L3 with a that -> the difference, the class L3 rejects most.
- (b) uses only variants ALREADY stored (`v`) plus stored alts, shown to the model; that the model currently sees a single reference is taken from the task statement, not verified in code. It cannot rescue F5 / F4v2 / F2B items (guards fire before the model). Conservative = the answer equals a non-first stored variant up to stored alts (2); central = additionally the determiner items whose "the" is attested in a stored variant (11); optimistic = any non-first variant closer on the rejected dimension (18).
- (c) X = demonstrative `ten/tie/tú` (that vs the), number of `hodiny`, open tense choice. Conservative = the ONLY difference is X (7 determiner + 2 number = 9); optimistic adds items with a second small difference and 2 tense items (21). Perfective futures answered with "will be V-ing" are NOT counted: the Slovak does fix that, those are E4. The gender chain's +18 is the only evidence that such an annotation moves the model; whether it transfers to determiners is unknown.
- Not reachable by any of the three as defined: 21 passives (no stored passive variant; 7 stopped by F4v2), 11 E4, 5 E5b behind F5, 1 F2B, the remaining LEX / STRUCT paraphrases with no stored counterpart.
- FA risk visible offline: variants widen what is accepted — several stored variant pairs differ in TENSE ("will have finished" / "will finish", "had sold out" / "sold out"), so ranking them equally legitimises exactly the shift the TF cell (1.76 % accepted) currently blocks; a number annotation is safe only on plurale tantum nouns; a determiner annotation looks low-risk (no W-type error in either set is a bare that/the swap) but was not measured.
- If the 11 E4 items were relabelled wrong, 1N's coverage would read 350/415 = 84.34 % (point only, no interval computed) — a label effect, not a stack effect.

## What could not be done
- F5's own body was not read (it lives in `phase1i/checker_1i.py`, outside the allowed directories); its description comes from the guards_c docstrings surfaced by the read-only import of `runner_1n`, which loads code from phase1i/1j/1k. All writes of those modules were redirected into `phase1o/` (none occurred), sockets and subprocess were disabled.
- The prompt confound (P-FROZEN vs P-FROZEN-1N) cannot be separated from a set effect without calls; the probe items are the wrong class for it.
- Classification is one rater, one pass, no second opinion; E2/E3/E5 borders are judgement calls (the rationale per item is in `taskCE_items.json`).
- No significance test beyond the cluster bootstrap and CP intervals; the bins are coarse and several 1N bins hold 25–56 items.
