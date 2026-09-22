# Phase 2L Part B: SOURCE-SIDE content check - CLOSED-SET, IN-SAMPLE

**CLOSED-SET, IN-SAMPLE re-score.** Both Slovak sets (2I, 2J Part D) were read while SOURCE-ONLY and this check were designed; these are not fresh-set numbers. Existing judge labels; 2K SOURCE-ONLY L3 replies are the STORED ones.

Check: content_check.py, prompt spec/content_check_prompt.txt, gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, input = Slovak sentence + language name + answer only. Run on every item L3 accepted under either TIP variant (L3 SAME or L3 TIP), one call per unique request.

Gemini: 1287 counted (HTTP 200) calls, 0 uncounted attempts, spend $0.0945; failed (unparsable) calls 0 = 0.00 %. Verdicts over the 1287 checked items: {"none": 1062, "missing": 225}.

2K's 35 added writer-type M false acceptances: **27 caught**, 0 failed calls. All 44 added FAs: 28 caught.

## Catches (judge-wrong newly rejected) and cost (judge-correct newly rejected)

| TIP handling | set | level | checked (wrong/correct) | catches | cost | failed calls (rate) |
|---|---|---|---|---|---|---|
| tip rejected | 2I | all | 514 (37/477) | 18 | 14 | 0 (0.00 %) |
| tip rejected | 2I | A1 | 119 (3/116) | 2 | 0 | 0 (0.00 %) |
| tip rejected | 2I | A2 | 127 (8/119) | 1 | 2 | 0 (0.00 %) |
| tip rejected | 2I | B1 | 131 (14/117) | 9 | 7 | 0 (0.00 %) |
| tip rejected | 2I | B2 | 137 (12/125) | 6 | 5 | 0 (0.00 %) |
| tip rejected | 2J | all | 510 (36/474) | 18 | 17 | 0 (0.00 %) |
| tip rejected | 2J | A1 | 119 (4/115) | 2 | 4 | 0 (0.00 %) |
| tip rejected | 2J | A2 | 129 (8/121) | 2 | 3 | 0 (0.00 %) |
| tip rejected | 2J | B1 | 131 (11/120) | 5 | 3 | 0 (0.00 %) |
| tip rejected | 2J | B2 | 131 (13/118) | 9 | 7 | 0 (0.00 %) |
| tip rejected | pooled | all | 1024 (73/951) | 36 | 31 | 0 (0.00 %) |
| tip rejected | pooled | A1 | 238 (7/231) | 4 | 4 | 0 (0.00 %) |
| tip rejected | pooled | A2 | 256 (16/240) | 3 | 5 | 0 (0.00 %) |
| tip rejected | pooled | B1 | 262 (25/237) | 14 | 10 | 0 (0.00 %) |
| tip rejected | pooled | B2 | 268 (25/243) | 15 | 12 | 0 (0.00 %) |
| tip accepted | 2I | all | 654 (164/490) | 96 | 21 | 0 (0.00 %) |
| tip accepted | 2I | A1 | 156 (35/121) | 22 | 3 | 0 (0.00 %) |
| tip accepted | 2I | A2 | 165 (40/125) | 18 | 5 | 0 (0.00 %) |
| tip accepted | 2I | B1 | 162 (43/119) | 29 | 8 | 0 (0.00 %) |
| tip accepted | 2I | B2 | 171 (46/125) | 27 | 5 | 0 (0.00 %) |
| tip accepted | 2J | all | 633 (148/485) | 85 | 23 | 0 (0.00 %) |
| tip accepted | 2J | A1 | 150 (28/122) | 20 | 9 | 0 (0.00 %) |
| tip accepted | 2J | A2 | 161 (38/123) | 20 | 3 | 0 (0.00 %) |
| tip accepted | 2J | B1 | 165 (43/122) | 20 | 4 | 0 (0.00 %) |
| tip accepted | 2J | B2 | 157 (39/118) | 25 | 7 | 0 (0.00 %) |
| tip accepted | pooled | all | 1287 (312/975) | 181 | 44 | 0 (0.00 %) |
| tip accepted | pooled | A1 | 306 (63/243) | 42 | 12 | 0 (0.00 %) |
| tip accepted | pooled | A2 | 326 (78/248) | 38 | 8 | 0 (0.00 %) |
| tip accepted | pooled | B1 | 327 (86/241) | 49 | 12 | 0 (0.00 %) |
| tip accepted | pooled | B2 | 328 (85/243) | 52 | 12 | 0 (0.00 %) |

## Every item the check rejected or failed on (225)

effect columns: catch = judge-wrong newly rejected; COST = judge-correct newly rejected; - = not checked in that variant (L3 TIP is already a rejection when TIP is rejected). M35 = one of 2K's 35 added M false acceptances.

