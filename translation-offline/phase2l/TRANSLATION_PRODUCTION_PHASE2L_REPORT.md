# Translation production — Phase 2L report (22.9.2026)

Working directory: `~/Projects/and-again-content/translation-offline/phase2l/` (below: `P2L/`).
Brief: `P2L/BRIEF_2L.md`. Stage log: `P2L/PROGRESS.md`. Stages: S1 (Parts A-C), S2 (Part D), S3 (Part E), main session (SHA re-check), report agent (this file).

## 0. Headline: Czech measured. Coverage MET on the point and the interval, FA MET on the point only

**This is the FIRST OUT-OF-SAMPLE measurement of the SOURCE-ONLY design.** The Part C stop did NOT fire. Stack = frozen
`P2L/stack_2l_cz.py` (SOURCE-ONLY L3 + Part B content check, TIP rejected; Czech freeze commit f9f794c), run on a fresh Czech
production set opened ONCE (`P2L/partE/run/ACCESS_LOG_VERBATIM.md`: 1 open, sha256 94d7ad91…, 07:10:57Z). Truth = 4 opus judge
sessions (`P2L/partE/judge/labels.jsonl`). Part E freeze commit 24daf57 (`FROZEN_SHA_E.txt`, hash 81184cb5…), RUN_COMMIT b74d58c,
run-done commit 35b7774. Numbers: `P2L/partE/analysis/HEADLINE.json` (checked against `ANALYSIS.md`: identical).

Exact 95 % Clopper-Pearson:

| block | coverage (accepted / judge-correct) | >= 90 % point / interval | FA (accepted / judge-wrong) | < 5 % point / interval |
|---|---|---|---|---|
| **pooled** | **473/497 = 95.17 % [92.90, 96.88]** | **MET / MET** | **13/403 = 3.23 % [1.73, 5.45]** | **MET / missed** |
| A1 | 120/124 = 96.77 % [91.95, 99.11] | MET / MET | 2/101 = 1.98 % [0.24, 6.97] | MET / missed |
| A2 | 120/125 = 96.00 % [90.91, 98.69] | MET / MET | 2/100 = 2.00 % [0.24, 7.04] | MET / missed |
| B1 | 115/123 = 93.50 % [87.59, 97.15] | MET / missed | 4/102 = 3.92 % [1.08, 9.74] | MET / missed |
| B2 | 118/125 = 94.40 % [88.80, 97.72] | MET / missed | 5/100 = 5.00 % [1.64, 11.28] | missed / missed |

Diagnostic, L3 alone (before the content check): coverage 481/497 = 96.78 % [94.82, 98.15], FA 27/403 = 6.70 % [4.46, 9.60].
So, out of sample, the content check made **14 catches** (FA 27 -> 13) for **8 costs** (coverage 481 -> 473).

## 1. Part C: the configuration, on the closed Slovak sets

**CLOSED-SET, IN-SAMPLE** (2I + 2J Part D, existing judge labels, 0 extra calls). The content check was designed while reading
these sets, so these numbers are optimistic. Source: `P2L/partC/partC.md`.

| configuration | pooled coverage | pooled FA | A1 cov / FA | A2 cov / FA | B1 cov / FA | B2 cov / FA |
|---|---|---|---|---|---|---|
| reference-based stack (2I tonly / 2J fixed) | 893/995 = 89.75 % [87.69, 91.56] | 43/805 = 5.34 % [3.89, 7.13] | 92.34 / 2.48 | 94.40 / 7.50 | 83.40 / 6.40 | 88.80 / 5.00 |
| 2K SOURCE-ONLY, TIP rejected | 951/995 = 95.58 % [94.11, 96.77] | 73/805 = 9.07 % [7.18, 11.27] | 93.15 / 3.47 | 96.00 / 8.00 | 95.95 / 12.32 | 97.20 / 12.50 |
| 2K SOURCE-ONLY, TIP accepted (Part A) | 975/995 = 97.99 % [96.91, 98.77] | 312/805 = 38.76 % [35.38, 42.22] | 97.98 / 31.19 | 99.20 / 39.00 | 97.57 / 42.36 | 97.20 / 42.50 |
| **SOURCE-ONLY + B, TIP rejected (CHOSEN)** | **920/995 = 92.46 % [90.64, 94.03]** | **37/805 = 4.60 % [3.26, 6.28]** | 91.53 / 1.49 | 94.00 / 6.50 | 91.90 / 5.42 | 92.40 / 5.00 |
| SOURCE-ONLY + B, TIP accepted | 931/995 = 93.57 % [91.86, 95.01] | 131/805 = 16.27 % [13.79, 19.01] | 93.15 / 10.40 | 96.00 / 20.00 | 92.71 / 18.23 | 92.40 / 16.50 |

Per set, chosen config: 2I 463/497 = 93.16 % [90.57, 95.22] / 19/403 = 4.71 % [2.86, 7.26]; 2J 457/498 = 91.77 % [89.00, 94.03] / 18/402 = 4.48 % [2.67, 6.98].

Rule (brief): take the higher pooled coverage among configs with pooled FA < 5 % on the point; stop if none has coverage >= 90 % AND FA < 5 %.
Only TIP rejected qualifies. **Chosen: SOURCE-ONLY + B, TIP rejected**, frozen as `P2L/stack_2l.py` (TIP_ACCEPT = False),
`FROZEN_SHA_C.txt`, **freeze commit 0042aaa5697447155227999e4b7a392940d73cf9**.

