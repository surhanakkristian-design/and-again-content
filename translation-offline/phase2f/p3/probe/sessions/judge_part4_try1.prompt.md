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

Write ONE file, judge/verdicts_part4.json, and nothing else. Exact JSON shape:
[{"jid": "q0001", "judged": "wrong", "type": "M", "borderline": false, "confidence": 4}, ...]
All 99 items, in the order given. No commentary; the file must parse as JSON.

THE PACKET:
{"jid": "q0298", "slovak": "Katastrofa! Ona nemá čas na dlhú návštevu!", "level": "A2", "topic": "Countable and uncountable", "answer": "A disaster! She hasn't got time for a long visit!"}
{"jid": "q0299", "slovak": "Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska.", "level": "B2", "topic": "Articles advanced", "answer": "They write their name on the last page of the contract for the new job and it is applauded."}
{"jid": "q0300", "slovak": "Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký.", "level": "B2", "topic": "Modals in past", "answer": "Girl, I was told by him that the iceberg was huge; he must have felt so tiny there."}
{"jid": "q0301", "slovak": "Stojí bosý na teplom piesku.", "level": "A1", "topic": "Prepositions of place/time", "answer": "He is standing barefoot on the cold sand."}
{"jid": "q0302", "slovak": "Už päť minút hľadá gumičku do vlasov a na zápästí má tri.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "She has been looking for a hair tie for five minutes and has two on her wrist."}
{"jid": "q0303", "slovak": "Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali.", "level": "B2", "topic": "All Past Tenses", "answer": "The submarine will have been moving under the surface for some time before the swimmers spot it."}
{"jid": "q0304", "slovak": "Stroj by si mal tlačiť veľmi pomaly.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "You should push the machine slowly."}
{"jid": "q0305", "slovak": "Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo.", "level": "B1", "topic": "Modal verbs Probability", "answer": "The guard couldn't know about the cheese - he was raising the ramp too quickly."}
{"jid": "q0306", "slovak": "Správa: oni zvyčajne dávajú pohľadnice, ale včera jej oni dali 12 darčekov.", "level": "A2", "topic": "Present or Past Simple", "answer": "Message: they usually give postcards, but yesterday they gave her 12 gifts."}
{"jid": "q0307", "slovak": "Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.", "level": "B2", "topic": "All Past Tenses", "answer": "Before he got to the narrow trail, he had spent an hour descending the rocky ledges."}
{"jid": "q0308", "slovak": "Model stíhačky opeká chlieb približne tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The model fighter jet has been toasting the bread for three minutes."}
{"jid": "q0309", "slovak": "Stroj by si mal tlačiť veľmi pomaly.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "He should push the machine very slowly."}
{"jid": "q0310", "slovak": "Fakt, tvoje dve baterky pekne osvetľujú tú tmavú rímsu.", "level": "A1", "topic": "Singular and plural", "answer": "Seriously, that dark ledge is lit up nicely by your two flashlights."}
{"jid": "q0311", "slovak": "Už päť minút hľadá gumičku do vlasov a na zápästí má tri.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "She has been looking for a hair tie for five minutes and she has three on her wrist."}
{"jid": "q0312", "slovak": "Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska.", "level": "B2", "topic": "Articles advanced", "answer": "They write their name on last page of the contract for the new job and the office applauds."}
{"jid": "q0313", "slovak": "Pred vhadzovaním si dala omotať hokejku páskou.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "Before the face-off, she wrapped her hockey stick with tape herself."}
{"jid": "q0314", "slovak": "Fanúšik má jednu pomaľovanú tvár a šálu.", "level": "A1", "topic": "A, AN, THE", "answer": "The fan had one painted face and a scarf."}
{"jid": "q0315", "slovak": "Kamarát tvrdil, že sa ho celý večer nikto nedotkol.", "level": "B2", "topic": "Reported speech", "answer": "It was claimed that nobody had touched him all evening."}
{"jid": "q0316", "slovak": "Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky.", "level": "A2", "topic": "Basic conjunctions", "answer": "Listen, she said they have the same dress, so they're still friends."}
{"jid": "q0317", "slovak": "Správa: oni zvyčajne dávajú pohľadnice, ale včera jej oni dali 12 darčekov.", "level": "A2", "topic": "Present or Past Simple", "answer": "The message: they usually hand out postcards, but yesterday they gave her twelve presents."}
{"jid": "q0318", "slovak": "Fakt, tvoje dve baterky pekne osvetľujú tú tmavú rímsu.", "level": "A1", "topic": "Singular and plural", "answer": "Honestly, your two torches are lighting that dark ledge up nicely."}
{"jid": "q0319", "slovak": "Úprimne, dúha možno vybledne, ale zajtra v tomto čase budeš ukazovať svoje video všetkým.", "level": "B1", "topic": "Future Continuous", "answer": "To be honest, the rainbow may fade, but tomorrow at this time you are going to be showing your video to everybody."}
{"jid": "q0320", "slovak": "Na dunách je len jedna ťava.", "level": "A2", "topic": "There is, are", "answer": "There is only one camel on the dunes."}
{"jid": "q0321", "slovak": "Ryby majú plán. Idú uplávať preč od žraloka.", "level": "A2", "topic": "Future BE GOING TO", "answer": "The fish have plan. They are going to swim away from the shark."}
{"jid": "q0322", "slovak": "Pri ľade kráčajú ďalšie dva tučniaky", "level": "A1", "topic": "Singular and plural", "answer": "By the ice, another two penguins are walking."}
{"jid": "q0323", "slovak": "Útok je rýchly a hlasný na zelenom poli.", "level": "A1", "topic": "TO BE", "answer": "Attack is fast and loud on the green field."}
{"jid": "q0324", "slovak": "Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.", "level": "B2", "topic": "All Past Tenses", "answer": "By the time he reached the narrow path, he had been climbing down the ledges for an hour."}
{"jid": "q0325", "slovak": "Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "About forty students have been applying for membership at the club fair since noon."}
{"jid": "q0326", "slovak": "Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt.", "level": "A2", "topic": "Basic conjunctions", "answer": "Man, the doors are open now, so they show the whole valley, seriously."}
{"jid": "q0327", "slovak": "Stupne víťazov boli postavené zo žineniek asi za minútu.", "level": "B1", "topic": "Passive or Active", "answer": "The winners' podium was built out of gym mats in about a minute."}
{"jid": "q0328", "slovak": "Ten most preklenuje celý desivý kaňon, však?", "level": "B1", "topic": "Question tags", "answer": "The bridge spans the whole terrifying canyon, doesn't it?"}
{"jid": "q0329", "slovak": "Stroj by si mal tlačiť veľmi pomaly.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "You should pull the machine very slowly."}
{"jid": "q0330", "slovak": "Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "They needed to have the old accordion repaired before the keys stopped working completely."}
{"jid": "q0331", "slovak": "Model stíhačky opeká chlieb približne tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The bread has been toasted for about three minutes."}
{"jid": "q0332", "slovak": "Do obeda odovzdalo 200 voličov svoje volebné lístky, výrazne pred termínom.", "level": "B2", "topic": "All Past Tenses", "answer": "By noon, 200 voters will have handed in their ballots, well ahead of the deadline."}
{"jid": "q0333", "slovak": "Vraj sa rúti dolu tou riekou každé leto, kamoška.", "level": "B2", "topic": "All Present Tenses", "answer": "Apparently he hurtles down that river every summer."}
{"jid": "q0334", "slovak": "Mäkká guma môže vyčistiť celú stranu.", "level": "A1", "topic": "Modal verb CAN", "answer": "A soft rubber is able to clean the entire page."}
{"jid": "q0335", "slovak": "Takže mi povedal, že v meste nejazdí veľkou rýchlosťou.", "level": "A2", "topic": "Much, Many, Some...", "answer": "So I was told by him that he doesn't drive at high speed in the city."}
{"jid": "q0336", "slovak": "Stále ukladal ďalšie knihy na kopu, kým sa nezakývala.", "level": "B1", "topic": "Gerund vs Infinitive", "answer": "He kept putting more books on the pile until it wobbled."}
{"jid": "q0337", "slovak": "Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The fighter-jet toaster has been heating the same two slices for three minutes."}
{"jid": "q0338", "slovak": "Nebudem klamať, letíš vysoko, dokonca vyššie než borovice.", "level": "A2", "topic": "Adjective comparison", "answer": "I won't lie, you are flying high, even higher than the palm trees."}
{"jid": "q0339", "slovak": "Vraj sa rúti dolu tou riekou každé leto, kamoška.", "level": "B2", "topic": "All Present Tenses", "answer": "Apparently he strolls down that river every summer, girl."}
{"jid": "q0340", "slovak": "Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe.", "level": "B2", "topic": "All Present Tenses", "answer": "Status update: the closet has stayed tidy for 3 weeks."}
{"jid": "q0341", "slovak": "Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.", "level": "B2", "topic": "All Past Tenses", "answer": "By the time he reaches the narrow path, he will have been climbing down the rock ledges for an hour."}
{"jid": "q0342", "slovak": "Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "Membership has been requested by about forty students at the club fair since noon."}
{"jid": "q0343", "slovak": "Správa: oni zvyčajne dávajú pohľadnice, ale včera jej oni dali 12 darčekov.", "level": "A2", "topic": "Present or Past Simple", "answer": "Message: they usually give postcards, but yesterday she was given 12 gifts by them."}
{"jid": "q0344", "slovak": "Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa!", "level": "A1", "topic": "Prepositions of place/time", "answer": "She cleans dirty floor on Monday morning. An absolute disaster!"}
{"jid": "q0345", "slovak": "Kamarát tvrdil, že sa ho celý večer nikto nedotkol.", "level": "B2", "topic": "Reported speech", "answer": "A friend claimed that nobody had touched him all evening."}
{"jid": "q0346", "slovak": "Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.", "level": "A2", "topic": "Present or Past Simple", "answer": "You usually hate queues, but tonight you are waiting for the toilet. Respect."}
{"jid": "q0347", "slovak": "Ryby majú plán. Idú uplávať preč od žraloka.", "level": "A2", "topic": "Future BE GOING TO", "answer": "The fish have got a plan. They're going to swim off away from the shark."}
{"jid": "q0348", "slovak": "Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "Membership has been applied for at the club fair since noon."}
{"jid": "q0349", "slovak": "Ten hmyz je drobný, tak ona by mala skúmať ho lupou.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "That insect is tiny, so she should study it with a magnifying glass."}
{"jid": "q0350", "slovak": "Úprimne, dúha možno vybledne, ale zajtra v tomto čase budeš ukazovať svoje video všetkým.", "level": "B1", "topic": "Future Continuous", "answer": "Honestly, the rainbow might fade, but at this time tomorrow you'll be showing everyone your video."}
{"jid": "q0351", "slovak": "Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky.", "level": "A2", "topic": "Basic conjunctions", "answer": "Listen, she said that they have the same dress, but they're still friends."}
{"jid": "q0352", "slovak": "Kamarát tvrdil, že sa ho celý večer nikto nedotkol.", "level": "B2", "topic": "Reported speech", "answer": "A friend claims that nobody has touched him all evening."}
{"jid": "q0353", "slovak": "Jedna košeľa, jeden golier a dve červené kravaty.", "level": "A1", "topic": "Singular and plural", "answer": "One shirt, one button and two red ties."}
{"jid": "q0354", "slovak": "Mäkká guma môže vyčistiť celú stranu.", "level": "A1", "topic": "Modal verb CAN", "answer": "A whole page can be cleaned."}
{"jid": "q0355", "slovak": "Kamarát tvrdil, že sa ho celý večer nikto nedotkol.", "level": "B2", "topic": "Reported speech", "answer": "A friend claimed that he had not been touched by anyone all evening."}
{"jid": "q0356", "slovak": "Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo.", "level": "B1", "topic": "Modal verbs Probability", "answer": "The guard can't know about the cheese; he lifts the barrier too quickly."}
{"jid": "q0357", "slovak": "Nebudem klamať, letíš vysoko, dokonca vyššie než borovice.", "level": "A2", "topic": "Adjective comparison", "answer": "I won't lie - you're flying high, higher even than the pines."}
{"jid": "q0358", "slovak": "Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach.", "level": "B2", "topic": "Modals in past", "answer": "You should check the pegs before that match - two came loose in the first ten minutes."}
{"jid": "q0359", "slovak": "Fanúšik má jednu pomaľovanú tvár a šálu.", "level": "A1", "topic": "A, AN, THE", "answer": "The fan has one painted face and a hat."}
{"jid": "q0360", "slovak": "Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt.", "level": "A2", "topic": "Basic conjunctions", "answer": "Buddy, the door is already open, and so it uncovers the entire valley, for real."}
{"jid": "q0361", "slovak": "Fakt, tvoje dve baterky pekne osvetľujú tú tmavú rímsu.", "level": "A1", "topic": "Singular and plural", "answer": "Really, your two flashlights light up dark ledge nicely."}
{"jid": "q0362", "slovak": "Stroj by si mal tlačiť veľmi pomaly.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "The machine should be pushed by you very slowly."}
{"jid": "q0363", "slovak": "Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky.", "level": "A2", "topic": "Basic conjunctions", "answer": "Listen, he said they have the same dress, but they're still friends."}
{"jid": "q0364", "slovak": "Ten hmyz je drobný, tak ona by mala skúmať ho lupou.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "The bug is tiny, so she ought to examine it with a magnifying glass."}
{"jid": "q0365", "slovak": "Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký.", "level": "B2", "topic": "Modals in past", "answer": "Girl, he told me that iceberg was huge; he must have felt so tiny there."}
{"jid": "q0366", "slovak": "Vraj sa rúti dolu tou riekou každé leto, kamoška.", "level": "B2", "topic": "All Present Tenses", "answer": "Apparently he goes hurtling down that river every summer, girl."}
{"jid": "q0367", "slovak": "V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej.", "level": "B1", "topic": "Past Simple or Continuos", "answer": "The instant the crutch landed on the wet floor, he gripped it tightly and carried on."}
{"jid": "q0368", "slovak": "Táto ceruzka je ostrejšia ako tá tupá.", "level": "A2", "topic": "Adjective comparison", "answer": "This pencil is sharper than blunt one."}
{"jid": "q0369", "slovak": "Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali.", "level": "B2", "topic": "All Past Tenses", "answer": "The submarine moved below the surface for a while until the swimmers noticed it."}
{"jid": "q0370", "slovak": "Dvaja kamaráti potrebujú dva hrebene", "level": "A1", "topic": "Singular and plural", "answer": "Two friends need two combs."}
{"jid": "q0371", "slovak": "Stupne víťazov boli postavené zo žineniek asi za minútu.", "level": "B1", "topic": "Passive or Active", "answer": "The winners' podium got built from gym mats in about a minute."}
{"jid": "q0372", "slovak": "Útok je rýchly a hlasný na zelenom poli.", "level": "A1", "topic": "TO BE", "answer": "The attack on the green field is quick and loud."}
{"jid": "q0373", "slovak": "Správa: oni zvyčajne dávajú pohľadnice, ale včera jej oni dali 12 darčekov.", "level": "A2", "topic": "Present or Past Simple", "answer": "Message: they usually give postcards, but yesterday she was given 12 gifts."}
{"jid": "q0374", "slovak": "Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli!", "level": "B1", "topic": "Past Perfect Simple", "answer": "By the time he turned on the kettle, everyone staring at his moustache went completely silent!"}
{"jid": "q0375", "slovak": "Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký.", "level": "B2", "topic": "Modals in past", "answer": "Girl, he tells me that the iceberg is huge; he must feel so tiny there."}
{"jid": "q0376", "slovak": "Takže mi povedal, že v meste nejazdí veľkou rýchlosťou.", "level": "A2", "topic": "Much, Many, Some...", "answer": "So he will tell me that he doesn't drive at high speed in the city."}
{"jid": "q0377", "slovak": "Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe.", "level": "B2", "topic": "All Present Tenses", "answer": "Status update: the closet has remained tidy three weeks running."}
{"jid": "q0378", "slovak": "Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.", "level": "B2", "topic": "All Past Tenses", "answer": "Before he got to the narrow trail, he had spent an hour descending the rocky ledges."}
{"jid": "q0379", "slovak": "Dvaja kamaráti potrebujú dva hrebene", "level": "A1", "topic": "Singular and plural", "answer": "Two combs are needed by two friends."}
{"jid": "q0380", "slovak": "Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli!", "level": "B1", "topic": "Past Perfect Simple", "answer": "By the time he switches on the kettle, everyone who is staring at his moustache goes completely silent!"}
{"jid": "q0381", "slovak": "Kámoška, povedal mi, že ten ľadovec bol obrovský; musel sa tam cítiť taký maličký.", "level": "B2", "topic": "Modals in past", "answer": "Girl, I was told that the iceberg was huge; he must have felt so tiny there."}
{"jid": "q0382", "slovak": "Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska.", "level": "B2", "topic": "Articles advanced", "answer": "On the last page of the contract for the new job they write their name, and the office applauds."}
{"jid": "q0383", "slovak": "Do porady o 9:00 sa zotaví z takého vyčerpania.", "level": "B2", "topic": "All Future Tenses", "answer": "By the 9:00 meeting, he will have recovered from such an injury."}
{"jid": "q0384", "slovak": "Vločky sú v miske – hneď ich zje", "level": "A2", "topic": "Going to or Will", "answer": "The flakes are in bowl – he's going to eat them right away."}
{"jid": "q0385", "slovak": "Jedna košeľa, jeden golier a dve červené kravaty.", "level": "A1", "topic": "Singular and plural", "answer": "One shirt, one collar and one red tie."}
{"jid": "q0386", "slovak": "Útok je rýchly a hlasný na zelenom poli.", "level": "A1", "topic": "TO BE", "answer": "The attack is fast and quiet on the green field."}
{"jid": "q0387", "slovak": "Hore je vietor. Môžeš vidieť tú vlajku?", "level": "A1", "topic": "Modal verb CAN", "answer": "It was windy up there. Could you see the flag?"}
{"jid": "q0388", "slovak": "Vraj sa rúti dolu tou riekou každé leto, kamoška.", "level": "B2", "topic": "All Present Tenses", "answer": "Apparently he hurtled down that river every summer, girl."}
{"jid": "q0389", "slovak": "Trénerka má obväz a bielu pásku.", "level": "A1", "topic": "HAVE GOT", "answer": "The coach has got white tape and a bandage."}
{"jid": "q0390", "slovak": "Vločky sú v miske – hneď ich zje", "level": "A2", "topic": "Going to or Will", "answer": "The flakes are in the bowl – I'm going to eat them right away."}
{"jid": "q0391", "slovak": "On kladie slaninu vedľa vajíčka do čiernej panvice.", "level": "B1", "topic": "Passive or Active", "answer": "He is putting the bacon next to the egg in the black pan."}
{"jid": "q0392", "slovak": "Úprimne, dúha možno vybledne, ale zajtra v tomto čase budeš ukazovať svoje video všetkým.", "level": "B1", "topic": "Future Continuous", "answer": "Honestly, the rainbow may fade, but this time tomorrow you will be showing your video to everyone."}
{"jid": "q0393", "slovak": "Na dunách je len jedna ťava.", "level": "A2", "topic": "There is, are", "answer": "There is one camel on the dunes."}
{"jid": "q0394", "slovak": "Útok je rýchly a hlasný na zelenom poli.", "level": "A1", "topic": "TO BE", "answer": "On the green field, the attack is rapid and noisy."}
{"jid": "q0395", "slovak": "Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "For three minutes now the fighter-jet toaster has been warming up the same two slices."}
{"jid": "q0396", "slovak": "Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska.", "level": "B2", "topic": "Articles advanced", "answer": "They write their name on the last page of the contract for the new job and the office applauds."}
