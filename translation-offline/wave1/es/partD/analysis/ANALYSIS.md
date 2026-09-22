# Wave 1 Part D - Spanish, fresh production set: analysis

Frozen stack (L3 SOURCE-ONLY + content check, TIP rejected, no F4/AG); set opened once; truth = 4 opus judge sessions.

| block | coverage (accepted / judge-correct) CP95 | >= 90 % point / interval | FA (accepted / judge-wrong) CP95 | < 5 % point / interval |
|---|---|---|---|---|
| pooled | 453/490 = 92.45 % [89.74, 94.63] | MET / missed | 12/410 = 2.93 % [1.52, 5.06] | MET / missed |
| A1 | 105/118 = 88.98 % [81.90, 94.00] | missed / missed | 4/107 = 3.74 % [1.03, 9.30] | MET / missed |
| A2 | 115/122 = 94.26 % [88.54, 97.66] | MET / missed | 4/103 = 3.88 % [1.07, 9.65] | MET / missed |
| B1 | 118/124 = 95.16 % [89.77, 98.20] | MET / missed | 4/101 = 3.96 % [1.09, 9.83] | MET / missed |
| B2 | 115/126 = 91.27 % [84.92, 95.56] | MET / missed | 0/99 = 0.00 % [0.00, 3.66] | MET / MET |

Both targets met on the point (pooled): True

Diagnostic, L3 only (before the content check): | L3 only | 469/490 = 95.71 % [93.52, 97.33] | MET / MET | 30/410 = 7.32 % [4.99, 10.28] | missed / missed |

Gemini: 1399 counted calls (HTTP 200; {'l3': 900, 'cc': 499}), 0 failed-but-counted, spend $0.134641; language ledger {'D_CC': 499, 'D_L3': 900}.

Judge noise (80 hidden duplicates, different sessions): 3/80 disagree = 3.75 % [0.78, 10.57].

## False rejections (37) by cause

by layer {'CC:MISSING': 16, 'L3:TIPrej': 14, 'L3': 7}; by writer {'correct/None': 36, 'wrong/W': 1}; by level {'B2': 11, 'B1': 6, 'A1': 13, 'A2': 7}

