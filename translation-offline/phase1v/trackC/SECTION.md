# Phase 1V — Track C: Czech-specific reader (0 model calls)

Model calls: **0** (counted 0 / failed 0 / retried 0). Spend $0. No Czech probe, no Czech test set, no DB,
no earlier phase dir modified. Code: `phase1v/trackC/cz_reader.py` (the Czech reader),
`phase1v/trackC/run_trackC.py` (runner). Output: `trackC_results.json`, `cz_validation_<run>.json`
(runs: before, fix_em, fix_se, fix_jestli, fix_aspect, after).

## C0. How the Czech reader is built, and proof the Slovak reader is untouched
`cz_reader.build(fixes)` executes the Slovak source text of `phase1n/f9.py`, `phase1i/checker_1i.py`,
`phase1s/taskC/agent_drop_v2.py`, `phase1t/taskA/agent_drop_v3.py` into NEW module objects
(`cz_f9_*`, `cz_ck_*`, `cz_v2_*`, `cz_v3_*`) and applies four named patches to those copies only
(source patches are asserted to match exactly once; Czech V3 is bound to the Czech V2). The Slovak
modules the validator loads are the original files, loaded by the original code.
- The 1T validator `phase1t/taskB/cz_validate.py` is executed **unchanged** (its own source text); the runner
  only (a) redirects the output path to trackC and (b) inserts a module swap per language: `cz` rows use the
  Czech reader, `sk` rows the original Slovak modules.
- `before` run reproduces the 1T summary **exactly**: True; Slovak `sk` rows of `before`
  byte-identical to the 1T `cz_validation.json` rows: True.
- Slovak control rows identical to `before` in every run (incl. `after`): True.
- SHA-256 before / after the whole Track C run (all unchanged: True):

| file | before | after | |
|---|---|---|---|
| `phase1n/f9.py` | `fe05a988d325f1f06c9c9588a1d5bd131cf03dafd1f50ee11dfb2080dd3e58f4` | `fe05a988d325f1f06c9c9588a1d5bd131cf03dafd1f50ee11dfb2080dd3e58f4` | same |
| `phase1i/checker_1i.py` | `49fa087bf2ecb511a960315e1c1e25a6f01ffbbb40fd285fc3157168af556f19` | `49fa087bf2ecb511a960315e1c1e25a6f01ffbbb40fd285fc3157168af556f19` | same |
| `phase1s/taskC/agent_drop_v2.py` | `ad2f9b3a17717ca042eec9c5859131f1c0cac31483423457eeaf67c4ea963e27` | `ad2f9b3a17717ca042eec9c5859131f1c0cac31483423457eeaf67c4ea963e27` | same |
| `phase1t/taskA/agent_drop_v3.py` | `35458e65feeafd394cb263b74cc122d3289db1fe40b1593b6c196b7d436cb6b0` | `35458e65feeafd394cb263b74cc122d3289db1fe40b1593b6c196b7d436cb6b0` | same |
| `phase1t/taskB/cz_validate.py` | `1053b79b6594846fabd4c85f14046a0c8aff1edd0e29a766d916d6e057c33012` | `1053b79b6594846fabd4c85f14046a0c8aff1edd0e29a766d916d6e057c33012` | same |
| `phase1t/taskB/cz_validation.json` | `ae9a07b70bc8c8ddd5168be640e81447dc850e538b67ad0f3fe6dc5d875e1cd3` | `ae9a07b70bc8c8ddd5168be640e81447dc850e538b67ad0f3fe6dc5d875e1cd3` | same |
| `phase1t/taskB/cz_gold.json` | `bd8ca71aa9e168dcf3427481f038b7c952ad90586226a8eebf9bfbacda4b41e2` | `bd8ca71aa9e168dcf3427481f038b7c952ad90586226a8eebf9bfbacda4b41e2` | same |
| `phase1t/taskB/sk_gold.json` | `9421ddbdc7a6e4ae7038ee89241fe051d6cfa0c5aed270aa6f812f5af67da9c0` | `9421ddbdc7a6e4ae7038ee89241fe051d6cfa0c5aed270aa6f812f5af67da9c0` | same |
| `phase1t/taskB/cz_sample_numbered.json` | `88ac99db7a3b4fb627167c8162a1e059b6bf3488bb4fc4438f073ca523f84998` | `88ac99db7a3b4fb627167c8162a1e059b6bf3488bb4fc4438f073ca523f84998` | same |

