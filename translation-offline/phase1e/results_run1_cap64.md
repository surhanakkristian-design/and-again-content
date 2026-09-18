# Phase 1e — three-layer hybrid (L1 checker / L2 grammar veto / L3 model)

Models: Flash-Lite `gemini-3.1-flash-lite`, Flash `gemini-3.7-flash`. Thinking config: {"gemini-3.1-flash-lite": "{\"thinkingBudget\": 0}", "gemini-3.7-flash": "{\"thinkingBudget\": 0}"}

Sanity: L1 100/235 = 42.6 % and 0 real false acceptances reproduced


## 1. Per model x prompt variant

| config | sent to L3 | end-to-end coverage /235 (baseline 42.6 %) | end-to-end FA /105 | FA by type | L2 caught (no model call) |
|---|---|---|---|---|---|
| gemini-3.1-flash-lite x P-A | 144 | 76.6 % | 24 | {"S": 3, "T": 1, "M": 11} | 39 |
| gemini-3.1-flash-lite x P-B | 144 | 75.3 % | 22 | {"M": 11, "S": 2} | 39 |
| gemini-3.7-flash x P-B | 144 | 66.0 % | 11 | {"T": 1, "M": 1} | 39 |

L1 false acceptances carried into every row: 9 of 105 (all judged tip-accept / valid reading in Phase 1c, 0 real).

## 2. Layer shares

| set | L1 | L2 | L3 |
|---|---|---|---|
| all 340 | 109 (32.1 %) | 87 (25.6 %) | 144 (42.4 %) |
| 235 correct | 100 (42.6 %) | 48 (20.4 %) | 87 (37.0 %) |

## 3. L3 latency (ms)

| config | warm median | warm p95 | cold first call(s) |
|---|---|---|---|
| gemini-3.1-flash-lite x P-A | 815 | 1104 | [908] |
| gemini-3.1-flash-lite x P-B | 875 | 1239 | [] |
| gemini-3.7-flash x P-B | 2362 | 9178 | [2076] |

## 4. Tokens and cost

| config | in | out | thoughts | cached | $/L3 call | $/active user/month |
|---|---|---|---|---|---|---|
| gemini-3.1-flash-lite x P-A | 123.0 | 1.0 | 0.0 | 0.0 | $0.000032 | $0.0072 |
| gemini-3.1-flash-lite x P-B | 148.5 | 1.0 | 0.0 | 0.0 | $0.000039 | $0.0086 |
| gemini-3.7-flash x P-B | 148.5 | 1.1 | 46.3 | 0.0 | $0.000289 | $0.0643 |

Assumption: 20 exercises/day x 30 days, and the L3 share measured on the correct-answer distribution (87 of 235 = 37.0 % of answers reach the model when the learner is right). Flash-Lite $0.25 in / $1.50 out / $0.025 cached per 1M. 3.7 Flash ai.google.dev/gemini-api/docs/pricing, fetched 2026-09-18, paid tier through 2026-12-31

## 5. Disagreements


**gemini-3.1-flash-lite x P-A** — 22 disagreements

