# Translation Wave 1: measurement of native de, ua, es -> English (report, 22 Sept 2026)

Pipeline: `~/Projects/and-again-content/translation-offline/wave1/` (below `W1/`). App branch: `translation-wave1`, checked out in the worktree `~/Projects/and-again-wave1-wt` (master untouched).

## 1. Result first

| lang | coverage (pooled) | FA (pooled) | both targets, point | both targets, interval | routed |
|---|---|---|---|---|---|
| de | 472/500 = 94.40 % [92.01, 96.25] | 13/400 = 3.25 % [1.74, 5.49] | **MET** | coverage MET, FA **missed** (upper bound 5.49) | **yes** |
| ua | 469/496 = 94.56 % [92.18, 96.38] | 11/404 = 2.72 % [1.37, 4.82] | **MET** | **MET** (both) | **yes** |
| es | not measured | not measured | - | - | **no** |

- Targets: coverage >= 90 % and FA < 5 %. Intervals are exact 95 % Clopper-Pearson.
- **es stopped alone.** Judge session s4 returned 244 of 245 items in all three attempts (a different jid missing each time). The set was never frozen or opened and used 0 Gemini calls. It can be reused.

Per level (exact CP 95 %), plus the L3-only diagnostic (the decision before the content check):

| lang | block | coverage, CP 95 % | >= 90 %: point / interval | FA, CP 95 % | < 5 %: point / interval |
|---|---|---|---|---|---|
| **de** | **pooled** | 472/500 = 94.40 % [92.01, 96.25] | MET / MET | 13/400 = 3.25 % [1.74, 5.49] | MET / missed |
| de | A1 | 119/124 = 95.97 % [90.84, 98.68] | MET / MET | 3/101 = 2.97 % [0.62, 8.44] | MET / missed |
| de | A2 | 122/125 = 97.60 % [93.15, 99.50] | MET / MET | 3/100 = 3.00 % [0.62, 8.52] | MET / missed |
| de | B1 | 118/125 = 94.40 % [88.80, 97.72] | MET / missed | 3/100 = 3.00 % [0.62, 8.52] | MET / missed |
| de | B2 | 113/126 = 89.68 % [83.00, 94.39] | missed / missed | 4/99 = 4.04 % [1.11, 10.02] | MET / missed |
| de | L3 only (diagnostic) | 483/500 = 96.60 % [94.61, 98.01] | MET / MET | 29/400 = 7.25 % [4.91, 10.25] | missed / missed |
| **ua** | **pooled** | 469/496 = 94.56 % [92.18, 96.38] | MET / MET | 11/404 = 2.72 % [1.37, 4.82] | MET / MET |
| ua | A1 | 115/123 = 93.50 % [87.59, 97.15] | MET / missed | 2/102 = 1.96 % [0.24, 6.90] | MET / missed |
| ua | A2 | 114/126 = 90.48 % [83.95, 94.98] | MET / missed | 3/99 = 3.03 % [0.63, 8.60] | MET / missed |
| ua | B1 | 119/123 = 96.75 % [91.88, 99.11] | MET / MET | 3/102 = 2.94 % [0.61, 8.36] | MET / missed |
| ua | B2 | 121/124 = 97.58 % [93.09, 99.50] | MET / MET | 3/101 = 2.97 % [0.62, 8.44] | MET / missed |
| ua | L3 only (diagnostic) | 478/496 = 96.37 % [94.33, 97.84] | MET / MET | 25/404 = 6.19 % [4.04, 9.00] | missed / missed |
| es | - | not measured | - | not measured | - |

- **Per-level misses:**
  - de B2 coverage 89.68 % misses on the point.
  - Every per-level FA interval lies above 5 %: with about 100 wrong answers per level, the CP upper bound cannot fall below 5 % unless there are 0-1 FAs.
- **What the content check did:**
  - de: it caught 16 FAs (29 -> 13) at a cost of 11 correct answers (483 -> 472).
  - ua: it caught 14 FAs (25 -> 11) at a cost of 9 (478 -> 469).
  - Without it, neither language meets FA < 5 %.

## 2. What was run (decision 26: no headless CLI)

