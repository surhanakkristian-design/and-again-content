# Wave 1 Part D - French, fresh production set: analysis

Frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG); set opened once; truth = 4 opus judge sessions.

| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |
|---|---|---|---|---|
| pooled | 480/499 = 96.19 % [94.12, 97.69] | MET / MET | 13/401 = 3.24 % [1.74, 5.48] | MET / missed |
| A1 | 120/125 = 96.00 % [90.91, 98.69] | MET / MET | 4/100 = 4.00 % [1.10, 9.93] | MET / missed |
| A2 | 125/125 = 100.00 % [97.09, 100.00] | MET / MET | 2/100 = 2.00 % [0.24, 7.04] | MET / missed |
| B1 | 114/124 = 91.94 % [85.67, 96.06] | MET / missed | 3/101 = 2.97 % [0.62, 8.44] | MET / missed |
| B2 | 121/125 = 96.80 % [92.01, 99.12] | MET / MET | 4/100 = 4.00 % [1.10, 9.93] | MET / missed |

Both targets met on the point (pooled): True

Diagnostic, L3 only (before the content check): | L3 only | 488/499 = 97.80 % [96.09, 98.89] | MET / MET | 31/401 = 7.73 % [5.31, 10.79] | missed / missed |

Gemini: 1419 counted calls (HTTP 200; {'l3': 900, 'cc': 519}), 0 failed-but-counted, spend $0.141787; language ledger {'D_CC': 519, 'D_L3': 900}.

Judge noise (80 hidden duplicates, different sessions): 0/80 disagree = 0.0 % [0.0, 4.51].

## False rejections (19) by cause

by layer {'CC:MISSING': 8, 'L3:TIPrej': 8, 'L3': 3}; by writer {'correct/None': 19}; by level {'B1': 10, 'B2': 4, 'A1': 5}

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:4298:c4 | B1 | CC:MISSING | Si | correct/ | Si tu perds tes clés dans un sac de cette taille, la panique arrive en deux secondes. | When you lose your keys in a bag that size, the panic comes in two seconds. | Same meaning |
| A:8454:c2 | B1 | CC:MISSING | détruite | correct/ | Cette eau a été détruite par un seul homme en une dizaine de secondes. | This water was ruined by one man in around ten seconds. | Same meaning, agent kept |
| A:9934:c5 | B1 | L3:TIPrej |  | correct/ | Pendant qu'elle pendait là, son amie s'est glissée sous elle. | While she was dangling there, his friend slid under her. | Son is genderless; his allowed |
| A:10008:c4 | B2 | L3:TIPrej |  | correct/ | Il aimerait que l'enflure disparaisse avant le match. | He hopes the swelling goes down before the game. | Close equivalent meaning |
| A:11170:c4 | A1 | L3 |  | correct/ | Un animal est gris, mais les autres animaux sont colorés. | One of the animals is grey, while the other animals are brightly coloured. | Same meaning. |
| A:14409:c2 | A1 | L3:TIPrej |  | correct/ | Il y a six verres sur la table. | Six glasses are on the table. | Same meaning. |
| A:15333:c5 | A1 | L3:TIPrej |  | correct/ | Elle met sa main au-dessus de ses yeux. | She places a hand above her eyes. | Same meaning; article choice free |
| A:21392:c5 | A1 | L3 |  | correct/ | Elle montre à droite après les stands. | She shows the way to the right after the booths. | Same meaning |
| A:36196:c3 | A1 | CC:MISSING | maison | correct/ | Les enfants font signe depuis leur maison au village. | The children wave from their village house. | Same meaning |
| A:37187:c5 | B1 | L3:TIPrej |  | correct/ | Si la poubelle n'était pas si profonde, le raton laveur sortirait facilement. | If the dustbin wasn't this deep, the racoon would escape easily. | Same meaning |
| A:37755:c2 | B1 | CC:MISSING | celle-là | correct/ | Le garçon a dit qu'il n'avait jamais entendu d'acclamation aussi forte que celle-là. | The boy said that he'd never heard such a loud cheer. | Same meaning |
| A:37755:c3 | B1 | CC:MISSING | celle-là | correct/ | Le garçon a dit qu'il n'avait jamais entendu d'acclamation aussi forte que celle-là. | The boy said he had never heard a cheer that loud. | Same meaning. |
| A:38440:c3 | B1 | L3:TIPrej |  | correct/ | La poule a défendu ses poussins toute la nuit, donc elle est restée éveillée toute la nuit. | The hen has been defending its chicks all night, so it has stayed awake all night. | Same meaning; tense free. |
| A:38934:c5 | B2 | CC:MISSING | prennent fin | correct/ | Nulle part sur la gravure les dunes infinies ne prennent fin. | In the engraving, the endless dunes end nowhere. | Same meaning. |
| A:40548:c5 | B1 | L3:TIPrej |  | correct/ | Pendant qu'elle s'appuyait sur la rambarde du pont, son partenaire a enregistré 5 km sur l'objectif hebdomadaire. | While she leaned on the bridge railing, his partner clocked 5 km towards the weekly target. | Genderless 'son' allows his |
| A:40913:c3 | B2 | L3:TIPrej |  | correct/ | Elle était restée assise sur le matelas dur pendant une minute avant de crier que c'était une catastrophe ! | She sat on the hard mattress for a minute before shouting it was a catastrophe! | Past frame kept |
| A:41379:c5 | B1 | CC:MISSING | avait l'habitude de | correct/ | Enfant, elle avait l'habitude de tenir ses paumes au-dessus des feux de plage chaque été. | When she was little, she held her palms above the beach fires every summer. | Habitual past kept. |
| A:42755:c2 | B2 | L3 |  | correct/ | Le vendeur versait du thé depuis une heure quand les jeunes ont commencé à le filmer. | The vendor had poured tea for an hour when the young people started to film him. | Past frame kept; tense free. |
| A:42785:c5 | B1 | CC:MISSING | tu | correct/ | Si tu entretiens une voiture régulièrement, elle dure plus longtemps. | If a car is maintained regularly, it lasts longer. | Generic 'tu' not a named agent |