## 2. Part B: the content check, item by item (CLOSED-SET, IN-SAMPLE)

`P2L/content_check.py`, prompt `P2L/spec/content_check_prompt.txt`, gemini-3.1-flash-lite, temperature 0, thinkingBudget 0. Input =
Slovak sentence + language name + answer only (no reference). It ran on every item L3 accepted under either TIP variant, one call per
unique request: **1,287 counted calls, 0 failed (0.00 %)**, 0 uncounted, $0.0945. Verdicts: NONE 1,062, MISSING 225.
2K's 35 added M false acceptances: **27/35 caught**, 0 failed calls. The 8 that got NONE: A:1507, A:2376, A:2640, A:3177, A:3506 in 2I; A:1599,
A:1852, A:2217 in 2J. Of all 44 FAs that 2K added, 28 were caught.

Summary per TIP handling (pooled; catch = judge-wrong newly rejected, cost = judge-correct newly rejected):

| TIP handling | checked (wrong/correct) | catches | cost | A1 catch/cost | A2 catch/cost | B1 catch/cost | B2 catch/cost |
|---|---|---|---|---|---|---|---|
| **TIP rejected (chosen)** | 1,024 (73/951) | **36** | **31** | 4/4 | 3/5 | 14/10 | 15/12 |
| TIP accepted | 1,287 (312/975) | 181 | 44 | 42/12 | 38/8 | 49/12 | 52/12 |

Every catch and every cost of the chosen TIP-rejected configuration, with the word the check named. The full 225-item list, including
effects seen only under TIP accepted, is in `P2L/partB/partB.md` and `partB.json`:

**Catches (36): judge-wrong, L3 accepted, content check named a missing word** (n = 36)

