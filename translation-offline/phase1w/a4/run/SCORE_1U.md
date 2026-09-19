# SCORE_1U - the fresh 1U set (AG v4, P-FROZEN-1U), 0 model calls

Coverage = judged-correct accepted / judged-correct.  FA = judged-wrong accepted / judged-wrong.  Exact 95 % Clopper-Pearson; P1 = odd sid, P2 = even sid; never averaged.

## headline (the judge labels)

| figure | k/n, point, 95 % CI | target |
| --- | --- | --- |
| coverage pooled | 392/401 = 97.76 % [95.78, 98.97] | MET on the point, MET on the interval |
| FA pooled | 16/499 = 3.21 % [1.84, 5.15] | MET on the point, MISSED on the interval |
| coverage P1 | 195/200 = 97.50 % [94.26, 99.18] | MET on the point, MET on the interval |
| FA P1 | 5/250 = 2.00 % [0.65, 4.61] | MET on the point, MET on the interval |
| coverage P2 | 197/201 = 98.01 % [94.98, 99.46] | MET on the point, MET on the interval |
| FA P2 | 11/249 = 4.42 % [2.23, 7.77] | MET on the point, MISSED on the interval |
| Fisher P1 vs P2 (coverage) | p = 0.7508 | |
| Fisher P1 vs P2 (FA) | p = 0.1366 | |

## cells, one per line

* missing-article, judged wrong: FA 3/97 = 3.09 % [0.64, 8.77], rejected by layer {"AG": 1, "L3": 66, "L3:TIPrej": 27}
* missing-article, judged correct: n = 0, coverage -
* agent-drop FA (all, writer tag among judged-wrong): 10/160 = 6.25 % [3.04, 11.19] (AG fired 138)
* agent-drop FA (main, writer tag among judged-wrong): 0/48 = 0.00 % [0.00, 7.40] (AG fired 48)
* agent-drop FA (fronted, writer tag among judged-wrong): 7/64 = 10.94 % [4.51, 21.25] (AG fired 55)
* agent-drop FA (misaligned, writer tag among judged-wrong): 3/48 = 6.25 % [1.31, 17.20] (AG fired 35)
* agent-drop FA (other, writer tag among judged-wrong): - (AG fired 0)
* by-passive coverage: 79/80 = 98.75 % [93.23, 99.97]
* SKP coverage: 70/72 = 97.22 % [90.32, 99.66]
* time-frame FA: 2/119 = 1.68 % [0.20, 5.94]
* AG v4: fired 144, catches 141, measured cost (judged-correct rejected) 3
* AG shadow v2 (offline, same items): fired 92, catches 92, cost 0
* AG shadow v3 (offline, same items): fired 110, catches 110, cost 0
* AG shadow guarded_union (offline, same items): fired 115, catches 114, cost 1
* AG shadow v4_full (offline, same items): fired 142, catches 139, cost 3
* false accepts by layer: {"L3": 16}
* false rejections by layer: {"AG": 3, "F2B": 1, "L3": 2, "L3:TIPrej": 3}
* true rejections by layer: {"AG": 141, "F5": 2, "L3": 309, "L3:TIPrej": 31}
* FA, judged type T: 2/119 = 1.68 % [0.20, 5.94]
* FA, judged type W: 1/120 = 0.83 % [0.02, 4.56]
* FA, judged type M: 10/160 = 6.25 % [3.04, 11.19]
* FA, judged type S: 3/100 = 3.00 % [0.62, 8.52]
* level A1: coverage 98/100 = 98.00 % [92.96, 99.76], FA 0/125 = 0.00 % [0.00, 2.91]
* level A2: coverage 95/100 = 95.00 % [88.72, 98.36], FA 5/125 = 4.00 % [1.31, 9.09]
* level B1: coverage 99/100 = 99.00 % [94.55, 99.97], FA 5/125 = 4.00 % [1.31, 9.09]
* level B2: coverage 100/101 = 99.01 % [94.61, 99.97], FA 6/124 = 4.84 % [1.80, 10.23]
* model replies: {"DIFF": 311, "SAME": 252, "TIP": 37}; failed calls 0
* tokens in/out 326015/0, latency mean 659.8 ms, spend <= $0.0326 (UPPER BOUND at the published flash-lite list price ($0.10/1M in, $0.40/1M out); free-tier calls cost 0)
* judge noise on the 80 duplicate controls: {"join_labels_1u.json": null, "assemble_1u.json": null}

## pre-declared sensitivities (SPLIT_1U.md S1-S6)

