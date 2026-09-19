# SCORE_1U - the fresh 1U set (AG v4, P-FROZEN-1U), 0 model calls

Coverage = judged-correct accepted / judged-correct.  FA = judged-wrong accepted / judged-wrong.  Exact 95 % Clopper-Pearson; P1 = odd sid, P2 = even sid; never averaged.

## headline (the judge labels)

| figure | k/n, point, 95 % CI | target |
| --- | --- | --- |
| coverage pooled | 382/402 = 95.02 % [92.42, 96.93] | MET on the point, MET on the interval |
| FA pooled | 16/498 = 3.21 % [1.85, 5.17] | MET on the point, MISSED on the interval |
| coverage P1 | 189/201 = 94.03 % [89.80, 96.88] | MET on the point, MISSED on the interval |
| FA P1 | 7/249 = 2.81 % [1.14, 5.71] | MET on the point, MISSED on the interval |
| coverage P2 | 193/201 = 96.02 % [92.31, 98.27] | MET on the point, MET on the interval |
| FA P2 | 9/249 = 3.61 % [1.67, 6.75] | MET on the point, MISSED on the interval |
| Fisher P1 vs P2 (coverage) | p = 0.4923 | |
| Fisher P1 vs P2 (FA) | p = 0.8004 | |

## cells, one per line

* missing-article, judged wrong: FA 2/97 = 2.06 % [0.25, 7.25], rejected by layer {"F2B": 1, "L3": 78, "L3:TIPrej": 16}
* missing-article, judged correct: n = 1, coverage 0/1 = 0.00 % [0.00, 97.50]
* agent-drop FA (all, writer tag among judged-wrong): 9/159 = 5.66 % [2.62, 10.47] (AG fired 137)
* agent-drop FA (main, writer tag among judged-wrong): 3/48 = 6.25 % [1.31, 17.20] (AG fired 45)
* agent-drop FA (fronted, writer tag among judged-wrong): 3/63 = 4.76 % [0.99, 13.29] (AG fired 53)
* agent-drop FA (misaligned, writer tag among judged-wrong): 3/48 = 6.25 % [1.31, 17.20] (AG fired 39)
* agent-drop FA (other, writer tag among judged-wrong): - (AG fired 0)
* by-passive coverage: 79/80 = 98.75 % [93.23, 99.97]
* SKP coverage: 59/63 = 93.65 % [84.53, 98.24]
* time-frame FA: 4/120 = 3.33 % [0.92, 8.31]
* AG v4: fired 139, catches 138, measured cost (judged-correct rejected) 1
* AG shadow v2 (offline, same items): fired 73, catches 73, cost 0
* AG shadow v3 (offline, same items): fired 117, catches 117, cost 0
* AG shadow guarded_union (offline, same items): fired 117, catches 117, cost 0
* AG shadow v4_full (offline, same items): fired 139, catches 138, cost 1
* false accepts by layer: {"L3": 16}
* false rejections by layer: {"AG": 1, "L3": 7, "L3:TIPrej": 12}
* true rejections by layer: {"AG": 136, "F2B": 1, "F5": 4, "L3": 324, "L3:TIPrej": 17}
* FA, judged type T: 4/120 = 3.33 % [0.92, 8.31]
* FA, judged type W: 1/120 = 0.83 % [0.02, 4.56]
* FA, judged type M: 9/159 = 5.66 % [2.62, 10.47]
* FA, judged type S: 2/99 = 2.02 % [0.25, 7.11]
* level A1: coverage 94/100 = 94.00 % [87.40, 97.77], FA 2/125 = 1.60 % [0.19, 5.66]
* level A2: coverage 93/100 = 93.00 % [86.11, 97.14], FA 2/125 = 1.60 % [0.19, 5.66]
* level B1: coverage 97/100 = 97.00 % [91.48, 99.38], FA 7/125 = 5.60 % [2.28, 11.20]
* level B2: coverage 98/102 = 96.08 % [90.26, 98.92], FA 5/123 = 4.07 % [1.33, 9.23]
* model replies: {"DIFF": 331, "SAME": 241, "TIP": 30}; failed calls 0
* tokens in/out 323895/0, latency mean 688.1 ms, spend <= $0.0324 (UPPER BOUND at the published flash-lite list price ($0.10/1M in, $0.40/1M out); free-tier calls cost 0)
* judge noise on the 80 duplicate controls: {"join_labels_1u.json": null, "assemble_1u.json": null}