| # | set | id | lvl | writer | Slovak | answer | word named | M35 |
|---|---|---|---|---|---|---|---|---|
| 1 | 2I | A:1038:m | B1 | M | Kamarátka povedala, že náramok je príliš voľný, tak ho upravila. | My friend said that it was too loose, so she adjusted it. | náramok | yes |
| 2 | 2I | A:1099:m | A1 | M | Veľká huba rastie zo zeme. | A mushroom grows out of the ground. | Veľká | yes |
| 3 | 2I | A:110:m | B1 | M | Babka za jedno popoludnie zložila desiatky dumplingov, však? Absolútne neuveriteľné! | Grandma folded dozens of dumplings, didn't she? Absolutely incredible! | popoludnie |  |
| 4 | 2I | A:1212:m | B1 | M | Zajtra o takomto čase bude robiť pred zrkadlom tú istú grimasu s otvorenými ústami. | This time tomorrow, she will be making the same face with her mouth open. | pred zrkadlom |  |
| 5 | 2I | A:1397:m | B2 | M | Celé námestie kričí po hudbe, ktorú táto kapela hrá! | The square is screaming for the music this band plays! | celé | yes |
| 6 | 2I | A:1577:m | B2 | M | Na poludnie ona už bude chodiť po šatníku v župane dve hodiny. | By noon she will have been walking around the wardrobe for two hours. | župane | yes |
| 7 | 2I | A:1702:m | B1 | M | Počuj, vraj už spálila štyri marshmallowy a pálenie ju baví. | Listen, apparently she has already burned four and she enjoys burning them. | marshmallowy | yes |
| 8 | 2I | A:1806:m | B1 | M | Keď sa bábätko usmieva takto, každý si myslí, že je rozkošné. | When it smiles like this, everyone thinks it's adorable. | bábätko | yes |
| 9 | 2I | A:2050:m | B1 | M | Nabudúce ona dá silnejší úder päsťou, lebo sa bude viac snažiť. | Next time she will throw a punch because she will try harder. | silnejší | yes |
| 10 | 2I | A:2402:m | B1 | M | Hádaj čo, chalan, ktorého zviera skočilo z toho útesu, sa vraj ani nebál. | Guess what, the guy whose animal jumped apparently wasn't even scared. | útesu | yes |
| 11 | 2I | A:2463:m | B2 | M | Do Vianoc si z toho bábikovského svetra bude uťahovať už mesiace. | By Christmas he will have been making fun of that sweater for months. | bábikovského | yes |
| 12 | 2I | A:262:m | B1 | M | Zdravotník povedal, že film bol poslaný z laboratória hodinu predtým. | The paramedic said that the film had been sent an hour before. | laboratória | yes |
| 13 | 2I | A:2948:m | B2 | M | Dve červené nákladné lode priviezli svoj tovar do prístavu po mori. | Two cargo ships brought their goods to the port by sea. | červené | yes |
| 14 | 2I | A:2989:m | B2 | M | Samozrejme si dala trasu nakresliť na mapu, pre prípad, že by zabudla vlastný plán. | Of course she had the route drawn in case she forgot her own plan. | na mapu | yes |
| 15 | 2I | A:3096:m | B1 | M | Ona zvykla hrať celé hodiny každú noc, kým sa nestala profesionálnou hráčkou! Úplne posadnutá! | She used to play every night until she became a professional player! Totally obsessed! | celé hodiny | yes |
| 16 | 2I | A:3631:m | A1 | M | Každý môže sledovať tanec z balkónov. | The dance can be watched from the balconies. | Každý | yes |
| 17 | 2I | A:3797:m | A2 | M | Hej, v miestnosti bola nuda, ale teraz je to dosť živé. | Hey, it was boring, but now it's quite lively. | miestnosti |  |
| 18 | 2I | A:3934:m | B2 | M | Červený lampión svietil pri okne celé hodiny, kým sa rozsvietilo svetlo v kuchyni. | The lantern had been shining by the window for hours before the light in the kitchen came on. | Červený | yes |
| 19 | 2J | A:1413:m | B2 | M | Škrečok, ktorého preukaz otvára dvere kancelárie, odchádza o piatej. | The hamster whose pass opens the door leaves at five. | kancelárie |  |
| 20 | 2J | A:1568:m | A2 | M | Tam je voľné miesto! — Super, zaparkujem tam. | There's a space! — Great, I'll park there. | voľné | yes |
| 21 | 2J | A:1781:m | A2 | M | Farebná girlanda spadla, lebo lepiaca páska bola príliš slabá. Úplná katastrofa! | The garland fell down because the tape was too weak. A complete disaster! | farebná |  |
| 22 | 2J | A:1918:m | B2 | M | Úradník sa jej spýtal, či má pri sebe preukaz totožnosti. | She was asked whether she had her ID card with her. | úradník | yes |
| 23 | 2J | A:2152:m | B1 | M | Jeho stará mama mávala svoje poháre v tejto kuchynskej skrinke. | His grandmother used to keep her glasses in this cabinet. | kuchynskej | yes |
| 24 | 2J | A:2358:m | B1 | M | Had je skutočná hrozba a uhryzne každého, kto príde bližšie. | The snake is a threat and will bite anyone who comes closer. | skutočná | yes |
| 25 | 2J | A:2397:m | B2 | M | Povedala, že sa opláchne rýchlo, ale ostala pod sprchou desať minút. | She said she would rinse off, but she stayed in the shower for ten minutes. | rýchlo |  |
| 26 | 2J | A:2487:m | B2 | M | Kámo, kým doniesli tortu, každý príbuzný sa už dvakrát objal, fakt. | Dude, by the time they brought the cake, every relative had already hugged, seriously. | dvakrát | yes |
| 27 | 2J | A:2825:m | B1 | M | Kedysi tu býval študentom, ale teraz sa mu trieda klania. | He used to be a student, but now the class bows to him. | tu | yes |
| 28 | 2J | A:3412:m | B2 | M | Takže, do budúceho týždňa vraj vyrozprávajú príbeh o útoku býka všetkým. | So, by next week they will supposedly have told the story about the attack to everyone. | býka |  |
| 29 | 2J | A:3434:m | B1 | M | Kamarátka, ktorá jej zatlačila chodidlo dozadu, mala ten istý kŕč už stokrát. | The friend who pushed her foot back has had the cramp a hundred times already. | mala |  |
| 30 | 2J | A:365:m | B1 | M | Ak cena pôjde ešte vyššie, položí tabuľku. | If the price goes even higher, she'll put it down. | tabuľku | yes |
| 31 | 2J | A:3963:m | B2 | M | Strany sprievodcu si pred cestou dali zalaminovať. | They had the pages laminated before the trip. | sprievodcu | yes |
| 32 | 2J | A:3970:m | B2 | M | Počuj, vraj z toho veľkého hrnca vyráža para zakaždým, keď zdvihne pokrievku. | Listen, apparently steam bursts out of that pot every time he lifts the lid. | veľkého | yes |
| 33 | 2J | A:3970:t | B2 | T | Počuj, vraj z toho veľkého hrnca vyráža para zakaždým, keď zdvihne pokrievku. | Listen, apparently steam burst out of that big pot every time he lifted the lid. | vyráža |  |
| 34 | 2J | A:40:m | A1 | M | Melón má štyridsať gumičiek, takže ich má štyridsať. | The melon has forty, so it has forty of them. | gumičiek | yes |
| 35 | 2J | A:497:m | A1 | M | Tieto miesta vzadu sú úplne prázdne! | These seats are completely empty! | vzadu | yes |
| 36 | 2J | A:592:m | B2 | M | Sviečky zapália, len čo posledné taniere budú na čerstvom obruse. | They will light the candles as soon as the plates are on the fresh tablecloth. | posledné | yes |

**Costs (31): judge-correct, L3 accepted, content check named a missing word** (n = 31)

