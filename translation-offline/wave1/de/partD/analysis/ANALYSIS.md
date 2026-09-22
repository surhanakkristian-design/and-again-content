# Wave 1 Part D - German, fresh production set: analysis

Frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG); set opened once; truth = 4 opus judge sessions.

| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |
|---|---|---|---|---|
| pooled | 472/500 = 94.40 % [92.01, 96.25] | MET / MET | 13/400 = 3.25 % [1.74, 5.49] | MET / missed |
| A1 | 119/124 = 95.97 % [90.84, 98.68] | MET / MET | 3/101 = 2.97 % [0.62, 8.44] | MET / missed |
| A2 | 122/125 = 97.60 % [93.15, 99.50] | MET / MET | 3/100 = 3.00 % [0.62, 8.52] | MET / missed |
| B1 | 118/125 = 94.40 % [88.80, 97.72] | MET / missed | 3/100 = 3.00 % [0.62, 8.52] | MET / missed |
| B2 | 113/126 = 89.68 % [83.00, 94.39] | missed / missed | 4/99 = 4.04 % [1.11, 10.02] | MET / missed |

Both targets met on the point (pooled): True

Diagnostic, L3 only (before the content check): | L3 only | 483/500 = 96.60 % [94.61, 98.01] | MET / MET | 29/400 = 7.25 % [4.91, 10.25] | missed / missed |

Gemini: 1412 counted calls (HTTP 200; {'l3': 900, 'cc': 512}), 0 failed-but-counted, spend $0.134965; language ledger {'D_CC': 512, 'D_L3': 900}.

Judge noise (80 hidden duplicates, different sessions): 0/80 disagree = 0.0 % [0.0, 4.51].

## False rejections (28) by cause