| # | set | id | level | writer | judge | L3 | Slovak | answer | word named / raw | TIP rej | TIP acc | M35 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2I | A:1004:c4 | B1 | None | correct | SAME | Muž volal hlasným hlasom, keď sa obloha sfarbila do fialova. | A man was calling loudly when the sky went purple. | hlasným | COST | COST |  |
| 2 | 2I | A:1004:m | B1 | M | wrong | TIP | Muž volal hlasným hlasom, keď sa obloha sfarbila do fialova. | The man was calling when the sky turned purple. | hlasným hlasom | - | catch |  |
| 3 | 2I | A:1038:m | B1 | M | wrong | SAME | Kamarátka povedala, že náramok je príliš voľný, tak ho upravila. | My friend said that it was too loose, so she adjusted it. | náramok | catch | catch | yes |
| 4 | 2I | A:1038:s | B1 | S | wrong | TIP | Kamarátka povedala, že náramok je príliš voľný, tak ho upravila. | My friend said that the bracelet was too loose, so she adjust it. | upravila | - | catch |  |
| 5 | 2I | A:1099:m | A1 | M | wrong | SAME | Veľká huba rastie zo zeme. | A mushroom grows out of the ground. | Veľká | catch | catch | yes |
| 6 | 2I | A:1106:s | B1 | S | wrong | TIP | Keby ryby mali ruky, ony by tlieskali tomu nahodeniu. Naozaj legendárna technika. | If fish had hands, they would applauded that cast. A truly legendary technique. | tlieskali | - | catch |  |
| 7 | 2I | A:110:m | B1 | M | wrong | SAME | Babka za jedno popoludnie zložila desiatky dumplingov, však? Absolútne neuveriteľné! | Grandma folded dozens of dumplings, didn't she? Absolutely incredible! | popoludnie | catch | catch |  |
| 8 | 2I | A:110:s | B1 | S | wrong | TIP | Babka za jedno popoludnie zložila desiatky dumplingov, však? Absolútne neuveriteľné! | Grandma folded dozens of dumpling in one afternoon, didn't she? Absolutely incredible! | zložila | - | catch |  |
| 9 | 2I | A:1145:s | A2 | S | wrong | TIP | Neuveriteľné! Nie je veľa darčekov veľkých ako babka! | Incredible! There isn't many presents as big as grandma! | veľa | - | catch |  |
| 10 | 2I | A:1212:m | B1 | M | wrong | SAME | Zajtra o takomto čase bude robiť pred zrkadlom tú istú grimasu s otvorenými ústami. | This time tomorrow, she will be making the same face with her mouth open. | pred zrkadlom | catch | catch |  |
| 11 | 2I | A:1212:s | B1 | S | wrong | TIP | Zajtra o takomto čase bude robiť pred zrkadlom tú istú grimasu s otvorenými ústami. | This time tomorrow, she will be make the same face in front of the mirror with her mouth open. | robiť | - | catch |  |
| 12 | 2I | A:1214:m | B1 | M | wrong | TIP | Povedal, že tréning bol najtvrdší v celom jeho živote! Čistá agónia! | He said that the training had been the hardest! Pure agony! | v celom jeho živote | - | catch |  |
| 13 | 2I | A:1330:c5 | A1 | None | correct | TIP | Toto je najťažší slovník na svete! | This one is the heaviest dictionary in the world! | najťažší | - | COST |  |
| 14 | 2I | A:1348:m | A1 | M | wrong | TIP | Čo stavajú? Drevenú kôlňu. | What are they building? A shed. | drevenú | - | catch |  |
| 15 | 2I | A:1371:m | A2 | M | wrong | TIP | Na tejto pláži je veľa jemného piesku | There is a lot of sand on this beach. | jemného | - | catch |  |
| 16 | 2I | A:1397:m | B2 | M | wrong | SAME | Celé námestie kričí po hudbe, ktorú táto kapela hrá! | The square is screaming for the music this band plays! | celé | catch | catch | yes |
| 17 | 2I | A:1398:m | A1 | M | wrong | TIP | Dvaja kamaráti čakajú pod starou strechou v dedine. | Two friends are waiting under a roof in the village. | starou | - | catch |  |
| 18 | 2I | A:1402:c4 | A1 | None | correct | TIP | Strieborná retiazka leží v drevenej škatuli. | The silver chain is in the wooden box. | leží | - | COST |  |
| 19 | 2I | A:1402:m | A1 | M | wrong | TIP | Strieborná retiazka leží v drevenej škatuli. | A silver chain lies in a box. | drevenej | - | catch |  |
| 20 | 2I | A:1446:c4 | A2 | None | correct | TIP | Už teraz som ohúrený: budúci týždeň sa chystáš držať modrého páva znova. | Even now I'm amazed: next week you're holding the blue peacock again. | chystáš | - | COST |  |
| 21 | 2I | A:1446:m | A2 | M | wrong | TIP | Už teraz som ohúrený: budúci týždeň sa chystáš držať modrého páva znova. | I'm already amazed: next week you're going to hold the peacock again. | modrého | - | catch |  |
| 22 | 2I | A:1447:m | B1 | M | wrong | TIP | Môj spolubývajúci prehral v kameň-papier-nožnice, tak vyniesol smeti! Absolútna zrada! | My roommate lost, so he took out the trash! Absolute betrayal! | kameň-papier-nožnice | - | catch |  |
| 23 | 2I | A:148:s | B1 | S | wrong | TIP | Keby sa sprievod pohyboval ešte rýchlejšie, tanečníci by predbehli ženu v zelenom. | If the parade moved even faster, the dancers would overtook the woman in green. | predbehli | - | catch |  |
| 24 | 2I | A:1577:m | B2 | M | wrong | SAME | Na poludnie ona už bude chodiť po šatníku v župane dve hodiny. | By noon she will have been walking around the wardrobe for two hours. | župane | catch | catch | yes |
| 25 | 2I | A:1577:s | B2 | S | wrong | TIP | Na poludnie ona už bude chodiť po šatníku v župane dve hodiny. | By noon she will have been walk around the wardrobe in her bathrobe for two hours. | chodiť | - | catch |  |
| 26 | 2I | A:1611:w | B1 | W | wrong | TIP | Dosiahla vankúše, otočila sa a padla na ne. Bezchybné pristátie. | She reached the blankets, turned around and fell onto them. A flawless landing. | vankúše | - | catch |  |
| 27 | 2I | A:1702:m | B1 | M | wrong | SAME | Počuj, vraj už spálila štyri marshmallowy a pálenie ju baví. | Listen, apparently she has already burned four and she enjoys burning them. | marshmallowy | catch | catch | yes |
| 28 | 2I | A:1727:t | A1 | T | wrong | TIP | Úplne neuveriteľné! Jej cestovanie zahŕňa tri druhy dopravy! | Absolutely incredible! Her travel included three kinds of transport! | zahŕňa | - | catch |  |
| 29 | 2I | A:1806:m | B1 | M | wrong | SAME | Keď sa bábätko usmieva takto, každý si myslí, že je rozkošné. | When it smiles like this, everyone thinks it's adorable. | bábätko | catch | catch | yes |
| 30 | 2I | A:1806:s | B1 | S | wrong | TIP | Keď sa bábätko usmieva takto, každý si myslí, že je rozkošné. | When the baby smile like this, everyone thinks it's adorable. | usmieva | - | catch |  |
| 31 | 2I | A:1858:m | B2 | M | wrong | TIP | Priala by si, aby jej mačka tiež nosila takúto loptu. | She wishes her cat would carry a ball too. | takúto | - | catch |  |
| 32 | 2I | A:1919:m | B2 | M | wrong | TIP | Zriedka si hostia užili takú vrelú pohostinnosť pri jednom samovare. | Rarely have guests enjoyed such hospitality at a single samovar. | vrelú | - | catch |  |
| 33 | 2I | A:1951:m | A2 | M | wrong | TIP | Ak dnes v noci nasneží, oblečiem si tento kabát znova. | If it snows, I'll put this coat on again. | v noci | - | catch |  |
| 34 | 2I | A:2035:m | A1 | M | wrong | TIP | Čo kupuje? Zrelé červené paradajky. | What is she buying? Red tomatoes. | zrelé | - | catch |  |
| 35 | 2I | A:2040:m | A1 | M | wrong | TIP | Táto brada je desať rokov práce! | This beard is years of work! | desať | - | catch |  |
| 36 | 2I | A:2050:m | B1 | M | wrong | SAME | Nabudúce ona dá silnejší úder päsťou, lebo sa bude viac snažiť. | Next time she will throw a punch because she will try harder. | silnejší | catch | catch | yes |
| 37 | 2I | A:219:m | A1 | M | wrong | TIP | Dom má v záhrade dve metly. | The house has two brooms. | v záhrade | - | catch |  |
| 38 | 2I | A:2354:m | A1 | M | wrong | TIP | Pozri sa na tieto zablatené čižmy na chodníku! | Look at these boots on the pavement! | zablatené | - | catch |  |
| 39 | 2I | A:2354:s | A1 | S | wrong | TIP | Pozri sa na tieto zablatené čižmy na chodníku! | Look at this muddy boots on the pavement! | tieto | - | catch |  |
| 40 | 2I | A:2356:m | B1 | M | wrong | TIP | Kým si prezerali modré mestečko, somár zablokoval uličku. Mierne neplánovaná zastávka. | While they were looking around the town, a donkey blocked the alley. A slightly unplanned stop. | modré | - | catch |  |
| 41 | 2I | A:2402:m | B1 | M | wrong | SAME | Hádaj čo, chalan, ktorého zviera skočilo z toho útesu, sa vraj ani nebál. | Guess what, the guy whose animal jumped apparently wasn't even scared. | útesu | catch | catch | yes |
| 42 | 2I | A:2456:c4 | A2 | None | correct | TIP | Majú plán. Zajtra sa chystajú pokosiť trávu znova. | They have a plan: they're mowing the grass again tomorrow. | chystajú | - | COST |  |
| 43 | 2I | A:2456:m | A2 | M | wrong | TIP | Majú plán. Zajtra sa chystajú pokosiť trávu znova. | They have a plan. Tomorrow they're going to mow again. | trávu | - | catch |  |
| 44 | 2I | A:2463:m | B2 | M | wrong | SAME | Do Vianoc si z toho bábikovského svetra bude uťahovať už mesiace. | By Christmas he will have been making fun of that sweater for months. | bábikovského | catch | catch | yes |
| 45 | 2I | A:2463:s | B2 | S | wrong | TIP | Do Vianoc si z toho bábikovského svetra bude uťahovať už mesiace. | By Christmas he will have been making fun of that doll sweater since months. | uťahovať | - | catch |  |
| 46 | 2I | A:2463:w | B2 | W | wrong | TIP | Do Vianoc si z toho bábikovského svetra bude uťahovať už mesiace. | By Christmas he will have been making fun of that doll sweater for weeks. | mesiacov | - | catch |  |
| 47 | 2I | A:2486:m | B1 | M | wrong | TIP | Kým jeden príbuzný niesol tortu cez dvere, ostatní prichádzali po chodníku. | While one relative was carrying the cake, the others were coming along the path. | cez dvere | - | catch |  |
| 48 | 2I | A:2495:m | A1 | M | wrong | TIP | Nočná mora! Mačka má príliš veľa práce, aj v posteli! | Nightmare! The cat has too much work! | v posteli | - | catch |  |
| 49 | 2I | A:2502:s | B1 | S | wrong | TIP | Ona samozrejme nakukla do učebnice raz a potom postavila stenu z kníh. | Of course she peeked into the textbook once and then build a wall of books. | postavila | - | catch |  |
| 50 | 2I | A:250:m | B1 | M | wrong | TIP | Vozidlo uháňalo po vidieckej ceste predtým, než bolo zaparkované pri dunách, ako bolo pozorované. | The vehicle had been racing along the road before it was parked by the dunes, as was observed. | vidieckej | - | catch |  |
| 51 | 2I | A:262:m | B1 | M | wrong | SAME | Zdravotník povedal, že film bol poslaný z laboratória hodinu predtým. | The paramedic said that the film had been sent an hour before. | laboratória | catch | catch | yes |
| 52 | 2I | A:262:s | B1 | S | wrong | TIP | Zdravotník povedal, že film bol poslaný z laboratória hodinu predtým. | The paramedic said that the film had been send from the laboratory an hour before. | poslaný | - | catch |  |
| 53 | 2I | A:2714:m | A1 | M | wrong | TIP | Kam ona dáva jablko? Na sklenenú policu. | Where is she putting the apple? On the shelf. | sklenenú | - | catch |  |
| 54 | 2I | A:276:m | A2 | M | wrong | TIP | Paradajky rastú na rastlinách, tak on ich musí odtrhnúť z rastliny. | Tomatoes grow on plants, so he must pick them. | z rastliny | - | catch |  |
| 55 | 2I | A:2798:c1 | B1 | None | correct | SAME | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | This time tomorrow, the subject will be unlocking the same wooden door, as it usually does. | dvere | COST | COST |  |
| 56 | 2I | A:2798:c2 | B1 | None | correct | SAME | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | At this hour tomorrow the subject will be unlocking the same wooden door, as he usually does. | dvere | COST | COST |  |
| 57 | 2I | A:2798:c3 | B1 | None | correct | SAME | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | Tomorrow at this time, the subject will be unlocking that same wooden door, just as they usually do. | dvere | COST | COST |  |
| 58 | 2I | A:2798:c4 | B1 | None | correct | SAME | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | At this time tomorrow the subject will unlock the same wooden door, as usual. | dvere | COST | COST |  |
| 59 | 2I | A:2798:c5 | B1 | None | correct | SAME | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | This time tomorrow the subject will be unlocking the same wooden door like it normally does. | dvere | COST | COST |  |
| 60 | 2I | A:2798:m | B1 | M | wrong | TIP | Zajtra o tejto hodine subjekt bude odomykať tie isté drevené dvere, ako to zvyčajne robí. | This time tomorrow, the subject will be unlocking the same door, as it usually does. | drevené | - | catch |  |
| 61 | 2I | A:284:m | A1 | M | wrong | TIP | Voda vo fľaši je veľmi studená. | The water is very cold. | fľaši | - | catch |  |
| 62 | 2I | A:2916:c3 | A1 | None | correct | TIP | Čo je rozpočet? Dve kvapky séra na lícach. | What is the budget? Two drops of serum on her cheeks. | lícach | - | COST |  |
| 63 | 2I | A:2916:s | A1 | S | wrong | TIP | Čo je rozpočet? Dve kvapky séra na lícach. | What is the budget? Two drop of serum on the cheeks. | kvapky | - | catch |  |
| 64 | 2I | A:2948:m | B2 | M | wrong | SAME | Dve červené nákladné lode priviezli svoj tovar do prístavu po mori. | Two cargo ships brought their goods to the port by sea. | červené | catch | catch | yes |
| 65 | 2I | A:2948:s | B2 | S | wrong | TIP | Dve červené nákladné lode priviezli svoj tovar do prístavu po mori. | Two red cargo ship brought their goods to the port by sea. | lode | - | catch |  |
| 66 | 2I | A:2960:m | B2 | M | wrong | TIP | Do budúceho týždňa klíčok, v ktorý dúfala, vyrastie na malú rastlinku. | By next week the sprout she was hoping for will grow into a plant. | malú | - | catch |  |
| 67 | 2I | A:2989:m | B2 | M | wrong | SAME | Samozrejme si dala trasu nakresliť na mapu, pre prípad, že by zabudla vlastný plán. | Of course she had the route drawn in case she forgot her own plan. | na mapu | catch | catch | yes |
| 68 | 2I | A:2989:s | B2 | S | wrong | TIP | Samozrejme si dala trasu nakresliť na mapu, pre prípad, že by zabudla vlastný plán. | Of course she had the route draw on the map in case she forgot her own plan. | nakresliť | - | catch |  |
| 69 | 2I | A:2989:t | B2 | T | wrong | TIP | Samozrejme si dala trasu nakresliť na mapu, pre prípad, že by zabudla vlastný plán. | Of course she has the route drawn on the map in case she forgets her own plan. | nakresliť | - | catch |  |
| 70 | 2I | A:2989:w | B2 | W | wrong | TIP | Samozrejme si dala trasu nakresliť na mapu, pre prípad, že by zabudla vlastný plán. | Of course she had the route drawn on the map in case she lost her own plan. | zabudla | - | catch |  |
| 71 | 2I | A:299:m | B2 | M | wrong | TIP | Roľník sa ďalej brodí vodou napriek dymu stúpajúcemu zo sopky. | The farmer keeps wading through the water despite the smoke rising. | sopky | - | catch |  |
| 72 | 2I | A:299:s | B2 | S | wrong | TIP | Roľník sa ďalej brodí vodou napriek dymu stúpajúcemu zo sopky. | The farmer keep wading through the water despite the smoke rising from the volcano. | ďalej | - | catch |  |
| 73 | 2I | A:299:w | B2 | W | wrong | TIP | Roľník sa ďalej brodí vodou napriek dymu stúpajúcemu zo sopky. | The farmer keeps wading through the water despite the ash rising from the volcano. | dymu | - | catch |  |
| 74 | 2I | A:3052:m | B2 | M | wrong | TIP | Vyliezla na tú debnu naľavo. | She climbed onto that crate. | naľavo | - | catch |  |
| 75 | 2I | A:3052:s | B2 | S | wrong | TIP | Vyliezla na tú debnu naľavo. | She climbed onto crate on the left. | tú | - | catch |  |
| 76 | 2I | A:3060:m | A1 | M | wrong | TIP | Ona môže trénovať golf celú noc! Muž je úplne v šoku! | She can practise all night! The man is completely shocked! | golf | - | catch |  |
| 77 | 2I | A:3096:c5 | B1 | None | correct | TIP | Ona zvykla hrať celé hodiny každú noc, kým sa nestala profesionálnou hráčkou! Úplne posadnutá! | She played for hours every night until she became a professional player! Completely obsessed! | zvykla | - | COST |  |
| 78 | 2I | A:3096:m | B1 | M | wrong | SAME | Ona zvykla hrať celé hodiny každú noc, kým sa nestala profesionálnou hráčkou! Úplne posadnutá! | She used to play every night until she became a professional player! Totally obsessed! | celé hodiny | catch | catch | yes |
| 79 | 2I | A:3146:c2 | A2 | None | correct | TIP | Jej skok je vyšší ako ktorýkoľvek skok dňa. | Her jump is higher than any other jump today. | dňa | - | COST |  |
| 80 | 2I | A:3285:m | B1 | M | wrong | TIP | Veža zo stoličiek sa kýve, takže liezť na ňu musí byť veľmi riskantné. | The tower is wobbling, so climbing it must be very risky. | zo stoličiek | - | catch |  |
| 81 | 2I | A:3363:m | A1 | M | wrong | TIP | Na dnešný večer majú jednu fľašu červeného vína. | They have one bottle of wine for tonight. | červeného | - | catch |  |
| 82 | 2I | A:3400:m | B2 | M | wrong | TIP | Žena pritiahla ich pozornosť práve vo chvíli, keď zdvíhali televízor z dodávky. | The woman caught their attention just as they were lifting the TV. | dodávky | - | catch |  |
| 83 | 2I | A:3489:w | A2 | W | wrong | TIP | Nikto by nemal teraz siahať na jeho karty, inak je všetko zničené! | Nobody should touch her cards now, otherwise everything is ruined! | jeho | - | catch |  |
| 84 | 2I | A:3519:m | A2 | M | wrong | TIP | Má plán. Budúci rok sa chystá napísať nový prejav. | She has a plan. Next year she's going to write a speech. | nový | - | catch |  |
| 85 | 2I | A:3545:m | A2 | M | wrong | TIP | Dnes si vlasy češe, ale včera na to zabudol. | Today he's combing, but yesterday he forgot to. | vlasy | - | catch |  |
| 86 | 2I | A:3545:s | A2 | S | wrong | TIP | Dnes si vlasy češe, ale včera na to zabudol. | Today he's combing him hair, but yesterday he forgot to. | vlasy | - | catch |  |
| 87 | 2I | A:3583:m | B2 | M | wrong | TIP | Katastrofa! Moji kamaráti vykopali obrovskú jamu a teraz som úplne zaseknutý! | Disaster! My friends have dug a hole and now I'm completely stuck! | obrovskú | - | catch |  |
| 88 | 2I | A:359:m | B1 | M | wrong | TIP | Kým dorazili k východu, oči jazdca si už zvykli na tmu. | By the time they reached the exit, the eyes had already got used to the darkness. | jazdca | - | catch |  |
| 89 | 2I | A:3631:m | A1 | M | wrong | SAME | Každý môže sledovať tanec z balkónov. | The dance can be watched from the balconies. | Každý | catch | catch | yes |
| 90 | 2I | A:3672:m | A2 | M | wrong | TIP | Pijú horúci čaj, aby sa zohriali a cítili v bezpečí. | They drink tea to warm up and feel safe. | horúci | - | catch |  |
| 91 | 2I | A:3709:m | A2 | M | wrong | TIP | Zloží si slúchadlá. Ide odísť zo štúdia. | She takes off her headphones. She's going to leave. | štúdia | - | catch |  |
| 92 | 2I | A:3783:c3 | B1 | None | correct | SAME | Keď pred zápasom hrá hymna, hráčky si dajú ruky na hruď. | Whenever the anthem plays before a match, the players put a hand on their chest. | ruky | COST | COST |  |
| 93 | 2I | A:3783:m | B1 | M | wrong | TIP | Keď pred zápasom hrá hymna, hráčky si dajú ruky na hruď. | When the anthem plays, the players put their hands on their chests. | pred zápasom | - | catch |  |
| 94 | 2I | A:3797:m | A2 | M | wrong | SAME | Hej, v miestnosti bola nuda, ale teraz je to dosť živé. | Hey, it was boring, but now it's quite lively. | miestnosti | catch | catch |  |
| 95 | 2I | A:3856:m | B1 | M | wrong | TIP | Ona zložila prísahu a všetko v tejto krajine sa navždy zmení! | She has taken the oath and everything will change forever! | v tejto krajine | - | catch |  |
| 96 | 2I | A:3899:c1 | B2 | None | correct | SAME | Keď vošla na trh, netušila, že odíde von s dvoma metrami zlatej potlače. | When she entered the market, she had no idea that she would leave with two metres of gold print. | von | COST | COST |  |
| 97 | 2I | A:3899:c3 | B2 | None | correct | SAME | Keď vošla na trh, netušila, že odíde von s dvoma metrami zlatej potlače. | As she went into the market, she had no idea she was going to leave with two metres of gold print. | von | COST | COST |  |
| 98 | 2I | A:3899:s | B2 | S | wrong | TIP | Keď vošla na trh, netušila, že odíde von s dvoma metrami zlatej potlače. | When she entered to the market, she had no idea she would leave with two metres of gold print. | von | - | catch |  |
| 99 | 2I | A:3934:m | B2 | M | wrong | SAME | Červený lampión svietil pri okne celé hodiny, kým sa rozsvietilo svetlo v kuchyni. | The lantern had been shining by the window for hours before the light in the kitchen came on. | Červený | catch | catch | yes |
| 100 | 2I | A:3957:m | A1 | M | wrong | TIP | Tak trochu pôsobivé, ty umývaš surové kura ako skutočný šéfkuchár. | Kind of impressive, you wash the chicken like a real chef. | surové | - | catch |  |
| 101 | 2I | A:462:c3 | A2 | None | correct | SAME | Ty bojuješ s tou alergiou lepšie než ktokoľvek na tejto lúke. Ikonické. | You deal with that allergy better than anyone on this meadow. Iconic. | bojuješ | COST | COST |  |
| 102 | 2I | A:462:c5 | A2 | None | correct | SAME | Ty bojuješ s tou alergiou lepšie než ktokoľvek na tejto lúke. Ikonické. | You cope with the allergy better than anybody in this meadow. Iconic. | bojuješ | COST | COST |  |
| 103 | 2I | A:462:s | A2 | S | wrong | TIP | Ty bojuješ s tou alergiou lepšie než ktokoľvek na tejto lúke. Ikonické. | You fights that allergy better than anyone in this meadow. Iconic. | bojuješ | - | catch |  |
| 104 | 2I | A:540:s | A2 | S | wrong | TIP | Autá opravuje každý deň, ale teraz práve nakúka pod kapotu. | He repairs cars every day, but right now he peeking under the hood. | opravuje | - | catch |  |
| 105 | 2I | A:541:m | A1 | M | wrong | TIP | Rozpočet na strihanie: 20 eur. Kto platí, tučný ježko alebo mačka? | Haircut budget: 20 euros. Who pays, the hedgehog or the cat? | tučný | - | catch |  |
| 106 | 2I | A:541:s | A1 | S | wrong | TIP | Rozpočet na strihanie: 20 eur. Kto platí, tučný ježko alebo mačka? | Haircut budget: 20 euros. Who pay, the fat hedgehog or the cat? | strihanie | - | catch |  |
| 107 | 2I | A:587:m | A1 | M | wrong | TIP | Tancovanie v kuchyni je jeden skvelý nápad. | Dancing is a great idea. | v kuchyni | - | catch |  |
| 108 | 2I | A:587:s | A1 | S | wrong | TIP | Tancovanie v kuchyni je jeden skvelý nápad. | Dancing in the kitchen is great idea. | jeden | - | catch |  |
| 109 | 2I | A:59:w | A2 | W | wrong | TIP | Pred hodinou vlny zničili jeho vysoký hrad z piesku. | An hour ago the waves destroyed her tall sandcastle. | jeho | - | catch |  |
| 110 | 2I | A:65:m | B2 | M | wrong | TIP | Kvôli mrazivej zime jej dal svoju bundu skôr, než sa lunapark zmenil na totálnu katastrofu! | Because of the winter, he gave her his jacket before the funfair turned into a total disaster! | mrazivej | - | catch |  |
| 111 | 2I | A:700:m | A2 | M | wrong | TIP | Pred začiatkom musíš vypnúť prúd. | You must turn off the power. | začiatkom | - | catch |  |
| 112 | 2I | A:737:m | A2 | M | wrong | TIP | Kámo, nejako jej dochádzajú štipce. Na streche ostalo už len niekoľko štipcov. | Dude, she's somehow running out of clothespins. Only a few are left. | na streche | - | catch |  |
| 113 | 2I | A:842:c1 | B2 | None | correct | SAME | Smoothie mu skočilo rovno na nos, takže mal vrchnák vtedy zatlačiť silnejšie. | The smoothie splashed right onto his nose, so he should have pressed the lid harder then. | skočilo | COST | COST |  |
| 114 | 2I | A:842:c2 | B2 | None | correct | SAME | Smoothie mu skočilo rovno na nos, takže mal vrchnák vtedy zatlačiť silnejšie. | The smoothie jumped straight onto his nose, so he should have pushed the lid down harder at that time. | zatlačiť | COST | COST |  |
| 115 | 2I | A:842:c4 | B2 | None | correct | SAME | Smoothie mu skočilo rovno na nos, takže mal vrchnák vtedy zatlačiť silnejšie. | The smoothie flew straight onto his nose, so he should've pressed the lid harder then. | skočilo | COST | COST |  |
| 116 | 2I | A:842:m | B2 | M | wrong | TIP | Smoothie mu skočilo rovno na nos, takže mal vrchnák vtedy zatlačiť silnejšie. | The smoothie jumped right onto his nose, so he should have pressed harder then. | vrchnák | - | catch |  |
| 117 | 2I | A:842:s | B2 | S | wrong | TIP | Smoothie mu skočilo rovno na nos, takže mal vrchnák vtedy zatlačiť silnejšie. | The smoothie jumped right onto his nose, so he should have press the lid harder then. | zatlačiť | - | catch |  |
| 118 | 2J | A:1030:m | A2 | M | wrong | TIP | Orechy je každú jeseň, ale vlani nezjedol ani jeden. | He eats nuts, but last year he didn't eat a single one. | každú jeseň | - | catch |  |
| 119 | 2J | A:1033:s | A2 | S | wrong | TIP | Publikum to miluje, tak divadlo budúci týždeň uvedie tú hru znova. | The audience love it, so the theatre will stages the play again next week. | uvedie | - | catch |  |
| 120 | 2J | A:1244:m | A2 | M | wrong | TIP | Uprostred série by si nemal prestať. | You shouldn't stop in the middle. | série | - | catch |  |
| 121 | 2J | A:128:m | A2 | M | wrong | TIP | Ak chceš čerstvý vzduch, mal by si sa prejsť v parku. | If you want air, you should take a walk in the park. | čerstvý | - | catch |  |
| 122 | 2J | A:1385:m | A2 | M | wrong | TIP | Ona zvyčajne griluje ryby, ale včera večer grilovala hovädzie mäso. | She usually grills fish, but she grilled beef. | večer | - | catch |  |
| 123 | 2J | A:1413:m | B2 | M | wrong | SAME | Škrečok, ktorého preukaz otvára dvere kancelárie, odchádza o piatej. | The hamster whose pass opens the door leaves at five. | kancelárie | catch | catch |  |
| 124 | 2J | A:1452:m | A2 | M | wrong | TIP | On dvíha svoj cylinder. Je zdvorilejší než ostatní muži v parku. | He raises his top hat. He is more polite than the other men. | v parku | - | catch |  |
| 125 | 2J | A:145:s | A2 | S | wrong | TIP | Skutočný profesionál, samozrejme: zubár potrebuje veľmi málo času na jej zuby. | A real professional, of course: the dentist needs very few time for her teeth. | málo | - | catch |  |
| 126 | 2J | A:1568:m | A2 | M | wrong | SAME | Tam je voľné miesto! — Super, zaparkujem tam. | There's a space! — Great, I'll park there. | voľné | catch | catch | yes |
| 127 | 2J | A:1599:s | B2 | S | wrong | TIP | Do západu slnka zlyžuje celý svah. Očividne len malá ranná prechádzka. | By sunset he will have ski down the whole slope. Obviously just a little morning walk. | zlyžuje | - | catch |  |
| 128 | 2J | A:1689:m | A1 | M | wrong | TIP | Na posteli sedí to oranžové mačiatko. | The kitten is sitting on the bed. | oranžové | - | catch |  |
| 129 | 2J | A:1689:s | A1 | S | wrong | TIP | Na posteli sedí to oranžové mačiatko. | Orange kitten is sitting on bed. | to | - | catch |  |
| 130 | 2J | A:1720:c4 | B2 | None | correct | SAME | Keby mu sestry ráno barle nenastavili, bol by skončil na tvár pred celým oddelením. | If his crutches hadn't been adjusted by the nurses in the morning, he would have ended up on his face in front of the whole ward. | nastaviť | COST | COST |  |
| 131 | 2J | A:1757:m | B1 | M | wrong | TIP | Holič strihá tú obrovskú bradu už desať minút a podlaha je celá od chlpov. | The barber has been cutting that beard for ten minutes and the floor is covered in hair. | obrovskú | - | catch |  |
| 132 | 2J | A:1757:s | B1 | S | wrong | TIP | Holič strihá tú obrovskú bradu už desať minút a podlaha je celá od chlpov. | The barber has been cut that huge beard for ten minutes and the floor is covered in hair. | strihá | - | catch |  |
| 133 | 2J | A:1781:m | A2 | M | wrong | SAME | Farebná girlanda spadla, lebo lepiaca páska bola príliš slabá. Úplná katastrofa! | The garland fell down because the tape was too weak. A complete disaster! | farebná | catch | catch |  |
| 134 | 2J | A:180:m | A1 | M | wrong | TIP | Handričkou utrie jej veľké zelené listy. | She wipes its big leaves with a cloth. | zelené | - | catch |  |
| 135 | 2J | A:1849:c4 | B2 | None | correct | SAME | Nebudem klamať, ty si prehľadával svoju peňaženku celú večnosť, kým si sa uškrnul ako bohatý muž. | Not gonna lie, you'd been going through your wallet for ages before grinning like a wealthy man. | prehľadával | COST | COST |  |
| 136 | 2J | A:1849:s | B2 | S | wrong | TIP | Nebudem klamať, ty si prehľadával svoju peňaženku celú večnosť, kým si sa uškrnul ako bohatý muž. | I won't lie, you had been search through your wallet for ages before you grinned like a rich man. | prehľadával | - | catch |  |
| 137 | 2J | A:1849:w | B2 | W | wrong | TIP | Nebudem klamať, ty si prehľadával svoju peňaženku celú večnosť, kým si sa uškrnul ako bohatý muž. | I won't lie, you had been searching through your bag for ages before you grinned like a rich man. | peňaženku | - | catch |  |
| 138 | 2J | A:1918:m | B2 | M | wrong | SAME | Úradník sa jej spýtal, či má pri sebe preukaz totožnosti. | She was asked whether she had her ID card with her. | úradník | catch | catch | yes |
| 139 | 2J | A:1918:t | B2 | T | wrong | TIP | Úradník sa jej spýtal, či má pri sebe preukaz totožnosti. | The clerk asks her whether she has her ID card with her. | spýtal | - | catch |  |
| 140 | 2J | A:1918:w | B2 | W | wrong | TIP | Úradník sa jej spýtal, či má pri sebe preukaz totožnosti. | The clerk asked her whether she had her passport with her. | preukaz totožnosti | - | catch |  |
| 141 | 2J | A:1939:c4 | A1 | None | correct | SAME | Stojíš naraz v štyroch farbách. Klobúk dole. | You're wearing four colours at once. Hats off. | Stojíš | COST | COST |  |
| 142 | 2J | A:2069:c3 | A2 | None | correct | SAME | Pouličný hudobník spieva nejaké piesne a dav počúva. | The busker sings a few songs and the crowd listens. | nejaké | COST | COST |  |
| 143 | 2J | A:2069:m | A2 | M | wrong | TIP | Pouličný hudobník spieva nejaké piesne a dav počúva. | The musician sings some songs and the crowd listens. | pouličný | - | catch |  |
| 144 | 2J | A:2069:s | A2 | S | wrong | TIP | Pouličný hudobník spieva nejaké piesne a dav počúva. | The street musician sings some song and the crowd listens. | piesne | - | catch |  |
| 145 | 2J | A:2121:m | B2 | M | wrong | TIP | Ten rozťahovací stôl je vraj najlepšia vec, akú kedy kúpil do bytu. | That table is supposedly the best thing he has ever bought for the flat. | rozťahovací | - | catch |  |
| 146 | 2J | A:2123:s | A2 | S | wrong | TIP | Fakt, učiteľka, máš toľko práce a stále ideš ďalej. | Really, teacher, you have so many works and you still keep going. | práce | - | catch |  |
| 147 | 2J | A:2126:m | A1 | M | wrong | TIP | Nočná mora! Táto bronzová socha má obrovskú bradu! | Nightmare! This statue has a huge beard! | bronzová | - | catch |  |
| 148 | 2J | A:2126:s | A1 | S | wrong | TIP | Nočná mora! Táto bronzová socha má obrovskú bradu! | Nightmare! This bronze statue have got huge beard! | bradu | - | catch |  |
| 149 | 2J | A:2152:c3 | B1 | None | correct | SAME | Jeho stará mama mávala svoje poháre v tejto kuchynskej skrinke. | His grandmother would keep her glasses in this kitchen cabinet. | poháre | COST | COST |  |
| 150 | 2J | A:2152:c5 | B1 | None | correct | SAME | Jeho stará mama mávala svoje poháre v tejto kuchynskej skrinke. | His grandmother used to keep her glasses here in this kitchen cabinet. | poháre | COST | COST |  |
| 151 | 2J | A:2152:m | B1 | M | wrong | SAME | Jeho stará mama mávala svoje poháre v tejto kuchynskej skrinke. | His grandmother used to keep her glasses in this cabinet. | kuchynskej | catch | catch | yes |
| 152 | 2J | A:2152:s | B1 | S | wrong | TIP | Jeho stará mama mávala svoje poháre v tejto kuchynskej skrinke. | His grandmother used to keeping her glasses in this kitchen cabinet. | poháre | - | catch |  |
| 153 | 2J | A:2237:m | B1 | M | wrong | TIP | Kým pútnik kráčal po kľukatom chodníku, vtáky krúžili nad jazerom. | While the pilgrim was walking along the path, birds were circling over the lake. | kľukatom | - | catch |  |
| 154 | 2J | A:225:m | A2 | M | wrong | TIP | Skvelý pacient. Koleno ho bolelo, ale teraz robí drepy ako profík. | A great patient. His knee hurt, but now he does squats. | profík | - | catch |  |
| 155 | 2J | A:22:c1 | B2 | None | correct | SAME | Keby administratíva prestala skôr, ona by sa nezvalila na stôl. | If the paperwork had stopped earlier, she wouldn't have collapsed onto the desk. | administratíva | COST | COST |  |
| 156 | 2J | A:22:c2 | B2 | None | correct | SAME | Keby administratíva prestala skôr, ona by sa nezvalila na stôl. | If the admin work had ended sooner, she would not have slumped onto the table. | administratíva | COST | COST |  |
| 157 | 2J | A:22:c5 | B2 | None | correct | SAME | Keby administratíva prestala skôr, ona by sa nezvalila na stôl. | If the paperwork had finished earlier, she wouldn't have slumped down on the desk. | administratíva | COST | COST |  |
| 158 | 2J | A:2315:m | A1 | M | wrong | TIP | Táto zubárka v tyrkysovom oblečení sa pozerá na jeho zuby. | This dentist is looking at his teeth. | v tyrkysovom oblečení | - | catch |  |
| 159 | 2J | A:2358:c4 | B1 | None | correct | TIP | Had je skutočná hrozba a uhryzne každého, kto príde bližšie. | This snake is a true threat and will bite whoever comes closer. | Had | - | COST |  |
| 160 | 2J | A:2358:m | B1 | M | wrong | SAME | Had je skutočná hrozba a uhryzne každého, kto príde bližšie. | The snake is a threat and will bite anyone who comes closer. | skutočná | catch | catch | yes |
| 161 | 2J | A:2359:c4 | A1 | None | correct | SAME | Vodu napúšťa do bieleho drezu. | He lets water into the white sink. | napúšťa | COST | COST |  |
| 162 | 2J | A:2389:m | A1 | M | wrong | TIP | Polievková lyžica je väčšia než tá malá čajová. | The tablespoon is bigger than the small one. | čajová | - | catch |  |
| 163 | 2J | A:2397:m | B2 | M | wrong | SAME | Povedala, že sa opláchne rýchlo, ale ostala pod sprchou desať minút. | She said she would rinse off, but she stayed in the shower for ten minutes. | rýchlo | catch | catch |  |
| 164 | 2J | A:2397:s | B2 | S | wrong | TIP | Povedala, že sa opláchne rýchlo, ale ostala pod sprchou desať minút. | She said she would rinse off quickly, but she stay in the shower for ten minutes. | opláchne | - | catch |  |
| 165 | 2J | A:242:m | A2 | M | wrong | TIP | Zvyčajne podáva tašky, ale teraz podáva zákazníkovi mincu. | He usually hands out bags, but now he is handing a coin. | zákazníkovi | - | catch |  |
| 166 | 2J | A:242:s | A2 | S | wrong | TIP | Zvyčajne podáva tašky, ale teraz podáva zákazníkovi mincu. | He usually hand out bags, but now he is handing the customer a coin. | podáva | - | catch |  |
| 167 | 2J | A:2487:m | B2 | M | wrong | SAME | Kámo, kým doniesli tortu, každý príbuzný sa už dvakrát objal, fakt. | Dude, by the time they brought the cake, every relative had already hugged, seriously. | dvakrát | catch | catch | yes |
| 168 | 2J | A:2494:m | A2 | M | wrong | TIP | Práve teraz sa mu hruď rýchlo dvíha | Right now his chest is rising. | rýchlo | - | catch |  |
| 169 | 2J | A:2562:m | A1 | M | wrong | TIP | Muž má na tvári veľa strniska. | The man has a lot of stubble. | tvári | - | catch |  |
| 170 | 2J | A:2724:s | B1 | S | wrong | TIP | Kámo, zajtra v tomto čase sa bude vrhať do mora za každou loptou, bez kecov. | Dude, this time tomorrow he'll be dive into the sea after every ball, no kidding. | vrhať | - | catch |  |
| 171 | 2J | A:2787:m | A1 | M | wrong | TIP | Kto sedí na kráľovskom tróne? Kráľ. | Who sits on the throne? The king. | kráľovskom | - | catch |  |
| 172 | 2J | A:2811:m | A2 | M | wrong | TIP | Ty sa usmievaš tak šťastne na rýchlom bicykli. Ikonické. | You smile so happily on the bike. Iconic. | rýchlom | - | catch |  |
| 173 | 2J | A:2825:m | B1 | M | wrong | SAME | Kedysi tu býval študentom, ale teraz sa mu trieda klania. | He used to be a student, but now the class bows to him. | tu | catch | catch | yes |
| 174 | 2J | A:2829:c5 | A1 | None | correct | SAME | Prečo je piesok teplý? Lebo svieti slnko. | Why is the sand warm? The sun is shining. | Lebo | COST | COST |  |
| 175 | 2J | A:282:t | A1 | T | wrong | TIP | Čo spáli na panvici? | What did he burn in the pan? | spáli | - | catch |  |
| 176 | 2J | A:3026:m | A1 | M | wrong | TIP | Zhora môžeš vidieť celú dedinu. | From the top you can see the village. | celú | - | catch |  |
| 177 | 2J | A:3026:t | A1 | T | wrong | TIP | Zhora môžeš vidieť celú dedinu. | From the top you could see the whole village. | môžeš | - | catch |  |
| 178 | 2J | A:3144:c4 | A1 | None | correct | SAME | Toto kopnutie vyhadzuje lístie do vzduchu. | This kick is throwing leaves into the air. | kopnutie | COST | COST |  |
| 179 | 2J | A:3147:m | A1 | M | wrong | TIP | Rozpočtové upozornenie: luxusný kočík je za 5000 eur. | Budget alert: the pram is 5000 euros. | luxusný | - | catch |  |
| 180 | 2J | A:315:m | A1 | M | correct | TIP | Rozvinúť ho im trvá päť minút. | It takes five minutes to unroll it. | im | - | COST |  |
| 181 | 2J | A:3207:m | A1 | M | wrong | TIP | Táto nahnevaná žena drží svoje mokré oblečenie. | This woman is holding her wet clothes. | nahnevaná | - | catch |  |
| 182 | 2J | A:3218:m | A1 | M | wrong | TIP | Ľadová stena je zamrznutá a tvrdá. | The wall is frozen and hard. | Ľadová | - | catch |  |
| 183 | 2J | A:3390:m | B1 | M | wrong | TIP | Práve si šnuroval topánky, keď slnko dopadlo na strechu chaty. | You were just lacing your shoes when the sun hit the roof. | chaty | - | catch |  |
| 184 | 2J | A:3396:m | B1 | M | wrong | TIP | Chce podať ruku svojmu kolegovi, lebo na podanie ruky treba dvoch ľudí. | He wants to shake hands, because it takes two people to shake hands. | kolegovi | - | catch |  |
| 185 | 2J | A:3396:s | B1 | S | wrong | TIP | Chce podať ruku svojmu kolegovi, lebo na podanie ruky treba dvoch ľudí. | He wants shaking hands with his colleague, because it takes two people to shake hands. | podať | - | catch |  |
| 186 | 2J | A:3405:m | A1 | M | wrong | TIP | Stoj! Tá drevená varecha je úplne plná omáčky! | Stop! That spoon is completely full of sauce! | drevená | - | catch |  |
| 187 | 2J | A:3405:w | A1 | W | wrong | TIP | Stoj! Tá drevená varecha je úplne plná omáčky! | Stop! That wooden spoon is completely full of soup! | omáčky | - | catch |  |
| 188 | 2J | A:3412:c4 | B2 | None | correct | SAME | Takže, do budúceho týždňa vraj vyrozprávajú príbeh o útoku býka všetkým. | So, by next week the story of the bull attack will apparently have been told to everyone. | vyrozprávajú | COST | COST |  |
| 189 | 2J | A:3412:m | B2 | M | wrong | SAME | Takže, do budúceho týždňa vraj vyrozprávajú príbeh o útoku býka všetkým. | So, by next week they will supposedly have told the story about the attack to everyone. | býka | catch | catch |  |
| 190 | 2J | A:3434:m | B1 | M | wrong | SAME | Kamarátka, ktorá jej zatlačila chodidlo dozadu, mala ten istý kŕč už stokrát. | The friend who pushed her foot back has had the cramp a hundred times already. | mala | catch | catch |  |
| 191 | 2J | A:3469:m | A2 | M | wrong | TIP | Ak je toto miesto voľné, sadnem si sem tiež. | If this seat is free, I'll sit here. | tiež | - | catch |  |
| 192 | 2J | A:3513:m | B2 | M | wrong | TIP | Naliala vodu z džbánu so zahnutým uchom do krhly. | She poured water from the jug into the watering can. | zahnutým uchom | - | catch |  |
| 193 | 2J | A:3523:m | B1 | M | wrong | TIP | Kamera bola pokrytá červenou hlinou, keď motorka pristála. Je úplne zničená! | The camera was covered with clay when the motorbike landed. It's completely destroyed! | červenou | - | catch |  |
| 194 | 2J | A:3523:w | B1 | W | wrong | TIP | Kamera bola pokrytá červenou hlinou, keď motorka pristála. Je úplne zničená! | The camera was covered with red sand when the motorbike landed. It's completely destroyed! | hlina | - | catch |  |
| 195 | 2J | A:3602:m | B1 | M | wrong | TIP | Zháňal zásuvku, keď zrazu ukázala na stenu za monsterou. | He was looking for a socket when she suddenly pointed at the wall. | monsterou | - | catch |  |
| 196 | 2J | A:3624:s | B2 | S | wrong | TIP | Celé mesiace si prezerali byty, kým tento konečne ukončil nočnú moru! | They had been look at flats for months before this one finally ended the nightmare! | prezerali | - | catch |  |
| 197 | 2J | A:3624:w | B2 | W | wrong | TIP | Celé mesiace si prezerali byty, kým tento konečne ukončil nočnú moru! | They had been looking at flats for weeks before this one finally ended the nightmare! | mesiace | - | catch |  |
| 198 | 2J | A:362:c4 | A2 | None | correct | SAME | On používa toľko zelenej farby na stenu. | He puts so much green paint on the wall. | používa | COST | COST |  |
| 199 | 2J | A:362:m | A2 | M | wrong | TIP | On používa toľko zelenej farby na stenu. | He uses so much paint on the wall. | zelenej | - | catch |  |
| 200 | 2J | A:365:c3 | B1 | None | correct | SAME | Ak cena pôjde ešte vyššie, položí tabuľku. | If the price rises even higher, she will lower her paddle. | položí | COST | COST |  |
| 201 | 2J | A:365:m | B1 | M | wrong | SAME | Ak cena pôjde ešte vyššie, položí tabuľku. | If the price goes even higher, she'll put it down. | tabuľku | catch | catch | yes |
| 202 | 2J | A:3759:m | B1 | M | wrong | TIP | Jej tréner si myslí, že budúci mesiac vyhrá športovú súťaž v surfovaní. | Her coach thinks she will win the competition next month. | športovú, v surfovaní | - | catch |  |
| 203 | 2J | A:3799:m | A2 | M | wrong | TIP | Pozri na tie nohy! Chystá sa skočiť veľmi vysoko. | Look at those legs! He's going to jump. | vysoko | - | catch |  |
| 204 | 2J | A:3961:m | B1 | M | wrong | TIP | Povedal si pastierovi, že jeho ovce blokujú tvoju dodávku. Úprimne, ikonická reflexná vesta. | You told the shepherd that his sheep were blocking your van. Honestly, iconic vest. | reflexná | - | catch |  |
| 205 | 2J | A:3963:m | B2 | M | wrong | SAME | Strany sprievodcu si pred cestou dali zalaminovať. | They had the pages laminated before the trip. | sprievodcu | catch | catch | yes |
| 206 | 2J | A:3970:m | B2 | M | wrong | SAME | Počuj, vraj z toho veľkého hrnca vyráža para zakaždým, keď zdvihne pokrievku. | Listen, apparently steam bursts out of that pot every time he lifts the lid. | veľkého | catch | catch | yes |
| 207 | 2J | A:3970:t | B2 | T | wrong | SAME | Počuj, vraj z toho veľkého hrnca vyráža para zakaždým, keď zdvihne pokrievku. | Listen, apparently steam burst out of that big pot every time he lifted the lid. | vyráža | catch | catch |  |
| 208 | 2J | A:3970:w | B2 | W | wrong | TIP | Počuj, vraj z toho veľkého hrnca vyráža para zakaždým, keď zdvihne pokrievku. | Listen, apparently smoke bursts out of that big pot every time he lifts the lid. | para | - | catch |  |
| 209 | 2J | A:39:m | B2 | M | wrong | TIP | Teraz sa skrýva pod mnohými vrstvami a vidno mu len tvár. | Now he is hiding under layers and only his face is visible. | mnohými | - | catch |  |
| 210 | 2J | A:4010:c1 | A1 | None | correct | TIP | Sú to jedny úžasné červené letné šaty. | It's an amazing red summer dress. | jedny | - | COST |  |
| 211 | 2J | A:4010:c3 | A1 | None | correct | TIP | Sú to jedny úžasné červené letné šaty. | That's an amazing red summer dress. | jedny | - | COST |  |
| 212 | 2J | A:4010:c4 | A1 | None | correct | TIP | Sú to jedny úžasné červené letné šaty. | This is a wonderful red summer dress. | jedny | - | COST |  |
| 213 | 2J | A:4010:c5 | A1 | None | correct | TIP | Sú to jedny úžasné červené letné šaty. | It's an incredible red summer dress. | jedny | - | COST |  |
| 214 | 2J | A:4010:s | A1 | S | wrong | TIP | Sú to jedny úžasné červené letné šaty. | It is amazing red summer dress. | jedny | - | catch |  |
| 215 | 2J | A:40:m | A1 | M | wrong | SAME | Melón má štyridsať gumičiek, takže ich má štyridsať. | The melon has forty, so it has forty of them. | gumičiek | catch | catch | yes |
| 216 | 2J | A:497:m | A1 | M | wrong | SAME | Tieto miesta vzadu sú úplne prázdne! | These seats are completely empty! | vzadu | catch | catch | yes |
| 217 | 2J | A:54:s | B2 | S | wrong | TIP | Farmár by si prial, aby nebol veril chlapcovi, ktorý sa pred pádom dozadu takto škerí. | The farmer wish he hadn't trusted the boy who grins like this before falling backwards. | prial | - | catch |  |
| 218 | 2J | A:570:m | B1 | M | wrong | TIP | Ty si dodržiavala recept riadok po riadku, keď ťa kamera zachytila s úsmevom. Dosť ikonické. | You were following the recipe when the camera caught you smiling. Pretty iconic. | riadok po riadku | - | catch |  |
| 219 | 2J | A:592:m | B2 | M | wrong | SAME | Sviečky zapália, len čo posledné taniere budú na čerstvom obruse. | They will light the candles as soon as the plates are on the fresh tablecloth. | posledné | catch | catch | yes |
| 220 | 2J | A:833:c4 | B2 | None | correct | SAME | Nikdy predtým nebolo toľko ľudí okolo jedného novonarodeného bábätka. | Never before had so many people been around a single newborn. | bábätka | COST | COST |  |
| 221 | 2J | A:833:m | B2 | M | wrong | TIP | Nikdy predtým nebolo toľko ľudí okolo jedného novonarodeného bábätka. | Never before had there been so many people around one baby. | novonarodeného | - | catch |  |
| 222 | 2J | A:865:c3 | A2 | None | correct | SAME | Pravidlá tábora: každý sa musí zobudiť pred raňajkami. | The camp rules: everyone must get up before breakfast. | zobudiť | COST | COST |  |
| 223 | 2J | A:900:m | B2 | M | wrong | TIP | Pozri sa na ňu - práve hádže žetóny do vzduchu oboma rukami! | Look at her - she's throwing chips into the air right now! | oboma rukami | - | catch |  |
| 224 | 2J | A:900:s | B2 | S | wrong | TIP | Pozri sa na ňu - práve hádže žetóny do vzduchu oboma rukami! | Look at her - she throwing chips into the air with both hands right now! | hádže | - | catch |  |
| 225 | 2J | A:979:m | B1 | M | wrong | TIP | Odkedy uvidel prasklinu, nezjedol nič. | He hasn't eaten anything since he saw it. | prasklinu | - | catch |  |