## C1. The four fixes
1. **`em` — instrumental `-em` read as 1sg** (`checker_1i.py` `sk_features`): the Czech copy drops `em`/`iem`
   from the 1sg ending list (Czech 1sg present is `-ím/-ám/-u`, never `-em`; Czech `-em` = instrumental,
   `kolem`, or `jsem`). Result: `-em/-ím` noun signals **8 -> 0** (probe `f4v2_instrumental_em`); false readings
   **6 -> 1**: n=17, 21, 61, 83, 87 ERROR -> CONSERVATIVE; **n=112 stays ERROR** — its second signal is
   `dalším` (instrumental adjective in `-ím`, the same ending as Czech 1sg `vidím`), not an `-em` token. n=79
   `sestřenicím` (dative pl `-ím`) also stays ERROR for the same reason. Cost: n=105 AGREE -> CONSERVATIVE
   (it was right only because `jsem` happened to be 1sg).
2. **`se` — missing from `SK_REFLEX`**: Czech copy `(se|sa|si)`. `se` misses **23 -> 0**; both gold reflexive
   passives **n=102, 120 ERROR_as_active -> AGREE** (v2 and v3). Guard 3 (first-word agent) errors
   **61 -> 45**. Side effect, stated: 10 gold-active sentences with an ordinary reflexive `se` verb now read as
   non-active (n=3, 27, 43, 44, 46, 50, 59, 61, 71, 97 AGREE -> ERROR_as_passive) — exactly the Slovak
   control's behaviour with `sa` (sk as_passive 18). Net guard-4 ERROR goes UP (v2 12 -> 20, v3 15 -> 23), but
   the dangerous direction (missed passive, `as_active`) goes DOWN (v2 6 -> 4, v3 5 -> 3). The Czech `si`
   (dative-only) over-fire from 1T (n=5, 8, 18, 19, 36, 118) is NOT a named bug and was left as is.
3. **`jestli` read as l-participle** (`f9`): `jestli/jestliže/zdali/zdalipak` added to `L_NONVERB` and
   `SUB_MARK` in the Czech copy. n=29 `past` ERROR -> `{future, present}` CONSERVATIVE (alone: F9 ERROR 3 -> 2).
4. **Czech aspect lexicon gap** (`f9`, n=15): Czech perfective list (~150 forms) added to `PERF_LEX`; `dokáže*`
   removed from the Czech copy's `MOD` (Slovak files it as a modal-present). n=15 `present` ERROR ->
   `{future, present}` CONSERVATIVE (alone: F9 ERROR 3 -> 2). With fix 3 it also supplies `zkusíme` for n=29.