- **Transport.** Every writer and judge ran as an Opus subagent (`tx-opus`) of this session.
  - The pipeline writes `sessions/<sid>/prompt.txt` plus `PENDING.json` and exits 6.
  - Each subagent was told to read only that one file and write only `reply.txt`.
  - The subagent's reported tokens go into `tokens.json`. The next run ingests the reply: same validation, same retry `_r1`, resume at 0 cost, same caps.
  - Code: `W1/common/pipeline_w1.py` (`sub_session`, `partA_live`), `W1/common/chain_w1_sub.sh`, `W1/common/rec_tokens.py`. Test t14 was added, and `test_w1` is 14/14.
  - `STOP_quota.md`, `STOP_usage_limit.md` and `CHAIN_FAIL.txt` were deleted in de, ua and es. The refused 22 Sept de headless set was archived to `W1/de/_headless_refused_20260922/`.
- **Data.** Built from the LIVE `exercise_localizations` rows of `translation_selected_exercises`, SELECT only (`W1/<lang>/partA_live/`).
  - All 4,064 rows per language are filled: A1 1,174 / A2 1,220 / B1 885 / B2 785.
  - Compared with the 22 Sept Part A snapshot:
    - de: 2,015 newly filled, 1 changed (3046: the missing period was added), 2,048 unchanged;
    - ua: 2,015 newly filled, 223 changed (the explicit-subject rewrite in the database), 1,826 unchanged;
    - es: 2,015 newly filled, 630 changed, 1,419 unchanged.
  - Part B (rewrite) and Part E (DB write) did not run. **No database write of any kind.**
- **Sets.**
  - 100 sentences per language, 25 per level.
  - The 460 exercise_ids of every earlier `set/` directory under phase1*/phase2* are excluded. Excluded per level: de 29/34/26/27, ua 27/31/30/38, es 34/25/34/25. No relaxation was needed.
  - The three sets are disjoint (one shared seeded order, positions mod 3). Checked: 0 overlap between every pair.
  - Set SHA-256: de 16e42257…, ua 7df16b26…, es 6d48d5f7….
- **Writers.**
  - 4 blind writer sessions per language, one per level. Each sees wid / source / level / topic only.
  - Output: 900 answers per language (500 correct + 400 wrong), T/W/M/S = 100/100/100/100 in all three languages, 0 dedupes.
