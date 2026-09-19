# RESCORE_1U (Phase 1U, task R) — re-score of a CLOSED set

Source: phase1t/run/results_1t.json + phase1t/set/judge/verdicts_P{1..4}.json + _key.json (raw).
Intervals: exact Clopper-Pearson 95 %% (own implementation). Fisher: two-sided exact.

## A. Article omission scored WRONG (owner ruling, brief §1.2) — re-score of a closed set

| scoring | coverage | FA |
|---|---|---|
| 1T primary (published) | 389/421 = 92.40 % [89.44, 94.74] | 16/479 = 3.34 % [1.92, 5.37] |
| A: S-art re-score (18 article answers = WRONG) | 388/403 = 96.28 % [93.94, 97.90] | 17/497 = 3.42 % [2.00, 5.42] |
| A: P1 (odd sid) | 194/200 = 97.00 % [93.58, 98.89] | 6/250 = 2.40 % [0.89, 5.15] |
| 1T primary P1 | 195/210 = 92.86 % [88.49, 95.95] | 5/240 = 2.08 % [0.68, 4.79] |
| A: P2 (even sid) | 194/203 = 95.57 % [91.75, 97.95] | 11/247 = 4.45 % [2.24, 7.83] |
| 1T primary P2 | 194/211 = 91.94 % [87.41, 95.24] | 11/239 = 4.60 % [2.32, 8.09] |

Fisher (A re-score) coverage P1 vs P2: accepted 194/200 vs 194/203, p = 0.6004
Fisher (A re-score) FA P1 vs P2: 6/250 vs 11/247, p = 0.2274

Brief expectation: coverage 388/403 = 96.28 %% [93.94, 97.90], FA 17/497 = 3.42 %% [2.00, 5.42].
ACTUAL from the raw files: coverage 388/403 = 96.28 % [93.94, 97.90], FA 17/497 = 3.42 % [2.00, 5.42].

### the 18 "article omission only" items (judge note match, raw verdicts)

| # | id | level/half | stack layer | model verdict | accepted | Slovak | answer |
|---|---|---|---|---|---|---|---|
| 1 | W:180004:w5 | A1 P2 | L3:TIPrej | TIP | no | Otec kúpi novú chladničku. | Dad will buy new fridge. |
| 2 | W:180013:w5 | A1 P1 | L3:TIPrej | TIP | no | V kuchyni je dnes zima. | It is cold in kitchen today. |
| 3 | W:180023:w5 | A1 P1 | L3 | SAME | YES | My upečieme koláč v sobotu. | We will bake cake on Saturday. |
| 4 | W:180026:w5 | A2 P2 | L3:TIPrej | TIP | no | Môj brat rezervoval hotel, lebo my sme kúpili letenky už v januári. | My brother booked hotel, because we already bought the plane tickets in January. |
| 5 | W:180031:w5 | A2 P1 | L3:TIPrej | TIP | no | My každú sobotu umývame to staré auto pred garážou. | We wash the old car in front of garage every Saturday. |
| 6 | W:180037:w5 | A2 P1 | L3:TIPrej | TIP | no | Tréner oznámil, že Jana vyhrala prvé miesto v dlhom behu. | The coach announced that Jana won first place in long race. |
| 7 | W:180042:w5 | A2 P2 | L3:TIPrej | TIP | no | My sme vrátili tú bundu, pretože predavač napísal zlú cenu na účet. | We returned that jacket, because the shop assistant wrote the wrong price on receipt. |
| 8 | W:180050:w5 | A2 P2 | L3:TIPrej | TIP | no | Martina tvrdí, že oni rezervovali stôl v tej novej reštaurácii. | Martina claims that they booked table at that new restaurant. |
| 9 | W:180051:w5 | B1 P1 | L3:TIPrej | TIP | no | Riaditeľka podpísala tú zmluvu, hoci právnik prepísal celý posledný odsek. | The director signed that contract, although the lawyer rewrote whole last paragraph. |
| 10 | W:180056:w5 | B1 P2 | L3:TIPrej | TIP | no | Organizátori predávajú lístky online, pretože dobrovoľníci pripravujú hlavnú scénu v hale. | The organisers are selling the tickets online, because the volunteers are preparing the main stage in hall. |
| 11 | W:180057:w5 | B1 P1 | L3:TIPrej | TIP | no | Vedúca tvrdí, že nový asistent už pripravil celú prezentáciu pre klienta. | The manager claims that the new assistant has already prepared whole presentation for the client. |
| 12 | W:180065:w5 | B1 P1 | L3:TIPrej | TIP | no | Keďže knižnica kúpila nové učebnice, náš lektor zmenil celý rozvrh skúšok. | Since the library bought new textbooks, our tutor changed whole exam schedule. |
| 13 | W:180067:w5 | B1 P1 | L3:TIPrej | TIP | no | Kapela zrušila ten koncert, hoci fanúšikovia už kúpili tisíc lístkov. | The band cancelled that concert, although the fans had already bought thousand tickets. |
| 14 | W:180072:w5 | B1 P2 | L3:TIPrej | TIP | no | Ak firma schváli ten rozpočet, náš tím vyvinie novú mobilnú aplikáciu. | If the company approves that budget, our team will develop new mobile app. |
| 15 | W:180076:w5 | B2 P2 | L3:TIPrej | TIP | no | Redaktorka potvrdila, že vydavateľ stiahol ten článok z webovej stránky. | The editor confirmed that the publisher removed the article from website. |
| 16 | W:180081:w5 | B2 P1 | L3:TIPrej | TIP | no | Hoci ona napísala ten scenár, režisér zmenil celý koniec filmu. | Although she wrote the screenplay, the director changed the whole ending of film. |
| 17 | W:180086:w5 | B2 P2 | L3:TIPrej | TIP | no | Galéria kúpila tie obrazy, ktoré mladá maliarka namaľovala počas pandémie. | The gallery bought the paintings that the young painter had painted during pandemic. |
| 18 | W:180089:w5 | B2 P1 | L3:TIPrej | TIP | no | Vedci potvrdili, že tá sonda zachytila neznámy signál nad Antarktídou. | The scientists confirmed that the probe had picked up unknown signal over Antarctica. |

