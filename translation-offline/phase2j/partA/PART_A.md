# Phase 2J Part A — F4v2 subject-guard misfire (stage S1, 0 model calls)

## A1 Diagnosis
Code path: `pipeline_1i.run_pipeline` -> `checker_1i.decide` (phase1i/checker_1i.py:815-820, flag F4v2 on via ROW7_FLAGS pipeline_1i.py:31) -> `f4v2_subject_mismatch` (checker_1i.py:608) -> `sk_features` (checker_1i.py:536). The misreading is in the present-tense ENDING heuristics of `sk_features`, checker_1i.py:552-563 (`-š` -> 2sg, `-me` -> 1pl, `-te` -> 2pl), whose only non-verb guards are `after_prep` = previous token is a preposition (checker_1i.py:542-544, one token back) and `SK_NOT_VERB` (checker_1i.py:526-527).
It is NOT reported speech, multi-clause structure or the wrong clause. In all 5 sentences a NOUN or ADVERB is read as a finite verb, the false feature is the only (or the agreeing) signal, and every 3rd-person answer pronoun then "clashes":

| sid | false signal (2I) | why it is not a verb | features 2I -> fixed |
|---|---|---|---|
| 250 | present -te ceste | locative noun, `po vidieckej ceste` (adjective between preposition and noun) | {'person': '2', 'number': None, 'gender': None} -> {'person': None, 'number': None, 'gender': None} |
| 1038 | present -š príliš | adverb `príliš` (too) | {'person': '2', 'number': 'sg', 'gender': None} -> {'person': None, 'number': None, 'gender': None} |
| 1214 | present -te živote | locative noun, `v celom jeho živote` (two modifiers) | {'person': '2', 'number': None, 'gender': None} -> {'person': None, 'number': None, 'gender': None} |
| 2461 | present -te plote | locative noun, `pri tomto plote` (demonstrative) | {'person': '2', 'number': None, 'gender': None} -> {'person': None, 'number': None, 'gender': None} |
| 2989 | present -me samozrejme, l-participle dala | adverb `samozrejme` (of course) | {'person': '1', 'number': None, 'gender': 'f'} -> {'person': None, 'number': 'sg', 'gender': 'f'} |

All 44 F4v2 rejections of 2I sit on these 5 sentences (24 judge-correct = the 24 FRs, 20 judge-wrong). None of the wrong ones is wrong because of its subject: they are m (dropped word), s (grammar), t (tense), w (word) variants whose pronoun is the same correct `he/she/it`. So F4v2 caught 0 real subject errors in 2I; the 20 'catches' were accidental.

## A2 Fix (phase2j/f4fix.py; applied by phase2j/stack_tonly.py, P2J_F4FIX=1 default)
Two source patches of `sk_features`, bound only into `f4v2_subject_mismatch` (reader_nom / rs_nom keep the original reader):
- PP: a preposition followed by 1-3 modifiers (closed determiner/possessive list or adjective ending -ej/-ých/-ého/-ému/-ým/-ovom/-skom/-ckom/-nom/-ém) shadows those modifiers AND the head noun after them, exactly as `after_prep` already shadows the first word.
- NV: closed non-verb list ending like a verb: príliš/příliš, samozrejme, proste, okrem, first names in -š (Tomáš, Lukáš, Matúš, ...).
No abstain rule, no threshold; a real finite verb is still read (unit checks: `Chodíte po starej ceste`, `Robíte to príliš často`, `sme` still fire; the 5 sentences no longer do): 9/9 unit checks pass.

Catches vs cost on the closed 2I set (F4v2 layer only):
- catches: 24 judge-correct items no longer F4v2-rejected (the 24 FRs); they now go to L3.
- cost: 20 judge-WRONG items no longer F4v2-rejected; they now go to L3 (FA risk, decided only by the S2 calls). Deterministic layers before L3 (F3/F5 run before F4v2) did not catch them.
- items newly rejected / otherwise changed by the fix: 0.

Production scan (sk_features signals, fixed vs 2I, every upload row): SK 125/4064 rows change signals, CZ 18/4064. Removed signals (top): present samozrejme x52; present príliš x28; present ceste x9; present proste x4; present pulte x3; present chate x3; present torte x2; present odlete x1; present skalám x1; present chrbte x1; present kurte x1; present reklamám x1; present lopte x1; present tablete x1; present parapete x1; present momente x1; present liste x1; present živote x1; present výlete x1; present uniforme x1.