| # | set | id | lvl | writer | Slovak | answer | word named | M35 |
|---|---|---|---|---|---|---|---|---|
| 1 | 2I | A:1004:c4 | B1 | - | Muž volal hlasným hlasom, keď sa obloha sfarbila do fialova. | A man was calling loudly when the sky went purple. | hlasným |  |
| 2 | 2I | A:2798:c1 | B1 | - | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | This time tomorrow, the subject will be unlocking the same wooden door, as it usually does. | dvere |  |
| 3 | 2I | A:2798:c2 | B1 | - | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | At this hour tomorrow the subject will be unlocking the same wooden door, as he usually does. | dvere |  |
| 4 | 2I | A:2798:c3 | B1 | - | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | Tomorrow at this time, the subject will be unlocking that same wooden door, just as they usually do. | dvere |  |
| 5 | 2I | A:2798:c4 | B1 | - | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | At this time tomorrow the subject will unlock the same wooden door, as usual. | dvere |  |
| 6 | 2I | A:2798:c5 | B1 | - | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | This time tomorrow the subject will be unlocking the same wooden door like it normally does. | dvere |  |
| 7 | 2I | A:3783:c3 | B1 | - | Keď pred zápasom hrá hymna, hráčky si dajú ruky na hruď. | Whenever the anthem plays before a match, the players put a hand on their chest. | ruky |  |
| 8 | 2I | A:3899:c1 | B2 | - | Keď vošla na trh, netušila, že odíde von s dvoma metrami zlatej potlače. | When she entered the market, she had no idea that she would leave with two metres of gold print. | von |  |
| 9 | 2I | A:3899:c3 | B2 | - | Keď vošla na trh, netušila, že odíde von s dvoma metrami zlatej potlače. | As she went into the market, she had no idea she was going to leave with two metres of gold print. | von |  |
| 10 | 2I | A:462:c3 | A2 | - | Ty bojuješ s tou alergiou lepšie než ktokoľvek na tejto lúke. Ikonické. | You deal with that allergy better than anyone on this meadow. Iconic. | bojuješ |  |
| 11 | 2I | A:462:c5 | A2 | - | Ty bojuješ s tou alergiou lepšie než ktokoľvek na tejto lúke. Ikonické. | You cope with the allergy better than anybody in this meadow. Iconic. | bojuješ |  |
| 12 | 2I | A:842:c1 | B2 | - | Smoothie mu skočilo rovno na nos, takže mal vrchnák vtedy zatlačiť silnejšie. | The smoothie splashed right onto his nose, so he should have pressed the lid harder then. | skočilo |  |
| 13 | 2I | A:842:c2 | B2 | - | Smoothie mu skočilo rovno na nos, takže mal vrchnák vtedy zatlačiť silnejšie. | The smoothie jumped straight onto his nose, so he should have pushed the lid down harder at that time. | zatlačiť |  |
| 14 | 2I | A:842:c4 | B2 | - | Smoothie mu skočilo rovno na nos, takže mal vrchnák vtedy zatlačiť silnejšie. | The smoothie flew straight onto his nose, so he should've pressed the lid harder then. | skočilo |  |
| 15 | 2J | A:1720:c4 | B2 | - | Keby mu sestry ráno barle nenastavili, bol by skončil na tvár pred celým oddelením. | If his crutches hadn't been adjusted by the nurses in the morning, he would have ended up on his face in front of the whole ward. | nastaviť |  |
| 16 | 2J | A:1849:c4 | B2 | - | Nebudem klamať, ty si prehľadával svoju peňaženku celú večnosť, kým si sa uškrnul ako bohatý muž. | Not gonna lie, you'd been going through your wallet for ages before grinning like a wealthy man. | prehľadával |  |
| 17 | 2J | A:1939:c4 | A1 | - | Stojíš naraz v štyroch farbách. Klobúk dole. | You're wearing four colours at once. Hats off. | Stojíš |  |
| 18 | 2J | A:2069:c3 | A2 | - | Pouličný hudobník spieva nejaké piesne a dav počúva. | The busker sings a few songs and the crowd listens. | nejaké |  |
| 19 | 2J | A:2152:c3 | B1 | - | Jeho stará mama mávala svoje poháre v tejto kuchynskej skrinke. | His grandmother would keep her glasses in this kitchen cabinet. | poháre |  |
| 20 | 2J | A:2152:c5 | B1 | - | Jeho stará mama mávala svoje poháre v tejto kuchynskej skrinke. | His grandmother used to keep her glasses here in this kitchen cabinet. | poháre |  |
| 21 | 2J | A:22:c1 | B2 | - | Keby administratíva prestala skôr, ona by sa nezvalila na stôl. | If the paperwork had stopped earlier, she wouldn't have collapsed onto the desk. | administratíva |  |
| 22 | 2J | A:22:c2 | B2 | - | Keby administratíva prestala skôr, ona by sa nezvalila na stôl. | If the admin work had ended sooner, she would not have slumped onto the table. | administratíva |  |
| 23 | 2J | A:22:c5 | B2 | - | Keby administratíva prestala skôr, ona by sa nezvalila na stôl. | If the paperwork had finished earlier, she wouldn't have slumped down on the desk. | administratíva |  |
| 24 | 2J | A:2359:c4 | A1 | - | Vodu napúšťa do bieleho drezu. | He lets water into the white sink. | napúšťa |  |
| 25 | 2J | A:2829:c5 | A1 | - | Prečo je piesok teplý? Lebo svieti slnko. | Why is the sand warm? The sun is shining. | Lebo |  |
| 26 | 2J | A:3144:c4 | A1 | - | Toto kopnutie vyhadzuje lístie do vzduchu. | This kick is throwing leaves into the air. | kopnutie |  |
| 27 | 2J | A:3412:c4 | B2 | - | Takže, do budúceho týždňa vraj vyrozprávajú príbeh o útoku býka všetkým. | So, by next week the story of the bull attack will apparently have been told to everyone. | vyrozprávajú |  |
| 28 | 2J | A:362:c4 | A2 | - | On používa toľko zelenej farby na stenu. | He puts so much green paint on the wall. | používa |  |
| 29 | 2J | A:365:c3 | B1 | - | Ak cena pôjde ešte vyššie, položí tabuľku. | If the price rises even higher, she will lower her paddle. | položí |  |
| 30 | 2J | A:833:c4 | B2 | - | Nikdy predtým nebolo toľko ľudí okolo jedného novonarodeného bábätka. | Never before had so many people been around a single newborn. | bábätka |  |
| 31 | 2J | A:865:c3 | A2 | - | Pravidlá tábora: každý sa musí zobudiť pred raňajkami. | The camp rules: everyone must get up before breakfast. | zobudiť |  |