## pre-declared sensitivities (SPLIT_1U.md S1-S6)

| sensitivity | n moved | coverage pooled | FA pooled | coverage P1 / P2 | FA P1 / P2 |
| --- | --- | --- | --- | --- | --- |
| S1_writer_intent | 2 | 382/400 = 95.50 % [92.98, 97.31] | 16/500 = 3.20 % [1.84, 5.14] | 189/200 = 94.50 % [90.37, 97.22] / 193/200 = 96.50 % [92.92, 98.58] | 7/250 = 2.80 % [1.13, 5.68] / 9/250 = 3.60 % [1.66, 6.72] |
| S2_wrong_borderline_correct | 20 | 387/422 = 91.71 % [88.65, 94.16] | 11/478 = 2.30 % [1.15, 4.08] | 191/214 = 89.25 % [84.31, 93.06] / 196/208 = 94.23 % [90.14, 96.98] | 5/236 = 2.12 % [0.69, 4.87] / 6/242 = 2.48 % [0.92, 5.32] |
| S3_correct_borderline_wrong | 20 | 367/382 = 96.07 % [93.61, 97.79] | 31/518 = 5.98 % [4.10, 8.39] | 181/189 = 95.77 % [91.83, 98.16] / 186/193 = 96.37 % [92.67, 98.53] | 15/261 = 5.75 % [3.25, 9.30] / 16/257 = 6.23 % [3.60, 9.91] |
| S4_exclude_S2_S3 | 40 | 367/382 = 96.07 % [93.61, 97.79] | 11/478 = 2.30 % [1.15, 4.08] | 181/189 = 95.77 % [91.83, 98.16] / 186/193 = 96.37 % [92.67, 98.53] | 5/236 = 2.12 % [0.69, 4.87] / 6/242 = 2.48 % [0.92, 5.32] |
| S5_article_pre_ruling | 97 | 384/499 = 76.95 % [73.00, 80.58] | 14/401 = 3.49 % [1.92, 5.79] | 190/250 = 76.00 % [70.21, 81.16] / 194/249 = 77.91 % [72.24, 82.91] | 6/200 = 3.00 % [1.11, 6.42] / 8/201 = 3.98 % [1.73, 7.69] |
| S6_leave_out_A1 | 225 | 288/302 = 95.36 % [92.34, 97.44] | 14/373 = 3.75 % [2.07, 6.22] | 142/149 = 95.30 % [90.56, 98.09] / 146/153 = 95.42 % [90.80, 98.14] | 6/184 = 3.26 % [1.21, 6.96] / 8/189 = 4.23 % [1.84, 8.17] |
| S6_leave_out_A2 | 225 | 289/302 = 95.70 % [92.75, 97.69] | 14/373 = 3.75 % [2.07, 6.22] | 144/153 = 94.12 % [89.13, 97.28] / 145/149 = 97.32 % [93.27, 99.26] | 7/189 = 3.70 % [1.50, 7.48] / 7/184 = 3.80 % [1.54, 7.68] |
| S6_leave_out_B1 | 225 | 285/302 = 94.37 % [91.14, 96.69] | 9/373 = 2.41 % [1.11, 4.53] | 140/149 = 93.96 % [88.84, 97.20] / 145/153 = 94.77 % [89.96, 97.72] | 3/184 = 1.63 % [0.34, 4.69] / 6/189 = 3.17 % [1.17, 6.78] |
| S6_leave_out_B2 | 225 | 284/300 = 94.67 % [91.48, 96.92] | 11/375 = 2.93 % [1.47, 5.19] | 141/152 = 92.76 % [87.42, 96.33] / 143/148 = 96.62 % [92.29, 98.89] | 5/190 = 2.63 % [0.86, 6.03] / 6/185 = 3.24 % [1.20, 6.93] |

### targets under each sensitivity (point / interval)