## A3 CLOSED-SET RE-SCORE (2I set, 900 items, TRANSLATION-ONLY stack through the real code path, stored 2I L3 replies by request hash, 0 calls)
Replay check (fix OFF): 800 items reach L3, 0 without a stored reply, 0 decisions differ from 2I results.jsonl.

| | coverage | FA |
|---|---|---|
| 2I (before) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| fixed, deterministic part (pending counted as reject) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| fixed, bound: all pending accepted | 466/497 = 93.76 % [91.26, 95.72] | 39/403 = 9.68 % [6.97, 12.99] |

With the fix 843 items reach L3; **43 new L3 calls are needed** (no stored 2I reply; the 2I run never planned a call for F4v2-rejected items): 23 judge-correct, 20 judge-wrong. Final A3 numbers come in S2 after exactly these calls.

Every item whose verdict changed or is pending:

| jid | judge | 2I layer, accept | fixed |
|---|---|---|---|
| A:1038:c1 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1038:c2 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1038:c3 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1038:c4 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1038:c5 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1038:m | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:1038:s | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:1038:t | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:1038:w | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:1214:c1 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1214:c2 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1214:c3 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1214:c4 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1214:c5 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:1214:m | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:1214:s | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:1214:t | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:1214:w | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:2461:c1 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2461:c2 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2461:c3 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2461:c4 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2461:c5 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2461:m | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:2461:s | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:2461:t | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:2461:w | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:250:c1 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:250:c3 | correct | F4v2, False | AG, False |
| A:250:c4 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:250:c5 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:250:m | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:250:s | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:250:t | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:250:w | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:2989:c1 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2989:c2 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2989:c3 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2989:c4 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2989:c5 | correct | F4v2, False | PENDING L3 (no stored reply) |
| A:2989:m | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:2989:s | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:2989:t | wrong | F4v2, False | PENDING L3 (no stored reply) |
| A:2989:w | wrong | F4v2, False | PENDING L3 (no stored reply) |

## A4 Regression gate (deterministic, 0 calls)
F4v2 runs after AG/F3/F5 and before L1/L2/L3 (checker_1i.decide 802-820), so a changed F4v2 decision is the only way the fix can move a verdict; every item is checked old vs fixed F4v2.
- 1W test set (phase1w/a4/run/results_1u.json, 900 rows): F4v2 final-layer rows 0; F4v2 fire changes 0; verdict flips 0; new calls needed 0. Coverage 392/401 = 97.76 % and FA 16/499 = 3.21 % unchanged.
- phase1t/run/selftest/data (8 items): F4v2 fire changes 0
- phase1t/set/data (900 items): F4v2 fire changes 0
- phase1t/set/selftest/fx/data (900 items): F4v2 fire changes 0
- phase1u/data (900 items): F4v2 fire changes 0
- phase1u/run/selftest/data (9 items): F4v2 fire changes 0
- phase1u/set/data (900 items): F4v2 fire changes 0
- phase1u/taskR/data_restored (900 items): F4v2 fire changes 0
- phase1w/a4/data (900 items): F4v2 fire changes 0
- phase1w/a4/set/data (900 items): F4v2 fire changes 0
Verdict: PASS — no F4v2 decision changes on the 1W set or any 1Q/1S/1T/1U/1W item file (the 1S packet = the closed 1Q set re-scored in 1S); coverage and FA cannot get worse; 0 new calls.

## A5 Czech reader
phase1v/trackC/cz_reader.py builds its Czech CK by executing checker_1i.py with only the `em` patch, so `sk_features` has the SAME ending heuristics and the same one-token `after_prep`. Unit (old -> fixed): `Jel po venkovské cestě příliš rychle.` {'person': '2', 'number': 'sg', 'gender': None} -> {'person': None, 'number': None, 'gender': None}; `Je příliš unavená, tak šla domů.` {'person': '2', 'number': 'sg', 'gender': None} -> {'person': None, 'number': None, 'gender': None}; `Při tomto plotě fotí letadla.` {'person': None, 'number': None, 'gender': None} -> {'person': None, 'number': None, 'gender': None}
Czech upload scan: 18/4064 rows change signals with the Czech variant (Slovak + Czech prepositions při/přes/ve/ze/ke/podle/kolem/…, same NV list). Removed (top): present příliš x15; present nádražím x1; present skalám x1; present reklamám x1.
Fix available as `f4fix.build_fixed(CZ_CK, "cz")`. Note: the 2I decide path for Czech items would call the Slovak checker_1i F4v2 (no Czech decide path is wired); the Czech CK is used by reader_nom (lang cz).

