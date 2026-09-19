# Phase 1S Task A - lever 1 out, rule AG in (re-score of the closed 1Q set)

0 model calls, 0 network calls. The stack decisions are the frozen 1Q ones with lever 1's rewrite-accept removed (the stored MAIN-side verdict is exactly the lever-1-OFF verdict of the unrewritten answer) and the deterministic rule AG inserted before L3.

## Fields of `rows_1s.json` (one object per item, 1,080 rows)

| field | meaning |
| --- | --- |
| iid, sid, half, tags, wrong_type | as in `phase1q/rows_1q.json` (tags are writer LABELS of the set) |
| judged, wrong_type | the ORIGINAL 1Q label |
| label_1r, label_1r_type | the 1R-corrected PRIMARY label (116 M2 movers -> wrong/M) - use this one |
| label_s2, label_s2_type | sensitivity S2 (the 7 borderline movers stay CORRECT) |
| accept_1q, layer_1q | the frozen 1Q decision (lever 1 ON) |
| lever1_fired, lever1_agent | lever 1's detector on this item |
| lever1_off_accept, lever1_off_layer | the stored MAIN-side verdict = lever 1 OFF |
| ag_fired, ag_reason, ag_agent, ag_agent_kind, ag_agent_source | rule AG (primary variant) |
| ag_answer_is_agentless_passive, ag_agent_elsewhere_in_answer, ag_noun_fired | AG diagnostics / AG-noun variant |
| accept_1s, layer_1s | the NEW stack decision (lever 1 off + AG) |
| slovak, answer, reference, l3_tip | source text, the answer, main reference, L3 tip for L3:TIPrej rows |

## Headline

| metric | BEFORE (1R) | AFTER | BEFORE S2 | AFTER S2 |
| --- | --- | --- | --- | --- |
| pooled coverage | 425/483 = 87.99 % [84.75, 90.75] | 359/483 = 74.33 % [70.19, 78.17] | 426/490 = 86.94 % [83.63, 89.79] | 360/490 = 73.47 % [69.32, 77.33] |
| pooled FA | 19/597 = 3.18 % [1.93, 4.93] | 9/597 = 1.51 % [0.69, 2.84] | 18/590 = 3.05 % [1.82, 4.78] | 8/590 = 1.36 % [0.59, 2.65] |
| P1 coverage | 215/241 = 89.21 % [84.59, 92.83] | 183/241 = 75.93 % [70.03, 81.19] | 216/247 = 87.45 % [82.66, 91.31] | 184/247 = 74.49 % [68.58, 79.81] |
| P1 FA | 9/299 = 3.01 % [1.39, 5.64] | 4/299 = 1.34 % [0.37, 3.39] | 8/293 = 2.73 % [1.19, 5.31] | 3/293 = 1.02 % [0.21, 2.96] |
| P2 coverage | 210/242 = 86.78 % [81.85, 90.78] | 176/242 = 72.73 % [66.65, 78.24] | 210/243 = 86.42 % [81.46, 90.46] | 176/243 = 72.43 % [66.35, 77.95] |
| P2 FA | 10/298 = 3.36 % [1.62, 6.08] | 5/298 = 1.68 % [0.55, 3.87] | 10/297 = 3.37 % [1.63, 6.10] | 5/297 = 1.68 % [0.55, 3.88] |

Fisher p: BEFORE cov 0.4843 / FA 0.8208; AFTER cov 0.4662 / FA 0.7518; S2 AFTER cov 0.6106 / FA 0.7247

## Cells

| cell | BEFORE | AFTER | BEFORE S2 | AFTER S2 |
| --- | --- | --- | --- | --- |
| agentless cov | 75/98 = 76.53 % [66.89, 84.50] | 12/98 = 12.24 % [6.49, 20.41] | 75/98 = 76.53 % [66.89, 84.50] | 12/98 = 12.24 % [6.49, 20.41] |
| agentless FA | 11/172 = 6.40 % [3.24, 11.15] | 1/172 = 0.58 % [0.01, 3.20] | 11/172 = 6.40 % [3.24, 11.15] | 1/172 = 0.58 % [0.01, 3.20] |
| by-passive cov | 42/42 = 100.00 % [91.59, 100.00] | 42/42 = 100.00 % [91.59, 100.00] | 42/42 = 100.00 % [91.59, 100.00] | 42/42 = 100.00 % [91.59, 100.00] |
| plain cov | 167/173 = 96.53 % [92.60, 98.72] | 166/173 = 95.95 % [91.84, 98.36] | 168/180 = 93.33 % [88.64, 96.51] | 167/180 = 92.78 % [87.97, 96.10] |
| timeframe FA | 3/224 = 1.34 % [0.28, 3.86] | 2/224 = 0.89 % [0.11, 3.19] | 3/224 = 1.34 % [0.28, 3.86] | 2/224 = 0.89 % [0.11, 3.19] |

