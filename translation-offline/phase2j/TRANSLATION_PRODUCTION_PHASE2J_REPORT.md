# Translation production — Phase 2J report (Slovak, TRANSLATION-ONLY stack)

Date: 21.9.2026. Work directory: `~/Projects/and-again-content/translation-offline/phase2j/`. Nothing was written to the database. No deploy, migration, push or rebase. Earlier phase directories are byte-identical (SHA check at the end). Sources for every number: `phase2j/PROGRESS.md`, `phase2j/analysis/ANALYSIS.md` + `numbers.json`, `partA/PART_A.md`, `partC/PART_C.md`, `partB/PART_B.md`, `partB/B1.md`, `upload/UPLOAD_README.md`, `TOKENS.jsonl`. Intervals are exact 95 % Clopper-Pearson. Coverage = accepted / judge-correct. FA = accepted / judge-wrong. Targets: coverage >= 90 %, FA <= 5 %.

## 1 Headline — Part D (100 fresh production Slovak sentences, opened once) beside 2I

Stack: the fixed TRANSLATION-ONLY stack (Part A fix on, Part B corrected references), L3 gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, TIP-as-rejection on. Set: 25 sentences per level from the corrected upload, only from the 3,200 B2-audited rows, excluding the 60 2F-probe and 100 2I sentences; 900 answers (500 correct-intent / 400 wrong-intent), 4 blind writers, 1 judge prompt (byte-identical to 2I) across 4 sessions. Freeze commit ea0992c, run commit 5d7008c, 1 open in the access log, 833 calls, all HTTP 200.

| level | 2J coverage | cov >= 90 point / interval | 2J FA | FA <= 5 point / interval | 2I coverage | 2I FA |
|---|---|---|---|---|---|---|
| A1 | 109/124 = 87.90 % [80.83, 93.07] | missed / missed | 3/101 = 2.97 % [0.62, 8.44] | met / missed | 96.77 % [91.95, 99.11] | 1.98 % [0.24, 6.97] |
| A2 | 119/125 = 95.20 % [89.85, 98.22] | met / missed | 7/100 = 7.00 % [2.86, 13.89] | missed / missed | 93.60 % [87.78, 97.20] | 8.00 % [3.52, 15.16] |
| B1 | 103/124 = 83.06 % [75.28, 89.20] | missed / missed | 7/101 = 6.93 % [2.83, 13.76] | missed / missed | 83.74 % [76.01, 89.78] | 5.88 % [2.19, 12.36] |
| B2 | 119/125 = 95.20 % [89.85, 98.22] | met / missed | 7/100 = 7.00 % [2.86, 13.89] | missed / missed | 82.40 % [74.57, 88.63] | 3.00 % [0.62, 8.52] |
| **pooled** | **450/498 = 90.36 % [87.42, 92.81]** | **met / missed** | **24/402 = 5.97 % [3.86, 8.75]** | **missed / missed** | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |

Coverage meets 90 % on the point only (2I missed it). FA misses 5 % on the point and on the interval (2I met it on the point). No level meets either target on the interval. 2I and 2J use different fresh sentences, so the change is not a paired effect.

## 2 Cause tables beside 2I

### False rejections (2J 48 of 498 judge-correct; 2I 54 of 497)

| cause | 2J | 2J rate | 2I | 2I rate |
|---|---|---|---|---|
| F4v2 subject-guard misfire | 0 | 0.00 % | 24 | 4.83 % |
| reference wrong or too narrow | 25 | 5.02 % | 16 | 3.22 % |
| synonym or different word | 4 | 0.80 % | 4 | 0.80 % |
| structural paraphrase | 2 | 0.40 % | 2 | 0.40 % |
| English tense within the Slovak's frame | 4 | 0.80 % | 2 | 0.40 % |
| dropped FUNCTION word (M1; F3 reads has got -> has as a drop) | 4 | 0.80 % | 2 | 0.40 % |
| determiner or article choice | 1 | 0.20 % | 1 | 0.20 % |
| voice or passive | 0 | 0.00 % | 1 | 0.20 % |
| AG misfire | 5 | 1.00 % | 1 | 0.20 % |
| judge label doubtful | 1 | 0.20 % | 1 | 0.20 % |
| F5 misfire: compound noun shortened (new in 2J) | 1 | 0.20 % | 0 | 0.00 % |
| L3 rejects an answer equal to a stored reference (new in 2J) | 1 | 0.20 % | 0 | 0.00 % |
| **total** | **48** | **9.64 %** | **54** | **10.87 %** |