Files: phase2j/f4fix.py, phase2j/stack_tonly.py (hook), phase2j/partA/partA.py, partA_result.json, partA_stdout.txt, _run/ (requests, reqkeys_fix0/1.json incl. the missing list, prepare/finish outputs).

## A3 FINAL (stage S2) — CLOSED-SET RE-SCORE (2I set, 900 items; 2I stored L3 replies by request hash + the new S2 calls)

Run: phase2j/run_S2 via run_2j.py (fixed TRANSLATION-ONLY stack, S2 hook fix): 843 L3 requests, 800 answered by stored 2I replies (0 cost), 43 new, 43 calls made (counted 43, uncounted 0), $0.005675.

| | coverage | FA |
|---|---|---|
| 2I (before) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| A2 fix (after) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |

Catches (judge-correct, F4v2 before, now accepted): 0; judge-correct now rejected by L3: 24. Cost (judge-wrong, F4v2 before, now accepted): 0; judge-wrong still rejected (by L3): 20. Items changed outside the 44: 0. Of the 44, still F4v2: 0.

Every item whose verdict changed (layer or accept):

| jid | judge | type | before | after | L3 | answer |
|---|---|---|---|---|---|---|
| A:1038:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | My friend said that the bracelet was too loose, so she adjusted it. |
| A:1038:c2 | correct |  | F4v2 rej | F4v3 rej | SAME | The friend said the bracelet was too loose, so she adjusted it. |
| A:1038:c3 | correct |  | F4v2 rej | F4v3 rej | TIP | My friend said the bracelet is too loose, so she fixed it. |
| A:1038:c4 | correct |  | F4v2 rej | L3 rej | DIFF | My friend told me that the bracelet was too loose, so she altered it. |
| A:1038:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | The friend said that the bracelet was too loose, and so she adjusted it. |
| A:1038:m | wrong |  | F4v2 rej | L3 rej | DIFF | My friend said that it was too loose, so she adjusted it. |
| A:1038:s | wrong |  | F4v2 rej | L3 rej | DIFF | My friend said that the bracelet was too loose, so she adjust it. |
| A:1038:t | wrong |  | F4v2 rej | L3 rej | DIFF | My friend says that the bracelet is too loose, so she will adjust it. |
| A:1038:w | wrong |  | F4v2 rej | L3 rej | DIFF | My friend said that the necklace was too loose, so she adjusted it. |
| A:1214:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | He said that the training had been the hardest of his whole life! Pure agony! |
| A:1214:c2 | correct |  | F4v2 rej | F4v3 rej | SAME | He said the training was the toughest in his entire life! Pure agony! |
| A:1214:c3 | correct |  | F4v2 rej | F4v3 rej | SAME | He said that the workout had been the hardest one in his whole life! Sheer agony! |
| A:1214:c4 | correct |  | F4v2 rej | F4v3 rej | SAME | He said the practice was the hardest of his entire life! Total agony! |
| A:1214:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | He told us the training had been the toughest in his whole life! Pure agony! |
| A:1214:m | wrong |  | F4v2 rej | L3 rej | DIFF | He said that the training had been the hardest! Pure agony! |
| A:1214:s | wrong |  | F4v2 rej | F4v3 rej | TIP | He said that the training had been the most hardest in his whole life! Pure agony! |
| A:1214:t | wrong |  | F4v2 rej | L3 rej | DIFF | He says that the training will be the hardest in his whole life! Pure agony! |
| A:1214:w | wrong |  | F4v2 rej | L3 rej | DIFF | He said that the training had been the easiest in his whole life! Pure agony! |
| A:2461:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | Since 2019 he has been photographing planes by this fence. Apparently a very undemanding hobby. |
| A:2461:c2 | correct |  | F4v2 rej | F4v3 rej | SAME | He has been taking pictures of aircraft at this fence since 2019. Clearly a very low-maintenance hobby. |
| A:2461:c3 | correct |  | F4v2 rej | F4v3 rej | SAME | Since 2019, he's been photographing airplanes near this fence. Evidently a very undemanding hobby. |
| A:2461:c4 | correct |  | F4v2 rej | F4v3 rej | SAME | He has photographed planes by this fence since 2019. Apparently a very modest hobby. |
| A:2461:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | Since 2019 he has been taking photos of planes next to this fence. Obviously a very undemanding hobby. |
| A:2461:m | wrong |  | F4v2 rej | F4v3 rej | TIP | Since 2019 he has been photographing planes. Apparently a very undemanding hobby. |
| A:2461:s | wrong |  | F4v2 rej | F4v3 rej | TIP | Since 2019 he is photographing planes by this fence. Apparently a very undemanding hobby. |
| A:2461:t | wrong |  | F4v2 rej | L3 rej | DIFF | Since 2019 he had been photographing planes by this fence. Apparently a very undemanding hobby. |
| A:2461:w | wrong |  | F4v2 rej | L3 rej | DIFF | Since 2019 he has been photographing trains by this fence. Apparently a very undemanding hobby. |
| A:250:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | The vehicle had been racing along the country road before it was parked by the dunes, as was observed. |
| A:250:c3 | correct |  | F4v2 rej | AG rej |  | As was observed, the vehicle had raced along the country road before it was parked by the dunes. |
| A:250:c4 | correct |  | F4v2 rej | F4v3 rej | SAME | The car was speeding along a country road before it was parked next to the dunes, as observed. |
| A:250:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | The vehicle had sped along the country road before it got parked by the dunes, as had been observed. |
| A:250:m | wrong |  | F4v2 rej | F4v3 rej | SAME | The vehicle had been racing along the road before it was parked by the dunes, as was observed. |
| A:250:s | wrong |  | F4v2 rej | L3 rej | DIFF | The vehicle had been race along the country road before it was parked by the dunes, as was observed. |
| A:250:t | wrong |  | F4v2 rej | L3 rej | DIFF | The vehicle is racing along the country road before it is parked by the dunes, as is observed. |
| A:250:w | wrong |  | F4v2 rej | L3 rej | DIFF | The vehicle had been racing along the country road before it was parked by the lake, as was observed. |
| A:2989:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | Of course she had the route drawn on the map in case she forgot her own plan. |
| A:2989:c2 | correct |  | F4v2 rej | F4v3 rej | SAME | Naturally, she had the route marked on the map, just in case she forgot her own plan. |
| A:2989:c3 | correct |  | F4v2 rej | F4v3 rej | SAME | Of course, she got the route drawn onto the map in case she should forget her own plan. |
| A:2989:c4 | correct |  | F4v2 rej | F4v3 rej | SAME | Of course she had someone draw the route on the map, in case she forgot her own plan. |
| A:2989:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | Obviously she had the route drawn on a map, in case she were to forget her own plan. |
| A:2989:m | wrong |  | F4v2 rej | F4v3 rej | TIP | Of course she had the route drawn in case she forgot her own plan. |
| A:2989:s | wrong |  | F4v2 rej | L3 rej | DIFF | Of course she had the route draw on the map in case she forgot her own plan. |
| A:2989:t | wrong |  | F4v2 rej | L3 rej | DIFF | Of course she has the route drawn on the map in case she forgets her own plan. |
| A:2989:w | wrong |  | F4v2 rej | L3 rej | DIFF | Of course she had the route drawn on the map in case she lost her own plan. |

