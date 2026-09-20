# SCORE_1U - the fresh 1U set (AG v4, P-FROZEN-1U), 0 model calls

Coverage = judged-correct accepted / judged-correct.  FA = judged-wrong accepted / judged-wrong.  Exact 95 % Clopper-Pearson; P1 = odd sid, P2 = even sid; never averaged.

## headline (the judge labels)

| figure | k/n, point, 95 % CI | target |
| --- | --- | --- |
| coverage pooled | 168/180 = 93.33 % [88.64, 96.51] | MET on the point, MISSED on the interval |
| FA pooled | 106/180 = 58.89 % [51.33, 66.15] | MISSED on the point, MISSED on the interval |
| coverage P1 | 81/90 = 90.00 % [81.86, 95.32] | MET on the point, MISSED on the interval |
| FA P1 | 54/90 = 60.00 % [49.13, 70.19] | MISSED on the point, MISSED on the interval |
| coverage P2 | 87/90 = 96.67 % [90.57, 99.31] | MET on the point, MET on the interval |
| FA P2 | 52/90 = 57.78 % [46.91, 68.12] | MISSED on the point, MISSED on the interval |
| Fisher P1 vs P2 (coverage) | p = 0.1324 | |
| Fisher P1 vs P2 (FA) | p = 0.8797 | |

## cells, one per line

* missing-article, judged wrong: FA 46/60 = 76.67 % [63.96, 86.62], rejected by layer {"F2B": 1, "F4v2": 4, "L3": 4, "L3:TIPrej": 5}
* missing-article, judged correct: n = 0, coverage -
* agent-drop FA (all, writer tag among judged-wrong): 31/60 = 51.67 % [38.39, 64.77] (AG fired 0)
* agent-drop FA (main, writer tag among judged-wrong): 31/60 = 51.67 % [38.39, 64.77] (AG fired 0)
* agent-drop FA (fronted, writer tag among judged-wrong): - (AG fired 0)
* agent-drop FA (misaligned, writer tag among judged-wrong): - (AG fired 0)
* agent-drop FA (other, writer tag among judged-wrong): - (AG fired 0)
* by-passive coverage: -
* SKP coverage: -
* time-frame FA: 29/60 = 48.33 % [35.23, 61.61]
* AG v4: fired 0, catches 0, measured cost (judged-correct rejected) 0
* AG shadow v2 (offline, same items): fired 0, catches 0, cost 0
* AG shadow v3 (offline, same items): fired 0, catches 0, cost 0
* AG shadow guarded_union (offline, same items): fired 0, catches 0, cost 0
* AG shadow v4_full (offline, same items): fired 0, catches 0, cost 0
* false accepts by layer: {"L1": 20, "L3": 86}
* false rejections by layer: {"F4v2": 12}
* true rejections by layer: {"F2B": 1, "F4v2": 12, "F4v3": 3, "L3": 34, "L3:TIPrej": 24}
* FA, judged type T: -
* FA, judged type W: -
* FA, judged type M: 106/180 = 58.89 % [51.33, 66.15]
* FA, judged type S: -
* level A1: coverage 45/45 = 100.00 % [92.13, 100.00], FA 29/45 = 64.44 % [48.78, 78.13]
* level A2: coverage 45/45 = 100.00 % [92.13, 100.00], FA 33/45 = 73.33 % [58.06, 85.40]
* level B1: coverage 39/45 = 86.67 % [73.21, 94.95], FA 23/45 = 51.11 % [35.77, 66.30]
* level B2: coverage 39/45 = 86.67 % [73.21, 94.95], FA 21/45 = 46.67 % [31.66, 62.13]
* model replies: {"DIFF": 34, "SAME": 89, "TIP": 25}; failed calls 0
* tokens in/out 1628/0, latency mean 1.0 ms, spend <= $0.0002 (UPPER BOUND at the published flash-lite list price ($0.10/1M in, $0.40/1M out); free-tier calls cost 0)
* judge noise on the 80 duplicate controls: null

## pre-declared sensitivities (SPLIT_1U.md S1-S6)

