# SCORE_1U - the fresh 1U set (AG v4, P-FROZEN-1U), 0 model calls

Coverage = judged-correct accepted / judged-correct.  FA = judged-wrong accepted / judged-wrong.  Exact 95 % Clopper-Pearson; P1 = odd sid, P2 = even sid; never averaged.

## headline (the judge labels)

| figure | k/n, point, 95 % CI | target |
| --- | --- | --- |
| coverage pooled | 154/182 = 84.62 % [78.54, 89.53] | MISSED on the point, MISSED on the interval |
| FA pooled | 11/178 = 6.18 % [3.12, 10.79] | MISSED on the point, MISSED on the interval |
| coverage P1 | 76/91 = 83.52 % [74.27, 90.47] | MISSED on the point, MISSED on the interval |
| FA P1 | 4/89 = 4.49 % [1.24, 11.11] | MET on the point, MISSED on the interval |
| coverage P2 | 78/91 = 85.71 % [76.81, 92.17] | MISSED on the point, MISSED on the interval |
| FA P2 | 7/89 = 7.87 % [3.22, 15.54] | MISSED on the point, MISSED on the interval |
| Fisher P1 vs P2 (coverage) | p = 0.8376 | |
| Fisher P1 vs P2 (FA) | p = 0.5356 | |

## cells, one per line

* missing-article, judged wrong: FA 3/27 = 11.11 % [2.35, 29.16], rejected by layer {"F4v2": 1, "L3": 8, "L3:TIPrej": 15}
* missing-article, judged correct: n = 2, coverage 1/2 = 50.00 % [1.26, 98.74]
* agent-drop FA (all, writer tag among judged-wrong): 2/22 = 9.09 % [1.12, 29.16] (AG fired 13)
* agent-drop FA (main, writer tag among judged-wrong): 2/19 = 10.53 % [1.30, 33.14] (AG fired 12)
* agent-drop FA (fronted, writer tag among judged-wrong): 0/1 = 0.00 % [0.00, 97.50] (AG fired 0)
* agent-drop FA (misaligned, writer tag among judged-wrong): - (AG fired 0)
* agent-drop FA (other, writer tag among judged-wrong): 0/2 = 0.00 % [0.00, 84.19] (AG fired 1)
* by-passive coverage: 20/24 = 83.33 % [62.62, 95.26]
* SKP coverage: 2/2 = 100.00 % [15.81, 100.00]
* time-frame FA: 1/52 = 1.92 % [0.05, 10.26]
* AG v4: fired 13, catches 13, measured cost (judged-correct rejected) 0
* AG shadow v2 (offline, same items): fired 11, catches 11, cost 0
* AG shadow v3 (offline, same items): fired 13, catches 13, cost 0
* AG shadow guarded_union (offline, same items): fired 13, catches 13, cost 0
* AG shadow v4_full (offline, same items): fired 13, catches 13, cost 0
* false accepts by layer: {"L3": 11}
* false rejections by layer: {"F4v2": 7, "L3": 16, "L3:TIPrej": 5}
* true rejections by layer: {"AG": 13, "F2B": 1, "F3": 4, "F4v2": 6, "F5": 4, "L3": 115, "L3:TIPrej": 24}
* FA, judged type T: 1/52 = 1.92 % [0.05, 10.26]
* FA, judged type W: 1/40 = 2.50 % [0.06, 13.16]
* FA, judged type M: 6/55 = 10.91 % [4.11, 22.25]
* FA, judged type S: 3/31 = 9.68 % [2.04, 25.75]
* level A1: coverage 37/45 = 82.22 % [67.95, 92.00], FA 2/45 = 4.44 % [0.54, 15.15]
* level A2: coverage 44/45 = 97.78 % [88.23, 99.94], FA 2/45 = 4.44 % [0.54, 15.15]
* level B1: coverage 34/46 = 73.91 % [58.87, 85.73], FA 1/44 = 2.27 % [0.06, 12.02]
* level B2: coverage 39/46 = 84.78 % [71.13, 93.66], FA 6/44 = 13.64 % [5.17, 27.35]
* model replies: {"DIFF": 131, "SAME": 151, "TIP": 30}; failed calls 0
* tokens in/out 162085/0, latency mean 528.5 ms, spend <= $0.0162 (UPPER BOUND at the published flash-lite list price ($0.10/1M in, $0.40/1M out); free-tier calls cost 0)
* judge noise on the 80 duplicate controls: null

