# Wave 1 Part D - Hungarian, fresh production set: analysis

Frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG); set opened once; truth = 4 opus judge sessions.

| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |
|---|---|---|---|---|
| pooled | 479/496 = 96.57 % [94.57, 97.99] | MET / MET | 21/404 = 5.20 % [3.25, 7.84] | missed / missed |
| A1 | 119/124 = 95.97 % [90.84, 98.68] | MET / MET | 3/101 = 2.97 % [0.62, 8.44] | MET / missed |
| A2 | 121/124 = 97.58 % [93.09, 99.50] | MET / MET | 5/101 = 4.95 % [1.63, 11.18] | MET / missed |
| B1 | 124/125 = 99.20 % [95.62, 99.98] | MET / MET | 6/100 = 6.00 % [2.23, 12.60] | missed / missed |
| B2 | 115/123 = 93.50 % [87.59, 97.15] | MET / missed | 7/102 = 6.86 % [2.80, 13.63] | missed / missed |

Both targets met on the point (pooled): False

Diagnostic, L3 only (before the content check): | L3 only | 488/496 = 98.39 % [96.85, 99.30] | MET / MET | 51/404 = 12.62 % [9.55, 16.26] | missed / missed |

Gemini: 1439 counted calls (HTTP 200; {'l3': 900, 'cc': 539}), 0 failed-but-counted, spend $0.143506; language ledger {'D_CC': 539, 'D_L3': 900}.

Judge noise (80 hidden duplicates, different sessions): 1/80 disagree = 1.25 % [0.03, 6.77].

## False rejections (17) by cause

by layer {'L3': 5, 'CC:MISSING': 9, 'L3:TIPrej': 3}; by writer {'correct/None': 17}; by level {'B1': 1, 'B2': 8, 'A2': 3, 'A1': 5}

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:1421:c3 | B1 | L3 |  | correct/ | Ő nem hagyta abba a kés húzogatását a kenyéren, amíg egyetlen száraz folt sem maradt. | He kept dragging the knife over the bread until no dry spot remained. | Same meaning, different structure. |
| A:8119:c3 | B2 | CC:MISSING | elő fogják adni | correct/ | Naplementéig hatszor elő fogják adni a műsort. | The show will have been performed six times by sundown. | Passive fine; no agent named. |
| A:10743:c5 | B2 | L3:TIPrej |  | correct/ | Rajzolt egy spirált, és egy hullám azonnal elmosta. | He had drawn a spiral, and a wave washed it off right away. | Past frame kept; tense free. |
| A:20586:c4 | A2 | CC:MISSING | arcába | correct/ | Tegnap egy hal ugrott és az arcába fröccsent a víz. | Yesterday a fish jumped, and the water splashed her face. | Meaning matches. |
| A:20918:c2 | A1 | CC:MISSING | húzzák | correct/ | Egy piros jelet húzzák át a fehér krétavonalon. | A red mark is drawn across the white chalk line. | Passive; source names no specific agent |
| A:20918:c3 | A1 | CC:MISSING | húzzák | correct/ | Egy piros jelet húzzák át a fehér krétavonalon. | They are drawing a red mark through the white chalk line. | Same meaning. |
| A:20918:c4 | A1 | L3 |  | correct/ | Egy piros jelet húzzák át a fehér krétavonalon. | They draw a red sign over the white chalk line. | Generic 'they' active acceptable; meaning kept. |
| A:24409:c5 | A2 | L3:TIPrej |  | correct/ | Ez a kávé édesebb, mint az első. | This coffee is sweeter than the first cup. | Same meaning. |
| A:31804:c1 | A1 | CC:MISSING | tönkreteszi | correct/ | Ő megérinti az üveget. Ez az álom tönkreteszi! | He touches the glass. This dream is ruining him! | Same meaning. |
| A:31804:c5 | A1 | L3 |  | correct/ | Ő megérinti az üveget. Ez az álom tönkreteszi! | He's touching the glass. This dream is wrecking him! | Accurate meaning. |
| A:32851:c3 | A2 | CC:MISSING | neki | correct/ | Nagyon kényelmes, nyilván: neki van ágya, de ő a hűtő mellett fekszik. | Very comfortable, obviously: it has a bed, but it lies beside the fridge. | Genderless source; 'it' acceptable for referent. |
| A:37311:c5 | B2 | L3:TIPrej |  | correct/ | Ő lenéz a határra a két ország között, és átlép rajta. | He looks down at the frontier between the two countries and crosses it with one step. | Same meaning |
| A:39567:c2 | B2 | L3 |  | correct/ | Haver, ha velük edzettem volna, én most abban a formációban zuhannék, nem kamu. | Mate, if I'd trained with them, I'd be skydiving in that formation right now, seriously. | Mixed conditional meaning preserved. |
| A:42927:c1 | B2 | CC:MISSING | ő | correct/ | Amikor felmászott a tetőre, ő már három órája fotózott. | When he climbed onto the roof, she had already been taking photos for three hours. | Accurate meaning; pronouns free. |
| A:42927:c2 | B2 | CC:MISSING | ő | correct/ | Amikor felmászott a tetőre, ő már három órája fotózott. | By the time she climbed up on the roof, he had already been taking pictures for three hours. | Meaning matches; genders free. |
| A:42927:c4 | B2 | L3 |  | correct/ | Amikor felmászott a tetőre, ő már három órája fotózott. | When she got up onto the roof, he had already been shooting photos for three hours. | Same meaning. |
| A:43666:c2 | B2 | CC:MISSING | pletyka | correct/ | Csajszi, a pletyka szerint ő évekig edzett, mielőtt átütötte a betont. | Girl, word is he had been training for years before he broke through the concrete. | Same meaning. |