### A3 FINAL — layer breakdown of the 44 (S2b, 21.9.2026; LABELLED: closed-set re-score of the 2I set, not a fresh measurement)

Coverage 443/497 = 89.13 % [86.06, 91.73] before and after; FA 19/403 = 4.71 % [2.86, 7.26] before and after (exact Clopper-Pearson 95 %).
The A2 fix removes every F4v2 fire on the 44 (0 still F4v2, 0 items changed outside the 44), but none is accepted:

| judge | layer after | L3 reply | n |
|---|---|---|---|
| correct | AG | - | 1 |
| correct | F4v3 | SAME | 21 |
| correct | F4v3 | TIP | 1 |
| correct | L3 | DIFF | 1 |
| wrong | F4v3 | SAME | 1 |
| wrong | F4v3 | TIP | 4 |
| wrong | L3 | DIFF | 15 |

- NOTE on the a3_final.py wording "judge-correct now rejected by L3: 24": only 1 is an L3 DIFF; 22 are rejected by **F4v3**
  (21 with L3 = SAME, 1 TIP), 1 by AG (A:250:c3; AG decides before L3, so c3 has no request and the 44 items make 43 requests).
- F4v3 now blocks 27 of the 44 (22 correct, 5 wrong). The same 5 sentences most likely trip the A1 sk_features misreading a second
  time through F4v3, which f4fix does not patch (it replaces only f4v2_subject_mismatch). Not verified in S2b. Next: per-item F4v3
  reason on the 27; if it is the same heuristic, extend f4fix to F4v3 + tests + re-freeze; the 43 S2 replies are then reused at
  0 cost (ceiling +22 coverage -> 465/497 = 93.56 %; FA risk up to +5 -> 24/403).