Reading of the costs: the 31 costs come from 16 distinct sentences, because several correct answers to one sentence were all rejected
(A:2798 x5 "dvere", A:22 x3, A:842 x3). The word named is often present in the answer as a synonym or a tolerable paraphrase
(dvere -> door, bojuješ -> deal with / cope with, skočilo -> splashed / flew). Twice it is a function word (**Lebo**, **nejaké**), plus
**jedny** and **im** in items that are costs only under TIP accepted. See defect 2.

## 3. Part A: TIP under SOURCE-ONLY (0 calls)

`P2L/partA/partA.md`. TIP rejected reproduces 2K `part3.json` exactly (every set, level and CP bound): YES. L3 TIP items by judge label:
239 wrong / 24 correct pooled (2I 127/13, 2J 112/11). Effect of accepting TIP:

| pooled | TIP rejected | TIP accepted |
|---|---|---|
| coverage | 951/995 = 95.58 % [94.11, 96.77] | 975/995 = **97.99 %** [96.91, 98.77] |
| FA | 73/805 = 9.07 % [7.18, 11.27] | 312/805 = **38.76 %** [35.38, 42.22] |

TIP is overwhelmingly a wrong-answer signal (239:24). Accepting it buys +24 coverage for +239 FA. Even behind the content check
(Part C), TIP accepted stays at 16.27 % FA. TIP stays a rejection.

## 4. Czech false rejections and false acceptances, by cause (every item)

### 4.1 False rejections (24)

By layer: content check MISSING 8, L3 DIFF 6, L3 TIP (rejected) 8, F4v2 2. By level: A1 4, A2 5, B1 8, B2 7. All 24 are
judge-correct answers from correct-type writers.

| aid | lvl | layer | cc word | writer | Czech | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:4171:c4 | A2 | CC:MISSING | Na autě | correct/ | Na autě jsou dvě čistá zrcátka. | The car has got two clean mirrors. | Same meaning |
| A:4220:c3 | B1 | L3 |  | correct/ | Zítra v tuhle dobu si ona zase bude dávat pauzu na tom gauči, bez kecu, kámo. | Tomorrow at this time she'll be having a break on that couch again, seriously, bro. | Same meaning, grammatical. |
| A:4587:c5 | B1 | CC:MISSING | přepadá | correct/ | Tahle nevolnost přepadá každého jezdce už hodinu! Totální noční můra! | This nausea has been getting every rider for an hour! A total nightmare! | Same meaning, colloquial but correct. |
| A:4591:c5 | A1 | L3:TIPrej |  | correct/ | Praští ho svým velkým bílým polštářem. | She'll hit him with her big white pillow. | Perfective present rendered as future; correct. |
| A:4627:c5 | A2 | L3:TIPrej |  | correct/ | Oči sovy jsou jasnější než displej mého telefonu. | The owl has eyes brighter than my phone's screen. | Same meaning |
| A:4641:c5 | A1 | L3 |  | correct/ | Podívá se na své hodinky a zpanikaří. | He'll look at his watch and panic. | Perfective present rendered as future, fine |
| A:5012:c2 | B2 | CC:MISSING | o tom | correct/ | O tom průvodu se říká, že ho zorganizovali za dva dny. | It is said that the parade was organised in two days. | No agent named in Czech; meaning kept. |
| A:5065:c2 | A2 | L3:TIPrej |  | correct/ | Brácho, kolik hranolků sní? Celej talíř, fakt. | Bro, how many chips is she going to eat? The whole plate, seriously. | Same meaning |
| A:5168:c5 | B1 | L3:TIPrej |  | correct/ | Kdyby byl obrovský hrnek úplně naplněný, jeho zvednutí by vyžadovalo značné úsilí. | If the huge cup were full, it would take a great deal of effort to lift it. | Only a degree adverb is dropped |
| A:5543:c1 | B2 | L3 |  | correct/ | Asi si přeje, aby netáhl boty po jezeře. Mokré ponožky, dokonalost. | She probably wishes he hadn't dragged his shoes through the lake. Wet socks, perfection. | Accurate meaning and grammar. |
| A:5543:c4 | B2 | L3 |  | correct/ | Asi si přeje, aby netáhl boty po jezeře. Mokré ponožky, dokonalost. | She must wish he hadn't dragged his boots through the lake. Wet socks, perfection. | Accurate |
| A:6061:c4 | B1 | CC:MISSING | Horní | correct/ | Horní míček byl hozen přes celý stůl a nikdo tomu nevěřil! | The ball on top was thrown across the whole table, and no one believed it! | Accurate |
| A:6320:c4 | B2 | L3:TIPrej |  | correct/ | Brácho, ta slanina se smaží tak pět minut a pořád prská, fakt. | Bro, that bacon has been in the pan for about five minutes and it keeps spitting, seriously. | Same meaning |
| A:6548:c4 | B1 | CC:MISSING | přikázala | correct/ | Než se slunce dotklo vody, přikázala té řadě dvakrát běžet. | Before the sun touched the water, she had told that row to run two times. | Same meaning |
| A:6548:c5 | B1 | CC:MISSING | řadě | correct/ | Než se slunce dotklo vody, přikázala té řadě dvakrát běžet. | Before the sun reached the water, she had commanded the row to run twice. | Accurate |
| A:6722:c5 | A2 | F4v2 |  | correct/ | On ji včera objal na zlaté louce. | She was hugged by him yesterday in the golden meadow. | Passive keeps named agent 'by him' |
| A:6761:c5 | B2 | L3:TIPrej |  | correct/ | V kanceláři se usmívá jako první, ačkoli stráví dvě hodiny denně v tramvaji. | In the office she is always first to smile, though she spends two hours each day on the tram. | Accurate; habitual sense preserved |
| A:6849:c4 | A1 | CC:MISSING | jedné | correct/ | Chaos! Deset kachen v jedné řadě a číslo deset je poslední! | Chaos! Ten ducks in a row and number ten comes last! | Same meaning |
| A:6901:c4 | B2 | F4v2 |  | correct/ | Přeje si, aby věděl aspoň něco o trubkách. | She'd like him to know at least something about pipes. | Wish meaning preserved. |
| A:6901:c5 | B2 | L3 |  | correct/ | Přeje si, aby věděl aspoň něco o trubkách. | If only he knew at least something about pipes, she thinks. | Wish meaning preserved. |
| A:7105:c2 | A1 | CC:MISSING | leží | correct/ | Zápalky leží v malé dřevěné krabičce. | The matches are in a small wooden box. | Accurate meaning. |
| A:7120:c5 | B1 | L3 |  | correct/ | Fanoušek uvedl, že jeho věrnost začala přibližně před čtyřiceti lety. | The fan said his loyalty started some forty years before. | Correct reported speech, same meaning |
| A:7280:c4 | B1 | L3:TIPrej |  | correct/ | Jestli ji nakreslí výš na pláži, moře na ni nedosáhne | If she draws it higher up the beach, the waves won't get to it. | Same meaning; waves reaching equals sea reaching. |
| A:7792:c5 | A2 | L3:TIPrej |  | correct/ | Podívej na ten prut! Dědeček právě se chystá vytáhnout rybu ven. | Look at that fishing pole! Grandpa is about to take the fish out. | Same meaning, grammatical. |