- **Judges.**
  - ONE judge prompt per language (the owner's rules verbatim, including decision 22 and the drop list) across 4 shuffled sessions of 245 items.
  - 80 hidden duplicates in different sessions. Packets carry jid / source / level / answer / topic only.
- **Freeze.** FROZEN_SHA_D covers common/*.py, common/*.sh, spec/*.txt, partA_live/rows.jsonl, items.jsonl and truth.jsonl. Then a freeze commit, a RUN_COMMIT, a clean-tree check and `shasum -c` before the open.
  - de: freeze hash 46a19f36…, FREEZE_COMMIT 5507135, RUN_COMMIT 2f57c5f.
  - ua: freeze hash e17b69fa…, FREEZE_COMMIT 112ccbb, RUN_COMMIT 877dc96.
- **Open.** Each set was opened ONCE (`run/access_log.jsonl`: 1 entry each) by the frozen stack:
  - L3 SOURCE-ONLY on gemini-3.1-flash-lite, where TIP / DIFF / unparsable are rejected;
  - then the content check, where NONE accepts and MISSING rejects;
  - no F4, no AG.

## 3. False acceptances and false rejections by cause (every item below)

**de. FA 13, all through L3 SAME + content check NONE:**
- 7 × M (a dropped qualifier: paper, captain's, krass, open, into the grass, in line, "ich glaube");
- 2 × T (stuck vs streckt, could vs kannst);
- 2 × S (a missing article, "a underground");
- 1 × W (she for er);
- 1 writer-correct answer that the judge marked wrong for adding "Wow".

**de. FR 28:**
- **13 L3 DIFF.** 10 of them are two B2 sentences: 41807 "loben … seit" and 44823 "hat … geschlagen" with "bis zum Ende". The checker rejects the English future-perfect reading that the judge accepts.
- **11 content-check MISSING.** Paraphrases that the CC reads as a lost word: pflegte, aufhören, Ehrfurcht, dieser, so, …
- **4 TIP rejections:** Help me!, Respect to you, a dropped "sehr", a dropped "endlich".

**ua. FA 11, all L3 SAME + NONE:**
- 2 × W (bag for пачка, bottle for балончик);
- 2 × T;
- 3 × M (a dropped adjective, a place phrase, the noun "taste");
- 4 writer-correct answers that the judge marked wrong:
  - "her" for Спортсмен … своїй, twice. This is debatable under decision 22, which covers genderless sources, but спортсмен is grammatically masculine;
  - an added "cosy";
  - an added "everywhere".

**ua. FR 27:**
- **9 CC MISSING** (e.g. passive "is written by her", "all boats" for кожен, "need little light" for не потребують багато).
- **9 L3 DIFF.** 4 are one sentence: 36274 "мав би" -> should / ought to.
- **9 TIP rejections.** 8 are on writer-correct answers, mostly a tense or aspect choice (for example "is lying down", "'s putting"). 1 is on a writer-M answer that the judge labelled correct: only "сьогодні по обіді" was dropped, a time phrase the judge accepts.

**Reading of the causes:**
- FAs are dominated by dropped modifiers (M) that both layers let through.
- FRs are dominated by the content check's literalism and by L3 on future-perfect and modal constructions.
- Neither cause is language-specific: the same pattern was seen in sk/cz.

#### de - False acceptances (13)

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:23310:t | A1 | L3+CC:NONE |  | wrong/T | Die Schlange streckt uns ihre dünne Zunge entgegen. | The snake stuck its thin tongue out at us. | Past instead of present. |
| A:29199:c4 | A1 | L3+CC:NONE |  | correct/- | Wann benutzt du deine Kamera? Jeden Abend. Beeindruckend. | When do you use your camera? Each evening. Wow, impressive. | Added content 'Wow'. |
| A:35656:t | A1 | L3+CC:NONE |  | wrong/T | Ehrlich, du kannst zehn Sonnenblumen in zwei Armen tragen. Beeindruckend. | Honestly, you could carry ten sunflowers in two arms. Impressive. | 'could' changes present ability. |
| A:16914:m | A2 | L3+CC:NONE |  | wrong/M | Schau! Sie fächelt sich gerade mit einem Papierfächer. | Look! She is fanning herself with a fan. | Drops 'paper' of paper fan. |
| A:25234:m | A2 | L3+CC:NONE |  | wrong/M | Der Turm ist zu groß. Ich glaube, ich werde das aufräumen. | The tower is too big. I'll tidy that up. | Dropped main verb 'I think'. |
| A:34515:m | A2 | L3+CC:NONE |  | wrong/M | Bro, schau dir diese krasse Gischt an. Er wird klatschnass werden, ohne Witz. | Bro, look at this spray. He's going to get soaking wet, no joke. | Drops adjective krass. |
| A:42849:s | B1 | L3+CC:NONE |  | wrong/S | Bro, der Jogger hat sich seinen Anteil Pizza genommen, und die Hundeausführerin auch, ohne Witz. | Bro, jogger took his share of pizza, and so did the dog walker, no joke. | Missing article before 'jogger'. |
| A:44700:m | B1 | L3+CC:NONE |  | wrong/M | Seine Waffe wurde ins Gras gesenkt! Es ist vorbei, komplett vorbei! | His weapon was lowered! It's over, completely over! | Drops 'into the grass'. |
| A:7123:m | B1 | L3+CC:NONE |  | wrong/M | Wenn Nina so weiterspielt, gibt der Trainer ihr auch die Kapitänsbinde. | If Nina keeps playing like this, the coach will give her the armband too. | Drops 'captain's' from armband. |
| A:1391:w | B2 | L3+CC:NONE |  | wrong/W | Er schlug vor, die fertige Platte ins Schaufenster des Ateliers zu hängen. | She suggested hanging the finished plate in the studio's shop window. | She instead of he. |
| A:40435:m | B2 | L3+CC:NONE |  | wrong/M | Die Lagune erstreckt sich bis zum offenen Meer jenseits der Felswände. | The lagoon stretches to the sea beyond the cliffs. | Dropped adjective 'open'. |
| A:44395:s | B2 | L3+CC:NONE |  | wrong/S | Bro, ich wünschte, ich hätte so eine Tiefgarage, echt jetzt. | Bro, I wish I had a underground garage like that, seriously. | 'a underground' article error. |
| A:44573:m | B2 | L3+CC:NONE |  | wrong/M | Hör mal, ich habe gehört, dass sie eine Stunde in der Schlange gewartet hatte, bevor sie endlich gewählt hat. | Listen, I heard that she had waited for an hour before she finally voted. | Drops place phrase in line. |

#### de - False rejections (28)

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:32949:c4 | A1 | CC:MISSING | Gärtnerin | correct/- | Die Gärtnerin hat Werkzeug in ihren Schürzentaschen. | There are tools in the gardener's apron pockets. | Same meaning, different structure. |
| A:34130:c5 | A1 | CC:MISSING | küssen | correct/- | Sie sind alt, und sie küssen sich ewig! Einfach wunderschön! | They are old and they keep kissing forever! Absolutely beautiful! | Same meaning. |
| A:35589:c3 | A2 | CC:MISSING | Kraft | correct/- | Mit dieser Kraft wird sie bald den Gipfel erreichen. | With this kind of strength she is going to reach the top soon. | Same meaning. |
| A:35589:c5 | A2 | CC:MISSING | dieser | correct/- | Mit dieser Kraft wird sie bald den Gipfel erreichen. | With strength like this, she will soon get to the top. | Same meaning. |
| A:36872:c4 | B1 | CC:MISSING | niemanden | correct/- | Bei ihren früheren Rennen brauchte sie niemanden, der ihr im Ziel assistierte. | In her past races, she never needed anyone to assist her at the finish line. | Same meaning. |
| A:36949:c3 | B1 | CC:MISSING | herunter | correct/- | Während er durch die Galerie ging, fiel ihm vor Ehrfurcht die Kinnlade herunter. | While he was going through the gallery, his jaw fell in awe. | Meaning preserved, slightly unidiomatic. |
| A:36949:c5 | B1 | CC:MISSING | Ehrfurcht | correct/- | Während er durch die Galerie ging, fiel ihm vor Ehrfurcht die Kinnlade herunter. | While he walked through the gallery, his jaw dropped in amazement. | Same meaning. |
| A:42734:c3 | B1 | CC:MISSING | wieder | correct/- | Nächste Woche um diese Zeit machen sie in derselben Nische wieder einen geheimen Deal. | Next week at this time, they will be making another secret deal in the same nook. | Same meaning; another covers wieder. |
| A:6526:c5 | B1 | CC:MISSING | pflegte | correct/- | Als Kind pflegte sie, den Globus zu drehen und auf ein zufälliges Land zu tippen. | When she was little, she spun the globe and tapped on a random country. | Habitual past preserved. |
| A:8838:c5 | B1 | CC:MISSING | aufhören | correct/- | Er hörte nicht auf, den Sack zu schlagen, bis er durch die Garage schwang. | He kept on hitting the bag until it swung across the garage. | Same meaning. |
| A:41628:c4 | B2 | CC:MISSING | so | correct/- | Bro, er wird diese Grube bis Sonnenuntergang so tief gegraben haben, dass er eine Leiter braucht, echt. | Bro, by sunset he will have dug this pit deep enough that he needs a ladder, really. | Same meaning. |
| A:33109:c5 | A1 | L3 |  | correct/- | Die Führerin führt die Gruppe eine schmale Gasse hinunter. | The guide leads the group down a narrow side street. | Same meaning. |
| A:8838:c4 | B1 | L3 |  | correct/- | Er hörte nicht auf, den Sack zu schlagen, bis er durch die Garage schwang. | He didn't stop punching the bag until it was swinging through the garage. | Same meaning. |
| A:40655:c4 | B2 | L3 |  | correct/- | Sie wartet im Bett, während die Flüssigkeit aus der braunen Flasche den Löffel füllt. | She is waiting in bed while the spoon fills with the liquid from the brown bottle. | Same meaning. |
| A:41807:c1 | B2 | L3 |  | correct/- | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | By the end of the day, the colleagues will have been praising this graphic for about eight hours. | Same meaning. |
| A:41807:c2 | B2 | L3 |  | correct/- | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | At the end of the day the colleagues will have been praising this chart for roughly eight hours. | Same meaning. |
| A:41807:c3 | B2 | L3 |  | correct/- | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | By the end of the day the co-workers will have been praising this graphic for around eight hours. | Accurate translation. |
| A:41807:c4 | B2 | L3 |  | correct/- | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | By the end of the day, the colleagues will have praised this graphic for about eight hours. | Same meaning. |
| A:41807:c5 | B2 | L3 |  | correct/- | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | By the end of the day, this graphic will have been praised by the colleagues for about eight hours. | Passive keeps agent; same meaning. |
| A:44823:c1 | B2 | L3 |  | correct/- | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the ride, the tram's pantograph will have struck hundreds of sparks from the wire. | Accurate translation. |
| A:44823:c2 | B2 | L3 |  | correct/- | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the journey the pantograph of the tram will have knocked hundreds of sparks off the wire. | Same meaning and time frame. |
| A:44823:c3 | B2 | L3 |  | correct/- | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the trip, the tram's pantograph will have thrown hundreds of sparks from the wire. | Future reference preserved. |
| A:44823:c4 | B2 | L3 |  | correct/- | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the ride the streetcar's pantograph will have made hundreds of sparks fly from the wire. | Same meaning. |
| A:44823:c5 | B2 | L3 |  | correct/- | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the ride, hundreds of sparks will have been struck from the wire by the tram's pantograph. | Passive keeps the agent. |
| A:34858:c5 | A1 | L3:TIPrej |  | correct/- | Hilfe! Etwas ist in diesem dunklen Raum! | Help me! Something is in this dark room! | Idiomatic 'Help me!'; meaning preserved. |
| A:35377:c4 | A1 | L3:TIPrej |  | correct/- | Du sagst mit Blumen sorry. Respekt. | You say sorry with flowers. Respect to you. | Idiomatic rendering of 'Respekt'. |
| A:23076:c5 | A2 | L3:TIPrej |  | correct/- | Die Wolken ziehen sehr langsam über den Himmel. | The clouds are moving slowly across the sky. | Dropped degree adverb acceptable. |
| A:44573:c5 | B2 | L3:TIPrej |  | correct/- | Hör mal, ich habe gehört, dass sie eine Stunde in der Schlange gewartet hatte, bevor sie endlich gewählt hat. | Listen, I heard she waited in line for an hour before she voted. | Same meaning; endlich drop acceptable. |

#### ua - False acceptances (11)

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:27540:c2 | A1 | L3+CC:NONE |  | correct/- | Спортсмен може бігти дуже швидко на своїй доріжці. | The athlete can run very fast on her track. | Masculine спортсмен rendered with her |
| A:27540:c5 | A1 | L3+CC:NONE |  | correct/- | Спортсмен може бігти дуже швидко на своїй доріжці. | The athlete can run very quickly in her lane. | Спортсмен is masculine; 'her' mismatches. |
| A:13260:w | A2 | L3+CC:NONE |  | wrong/W | Скільки жуйки лишилося в пачці? | How much gum is left in the bag? | Bag instead of pack. |
| A:22528:w | A2 | L3+CC:NONE |  | wrong/W | Учора він витратив цілий балончик за раз. | Yesterday he used up a whole bottle in one go. | Bottle instead of spray can |
| A:27150:t | A2 | L3+CC:NONE |  | wrong/T | Примітка до бюджету: двоє гостей налякані й не потребують багато світла. | Budget note: two guests were scared and didn't need much light. | Past time frame; source is present. |
| A:38954:t | B1 | L3+CC:NONE |  | wrong/T | Чесно, вона не може не вболівати як найзапекліша фанатка. | Honestly, she couldn't help cheering like the most die-hard fan. | Past tense; source is present. |
| A:39952:m | B1 | L3+CC:NONE |  | wrong/M | Бро, вона в хустці прямо біля гарячої духовки, їй мабуть досить жарко. | Bro, she's in a headscarf right next to the oven, she must be pretty hot. | Drops adjective 'hot'. |
| A:40700:c5 | B1 | L3+CC:NONE |  | correct/- | Якщо вона скоро повернеться до зрубу, сьогодні ввечері вона буде в теплі біля вогню. | If she returns to the log cabin soon, she will be cosy and warm by the fire tonight. | Adds 'cosy'. |
| A:37997:m | B2 | L3+CC:NONE |  | wrong/M | Конфлікт за столом триває попри жінку, яка дивиться з дверей. | The conflict continues despite the woman who is watching from the doorway. | Drops place phrase 'at the table'. |
| A:43943:m | B2 | L3+CC:NONE |  | wrong/M | Чесно, ти зробив смак цього смузі ідеальним завдяки тому манго. | Honestly, you made this smoothie perfect thanks to that mango. | Dropped noun taste |
| A:44381:c3 | B2 | L3+CC:NONE |  | correct/- | Вони крутили те тісто десять хвилин, поки борошно не вибухнуло. Трохи безладно. | They spun that dough for ten minutes until the flour burst everywhere. A little messy. | Added content everywhere |

#### ua - False rejections (27)

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:13416:c5 | A1 | CC:MISSING | пише | correct/- | Вона пише те рівняння на старій дошці. | That equation is written by her on the old blackboard. | Passive keeps agent; same meaning. |
| A:25782:c4 | A1 | CC:MISSING | розпаковує | correct/- | Що він розпаковує першим? Складений одяг. | What does he take out first? The folded clothing. | Same meaning. |
| A:27437:c5 | A1 | CC:MISSING | руки | correct/- | Чому вони використовують свої руки? Бо руки на тілі. | Why do they use their hands? Because they are on the body. | Same meaning |
| A:33589:c2 | A1 | CC:MISSING | одну | correct/- | Вона дістає з набору одну викрутку. | She takes a screwdriver from the set. | Same meaning. |
| A:27150:c4 | A2 | CC:MISSING | не потребують | correct/- | Примітка до бюджету: двоє гостей налякані й не потребують багато світла. | Note for the budget: two guests are scared and need little light. | Same meaning. |
| A:28019:c3 | A2 | CC:MISSING | Чергування | correct/- | Чергування в затоці: кожен човен має бути зареєстрований. | Bay watch duty: every boat must be registered. | Same meaning. |
| A:28019:c5 | A2 | CC:MISSING | кожен | correct/- | Чергування в затоці: кожен човен має бути зареєстрований. | Bay duty: all boats have to be registered. | Same meaning. |
| A:34283:c4 | A2 | CC:MISSING | оглядає | correct/- | Медсестра оглядає багато пацієнтів на шкільному ярмарку. | The nurse sees lots of patients at the school fair. | Same meaning |
| A:37763:c1 | B1 | CC:MISSING | за столом | correct/- | Якщо вона наллє ще одну склянку так, за столом стане ще веселіше. | If she pours another glass like that, the table will get even merrier. | Accurate translation. |
| A:25189:c3 | A1 | L3 |  | correct/- | Стіна має багато старих інструментів. | There are many old tools on the wall. | Same meaning |
| A:16686:c3 | A2 | L3 |  | correct/- | За столом є одна гостя й один господар. | There's a guest and a host at the table. | Same meaning. |
| A:21981:c5 | A2 | L3 |  | correct/- | Зазвичай він ллє мало соусу, але сьогодні він ллє цілу миску. | He usually doesn't pour much sauce, but today he is pouring a whole bowl. | Same meaning. |
| A:36274:c1 | A2 | L3 |  | correct/- | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The racer should wash the motorbike before the 2 pm meeting. | Same meaning. |
| A:36274:c2 | A2 | L3 |  | correct/- | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The racer ought to wash the motorcycle before the meeting at 2:00 pm. | Same meaning |
| A:36274:c3 | A2 | L3 |  | correct/- | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The rider should wash his motorbike before the meeting at 14:00. | Same meaning |
| A:36274:c5 | A2 | L3 |  | correct/- | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The motorcycle should be washed by the racer before the meeting at 2 pm. | Passive keeps agent |
| A:38142:c3 | B1 | L3 |  | correct/- | Вона вирішила вдягнути райдужний костюм із пір'я на чолі параду. | She decided she would wear a rainbow-coloured feather costume leading the parade. | Same meaning |
| A:3344:c4 | B2 | L3 |  | correct/- | Вона хоче віддати вкоротити зелений комбінезон до вечірки. | She wants the green jumpsuit shortened by the party. | Same meaning. |
| A:11681:c4 | A1 | L3:TIPrej |  | correct/- | Вона кладе на стіл одну стару батарейку. | She's putting an old battery on the table. | Same meaning. |
| A:12537:c3 | A1 | L3:TIPrej |  | correct/- | Маленький ґудзик лежить на дерев'яному столі. | A little button is on the wooden table. | Same meaning. |
| A:18309:c5 | A1 | L3:TIPrej |  | correct/- | Лев лягає в золоту траву. | A lion is lying down in golden grass. | Same meaning |
| A:36130:m | A2 | L3:TIPrej |  | wrong/M | Спокійний день, звісно: вона сьогодні по обіді збирається надрукувати п'ятдесят імейлів. | A calm day, of course: she is going to type fifty emails. | Only time phrase dropped |
| A:36274:c4 | A2 | L3:TIPrej |  | correct/- | Гонщик мав би помити мотоцикл до зустрічі о 14:00. | The racer should clean the motorcycle before the 2 o'clock meeting. | Same meaning |
| A:39243:c4 | B1 | L3:TIPrej |  | correct/- | Він полоскав ганчірку, коли помітив ще більше волосся на брудному дзеркалі. | While he was rinsing the rag, he noticed more hair on the dirty mirror. | Same meaning |
| A:600:c5 | B1 | L3:TIPrej |  | correct/- | «Оце так!» - крикнув коментатор. - Він крикнув, що ніколи не бачив такого стрибка. | The commentator yelled that he had never seen such a jump. | Only interjection 'Wow!' dropped. |
| A:44438:c4 | B2 | L3:TIPrej |  | correct/- | Чесно, до заходу сонця ти проїдеш на тому мотоциклі вертикально цілий кілометр. | Honestly, by sunset you'll be riding that motorcycle vertically for an entire kilometre. | Same meaning, future frame. |
| A:5578:c5 | B2 | L3:TIPrej |  | correct/- | Ще ніколи я не бачив, щоб корок вийшов у цій кухні так чисто. | Never have I watched a cork come out so cleanly in this kitchen. | Same meaning |

## 4. Judge noise (80 hidden duplicates per language)

- **de:** 80/80 agree, 0 disagree (0.00 % [0.00, 4.51]).
- **ua:** 79/80 agree, 1 disagreement (1.25 % [0.03, 6.77]): A:44381:c3 (B2, writer-correct) "They spun that dough … until the flour burst everywhere. A little messy." Its original in s4 was labelled wrong ("Added content everywhere"), and its duplicate in s1 was labelled correct ("Same meaning"). The original label (wrong) counts, so this item is also one of the ua FAs.
- **Writer intent vs judge label:**
  - de: 499/500 correct -> correct; 399/400 wrong -> wrong (1 T judged correct, 1 correct judged wrong).
  - ua: 494/500 correct -> correct; 398/400 wrong -> wrong (6 correct judged wrong; 1 M and 1 T judged correct).
- **es:** no labels. s1, s2 and s3 (the latter on its retry) were valid. s4 missed one jid three times: s4 missed j68edd and j8f71a and invented j8f711; s4_r1 missed j68edd; s4_r2 missed j19029.

## 5. Part F: app branch `translation-wave1` (no deploy, no push, no merge)

- **Commit 93b3f70** on top of 82c4059, in the worktree `~/Projects/and-again-wave1-wt`. Master (`~/Projects/and-again`) was not touched.
- **Routing:**
  - `WAVE1_ROUTED = ['de', 'ua']`, so `SOURCE_ONLY_NATIVE_LANGUAGES = sk, cz, de, ua`, for learning English only.
  - `lib/translateExercise.ts`: `TRANSLATE_SCOPE_RESTRICTED_NATIVES = ['sk', 'cz', 'de', 'ua']`, which replaces the hard-coded ['sk', 'cz'].
  - **Consequence:** de and ua learners of English now get the translate format ONLY on the 4,064 selected exercises, like sk/cz. The owner should confirm before a deploy.
  - es and all other pairs are unchanged.
- **Replay parity:** `sourceOnly.wave1.replay.test.ts` re-decides all 1,800 de+ua Part D items in the TS stack from the stored Gemini reply texts. **1,800/1,800 = 100 %** match Python on accept, layer and the content-check word.
  - Fixture: `scripts/translation-wave1/gen_replay_fixture.py`, which writes `fixtures/replay_wave1_partD.json` (no English reference, no labels).
  - A mutation check (one flipped accept) makes the test fail.
- **Routing tests updated:** `sourceOnly.wave1.test.ts`, `sourceOnly.stack.test.ts`, `lib/translateExercise.test.ts`.
- **Results:**
  - `npm test`: **427 pass, 0 fail** (425 before, plus 2 replay tests).
  - `npm run typecheck` (both tsc configs): **clean**, exit 0.
  - `deno check` was not run (no deno on this Mac).

## 6. Gemini calls and spend (counted = HTTP 200 only)

| lang | L3 | content check | counted total | failed-but-counted | non-200 | spend |
|---|---:|---:|---:|---:|---:|---:|
| de | 900 | 512 | 1,412 | 0 | 0 | $0.1350 |
| ua | 900 | 503 | 1,403 | 0 | 0 | $0.1378 |
| es | 0 | 0 | 0 | 0 | 0 | $0.0000 |
| **wave** | | | **2,815 of 5,000** | 0 | 0 | **$0.2728 of $1.50** |

No rate limit and no quota envelope occurred.

## 7. Claude tokens (budget 4,000,000)

The subagent figures are the `subagent_tokens` the harness reported for each subagent.

| language | writers | judges | total |
|---|---:|---:|---:|
| de | 135,339 | 216,779 | 352,118 |
| ua | 120,565 | 208,595 | 329,160 |
| es | 132,590 | 373,446 (7 sessions: s1, s2, s3, s3_r1, s4, s4_r1, s4_r2) | 506,036 |

- **Main session:** about 260,000 (estimate, own context).
- **Wave total:** about **1.45 M of 4.0 M**.
- Cumulative per stage, from `W1/<lang>/TOKENS.md`:
  - projection 0 (each language);
  - after the writers: de 135,339, ua 120,565, es 132,590;
  - after the judges: de 352,118, ua 329,160, es 452,991 before s4_r2 and 506,036 after it.

## 8. Defects recorded, NOT fixed

1. **es judge packet s4 lost one item in each of three Opus attempts.** Several items in that packet share one source sentence and differ only in the answer (for example "Él paga con monedas …" appears 4 times). A packet of 245 items is at the edge. Candidate fixes for a later run: smaller packets, or a deterministic "missing jids only" follow-up session.
2. **A third judge attempt `_r2` was added mid-wave** (after de and ua had finished and been frozen). It applies only when both earlier replies failed on the jid set alone, and it did not rescue es. It is recorded in `W1/es/PROGRESS.md` and t14.
3. **Chain bug:** the freeze check ran `git ls-tree` with a path relative to `wave1/`, which reported "freeze commit missing file" although the file was committed. It was fixed with `--full-tree`. de was frozen twice: first b783108, then 5507135. The set was not opened between the two freezes.
4. **Parallel preflights race on `W1/_test/`.** The first ua and es preflights failed when all three started at once. Re-run one after another, 14/14 pass.
5. **Blindness is by instruction, not by tool restriction.** `tx-opus` has Bash, Glob and Grep; the wrapper told each subagent to read only its prompt file. The wrapper also overrides the prompt's "Do not use any tools" line to allow that one Read and one Write. The retry wrappers added one clarifying sentence on copying jids exactly. The judge prompt text itself is byte-identical across all sessions.
6. **Judge labels to review:**
   - ua 27540 ("her" for Спортсмен … своїй, 2 FAs): does decision 22 extend to a masculine generic noun?
   - de 29199 ("Wow" judged as added content).
   - The ua duplicate disagreement A:44381:c3.
7. **Recurring FR pattern:** L3 rejects future-perfect renderings of German present or perfect with "bis / am Ende" (de 41807, 44823: 10 FRs) and of Ukrainian "мав би" (4 FRs).
8. **Scope consequence in Part F:** routing de and ua also restricts their translate format to the 4,064 selected exercises (as for sk/cz). This needs an owner decision before a deploy.
9. **Stale files:** `W1/<lang>/REPORT_<lang>.md` and `W1/TRANSLATION_WAVE1_DE_UA_ES_REPORT.md` describe the 22 Sept headless stop.
10. **Report location:** this report is committed on branch `translation-wave1` (worktree) and copied to `W1/`. It was not written into the master checkout, which another session is deploying from.
11. **Estimates:** the main-session token figure is an estimate. The per-level FA intervals are uninformative at n ≈ 100.

## 9. Judgement

1. **German and Ukrainian meet both targets on the point:**
   - de: coverage 94.4 %, FA 3.25 %;
   - ua: coverage 94.6 %, FA 2.7 %.
   - Ukrainian also meets both on the interval. German's FA upper bound is 5.49 %, so the interval target is missed.
2. **Spanish was not measured.** One judge packet repeatedly lost one item, so es stopped alone with its set unopened, at 0 Gemini cost. It can be resumed with a packet-level fix.
3. **The content check is what brings FA under 5 %.** It halves the L3-only FA (7.3 -> 3.3 % and 6.2 -> 2.7 %) for about 2 points of coverage. The remaining FAs are mostly dropped modifiers.
4. **The branch routes de and ua** with 100 % replay parity, npm test 427/427 and tsc clean. Nothing was deployed, pushed or merged, and no database row was written.
5. **Before a deploy, the owner should confirm two points:**
   - the scope restriction to the 4,064 selected exercises for de and ua;
   - the two judge-rule questions (decision 22 for masculine generic nouns, and "Wow" as added content).
