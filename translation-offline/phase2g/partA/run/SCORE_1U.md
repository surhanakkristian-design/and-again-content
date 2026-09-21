# SCORE_1U - the fresh 1U set (AG v4, P-FROZEN-1U), 0 model calls

Coverage = judged-correct accepted / judged-correct.  FA = judged-wrong accepted / judged-wrong.  Exact 95 % Clopper-Pearson; P1 = odd sid, P2 = even sid; never averaged.

## headline (the judge labels)

| figure | k/n, point, 95 % CI | target |
| --- | --- | --- |
| coverage pooled | 149/182 = 81.87 % [75.49, 87.18] | MISSED on the point, MISSED on the interval |
| FA pooled | 10/178 = 5.62 % [2.73, 10.09] | MISSED on the point, MISSED on the interval |
| coverage P1 | 73/91 = 80.22 % [70.55, 87.84] | MISSED on the point, MISSED on the interval |
| FA P1 | 5/89 = 5.62 % [1.85, 12.63] | MISSED on the point, MISSED on the interval |
| coverage P2 | 76/91 = 83.52 % [74.27, 90.47] | MISSED on the point, MISSED on the interval |
| FA P2 | 5/89 = 5.62 % [1.85, 12.63] | MISSED on the point, MISSED on the interval |
| Fisher P1 vs P2 (coverage) | p = 0.7008 | |
| Fisher P1 vs P2 (FA) | p = 1.0 | |

## cells, one per line

* missing-article, judged wrong: FA 3/27 = 11.11 % [2.35, 29.16], rejected by layer {"F4v2": 1, "L3": 11, "L3:TIPrej": 12}
* missing-article, judged correct: n = 2, coverage 0/2 = 0.00 % [0.00, 84.19]
* agent-drop FA (all, writer tag among judged-wrong): 2/22 = 9.09 % [1.12, 29.16] (AG fired 13)
* agent-drop FA (main, writer tag among judged-wrong): 2/19 = 10.53 % [1.30, 33.14] (AG fired 12)
* agent-drop FA (fronted, writer tag among judged-wrong): 0/1 = 0.00 % [0.00, 97.50] (AG fired 0)
* agent-drop FA (misaligned, writer tag among judged-wrong): - (AG fired 0)
* agent-drop FA (other, writer tag among judged-wrong): 0/2 = 0.00 % [0.00, 84.19] (AG fired 1)
* by-passive coverage: 17/24 = 70.83 % [48.91, 87.38]
* SKP coverage: 2/2 = 100.00 % [15.81, 100.00]
* time-frame FA: 0/52 = 0.00 % [0.00, 6.85]
* AG v4: fired 13, catches 13, measured cost (judged-correct rejected) 0
* AG shadow v2 (offline, same items): fired 11, catches 11, cost 0
* AG shadow v3 (offline, same items): fired 13, catches 13, cost 0
* AG shadow guarded_union (offline, same items): fired 13, catches 13, cost 0
* AG shadow v4_full (offline, same items): fired 13, catches 13, cost 0
* false accepts by layer: {"L3": 10}
* false rejections by layer: {"F4v2": 7, "L3": 16, "L3:TIPrej": 10}
* true rejections by layer: {"AG": 13, "F4v2": 5, "F5": 14, "L3": 114, "L3:TIPrej": 22}
* FA, judged type T: 0/52 = 0.00 % [0.00, 6.85]
* FA, judged type W: 2/40 = 5.00 % [0.61, 16.92]
* FA, judged type M: 5/55 = 9.09 % [3.02, 19.95]
* FA, judged type S: 3/31 = 9.68 % [2.04, 25.75]
* level A1: coverage 39/45 = 86.67 % [73.21, 94.95], FA 2/45 = 4.44 % [0.54, 15.15]
* level A2: coverage 42/45 = 93.33 % [81.73, 98.60], FA 2/45 = 4.44 % [0.54, 15.15]
* level B1: coverage 32/46 = 69.57 % [54.25, 82.26], FA 0/44 = 0.00 % [0.00, 8.04]
* level B2: coverage 36/46 = 78.26 % [63.64, 89.05], FA 6/44 = 13.64 % [5.17, 27.35]
* model replies: {"DIFF": 130, "SAME": 133, "TIP": 32}; failed calls 0
* tokens in/out 162952/0, latency mean 544.5 ms, spend <= $0.0163 (UPPER BOUND at the published flash-lite list price ($0.10/1M in, $0.40/1M out); free-tier calls cost 0)
* judge noise on the 80 duplicate controls: null