Cause reading: the 8 TIP rejections are TIPs the judge rated correct (perfective present -> future, habitual, synonyms). The 8
content-check costs name a word the answer covers (leží -> "are in", přikázala -> "told", řadě -> "row") or a function word
(**o tom**, **jedné**, partly **Na autě**). The 2 F4v2 rejections are a passive that keeps its named agent (A:6722:c5) and a wish
paraphrase (A:6901:c4).

### 4.2 False acceptances (13)

All 13 passed L3 (SAME) AND the content check (NONE). By writer type: M 8, T 3, W 1, correct-type writer 1. By level: A1 2, A2 2, B1 4, B2 5.

| aid | lvl | layer | cc | writer type | Czech | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:4236:m | B1 | L3+CC:NONE | none | M | Poslouchej, žralok, kterého zachránil, se prý druhý den vrátil. | Listen, the shark that was saved apparently came back the next day. | Passive drops named agent 'he' |
| A:4386:m | B2 | L3+CC:NONE | none | M | Kdyby byla typ, co to vzdává, tu pásku by teď nedržela. | If she were the type, she wouldn't be holding the tape now. | Drops 'who gives up' |
| A:4386:w | B2 | L3+CC:NONE | none | W | Kdyby byla typ, co to vzdává, tu pásku by teď nedržela. | If she were the type who gives up, she wouldn't be holding the rope now. | 'rope' instead of tape. |
| A:4587:m | B1 | L3+CC:NONE | none | M | Tahle nevolnost přepadá každého jezdce už hodinu! Totální noční můra! | This nausea has been hitting everyone for an hour! A total nightmare! | Noun 'rider' dropped. |
| A:4623:m | A2 | L3+CC:NONE | none | M | Holič obvykle holí brady, ale teď češe hustý plnovous. | The barber usually shaves chins, but now he is combing a full beard. | Adjective 'thick' dropped. |
| A:4837:m | A1 | L3+CC:NONE | none | M | Ona dělá každou neděli k obědu těstoviny, to se musí milovat, kámo. | She makes pasta every Sunday, you've got to love that, mate. | Drops 'for lunch'. |
| A:5065:t | A2 | L3+CC:NONE | none | T | Brácho, kolik hranolků sní? Celej talíř, fakt. | Bro, how many fries did he eat? A whole plate, really. | Past instead of future |
| A:5638:c3 | B1 | L3+CC:NONE | none | None | Prostorná pohovka, kterou chtěl jen pro sebe, byla úplně obsazena! | The big spacious sofa he wanted only for himself was fully occupied! | Added 'big' |
| A:6761:m | B2 | L3+CC:NONE | none | M | V kanceláři se usmívá jako první, ačkoli stráví dvě hodiny denně v tramvaji. | She's the first to smile, even though she spends two hours a day on the tram. | Place phrase 'at the office' dropped. |
| A:6834:m | B2 | L3+CC:NONE | none | M | Kámo, do poledne ten úředník povolí vstup do země tak 200 lidem, fakt. | Dude, by noon that official will have granted about 200 people entry, seriously. | Direction phrase 'into the country' dropped. |
| A:6849:t | A1 | L3+CC:NONE | none | T | Chaos! Deset kachen v jedné řadě a číslo deset je poslední! | Chaos! Ten ducks were in one row and number ten was last! | Past time frame; Czech is present. |
| A:6913:m | B2 | L3+CC:NONE | none | M | Není to ideální: tým tu stojí už hodinu a horizont pořád vypadá úplně stejně. | It's not ideal: the team has been standing for an hour and the horizon still looks exactly the same. | Drops the place word 'here' |
| A:7867:t | B1 | L3+CC:NONE | none | T | Kdyby byly neonové nápisy ještě jasnější, potřebovala by o půlnoci sluneční brýle. Dokonalé osvětlení. | If the neon signs had been even brighter, she would have needed sunglasses at midnight. Perfect lighting. | Past unreal; the Czech is present unreal |