## C2. 1T Czech gold validation, before / after, Slovak control beside it (n = 120 each, exact CP 95 %)
| guard | lang | run | AGREE | CONSERVATIVE | ERROR | ERROR rate [95 % CI] |
|---|---|---|---|---|---|---|
| g1 F9 | cz | before | 82 | 35 | 3 | 2.5 % [0.5, 7.1] |
| g1 F9 | cz | after | 82 | 37 | 1 | 0.8 % [0.0, 4.6] |
| g1 F9 | sk | before | 96 | 23 | 1 | 0.8 % [0.0, 4.6] |
| g1 F9 | sk | after | 96 | 23 | 1 | 0.8 % [0.0, 4.6] |
| g2 F4v2 | cz | before | 17 | 83 | 20 | 16.7 % [10.5, 24.6] |
| g2 F4v2 | cz | after | 16 | 89 | 15 | 12.5 % [7.2, 19.8] |
| g2 F4v2 | sk | before | 17 | 87 | 16 | 13.3 % [7.8, 20.7] |
| g2 F4v2 | sk | after | 17 | 87 | 16 | 13.3 % [7.8, 20.7] |
| g3 AG v2 | cz | before | 53 | 6 | 61 | 50.8 % [41.6, 60.1] |
| g3 AG v2 | cz | after | 59 | 16 | 45 | 37.5 % [28.8, 46.8] |
| g3 AG v2 | sk | before | 55 | 18 | 47 | 39.2 % [30.4, 48.5] |
| g3 AG v2 | sk | after | 55 | 18 | 47 | 39.2 % [30.4, 48.5] |
| g3 AG v3 | cz | before | 53 | 6 | 61 | 50.8 % [41.6, 60.1] |
| g3 AG v3 | cz | after | 59 | 16 | 45 | 37.5 % [28.8, 46.8] |
| g3 AG v3 | sk | before | 55 | 18 | 47 | 39.2 % [30.4, 48.5] |
| g3 AG v3 | sk | after | 55 | 18 | 47 | 39.2 % [30.4, 48.5] |
| g4 voice v2 | cz | before | 108 | 0 | 12 (as_active 6, as_passive 6) | 10.0 % [5.3, 16.8] |
| g4 voice v2 | cz | after | 100 | 0 | 20 (as_active 4, as_passive 16) | 16.7 % [10.5, 24.6] |
| g4 voice v2 | sk | before | 98 | 0 | 22 (as_active 4, as_passive 18) | 18.3 % [11.9, 26.4] |
| g4 voice v2 | sk | after | 98 | 0 | 22 (as_active 4, as_passive 18) | 18.3 % [11.9, 26.4] |
| g4 voice v3 | cz | before | 105 | 0 | 15 (as_active 5, as_passive 10) | 12.5 % [7.2, 19.8] |
| g4 voice v3 | cz | after | 97 | 0 | 23 (as_active 3, as_passive 20) | 19.2 % [12.6, 27.4] |
| g4 voice v3 | sk | before | 98 | 0 | 22 (as_active 2, as_passive 20) | 18.3 % [11.9, 26.4] |
| g4 voice v3 | sk | after | 98 | 0 | 22 (as_active 2, as_passive 20) | 18.3 % [11.9, 26.4] |

Remaining F9 Czech ERROR (1): n=68 `barbell` loanword, not Czech-specific (Slovak has the same ERROR).

## C3. Ablation, each fix alone (Czech side)
| guard | lang | run | AGREE | CONSERVATIVE | ERROR | ERROR rate [95 % CI] |
|---|---|---|---|---|---|---|
| g1 F9 | cz | fix_em | 82 | 35 | 3 | 2.5 % [0.5, 7.1] |
| g1 F9 | cz | fix_se | 82 | 35 | 3 | 2.5 % [0.5, 7.1] |
| g1 F9 | cz | fix_jestli | 82 | 36 | 2 | 1.7 % [0.2, 5.9] |
| g1 F9 | cz | fix_aspect | 82 | 36 | 2 | 1.7 % [0.2, 5.9] |
| g2 F4v2 | cz | fix_em | 16 | 89 | 15 | 12.5 % [7.2, 19.8] |
| g2 F4v2 | cz | fix_se | 17 | 83 | 20 | 16.7 % [10.5, 24.6] |
| g2 F4v2 | cz | fix_jestli | 17 | 83 | 20 | 16.7 % [10.5, 24.6] |
| g2 F4v2 | cz | fix_aspect | 17 | 83 | 20 | 16.7 % [10.5, 24.6] |
| g3 AG v2 | cz | fix_em | 53 | 6 | 61 | 50.8 % [41.6, 60.1] |
| g3 AG v2 | cz | fix_se | 59 | 16 | 45 | 37.5 % [28.8, 46.8] |
| g3 AG v2 | cz | fix_jestli | 53 | 6 | 61 | 50.8 % [41.6, 60.1] |
| g3 AG v2 | cz | fix_aspect | 53 | 6 | 61 | 50.8 % [41.6, 60.1] |
| g3 AG v3 | cz | fix_em | 53 | 6 | 61 | 50.8 % [41.6, 60.1] |
| g3 AG v3 | cz | fix_se | 59 | 16 | 45 | 37.5 % [28.8, 46.8] |
| g3 AG v3 | cz | fix_jestli | 53 | 6 | 61 | 50.8 % [41.6, 60.1] |
| g3 AG v3 | cz | fix_aspect | 53 | 6 | 61 | 50.8 % [41.6, 60.1] |
| g4 voice v2 | cz | fix_em | 108 | 0 | 12 (as_active 6, as_passive 6) | 10.0 % [5.3, 16.8] |
| g4 voice v2 | cz | fix_se | 100 | 0 | 20 (as_active 4, as_passive 16) | 16.7 % [10.5, 24.6] |
| g4 voice v2 | cz | fix_jestli | 108 | 0 | 12 (as_active 6, as_passive 6) | 10.0 % [5.3, 16.8] |
| g4 voice v2 | cz | fix_aspect | 108 | 0 | 12 (as_active 6, as_passive 6) | 10.0 % [5.3, 16.8] |
| g4 voice v3 | cz | fix_em | 105 | 0 | 15 (as_active 5, as_passive 10) | 12.5 % [7.2, 19.8] |
| g4 voice v3 | cz | fix_se | 97 | 0 | 23 (as_active 3, as_passive 20) | 19.2 % [12.6, 27.4] |
| g4 voice v3 | cz | fix_jestli | 105 | 0 | 15 (as_active 5, as_passive 10) | 12.5 % [7.2, 19.8] |
| g4 voice v3 | cz | fix_aspect | 105 | 0 | 15 (as_active 5, as_passive 10) | 12.5 % [7.2, 19.8] |