## FA by wrong type

| type | BEFORE | AFTER | BEFORE S2 | AFTER S2 |
| --- | --- | --- | --- | --- |
| T | 3/224 = 1.34 % [0.28, 3.86] | 2/224 = 0.89 % [0.11, 3.19] | 3/224 = 1.34 % [0.28, 3.86] | 2/224 = 0.89 % [0.11, 3.19] |
| W | 1/127 = 0.79 % [0.02, 4.31] | 1/127 = 0.79 % [0.02, 4.31] | 1/127 = 0.79 % [0.02, 4.31] | 1/127 = 0.79 % [0.02, 4.31] |
| M | 11/126 = 8.73 % [4.44, 15.08] | 2/126 = 1.59 % [0.19, 5.62] | 10/119 = 8.40 % [4.10, 14.91] | 1/119 = 0.84 % [0.02, 4.59] |
| S | 4/120 = 3.33 % [0.92, 8.31] | 4/120 = 3.33 % [0.92, 8.31] | 4/120 = 3.33 % [0.92, 8.31] | 4/120 = 3.33 % [0.92, 8.31] |

## Layers

- false rejections BEFORE: L3 30, L3:TIPrej 22, F5 4, F2B 2
- false rejections AFTER: AG 81, L3:TIPrej 22, L3 15, F5 4, F2B 2

- false accepts BEFORE: L3 19
- false accepts AFTER: L3 9

- true rejections AFTER: L3 285, AG 142, L3:TIPrej 92, F5 63, F3 5, F2B 1

## A5 - the cost (AG fires on judged-correct agentless items)