Cause reading: 8 of the 13 are M, where a modifier, place phrase or noun was dropped (rider, thick, for lunch, at the office, into the
country, here, who gives up, agent "he"). The content check said NONE on all 8, so out of sample it misses small modifiers and
adverbial phrases, not head nouns. 3 are T (wrong tense frame: past for future, present or present unreal). The check does not test
tense by design (S1's added line, defect 1). 1 is W (tape -> rope) and 1 is an added word ("big").

## 5. Part D: the Czech stack and its gold validation

Stack: `P2L/stack_2l_cz.py` + `stack_source_cz.py` (= `stack_source.py` + `cz_assemble.SUBS` only, test T16). `cz_assemble.py`
binds phase1v cz_reader's 4 fixes into the AG chain. `f4fix.build_fixed(CK, 'cz')` serves F4v2/F4v3. L3 runs on the Czech sentence with the
SOURCE-ONLY spec `phase2k/spec/l3_system_cz.txt` + `l3_user_cz.txt` (T17: no reference or English sentence is sent). The content check
uses language 'Czech'. TIP is rejected. `test_2l_cz`: **19/19 PASS** (121 mocked calls, 0 real; re-run in S3 before the freeze). Freeze commit
**f9f794c67c216a153c67a602583621cd6cf0f8d8** (`FROZEN_SHA_D.txt`).

Gold validation (`P2L/partD/gold_validation.md`): the 1T validator `phase1t/taskB/cz_validate.py`, unchanged, 120 gold rows, run once,
0 model calls. Cells = agree / conservative / ERROR:

| guard | in SOURCE-ONLY stack | CZ assembled (2L) | CZ 1V after | CZ 1T before | SK (stored) |
|---|---|---|---|---|---|
| g1 F9 | no | 82 / 37 / 1 | 82 / 37 / 1 | 82 / 35 / 3 | 96 / 23 / 1 |
| g2 F4v2 | yes | 16 / 89 / 15 | 16 / 89 / 15 | 17 / 83 / 20 | 17 / 87 / 16 |
| g3 AG v2 | yes | 59 / 16 / 45 | 59 / 16 / 45 | 53 / 6 / 61 | 55 / 18 / 47 |
| g3 AG v3 | yes | 59 / 16 / 45 | 59 / 16 / 45 | 53 / 6 / 61 | 55 / 18 / 47 |
| g4 voice v2 | yes | 100 / 0 / 20 (16 as-passive, 4 as-active) | same | 108 / 0 / 12 | 98 / 0 / 22 |
| g4 voice v3 | yes | 97 / 0 / 23 (20 as-passive, 3 as-active) | same | 105 / 0 / 15 | 98 / 0 / 22 |

Czech class changes vs 1V Track C after: none in any guard. The Czech assembly is the 1V state, no better and no worse, and its g4
errors match the Slovak ones (defect 7). The validator's Slovak control equals the stored figures: True. Note: Czech g2 uses the 2J-fixed
reader; the stored Slovak g2 is the unfixed checker_1i reader.

## 6. The Czech upload file

`P2L/upload/upload_cz_final.xlsx` (sheet `cz`: exercise_id, language_code, level, src, en, structure_json) +
`annotations_cz_final.jsonl`, built by `build_upload_cz.py` mirroring 2K `build_upload.py` (`P2L/upload/UPLOAD_CZ_CHECK.md`).
**4,064 rows**, 4,064 unique int ids, `v[0] == en` on every row, language_code cz, header OK, written file == source, jsonl == source.
50 rows with empty `v` were set to `[en]` as in 2I Part 0 (defect 6). Against phase2j `annotations_cz_fixed.jsonl`: same ids, 0 `v`
differences, 107 B3 entries listed. `v` is display-only; the checker never grades against `en` / `v`. The 2K reference-ending scan found
102 broad hits and 1 strict, identical to 2K's Czech scan (0 new, 0 gone). Nothing was uploaded and no DB was touched.

## 7. Gemini calls and spend

| stage | calls (HTTP 200) | failed | spend |
|---|---:|---:|---:|
| S1 Part B content check (S1_B2) | 1,287 | 0 | $0.0945 |
| S2 Part D | 0 | 0 | $0 |
| S3 Part E L3 (S3E_L3) | 896 | 0 | $0.1272 (L3 + content check together) |
| S3 Part E content check (S3E_CC) | 508 | 0 | (included above) |
| **total** | **2,691 of 3,500** (809 left) | 0 | **$0.2217** |

Counts come from `P2L/GEMINI_LEDGER.json`. The ledger stores counts only, so the dollars come from `partB.json` (0.094508) and
`HEADLINE.json` (0.127226). This report made 0 Gemini calls.

## 8. Claude tokens against the 2,000,000 budget

| session | tokens |
|---|---:|
| main session (estimate) | ≈ 110,000 |
| S1 agent (Parts A-C) | 155,035 |
| S2 agent (Part D) | 152,342 |
| S3 agent (Part E, its own context) | 136,953 |
| headless writers: A1 53,925 / A2 57,949 / B1 52,987 / B2 54,906 | 219,767 |
| headless judges: s1 79,019 / s2 78,204 / s3 78,415 / s4 77,420 | 313,058 |
| this report agent (estimate) | ≈ 75,000 |
| **total** | **≈ 1,162,155** |
| **remainder of 2,000,000** | **≈ 837,845** |

Headless writers + judges = 532,825 (`P2L/TOKENS.md`), within the S3 stage cap of 1,400,000 (projection 1,006,693). No judge retry was needed.

## 9. Judge noise

80 hidden duplicate items, each judged in two different sessions: **0/80 disagree = 0.0 % [0.0, 4.51]**.

## 10. Defects recorded, NOT fixed

1. **The content-check prompt has one line that is not in the brief.** S1 added: "Judge word meaning only; tense, articles and word
   order are not part of this question." This keeps tense out of the check, so 3 of the 13 Czech FAs are tense (T) errors that pass it
   by construction. Owner to accept or strike the line.
2. **The content check misfires on function words.** Slovak costs: **Lebo** (A:2829:c5), **nejaké** (A:2069:c3); costs only under TIP
   accepted: **jedny**, **im**. Czech costs: **o tom** (A:5012:c2), **jedné** (A:6849:c4), and partly **Na autě** (A:4171:c4, a
   prepositional phrase rendered as "has got"). No stop-list was added.
3. **The 2K defect-3 judge line was REPLACED, not deleted.** Per `P2L/partE/judge/PROMPT_CHANGE.md`, "- A dropped function word is
   correct, a dropped content word is wrong, added content is wrong." was replaced by "- Added content is wrong." (the one clause the
   KIND ruling does not restate). Owner to confirm this is what "drop the line" meant.
