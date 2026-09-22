# Phase 2L Part E - Czech, fresh production set: analysis

**This is the FIRST OUT-OF-SAMPLE measurement of the SOURCE-ONLY design** (frozen Czech stack_2l_cz.py, SOURCE-ONLY + B content check, TIP rejected; set opened once; truth = 4 opus judge sessions).

| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |
|---|---|---|---|---|
| pooled | 473/497 = 95.17 % [92.90, 96.88] | MET / MET | 13/403 = 3.23 % [1.73, 5.45] | MET / missed |
| A1 | 120/124 = 96.77 % [91.95, 99.11] | MET / MET | 2/101 = 1.98 % [0.24, 6.97] | MET / missed |
| A2 | 120/125 = 96.00 % [90.91, 98.69] | MET / MET | 2/100 = 2.00 % [0.24, 7.04] | MET / missed |
| B1 | 115/123 = 93.50 % [87.59, 97.15] | MET / missed | 4/102 = 3.92 % [1.08, 9.74] | MET / missed |
| B2 | 118/125 = 94.40 % [88.80, 97.72] | MET / missed | 5/100 = 5.00 % [1.64, 11.28] | missed / missed |

Diagnostic, L3 only (before the content check): | L3 only | 481/497 = 96.78 % [94.82, 98.15] | MET / MET | 27/403 = 6.70 % [4.46, 9.60] | missed / missed |

Gemini: 1404 counted calls (HTTP 200; {'l3': 896, 'cc': 508}), 0 failed-but-counted, spend $0.127226; phase ledger {'S1_B2': 1287, 'S3E_CC': 508, 'S3E_L3': 896}.

Judge noise (80 hidden duplicates, different sessions): 0/80 disagree = 0.0 % [0.0, 4.51].

## False rejections (24) by cause

by layer {'CC:MISSING': 8, 'L3': 6, 'L3:TIPrej': 8, 'F4v2': 2}; by writer {'correct/None': 24}; by level {'A2': 5, 'B1': 8, 'A1': 4, 'B2': 7}

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

## False acceptances (13) by cause

by layer {'L3+CC:NONE': 13}; by writer type {'M': 8, 'W': 1, 'T': 3, 'None': 1}; by level {'B1': 4, 'B2': 5, 'A2': 2, 'A1': 2}

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

## Judge duplicate disagreements