* S1_writer_intent: coverage MET on the point, MET on the interval; FA MET on the point, MISSED on the interval
* S2_wrong_borderline_correct: coverage MET on the point, MISSED on the interval; FA MET on the point, MET on the interval
* S3_correct_borderline_wrong: coverage MET on the point, MET on the interval; FA MISSED on the point, MISSED on the interval
* S4_exclude_S2_S3: coverage MET on the point, MET on the interval; FA MET on the point, MET on the interval
* S5_article_pre_ruling: coverage MISSED on the point, MISSED on the interval; FA MET on the point, MISSED on the interval
* S6_leave_out_A1: coverage MET on the point, MET on the interval; FA MET on the point, MISSED on the interval
* S6_leave_out_A2: coverage MET on the point, MET on the interval; FA MET on the point, MISSED on the interval
* S6_leave_out_B1: coverage MET on the point, MET on the interval; FA MET on the point, MET on the interval
* S6_leave_out_B2: coverage MET on the point, MET on the interval; FA MET on the point, MISSED on the interval

## every false accept

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| W:190008:w4 | 190008 | L3 | missing-article | Zatiaľ čo Marek vozí deti autobusom, mama upratuje dom. | While Marek is taking the children by bus, Mum is cleaning house. |
| W:190017:w5 | 190017 | L3 | wrong-word | Chlapec odomkol malú skrinku. | The boy unlocked the small box. |
| W:190036:w2 | 190036 | L3 | drop-misaligned | Sused tvrdí, že mechanik opraví auto už zajtra. | The neighbour says the car is getting repaired tomorrow. |
| W:190038:w2 | 190038 | L3 | drop-misaligned | Na stene visí obraz, ktorý moja teta namaľovala pri rieke. | A picture painted by the river is hanging on the wall. |
| W:190052:w2 | 190052 | L3 | drop-fronted | Kým sprievodca vysvetľoval históriu hradu, turisti fotili nádvorie. | During the explanation of the castle's history, the tourists were photographing the courtyard. |
| W:190054:w2 | 190054 | L3 | drop-fronted | Pretože učiteľka zrušila písomku, žiaci si mohli cez víkend konečne oddýchnuť. | Because of the cancellation of the test, the pupils could finally rest at the weekend. |
| W:190057:w1 | 190057 | L3 | drop-fronted | Len čo technik poslal e-mailom podrobnú správu, klient okamžite odpovedal. | As soon as the detailed report was sent by email, the client replied immediately. |
| W:190059:w3 | 190059 | L3 | time-frame | Riaditeľka na porade oznámila, že údržbár opraví strechu telocvične cez prázdniny. | At the meeting the headmistress announces that the caretaker will repair the gym roof during the holidays. |
| W:190061:w4 | 190061 | L3 | missing-article | Deti sa celé popoludnie hrali pri rieke a moja mama zatiaľ pripravovala grilovanú večeru. | The children played by the river all afternoon and my mum was preparing barbecue dinner in the meantime. |
| W:190062:w3 | 190062 | L3 | time-frame | Noviny píšu, že mesto postaví novú cyklotrasu pozdĺž rieky už na budúci rok. | The newspapers wrote that the city would build a new cycle path along the river as early as next year. |
| W:190073:w2 | 190073 | L3 | time-frame | Treba čo najskôr opraviť tú starú strechu na chate. | The old roof on the cottage will have to be repaired as soon as possible. |
| W:190084:w3 | 190084 | L3 | time-frame | Hovorkyňa oznámila, že mesto obnoví historickú radnicu ešte pred koncom budúceho roka. | The spokeswoman announces that the city will restore the historic town hall before the end of next year. |
| W:190086:w2 | 190086 | L3 | drop-misaligned | Učitelia sa dozvedeli, že ministerstvo zrušilo dotáciu na školské výlety už v marci. | The teachers found out about the cancellation of the subsidy for school trips back in March. |
| W:190090:w1 | 190090 | L3 | drop-main | Archeológovia objavili rozsiahlu keltskú osadu pri jazere počas letného výskumu. | A large Celtic settlement was discovered by the lake during the summer research. |
| W:190091:w1 | 190091 | L3 | drop-main | My pravidelne zverejňujeme výsledky klinických testov na webovej stránke univerzity. | The results of the clinical tests are regularly published on the university website. |
| W:190091:w2 | 190091 | L3 | drop-main | My pravidelne zverejňujeme výsledky klinických testov na webovej stránke univerzity. | On the university website the results of the clinical tests get published regularly. |