| id | set/type | Slovak | reference | learner answer | model |
|---|---|---|---|---|---|
| 29691 | correct/- | Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa! | He drops his guidebook on the church steps! Total disaster! | He's going to drop his guide on the church steps! A total catastrophe! | DIFF |
| 16261 | correct/- | Má plán. Chystá sa odprevadiť ju domov. | He has a plan. He is going to walk her home. | She's got a plan. She is going to accompany her home. | DIFF |
| 16403 | correct/- | Rozlúč sa a o hodinu sa vráti naspäť. | Say bye now and she will come back in an hour. | Say goodbye - he will return in an hour. | DIFF |
| 27628 | correct/- | Deti sa zobudia o siedmej ráno. | The children awake at seven in the morning. | The children will wake up at seven o'clock in the morning. | DIFF |
| 27628 | correct/- | Deti sa zobudia o siedmej ráno. | The children awake at seven in the morning. | The children will wake up at seven in the morning. | DIFF |
| 26084 | correct/- | Dokáže ju nájsť skôr, než príde domov. | He can find her before she gets home. | He can find her before he gets home. | DIFF |
| 26084 | correct/- | Dokáže ju nájsť skôr, než príde domov. | He can find her before she gets home. | He can find it before he comes home. | DIFF |
| 16403 | wrong/S | Rozlúč sa a o hodinu sa vráti naspäť. | Say bye now and she will come back in an hour. | Say bye now and they will come back in an hour. | TIP |
| 16403 | wrong/T | Rozlúč sa a o hodinu sa vráti naspäť. | Say bye now and she will come back in an hour. | Say bye now and she will came back in an hour. | TIP |
| 4612 | wrong/M | Keby skrutkovač držal on, tá polica by už dávno bola na zemi. | If he held the screwdriver, that shelf would be on the floor by now. | If he held the screwdriver, that shelf would be on the floor. | TIP |
| 9907 | wrong/M | Keby si bola vzala béžovú bundu, tento look by nikdy nevznikol. | If she had taken the beige jacket, this look would never have happened. | If she had taken the beige jacket, this would never have happened. | TIP |
| 14266 | wrong/M | Čo tancujú? — Salsu. | What do they dance? — Salsa. | What do they dance? | TIP |
| 11348 | wrong/M | Pozri! Asistent práve drží odrazovú dosku hore. | Look! The assistant is holding the reflector up now. | Look! The assistant is holding the reflector. | TIP |
| 11980 | wrong/M | Počkaj chvíľu a voda zovrie! | Wait a minute and the water will boil! | Wait and the water will boil! | TIP |
| 1452 | wrong/M | Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta. | If he touches that cactus, he will spend the evening pulling spines out of his finger. | If he touches that cactus, he will spend the evening pulling spines out. | TIP |
| 9244 | wrong/M | Kým sa vlny valili, čierna mačka nepohla ani fúzom. | While the waves were rolling in, the black cat did not move a whisker. | While the waves were rolling in, the black cat did not move. | TIP |
| 4571 | wrong/M | Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve. | If you leave one screw loose, the whole chair wobbles. | If you leave one screw loose, the chair wobbles. | TIP |
| 4571 | wrong/S | Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve. | If you leave one screw loose, the whole chair wobbles. | If I leave one screw loose, the whole chair wobbles. | TIP |
| 7238 | wrong/M | Ak stúpaš presne tam, kam stúpa Mira, nohy ti zostanú úplne suché. | If you step exactly where Mira steps, your feet stay completely dry. | If you step exactly where Mira steps, your feet stay dry. | TIP |
| 3494 | wrong/M | Keby bola guľôčka padla na čiernej, išla by domov s prázdnymi vreckami. | If the ball had landed in black, she would have gone home with empty pockets. | If the ball had landed in black, she would have gone home. | TIP |
| 3494 | wrong/S | Keby bola guľôčka padla na čiernej, išla by domov s prázdnymi vreckami. | If the ball had landed in black, she would have gone home with empty pockets. | If the ball had landed in black, they would have gone home with empty pockets. | SAME |
| 8209 | wrong/M | Do piatku si zarezervuje piaty termín v štúdiu. | By Friday she will have booked a fifth appointment at the studio. | By Friday she will have booked a fifth appointment. | TIP |

**gemini-3.1-flash-lite x P-B** — 23 disagreements