| aid | lvl | layer | cc word | writer | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:1426:c2 | B2 | CC:MISSING | mantequilla | correct/ | Para cuando esté cubierta la última esquina, él habrá estado untando mantequilla durante un minuto entero. | By the time the last corner has been covered, he'll have been buttering for an entire minute. | Same meaning. |
| A:1426:c4 | B2 | CC:MISSING | mantequilla | correct/ | Para cuando esté cubierta la última esquina, él habrá estado untando mantequilla durante un minuto entero. | By the time the final corner is covered, he will have been buttering for a whole minute. | Accurate translation. |
| A:4531:c5 | B1 | L3:TIPrej |  | correct/ | Mañana a esta hora ella lo estará regañando por algo completamente distinto, seguramente las gallinas. | This time tomorrow she'll scold him for something different, probably the chickens. | Dropped degree adverb acceptable |
| A:13052:c2 | A1 | CC:MISSING | Hay | correct/ | Hay dos boles de cereales en la mesa. | Two bowls of cereal are on the table. | Same meaning. |
| A:13896:c4 | A1 | CC:MISSING | calma | correct/ | Este té caliente le calma la garganta irritada. | This hot tea is soothing her irritated throat. | Same meaning, present frame. |
| A:16173:c2 | A1 | CC:MISSING | pela | correct/ | Ella pela tres dientes blancos para la sartén. | She is peeling three white cloves for the frying pan. | Accurate translation. |
| A:16173:c5 | A1 | L3:TIPrej |  | correct/ | Ella pela tres dientes blancos para la sartén. | She's peeling three white cloves for the pan. | Faithful translation. |
| A:17154:c4 | A2 | L3:TIPrej |  | correct/ | Él se lamió el dedo porque la miel estaba muy pegajosa. | He licked the finger because the honey was very sticky. | Accurate |
| A:17871:c5 | A2 | CC:MISSING | quieta | correct/ | Ahora vuela, pero hace un segundo estaba quieta. | It's flying now, but it was still a second ago. | Faithful translation. |
| A:24801:c1 | A1 | L3 |  | correct/ | Mira la luna con el telescopio. | He looks at the moon with the telescope. | Faithful translation. |
| A:24801:c3 | A1 | L3:TIPrej |  | correct/ | Mira la luna con el telescopio. | He is looking at the moon with the telescope. | Genderless subject; faithful. |
| A:24801:c4 | A1 | L3:TIPrej |  | correct/ | Mira la luna con el telescopio. | She watches the moon with the telescope. | Genderless subject; same meaning |
| A:24801:c5 | A1 | L3:TIPrej |  | correct/ | Mira la luna con el telescopio. | He looks at the moon through a telescope. | Faithful translation. |
| A:26017:c3 | A2 | CC:MISSING | despertarte | correct/ | Para despertarte a las seis necesitas mucha energía. | To get up at six o'clock, you need a lot of energy. | Faithful translation. |
| A:27345:c5 | A2 | L3 |  | correct/ | Tío, él cepilló esa piedra antigua súper suavemente, en serio. | Dude, he has brushed that old stone super gently, seriously. | Past event kept; tense free within frame. |
| A:29399:c4 | A2 | CC:MISSING | volver | correct/ | Todo un profesional. Va a llevar la margarita a casa sin volver a caerse. | Quite the professional. He's gonna carry the daisy home without falling again. | Same meaning |
| A:32847:c4 | A1 | L3:TIPrej |  | correct/ | 2 perros están tumbados en el suelo junto a la nevera. | Two dogs lie on the floor next to the fridge. | Accurate |
| A:34092:c3 | A2 | CC:MISSING | levantado | correct/ | Amiga, ella se ha levantado con la nota, así que al parecer va a preguntar a todo el mundo. | Girl, she stood up with the note, so it seems she's going to ask everyone. | Same meaning; tense free. |
| A:34288:c3 | A1 | L3:TIPrej |  | correct/ | Tío, ¿puedo yo pagar con tarjeta? Necesito ese perrito caliente sí o sí. | Mate, can I pay by card? I really need that hot dog. | Same meaning. |
| A:34768:c3 | A1 | CC:MISSING | revelan | correct/ | Actualización trimestral: las puertas revelan una vista que vale 2 millones de euros. | Quarterly update: the doors open onto a view worth 2 million euros. | Same meaning. |
| A:34933:c5 | A1 | L3 |  | correct/ | ¡Él lleva su bufanda de la suerte en cada partido, para siempre! | He puts on his lucky scarf for every match, forever! | Same meaning |
| A:35277:c2 | A1 | CC:MISSING | acerca | correct/ | Ella acerca las flores a su nariz para olerlas. | She holds the flowers up to her nose to smell them. | Same meaning |
| A:36179:c4 | A2 | L3:TIPrej |  | correct/ | No voy a mentir, tú picas tantas verduras en segundos. | I'm not going to lie, you chop that many vegetables in a matter of seconds. | Accurate |
| A:38581:c4 | B2 | L3:TIPrej |  | correct/ | Vale, él me dijo que había estado usando este detergente durante semanas antes de que por fin funcionara. | Okay, he told me he had used this detergent for weeks before it worked. | Dropped 'por fin' acceptable; meaning kept |
| A:38585:c4 | B2 | CC:MISSING | cada | correct/ | Para medianoche, ella habrá desenchufado todos y cada uno de los aparatos del piso. ¡Absolutamente todo se apaga! | By midnight she will have unplugged all the appliances in the apartment. Every last thing goes off! | Same meaning. |
| A:38714:c5 | B1 | CC:MISSING | esquivó | correct/ | Él esquivó cada intento de agarrarlo hasta que ella lo acorraló junto al sofá. | He dodged every try to grab him until he was cornered by her next to the sofa. | Passive keeps agent; meaning kept |
| A:39259:c3 | B2 | CC:MISSING | montar | correct/ | ¡Dicen que su pobre dedo se quedó atrapado en la mesa de montar! ¡Lo peor de lo peor! | It's said that her poor finger was trapped in the assembly table! Worst of the worst! | Same meaning. |
| A:39259:w | B2 | L3 |  | wrong/W | ¡Dicen que su pobre dedo se quedó atrapado en la mesa de montar! ¡Lo peor de lo peor! | They say her poor toe got stuck in the assembly table! The worst of the worst! | Dedo can mean toe; same meaning. |
| A:39323:c5 | B2 | L3:TIPrej |  | correct/ | Amiga, él me dijo que ojalá hubiera arreglado ese fregadero la semana pasada, no hoy. | Girl, he told me he wishes he had fixed that sink last week instead of today. | Same meaning. |
| A:40144:c5 | B2 | L3 |  | correct/ | Tío, él debería haber comprado menos plantas de interior, no hay espacio, bro. | Dude, he shouldn't have bought so many houseplants, there's no room, bro. | Same meaning. |
| A:41556:c5 | B1 | L3:TIPrej |  | correct/ | Bro, para cuando él salió a la superficie, sus amigos también habían saltado del muelle, en serio. | Bro, by the time he surfaced, her friends had also leapt off the pier, seriously. | Genderless 'sus' allows her; meaning kept |
| A:41984:c5 | B1 | CC:MISSING | solía | correct/ | Esta pirámide solía ser el centro de una ciudad para miles de personas, según el informe turístico. | This pyramid was the centre of a city for thousands of people, according to the tourist report. | Same past meaning. |
| A:42156:c2 | B2 | CC:MISSING | recordado | correct/ | Escucha, al parecer él había recordado cada tarjeta antes de dar un puñetazo al aire. | Listen, apparently he'd memorized every card before he punched the air. | Same meaning. |
| A:42156:c5 | B2 | L3 |  | correct/ | Escucha, al parecer él había recordado cada tarjeta antes de dar un puñetazo al aire. | Listen, apparently he had learned every card by heart before punching the air. | Memorised card meaning preserved. |
| A:42673:c3 | B1 | L3:TIPrej |  | correct/ | El hombre le ha rascado el pecho al canguro tres veces, y quiere una cuarta. | The man scratched the kangaroo's chest three times, and wants a fourth. | Accurate, tense free |
| A:43775:c5 | B1 | L3:TIPrej |  | correct/ | La puesta de sol ha teñido todo el aparcamiento de naranja; ¡parece que el mundo está en llamas! | The sunset turned the whole parking lot orange; it looks like the world is in flames! | Same past time frame; tense free. |
| A:43998:c4 | B2 | L3 |  | correct/ | Sus lágrimas han estado inundando el suelo desde hace un minuto entero. Una reacción tranquila, obviamente. | Her tears have flooded the floor for a whole minute. A calm reaction, obviously. | Present frame kept; same meaning. |

