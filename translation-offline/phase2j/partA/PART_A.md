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
- catches: 0 judge-correct items no longer F4v2-rejected (the 24 FRs); they now go to L3.
- cost: 0 judge-WRONG items no longer F4v2-rejected; they now go to L3 (FA risk, decided only by the S2 calls). Deterministic layers before L3 (F3/F5 run before F4v2) did not catch them.
- items newly rejected / otherwise changed by the fix: 0.

Production scan (sk_features signals, fixed vs 2I, every upload row): SK 128/4064 rows change signals, CZ 21/4064. Removed signals (top): present samozrejme x52; present príliš x28; present ceste x9; present proste x4; present pulte x3; present chate x3; present torte x2; present odlete x1; present skalám x1; present chrbte x1; present kurte x1; l-participle bola x1; present reklamám x1; present lopte x1; present tablete x1; present parapete x1; present momente x1; present liste x1; present živote x1; present výlete x1.

## A3 CLOSED-SET RE-SCORE (2I set, 900 items, TRANSLATION-ONLY stack through the real code path, stored 2I L3 replies by request hash, 0 calls)
Replay check (fix OFF): 800 items reach L3, 0 without a stored reply, 0 decisions differ from 2I results.jsonl.

| | coverage | FA |
|---|---|---|
| 2I (before) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| fixed, deterministic part (pending counted as reject) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| fixed, bound: all pending accepted | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |

With the fix 800 items reach L3; **0 new L3 calls are needed** (no stored 2I reply; the 2I run never planned a call for F4v2-rejected items): 0 judge-correct, 0 judge-wrong. Final A3 numbers come in S2 after exactly these calls.

Every item whose verdict changed or is pending:

| jid | judge | 2I layer, accept | fixed |
|---|---|---|---|

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
Czech upload scan: 21/4064 rows change signals with the Czech variant (Slovak + Czech prepositions při/přes/ve/ze/ke/podle/kolem/…, same NV list). Removed (top): present příliš x15; present nádražím x1; present skalám x1; l-participle byla x1; present reklamám x1; l-participle mluvila x1; l-participle dala x1.
Fix available as `f4fix.build_fixed(CZ_CK, "cz")`. Note: the 2I decide path for Czech items would call the Slovak checker_1i F4v2 (no Czech decide path is wired); the Czech CK is used by reader_nom (lang cz).

Files: phase2j/f4fix.py, phase2j/stack_tonly.py (hook), phase2j/partA/partA.py, partA_result.json, partA_stdout.txt, _run/ (requests, reqkeys_fix0/1.json incl. the missing list, prepare/finish outputs).

## A3 CORRECTION (supersedes the A3 table above) — hook defect, direct deterministic re-score
The stack-path replay with the fix ON reproduced 2I exactly (800 reach L3, 0 changes): the `stack_tonly.py` hook patched a
`checker_1i` module object that is NOT the one the pre-L3 plan/decide uses (the replay with fix OFF is valid: 800 requests,
0 missing stored replies, 0 decisions differing from 2I — the stored-reply replay machinery works). DEFECT for S2: find the
instance runner_1u/R1P plan_ids + decide actually call and patch that one; re-run partA.py; it must show 44 new requests.
Direct deterministic re-score (every 2I item, old vs fixed F4v2 on the same sk/answer; items rejected earlier by AG/F3/F5 excluded):
- F4v2 un-fires on 44 items (all 44 of the 2I F4v2 layer: 24 judge-correct = the 24 FRs, 20 judge-wrong); newly fires on 0 items.
- These 44 items need **44 new L3 calls** (no stored 2I reply); A4 needs 0.
- CLOSED-SET RE-SCORE, bounds until S2 makes the calls: coverage 443/497 = 89.13 % [86.06, 91.73] (all 44 L3-rejected) to 467/497 = 93.96 % [91.49, 95.89] (all accepted);
  FA 19/403 = 4.71 % [2.86, 7.26] (all rejected) to 39/403 = 9.68 % [6.97, 12.99] (all accepted). 2I: coverage 443/497 = 89.13 %, FA 19/403 = 4.71 %.
Production-scan cost candidates (sk upload, removed signals that ARE verbs): `potrebuješ` x1 (2sg) and `l-participle bola` x1
(SK); CZ `byla`/`mluvila`/`dala` x1 each - the PP shadow swallowed a verb after a mis-read modifier. S2/S3: inspect these 5 rows
(partA_result.json A5 examples) and tighten `is_mod` if they are real; everything else removed is a noun/adverb.