| id | set/type | Slovak | reference | learner answer | model |
|---|---|---|---|---|---|
| 29691 | correct/- | Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa! | He drops his guidebook on the church steps! Total disaster! | He will drop his guidebook on the church steps! A complete catastrophe! | DIFF |
| 29691 | correct/- | Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa! | He drops his guidebook on the church steps! Total disaster! | He's going to drop his guide on the church steps! A total catastrophe! | DIFF |
| 16261 | correct/- | Má plán. Chystá sa odprevadiť ju domov. | He has a plan. He is going to walk her home. | She's got a plan. She is going to accompany her home. | DIFF |
| 16403 | correct/- | Rozlúč sa a o hodinu sa vráti naspäť. | Say bye now and she will come back in an hour. | Say goodbye - he will return in an hour. | DIFF |
| 27628 | correct/- | Deti sa zobudia o siedmej ráno. | The children awake at seven in the morning. | The children will wake up at seven o'clock in the morning. | DIFF |
| 27628 | correct/- | Deti sa zobudia o siedmej ráno. | The children awake at seven in the morning. | The children will wake up at seven in the morning. | DIFF |
| 26084 | correct/- | Dokáže ju nájsť skôr, než príde domov. | He can find her before she gets home. | He can find her before he gets home. | DIFF |
| 26084 | correct/- | Dokáže ju nájsť skôr, než príde domov. | He can find her before she gets home. | He can find it before he comes home. | DIFF |
| 21124 | correct/- | Zvyčajne ostáva pod strechou, ale dnes tancuje v daždi. | She usually stays dry, but today she is dancing in the rain. | He usually stays under the roof, but today he is dancing in the rain. | DIFF |
| 8293 | correct/- | Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný. | She never shares food, so this one must be special. | He never shares food, so this particular croissant must be exceptional. | DIFF |
| 4612 | wrong/M | Keby skrutkovač držal on, tá polica by už dávno bola na zemi. | If he held the screwdriver, that shelf would be on the floor by now. | If he held the screwdriver, that shelf would be on the floor. | TIP |
| 9907 | wrong/M | Keby si bola vzala béžovú bundu, tento look by nikdy nevznikol. | If she had taken the beige jacket, this look would never have happened. | If she had taken the beige jacket, this would never have happened. | TIP |
| 11348 | wrong/M | Pozri! Asistent práve drží odrazovú dosku hore. | Look! The assistant is holding the reflector up now. | Look! The assistant is holding the reflector. | TIP |
| 11980 | wrong/M | Počkaj chvíľu a voda zovrie! | Wait a minute and the water will boil! | Wait and the water will boil! | TIP |
| 1452 | wrong/M | Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta. | If he touches that cactus, he will spend the evening pulling spines out of his finger. | If he touches that cactus, he will spend the evening pulling spines out. | TIP |
| 9244 | wrong/M | Kým sa vlny valili, čierna mačka nepohla ani fúzom. | While the waves were rolling in, the black cat did not move a whisker. | While the waves were rolling in, the black cat did not move. | TIP |
| 4571 | wrong/M | Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve. | If you leave one screw loose, the whole chair wobbles. | If you leave one screw loose, the chair wobbles. | TIP |
| 4571 | wrong/S | Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve. | If you leave one screw loose, the whole chair wobbles. | If I leave one screw loose, the whole chair wobbles. | SAME |
| 7238 | wrong/M | Ak stúpaš presne tam, kam stúpa Mira, nohy ti zostanú úplne suché. | If you step exactly where Mira steps, your feet stay completely dry. | If you step exactly where Mira steps, your feet stay dry. | TIP |
| 8824 | wrong/M | Kým sa reťaz kývala, dotlačil vrece na miesto. | While the chain was swinging, he pushed the bag into place. | While the chain was swinging, he pushed the bag. | TIP |
| 3494 | wrong/M | Keby bola guľôčka padla na čiernej, išla by domov s prázdnymi vreckami. | If the ball had landed in black, she would have gone home with empty pockets. | If the ball had landed in black, she would have gone home. | TIP |
| 3494 | wrong/S | Keby bola guľôčka padla na čiernej, išla by domov s prázdnymi vreckami. | If the ball had landed in black, she would have gone home with empty pockets. | If the ball had landed in black, they would have gone home with empty pockets. | SAME |
| 8209 | wrong/M | Do piatku si zarezervuje piaty termín v štúdiu. | By Friday she will have booked a fifth appointment at the studio. | By Friday she will have booked a fifth appointment. | TIP |

**gemini-3.7-flash x P-B** — 34 disagreements