## pre-declared sensitivities (SPLIT_1U.md S1-S6)

| sensitivity | n moved | coverage pooled | FA pooled | coverage P1 / P2 | FA P1 / P2 |
| --- | --- | --- | --- | --- | --- |
| S1_writer_intent | 4 | 149/180 = 82.78 % [76.45, 87.99] | 10/180 = 5.56 % [2.70, 9.98] | 73/90 = 81.11 % [71.49, 88.59] / 76/90 = 84.44 % [75.28, 91.23] | 5/90 = 5.56 % [1.83, 12.49] / 5/90 = 5.56 % [1.83, 12.49] |
| S2_wrong_borderline_correct | 24 | 155/206 = 75.24 % [68.77, 80.98] | 4/154 = 2.60 % [0.71, 6.52] | 76/102 = 74.51 % [64.92, 82.62] / 79/104 = 75.96 % [66.59, 83.80] | 2/78 = 2.56 % [0.31, 8.96] / 2/76 = 2.63 % [0.32, 9.18] |
| S3_correct_borderline_wrong | 20 | 137/162 = 84.57 % [78.07, 89.76] | 22/198 = 11.11 % [7.10, 16.34] | 61/75 = 81.33 % [70.67, 89.40] / 76/87 = 87.36 % [78.50, 93.52] | 17/105 = 16.19 % [9.72, 24.65] / 5/93 = 5.38 % [1.77, 12.10] |
| S4_exclude_S2_S3 | 44 | 137/162 = 84.57 % [78.07, 89.76] | 4/154 = 2.60 % [0.71, 6.52] | 61/75 = 81.33 % [70.67, 89.40] / 76/87 = 87.36 % [78.50, 93.52] | 2/78 = 2.56 % [0.31, 8.96] / 2/76 = 2.63 % [0.32, 9.18] |
| S5_article_pre_ruling | 27 | 152/209 = 72.73 % [66.15, 78.64] | 7/151 = 4.64 % [1.88, 9.32] | 75/105 = 71.43 % [61.79, 79.82] / 77/104 = 74.04 % [64.52, 82.14] | 3/75 = 4.00 % [0.83, 11.25] / 4/76 = 5.26 % [1.45, 12.93] |
| S6_leave_out_A1 | 90 | 110/137 = 80.29 % [72.64, 86.59] | 8/133 = 6.02 % [2.63, 11.51] | 49/64 = 76.56 % [64.31, 86.25] / 61/73 = 83.56 % [73.05, 91.21] | 5/62 = 8.06 % [2.67, 17.83] / 3/71 = 4.23 % [0.88, 11.86] |
| S6_leave_out_A2 | 90 | 107/137 = 78.10 % [70.24, 84.71] | 8/133 = 6.02 % [2.63, 11.51] | 52/67 = 77.61 % [65.78, 86.89] / 55/70 = 78.57 % [67.13, 87.48] | 4/65 = 6.15 % [1.70, 15.01] / 4/68 = 5.88 % [1.63, 14.38] |
| S6_leave_out_B1 | 90 | 117/136 = 86.03 % [79.05, 91.37] | 10/134 = 7.46 % [3.64, 13.30] | 62/72 = 86.11 % [75.94, 93.13] / 55/64 = 85.94 % [74.98, 93.36] | 5/72 = 6.94 % [2.29, 15.47] / 5/62 = 8.06 % [2.67, 17.83] |
| S6_leave_out_B2 | 90 | 113/136 = 83.09 % [75.71, 88.97] | 4/134 = 2.99 % [0.82, 7.47] | 56/70 = 80.00 % [68.73, 88.61] / 57/66 = 86.36 % [75.69, 93.57] | 1/68 = 1.47 % [0.04, 7.92] / 3/66 = 4.55 % [0.95, 12.71] |