| iid | Slovak | answer | agent | kind | was accepted |
| --- | --- | --- | --- | --- | --- |
| C:170001:c2 | Marek každý večer zamyká bránu do záhrady. | The garden gate is locked every evening. | Marek | noun | True |
| C:170002:c2 | Ona včera upiekla jablkový koláč pre susedov. | An apple pie was baked for the neighbours yesterday. | ona | pronoun | True |
| C:170003:c2 | Môj brat zajtra umyje naše auto pred domom. | Our car will be washed in front of the house tomorrow. | môj brat | noun | True |
| C:170004:c2 | Učiteľka teraz opravuje naše písomky v triede. | Our tests are being corrected in the classroom now. | učiteľka | noun | True |
| C:170006:c2 | Otec minulý týždeň natrel plot na zeleno. | The fence was painted green last week. | otec | noun | True |
| C:170007:c2 | Ona každé ráno varí čaj pre celú rodinu. | Tea is made for the whole family every morning. | ona | pronoun | True |
| C:170008:c2 | My zajtra uvaríme polievku pre celú rodinu. | Soup will be cooked for the whole family tomorrow. | my | pronoun | True |
| C:170009:c2 | Deti včera nakreslili veľký obrázok na chodník. | A big picture was drawn on the pavement yesterday. | deti | noun | True |
| C:170011:c2 | Sused opravil môj bicykel v garáži. | My bike was repaired in the garage. | sused | noun | True |
| C:170012:c2 | Ja teraz čítam novú knihu o zvieratách. | A new book about animals is being read now. | ja | pronoun | True |
| C:170013:c2 | Mama zajtra kúpi chlieb v novej pekárni. | Bread will be bought at the new bakery tomorrow. | mama | noun | False |
| C:170016:c2 | Ona napísala dlhý list svojej babke. | A long letter was written to her grandmother. | ona | pronoun | True |
| C:170017:c2 | Chlapec nesie ťažkú tašku po schodoch. | A heavy bag is being carried up the stairs. | chlapec | noun | True |
| C:170018:c2 | Ja zajtra pošlem ten balík svojej sestre. | The parcel will be sent to my sister tomorrow. | ja | pronoun | True |
| C:170021:c2 | Môj dedko pestuje paradajky v skleníku. | Tomatoes are grown in the greenhouse. | môj dedko | noun | True |
| C:170022:c2 | Ty si včera stratil kľúče od bytu. | The keys to the flat were lost yesterday. | ty | pronoun | False |
| C:170023:c2 | Ona zajtra upratá celú kuchyňu. | The whole kitchen will be cleaned tomorrow. | ona | pronoun | False |
| C:170024:c2 | Pes zjedol moju večeru zo stola. | My dinner was eaten off the table. | pes | noun | False |
| C:170026:c2 | Sestra fotí kvety v záhrade. | The flowers in the garden are being photographed. | sestra | noun | True |
| C:170027:c2 | Oni postavili nový most cez rieku. | A new bridge was built over the river. | oni | pronoun | True |
| C:170028:c2 | Ja zajtra prinesiem koláč do školy. | A cake will be brought to school tomorrow. | ja | pronoun | False |
| C:170029:c2 | Babka uvarila veľký hrniec polievky. | A big pot of soup was cooked. | babka | noun | True |
| C:170031:c2 | Môj kolega včera preložil celý dokument do angličtiny. | The whole document was translated into English yesterday. | môj kolega | noun | False |
| C:170032:c2 | Ona každý mesiac platí nájom za ten malý byt. | The rent for that small flat is paid every month. | ona | pronoun | True |
| C:170033:c2 | Robotníci budúci týždeň opravia cestu pred školou. | The road in front of the school will be repaired next week. | robotníci | noun | True |
| C:170034:c2 | Ja som minulý rok predal svoj starý bicykel cez internet. | My old bike was sold online last year. | ja | pronoun | True |
| C:170036:c2 | Riaditeľ práve podpisuje tie nové zmluvy v kancelárii. | The new contracts are being signed in the office right now. | riaditeľ | noun | True |
| C:170037:c2 | Ona zajtra odovzdá svoju seminárnu prácu profesorovi. | Her term paper will be handed in to the professor tomorrow. | ona | pronoun | True |
| C:170038:c2 | Zlodej minulú noc ukradol susedovi bicykel z dvora. | The neighbour's bike was stolen from the yard last night. | zlodej | noun | True |
| C:170039:c2 | Kuchár pripravuje obed pre tridsať hostí. | Lunch is being prepared for thirty guests. | kuchár | noun | True |
| C:170041:c2 | Moja teta upratala celý dom pred návštevou. | The whole house was cleaned before the visit. | moja teta | noun | True |
| C:170042:c2 | Technik zajtra vymení pokazenú práčku v kúpeľni. | The broken washing machine in the bathroom will be replaced tomorrow. | technik | noun | True |
| C:170043:c2 | Ona číta deťom rozprávku každý večer pred spaním. | A fairy tale is read to the children every evening before bed. | ona | pronoun | True |
| C:170044:c2 | Študenti minulý semester preštudovali tri hrubé knihy. | Three thick books were studied last semester. | študenti | noun | True |
| C:170046:c2 | Firma budúci mesiac otvorí novú pobočku v Košiciach. | A new branch will be opened in Košice next month. | firma | noun | True |
| C:170047:c2 | On si každé ráno čistí topánky pred odchodom do práce. | His shoes are cleaned every morning before he leaves for work. | on | pronoun | False |
| C:170048:c2 | Záhradník pokosil trávnik pred naším domom. | The lawn in front of our house was mowed. | záhradník | noun | True |
| C:170049:c2 | Ona zajtra pozve celú rodinu na obed. | The whole family will be invited to lunch tomorrow. | ona | pronoun | True |
| C:170051:c2 | Môj otec opravuje starý nábytok vo svojej dielni. | Old furniture is repaired in his workshop. | môj otec | noun | True |
| C:170052:c2 | Poštár doručil ten balík až v piatok popoludní. | The parcel was delivered only on Friday afternoon. | poštár | noun | True |
| C:170053:c2 | Ja zajtra zaplatím účet za elektrinu cez internet. | The electricity bill will be paid online tomorrow. | ja | pronoun | True |
| C:170054:c2 | Ona si kúpila nový kabát v zľave. | A new coat was bought on sale. | ona | pronoun | True |
| C:170056:c2 | Susedia budúci rok postavia malý bazén za domom. | A small pool will be built behind the house next year. | susedia | noun | True |
| C:170058:c2 | Naša škola organizuje výlet do hlavného mesta každú jar. | A trip to the capital is organised every spring. | naša škola | noun | True |
| C:170059:c2 | Ty si zabudol svoj mobil na stole v kuchyni. | Your mobile phone was left on the table in the kitchen. | ty | pronoun | True |
| C:170064:c3 | Keď zazvonil telefón, on práve krájal cibuľu na večeru. | When the phone rang, onions were just being chopped for dinner. | on | pronoun | False |
| C:170066:c3 | Ona práve dokončila prihlášku na ten jazykový kurz. | The application for that language course has just been finished. | ona | pronoun | True |
| C:170067:c3 | Budúci mesiac oni otvoria novú pobočku na hlavnej ulici. | Next month a new branch will be opened on the main street. | oni | pronoun | True |
| C:170068:c3 | Susedov syn rozbil naše kuchynské okno futbalovou loptou. | Our kitchen window was broken with a football. | susedov syn | noun | False |
| C:170069:c3 | Naša učiteľka opravuje písomky vždy až v nedeľu večer. | The tests are always marked on Sunday evening. | naša učiteľka | noun | True |
| C:170072:c3 | Susedia minulý rok vymenili staré okná za nové. | Last year the old windows were replaced with new ones. | susedia | noun | False |
| C:170073:c3 | Ona teraz píše referát o slovenských hradoch. | A paper about Slovak castles is being written right now. | ona | pronoun | True |
| C:170076:c3 | Oni každý večer zamykajú bránu do dvora o desiatej. | The gate to the courtyard is locked at ten every evening. | oni | pronoun | False |
| C:170078:c3 | Kedysi moja stará mama piekla koláče každú sobotu. | Cakes used to be baked every Saturday. | moja stará mama | noun | True |
| C:170079:c3 | Väčšina študentov odovzdáva tie eseje na poslednú chvíľu. | Those essays are handed in at the last minute. | väčšina študentov | noun | False |
| C:170082:c3 | Technik vymenil batériu v mojom notebooku za dvadsať minút. | The battery in my laptop was replaced in twenty minutes. | technik | noun | True |
| C:170084:c3 | Policajt zastavil naše auto hneď za mostom a skontroloval doklady. | Our car was stopped just past the bridge and the documents were checked. | policajt | noun | True |
| C:170087:c3 | Riaditeľka nepodpísala tie zmluvy, lebo chýbali dve prílohy. | Those contracts were not signed because two attachments were missing. | riaditeľka | noun | True |
| C:170091:c3 | Keby si Lucia bola prečítala pokyny, nebola by pokazila celú tabuľku. | If the instructions had been read, the whole spreadsheet would not have been ruined. | Lucia | noun | False |
| C:170092:c3 | Zjavne niekto prehodil tie štítky, pretože všetky škatule sú pomiešané. | Those labels have obviously been swapped, because all the boxes are mixed up. | niekto | noun | True |
| C:170096:c3 | Architektka prepracovala celý projekt po pripomienkach z úradu. | The whole project was reworked after the comments from the authority. | architektka | noun | True |
| C:170097:c3 | Hoci firma sľubuje rýchle dodanie, zákazníci čakajú na objednávky aj tri týždne. | Although fast delivery is promised, customers wait up to three weeks for their orders. | firma | noun | True |
| C:170098:c3 | Do konca roka tím dokončí druhú etapu rekonštrukcie mosta. | By the end of the year the second stage of the bridge reconstruction will have been finished. | tím | noun | True |
| C:170101:c3 | Pokiaľ komisia schváli rozpočet, mesto obnoví detské ihriská už na jar. | If the budget is approved, the playgrounds will be renovated as early as spring. | mesto | noun | True |
| C:170102:c3 | Prekladateľka, ktorú nám odporučili kolegovia, odovzdala hotový text o deň skôr. | The finished text was delivered a day early. | prekladateľka | noun | False |
| C:170103:c3 | Redakcia zverejňuje opravy chýb vždy na konci mesiaca. | Corrections of mistakes are always published at the end of the month. | redakcia | noun | True |
| C:170106:c3 | Vedenie spoločnosti prepustí desať zamestnancov ešte pred koncom roka. | Ten employees will be laid off before the end of the year. | vedenie spoločnosti | noun | True |
| C:170107:c3 | Až keď technici vymenili server, stránka konečne prestala padať. | Only when the server was replaced did the website finally stop crashing. | technici | noun | True |
| C:170108:c3 | Zahraniční kritici chvália tohtoročný program festivalu. | This year's festival programme is being praised. | zahraniční kritici | noun | False |
| C:170109:c3 | Hneď ako komisia vyhodnotí prihlášky, organizátori pošlú uchádzačom výsledky. | As soon as the applications are evaluated, the results will be sent to the applicants. | organizátori | noun | True |
| C:170111:c3 | Táto aplikácia zbiera príliš veľa údajov o svojich používateľoch. | Too much data about users is collected. | táto aplikácia | noun | True |
| C:170112:c3 | Kurátorka presunula najcennejšie obrazy do vedľajšej sály ešte pred otvorením. | The most valuable paintings were moved to the next room before the opening. | kurátorka | noun | True |
| C:170113:c3 | Ak vláda schváli tú novelu, úrady zrušia poplatky za výpisy. | If that amendment is approved, the fees for extracts will be abolished. | úrady | noun | True |
| C:170114:c3 | Odkedy zaviedli nový systém, zamestnanci hlásia oveľa menej chýb. | Since the new system was introduced, far fewer errors have been reported. | zamestnanci | noun | True |
| C:170115:c3 | Napriek zlému počasiu organizátori nezrušili sobotný koncert. | Despite the bad weather, the Saturday concert was not cancelled. | organizátori | noun | True |
| C:170116:c3 | Práve táto poisťovňa pokrýva aj škody spôsobené vetrom. | Damage caused by wind is covered as well. | táto poisťovňa | noun | True |
| C:170119:c3 | Mnohé školy dnes nahrádzajú tlačené učebnice tabletmi. | Printed textbooks are being replaced with tablets today. | mnohé školy | noun | True |
| C:170120:c3 | Búrka minulý týždeň poškodila strechu telocvične a vyvrátila dva stromy. | Last week the roof of the gym was damaged and two trees were uprooted. | búrka | noun | False |