| sensitivity | n moved | coverage pooled | FA pooled | coverage P1 / P2 | FA P1 / P2 |
| --- | --- | --- | --- | --- | --- |
| S1_writer_intent | 0 | 168/180 = 93.33 % [88.64, 96.51] | 106/180 = 58.89 % [51.33, 66.15] | 81/90 = 90.00 % [81.86, 95.32] / 87/90 = 96.67 % [90.57, 99.31] | 54/90 = 60.00 % [49.13, 70.19] / 52/90 = 57.78 % [46.91, 68.12] |
| S2_wrong_borderline_correct | 20 | 178/200 = 89.00 % [83.82, 92.98] | 96/160 = 60.00 % [51.97, 67.65] | 88/103 = 85.44 % [77.12, 91.61] / 90/97 = 92.78 % [85.70, 97.05] | 47/77 = 61.04 % [49.25, 71.95] / 49/83 = 59.04 % [47.69, 69.72] |
| S3_correct_borderline_wrong | 20 | 148/160 = 92.50 % [87.27, 96.06] | 126/200 = 63.00 % [55.91, 69.70] | 69/78 = 88.46 % [79.22, 94.59] / 79/82 = 96.34 % [89.68, 99.24] | 66/102 = 64.71 % [54.62, 73.91] / 60/98 = 61.22 % [50.85, 70.90] |
| S4_exclude_S2_S3 | 40 | 148/160 = 92.50 % [87.27, 96.06] | 96/160 = 60.00 % [51.97, 67.65] | 69/78 = 88.46 % [79.22, 94.59] / 79/82 = 96.34 % [89.68, 99.24] | 47/77 = 61.04 % [49.25, 71.95] / 49/83 = 59.04 % [47.69, 69.72] |
| S5_article_pre_ruling | 60 | 214/240 = 89.17 % [84.53, 92.80] | 60/120 = 50.00 % [40.74, 59.26] | 104/120 = 86.67 % [79.25, 92.18] / 110/120 = 91.67 % [85.21, 95.93] | 31/60 = 51.67 % [38.39, 64.77] / 29/60 = 48.33 % [35.23, 61.61] |
| S6_leave_out_A1 | 90 | 123/135 = 91.11 % [84.99, 95.32] | 77/135 = 57.04 % [48.24, 65.52] | 54/63 = 85.71 % [74.61, 93.25] / 69/72 = 95.83 % [88.30, 99.13] | 38/63 = 60.32 % [47.20, 72.43] / 39/72 = 54.17 % [42.00, 65.98] |
| S6_leave_out_A2 | 90 | 123/135 = 91.11 % [84.99, 95.32] | 73/135 = 54.07 % [45.29, 62.68] | 57/66 = 86.36 % [75.69, 93.57] / 66/69 = 95.65 % [87.82, 99.09] | 38/66 = 57.58 % [44.79, 69.66] / 35/69 = 50.72 % [38.41, 62.98] |
| S6_leave_out_B1 | 90 | 129/135 = 95.56 % [90.58, 98.35] | 83/135 = 61.48 % [52.72, 69.72] | 69/72 = 95.83 % [88.30, 99.13] / 60/63 = 95.24 % [86.71, 99.01] | 44/72 = 61.11 % [48.89, 72.38] / 39/63 = 61.90 % [48.80, 73.85] |
| S6_leave_out_B2 | 90 | 129/135 = 95.56 % [90.58, 98.35] | 85/135 = 62.96 % [54.23, 71.11] | 63/69 = 91.30 % [82.03, 96.74] / 66/66 = 100.00 % [94.56, 100.00] | 42/69 = 60.87 % [48.37, 72.40] / 43/66 = 65.15 % [52.42, 76.47] |

### targets under each sensitivity (point / interval)

* S1_writer_intent: coverage MET on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S2_wrong_borderline_correct: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S3_correct_borderline_wrong: coverage MET on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S4_exclude_S2_S3: coverage MET on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S5_article_pre_ruling: coverage MISSED on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_A1: coverage MET on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_A2: coverage MET on the point, MISSED on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_B1: coverage MET on the point, MET on the interval; FA MISSED on the point, MISSED on the interval
* S6_leave_out_B2: coverage MET on the point, MET on the interval; FA MISSED on the point, MISSED on the interval