| id | set/type | Slovak | reference | learner answer | model |
|---|---|---|---|---|---|
| 24733 | wrong/T | Pohárik je horúci, tak ho musíš držať opatrne. | The glass is hot, so you must hold it carefully. | The glass is hot, so you must held it carefully. | TIP |
| 4571 | wrong/M | Keď necháš jednu skrutku uvoľnenú, celá stolička sa kýve. | If you leave one screw loose, the whole chair wobbles. | If you leave one screw loose, the chair wobbles. | TIP |
| 8812 | correct/- | Tréner by si prial, aby jeho lapy boli trochu hrubšie. | Her trainer wishes his pads were a bit thicker. | The coach wishes that his mitts were a bit thicker. | PARSE_FAIL |
| 1018 | correct/- | Smoothie prelial do vysokého pohára, takže mixér je teraz úplne prázdny. | He has poured the smoothie into the tall glass, so the blender is completely empty now. | He has poured the smoothie into a tall glass, so the blender is now completely empty. | PARSE_FAIL |
| 29691 | correct/- | Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa! | He drops his guidebook on the church steps! Total disaster! | He's going to drop his guide on the church steps! A total catastrophe! | PARSE_FAIL |
| 23026 | correct/- | Túto sukňu nosí do parku každú nedeľu. | She wears the skirt in the park every Sunday. | She wears this skirt to the park each Sunday. | PARSE_FAIL |
| 11348 | correct/- | Pozri! Asistent práve drží odrazovú dosku hore. | Look! The assistant is holding the reflector up now. | Look! The assistant is holding the reflector board up. | PARSE_FAIL |
| 26084 | correct/- | Dokáže ju nájsť skôr, než príde domov. | He can find her before she gets home. | He can find her before he gets home. | DIFF |
| 7716 | correct/- | Podarilo sa jej vydržať úplne nehybne, kým sa vážka usadila. | She managed to stay completely still until the dragonfly settled. | She managed to hold completely still until the dragonfly had settled. | PARSE_FAIL |
| 29691 | correct/- | Pustí svojho sprievodcu na kostolné schody! Úplná katastrofa! | He drops his guidebook on the church steps! Total disaster! | He will drop his guidebook on the church steps! A complete catastrophe! | PARSE_FAIL |
| 10167 | correct/- | Ústa má také suché, že smäd musí byť skutočný. | His mouth is that dry, so the thirst must be real. | Her mouth is so dry the thirst must be real. | PARSE_FAIL |
| 2955 | correct/- | Strážnik ľutuje - kiežby bol otočil kameru k obzoru o minútu skôr. | The guard wishes he had turned the camera towards the horizon a minute earlier. | The guard regrets it - if only he had turned the camera toward the horizon a minute earlier. | PARSE_FAIL |
| 8293 | correct/- | Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný. | She never shares food, so this one must be special. | He never shares food, so this particular croissant must be exceptional. | PARSE_FAIL |
| 8756 | correct/- | Povedal, že puk letí rýchlejšie na studenom ľade. | He said the puck travelled faster on cold ice. | He said that the puck flies faster on cold ice. | PARSE_FAIL |
| 13034 | correct/- | Práve teraz dievča sfukuje sviečky. | Right now the girl is blowing out the candles. | Right now, the girl is blowing out candles. | PARSE_FAIL |
| 27628 | correct/- | Deti sa zobudia o siedmej ráno. | The children awake at seven in the morning. | The children will wake up at seven o'clock in the morning. | PARSE_FAIL |
| 7238 | correct/- | Ak stúpaš presne tam, kam stúpa Mira, nohy ti zostanú úplne suché. | If you step exactly where Mira steps, your feet stay completely dry. | Whenever you step exactly where Mira steps, your feet stay completely dry. | PARSE_FAIL |
| 2874 | correct/- | Mal ísť k lekárovi už pred pár dňami, ale čakal, kým sa sotva udržal na nohách. | He should have seen a doctor days ago, but he waited until he could hardly stand. | He should have gone to the doctor a few days ago, but he waited until he could barely stand. | PARSE_FAIL |
| 21467 | correct/- | Voda je studená, mal by si si obuť čižmy. | The water is cold, so you should wear boots. | The water is cold, you should put your boots on. | PARSE_FAIL |
| 16403 | correct/- | Rozlúč sa a o hodinu sa vráti naspäť. | Say bye now and she will come back in an hour. | Say goodbye - he will return in an hour. | DIFF |
| 8799 | correct/- | Stále hádzala tú istú kombináciu, kým nešla hladko. | She kept throwing the same combination until it felt smooth. | She kept throwing the same combo until it went smoothly. | PARSE_FAIL |
| 9966 | correct/- | Práve teraz si na slnečnej streche podávajú ruky. | Right now they are shaking hands on the sunny rooftop. | At the moment they are shaking hands on a sunny roof. | PARSE_FAIL |
| 9913 | correct/- | Vlani si dala čižmy zafarbiť na fialovo. | She had her boots dyed purple last summer. | Last year she got her boots dyed purple. | PARSE_FAIL |
| 9038 | correct/- | Práve teraz čmára poznámku, kým obrazovka notebooku svieti. | Right now he is scribbling a note while the laptop screen glows. | Right now he is scribbling a note as the laptop screen shines. | PARSE_FAIL |
| 26084 | correct/- | Dokáže ju nájsť skôr, než príde domov. | He can find her before she gets home. | He can find it before he comes home. | DIFF |
| 11216 | correct/- | Ak sa ti odpoveď nepáči, nemal by si sa kariet pýtať. | If you hate the answer, you should not ask the cards. | If you don't like the answer, you shouldn't ask the cards. | PARSE_FAIL |
| 16261 | correct/- | Má plán. Chystá sa odprevadiť ju domov. | He has a plan. He is going to walk her home. | She's got a plan. She is going to accompany her home. | PARSE_FAIL |
| 9913 | correct/- | Vlani si dala čižmy zafarbiť na fialovo. | She had her boots dyed purple last summer. | Last year, she had her boots dyed violet. | PARSE_FAIL |
| 13395 | correct/- | Zvyčajne kreslí srdcia, ale dnes nakreslila kruh. | She usually draws hearts, but today she drew a circle. | She normally draws hearts, but she drew a circle today. | PARSE_FAIL |
| 10959 | correct/- | Keby bola kúpila hrubší papier, kytica by bola teraz dokonalá. | If she had bought thicker paper, the bouquet would be perfect now. | If she had bought heavier paper, the bouquet would be perfect now. | PARSE_FAIL |
| 9966 | correct/- | Práve teraz si na slnečnej streche podávajú ruky. | Right now they are shaking hands on the sunny rooftop. | They are shaking hands on the sunlit roof at this very moment. | PARSE_FAIL |
| 16261 | correct/- | Má plán. Chystá sa odprevadiť ju domov. | He has a plan. He is going to walk her home. | He's got a plan. He is going to walk her home. | PARSE_FAIL |
| 7998 | correct/- | Veranda, na ktorej teraz trávi každé ráno, je otočená na východ slnka. | The veranda, where she now spends every morning, faces the sunrise. | The veranda where she now spends every single morning faces the sunrise. | PARSE_FAIL |
| 21124 | correct/- | Zvyčajne ostáva pod strechou, ale dnes tancuje v daždi. | She usually stays dry, but today she is dancing in the rain. | She usually stays indoors under the roof, but today she is dancing in the rain. | DIFF |

## 6. Budget

- calls used: 436 of the 500 cap (436 HTTP attempts, cap 650)
- 429 "free tier rate-limited" responses: 0
- free tier throughout: yes, no 429-forced switch
- 4th variant (3.7 Flash x the other prompt) is CUT — not enough budget under the 500 cap.

## 7. Selfcheck

```
selfcheck(a) .env.local git-ignored: PASS
selfcheck(b) key value absent from phase1e/: PASS
```
