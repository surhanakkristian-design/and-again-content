# Phase 1e — three-layer hybrid (L1 checker / L2 grammar veto / L3 model)

Models: Flash-Lite `gemini-3.1-flash-lite`, Flash `gemini-3.7-flash`. Thinking config: {"gemini-3.1-flash-lite": "{\"thinkingBudget\": 0}", "gemini-3.7-flash": "{\"thinkingBudget\": 0}"}

Sanity: L1 100/235 = 42.6 % and 0 real false acceptances reproduced


## 1. Per model x prompt variant

| config | sent to L3 | end-to-end coverage /235 (baseline 42.6 %) | end-to-end FA /105 | FA by type | L2 caught (no model call) |
|---|---|---|---|---|---|
| gemini-3.1-flash-lite x P-A | 57 | n/a | 24 | {"S": 3, "T": 1, "M": 11} | 39 |
| gemini-3.1-flash-lite x P-B | 57 | n/a | 22 | {"M": 11, "S": 2} | 39 |

L1 false acceptances carried into every row: 9 of 105 (all judged tip-accept / valid reading in Phase 1c, 0 real).

## 2. Layer shares

| set | L1 | L2 | L3 |
|---|---|---|---|
| all 340 | 109 (32.1 %) | 87 (25.6 %) | 144 (42.4 %) |
| 235 correct | 100 (42.6 %) | 48 (20.4 %) | 87 (37.0 %) |

## 3. L3 latency (ms)

| config | warm median | warm p95 | cold first call(s) |
|---|---|---|---|
| gemini-3.1-flash-lite x P-A | 804 | 1087 | [] |
| gemini-3.1-flash-lite x P-B | 887 | 1245 | [] |

## 4. Tokens and cost

| config | in | out | thoughts | cached | $/L3 call | $/active user/month |
|---|---|---|---|---|---|---|
| gemini-3.1-flash-lite x P-A | 124.4 | 1.0 | 0.0 | 0.0 | $0.000033 | $0.0072 |
| gemini-3.1-flash-lite x P-B | 150.0 | 1.0 | 0.0 | 0.0 | $0.000039 | $0.0087 |

Assumption: 20 exercises/day x 30 days, and the L3 share measured on the correct-answer distribution (87 of 235 = 37.0 % of answers reach the model when the learner is right). Flash-Lite $0.25 in / $1.50 out / $0.025 cached per 1M. 3.7 Flash ai.google.dev/gemini-api/docs/pricing, fetched 2026-09-18, paid tier through 2026-12-31

## 5. Disagreements


**gemini-3.1-flash-lite x P-A** — 15 disagreements

| id | set/type | Slovak | reference | learner answer | model |
|---|---|---|---|---|---|
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

**gemini-3.1-flash-lite x P-B** — 13 disagreements

| id | set/type | Slovak | reference | learner answer | model |
|---|---|---|---|---|---|
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

## 6. Budget

- calls used: 436 of the 500 cap (436 HTTP attempts, cap 650)
- 429 "free tier rate-limited" responses: 0
- free tier throughout: yes, no 429-forced switch
- Stage 2 (3.7 Flash) SKIPPED and the 4th variant CUT: 2N=288 exceeds the remaining budget.

## 7. Selfcheck

```
selfcheck(a) .env.local git-ignored: PASS
selfcheck(b) key value absent from phase1e/: PASS
```