By layer: L3 32, F3 5, L3:TIPrej 5, AG 5, F5 1 (2I: F4v2 24, L3 20, L3:TIPrej 6, F3 3, AG 1). By level, reference causes are 1 / 4 / 18 / 2 (A1/A2/B1/B2): B1's coverage gap is almost all references (sid 2152 "poháre" = jars only, 5 FR; sid 3390 "si šnuroval" read as he only, 5 FR; sid 1613 pro-drop fixed to she, 3 FR; sid 92, 2362).

### False acceptances (2J 24 of 402 judge-wrong; 2I 19 of 403)

| cause | 2J | 2J rate | 2I | 2I rate |
|---|---|---|---|---|
| content word dropped, accepted | 18 | 4.48 % | 15 | 3.72 % |
| wrong word accepted | 4 | 1.00 % | 1 | 0.25 % |
| grammar error accepted | 0 | 0.00 % | 2 | 0.50 % |
| judge doubtful | 0 | 0.00 % | 1 | 0.25 % |
| agent drop accepted (new in 2J) | 1 | 0.25 % | 0 | 0.00 % |
| time-frame shift accepted (new in 2J) | 1 | 0.25 % | 0 | 0.00 % |
| **total** | **24** | **5.97 %** | **19** | **4.71 %** |

All 24 FAs are L3 with reply SAME. Writer type: M 19, T 1, W 1, correct-intent 3 (2I: M 16, correct-intent 3). Three FAs are caused by a reference (A:54:m, A:54:t on a truncated B3 reference; A:2889:m where the reference itself omits "here"). The agent drop (A:1720:m) got through because the annotation records no nominative agent although "sestry" is one. The full per-item lists (48 FR, 24 FA) are in `phase2j/analysis/ANALYSIS.md` §3–4.

## 3 Part A — the F4v2 subject-guard misfire

**Diagnosis (A1).** It is not reported speech and not the wrong clause. `checker_1i.sk_features` (phase1i/checker_1i.py:552–563) guesses person from word endings (-š -> 2sg, -me -> 1pl, -te -> 2pl), and its preposition guard `after_prep` (542–544) looks only one token back. So nouns and adverbs get read as finite verbs: `po vidieckej ceste`, `v celom jeho živote`, `pri tomto plote` (-te -> 2pl), `príliš` (-š -> 2sg), `samozrejme` (-me -> 1pl). Every 3rd-person answer then "clashes". Code path: `checker_1i.decide` 815–820 -> `f4v2_subject_mismatch` :608 -> `sk_features` :536. All 44 F4v2 rejections in 2I are on the 5 sentences (sids 250, 1038, 1214, 2461, 2989): the 24 judge-correct ones and 20 judge-wrong ones. None of the 20 wrong answers is wrong because of its subject; they are m/s/t/w variants with the correct pronoun, so F4v2 caught 0 real subject errors in 2I.

**F4v3 (found in S2b/S2c).** With F4v2 fixed, 27 of the 44 were still rejected, now by F4v3 (phase1i/taskC/guards_c.py:339 `f4v3_subject_mismatch` -> :323 `sk_features_v3` -> :328 the same `C.sk_features`). Same misreading, same false signals; the extra F4v3 number signal was used 0 times. F4v3 runs in the guards_c wrapper after L3 (:127–142), which is why these items had L3 replies but were rejected anyway.