## every false rejection

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| C:190007:c3 | 190007 | L3 | by-passive | Odkedy sused predáva zeleninu, my nechodíme do obchodu. | Since vegetables have been sold by the neighbour, we do not go to the shop. |
| C:190009:c2 | 190009 | L3 | determiner | Učiteľka povedala, že školník opraví dvere. | The teacher said the caretaker would fix that door. |
| C:190022:c2 | 190022 | L3:TIPrej | skp-passive | Raňajky sa podávajú v kuchyni. | Breakfast is served in our kitchen. |
| C:190023:c2 | 190023 | L3:TIPrej | skp-passive | Dnes je v triede veľmi chladno. | It's very cold in our classroom today. |
| C:190025:c2 | 190025 | L3:TIPrej | skp-passive | Obchod sa zatvára o šiestej. | This shop is closed at six o'clock. |
| C:190025:c3 | 190025 | L3:TIPrej | skp-passive | Obchod sa zatvára o šiestej. | The shop gets closed at six o'clock. |
| C:190028:c2 | 190028 | L3 | determiner | Keďže šéf číta všetky e-maily, kolegovia píšu veľmi opatrne. | Since the boss reads all the emails, my colleagues write very carefully. |
| C:190034:c2 | 190034 | L3:TIPrej | determiner | Učiteľka oznámi, že žiaci prepíšu test budúci týždeň. | The teacher will announce that the pupils will rewrite that test next week. |
| C:190039:c2 | 190039 | L3 | determiner | Tréner verí, že Marek vyhrá preteky v nedeľu. | The coach believes that Marek will win that race on Sunday. |
| C:190039:c4 | 190039 | L3:TIPrej | paraphrase | Tréner verí, že Marek vyhrá preteky v nedeľu. | The coach is sure Marek is going to win the race on Sunday. |
| C:190042:c2 | 190042 | L3:TIPrej | determiner | My pozveme celú triedu na výlet do Tatier. | We will invite the whole class on the trip to the Tatras. |
| C:190043:c2 | 190043 | L3:TIPrej | determiner | Veterinár vyšetril našu chorú mačku v sobotu ráno. | The vet examined the sick cat on Saturday morning. |
| C:190044:c2 | 190044 | L3:TIPrej | determiner | Náš sused poleje záhradu dnes večer. | Our neighbour will water his garden this evening. |
| C:190055:c2 | 190055 | L3:TIPrej | determiner | Hoci tréner vymení brankára, náš tím podľa mňa zápas nevyhrá. | Although the coach will replace our goalkeeper, I think our team will not win the match. |
| C:190059:c2 | 190059 | L3 | determiner | Riaditeľka na porade oznámila, že údržbár opraví strechu telocvične cez prázdniny. | At the meeting the headmistress announced that our caretaker would repair the gym roof during the holidays. |
| C:190067:c2 | 190067 | L3:TIPrej | determiner | Náš vedúci pošle všetky vzorky do laboratória vo Viedni vlakom zajtra ráno. | Our manager will send all of those samples to the laboratory in Vienna by train tomorrow morning. |
| C:190084:c2 | 190084 | L3 | determiner | Hovorkyňa oznámila, že mesto obnoví historickú radnicu ešte pred koncom budúceho roka. | The spokeswoman announced that the city would restore that historic town hall before the end of next year. |
| C:190094:c2 | 190094 | L3 | determiner | Kuriér prepravuje krvné vzorky do mestského laboratória vlakom každé ráno. | The courier transports the blood samples to that city laboratory by train every morning. |
| W:190081:w2 | 190081 | AG | drop-fronted | Len čo vedci dokončia klinickú štúdiu, farmaceutická firma požiada o registráciu lieku. | The pharmaceutical company will apply for registration of the drug once the clinical trial has been completed. |
| W:190088:w4 | 190088 | L3:TIPrej | missing-article | Zasadnutie sa skončilo neskoro, a preto tajomníčka poslala zápisnicu všetkým členom komisie emailom. | The meeting ended late, so the secretary sent minutes to all the members of the committee by email. |

## failed calls (counted, never guessed, never silently retried)

```
[]
```

an empty or unparsable HTTP 200 reply is a FAILED call: it is counted against the cap, never guessed and never silently retried; the item keeps the stack decision it gets without a model verdict (a rejection), stays in its own denominator and is listed under detail.failed_calls

