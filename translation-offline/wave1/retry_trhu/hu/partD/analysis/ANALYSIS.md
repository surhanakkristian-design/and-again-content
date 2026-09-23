# Wave 1 Part D - Hungarian, fresh production set: analysis

Frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG); set opened once; truth = 4 opus judge sessions.

| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |
|---|---|---|---|---|
| pooled | 464/494 = 93.93 % [91.44, 95.87] | MET / MET | 19/406 = 4.68 % [2.84, 7.21] | MET / missed |
| A1 | 117/125 = 93.60 % [87.78, 97.20] | MET / missed | 2/100 = 2.00 % [0.24, 7.04] | MET / missed |
| A2 | 109/121 = 90.08 % [83.32, 94.77] | MET / missed | 4/104 = 3.85 % [1.06, 9.56] | MET / missed |
| B1 | 121/123 = 98.37 % [94.25, 99.80] | MET / MET | 10/102 = 9.80 % [4.80, 17.29] | missed / missed |
| B2 | 117/125 = 93.60 % [87.78, 97.20] | MET / missed | 3/100 = 3.00 % [0.62, 8.52] | MET / missed |

Both targets met on the point (pooled): True

Diagnostic, L3 only (before the content check): | L3 only | 474/494 = 95.95 % [93.82, 97.51] | MET / MET | 44/406 = 10.84 % [7.99, 14.27] | missed / missed |

Gemini: 1418 counted calls (HTTP 200; {'l3': 900, 'cc': 518}), 0 failed-but-counted, spend $0.208738; language ledger {'D_CC': 518, 'D_L3': 900}.

Judge noise (80 hidden duplicates, different sessions): 0/80 disagree = 0.0 % [0.0, 4.51].

## False rejections (30) by cause