## pre-declared sensitivities (SPLIT_1U.md S1-S6)

| sensitivity | n moved | coverage pooled | FA pooled | coverage P1 / P2 | FA P1 / P2 |
| --- | --- | --- | --- | --- | --- |
| S1_writer_intent | 4 | 153/180 = 85.00 % [78.93, 89.88] | 12/180 = 6.67 % [3.49, 11.36] | 76/90 = 84.44 % [75.28, 91.23] / 77/90 = 85.56 % [76.57, 92.08] | 4/90 = 4.44 % [1.22, 10.99] / 8/90 = 8.89 % [3.92, 16.77] |
| S2_wrong_borderline_correct | 24 | 160/206 = 77.67 % [71.36, 83.16] | 5/154 = 3.25 % [1.06, 7.41] | 79/102 = 77.45 % [68.11, 85.14] / 81/104 = 77.88 % [68.69, 85.43] | 1/78 = 1.28 % [0.03, 6.94] / 4/76 = 5.26 % [1.45, 12.93] |
| S3_correct_borderline_wrong | 20 | 141/162 = 87.04 % [80.87, 91.79] | 24/198 = 12.12 % [7.92, 17.50] | 63/75 = 84.00 % [73.72, 91.45] / 78/87 = 89.66 % [81.27, 95.16] | 17/105 = 16.19 % [9.72, 24.65] / 7/93 = 7.53 % [3.08, 14.90] |
| S4_exclude_S2_S3 | 44 | 141/162 = 87.04 % [80.87, 91.79] | 5/154 = 3.25 % [1.06, 7.41] | 63/75 = 84.00 % [73.72, 91.45] / 78/87 = 89.66 % [81.27, 95.16] | 1/78 = 1.28 % [0.03, 6.94] / 4/76 = 5.26 % [1.45, 12.93] |
| S5_article_pre_ruling | 27 | 157/209 = 75.12 % [68.69, 80.83] | 8/151 = 5.30 % [2.31, 10.17] | 77/105 = 73.33 % [63.81, 81.49] / 80/104 = 76.92 % [67.64, 84.62] | 3/75 = 4.00 % [0.83, 11.25] / 5/76 = 6.58 % [2.17, 14.69] |
| S6_leave_out_A1 | 90 | 117/137 = 85.40 % [78.36, 90.85] | 9/133 = 6.77 % [3.14, 12.46] | 52/64 = 81.25 % [69.54, 89.92] / 65/73 = 89.04 % [79.54, 95.15] | 4/62 = 6.45 % [1.79, 15.70] / 5/71 = 7.04 % [2.33, 15.67] |
| S6_leave_out_A2 | 90 | 110/137 = 80.29 % [72.64, 86.59] | 9/133 = 6.77 % [3.14, 12.46] | 53/67 = 79.10 % [67.43, 88.08] / 57/70 = 81.43 % [70.34, 89.72] | 3/65 = 4.62 % [0.96, 12.90] / 6/68 = 8.82 % [3.31, 18.22] |
| S6_leave_out_B1 | 90 | 120/136 = 88.24 % [81.60, 93.12] | 10/134 = 7.46 % [3.64, 13.30] | 64/72 = 88.89 % [79.28, 95.08] / 56/64 = 87.50 % [76.85, 94.45] | 3/72 = 4.17 % [0.87, 11.70] / 7/62 = 11.29 % [4.66, 21.89] |
| S6_leave_out_B2 | 90 | 115/136 = 84.56 % [77.37, 90.18] | 5/134 = 3.73 % [1.22, 8.49] | 59/70 = 84.29 % [73.62, 91.89] / 56/66 = 84.85 % [73.90, 92.49] | 2/68 = 2.94 % [0.36, 10.22] / 3/66 = 4.55 % [0.95, 12.71] |