## False acceptances (13) by cause

by layer {'L3+CC:NONE': 13}; by writer type {'T': 6, 'M': 5, 'None': 1, 'W': 1}; by level {'A1': 4, 'A2': 2, 'B1': 3, 'B2': 4}

| aid | lvl | layer | cc | writer type | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:23662:t | A1 | L3+CC:NONE | none | T | À chaque cours de sciences, il apprend des choses sur l'espace. | In every science class, he learned things about space. | Past time frame instead of present |
| A:24603:t | A1 | L3+CC:NONE | none | T | Quel t-shirt choisit-il ? Le bleu canard. | Which T-shirt did he choose? The teal one. | Past time frame; French is present |
| A:34791:m | A2 | L3+CC:NONE | none | M | Devine quoi, apparemment ce mec riche ne cuisine jamais, mais là, il est en train de faire frire des poivrons. | Guess what, apparently this guy never cooks, but right now he's frying peppers. | Dropped adjective 'riche'. |
| A:35597:t | A2 | L3+CC:NONE | none | T | Évaluation de performance : elle balance le kettlebell de 20 kg fortement. | Performance review: she swung the 20 kg kettlebell strongly. | Past time frame instead of present |
| A:35730:t | A1 | L3+CC:NONE | none | T | Où les plongeurs nagent-ils ? Vers la surface ensoleillée, tout en haut. | Where were the divers swimming? Towards the sunny surface, right at the top. | Past time frame instead of present |
| A:36196:t | A1 | L3+CC:NONE | none | T | Les enfants font signe depuis leur maison au village. | The children waved from their house in the village. | Present time frame changed to past. |
| A:37488:c4 | B1 | L3+CC:NONE | none | None | Si l'entraîneur lui étire le mollet, le joueur sera bientôt de retour sur le terrain. | If the coach stretches her calf, the player will be back on the pitch before long. | 'her' refers to masculine le joueur. |
| A:38324:m | B2 | L3+CC:NONE | none | M | Les individus au centre souhaitent vraisemblablement que les autres se serrent moins. | The individuals probably wish that the others would squeeze together less. | Dropped place phrase 'in the centre' |
| A:38934:m | B2 | L3+CC:NONE | none | M | Nulle part sur la gravure les dunes infinies ne prennent fin. | Nowhere in the engraving do the dunes come to an end. | Dropped adjective 'infinies' (endless). |
| A:38934:t | B2 | L3+CC:NONE | none | T | Nulle part sur la gravure les dunes infinies ne prennent fin. | Nowhere in the engraving did the endless dunes come to an end. | Present time frame changed to past. |
| A:38934:w | B2 | L3+CC:NONE | none | W | Nulle part sur la gravure les dunes infinies ne prennent fin. | Nowhere in the painting do the endless dunes come to an end. | Painting instead of engraving. |
| A:40548:m | B1 | L3+CC:NONE | none | M | Pendant qu'elle s'appuyait sur la rambarde du pont, son partenaire a enregistré 5 km sur l'objectif hebdomadaire. | While she was leaning on the railing, her partner logged 5 km towards the weekly goal. | Drops 'bridge' from the railing. |
| A:43045:m | B1 | L3+CC:NONE | none | M | Clairement un chef-d'œuvre : ce panneau a été peint à la main il y a environ cent ans. | Clearly a masterpiece: this sign was painted about a hundred years ago. | Drops 'by hand'. |

## Judge duplicate disagreements

