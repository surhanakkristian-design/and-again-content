You are the blind judge for a measurement of a translation checker.

Each packet item gives you a Slovak sentence, its CEFR level, its topic, and ONE English answer.
Judge that answer. You do NOT see who wrote it, whether it was meant to be right or wrong, or any
English reference translation.

ACCEPTANCE RULES (these are the owner's rules, verbatim, and they are the only
rules that decide):
- the Slovak sentence is the ground truth, not the English reference;
- a passive is acceptable;
- a dropped agent where the Slovak names one is WRONG;
- a missing obligatory English article is an ERROR;
- the time frame must match the Slovak while the English tense inside that frame is free;
- a dropped function word is correct, a dropped content word is wrong, added content is wrong.

Apply those rules and nothing else. In particular: do not mark an answer wrong for being a
passive, for wording you would not have chosen, or for a tense that keeps the Slovak time frame.

For every item output:
  "judged": "correct" or "wrong"
  "type":   null when correct; when wrong, exactly one of
            "T" (time frame does not match the Slovak),
            "S" (subject/agent wrong, or an agent the Slovak names is dropped),
            "M" (a content word the Slovak says is missing, or a missing obligatory article),
            "W" (wrong word choice, changed meaning, or added content)
  "borderline": true if you could argue it either way, otherwise false
  "confidence": an integer 1-5 (1 = a guess, 5 = certain)

Judge every item independently and on its own. Some Slovak sentences appear more than once with
different answers; that is normal and tells you nothing.

Write ONE file, judge/verdicts_part2.json, and nothing else. Exact JSON shape:
[{"jid": "q0001", "judged": "wrong", "type": "M", "borderline": false, "confidence": 4}, ...]
All 99 items, in the order given. No commentary; the file must parse as JSON.