**Fix (A2), `phase2j/f4fix.py`.** Deterministic, no abstain rule, no threshold: (PP) a preposition followed by 1–3 modifiers shadows the modifiers and the head noun, as `after_prep` already does for one word; (NV) a closed list of non-verbs with verb-like endings (príliš/příliš, samozrejme, proste, okrem, first names in -š); (verb-head guard, S2) the PP head is not shadowed when it is an l-participle, a 2sg -š form or byť/mať, so the fix can never remove a real verb. Bound only into F4v2 and F4v3 (reader_nom and rs_nom keep the original reader). A hook defect in S2 (the stack runs the guards_c wrapper, whose globals are not `checker_1i.__dict__`) was fixed with `f4fix.sweep()`, which replaces the function in every namespace and closure. Tests T8, T14, T15 in `test_2j.py`.

**Catches vs cost (closed 2I set).** F4v2 fix alone: 44 items no longer F4v2-rejected, 0 accepted (F4v3 took 27, L3 16, AG 1). F4v2 + F4v3 fix: catches 21 judge-correct now accepted; cost 1 judge-wrong now accepted (A:250:m, drops "vidieckej"); 5 moved to L3:TIPrej (4 wrong, 1 correct). 0 items changed outside the 44.

**Closed-set re-score (A3) — labelled: a re-score of the closed 2I set, not a fresh measurement.**

| | coverage | FA |
|---|---|---|
| 2I | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| F4v2 fix only (S2, 43 new L3 calls) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| F4v2 + F4v3 fix (S2c, 0 calls, stored replies) | 464/497 = 93.36 % [90.80, 95.39] | 20/403 = 4.96 % [3.06, 7.56] |

Every changed item is listed in `partA/PART_A.md` and `partA/A3_FINAL_S2c.md`.

**Regression gate (A4).** 1W test set (900 rows), 1S rows (1,080), 1S packet (183), plus the 1T/1U/1W item files: 0 F4v2 and 0 F4v3 decision changes, 0 verdict flips, 0 calls. PASS; 1W coverage 97.76 % and FA 3.21 % unchanged.

**Czech (A5).** Same defect: `phase1v/trackC/cz_reader.py` builds its reader by executing checker_1i.py, so the ending heuristics are the same (`příliš` -> 2sg, 15 times in the Czech upload). `f4fix.build_fixed(CK, 'cz')` changes the signals on 18/4,064 CZ rows (SK 125/4,064). The Czech path has no F4v3 and no Czech decide is wired; the fix is available if one is.

**Part D.** 0 F4v2/F4v3 misfires on fresh sentences (2I: 24).

## 4 Part C — false acceptances (dropped content words)