## False acceptances (21) by cause

by layer {'L3+CC:NONE': 21}; by writer type {'None': 2, 'S': 3, 'M': 11, 'W': 2, 'T': 3}; by level {'B2': 7, 'B1': 6, 'A2': 5, 'A1': 3}

| aid | lvl | layer | cc | writer type | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:4674:c2 | B2 | L3+CC:NONE | none | None | A kordon mögötti sok karlengetés ellenére ő egyszer sem nézett fel. | In spite of the lots of arm waving behind the cordon, she never once looked up. | Ungrammatical 'the lots of'. |
| A:10764:s | B1 | L3+CC:NONE | none | S | Ha egy csapat elsőként ér célba, a tömeg megőrül minden alkalommal. | If a team finish first, the crowd go crazy every time. | Agreement errors: 'a team finish', 'crowd go'. |
| A:10868:m | B2 | L3+CC:NONE | none | M | Ma estére már hat órája fogja mutogatni mindenkinek azt az oldalt. | By tonight he will have been showing that page for six hours. | Dropped 'to everyone'. |
| A:12144:m | A2 | L3+CC:NONE | none | M | Épp most csukja a doboz fedelét. | He is closing the lid right now. | Drops 'of the box'. |
| A:12320:m | A2 | L3+CC:NONE | none | M | A szomszéd agyagedényét nem kellene eltörnöd. | You shouldn't break the neighbour's pot. | Dropped 'clay'. |
| A:19625:w | A1 | L3+CC:NONE | none | W | A családnak van egy nagy fazék étele a kinti ebédhez. | The family has a big pot of food for the outdoor dinner. | 'dinner' instead of 'lunch'. |
| A:25450:t | A1 | L3+CC:NONE | none | T | A bőröndök az ülések fölött | The suitcases were above the seats. | Adds past time frame |
| A:32607:m | A2 | L3+CC:NONE | none | M | A kamara szabálya: a szónoknak vitában fel kell állnia. | The rule: the speaker must stand up in a debate. | Drops 'of the chamber'. |
| A:33941:m | A1 | L3+CC:NONE | none | M | Ágyjelentés: 1 mopsz elfoglalhatja az egész közepet. | Report: 1 pug can take up the whole middle. | Dropped noun 'bed'. |
| A:34679:m | A2 | L3+CC:NONE | none | M | Most ő vár a piros lámpánál, szóval ott van. | He's waiting at the light now, so he's there. | Dropped adjective 'red'. |
| A:35262:c5 | A2 | L3+CC:NONE | none | None | Haver, a teknős olyan lassan megy, elég gyenge, de nyer. | Dude, the tortoise goes so slow, it's pretty weak, but it still wins. | Added 'still' not in source. |
| A:37147:s | B2 | L3+CC:NONE | none | S | A fenevad sokáig állt a sziklán, mielőtt leugrott. | Beast had been standing on the rock for a long time before it jumped down. | Missing article before beast. |
| A:37579:m | B2 | L3+CC:NONE | none | M | Képzeld, ő állítólag abban a fekete beterítőben megcsináltatta a haját. | Imagine, she apparently had her hair done in that cape. | Drops adjective 'black' |
| A:38420:t | B1 | L3+CC:NONE | none | T | A férfi hajnalban kint van a tavon, és a jávorszarvas is. | The man was out on the lake at dawn, and so was the moose. | Past instead of present. |
| A:40386:m | B1 | L3+CC:NONE | none | M | Ő térdelt a füvön, üvöltve, amikor a csapattársa nekirohant! | He was kneeling, screaming, when his teammate ran into him! | Dropped place phrase 'on the grass'. |
| A:41455:m | B2 | L3+CC:NONE | none | M | Ő tovább ment felfelé az ösvényen, pedig a köd egyre sűrűsödött. | He kept going up, even though the fog was getting thicker. | Dropped 'the path'. |
| A:41904:m | B2 | L3+CC:NONE | none | M | Tesó, ők hetekig programozták azt az appot, mire végre megjelent a zöld pipa, komolyan. | Bro, they had been programming that app for weeks before the tick finally appeared, seriously. | Dropped adjective 'green'. |
| A:43213:w | B1 | L3+CC:NONE | none | W | Tesó, holnap ilyenkor az a tyúk megint fog elosonni a farkasok mellett, komolyan. | Bro, this time tomorrow that hen will be sneaking past the foxes again, seriously. | Foxes instead of wolves. |
| A:44085:t | B2 | L3+CC:NONE | none | T | Ő azt kívánja, bárcsak a nagy nap előtt megtanulta volna, hogyan kell csokornyakkendőt kötni. | She wished she had learned how to tie a bow tie before the big day. | 'wished' shifts present wishing to past. |
| A:44216:m | B1 | L3+CC:NONE | none | M | Ha még közelebb jön, az a hullám teljesen el fogja tüntetni a kis nyomukat! | If it comes any closer, that wave will completely wipe out their footprints! | Dropped adjective 'little'. |
| A:44784:s | B1 | L3+CC:NONE | none | S | Te nyugodt maradtál azok alatt a széles szárnyak alatt, és őszintén a sólyom is. | You stayed calm under those wide wings, and honestly, so was the falcon. | 'so was' wrong auxiliary for 'stayed'. |

## Judge duplicate disagreements

- A:4074:c5 (B1, correct/None) s1 correct vs s6 wrong: "There was poppy everywhere on that hillside, wasn't there?"