Fixes are disjoint: `em` moves only guard 2, `se` only guards 3/4, `jestli` and `aspect` only guard 1.

## C4. Every Czech cell that changed class, before -> after
- g1: 15 ERROR->CONSERVATIVE, 29 ERROR->CONSERVATIVE
- g2: 17 ERROR->CONSERVATIVE, 21 ERROR->CONSERVATIVE, 61 ERROR->CONSERVATIVE, 83 ERROR->CONSERVATIVE, 87 ERROR->CONSERVATIVE, 105 AGREE->CONSERVATIVE
- g3 (v2 = v3): 3 AGREE->CONSERVATIVE, 4 ERROR->AGREE, 6 ERROR->AGREE, 17 ERROR->AGREE, 27 ERROR->CONSERVATIVE, 30 ERROR->AGREE, 31 ERROR->AGREE, 43 AGREE->CONSERVATIVE, 44 ERROR->CONSERVATIVE, 45 ERROR->AGREE, 46 ERROR->CONSERVATIVE, 50 AGREE->CONSERVATIVE, 59 AGREE->CONSERVATIVE, 61 AGREE->CONSERVATIVE, 71 AGREE->CONSERVATIVE, 80 ERROR->AGREE, 94 ERROR->AGREE, 97 AGREE->CONSERVATIVE, 102 ERROR->AGREE, 111 ERROR->AGREE, 112 ERROR->AGREE, 114 ERROR->AGREE, 120 ERROR->AGREE
- g4 v2 (= v3): 3 AGREE->ERROR_as_passive, 27 AGREE->ERROR_as_passive, 43 AGREE->ERROR_as_passive, 44 AGREE->ERROR_as_passive, 46 AGREE->ERROR_as_passive, 50 AGREE->ERROR_as_passive, 59 AGREE->ERROR_as_passive, 61 AGREE->ERROR_as_passive, 71 AGREE->ERROR_as_passive, 97 AGREE->ERROR_as_passive, 102 ERROR_as_active->AGREE, 120 ERROR_as_active->AGREE

## C5. End to end (AG `decide` on the English reference)
0 false rejections on cz and sk, before and after, `ann` empty and gold-injected, v2 and v3; 0 crashes.
The AG gate stays inert on Czech (no Czech annotation exists), so none of this reaches a learner yet.

## C6. Not done / out of scope
No Czech probe, no Czech test set (per brief). Not fixed (not named): Czech `si` dative over-fire; Czech
`-ím` dative/instrumental (n=79, 112); `SK_PRON` demonstrative `ty` (n=31, 47, 111); relative-clause scope
(11 cz); Czech `BUD/COP/jsem` lexicon (F9 CONSERVATIVE 35 -> 37, i.e. no coverage recovered); first-word agent
heuristic (45 errors remain). Single blind gold per language, one 120-sentence sample: a PROBE, not a measurement.