| sensitivity | n moved | coverage pooled | FA pooled | coverage P1 / P2 | FA P1 / P2 |
| --- | --- | --- | --- | --- | --- |
| S1_writer_intent | 1 | 391/400 = 97.75 % [95.77, 98.97] | 17/500 = 3.40 % [1.99, 5.39] | 195/200 = 97.50 % [94.26, 99.18] / 196/200 = 98.00 % [94.96, 99.45] | 5/250 = 2.00 % [0.65, 4.61] / 12/250 = 4.80 % [2.50, 8.23] |
| S2_wrong_borderline_correct | 20 | 397/421 = 94.30 % [91.64, 96.31] | 11/479 = 2.30 % [1.15, 4.07] | 196/207 = 94.69 % [90.69, 97.32] / 201/214 = 93.93 % [89.84, 96.73] | 4/243 = 1.65 % [0.45, 4.16] / 7/236 = 2.97 % [1.20, 6.02] |
| S3_correct_borderline_wrong | 20 | 375/381 = 98.43 % [96.60, 99.42] | 33/519 = 6.36 % [4.42, 8.81] | 187/191 = 97.91 % [94.72, 99.43] / 188/190 = 98.95 % [96.25, 99.87] | 13/259 = 5.02 % [2.70, 8.43] / 20/260 = 7.69 % [4.76, 11.63] |
| S4_exclude_S2_S3 | 40 | 375/381 = 98.43 % [96.60, 99.42] | 11/479 = 2.30 % [1.15, 4.07] | 187/191 = 97.91 % [94.72, 99.43] / 188/190 = 98.95 % [96.25, 99.87] | 4/243 = 1.65 % [0.45, 4.16] / 7/236 = 2.97 % [1.20, 6.02] |
| S5_article_pre_ruling | 97 | 395/498 = 79.32 % [75.49, 82.79] | 13/402 = 3.23 % [1.73, 5.47] | 196/247 = 79.35 % [73.76, 84.22] / 199/251 = 79.28 % [73.74, 84.12] | 4/203 = 1.97 % [0.54, 4.97] / 9/199 = 4.52 % [2.09, 8.41] |
| S6_leave_out_A1 | 225 | 294/301 = 97.67 % [95.27, 99.06] | 16/374 = 4.28 % [2.46, 6.85] | 143/148 = 96.62 % [92.29, 98.89] / 151/153 = 98.69 % [95.36, 99.84] | 5/185 = 2.70 % [0.88, 6.19] / 11/189 = 5.82 % [2.94, 10.17] |
| S6_leave_out_A2 | 225 | 297/301 = 98.67 % [96.63, 99.64] | 11/374 = 2.94 % [1.48, 5.20] | 151/152 = 99.34 % [96.39, 99.98] / 146/149 = 97.99 % [94.23, 99.58] | 2/190 = 1.05 % [0.13, 3.75] / 9/184 = 4.89 % [2.26, 9.08] |
| S6_leave_out_B1 | 225 | 293/301 = 97.34 % [94.83, 98.85] | 11/374 = 2.94 % [1.48, 5.20] | 144/148 = 97.30 % [93.22, 99.26] / 149/153 = 97.39 % [93.44, 99.28] | 4/185 = 2.16 % [0.59, 5.44] / 7/189 = 3.70 % [1.50, 7.48] |
| S6_leave_out_B2 | 225 | 292/300 = 97.33 % [94.81, 98.84] | 10/375 = 2.67 % [1.29, 4.85] | 147/152 = 96.71 % [92.49, 98.92] / 145/148 = 97.97 % [94.19, 99.58] | 4/190 = 2.11 % [0.58, 5.30] / 6/185 = 3.24 % [1.20, 6.93] |

### targets under each sensitivity (point / interval)

* S1_writer_intent: coverage MET on the point, MET on the interval; FA MET on the point, MISSED on the interval
* S2_wrong_borderline_correct: coverage MET on the point, MET on the interval; FA MET on the point, MET on the interval
* S3_correct_borderline_wrong: coverage MET on the point, MET on the interval; FA MISSED on the point, MISSED on the interval
* S4_exclude_S2_S3: coverage MET on the point, MET on the interval; FA MET on the point, MET on the interval
* S5_article_pre_ruling: coverage MISSED on the point, MISSED on the interval; FA MET on the point, MISSED on the interval
* S6_leave_out_A1: coverage MET on the point, MET on the interval; FA MET on the point, MISSED on the interval
* S6_leave_out_A2: coverage MET on the point, MET on the interval; FA MET on the point, MISSED on the interval
* S6_leave_out_B1: coverage MET on the point, MET on the interval; FA MET on the point, MISSED on the interval
* S6_leave_out_B2: coverage MET on the point, MET on the interval; FA MET on the point, MET on the interval

