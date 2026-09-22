# Wave 1 Part D - Ukrainian, fresh production set: analysis

Frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG); set opened once; truth = 4 opus judge sessions.

| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |
|---|---|---|---|---|
| pooled | 469/496 = 94.56 % [92.18, 96.38] | MET / MET | 11/404 = 2.72 % [1.37, 4.82] | MET / MET |
| A1 | 115/123 = 93.50 % [87.59, 97.15] | MET / missed | 2/102 = 1.96 % [0.24, 6.90] | MET / missed |
| A2 | 114/126 = 90.48 % [83.95, 94.98] | MET / missed | 3/99 = 3.03 % [0.63, 8.60] | MET / missed |
| B1 | 119/123 = 96.75 % [91.88, 99.11] | MET / MET | 3/102 = 2.94 % [0.61, 8.36] | MET / missed |
| B2 | 121/124 = 97.58 % [93.09, 99.50] | MET / MET | 3/101 = 2.97 % [0.62, 8.44] | MET / missed |

Both targets met on the point (pooled): True

Diagnostic, L3 only (before the content check): | L3 only | 478/496 = 96.37 % [94.33, 97.84] | MET / MET | 25/404 = 6.19 % [4.04, 9.00] | missed / missed |

Gemini: 1403 counted calls (HTTP 200; {'l3': 900, 'cc': 503}), 0 failed-but-counted, spend $0.137797; language ledger {'D_CC': 503, 'D_L3': 900}.

Judge noise (80 hidden duplicates, different sessions): 1/80 disagree = 1.25 % [0.03, 6.77].

## False rejections (27) by cause

by layer {'L3:TIPrej': 9, 'L3': 9, 'CC:MISSING': 9}; by writer {'correct/None': 26, 'wrong/M': 1}; by level {'B1': 4, 'B2': 3, 'A1': 8, 'A2': 12}

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:600:c5 | B1 | L3:TIPrej |  | correct/ | «Оце так!» - крикнув коментатор. - Він крикнув, що ніколи не бачив такого стрибка. | The commentator yelled that he had never seen such a jump. | Only interjection 'Wow!' dropped. |
| A:3344:c4 | B2 | L3 |  | correct/ | Вона хоче віддати вкоротити зелений комбінезон до вечірки. | She wants the green jumpsuit shortened by the party. | Same meaning. |
| A:5578:c5 | B2 | L3:TIPrej |  | correct/ | Ще ніколи я не бачив, щоб корок вийшов у цій кухні так чисто. | Never have I watched a cork come out so cleanly in this kitchen. | Same meaning |
| A:11681:c4 | A1 | L3:TIPrej |  | correct/ | Вона кладе на стіл одну стару батарейку. | She's putting an old battery on the table. | Same meaning. |
| A:12537:c3 | A1 | L3:TIPrej |  | correct/ | Маленький ґудзик лежить на дерев'яному столі. | A little button is on the wooden table. | Same meaning. |
| A:13416:c5 | A1 | CC:MISSING | пише | correct/ | Вона пише те рівняння на старій дошці. | That equation is written by her on the old blackboard. | Passive keeps agent; same meaning. |
| A:16686:c3 | A2 | L3 |  | correct/ | За столом є одна гостя й один господар. | There's a guest and a host at the table. | Same meaning. |
| A:18309:c5 | A1 | L3:TIPrej |  | correct/ | Лев лягає в золоту траву. | A lion is lying down in golden grass. | Same meaning |
| A:21981:c5 | A2 | L3 |  | correct/ | Зазвичай він ллє мало соусу, але сьогодні він ллє цілу миску. | He usually doesn't pour much sauce, but today he is pouring a whole bowl. | Same meaning. |
| A:25189:c3 | A1 | L3 |  | correct/ | Стіна має багато старих інструментів. | There are many old tools on the wall. | Same meaning |
| A:25782:c4 | A1 | CC:MISSING | розпаковує | correct/ | Що він розпаковує першим? Складений одяг. | What does he take out first? The folded clothing. | Same meaning. |
| A:27150:c4 | A2 | CC:MISSING | не потребують | correct/ | Примітка до бюджету: двоє гостей налякані й не потребують багато світла. | Note for the budget: two guests are scared and need little light. | Same meaning. |
| A:27437:c5 | A1 | CC:MISSING | руки | correct/ | Чому вони використовують свої руки? Бо руки на тілі. | Why do they use their hands? Because they are on the body. | Same meaning |
| A:28019:c3 | A2 | CC:MISSING | Чергування | correct/ | Чергування в затоці: кожен човен має бути зареєстрований. | Bay watch duty: every boat must be registered. | Same meaning. |
| A:28019:c5 | A2 | CC:MISSING | кожен | correct/ | Чергування в затоці: кожен човен має бути зареєстрований. | Bay duty: all boats have to be registered. | Same meaning. |
| A:33589:c2 | A1 | CC:MISSING | одну | correct/ | Вона дістає з набору одну викрутку. | She takes a screwdriver from the set. | Same meaning. |
| A:34283:c4 | A2 | CC:MISSING | оглядає | correct/ | Медсестра оглядає багато пацієнтів на шкільному ярмарку. | The nurse sees lots of patients at the school fair. | Same meaning |
| A:36130:m | A2 | L3:TIPrej |  | wrong/M | Спокійний день, звісно: вона сьогодні по обіді збирається надрукувати п'ятдесят імейлів. | A calm day, of course: she is going to type fifty emails. | Only time phrase dropped |
| A:36274:c1 | A2 | L3 |  | correct/ | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The racer should wash the motorbike before the 2 pm meeting. | Same meaning. |
| A:36274:c2 | A2 | L3 |  | correct/ | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The racer ought to wash the motorcycle before the meeting at 2:00 pm. | Same meaning |
| A:36274:c3 | A2 | L3 |  | correct/ | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The rider should wash his motorbike before the meeting at 14:00. | Same meaning |
| A:36274:c4 | A2 | L3:TIPrej |  | correct/ | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The racer should clean the motorcycle before the 2 o'clock meeting. | Same meaning |
| A:36274:c5 | A2 | L3 |  | correct/ | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The motorcycle should be washed by the racer before the meeting at 2 pm. | Passive keeps agent |
| A:37763:c1 | B1 | CC:MISSING | за столом | correct/ | Якщо вона наллє ще одну склянку так, за столом стане ще веселіше. | If she pours another glass like that, the table will get even merrier. | Accurate translation. |
| A:38142:c3 | B1 | L3 |  | correct/ | Вона вирішила вдягнути райдужний костюм із пір'я на чолі параду. | She decided she would wear a rainbow-coloured feather costume leading the parade. | Same meaning |
| A:39243:c4 | B1 | L3:TIPrej |  | correct/ | Він полоскав ганчірку, коли помітив ще більше волосся на брудному дзеркалі. | While he was rinsing the rag, he noticed more hair on the dirty mirror. | Same meaning |
| A:44438:c4 | B2 | L3:TIPrej |  | correct/ | Чесно, до заходу сонця ти проїдеш на тому мотоциклі вертикально цілий кілометр. | Honestly, by sunset you'll be riding that motorcycle vertically for an entire kilometre. | Same meaning, future frame. |