### targets under each sensitivity (point / interval)

* S1_writer_intent: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S2_wrong_borderline_correct: coverage MISSED on the point, MISSED on the interval; FA MET on the point, MISSED on the interval
* S3_correct_borderline_wrong: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S4_exclude_S2_S3: coverage MISSED on the point, MISSED on the interval; FA MET on the point, MISSED on the interval
* S5_article_pre_ruling: coverage MISSED on the point, MISSED on the interval; FA MET on the point, MISSED on the interval
* S6_leave_out_A1: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_A2: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_B1: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_B2: coverage MISSED on the point, MISSED on the interval; FA MET on the point, MISSED on the interval

## every false accept

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| C:220057:c1 | 220057 | L3 | plain | Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať. | They need to have the old accordion repaired before the keys stop working completely. |
| W:220025:w1 | 220025 | L3 | drop-main | Poprosila ma, aby som nehýbal rukou, kým spí. | I was asked not to move my arm while she was sleeping. |
| W:220027:w2 | 220027 | L3 | missing-article | Vločky sú v miske – hneď ich zje | The flakes are in bowl – he's going to eat them right away. |
| W:220028:w2 | 220028 | L3 | plain | Pred vhadzovaním si dala omotať hokejku páskou. | Before the face-off, she had her hockey stick wrapped. |
| W:220034:w1 | 220034 | L3 | missing-article | On má sivú handričku na čistenie auta. | He has got grey cloth for cleaning the car. |
| W:220039:w3 | 220039 | L3 | determiner | O šiestej už bude búchať do tých lap dve hodiny v kuse. | By six o'clock he will have been pounding some mitts for two hours straight. |
| W:220044:w2 | 220044 | L3 | plain | Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach. | By the time he reached the narrow path, he had been climbing down the ledges for an hour. |
| W:220046:w2 | 220046 | L3 | drop-main | Takže mi povedal, že v meste nejazdí veľkou rýchlosťou. | So I was told that he doesn't drive at high speed in the city. |
| W:220055:w1 | 220055 | L3 | missing-article | Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska. | They write their name on last page of the contract for the new job and the office applauds. |
| W:220056:w1 | 220056 | L3 | determiner | Táto váha ukazuje oveľa viac ako pred chvíľou. | That scale shows a lot more than a moment ago. |