### targets under each sensitivity (point / interval)

* S1_writer_intent: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S2_wrong_borderline_correct: coverage MISSED on the point, MISSED on the interval; FA MET on the point, MISSED on the interval
* S3_correct_borderline_wrong: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S4_exclude_S2_S3: coverage MISSED on the point, MISSED on the interval; FA MET on the point, MISSED on the interval
* S5_article_pre_ruling: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_A1: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_A2: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_B1: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_B2: coverage MISSED on the point, MISSED on the interval; FA MET on the point, MISSED on the interval

## every false accept

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| C:220057:c1 | 220057 | L3 | plain | Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať. | They need to have the old accordion repaired before the keys stop working completely. |
| W:220015:w2 | 220015 | L3 | plain | Stále ukladal ďalšie knihy na kopu, kým sa nezakývala. | He kept putting books on the pile until it wobbled. |
| W:220025:w1 | 220025 | L3 | drop-main | Poprosila ma, aby som nehýbal rukou, kým spí. | I was asked not to move my arm while she was sleeping. |
| W:220026:w1 | 220026 | L3 | time-frame | Kdeže, gekón práve teraz chrlí oheň, lebo papričky sú také pálivé. | No way, the gecko is going to spit fire right now, because the peppers are so hot. |
| W:220026:w2 | 220026 | L3 | missing-article | Kdeže, gekón práve teraz chrlí oheň, lebo papričky sú také pálivé. | No way, gecko is spitting fire right now, because the peppers are so hot. |
| W:220027:w2 | 220027 | L3 | missing-article | Vločky sú v miske – hneď ich zje | The flakes are in bowl – he's going to eat them right away. |
| W:220028:w2 | 220028 | L3 | plain | Pred vhadzovaním si dala omotať hokejku páskou. | Before the face-off, she had her hockey stick wrapped. |
| W:220034:w1 | 220034 | L3 | missing-article | On má sivú handričku na čistenie auta. | He has got grey cloth for cleaning the car. |
| W:220044:w2 | 220044 | L3 | plain | Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach. | By the time he reached the narrow path, he had been climbing down the ledges for an hour. |
| W:220046:w2 | 220046 | L3 | drop-main | Takže mi povedal, že v meste nejazdí veľkou rýchlosťou. | So I was told that he doesn't drive at high speed in the city. |
| W:220056:w1 | 220056 | L3 | determiner | Táto váha ukazuje oveľa viac ako pred chvíľou. | That scale shows a lot more than a moment ago. |