by layer {'L3': 14, 'L3:TIPrej': 6, 'CC:MISSING': 10}; by writer {'correct/None': 30}; by level {'B2': 8, 'A2': 12, 'A1': 8, 'B1': 2}

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:1465:c1 | B2 | L3 |  | correct/ | Az ösvény végére három órán át fognak gyalogolni a kaktuszok között. | By the end of the trail, they will have been walking among the cacti for three hours. | Accurate meaning and grammar. |
| A:12937:c3 | A2 | L3:TIPrej |  | correct/ | A fiú nagyon könnyen kapja el a piros labdát. | The boy is catching the red ball very easily. | Accurate meaning. |
| A:16071:c4 | A2 | L3 |  | correct/ | Nem sok idő maradt a meccsből. | Not much of the match time remains. | Same meaning |
| A:16791:c3 | A1 | CC:MISSING | tele | correct/ | A hörcsög magokkal tömi tele a pofazacskóját. | The hamster fills its cheeks with seeds. | Cheeks acceptable for cheek pouches. |
| A:18558:c2 | A1 | CC:MISSING | sakktáblájuk | correct/ | Az idős férfiaknak kis sakktáblájuk van. | The elderly men have got small chessboards. | Faithful |
| A:20767:c1 | A2 | CC:MISSING | elolvasnod | correct/ | Ha jó jegyet akarsz, el kellene olvasnod a jegyzeteidet. | If you want a good grade, you should read your notes. | Accurate meaning. |
| A:20767:c2 | A2 | CC:MISSING | el | correct/ | Ha jó jegyet akarsz, el kellene olvasnod a jegyzeteidet. | If you want a good mark, you ought to read your notes. | Faithful |
| A:26068:c5 | A2 | L3:TIPrej |  | correct/ | Gyere hatkor, és a sétájuk éppen csak kezdődni fog. | Come at six, and their walk will be starting. | Dropped 'just' is acceptable. |
| A:26454:c2 | A2 | L3 |  | correct/ | Nézd! A felesége épp fordítja egy palacsintát a serpenyőben. | Look! Her wife is turning a pancake in the frying pan. | Genderless possessor; her allowed. |
| A:27588:c5 | A2 | L3:TIPrej |  | correct/ | A támadás hirtelen véget ér, és a mező teljesen üres! | The attack suddenly ends and the field is empty! | Dropped degree adverb acceptable |
| A:31482:c2 | A1 | CC:MISSING | kap | correct/ | Mi kap oda a huskynak? Két játék dinoszaurusz. | What is the husky given? Two toy dinosaurs. | Same meaning via passive. |
| A:31482:c3 | A1 | CC:MISSING | oda | correct/ | Mi kap oda a huskynak? Két játék dinoszaurusz. | What does the husky receive? Two toy dinosaurs. | Accurate meaning. |
| A:32585:c3 | A1 | L3 |  | correct/ | A szobájában van egy nagyon hideg légkondi. | His room has a very cold air conditioner. | Same meaning; genderless possessive. |
| A:33560:c4 | A1 | L3 |  | correct/ | A gyerek szombaton a labdájához fut. | The kid runs to his ball on Saturdays. | Accurate meaning. |
| A:33847:c5 | A1 | L3:TIPrej |  | correct/ | A lánynak ma sok postája van. | The girl has a lot of mail. | Dropped 'today' is acceptable. |
| A:34183:c1 | A2 | CC:MISSING | semmilyen | correct/ | Képzeld, ő azt mondta, hogy a szekrényében nincs semmilyen narancssárga ing. | Imagine, she said there are no orange shirts in her wardrobe. | Accurate reported meaning. |
| A:34325:c4 | A1 | L3 |  | correct/ | A házi cica ráugorhat a játékegérre. | The pet cat is allowed to jump on the toy mouse. | -hat allows permission reading. |
| A:36362:c1 | A2 | CC:MISSING | kormánynál | correct/ | Őszintén, ennél a kormánynál nálad jobb sofőr nincs. | Honestly, there's no better driver than you at this wheel. | Same meaning |
| A:36362:c2 | A2 | L3 |  | correct/ | Őszintén, ennél a kormánynál nálad jobb sofőr nincs. | Honestly, there is no better driver behind this wheel than you. | Accurate translation. |
| A:36362:c4 | A2 | L3 |  | correct/ | Őszintén, ennél a kormánynál nálad jobb sofőr nincs. | Honestly, nobody drives better than you at this wheel. | Same meaning. |
| A:36362:c5 | A2 | L3 |  | correct/ | Őszintén, ennél a kormánynál nálad jobb sofőr nincs. | Honestly, at this wheel there is no better driver than you. | Accurate translation. |
| A:37518:c5 | B2 | L3:TIPrej |  | correct/ | A nyugalma a T-rex-támadás óta odavan, ezért a takaró alá bújik. | He hasn't been calm since the T-rex attack, so he's hiding under the blanket. | Same meaning, rephrased. |
| A:38669:c1 | B2 | L3 |  | correct/ | Mire ő a kamerához ér, a távoli tornyok eltűnnek a ködben. | By the time he reaches the camera, the distant towers will have disappeared into the fog. | Future frame kept, meaning matches. |
| A:38669:c4 | B2 | L3 |  | correct/ | Mire ő a kamerához ér, a távoli tornyok eltűnnek a ködben. | By the time she reaches the camera, the far-off towers will have disappeared in the fog. | Faithful future meaning |
| A:39777:c2 | B1 | L3 |  | correct/ | A kukorica egy nagylelkű tyúk által lett betolva a lyukba. Nyilván az egerek végezték az összes munkát. | A generous hen pushed the corn into the hole. Obviously the mice did all the work. | Active keeps agent; same meaning. |
| A:40273:c4 | B1 | CC:MISSING | útmutatókkal | correct/ | Kicsit le vagyok nyűgözve: te biztos zseniális vagy az útmutatókkal; a szekrény olyan gyorsan összeállt. | I'm kind of impressed: you must be brilliant at following instructions; the wardrobe was put together so fast. | Same meaning. |
| A:41343:c4 | B2 | L3:TIPrej |  | correct/ | Katasztrófa! Ő tíz perce kopog az ajtón, és a csomag még mindig a kezében van! | Disaster! She has been knocking on the door for 10 minutes and the package is in her hand! | Dropped 'still' is acceptable. |
| A:41398:c4 | B2 | L3 |  | correct/ | Ha nem hozta volna el az iratokat, a megbeszélés most lenne szüneteltetve. | Had she not brought the documents, the meeting would be paused. | Dropped 'now' is acceptable. |
| A:42805:c3 | B2 | L3 |  | correct/ | Több kutya most követi a futót, ami jellemzően megfigyelhető a társas fajoknál. | A few dogs are following the jogger now, which is typical of social species. | Same meaning, correct English. |
| A:44237:c2 | B2 | CC:MISSING | beszállt | correct/ | Csajszi, ő azt mondta nekem, hogy az edző már tíz perce vezette az órát, amikor a macska beszállt. | Girl, she told me the trainer had been running the class for ten minutes when the cat got involved. | Same meaning; dropped "already" acceptable. |

## False acceptances (19) by cause

by layer {'L3+CC:NONE': 19}; by writer type {'None': 6, 'M': 6, 'W': 2, 'T': 4, 'S': 1}; by level {'B1': 10, 'A1': 2, 'A2': 4, 'B2': 3}