**C1.** Current closed-set FAs are 20 (2I's 19 + A:250:m); 16 are dropped content words. One path for all 20: F5 (`f5_adjunct_deletion` :705) only fires when the answer is an order-preserving subsequence of a reference; `_subseq_positions` returns None at checker_1i.py:669 and the loop continues at :719, so `span_information` (:683) is never reached. Two causes combine: every FA sentence has exactly one reference (873/900 closed-set items have one), and every M answer also swaps at least one token (must/has to, put on/wore, incredible/unbelievable). Secondary: now/today/totally are in FUNCTION/INFO_FUNC.

**C2 — sized, not built.** Five deterministic variants were sized on the closed 2I set, the 1W set and the 1S rows. The cheapest costs 16 judge-correct answers on the closed 2I set for 3 catches (V3/V4); V5 (F5 relaxed) catches 5 and costs 34. The rule was to build only at no measurable cost, so nothing was wired, tested or re-frozen. The reason: the repo has no Slovak -> English content-word map; the only lexical resource is the annotation `alt`, which misses common synonyms. The 1S packet has no references or labels, so it could not be sized.

**C3 — A2 FA 8.00 % [3.52, 15.16].** The same 8 items on the 2I stack and on the fixed stack: 7 dropped words (now, today, totally, Look!, off the plant, hot, in the room) + 1 doubtful (honestly). All are writer-M, L3 SAME, single-reference, non-subsequence. A2 sentences are short, so the M writer drops one word and paraphrases one other, which is exactly what F5 cannot see. In Part D, A2 FA is 7/100.

## 5 Part B — the references

**B1 — deterministic subject audit (0 calls).** Reader `phase1w/reader_nom` with the A2 fix swapped in. Two reader defects were found and repaired in the audit only: R1, 3sg past gender left None (gender taken from the l-participle, 753 SK / 730 CZ rows); R2, Czech bys/jsi/jsem… not read (49 rows) and SK `si` beside an l-participle (57 rows, person left open).

| | SK | CZ |
|---|---|---|
| rows read / 4,064 | 1,824 | 1,782 |
| references compared | 1,169 / 4,341 | 1,097 / 4,313 |
| flags (rows) | 92 (83) | 107 (99) |
| person | 44 | 53 |
| number | 19 | 16 |
| neuter as he/she (review only) | 15 | 13 |
| gender fixed where the Slovak leaves it open | 9 | 10 |
| gender contradiction | 5 | 15 |

Some reader noise remains in the flags (for example `Udrie ho` read as 1sg). Ten examples per class and language are in `partB/B1.md`.

**B2 — model audit of Slovak references.** One prompt (sha256 ccf78e15…0eea4), N = 100 per session, waves of 4. Audited: **3,200 of 4,064 SK rows** (3,413 references, 32 packets). Why not all: wave 1 cost 44,403 tokens per packet on average, which projected 1.86M for all 41 packets. The B2 cap was 1,500,000 by reservation, so the driver stopped before wave 9 (p032–p040 not audited). Part D sampled only audited rows. Czech was sized, not run (~1.81–1.86M tokens).

| class (per reference) | A1 | A2 | B1 | B2 | all |
|---|---|---|---|---|---|
| faithful | 753 | 758 | 580 | 475 | 2,566 |
| adds content | 21 | 12 | 15 | 17 | 65 |
| narrows a word | 34 | 55 | 40 | 43 | 172 |
| wrong person or gender | 208 | 127 | 55 | 79 | 469 |
| other | 37 | 44 | 31 | 29 | 141 |

778 of the 3,200 sentences have at least one flagged reference. Agreement with B1 is low: of 70 B1 SK flags on audited rows, B2 marks 21 as wrong person/gender (26 with any flag).

**B3 — corrections, flagged references only, 1P tense filter applied.** SK rows changed: **577** (references on those rows 643 -> 1,191). Wrong person/gender: 385 other-gender variants added, 84 listed only (person/number). Narrows: 164 broader variants added, 8 listed. Adds content: 60 replaced in place, 5 listed. Other: 141 listed. 1 duplicate removed. v[0] changed on 58 rows (en kept equal to v[0]). Faithful references were not touched. Czech: 0 changes; all 107 B1 CZ flags listed, because they are unreviewed reader output.

**Broken or truncated replacements found in S9.** A deterministic scan of the 60 "adds content" replacements found 4 that removed a required word:
- ex 927: "… grins like that before a trust fall." -> "… grins like that before a." (Part D sid 54)
- ex 22385: "She puts a hot bowl in front of the happy man." -> "She puts a hot bowl in front of."
- ex 35040: "He shares his ice cream with his friend." -> "He shares his ice cream with."
- ex 41408: "… she wouldn't have slumped onto her desk." -> "… slumped onto desk." (Part D sid 22)

Two of these reached Part D and cost 2 FR (A:22:c4, A:54:c3) and 2 FA (A:54:m, A:54:t). The 385 added gender swaps were well-formed in the scan (0 non-pure swaps, 0 mixed he+she) but were never reviewed by a person. In Part D, rows with a B3-changed reference had coverage 68/89 = 76.40 % vs 382/409 = 93.40 % on other rows; FA 5/73 = 6.85 % vs 19/329 = 5.78 %. Most of those FRs came from something B3 did not fix (tense, synonym, the other person), not from the swap itself.

**B4 — combined A + B, labelled: a re-score of the closed 2I set.** 12 of the 100 closed-set sentences (108 items) have corrected references; 101 new L3 calls, $0.012708.

| | coverage | FA |
|---|---|---|
| 2I | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| A (F4v2 + F4v3 fix) | 464/497 = 93.36 % [90.80, 95.39] | 20/403 = 4.96 % [3.06, 7.56] |
| A + B | 474/497 = 95.37 % [93.14, 97.04] | 21/403 = 5.21 % [3.25, 7.86] |

22 verdicts changed vs A, 63 vs 2I (`partB/b4/B4.json`).

## 6 Corrected upload files

| file | rows | sha256 |
|---|---|---|
| `phase2j/upload/B3_diff.jsonl` | 955 | 4de304a2fbde24250ed2df8c23e768a8db7ebfc29c742a294b07731c9a2cd127 |
| `phase2j/upload/UPLOAD_README.md` | - | c4e45219f869b7bbe30f1312334f9e5a1ada282dd5344c590bc242e2285f2a9d |
| `phase2j/upload/annotations_cz_fixed.jsonl` | 4064 | 8032b048425df9a305c54dcfd4346e33702d7e5bb64cd223949b50e399c30450 |
| `phase2j/upload/annotations_sk_fixed.jsonl` | 4064 | 064ff5aeef27d7f0af4bfbd843fd40f74cb04a17adf4c0e3faad14ba8e9aa694 |
| `phase2j/upload/upload_cz_final.xlsx` | cz 4064 | 599d192cc9370d44d30c172d6d2e39216c7caf2fbb0a4976ee8d9115b0d02dd7 |
| `phase2j/upload/upload_sk_final.xlsx` | sk 4064 | fec069a2d1ea434492a99718553e9d6189320e6a681de658b150172788d62c75 |

Format is the same as `phase2i/upload/`. `phase2i/upload/` is unchanged. Per-reference changes: `upload/B3_diff.jsonl`. **The 4 truncated references above are still in these files. Repair them before any upload.**

## 7 Gemini calls and spend

| stage | counted calls | spend |
|---|---|---|
| S1 (Part A deterministic) | 0 | $0 |
| S2 (A3, F4v2 fix new L3 items) | 43 | $0.005674 |
| S2c (F4v3 extension, stored replies) | 0 | $0 |
| S3 (Part C) | 0 | $0 |
| S5 (B4) | 101 | $0.012708 |
| S8 (Part D, opened once) | 833 | $0.104052 |
| **total** | **977 of the 1,200 cap** | **$0.122434 of $1.00** |

Counted means HTTP 200 only. 0 uncounted attempts and 0 failed calls in every run.

## 8 Claude tokens against the 4,000,000 budget

| item | tokens | source |
|---|---|---|
| headless: B2 audit | 1,414,860 | measured (session envelopes) |
| headless: 4 blind writers | 225,497 | measured |
| headless: 4 judge sessions (s1 needed one retry) | 340,352 | measured |
| **headless subtotal** | **1,980,709** | measured |
| agent S1 / S2 / S2b / S2c | 109,306 / 150,490 / 60,566 / 100,486 | harness |
| agent S3 / S4 / S5 / S6 | 98,586 / 98,600 / 96,472 / 61,169 | harness |
| agent S7 / S8 / S9 | 77,400 / 54,900 / 130,836 | harness |
| **agent stages subtotal** | **1,038,811** | harness |
| this report stage | ~100,000 | estimate |
| orchestrator | ~140,000 | estimate |
| **total** | **~3,259,520 of 4,000,000 (81.5 %)** | the last two lines are estimates |

No headless session hit a usage limit or quota error.

## 9 Judge noise

Hidden duplicate controls: 79/80 agree (2I 80/80); the one disagreement is in session pair 1–4. Judge vs writer intent: 894/900 agree (correct->wrong 4, wrong->correct 2). One FR is recorded as a doubtful label (A:315:m, a dropped "them" judged correct). At n ≈ 100 per level, one label moves a level's rate by about 1 point. This is small beside the 2.7-point interval half-width of the pooled rates.

## 10 Defects recorded, not fixed

- B3 "adds content" replacements truncated 4 references (ex 927, 22385, 35040, 41408), and they are still in `phase2j/upload/`. The 385 added gender swaps have had no human or model review.
- The references are still the largest FR cause (25/48). Some are person/gender ambiguity B3 did not cover (pro-drop 3sg fixed to one gender; `si` + l-participle read only as he, not as 2sg "you"). Others are narrow words (poháre = jars only).
- C2 dropped-content-word rule not built. There is no deterministic Slovak content-word -> English map.
- AG misfires on adjectival predicates ("worn out", "priced at", "performed at the theatre"): 5 FR in Part D.
- F3 treats "has got" -> "has" as a dropped word: 4 FR in Part D.
- F5 reads "pan" for "frying pan" as a dropped word (1 FR). L3 rejected an answer equal to a stored reference up to a contraction (1 FR).
- AG annotation for A:1720 records no nominative agent although "sestry" is one, so an agent drop was accepted.
- reader_nom gaps (3sg past gender None; Czech 1st/2nd-person auxiliaries; SK `si` + l-participle): repaired in the B1 audit only, not in the reader.
- B2 covered 3,200/4,064 SK rows; 864 rows are unaudited. Czech: B1 flags listed, 0 corrected, B2 not run.
- The 1S packet (183) has no references or labels and cannot be used to size C2.

## 11 Process slips

- S2: the stage ended with files uncommitted, and a 122-line SHA diff looked like a write to an earlier phase. It was a generator mismatch: the chain's own `find` included phase2i files that `sha_tree.sh` prunes. Re-running the S1 generator gave an empty diff. Nothing was restored. The files were committed in e5db040 (`partA/SHA_INCIDENT_S2.md`).
- S2c: a zsh word-split bug skipped the pre-run freeze commit. The 0-call run used exactly the files hashed in FROZEN_SHA.txt (shasum -c after the run: 0 mismatches), and the freeze was committed right after the run.
- S8: RUN_COMMIT (5d7008c) is one commit after FREEZE_COMMIT (ea0992c), because it is the commit that carries FREEZE_COMMIT.txt. All three were verified in HEAD before the open.
- Slips of the same kind (freeze and commit bookkeeping, path handling) happened in 2F and 2I. 2I's first set open crashed on a relative `--run-dir`. In 2J every invocation used absolute paths and relative paths were refused in the tests.

## 12 Judgement

1. Production does not yet meet the targets. Fresh coverage is 90.36 % [87.42, 92.81] (90 % met on the point, not the interval), and FA is 5.97 % [3.86, 8.75] (5 % missed on both).
2. Part A worked. The F4v2/F4v3 misreading is gone: 0 misfires on fresh sentences, versus 24 FR in 2I. On the closed set it added 21 correct answers for 1 FA (89.13 -> 93.36 %). The regression gates are clean.
3. Part B added 10 more correct answers on the closed set (-> 95.37 %) for 1 more FA. On fresh sentences, references are now the largest FR cause (25/48, 18 of them in B1), and 2 truncated B3 references cost 2 FR + 2 FA.
4. Part C was not built. Dropped content words are 18 of 24 FAs, all accepted by L3 with SAME, and M answers are the leak (19 of 100 accepted).
5. What is left: FA is the binding target. Coverage is at the line, and A1 (87.90 %) and B1 (83.06 %) are still below it.
6. Next lever: a per-sentence Slovak content-word -> English map, so that a deterministic dropped-word check can work without thin references. Then repair the 4 truncated references and cover pro-drop person/gender ambiguity in the references. The AG adjectival-predicate misfire and the F3 "has got" rule are small fixes worth 9 FR.