4. **The judge per-session 400k cap** is enforced only before spawn (reservation), after the session (post-hoc check) and by the
   2,400 s wall kill, not during the session. No session came near it (max 79,019).
5. **The partE chain's own SHA check used the wrong file scope.** The chain printed "sha diff lines: 755" (`P2L/partE/chain.log`)
   because it hashed a different set of files: checker/ and other S0 directories were missing from its after-list. The main session
   re-hashed the full S0 scope: `P2L/SHA_after_main.txt` vs `SHA_before.txt` = **0 differences over 4,475 files**. The chain's check
   itself is still wrong.
6. **50 phase2h rows with empty `v`** were set to `[en]` in the Czech upload, as 2I Part 0 did for Slovak. This is an inherited data
   patch, not a fix at the source.
7. **Czech voice guard errors 20/23 (g4 v3), inherited from 1V** (16/20 as-passive under v2). Unchanged in 2L.
8. **The guards_c lazy checker bug** was caught and fixed in Part D. Test T10b now asserts that `guards_c._C` is the Czech CK after a
   full run, and the fix is in the frozen stack.
9. **Slovak Parts B and C are closed-set and in-sample**: the content check and the TIP decision were designed on the sets they are
   scored on. Only the Czech Part E number is out of sample.
10. **Part E chain attempt 1 stopped at make_set** (`P2L/partE/CHAIN_FAIL_attempt1.txt`, 07:04:01Z, commit 033f5b3), before any set
    was opened or any model was called. Attempt 2 ran clean, and the access log shows the set was opened once.
11. **Out of sample, the content check misses small modifiers and adverbials**: all 8 Czech M FAs passed with NONE (thick, for lunch,
    at the office, into the country, here, rider, who gives up, agent "he").
12. The main-session and report-agent token rows are estimates, not counted figures.

## 11. Judgement

1. The content check fixes SOURCE-ONLY's FA problem on the point: Slovak closed-set 9.07 % -> 4.60 % (in-sample), Czech out of sample 6.70 % -> 3.23 % (14 catches for 8 costs).
2. Czech coverage meets the target on the point and the interval (95.17 % [92.90, 96.88]); B1 and B2 meet it on the point only.
3. Czech FA meets the target on the point only (3.23 %, upper bound 5.45 %); B2 sits at 5.00 % and misses even on the point.
4. This is ONE out-of-sample measurement of a new layer; 8 of the 13 remaining FAs are dropped modifiers the check did not see.
5. Czech is fit to upload on the point estimate (`P2L/upload/upload_cz_final.xlsx`, 4,064 rows), but the FA interval is not met. The owner decides; nothing was uploaded.