| aid | lvl | layer | cc | writer type | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:4096:c5 | B1 | L3+CC:NONE | none | None | Miközben tartotta a régi kagylót a füléhez, a telefonja a folyosó padlóján zümmögött. | While holding the old receiver to his ear, his phone was vibrating on the corridor floor. | Dangling participle makes the phone hold the receiver |
| A:4096:m | B1 | L3+CC:NONE | none | M | Miközben tartotta a régi kagylót a füléhez, a telefonja a folyosó padlóján zümmögött. | While he was holding the receiver to his ear, his phone was buzzing on the hallway floor. | Drops adjective 'old'. |
| A:16791:w | A1 | L3+CC:NONE | none | W | A hörcsög magokkal tömi tele a pofazacskóját. | The hamster stuffs its cheek pouches with nuts. | Nuts instead of seeds |
| A:17769:c5 | A2 | L3+CC:NONE | none | None | Ezt csókkal kellene elmondanod, nem üzenettel. | This should be said with a kiss, not a message. | Passive drops agent 'you' named by the verb. |
| A:27224:c4 | A2 | L3+CC:NONE | none | None | Csajszi, ő azt mondta, hogy a repülőgép pont a feje fölött repült el! | Girl, he told me the plane flew just over his head! | Added content: told me. |
| A:30885:m | A1 | L3+CC:NONE | none | M | Hol áll meg a kerékpáros? A lámpánál. | Where does he stop? At the traffic light. | Dropped noun cyclist |
| A:31300:c2 | A2 | L3+CC:NONE | none | None | Határidő hétfő: ő a tervet maga fogja befejezni. | Deadline is Monday: he will finish the plan himself. | Missing article before 'Deadline' |
| A:34432:c3 | A2 | L3+CC:NONE | none | None | Több száz cetli! Ez a terv annyi időt igényel, rémálom! | Hundreds of sticky notes! This plan needs so much time, what a nightmare! | Added 'sticky'. |
| A:36905:c1 | B1 | L3+CC:NONE | none | None | Az üzlet arra számít, hogy bevonz 500 új ügyfelet, amint felszerelik a tévét. | The shop expects to attract 500 new customers as soon as the TV is installed. | Hungarian subject is "you" (bevonz), not the shop. |
| A:38740:m | B1 | L3+CC:NONE | none | M | Neki sikerül széthúznia a nehéz ajtókat, és ő megáll az ajtónyílásban. | He manages to pull the doors apart, and he stops in the doorway. | Dropped adjective heavy. |
| A:38740:t | B1 | L3+CC:NONE | none | T | Neki sikerül széthúznia a nehéz ajtókat, és ő megáll az ajtónyílásban. | He managed to pull the heavy doors apart, and he stopped in the doorway. | Past tense; Hungarian is present. |
| A:39999:m | B2 | L3+CC:NONE | none | M | Ők tíz percig billegtek a tüskés sarkakon, mire a nő végül nevetve összeesett! | They wobbled on the spiky heels for ten minutes before the woman finally collapsed! | 'laughing' dropped. |
| A:40202:m | B1 | L3+CC:NONE | none | M | Ha a vásárlók figyelmen kívül hagyják egy ajtóban álló eladót, ő jellemzően végül egyedül ül. | If customers ignore a salesperson, he typically ends up sitting alone. | Drops 'standing in a doorway' |
| A:40202:t | B1 | L3+CC:NONE | none | T | Ha a vásárlók figyelmen kívül hagyják egy ajtóban álló eladót, ő jellemzően végül egyedül ül. | If customers ignored a salesperson standing in a doorway, he typically ended up sitting alone. | General present shifted to past. |
| A:40438:m | B1 | L3+CC:NONE | none | M | A nagy piros lámpás az ablak mellé lett helyezve, hogy elkapja az esti fényt. | The big lantern was placed next to the window to catch the evening light. | Dropped adjective 'red'. |
| A:40592:t | B1 | L3+CC:NONE | none | T | Őszintén, a keret, amelyet te vízszintbe tettél, nagyon elegáns. | Honestly, the frame that you levelled was very elegant. | Present time frame shifted to past |
| A:41194:t | B2 | L3+CC:NONE | none | T | Ritkán néz ki egy kutya ilyen rendezetten egy nyírás után. Enyhén lenyűgöző. | Rarely did a dog look so neat after a haircut. Mildly impressive. | Past time frame; source is present. |
| A:41543:w | B2 | L3+CC:NONE | none | W | A tehén persze tagadta, hogy megette az egész pitét, miközben az üres tányér fölé hajolt. | The cow of course denied that it had eaten the whole cake while leaning over the empty plate. | Cake instead of pie |
| A:44454:s | B1 | L3+CC:NONE | none | S | Az esernyőt a szél kifordította, így most használhatatlan. | The umbrella was turn inside out by the wind, so now it's useless. | Grammar error: was turn. |

## Judge duplicate disagreements