## False acceptances (11) by cause

by layer {'L3+CC:NONE': 11}; by writer type {'W': 2, 'T': 2, 'None': 4, 'M': 3}; by level {'A2': 3, 'A1': 2, 'B2': 3, 'B1': 3}

| aid | lvl | layer | cc | writer type | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:13260:w | A2 | L3+CC:NONE | none | W | Скільки жуйки лишилося в пачці? | How much gum is left in the bag? | Bag instead of pack. |
| A:22528:w | A2 | L3+CC:NONE | none | W | Учора він витратив цілий балончик за раз. | Yesterday he used up a whole bottle in one go. | Bottle instead of spray can |
| A:27150:t | A2 | L3+CC:NONE | none | T | Примітка до бюджету: двоє гостей налякані й не потребують багато світла. | Budget note: two guests were scared and didn't need much light. | Past time frame; source is present. |
| A:27540:c2 | A1 | L3+CC:NONE | none | None | Спортсмен може бігти дуже швидко на своїй доріжці. | The athlete can run very fast on her track. | Masculine спортсмен rendered with her |
| A:27540:c5 | A1 | L3+CC:NONE | none | None | Спортсмен може бігти дуже швидко на своїй доріжці. | The athlete can run very quickly in her lane. | Спортсмен is masculine; 'her' mismatches. |
| A:37997:m | B2 | L3+CC:NONE | none | M | Конфлікт за столом триває попри жінку, яка дивиться з дверей. | The conflict continues despite the woman who is watching from the doorway. | Drops place phrase 'at the table'. |
| A:38954:t | B1 | L3+CC:NONE | none | T | Чесно, вона не може не вболівати як найзапекліша фанатка. | Honestly, she couldn't help cheering like the most die-hard fan. | Past tense; source is present. |
| A:39952:m | B1 | L3+CC:NONE | none | M | Бро, вона в хустці прямо біля гарячої духовки, їй мабуть досить жарко. | Bro, she's in a headscarf right next to the oven, she must be pretty hot. | Drops adjective 'hot'. |
| A:40700:c5 | B1 | L3+CC:NONE | none | None | Якщо вона скоро повернеться до зрубу, сьогодні ввечері вона буде в теплі біля вогню. | If she returns to the log cabin soon, she will be cosy and warm by the fire tonight. | Adds 'cosy'. |
| A:43943:m | B2 | L3+CC:NONE | none | M | Чесно, ти зробив смак цього смузі ідеальним завдяки тому манго. | Honestly, you made this smoothie perfect thanks to that mango. | Dropped noun taste |
| A:44381:c3 | B2 | L3+CC:NONE | none | None | Вони крутили те тісто десять хвилин, поки борошно не вибухнуло. Трохи безладно. | They spun that dough for ten minutes until the flour burst everywhere. A little messy. | Added content everywhere |

## Judge duplicate disagreements

- A:44381:c3 (B2, correct/None) s4 wrong vs s1 correct: "They spun that dough for ten minutes until the flour burst everywhere. A little messy."