## every false accept

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| W:220001:w2 | 220001 | L3 | time-frame | Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa! | Yesterday He cleans the dirty floor on Monday morning. Absolute catastrophe! |
| W:220001:w3 | 220001 | L3 | drop-main | Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa! | It He cleans the dirty floor on Monday morning. Absolute catastrophe! |
| W:220003:w1 | 220003 | L1 | missing-article | Model stíhačky opeká chlieb približne tri minúty. | The model fighter jet has been toasting bread for approximately three minutes. |
| W:220003:w2 | 220003 | L3 | time-frame | Model stíhačky opeká chlieb približne tri minúty. | Yesterday The model fighter jet has been toasting bread for approximately three minutes. |
| W:220003:w3 | 220003 | L3 | drop-main | Model stíhačky opeká chlieb približne tri minúty. | It The model fighter jet has been toasting bread for approximately three minutes. |
| W:220004:w1 | 220004 | L3 | missing-article | Ten most preklenuje celý desivý kaňon, však? | That bridge spans whole terrifying canyon, doesn't it? |
| W:220006:w1 | 220006 | L3 | missing-article | Útok je rýchly a hlasný na zelenom poli. | The attack is fast and loud on green field. |
| W:220006:w3 | 220006 | L3 | drop-main | Útok je rýchly a hlasný na zelenom poli. | It The attack is fast and loud on the green field. |
| W:220007:w1 | 220007 | L3 | missing-article | Stojí bosý na teplom piesku. | He stands with bare feet on warm sand. |
| W:220008:w1 | 220008 | L3 | missing-article | Nebudem klamať, letíš vysoko, dokonca vyššie než borovice. | Not gonna lie, you fly high, even higher than pine trees. |
| W:220008:w2 | 220008 | L3 | time-frame | Nebudem klamať, letíš vysoko, dokonca vyššie než borovice. | Yesterday Not gonna lie, you fly high, even higher than the pine trees. |
| W:220008:w3 | 220008 | L3 | drop-main | Nebudem klamať, letíš vysoko, dokonca vyššie než borovice. | It Not gonna lie, you fly high, even higher than the pine trees. |
| W:220009:w2 | 220009 | L3 | time-frame | Stroj by si mal tlačiť veľmi pomaly. | Yesterday You should push the machine very slowly. |
| W:220009:w3 | 220009 | L3 | drop-main | Stroj by si mal tlačiť veľmi pomaly. | It You should push the machine very slowly. |
| W:220010:w1 | 220010 | L3 | missing-article | Na dunách je len jedna ťava. | There is only one camel on dunes. |
| W:220010:w2 | 220010 | L3 | time-frame | Na dunách je len jedna ťava. | Yesterday There is only one camel on the dunes. |
| W:220010:w3 | 220010 | L3 | drop-main | Na dunách je len jedna ťava. | It There is only one camel on the dunes. |
| W:220011:w1 | 220011 | L3 | missing-article | Úprimne, dúha možno vybledne, ale zajtra v tomto čase budeš ukazovať svoje video všetkým. | Honestly, rainbow may fade, but this time tomorrow you will be showing your video to everyone. |
| W:220011:w3 | 220011 | L3 | drop-main | Úprimne, dúha možno vybledne, ale zajtra v tomto čase budeš ukazovať svoje video všetkým. | It Honestly, the rainbow may fade, but this time tomorrow you will be showing your video to everyone. |
| W:220012:w1 | 220012 | L1 | missing-article | Správa: oni zvyčajne dávajú pohľadnice, ale včera jej oni dali 12 darčekov. | Report: they usually give cards, but yesterday they gave her 12 gifts. |
| W:220012:w3 | 220012 | L3 | drop-main | Správa: oni zvyčajne dávajú pohľadnice, ale včera jej oni dali 12 darčekov. | It Report: they usually give cards, but yesterday they gave her 12 gifts. |
| W:220013:w1 | 220013 | L3 | missing-article | Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali. | The submarine had been travelling below surface for some time before swimmers observed it. |
| W:220013:w2 | 220013 | L3 | time-frame | Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali. | Yesterday The submarine had been travelling below the surface for some time before the swimmers observed it. |
| W:220013:w3 | 220013 | L3 | drop-main | Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali. | It The submarine had been travelling below the surface for some time before the swimmers observed it. |
| W:220014:w1 | 220014 | L1 | missing-article | Dvaja kamaráti potrebujú dva hrebene | Two friends need two combs. |
| W:220014:w2 | 220014 | L3 | time-frame | Dvaja kamaráti potrebujú dva hrebene | Yesterday Two friends need two combs. |
| W:220015:w2 | 220015 | L3 | time-frame | Stále ukladal ďalšie knihy na kopu, kým sa nezakývala. | Yesterday He kept stacking books onto the pile until it swayed. |
| W:220015:w3 | 220015 | L3 | drop-main | Stále ukladal ďalšie knihy na kopu, kým sa nezakývala. | It He kept stacking books onto the pile until it swayed. |
| W:220017:w1 | 220017 | L3 | missing-article | Táto ceruzka je ostrejšia ako tá tupá. | This pencil is sharper than blunt one. |
| W:220017:w2 | 220017 | L3 | time-frame | Táto ceruzka je ostrejšia ako tá tupá. | Yesterday This pencil is sharper than the blunt one. |
| W:220017:w3 | 220017 | L3 | drop-main | Táto ceruzka je ostrejšia ako tá tupá. | It This pencil is sharper than the blunt one. |
| W:220018:w1 | 220018 | L1 | missing-article | Vraj sa rúti dolu tou riekou každé leto, kamoška. | Apparently he rushes down that river every summer, bestie. |
| W:220018:w2 | 220018 | L3 | time-frame | Vraj sa rúti dolu tou riekou každé leto, kamoška. | Yesterday Apparently he rushes down that river every summer, bestie. |
| W:220019:w1 | 220019 | L1 | missing-article | Ten hmyz je drobný, tak ona by mala skúmať ho lupou. | The insect is tiny, so she should study it with a lens. |
| W:220020:w1 | 220020 | L1 | missing-article | Muž obdivuje svoje luxusné auto už dvadsať minút. | The man has been admiring his luxury car for twenty minutes. |
| W:220020:w2 | 220020 | L3 | time-frame | Muž obdivuje svoje luxusné auto už dvadsať minút. | Yesterday The man has been admiring his luxury car for twenty minutes. |
| W:220021:w1 | 220021 | L3 | missing-article | Hore je vietor. Môžeš vidieť tú vlajku? | It is windy up here. Can you see flag? |
| W:220021:w3 | 220021 | L3 | drop-main | Hore je vietor. Môžeš vidieť tú vlajku? | It It is windy up here. Can you see the flag? |
| W:220022:w1 | 220022 | L3 | missing-article | Úprimne, dnes si hlasnejší než celý národný tím. | Honestly, you are louder than whole national team today. |
| W:220022:w3 | 220022 | L3 | drop-main | Úprimne, dnes si hlasnejší než celý národný tím. | It Honestly, you are louder than the whole national team today. |
| W:220023:w1 | 220023 | L3 | missing-article | Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky. | Listen, she said they have same dress, but they are still friends. |
| W:220023:w3 | 220023 | L3 | drop-main | Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky. | It Listen, she said they have the same dress, but they are still friends. |
| W:220024:w1 | 220024 | L3 | missing-article | Do porady o 9:00 sa zotaví z takého vyčerpania. | By 9 a.m. meeting, he will have recovered from being this exhausted. |
| W:220024:w2 | 220024 | L3 | time-frame | Do porady o 9:00 sa zotaví z takého vyčerpania. | Yesterday By the 9 a.m. meeting, he will have recovered from being this exhausted. |
| W:220027:w1 | 220027 | L3 | missing-article | Vločky sú v miske – hneď ich zje | The flakes are in bowl — he is going to eat. |
| W:220027:w3 | 220027 | L3 | drop-main | Vločky sú v miske – hneď ich zje | It The flakes are in the bowl — he is going to eat. |
| W:220028:w1 | 220028 | L3 | missing-article | Pred vhadzovaním si dala omotať hokejku páskou. | She had her stick taped before face-off. |
| W:220029:w1 | 220029 | L1 | missing-article | Kamarát tvrdil, že sa ho celý večer nikto nedotkol. | His mate insisted that nobody had touched him all night. |
| W:220030:w1 | 220030 | L1 | missing-article | Fanúšik má jednu pomaľovanú tvár a šálu. | The fan has a painted face and a scarf. |
| W:220030:w3 | 220030 | L3 | drop-main | Fanúšik má jednu pomaľovanú tvár a šálu. | It The fan has a painted face and a scarf. |
| W:220031:w1 | 220031 | L3 | missing-article | Pri ľade kráčajú ďalšie dva tučniaky | Two more penguins walk near ice. |
| W:220031:w2 | 220031 | L3 | time-frame | Pri ľade kráčajú ďalšie dva tučniaky | Yesterday Two more penguins walk near the ice. |
| W:220032:w3 | 220032 | L3 | drop-main | Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty. | It The jet toaster has been heating the same two slices for three minutes now. |
| W:220033:w1 | 220033 | L3 | missing-article | Do obeda odovzdalo 200 voličov svoje volebné lístky, výrazne pred termínom. | By noon, 200 voters had submitted their election papers, well ahead of deadline. |
| W:220033:w2 | 220033 | L3 | time-frame | Do obeda odovzdalo 200 voličov svoje volebné lístky, výrazne pred termínom. | Yesterday By noon, 200 voters had submitted their election papers, well ahead of the deadline. |
| W:220034:w1 | 220034 | L3 | missing-article | On má sivú handričku na čistenie auta. | He has got a grey cloth to clean car. |
| W:220034:w2 | 220034 | L3 | time-frame | On má sivú handričku na čistenie auta. | Yesterday He has got a grey cloth to clean the car. |
| W:220035:w1 | 220035 | L1 | missing-article | Tieto konzervy vyletujú z jeho papierovej tašky. | These cans fly out of his paper bag. |
| W:220035:w2 | 220035 | L3 | time-frame | Tieto konzervy vyletujú z jeho papierovej tašky. | Yesterday These cans fly out of his paper bag. |
| W:220037:w1 | 220037 | L1 | missing-article | Katastrofa! Ona nemá čas na dlhú návštevu! | Disaster! She has no time for a long visit! |
| W:220037:w3 | 220037 | L3 | drop-main | Katastrofa! Ona nemá čas na dlhú návštevu! | It Disaster! She has no time for a long visit! |
| W:220038:w1 | 220038 | L1 | missing-article | Už päť minút hľadá gumičku do vlasov a na zápästí má tri. | She has been looking for a hair tie for five minutes, and there are three on her wrist. |
| W:220038:w2 | 220038 | L3 | time-frame | Už päť minút hľadá gumičku do vlasov a na zápästí má tri. | Yesterday She has been looking for a hair tie for five minutes, and there are three on her wrist. |
| W:220039:w1 | 220039 | L1 | missing-article | O šiestej už bude búchať do tých lap dve hodiny v kuse. | By six she will have been hitting those pads for two hours straight. |
| W:220039:w3 | 220039 | L3 | drop-main | O šiestej už bude búchať do tých lap dve hodiny v kuse. | It By six she will have been hitting those pads for two hours straight. |
| W:220040:w1 | 220040 | L1 | missing-article | Žena mu na krk zavesí jednu zlatú medailu. | A woman hangs a gold medal around his neck. |
| W:220040:w3 | 220040 | L3 | drop-main | Žena mu na krk zavesí jednu zlatú medailu. | It A woman hangs a gold medal around his neck. |
| W:220041:w1 | 220041 | L3 | missing-article | Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt. | Bro, doors are open now, so they reveal whole valley, fr. |
| W:220041:w2 | 220041 | L3 | time-frame | Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt. | Yesterday Bro, the doors are open now, so they reveal the whole valley, fr. |
| W:220042:w1 | 220042 | L1 | missing-article | On spal. Preto nič videl. | He was asleep. That is why he saw nothing. |
| W:220042:w3 | 220042 | L3 | drop-main | On spal. Preto nič videl. | It He was asleep. That is why he saw nothing. |
| W:220043:w1 | 220043 | L1 | missing-article | Trénerka má obväz a bielu pásku. | The coach has got a bandage and white tape. |
| W:220044:w1 | 220044 | L3 | missing-article | Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach. | Before he reached narrow path, he had been climbing down rock ledges for an hour. |
| W:220045:w1 | 220045 | L1 | missing-article | Jedna košeľa, jeden golier a dve červené kravaty. | One shirt, one collar and two red ties. |
| W:220045:w2 | 220045 | L3 | time-frame | Jedna košeľa, jeden golier a dve červené kravaty. | Yesterday One shirt, one collar and two red ties. |
| W:220046:w1 | 220046 | L1 | missing-article | Takže mi povedal, že v meste nejazdí veľkou rýchlosťou. | Ok so he told me he doesn't drive with much speed in town. |
| W:220046:w2 | 220046 | L3 | time-frame | Takže mi povedal, že v meste nejazdí veľkou rýchlosťou. | Yesterday Ok so he told me he doesn't drive with much speed in town. |
| W:220046:w3 | 220046 | L3 | drop-main | Takže mi povedal, že v meste nejazdí veľkou rýchlosťou. | It Ok so he told me he doesn't drive with much speed in town. |
| W:220047:w1 | 220047 | L3 | missing-article | Fakt, tvoje dve baterky pekne osvetľujú tú tmavú rímsu. | Honestly, your two torches light up dark ledge nicely. |
| W:220048:w1 | 220048 | L3 | missing-article | Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala. | Not gonna lie, you were smoothest official; she had never smiled like that before. |
| W:220048:w2 | 220048 | L3 | time-frame | Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala. | Yesterday Not gonna lie, you were the smoothest official; she had never smiled like that before. |
| W:220048:w3 | 220048 | L3 | drop-main | Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala. | It Not gonna lie, you were the smoothest official; she had never smiled like that before. |
| W:220049:w1 | 220049 | L3 | missing-article | Ryby majú plán. Idú uplávať preč od žraloka. | The fish have a plan. They are going to swim away from shark. |
| W:220049:w2 | 220049 | L3 | time-frame | Ryby majú plán. Idú uplávať preč od žraloka. | Yesterday The fish have a plan. They are going to swim away from the shark. |
| W:220050:w2 | 220050 | L3 | time-frame | V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej. | Yesterday The moment his crutch hit the wet floor, he gripped it tight and kept going. |
| W:220050:w3 | 220050 | L3 | drop-main | V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej. | It The moment his crutch hit the wet floor, he gripped it tight and kept going. |
| W:220051:w1 | 220051 | L3 | missing-article | Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda. | Approximately forty students have been applying for membership at club fair since noon. |
| W:220051:w2 | 220051 | L3 | time-frame | Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda. | Yesterday Approximately forty students have been applying for membership at the club fair since noon. |
| W:220051:w3 | 220051 | L3 | drop-main | Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda. | It Approximately forty students have been applying for membership at the club fair since noon. |
| W:220052:w1 | 220052 | L3 | missing-article | Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe. | Status update: wardrobe has stayed tidy for 3 weeks in a row. |
| W:220052:w2 | 220052 | L3 | time-frame | Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe. | Yesterday Status update: the wardrobe has stayed tidy for 3 weeks in a row. |
| W:220052:w3 | 220052 | L3 | drop-main | Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe. | It Status update: the wardrobe has stayed tidy for 3 weeks in a row. |
| W:220054:w1 | 220054 | L1 | missing-article | Stupne víťazov boli postavené zo žineniek asi za minútu. | The podium was built out of gym mats in about a minute. |
| W:220054:w2 | 220054 | L3 | time-frame | Stupne víťazov boli postavené zo žineniek asi za minútu. | Yesterday The podium was built out of gym mats in about a minute. |
| W:220055:w3 | 220055 | L3 | drop-main | Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska. | It He puts his name on the last page of the contract for his new job, and the office claps. |
| W:220056:w1 | 220056 | L1 | missing-article | Táto váha ukazuje oveľa viac ako pred chvíľou. | This scale shows much more than a minute ago. |
| W:220056:w2 | 220056 | L3 | time-frame | Táto váha ukazuje oveľa viac ako pred chvíľou. | Yesterday This scale shows much more than a minute ago. |
| W:220056:w3 | 220056 | L3 | drop-main | Táto váha ukazuje oveľa viac ako pred chvíľou. | It This scale shows much more than a minute ago. |
| W:220057:w1 | 220057 | L3 | missing-article | Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať. | He needs to get his old accordion repaired before keys stop working completely. |
| W:220057:w2 | 220057 | L3 | time-frame | Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať. | Yesterday He needs to get his old accordion repaired before the keys stop working completely. |
| W:220057:w3 | 220057 | L3 | drop-main | Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať. | It He needs to get his old accordion repaired before the keys stop working completely. |
| W:220058:w1 | 220058 | L3 | missing-article | Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt. | You usually hate queues, but last night you waited for toilet. Respect. |
| W:220058:w3 | 220058 | L3 | drop-main | Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt. | It You usually hate queues, but last night you waited for the toilet. Respect. |
| W:220059:w1 | 220059 | L1 | missing-article | Mäkká guma môže vyčistiť celú stranu. | A soft eraser can clean a whole page. |
| W:220059:w2 | 220059 | L3 | time-frame | Mäkká guma môže vyčistiť celú stranu. | Yesterday A soft eraser can clean a whole page. |
| W:220059:w3 | 220059 | L3 | drop-main | Mäkká guma môže vyčistiť celú stranu. | It A soft eraser can clean a whole page. |