THE PACKET:
{"jid": "q0100", "slovak": "Stále ukladal ďalšie knihy na kopu, kým sa nezakývala.", "level": "B1", "topic": "Gerund vs Infinitive", "answer": "He kept adding more books to the pile until it swayed."}
{"jid": "q0101", "slovak": "Pamätník zbožňoval, a samozrejme aj jeho fotoaparát.", "level": "B1", "topic": "So, Neither, Nor", "answer": "He will adore the monument, and so will his camera, of course."}
{"jid": "q0102", "slovak": "Katastrofa! Ona nemá čas na dlhú návštevu!", "level": "A2", "topic": "Countable and uncountable", "answer": "Disaster! She doesn't have time for long visit!"}
{"jid": "q0103", "slovak": "Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali.", "level": "B2", "topic": "All Past Tenses", "answer": "The submarine had been travelling under the surface for some time before it was noticed by the swimmers."}
{"jid": "q0104", "slovak": "Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "They need to get the old accordion fixed before the keys completely stop working."}
{"jid": "q0105", "slovak": "Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.", "level": "B2", "topic": "All Past Tenses", "answer": "By the time he reaches the narrow path, he will have been climbing down the rock ledges for an hour."}
{"jid": "q0106", "slovak": "Hore je vietor. Môžeš vidieť tú vlajku?", "level": "A1", "topic": "Modal verb CAN", "answer": "It's windy up there. Can you see flag?"}
{"jid": "q0107", "slovak": "Mäkká guma môže vyčistiť celú stranu.", "level": "A1", "topic": "Modal verb CAN", "answer": "Soft eraser can clean a whole page."}
{"jid": "q0108", "slovak": "Stupne víťazov boli postavené zo žineniek asi za minútu.", "level": "B1", "topic": "Passive or Active", "answer": "The victory podium was put together from gym mats in roughly a minute."}
{"jid": "q0109", "slovak": "Model stíhačky opeká chlieb približne tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The bread has been toasted by the model fighter jet for about three minutes."}
{"jid": "q0110", "slovak": "Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.", "level": "A2", "topic": "Present or Past Simple", "answer": "You usually hate queues, but last night you waited for toilet. Respect."}
{"jid": "q0111", "slovak": "Pred vhadzovaním si dala omotať hokejku páskou.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "Before the face-off, she will have her hockey stick wrapped with tape."}
{"jid": "q0112", "slovak": "Ten most preklenuje celý desivý kaňon, však?", "level": "B1", "topic": "Question tags", "answer": "The entire scary canyon is spanned by the bridge, isn't it?"}
{"jid": "q0113", "slovak": "On má sivú handričku na čistenie auta.", "level": "A1", "topic": "HAVE GOT", "answer": "He has got a grey cloth for cleaning the car."}
{"jid": "q0114", "slovak": "Vločky sú v miske – hneď ich zje", "level": "A2", "topic": "Going to or Will", "answer": "The flakes are in the bowl – he's going to eat them right away."}
{"jid": "q0115", "slovak": "Stojí bosý na teplom piesku.", "level": "A1", "topic": "Prepositions of place/time", "answer": "He is standing barefoot on the warm sand."}
{"jid": "q0116", "slovak": "Poprosila ma, aby som nehýbal rukou, kým spí.", "level": "B2", "topic": "Reported speech", "answer": "She asked me not to move my arm while she was sleeping."}
{"jid": "q0117", "slovak": "Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala.", "level": "B1", "topic": "Past Perfect Simple", "answer": "I won't lie, you were the most charming clerk; she never smiled like that before."}
{"jid": "q0118", "slovak": "Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa!", "level": "A1", "topic": "Prepositions of place/time", "answer": "She cleans the dirty floor on Monday morning. An absolute disaster!"}
{"jid": "q0119", "slovak": "Útok je rýchly a hlasný na zelenom poli.", "level": "A1", "topic": "TO BE", "answer": "The attack is fast and loud on the green field."}
{"jid": "q0120", "slovak": "Takže mi povedal, že v meste nejazdí veľkou rýchlosťou.", "level": "A2", "topic": "Much, Many, Some...", "answer": "So he told me that he doesn't drive at high speed in city."}
{"jid": "q0121", "slovak": "Dvaja kamaráti potrebujú dva hrebene", "level": "A1", "topic": "Singular and plural", "answer": "Two friends needed two combs."}
{"jid": "q0122", "slovak": "On má sivú handričku na čistenie auta.", "level": "A1", "topic": "HAVE GOT", "answer": "He has got a blue cloth for cleaning the car."}
{"jid": "q0123", "slovak": "Pamätník zbožňoval, a samozrejme aj jeho fotoaparát.", "level": "B1", "topic": "So, Neither, Nor", "answer": "He loved the memorial, and of course his camera did too."}
{"jid": "q0124", "slovak": "Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska.", "level": "B2", "topic": "Articles advanced", "answer": "They write their name on the last page of the contract for the old job and the office applauds."}
{"jid": "q0125", "slovak": "Stále ukladal ďalšie knihy na kopu, kým sa nezakývala.", "level": "B1", "topic": "Gerund vs Infinitive", "answer": "He keeps putting more books on the pile until it wobbles."}
{"jid": "q0126", "slovak": "Fakt, tvoje dve baterky pekne osvetľujú tú tmavú rímsu.", "level": "A1", "topic": "Singular and plural", "answer": "Really, your two flashlights light up those dark ledges nicely."}
{"jid": "q0127", "slovak": "Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala.", "level": "B1", "topic": "Past Perfect Simple", "answer": "I won't lie, you were most charming clerk; she had never smiled like that before."}
{"jid": "q0128", "slovak": "Ten most preklenuje celý desivý kaňon, však?", "level": "B1", "topic": "Question tags", "answer": "The bridge spans the whole beautiful canyon, doesn't it?"}
{"jid": "q0129", "slovak": "On kladie slaninu vedľa vajíčka do čiernej panvice.", "level": "B1", "topic": "Passive or Active", "answer": "The bacon is being put next to the egg into the black pan by him."}
{"jid": "q0130", "slovak": "Muž obdivuje svoje luxusné auto už dvadsať minút.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "His luxury car has been admired for twenty minutes."}
{"jid": "q0131", "slovak": "Úprimne, dnes si hlasnejší než celý národný tím.", "level": "A2", "topic": "Adjective comparison", "answer": "Honestly, today you're louder than the whole national team."}
{"jid": "q0132", "slovak": "On kladie slaninu vedľa vajíčka do čiernej panvice.", "level": "B1", "topic": "Passive or Active", "answer": "He is putting the bacon next to the egg in the pan."}
{"jid": "q0133", "slovak": "Stroj by si mal tlačiť veľmi pomaly.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "You should push the machine very slowly."}
{"jid": "q0134", "slovak": "Ten hmyz je drobný, tak ona by mala skúmať ho lupou.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "The bug is tiny, so she ought to examine it with a magnifying glass."}
{"jid": "q0135", "slovak": "Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "Roughly forty students have been asking for membership at the club fair since lunchtime."}
{"jid": "q0136", "slovak": "Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.", "level": "B2", "topic": "All Past Tenses", "answer": "By the time he reached the narrow path, the rocky ledges had been descended for an hour."}
{"jid": "q0137", "slovak": "Poprosila ma, aby som nehýbal rukou, kým spí.", "level": "B2", "topic": "Reported speech", "answer": "She asked me not to move my hand while she slept."}
{"jid": "q0138", "slovak": "On spal. Preto nič videl.", "level": "A2", "topic": "Past Simple", "answer": "He slept. That's why he did not see."}
{"jid": "q0139", "slovak": "Táto ceruzka je ostrejšia ako tá tupá.", "level": "A2", "topic": "Adjective comparison", "answer": "This pencil is sharper than the thin one."}
{"jid": "q0140", "slovak": "Na dunách je len jedna ťava.", "level": "A2", "topic": "There is, are", "answer": "There are only two camels on the dunes."}
{"jid": "q0141", "slovak": "Táto váha ukazuje oveľa viac ako pred chvíľou.", "level": "A1", "topic": "This, That, These...", "answer": "This scale shows a lot more."}
{"jid": "q0142", "slovak": "V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej.", "level": "B1", "topic": "Past Simple or Continuos", "answer": "The moment the crutch hit the wet floor, it was grabbed firmly and the walk carried on."}
{"jid": "q0143", "slovak": "Pamätník zbožňoval, a samozrejme aj jeho fotoaparát.", "level": "B1", "topic": "So, Neither, Nor", "answer": "The monument was adored by him, and of course by his camera too."}
{"jid": "q0144", "slovak": "Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe.", "level": "B2", "topic": "All Present Tenses", "answer": "Status update: the wardrobe has stayed tidy for 3 weeks in a row."}
{"jid": "q0145", "slovak": "Ryby majú plán. Idú uplávať preč od žraloka.", "level": "A2", "topic": "Future BE GOING TO", "answer": "The fish have a plan. They are going to swim toward the shark."}
{"jid": "q0146", "slovak": "Do obeda odovzdalo 200 voličov svoje volebné lístky, výrazne pred termínom.", "level": "B2", "topic": "All Past Tenses", "answer": "By noon, 200 voters had handed in their ballots, well ahead of the deadline."}
{"jid": "q0147", "slovak": "On má sivú handričku na čistenie auta.", "level": "A1", "topic": "HAVE GOT", "answer": "He had a grey cloth for cleaning the car."}
{"jid": "q0148", "slovak": "Žena mu na krk zavesí jednu zlatú medailu.", "level": "A1", "topic": "A, AN, THE", "answer": "The woman will hang a gold medal around his neck."}
{"jid": "q0149", "slovak": "V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej.", "level": "B1", "topic": "Past Simple or Continuos", "answer": "The moment the crutch hits the wet floor, he grabs it firmly and walks on."}
{"jid": "q0150", "slovak": "Fanúšik má jednu pomaľovanú tvár a šálu.", "level": "A1", "topic": "A, AN, THE", "answer": "A fan has one painted face and a scarf."}
{"jid": "q0151", "slovak": "Ryby majú plán. Idú uplávať preč od žraloka.", "level": "A2", "topic": "Future BE GOING TO", "answer": "The fish had a plan. They were going to swim away from the shark."}
{"jid": "q0152", "slovak": "Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa!", "level": "A1", "topic": "Prepositions of place/time", "answer": "She cleaned the dirty floor on Monday morning. An absolute disaster!"}
{"jid": "q0153", "slovak": "Pamätník zbožňoval, a samozrejme aj jeho fotoaparát.", "level": "B1", "topic": "So, Neither, Nor", "answer": "He adored the monument, and so did his camera, of course."}
{"jid": "q0154", "slovak": "Nebudem klamať, letíš vysoko, dokonca vyššie než borovice.", "level": "A2", "topic": "Adjective comparison", "answer": "I'm not going to lie, you fly high, even higher than the pine trees."}
{"jid": "q0155", "slovak": "Tieto konzervy vyletujú z jeho papierovej tašky.", "level": "A1", "topic": "This, That, These...", "answer": "These cans flew out of his paper bag."}
{"jid": "q0156", "slovak": "Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa!", "level": "A1", "topic": "Prepositions of place/time", "answer": "She cleans the dirty floor on Monday evening. An absolute disaster!"}
{"jid": "q0157", "slovak": "Nebudem klamať, letíš vysoko, dokonca vyššie než borovice.", "level": "A2", "topic": "Adjective comparison", "answer": "I won't lie, he is flying high, even higher than the pines."}
{"jid": "q0158", "slovak": "Stroj by si mal tlačiť veľmi pomaly.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "He should push the machine very slowly."}
{"jid": "q0159", "slovak": "Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.", "level": "B2", "topic": "All Past Tenses", "answer": "By the time he reached the narrow path, the rocky ledges had been descended for an hour."}
{"jid": "q0160", "slovak": "Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala.", "level": "B1", "topic": "Past Perfect Simple", "answer": "I won't lie, you were the most charming clerk; she had never smiled like that before."}
{"jid": "q0161", "slovak": "Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo.", "level": "B1", "topic": "Modal verbs Probability", "answer": "The guard can't know about cheese - he raises the ramp too quickly."}
{"jid": "q0162", "slovak": "Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký.", "level": "B2", "topic": "Modals in past", "answer": "Girl, he told me the iceberg was enormous; he must have felt so small there."}
{"jid": "q0163", "slovak": "Úprimne, dúha možno vybledne, ale zajtra v tomto čase budeš ukazovať svoje video všetkým.", "level": "B1", "topic": "Future Continuous", "answer": "Honestly, the rainbow may fade, but at this time yesterday you were showing your video to everyone."}
{"jid": "q0164", "slovak": "Stále ukladal ďalšie knihy na kopu, kým sa nezakývala.", "level": "B1", "topic": "Gerund vs Infinitive", "answer": "He kept on stacking more books onto the pile until it began to sway."}
{"jid": "q0165", "slovak": "On kladie slaninu vedľa vajíčka do čiernej panvice.", "level": "B1", "topic": "Passive or Active", "answer": "He is putting the bacon next to the egg in the black bowl."}
{"jid": "q0166", "slovak": "Dvaja kamaráti potrebujú dva hrebene", "level": "A1", "topic": "Singular and plural", "answer": "The two friends need two combs."}
{"jid": "q0167", "slovak": "Trénerka má obväz a bielu pásku.", "level": "A1", "topic": "HAVE GOT", "answer": "The coach has got bandage and white tape."}
{"jid": "q0168", "slovak": "Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali.", "level": "B2", "topic": "All Past Tenses", "answer": "The submarine had been moving under the surface for some time before it was spotted."}
{"jid": "q0169", "slovak": "Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "They need to have old accordion repaired before the keys stop working completely."}
{"jid": "q0170", "slovak": "Kdeže, gekón práve teraz chrlí oheň, lebo papričky sú také pálivé.", "level": "B2", "topic": "All Present Tenses", "answer": "No way, the gecko is spitting fire right now, because the chillies are so hot."}
{"jid": "q0171", "slovak": "Táto ceruzka je ostrejšia ako tá tupá.", "level": "A2", "topic": "Adjective comparison", "answer": "This pencil is sharper than the blunt one."}
{"jid": "q0172", "slovak": "Muž obdivuje svoje luxusné auto už dvadsať minút.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The man has been admiring his car for twenty minutes."}
{"jid": "q0173", "slovak": "Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký.", "level": "B2", "topic": "Modals in past", "answer": "Girl, he told me that the iceberg was huge; he must have felt so tiny there."}
{"jid": "q0174", "slovak": "Katastrofa! Ona nemá čas na dlhú návštevu!", "level": "A2", "topic": "Countable and uncountable", "answer": "Disaster! She doesn't have time for a long visit!"}
{"jid": "q0175", "slovak": "Stupne víťazov boli postavené zo žineniek asi za minútu.", "level": "B1", "topic": "Passive or Active", "answer": "The winners' podium will be built out of gym mats in about a minute."}
{"jid": "q0176", "slovak": "V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej.", "level": "B1", "topic": "Past Simple or Continuos", "answer": "The moment the crutch fell onto the wet floor, it was grabbed firmly by him and he went on."}
{"jid": "q0177", "slovak": "On má sivú handričku na čistenie auta.", "level": "A1", "topic": "HAVE GOT", "answer": "He has a gray rag for cleaning the car."}
{"jid": "q0178", "slovak": "Pri ľade kráčajú ďalšie dva tučniaky", "level": "A1", "topic": "Singular and plural", "answer": "Two more penguins are walking by ice."}
{"jid": "q0179", "slovak": "Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali.", "level": "B2", "topic": "All Past Tenses", "answer": "The submarine had been moving under the surface for some time before the swimmers spotted it."}
{"jid": "q0180", "slovak": "Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The fighter-jet toaster heated the same two slices three minutes ago."}
{"jid": "q0181", "slovak": "Pamätník zbožňoval, a samozrejme aj jeho fotoaparát.", "level": "B1", "topic": "So, Neither, Nor", "answer": "The monument was adored, and of course by his camera too."}
{"jid": "q0182", "slovak": "Poprosila ma, aby som nehýbal rukou, kým spí.", "level": "B2", "topic": "Reported speech", "answer": "She asked me not to move my arm."}
{"jid": "q0183", "slovak": "Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali.", "level": "B2", "topic": "All Past Tenses", "answer": "The submarine had been moving under the surface before the swimmers spotted it."}
{"jid": "q0184", "slovak": "On spal. Preto nič videl.", "level": "A2", "topic": "Past Simple", "answer": "He was asleep. Therefore he saw nothing."}
{"jid": "q0185", "slovak": "Ryby majú plán. Idú uplávať preč od žraloka.", "level": "A2", "topic": "Future BE GOING TO", "answer": "The fish have a plan. They are going to swim away from the shark."}
{"jid": "q0186", "slovak": "Žena mu na krk zavesí jednu zlatú medailu.", "level": "A1", "topic": "A, AN, THE", "answer": "A gold medal will be hung around his neck."}
{"jid": "q0187", "slovak": "Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa!", "level": "A1", "topic": "Prepositions of place/time", "answer": "On Monday morning she is cleaning the dirty floor. An absolute catastrophe!"}
{"jid": "q0188", "slovak": "Táto ceruzka je ostrejšia ako tá tupá.", "level": "A2", "topic": "Adjective comparison", "answer": "This pencil was sharper than the blunt one."}
{"jid": "q0189", "slovak": "Takže mi povedal, že v meste nejazdí veľkou rýchlosťou.", "level": "A2", "topic": "Much, Many, Some...", "answer": "So he told me that he doesn't drive at high speed in the city."}
{"jid": "q0190", "slovak": "Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The same two slices have been heated by the fighter-jet toaster for three minutes."}
{"jid": "q0191", "slovak": "Táto váha ukazuje oveľa viac ako pred chvíľou.", "level": "A1", "topic": "This, That, These...", "answer": "That scale shows a lot more than a moment ago."}
{"jid": "q0192", "slovak": "Útok je rýchly a hlasný na zelenom poli.", "level": "A1", "topic": "TO BE", "answer": "The attack was fast and loud on the green field."}
{"jid": "q0193", "slovak": "Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "They need to repair the old accordion themselves before the keys stop working completely."}
{"jid": "q0194", "slovak": "Nebudem klamať, letíš vysoko, dokonca vyššie než borovice.", "level": "A2", "topic": "Adjective comparison", "answer": "I wasn't going to lie, you were flying high, even higher than the pines."}
{"jid": "q0195", "slovak": "Do porady o 9:00 sa zotaví z takého vyčerpania.", "level": "B2", "topic": "All Future Tenses", "answer": "He'll have recovered from exhaustion like that before the 9:00 meeting."}
{"jid": "q0196", "slovak": "Fakt, tvoje dve baterky pekne osvetľujú tú tmavú rímsu.", "level": "A1", "topic": "Singular and plural", "answer": "Really, your two flashlights lit up that dark ledge nicely."}
{"jid": "q0197", "slovak": "Do porady o 9:00 sa zotaví z takého vyčerpania.", "level": "B2", "topic": "All Future Tenses", "answer": "By the 9:00 meeting, he will have recovered from such exhaustion."}
{"jid": "q0198", "slovak": "Útok je rýchly a hlasný na zelenom poli.", "level": "A1", "topic": "TO BE", "answer": "The attack is fast and loud on the green field."}