by layer {'CC:MISSING': 11, 'L3': 13, 'L3:TIPrej': 4}; by writer {'correct/None': 28}; by level {'B1': 7, 'A2': 3, 'A1': 5, 'B2': 13}

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:6526:c5 | B1 | CC:MISSING | pflegte | correct/ | Als Kind pflegte sie, den Globus zu drehen und auf ein zufälliges Land zu tippen. | When she was little, she spun the globe and tapped on a random country. | Habitual past preserved. |
| A:8838:c4 | B1 | L3 |  | correct/ | Er hörte nicht auf, den Sack zu schlagen, bis er durch die Garage schwang. | He didn't stop punching the bag until it was swinging through the garage. | Same meaning. |
| A:8838:c5 | B1 | CC:MISSING | aufhören | correct/ | Er hörte nicht auf, den Sack zu schlagen, bis er durch die Garage schwang. | He kept on hitting the bag until it swung across the garage. | Same meaning. |
| A:23076:c5 | A2 | L3:TIPrej |  | correct/ | Die Wolken ziehen sehr langsam über den Himmel. | The clouds are moving slowly across the sky. | Dropped degree adverb acceptable. |
| A:32949:c4 | A1 | CC:MISSING | Gärtnerin | correct/ | Die Gärtnerin hat Werkzeug in ihren Schürzentaschen. | There are tools in the gardener's apron pockets. | Same meaning, different structure. |
| A:33109:c5 | A1 | L3 |  | correct/ | Die Führerin führt die Gruppe eine schmale Gasse hinunter. | The guide leads the group down a narrow side street. | Same meaning. |
| A:34130:c5 | A1 | CC:MISSING | küssen | correct/ | Sie sind alt, und sie küssen sich ewig! Einfach wunderschön! | They are old and they keep kissing forever! Absolutely beautiful! | Same meaning. |
| A:34858:c5 | A1 | L3:TIPrej |  | correct/ | Hilfe! Etwas ist in diesem dunklen Raum! | Help me! Something is in this dark room! | Idiomatic 'Help me!'; meaning preserved. |
| A:35377:c4 | A1 | L3:TIPrej |  | correct/ | Du sagst mit Blumen sorry. Respekt. | You say sorry with flowers. Respect to you. | Idiomatic rendering of 'Respekt'. |
| A:35589:c3 | A2 | CC:MISSING | Kraft | correct/ | Mit dieser Kraft wird sie bald den Gipfel erreichen. | With this kind of strength she is going to reach the top soon. | Same meaning. |
| A:35589:c5 | A2 | CC:MISSING | dieser | correct/ | Mit dieser Kraft wird sie bald den Gipfel erreichen. | With strength like this, she will soon get to the top. | Same meaning. |
| A:36872:c4 | B1 | CC:MISSING | niemanden | correct/ | Bei ihren früheren Rennen brauchte sie niemanden, der ihr im Ziel assistierte. | In her past races, she never needed anyone to assist her at the finish line. | Same meaning. |
| A:36949:c3 | B1 | CC:MISSING | herunter | correct/ | Während er durch die Galerie ging, fiel ihm vor Ehrfurcht die Kinnlade herunter. | While he was going through the gallery, his jaw fell in awe. | Meaning preserved, slightly unidiomatic. |
| A:36949:c5 | B1 | CC:MISSING | Ehrfurcht | correct/ | Während er durch die Galerie ging, fiel ihm vor Ehrfurcht die Kinnlade herunter. | While he walked through the gallery, his jaw dropped in amazement. | Same meaning. |
| A:40655:c4 | B2 | L3 |  | correct/ | Sie wartet im Bett, während die Flüssigkeit aus der braunen Flasche den Löffel füllt. | She is waiting in bed while the spoon fills with the liquid from the brown bottle. | Same meaning. |
| A:41628:c4 | B2 | CC:MISSING | so | correct/ | Bro, er wird diese Grube bis Sonnenuntergang so tief gegraben haben, dass er eine Leiter braucht, echt. | Bro, by sunset he will have dug this pit deep enough that he needs a ladder, really. | Same meaning. |
| A:41807:c1 | B2 | L3 |  | correct/ | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | By the end of the day, the colleagues will have been praising this graphic for about eight hours. | Same meaning. |
| A:41807:c2 | B2 | L3 |  | correct/ | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | At the end of the day the colleagues will have been praising this chart for roughly eight hours. | Same meaning. |
| A:41807:c3 | B2 | L3 |  | correct/ | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | By the end of the day the co-workers will have been praising this graphic for around eight hours. | Accurate translation. |
| A:41807:c4 | B2 | L3 |  | correct/ | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | By the end of the day, the colleagues will have praised this graphic for about eight hours. | Same meaning. |
| A:41807:c5 | B2 | L3 |  | correct/ | Am Ende des Tages loben die Kollegen diese Grafik seit ungefähr acht Stunden. | By the end of the day, this graphic will have been praised by the colleagues for about eight hours. | Passive keeps agent; same meaning. |
| A:42734:c3 | B1 | CC:MISSING | wieder | correct/ | Nächste Woche um diese Zeit machen sie in derselben Nische wieder einen geheimen Deal. | Next week at this time, they will be making another secret deal in the same nook. | Same meaning; another covers wieder. |
| A:44573:c5 | B2 | L3:TIPrej |  | correct/ | Hör mal, ich habe gehört, dass sie eine Stunde in der Schlange gewartet hatte, bevor sie endlich gewählt hat. | Listen, I heard she waited in line for an hour before she voted. | Same meaning; endlich drop acceptable. |
| A:44823:c1 | B2 | L3 |  | correct/ | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the ride, the tram's pantograph will have struck hundreds of sparks from the wire. | Accurate translation. |
| A:44823:c2 | B2 | L3 |  | correct/ | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the journey the pantograph of the tram will have knocked hundreds of sparks off the wire. | Same meaning and time frame. |
| A:44823:c3 | B2 | L3 |  | correct/ | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the trip, the tram's pantograph will have thrown hundreds of sparks from the wire. | Future reference preserved. |
| A:44823:c4 | B2 | L3 |  | correct/ | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the ride the streetcar's pantograph will have made hundreds of sparks fly from the wire. | Same meaning. |
| A:44823:c5 | B2 | L3 |  | correct/ | Bis zum Ende der Fahrt hat der Stromabnehmer der Straßenbahn Hunderte Funken aus dem Draht geschlagen. | By the end of the ride, hundreds of sparks will have been struck from the wire by the tram's pantograph. | Passive keeps the agent. |