## every false rejection

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| C:220002:c1 | 220002 | L3:TIPrej | plain | Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký. | Girl, he told me that the iceberg was huge; he must have felt so tiny there. |
| C:220002:c3 | 220002 | L3 | by-passive | Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký. | Girl, I was told by him that the iceberg was huge; he must have felt so tiny there. |
| C:220003:c2 | 220003 | L3 | by-passive | Model stíhačky opeká chlieb približne tri minúty. | The bread has been toasted by the model fighter jet for about three minutes. |
| C:220003:c3 | 220003 | L3 | aspect | Model stíhačky opeká chlieb približne tri minúty. | The model of the fighter jet toasts the bread for approximately three minutes. |
| C:220005:c1 | 220005 | F4v2 | plain | Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo. | The guard can't know about the cheese - he raises the ramp too quickly. |
| C:220005:c3 | 220005 | F4v2 | plain | Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo. | The guard can't know about the cheese; he lifts the barrier too quickly. |
| C:220016:c1 | 220016 | L3 | plain | Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli! | By the time he switched on the kettle, everyone who was staring at his moustache had fallen completely silent! |
| C:220016:c2 | 220016 | L3 | plain | Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli! | By the time he turned on the kettle, everyone staring at his moustache went completely silent! |
| C:220016:c3 | 220016 | L3 | by-passive | Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli! | By the time the kettle had been switched on by him, everyone who was staring at his moustache fell completely silent! |
| C:220021:c1 | 220021 | L3 | plain | Hore je vietor. Môžeš vidieť tú vlajku? | It's windy up there. Can you see the flag? |
| C:220021:c2 | 220021 | L3:TIPrej | determiner | Hore je vietor. Môžeš vidieť tú vlajku? | There's wind up there. Can you see that flag? |
| C:220023:c3 | 220023 | L3:TIPrej | number | Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky. | Listen, she said they have the same dresses, but they're still friends. |
| C:220025:c1 | 220025 | F4v2 | plain | Poprosila ma, aby som nehýbal rukou, kým spí. | She asked me not to move my arm while she was sleeping. |
| C:220025:c2 | 220025 | F4v2 | plain | Poprosila ma, aby som nehýbal rukou, kým spí. | She asked me not to move my hand while she slept. |
| C:220030:c3 | 220030 | L3:TIPrej | plain | Fanúšik má jednu pomaľovanú tvár a šálu. | The fan has got one painted face and a scarf. |
| C:220032:c2 | 220032 | L3 | by-passive | Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty. | The same two slices have been heated by the fighter-jet toaster for three minutes. |
| C:220039:c2 | 220039 | L3:TIPrej | plain | O šiestej už bude búchať do tých lap dve hodiny v kuse. | At six he'll have been pounding those pads for two solid hours. |
| C:220040:c1 | 220040 | L3 | plain | Žena mu na krk zavesí jednu zlatú medailu. | The woman will hang a gold medal around his neck. |
| C:220040:c2 | 220040 | L3:TIPrej | plain | Žena mu na krk zavesí jednu zlatú medailu. | The woman is going to hang one gold medal on his neck. |
| C:220041:c1 | 220041 | L3:TIPrej | plain | Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt. | Dude, the door is already open, so it reveals the whole valley, really. |
| C:220045:c3 | 220045 | L3:TIPrej | plain | Jedna košeľa, jeden golier a dve červené kravaty. | One shirt, one collar, two red ties. |
| C:220048:c3 | 220048 | L3 | plain | Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala. | I won't lie, you were the most charming clerk; she never smiled like that before. |
| C:220049:c2 | 220049 | L3:TIPrej | plain | Ryby majú plán. Idú uplávať preč od žraloka. | The fish have got a plan. They're going to swim off away from the shark. |
| C:220050:c3 | 220050 | L3:TIPrej | by-passive | V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej. | The moment the crutch fell onto the wet floor, it was grabbed firmly by him and he went on. |
| C:220051:c3 | 220051 | L3 | by-passive | Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda. | Membership has been requested by about forty students at the club fair since noon. |
| C:220053:c1 | 220053 | F4v2 | plain | Pamätník zbožňoval, a samozrejme aj jeho fotoaparát. | He adored the monument, and so did his camera, of course. |
| C:220053:c2 | 220053 | F4v2 | plain | Pamätník zbožňoval, a samozrejme aj jeho fotoaparát. | He loved the memorial, and of course his camera did too. |
| C:220057:c3 | 220057 | L3 | plain | Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať. | Before the keys stop working completely, they need to have the old accordion repaired. |
| C:220060:c1 | 220060 | L3 | plain | Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach. | You should have checked the pegs before that match - two came loose in the first ten minutes. |
| C:220060:c2 | 220060 | L3 | plain | Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach. | You ought to have checked the pegs before that match; two of them worked loose within the first ten minutes. |
| C:220060:c3 | 220060 | L3 | by-passive | Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach. | The pegs should have been checked by you before that match - two came loose in the first ten minutes. |
| W:220002:w3 | 220002 | L3 | missing-article | Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký. | Girl, he told me that iceberg was huge; he must have felt so tiny there. |
| W:220005:w3 | 220005 | F4v2 | missing-article | Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo. | The guard can't know about cheese - he raises the ramp too quickly. |

## failed calls (counted, never guessed, never silently retried)

```
[]
```

an empty or unparsable HTTP 200 reply is a FAILED call: it is counted against the cap, never guessed and never silently retried; the item keeps the stack decision it gets without a model verdict (a rejection), stays in its own denominator and is listed under detail.failed_calls