- L3 on the 43 new requests (per item): SAME 22, TIP 5, DIFF 16 (15 of the 16 DIFF judge-wrong).

## S2c — F4v3 carries the same misreading (A1/A2/A3/A4/A5 extension, 21.9.2026; "F4v2 misfire" = F4v2+F4v3)
**A1 ext.** F4v3 = phase1i/taskC/guards_c.py:339 `f4v3_subject_mismatch` -> :323 `sk_features_v3`, whose first step (:328)
is `C.sk_features(sk)` = the ORIGINAL checker_1i.sk_features (checker_1i.py:552-563 ending heuristics, one-token after_prep
542-544). Same cause, not a different one: all 27 F4v3 rejections fire on the A1 false signals only (present -te plote x7,
-te živote x6, -me samozrejme + l-participle dala x6, -š príliš x4, -te ceste x4); the F4v3 extra number signal
(sk_number_extra :291) is used 0 times. F4v3 runs in the guards_c decide wrapper AFTER the model layer (:127-142), which is
why the 27 had L3 replies but were rejected anyway. f4fix (S1/S2) only replaced f4v2_subject_mismatch.
**A2 ext.** f4fix.build_fixed_v3 + v3_patch/sweep3: copies of sk_features_v3 + f4v3_subject_mismatch bound to the SAME fixed
sk_features (PP shadow + NV list + verb-head narrowing); GUARDS['F4v3'] and every namespace/closure reference swapped;
sk_number_extra untouched; no abstain rule. P2J_F4V3FIX=0 reproduces run_S2. Tests: T14 (5 sentences fire in 2I, not fixed;
number-only controls -ujú/budú still fire), T15 (real stack path via run_2j, 45 items, all replies stored, HTTP forbidden:
OFF = run_S2 exactly, ON = 0 F4v3 layers, only the 27 change). test_2j 14/14 PASS.
Catches vs cost (closed 2I set, vs run_S2): catches 21 judge-correct now accepted (L3 SAME); cost 1 judge-wrong now accepted
(A:250:m, "along the road" - drops *vidieckej*; L3 SAME); 4 judge-wrong + 1 judge-correct (A:1038:c3) now rejected by
L3:TIPrej instead of F4v3; 0 changes outside the 27. F4v3 fire changes on the 900 closed items: exactly the 44 of the 5 sids.
**A3 FINAL (S2c) — CLOSED-SET RE-SCORE, labelled** (run_S2c: 843 requests, 843 seeded = 2I ledger + run_S2 ledger, 0 new, 0 calls):
| | coverage | FA |
|---|---|---|
| 2I (before) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| A2 F4v2 only (S2) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| A2 F4v2+F4v3 (S2c, after) | 464/497 = 93.36 % [90.80, 95.39] | 20/403 = 4.96 % [3.06, 7.56] |
Exact Clopper-Pearson 95 %. Of the 44 vs 2I: 21 correct accepted, 1 wrong accepted (A:250:m), 1 correct AG (A:250:c3),
1 correct L3 DIFF (A:1038:c4), 1 correct L3:TIPrej (A:1038:c3), 19 wrong rejected (15 L3 DIFF, 4 L3:TIPrej). Coverage target
90 % met on the point AND the interval (closed set); FA 5 % met on the point only. Per item: partA/A3_FINAL_S2c.md/.json.
**A4 ext.** F4v3 old vs fixed (partA/GATE_F4V3.json): 1W test set 900 rows, 1S rows_1s.json 1,080, 1S packet.json 183 ->
0 fire changes, 0 verdict flips, 0 new calls each; PASS (coverage/FA cannot move). Upload scan: SK 125/4,064 rows change
v3 features, 2 rows newly get the F4v3 extra number signal (byt-future budú/bude, real verbs); CZ 18/4,064, 0 new extra.
**A5 ext.** The Czech path has NO F4v3: cz_reader.py references no guards_c/decide, and guards_c._c() imports the Slovak
checker_1i. If a Czech decide is ever wired, f4fix.build_fixed_v3(G, CZ_CK, 'cz') is the same fix (scan above).
Freeze: d9b806d1c06093d7a360b82b84d97a787eec164f (FROZEN_SHA.txt written before the run; shasum -c of the frozen files after the run = 0 mismatches).