## every false rejection

| item | sid | layer | tags | Slovak | answer |
| --- | --- | --- | --- | --- | --- |
| C:220005:c1 | 220005 | F4v2 | plain | Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo. | That guard can't know about the cheese — he lifts the barrier too fast. |
| C:220005:c2 | 220005 | F4v2 | plain | Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo. | That guard can't know about the cheese — he lifts the barrier too fast. |
| C:220005:c3 | 220005 | F4v2 | plain | Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo. | That guard can't know about the cheese — he lifts the barrier too fast. |
| C:220025:c1 | 220025 | F4v2 | plain | Poprosila ma, aby som nehýbal rukou, kým spí. | She asked me to keep my arm still while it slept. |
| C:220025:c2 | 220025 | F4v2 | plain | Poprosila ma, aby som nehýbal rukou, kým spí. | She asked me to keep my arm still while it slept. |
| C:220025:c3 | 220025 | F4v2 | plain | Poprosila ma, aby som nehýbal rukou, kým spí. | She asked me to keep my arm still while it slept. |
| C:220053:c1 | 220053 | F4v2 | plain | Pamätník zbožňoval, a samozrejme aj jeho fotoaparát. | He loved the monument, and obviously so did his camera. |
| C:220053:c2 | 220053 | F4v2 | plain | Pamätník zbožňoval, a samozrejme aj jeho fotoaparát. | He loved the monument, and obviously so did his camera. |
| C:220053:c3 | 220053 | F4v2 | plain | Pamätník zbožňoval, a samozrejme aj jeho fotoaparát. | He loved the monument, and obviously so did his camera. |
| C:220060:c1 | 220060 | F4v2 | plain | Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach. | He should have checked the studs before that match - two of them came loose in the first ten minutes. |
| C:220060:c2 | 220060 | F4v2 | plain | Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach. | He should have checked the studs before that match - two of them came loose in the first ten minutes. |
| C:220060:c3 | 220060 | F4v2 | plain | Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach. | He should have checked the studs before that match - two of them came loose in the first ten minutes. |

## failed calls (counted, never guessed, never silently retried)

```
[]
```

an empty or unparsable HTTP 200 reply is a FAILED call: it is counted against the cap, never guessed and never silently retried; the item keeps the stack decision it gets without a model verdict (a rejection), stays in its own denominator and is listed under detail.failed_calls