## False acceptances (12) by cause

by layer {'L3+CC:NONE': 12}; by writer type {'T': 2, 'M': 4, 'None': 6}; by level {'A1': 4, 'A2': 4, 'B1': 4}

| aid | lvl | layer | cc | writer type | source | answer | judge reason |
|---|---|---|---|---|---|---|---|
| A:13083:t | A1 | L3+CC:NONE | none | T | ¿Qué cierran con la cadena? | What did they close with the chain? | Past instead of present frame. |
| A:27345:m | A2 | L3+CC:NONE | none | M | Tío, él cepilló esa piedra antigua súper suavemente, en serio. | Dude, he brushed that stone super gently, seriously. | Dropped adjective antigua. |
| A:29399:c2 | A2 | L3+CC:NONE | none | None | Todo un profesional. Va a llevar la margarita a casa sin volver a caerse. | A true pro. She is going to carry the daisy home without falling over again. | Masculine 'profesional' requires he, not she. |
| A:29399:c5 | A2 | L3+CC:NONE | none | None | Todo un profesional. Va a llevar la margarita a casa sin volver a caerse. | A complete professional. She's going to take the daisy back home without falling again. | Masculine 'un profesional' requires he, not she |
| A:34288:c5 | A1 | L3+CC:NONE | none | None | Tío, ¿puedo yo pagar con tarjeta? Necesito ese perrito caliente sí o sí. | Man, can I pay by credit card? I have to have that hot dog no matter what. | Added 'credit' not in Spanish. |
| A:34651:c2 | A2 | L3+CC:NONE | none | None | ¡Ni un autobús, el peor día de mi vida! ¡Vale, yo leeré mi libro aquí! | Not one bus, worst day of my life! Fine, I will read my book here! | Missing article before 'worst day'. |
| A:35387:t | A1 | L3+CC:NONE | none | T | Oye, tú puedes oír el sonido de ese radiocasete desde la calle de al lado, tío. | Hey, you could hear the sound of that radio cassette player from the next street, man. | 'could' shifts present ability to past |
| A:35803:c3 | A1 | L3+CC:NONE | none | None | La profesora sostiene su bolígrafo, así que está en su mano. | The teacher holds his pen, so it is in his hand. | La profesora is female; his misassigns possessor. |
| A:36739:c4 | B1 | L3+CC:NONE | none | None | Tú estabas terminando la manzana cuando llegó esa hamburguesa gigante, y sinceramente, tu apetito es icónico. | You were just finishing the apple when that enormous burger arrived, and honestly your appetite is iconic. | Added 'just' not in Spanish. |
| A:36739:m | B1 | L3+CC:NONE | none | M | Tú estabas terminando la manzana cuando llegó esa hamburguesa gigante, y sinceramente, tu apetito es icónico. | You were finishing the apple when that burger arrived, and honestly, your appetite is iconic. | Dropped adjective 'giant'. |
| A:41860:m | B1 | L3+CC:NONE | none | M | El funcionario dijo que ese día serían liberados 12 hombres de la prisión, como mostraba el informe. | The official said that 12 men would be released that day, as the report showed. | Dropped 'from the prison'. |
| A:43835:m | B1 | L3+CC:NONE | none | M | Las flores la sorprendieron porque ella no las esperaba, y yo tampoco. | They surprised her because she wasn't expecting them, and neither was I. | Dropped noun las flores. |

## Judge duplicate disagreements

- A:32586:c4 (A1, correct/None) s1 wrong vs s2 correct: "Dandelions have white seeds for the wind to carry."
- A:34288:c4 (A1, correct/None) s5 wrong vs s6 correct: "Dude, can I pay with card? I absolutely need that hot dog."
- A:34651:c2 (A2, correct/None) s8 wrong vs s3 correct: "Not one bus, worst day of my life! Fine, I will read my book here!"