## every false accept

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| W:200030:w4 | 200030 | L3 | missing-article | Ak Janko umyje riad, mama upečie koláč pre deti. | If Janko washes the dishes, Mum will bake cake for the children. |
| W:200031:w2 | 200031 | L3 | drop-fronted | Len čo poštár priniesol listy, babka si nasadila okuliare. | Grandma put on her glasses as soon as the letters arrived by post. |
| W:200035:w2 | 200035 | L3 | drop-misaligned | Deti si myslia, že babka upečie tortu v sobotu. | On Saturday a cake is going to be baked, the children think. |
| W:200035:w4 | 200035 | L3 | missing-article | Deti si myslia, že babka upečie tortu v sobotu. | The children think that Grandma will bake cake on Saturday. |
| W:200038:w2 | 200038 | L3 | drop-misaligned | Ja som stratil knihu, ktorú mi požičala učiteľka. | The book that was lent to me was lost by me. |
| W:200052:w2 | 200052 | L3 | drop-fronted | Kým učiteľka vysvetľovala nové pravidlá, žiaci si potichu prepisovali poznámky z tabule. | The pupils quietly copied the notes from the board while the new rules got explained. |
| W:200056:w2 | 200056 | L3 | drop-fronted | Ak lekárka predpíše silnejšie antibiotiká, môj brat sa uzdraví do konca týždňa. | My brother will get better by the end of the week if stronger antibiotics get prescribed. |
| W:200061:w2 | 200061 | L3 | drop-misaligned | Ranné vlaky meškali, a preto môj kolega odviezol turistov na letisko autobusom. | The tourists got driven to the airport by bus, because the morning trains were late. |
| W:200064:w5 | 200064 | L3 | wrong-word | Ja som čakal pred kinom, ale môj kamarát medzitým kúpil lístky na neskorší film. | I was waiting in front of the theatre, but in the meantime my friend bought the tickets for a later film. |
| W:200066:w4 | 200066 | L3 | missing-article | Moja teta šije svadobné šaty ručne v malej dielni na hlavnej ulici. | My aunt sews wedding dresses by hand in a small workshop on main street. |
| W:200076:w2 | 200076 | L3 | drop-fronted | Keď dopravný podnik zavedie nové jazdné poriadky, cestujúci si budú musieť zvyknúť na kratšie prestupy. | Passengers will have to get used to shorter connections as soon as the new timetables get introduced. |
| W:200078:w2 | 200078 | L3 | drop-fronted | Keďže organizátori zrušili nedeľný pretek, mnohí bežci strávili celé popoludnie v miestnej kaviarni. | Because of the cancelled Sunday race, many runners spent the whole afternoon in the local café. |
| W:200079:w2 | 200079 | L3 | drop-fronted | Pretože učiteľka fyziky vysvetľuje pokusy veľmi trpezlivo, celá trieda rozumie aj náročnejším témam. | Thanks to the very patient explanation of the experiments, the whole class understands even the harder topics. |
| W:200080:w2 | 200080 | L3 | drop-fronted | Hoci sused opravil spoločnú bránu už minulý týždeň, správca budovy ešte stále nepodpísal protokol. | Despite the repair of the shared gate last week, the building manager still has not signed the report. |
| W:200084:w3 | 200084 | L3 | time-frame | Riaditeľka oznámila, že nový technik vymení všetky staré počítače počas jesenných prázdnin. | The headmistress announces that the new technician will replace all the old computers during the autumn holidays. |
| W:200086:w3 | 200086 | L3 | time-frame | Predavačka tvrdí, že výrobca znížil ceny všetkých bicyklov už v polovici sezóny. | The shop assistant claimed that the manufacturer had lowered the prices of all the bicycles in the middle of the season. |

## every false rejection

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| C:200006:c2 | 200006 | L3 | determiner | Len čo Martin napíše list, mama pôjde na poštu. | As soon as Martin writes a letter, Mum will go to the post office. |
| C:200008:c3 | 200008 | L3 | by-passive | Odkedy Tomáš predáva ovocie, ľudia chodia do obchodu. | Since the fruit is sold by Tomáš, people go to the shop. |
| C:200027:c1 | 200027 | AG | plain | Pretože vodič zabudol mapu, turisti zablúdili v lese. | Because the driver forgot the map, the tourists got lost in the forest. |
| C:200027:c2 | 200027 | AG | determiner | Pretože vodič zabudol mapu, turisti zablúdili v lese. | Because the driver forgot the map, the tourists got lost in a forest. |
| C:200027:c4 | 200027 | AG | paraphrase | Pretože vodič zabudol mapu, turisti zablúdili v lese. | The tourists got lost in the woods because the driver forgot the map. |
| C:200049:c4 | 200049 | L3:TIPrej | skp-passive,determiner | Trieda bola vyzdobená kvetmi pred oslavou. | The classroom was decorated with the flowers before the celebration. |
| C:200050:c3 | 200050 | L3:TIPrej | paraphrase | Dom sa stavia už dva roky. | The house has been getting built for two years. |
| C:200071:c2 | 200071 | L3:TIPrej | skp-passive | Nový most nad riekou sa stavia už viac ako dva roky. | The new bridge over the river has been being built for more than two years. |
| C:200094:c2 | 200094 | F2B | determiner | Miestny spolok zorganizuje výstavu mačiek v kultúrnom dome už na jeseň. | The local association will organise the cat show in the culture house in the autumn. |

## failed calls (counted, never guessed, never silently retried)

```
[]
```

an empty or unparsable HTTP 200 reply is a FAILED call: it is counted against the cap, never guessed and never silently retried; the item keeps the stack decision it gets without a model verdict (a rejection), stays in its own denominator and is listed under detail.failed_calls