## False acceptances (13) by cause

by layer {'L3+CC:NONE': 13}; by writer type {'W': 1, 'M': 7, 'T': 2, 'None': 1, 'S': 2}; by level {'B2': 4, 'B1': 3, 'A2': 3, 'A1': 3}

| aid | lvl | layer | cc | writer type | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:1391:w | B2 | L3+CC:NONE | none | W | Er schlug vor, die fertige Platte ins Schaufenster des Ateliers zu hängen. | She suggested hanging the finished plate in the studio's shop window. | She instead of he. |
| A:7123:m | B1 | L3+CC:NONE | none | M | Wenn Nina so weiterspielt, gibt der Trainer ihr auch die Kapitänsbinde. | If Nina keeps playing like this, the coach will give her the armband too. | Drops 'captain's' from armband. |
| A:16914:m | A2 | L3+CC:NONE | none | M | Schau! Sie fächelt sich gerade mit einem Papierfächer. | Look! She is fanning herself with a fan. | Drops 'paper' of paper fan. |
| A:23310:t | A1 | L3+CC:NONE | none | T | Die Schlange streckt uns ihre dünne Zunge entgegen. | The snake stuck its thin tongue out at us. | Past instead of present. |
| A:25234:m | A2 | L3+CC:NONE | none | M | Der Turm ist zu groß. Ich glaube, ich werde das aufräumen. | The tower is too big. I'll tidy that up. | Dropped main verb 'I think'. |
| A:29199:c4 | A1 | L3+CC:NONE | none | None | Wann benutzt du deine Kamera? Jeden Abend. Beeindruckend. | When do you use your camera? Each evening. Wow, impressive. | Added content 'Wow'. |
| A:34515:m | A2 | L3+CC:NONE | none | M | Bro, schau dir diese krasse Gischt an. Er wird klatschnass werden, ohne Witz. | Bro, look at this spray. He's going to get soaking wet, no joke. | Drops adjective krass. |
| A:35656:t | A1 | L3+CC:NONE | none | T | Ehrlich, du kannst zehn Sonnenblumen in zwei Armen tragen. Beeindruckend. | Honestly, you could carry ten sunflowers in two arms. Impressive. | 'could' changes present ability. |
| A:40435:m | B2 | L3+CC:NONE | none | M | Die Lagune erstreckt sich bis zum offenen Meer jenseits der Felswände. | The lagoon stretches to the sea beyond the cliffs. | Dropped adjective 'open'. |
| A:42849:s | B1 | L3+CC:NONE | none | S | Bro, der Jogger hat sich seinen Anteil Pizza genommen, und die Hundeausführerin auch, ohne Witz. | Bro, jogger took his share of pizza, and so did the dog walker, no joke. | Missing article before 'jogger'. |
| A:44395:s | B2 | L3+CC:NONE | none | S | Bro, ich wünschte, ich hätte so eine Tiefgarage, echt jetzt. | Bro, I wish I had a underground garage like that, seriously. | 'a underground' article error. |
| A:44573:m | B2 | L3+CC:NONE | none | M | Hör mal, ich habe gehört, dass sie eine Stunde in der Schlange gewartet hatte, bevor sie endlich gewählt hat. | Listen, I heard that she had waited for an hour before she finally voted. | Drops place phrase in line. |
| A:44700:m | B1 | L3+CC:NONE | none | M | Seine Waffe wurde ins Gras gesenkt! Es ist vorbei, komplett vorbei! | His weapon was lowered! It's over, completely over! | Drops 'into the grass'. |

## Judge duplicate disagreements