## A5 - the 11 agentless false accepts

caught: 10, missed: 1

| iid | answer | caught | why |
| --- | --- | --- | --- |
| W:170003:w2 | Our car will be washed tomorrow. | caught | agent môj brat |
| W:170012:w2 | A new book is being read now. | caught | agent ja |
| W:170021:w2 | Tomatoes are grown. | caught | agent môj dedko |
| W:170027:w2 | A new bridge was built. | caught | agent oni |
| W:170036:w2 | The new contracts are being signed right now. | caught | agent riaditeľ |
| W:170039:w2 | Lunch is being prepared. | caught | agent kuchár |
| W:170048:w2 | The lawn was mowed. | caught | agent záhradník |
| W:170051:w2 | Old furniture is repaired. | caught | agent môj otec |
| W:170054:w2 | A new coat was bought. | caught | agent ona |
| W:170058:w1 | A trip to the capital will be organised every spring. | caught | agent naša škola |
| W:170088:w2 | These textbooks will be lent for one semester only. | MISSED | the answer is not a marked passive without a by-agent |

## Side lines

- AG firings: 223 (AG-noun: 153). Detector vs writer tag: {"ag_fired & tag agentless": 217, "ag_fired & tag NOT agentless": 6, "ag_abstain & tag agentless": 53, "ag_abstain & tag NOT agentless": 804, "tag by-passive & ag_fired": 0}

- AG-noun pooled: coverage 371/483 = 76.81 % [72.79, 80.50], FA 9/597 = 1.51 % [0.69, 2.84]

- lever 1 OFF, no AG: coverage 401/483 = 83.02 % [79.37, 86.26], FA 9/597 = 1.51 % [0.69, 2.84]

- needs new call: 0