## 2K's 35 added M false acceptances

| set | id | Slovak | answer | check |
|---|---|---|---|---|
| 2I | A:262:m | Zdravotník povedal, že film bol poslaný z laboratória hodinu predtým. | The paramedic said that the film had been sent an hour before. | MISSING: laboratória |
| 2I | A:1038:m | Kamarátka povedala, že náramok je príliš voľný, tak ho upravila. | My friend said that it was too loose, so she adjusted it. | MISSING: náramok |
| 2I | A:1099:m | Veľká huba rastie zo zeme. | A mushroom grows out of the ground. | MISSING: Veľká |
| 2I | A:1397:m | Celé námestie kričí po hudbe, ktorú táto kapela hrá! | The square is screaming for the music this band plays! | MISSING: celé |
| 2I | A:1507:m | Dvaja politici kričali na seba, keď dopadlo obrovské kladivko. | Two politicians were shouting at each other when the gavel came down. | NONE |
| 2I | A:1577:m | Na poludnie ona už bude chodiť po šatníku v župane dve hodiny. | By noon she will have been walking around the wardrobe for two hours. | MISSING: župane |
| 2I | A:1702:m | Počuj, vraj už spálila štyri marshmallowy a pálenie ju baví. | Listen, apparently she has already burned four and she enjoys burning them. | MISSING: marshmallowy |
| 2I | A:1806:m | Keď sa bábätko usmieva takto, každý si myslí, že je rozkošné. | When it smiles like this, everyone thinks it's adorable. | MISSING: bábätko |
| 2I | A:2050:m | Nabudúce ona dá silnejší úder päsťou, lebo sa bude viac snažiť. | Next time she will throw a punch because she will try harder. | MISSING: silnejší |
| 2I | A:2376:m | Do polnoci dočíta celú knihu a jej drdol prežije úplne všetko! | By midnight she will have finished reading the book and her bun will survive absolutely everything! | NONE |
| 2I | A:2402:m | Hádaj čo, chalan, ktorého zviera skočilo z toho útesu, sa vraj ani nebál. | Guess what, the guy whose animal jumped apparently wasn't even scared. | MISSING: útesu |
| 2I | A:2463:m | Do Vianoc si z toho bábikovského svetra bude uťahovať už mesiace. | By Christmas he will have been making fun of that sweater for months. | MISSING: bábikovského |
| 2I | A:2640:m | Stôl je čistý, takže môže konečne pracovať. | The desk is clean, so he can work. | NONE |
| 2I | A:2948:m | Dve červené nákladné lode priviezli svoj tovar do prístavu po mori. | Two cargo ships brought their goods to the port by sea. | MISSING: červené |
| 2I | A:2989:m | Samozrejme si dala trasu nakresliť na mapu, pre prípad, že by zabudla vlastný plán. | Of course she had the route drawn in case she forgot her own plan. | MISSING: na mapu |
| 2I | A:3096:m | Ona zvykla hrať celé hodiny každú noc, kým sa nestala profesionálnou hráčkou! Úplne posadnutá! | She used to play every night until she became a professional player! Totally obsessed! | MISSING: celé hodiny |
| 2I | A:3177:m | Takéto meškanie už raz prečkala, však? | She has already sat out one like this once, hasn't she? | NONE |
| 2I | A:3506:m | Až po dlhom boji sa dostal na vrchol kopca. | Only after a struggle did he reach the top of the hill. | NONE |
| 2I | A:3631:m | Každý môže sledovať tanec z balkónov. | The dance can be watched from the balconies. | MISSING: Každý |
| 2I | A:3934:m | Červený lampión svietil pri okne celé hodiny, kým sa rozsvietilo svetlo v kuchyni. | The lantern had been shining by the window for hours before the light in the kitchen came on. | MISSING: Červený |
| 2J | A:40:m | Melón má štyridsať gumičiek, takže ich má štyridsať. | The melon has forty, so it has forty of them. | MISSING: gumičiek |
| 2J | A:365:m | Ak cena pôjde ešte vyššie, položí tabuľku. | If the price goes even higher, she'll put it down. | MISSING: tabuľku |
| 2J | A:497:m | Tieto miesta vzadu sú úplne prázdne! | These seats are completely empty! | MISSING: vzadu |
| 2J | A:592:m | Sviečky zapália, len čo posledné taniere budú na čerstvom obruse. | They will light the candles as soon as the plates are on the fresh tablecloth. | MISSING: posledné |
| 2J | A:1568:m | Tam je voľné miesto! — Super, zaparkujem tam. | There's a space! — Great, I'll park there. | MISSING: voľné |
| 2J | A:1599:m | Do západu slnka zlyžuje celý svah. Očividne len malá ranná prechádzka. | By sunset he will have skied down the slope. Obviously just a little morning walk. | NONE |
| 2J | A:1852:m | Namaľované horské jazero ležalo úplne nehybné, keď hladinu zrazu prerušil špľachot. | The mountain lake was lying completely still when a splash suddenly broke the surface. | NONE |
| 2J | A:1918:m | Úradník sa jej spýtal, či má pri sebe preukaz totožnosti. | She was asked whether she had her ID card with her. | MISSING: úradník |
| 2J | A:2152:m | Jeho stará mama mávala svoje poháre v tejto kuchynskej skrinke. | His grandmother used to keep her glasses in this cabinet. | MISSING: kuchynskej |
| 2J | A:2217:m | Včera bola tiež úplne zmätená. | She was also completely confused. | NONE |
| 2J | A:2358:m | Had je skutočná hrozba a uhryzne každého, kto príde bližšie. | The snake is a threat and will bite anyone who comes closer. | MISSING: skutočná |
| 2J | A:2487:m | Kámo, kým doniesli tortu, každý príbuzný sa už dvakrát objal, fakt. | Dude, by the time they brought the cake, every relative had already hugged, seriously. | MISSING: dvakrát |
| 2J | A:2825:m | Kedysi tu býval študentom, ale teraz sa mu trieda klania. | He used to be a student, but now the class bows to him. | MISSING: tu |
| 2J | A:3963:m | Strany sprievodcu si pred cestou dali zalaminovať. | They had the pages laminated before the trip. | MISSING: sprievodcu |
| 2J | A:3970:m | Počuj, vraj z toho veľkého hrnca vyráža para zakaždým, keď zdvihne pokrievku. | Listen, apparently steam bursts out of that pot every time he lifts the lid. | MISSING: veľkého |