layer breakdown: {'L3:TIPrej': 17, 'L3': 1} · accepted by the stack: 1 · rejected: 17

## B. Sensitivity table reconciled from the RAW files (brief §3)

true borderline counts (primary verdict per item, duplicates dropped):
- judged-correct borderline: **37**
- judged-wrong borderline:   **15**
- total unique borderline items: **52**
- borderline verdict ROWS incl. duplicate judgements: **55** (duplicate jids in the key: 80)
- items whose duplicate judgement disagrees on the borderline flag: 0 []
- items where results_1t.json row["borderline"] != primary verdict borderline: 0 []

| scenario | coverage | FA |
|---|---|---|
| primary | 389/421 = 92.40 % [89.44, 94.74] | 16/479 = 3.34 % [1.92, 5.37] |
| S2-wide (judged-wrong borderline -> correct) | 390/436 = 89.45 % [86.18, 92.17] | 15/464 = 3.23 % [1.82, 5.28] |
| S-art (A) | 388/403 = 96.28 % [93.94, 97.90] | 17/497 = 3.42 % [2.00, 5.42] |
| S3 (judged-correct borderline -> wrong) | 374/384 = 97.40 % [95.26, 98.74] | 31/516 = 6.01 % [4.12, 8.42] |
| S5 (borderline excluded) | 374/384 = 97.40 % [95.26, 98.74] | 15/464 = 3.23 % [1.82, 5.28] |

published 1T: S2-wide 390/436 & 15/464 · S3 and S5 coverage denominator 384
recomputed:   S2-wide 390/436 & 15/464 · S3 coverage n=384 · S5 coverage n=384
arithmetic check: 421 + 15 judged-wrong borderline = 436; 479 - 15 = 464; 421 - 37 judged-correct borderline = 384

### cause

The published 1T sensitivity NUMBERS are correct: S2-wide 390/436 and 15/464, S3 and S5 coverage
n = 384 all reproduce exactly from the raw verdict files. What is wrong is the prose borderline
COUNTS the report and analysis_1t.py put on them: the true figures are 37 judged-correct and
15 judged-wrong borderline items, 52 unique borderline items in all — not 38 / 17 / 55.

* analysis_1t.py **line 37** — `P('S2-wide (all 17 judged-wrong borderline items scored correct)...')`
  — the label says 17 while the very computation on that line (`bw`, line 36) moves 15. The number
  17 was carried over from the "21 S-intent answers judged correct" narrative, not counted.
* The 55 in "55 borderline flags" counts borderline VERDICT ROWS across verdicts_P1..P4
  (55 rows), i.e. duplicate judgements included: the key holds 80 duplicate jids. The de-duplication
  at analysis_1t.py **line 14** (`if not k.get('duplicate_of') or k['item'] not in V`) is itself
  sound — 0 items disagree between their primary and duplicate borderline flag, and 0 items
  disagree with `results_1t.json` row["borderline"] — so only the counting of the flags, done
  before the de-duplication, is off. 52 unique items carry the flag.
* 421 - 37 = 384 (S3 / S5 coverage denominator, as published) and 421 + 15 = 436, 479 - 15 = 464
  (S2-wide, as published). There is no off-by-one and no double count in the figures themselves.

## C. Minimal pairs: is the article the reason the stack rejects? (brief §1.3)

mode: rebuilt from restored answers through the frozen 1T build_req · model calls counted (http 200): 18 · failed (empty/unparsable 200): 0 · tokens in 7685 / out 18

| id | bare answer verdict (1T, stored) | stack layer | restored answer verdict (new call) | article is the cause? | added |
|---|---|---|---|---|---|
| W:180004:w5 | TIP | L3:TIPrej | SAME | YES | a |
| W:180013:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180023:w5 | SAME | L3 | SAME | n/a (bare SAME) | a |
| W:180026:w5 | TIP | L3:TIPrej | SAME | YES | a |
| W:180031:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180037:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180042:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180050:w5 | TIP | L3:TIPrej | SAME | YES | a |
| W:180051:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180056:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180057:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180065:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180067:w5 | TIP | L3:TIPrej | SAME | YES | a |
| W:180072:w5 | TIP | L3:TIPrej | SAME | YES | a |
| W:180076:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180081:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180086:w5 | TIP | L3:TIPrej | SAME | YES | the |
| W:180089:w5 | TIP | L3:TIPrej | SAME | YES | an |

**the article is the cause in 17 of 18.**
restored answer still TIP/DIFF: none

### the 21 S-intent answers judged CORRECT — the 3 the stack ACCEPTED

n = 21, accepted 3
| id | layer | model | Slovak | answer | judge note |
|---|---|---|---|---|---|
| W:180023:w5 | L3 | SAME | My upečieme koláč v sobotu. | We will bake cake on Saturday. | article omission only, M1 |
| W:180054:w5 | L3 | SAME | Mesto vymení všetky lampy na námestí, keďže technici našli starú kabeláž. | The city will replace all the lamps on the square, since the technicians found the old cabling. | 'on the square' acceptable variant |
| W:180094:w5 | L3 | SAME | Kým doktorandi spracúvajú tie vzorky, ona pripravuje záverečnú správu pre komisiu. | While the doctoral students are processing the samples, she is preparing the final report to the committee. | 'report to the committee' idiomatic |