## every false rejection

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| C:220002:c3 | 220002 | L3 | by-passive | Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký. | Girl, I was told by him that the iceberg was huge; he must have felt so tiny there. |
| C:220003:c3 | 220003 | L3 | aspect | Model stíhačky opeká chlieb približne tri minúty. | The model of the fighter jet toasts the bread for approximately three minutes. |
| C:220005:c1 | 220005 | F4v2 | plain | Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo. | The guard can't know about the cheese - he raises the ramp too quickly. |
| C:220005:c3 | 220005 | F4v2 | plain | Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo. | The guard can't know about the cheese; he lifts the barrier too quickly. |
| C:220016:c1 | 220016 | L3 | plain | Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli! | By the time he switched on the kettle, everyone who was staring at his moustache had fallen completely silent! |
| C:220016:c2 | 220016 | L3 | plain | Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli! | By the time he turned on the kettle, everyone staring at his moustache went completely silent! |
| C:220016:c3 | 220016 | L3 | by-passive | Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli! | By the time the kettle had been switched on by him, everyone who was staring at his moustache fell completely silent! |
| C:220021:c1 | 220021 | L3 | plain | Hore je vietor. Môžeš vidieť tú vlajku? | It's windy up there. Can you see the flag? |
| C:220021:c2 | 220021 | L3:TIPrej | determiner | Hore je vietor. Môžeš vidieť tú vlajku? | There's wind up there. Can you see that flag? |
| C:220025:c1 | 220025 | F4v2 | plain | Poprosila ma, aby som nehýbal rukou, kým spí. | She asked me not to move my arm while she was sleeping. |
| C:220025:c2 | 220025 | F4v2 | plain | Poprosila ma, aby som nehýbal rukou, kým spí. | She asked me not to move my hand while she slept. |
| C:220030:c1 | 220030 | L3 | plain | Fanúšik má jednu pomaľovanú tvár a šálu. | The fan has one painted face and a scarf. |
| C:220030:c2 | 220030 | L3 | determiner | Fanúšik má jednu pomaľovanú tvár a šálu. | A fan has one painted face and a scarf. |
| C:220030:c3 | 220030 | L3:TIPrej | plain | Fanúšik má jednu pomaľovanú tvár a šálu. | The fan has got one painted face and a scarf. |
| C:220032:c2 | 220032 | L3 | by-passive | Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty. | The same two slices have been heated by the fighter-jet toaster for three minutes. |
| C:220040:c1 | 220040 | L3 | plain | Žena mu na krk zavesí jednu zlatú medailu. | The woman will hang a gold medal around his neck. |
| C:220040:c2 | 220040 | L3 | plain | Žena mu na krk zavesí jednu zlatú medailu. | The woman is going to hang one gold medal on his neck. |
| C:220045:c3 | 220045 | L3:TIPrej | plain | Jedna košeľa, jeden golier a dve červené kravaty. | One shirt, one collar, two red ties. |
| C:220048:c3 | 220048 | L3:TIPrej | plain | Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala. | I won't lie, you were the most charming clerk; she never smiled like that before. |
| C:220049:c2 | 220049 | L3:TIPrej | plain | Ryby majú plán. Idú uplávať preč od žraloka. | The fish have got a plan. They're going to swim off away from the shark. |
| C:220051:c3 | 220051 | L3 | by-passive | Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda. | Membership has been requested by about forty students at the club fair since noon. |
| C:220053:c1 | 220053 | F4v2 | plain | Pamätník zbožňoval, a samozrejme aj jeho fotoaparát. | He adored the monument, and so did his camera, of course. |
| C:220053:c2 | 220053 | F4v2 | plain | Pamätník zbožňoval, a samozrejme aj jeho fotoaparát. | He loved the memorial, and of course his camera did too. |
| C:220055:c3 | 220055 | L3 | plain | Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska. | On the last page of the contract for the new job they write their name, and the office applauds. |
| C:220057:c3 | 220057 | L3 | plain | Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať. | Before the keys stop working completely, they need to have the old accordion repaired. |
| C:220060:c1 | 220060 | L3 | plain | Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach. | You should have checked the pegs before that match - two came loose in the first ten minutes. |
| C:220060:c2 | 220060 | L3 | plain | Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach. | You ought to have checked the pegs before that match; two of them worked loose within the first ten minutes. |
| W:220005:w3 | 220005 | F4v2 | missing-article | Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo. | The guard can't know about cheese - he raises the ramp too quickly. |

## failed calls (counted, never guessed, never silently retried)

```
[]
```

an empty or unparsable HTTP 200 reply is a FAILED call: it is counted against the cap, never guessed and never silently retried; the item keeps the stack decision it gets without a model verdict (a rejection), stays in its own denominator and is listed under detail.failed_calls

