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

Write ONE file, judge/verdicts_part3.json, and nothing else. Exact JSON shape:
[{"jid": "q0001", "judged": "wrong", "type": "M", "borderline": false, "confidence": 4}, ...]
All 99 items, in the order given. No commentary; the file must parse as JSON.

THE PACKET:
{"jid": "q0199", "slovak": "Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli!", "level": "B1", "topic": "Past Perfect Simple", "answer": "By the time the kettle was switched on, everyone who was staring at his moustache had fallen completely silent!"}
{"jid": "q0200", "slovak": "Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "About forty students have been applying for membership at the club fair."}
{"jid": "q0201", "slovak": "O šiestej už bude búchať do tých lap dve hodiny v kuse.", "level": "B2", "topic": "Future Perfect Continuous", "answer": "By six o'clock he will have been pounding those mitts for two hours."}
{"jid": "q0202", "slovak": "Tieto konzervy vyletujú z jeho papierovej tašky.", "level": "A1", "topic": "This, That, These...", "answer": "These tins fly out of his paper bag."}
{"jid": "q0203", "slovak": "Táto ceruzka je ostrejšia ako tá tupá.", "level": "A2", "topic": "Adjective comparison", "answer": "This pencil is sharper than the dull one."}
{"jid": "q0204", "slovak": "Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The fighter-jet toaster has been heating two slices for three minutes."}
{"jid": "q0205", "slovak": "Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli!", "level": "B1", "topic": "Past Perfect Simple", "answer": "By the time he switched on kettle, everyone who was staring at his moustache had fallen completely silent!"}
{"jid": "q0206", "slovak": "Jedna košeľa, jeden golier a dve červené kravaty.", "level": "A1", "topic": "Singular and plural", "answer": "A shirt, a collar, and two red neckties."}
{"jid": "q0207", "slovak": "Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.", "level": "A2", "topic": "Present or Past Simple", "answer": "You usually hate queues, but last night you waited for the toilet. Respect."}
{"jid": "q0208", "slovak": "Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky.", "level": "A2", "topic": "Basic conjunctions", "answer": "Listen, she said they had the same dress, but they are still friends."}
{"jid": "q0209", "slovak": "Žena mu na krk zavesí jednu zlatú medailu.", "level": "A1", "topic": "A, AN, THE", "answer": "The woman will hang a gold medal around his neck."}
{"jid": "q0210", "slovak": "Tieto konzervy vyletujú z jeho papierovej tašky.", "level": "A1", "topic": "This, That, These...", "answer": "Those cans are flying out of his paper bag."}
{"jid": "q0211", "slovak": "Kdeže, gekón práve teraz chrlí oheň, lebo papričky sú také pálivé.", "level": "B2", "topic": "All Present Tenses", "answer": "No way, the gecko is spitting fire right now, because the peppers are so sweet."}
{"jid": "q0212", "slovak": "Kdeže, gekón práve teraz chrlí oheň, lebo papričky sú také pálivé.", "level": "B2", "topic": "All Present Tenses", "answer": "No, the gecko is breathing out fire right now, because the peppers are that hot."}
{"jid": "q0213", "slovak": "Kamarát tvrdil, že sa ho celý večer nikto nedotkol.", "level": "B2", "topic": "Reported speech", "answer": "A friend claimed that nobody had touched him."}
{"jid": "q0214", "slovak": "Stále ukladal ďalšie knihy na kopu, kým sa nezakývala.", "level": "B1", "topic": "Gerund vs Infinitive", "answer": "He kept putting books on the pile until it wobbled."}
{"jid": "q0215", "slovak": "O šiestej už bude búchať do tých lap dve hodiny v kuse.", "level": "B2", "topic": "Future Perfect Continuous", "answer": "By six o'clock he will have been pounding some mitts for two hours straight."}
{"jid": "q0216", "slovak": "Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.", "level": "A2", "topic": "Present or Past Simple", "answer": "Usually you hate queues, but last night you did wait for the toilet. Respect."}
{"jid": "q0217", "slovak": "Jedna košeľa, jeden golier a dve červené kravaty.", "level": "A1", "topic": "Singular and plural", "answer": "One shirt, one collar, two red ties."}
{"jid": "q0218", "slovak": "On má sivú handričku na čistenie auta.", "level": "A1", "topic": "HAVE GOT", "answer": "He's got a grey cleaning cloth for the car."}
{"jid": "q0219", "slovak": "On má sivú handričku na čistenie auta.", "level": "A1", "topic": "HAVE GOT", "answer": "He has got a grey cloth for cleaning the car."}
{"jid": "q0220", "slovak": "Správa: oni zvyčajne dávajú pohľadnice, ale včera jej oni dali 12 darčekov.", "level": "A2", "topic": "Present or Past Simple", "answer": "Message: they usually give postcards, but yesterday they gave her gifts."}
{"jid": "q0221", "slovak": "Trénerka má obväz a bielu pásku.", "level": "A1", "topic": "HAVE GOT", "answer": "The trainer has a bandage and white tape."}
{"jid": "q0222", "slovak": "Fanúšik má jednu pomaľovanú tvár a šálu.", "level": "A1", "topic": "A, AN, THE", "answer": "The fan has one painted face and a scarf."}
{"jid": "q0223", "slovak": "Mäkká guma môže vyčistiť celú stranu.", "level": "A1", "topic": "Modal verb CAN", "answer": "A whole page can be cleaned by a soft eraser."}
{"jid": "q0224", "slovak": "Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach.", "level": "B2", "topic": "Modals in past", "answer": "You should have checked the pegs before that match - two came loose in first ten minutes."}
{"jid": "q0225", "slovak": "Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe.", "level": "B2", "topic": "All Present Tenses", "answer": "Status update: three weeks in a row, the wardrobe has stayed tidy."}
{"jid": "q0226", "slovak": "Stále ukladal ďalšie knihy na kopu, kým sa nezakývala.", "level": "B1", "topic": "Gerund vs Infinitive", "answer": "He kept putting more books on the pile until it fell."}
{"jid": "q0227", "slovak": "Stupne víťazov boli postavené zo žineniek asi za minútu.", "level": "B1", "topic": "Passive or Active", "answer": "The winners' podium was built out of gym mats in about minute."}
{"jid": "q0228", "slovak": "Ponorka sa pohybovala pod hladinou istý čas, kým ju plavci spozorovali.", "level": "B2", "topic": "All Past Tenses", "answer": "The submarine had been moving under the surface before the swimmers spotted it."}
{"jid": "q0229", "slovak": "Táto váha ukazuje oveľa viac ako pred chvíľou.", "level": "A1", "topic": "This, That, These...", "answer": "This scale showed a lot more than a moment ago."}
{"jid": "q0230", "slovak": "Nebudem klamať, letíš vysoko, dokonca vyššie než borovice.", "level": "A2", "topic": "Adjective comparison", "answer": "I won't lie, you are flying high, even higher than the pines."}
{"jid": "q0231", "slovak": "Ten hmyz je drobný, tak ona by mala skúmať ho lupou.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "The insect is tiny, so she should examine it with a magnifying glass."}
{"jid": "q0232", "slovak": "Takže mi povedal, že v meste nejazdí veľkou rýchlosťou.", "level": "A2", "topic": "Much, Many, Some...", "answer": "So I was told that he doesn't drive at high speed in the city."}
{"jid": "q0233", "slovak": "Pred vhadzovaním si dala omotať hokejku páskou.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "She had her hockey stick wrapped in tape before the face-off."}
{"jid": "q0234", "slovak": "Jedna košeľa, jeden golier a dve červené kravaty.", "level": "A1", "topic": "Singular and plural", "answer": "One shirt, one collar and two ties."}
{"jid": "q0235", "slovak": "Úprimne, dnes si hlasnejší než celý národný tím.", "level": "A2", "topic": "Adjective comparison", "answer": "Honestly, today you're faster than the whole national team."}
{"jid": "q0236", "slovak": "On má sivú handričku na čistenie auta.", "level": "A1", "topic": "HAVE GOT", "answer": "He's got a grey cleaning cloth for the car."}
{"jid": "q0237", "slovak": "V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej.", "level": "B1", "topic": "Past Simple or Continuos", "answer": "The moment the crutch hit the wet floor, he grabbed it firmly and walked on."}
{"jid": "q0238", "slovak": "Fakt, tvoje dve baterky pekne osvetľujú tú tmavú rímsu.", "level": "A1", "topic": "Singular and plural", "answer": "Really, your two flashlights light up that dark ledge nicely."}
{"jid": "q0239", "slovak": "Ten hmyz je drobný, tak ona by mala skúmať ho lupou.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "The insect is tiny, so she should examine it with a microscope."}
{"jid": "q0240", "slovak": "Úprimne, dnes si hlasnejší než celý národný tím.", "level": "A2", "topic": "Adjective comparison", "answer": "Honestly, today you will be louder than the whole national team."}
{"jid": "q0241", "slovak": "Fanúšik má jednu pomaľovanú tvár a šálu.", "level": "A1", "topic": "A, AN, THE", "answer": "The fan has got one painted face and a scarf."}
{"jid": "q0242", "slovak": "Muž obdivuje svoje luxusné auto už dvadsať minút.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The man will have been admiring his luxury car for twenty minutes."}
{"jid": "q0243", "slovak": "Do porady o 9:00 sa zotaví z takého vyčerpania.", "level": "B2", "topic": "All Future Tenses", "answer": "By the meeting at 9:00 he is going to recover from such exhaustion."}
{"jid": "q0244", "slovak": "On spal. Preto nič videl.", "level": "A2", "topic": "Past Simple", "answer": "He is sleeping. That's why he sees nothing."}
{"jid": "q0245", "slovak": "On má sivú handričku na čistenie auta.", "level": "A1", "topic": "HAVE GOT", "answer": "He has got grey cloth for cleaning the car."}
{"jid": "q0246", "slovak": "Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "They need to have the old accordion repaired before the keys stop working completely."}
{"jid": "q0247", "slovak": "Stupne víťazov boli postavené zo žineniek asi za minútu.", "level": "B1", "topic": "Passive or Active", "answer": "The winners' podium was built out of wooden crates in about a minute."}
{"jid": "q0248", "slovak": "O šiestej už bude búchať do tých lap dve hodiny v kuse.", "level": "B2", "topic": "Future Perfect Continuous", "answer": "At six he'll have been pounding those pads for two solid hours."}
{"jid": "q0249", "slovak": "Do obeda odovzdalo 200 voličov svoje volebné lístky, výrazne pred termínom.", "level": "B2", "topic": "All Past Tenses", "answer": "By noon, the ballots had been handed in by 200 voters, well before the deadline."}
{"jid": "q0250", "slovak": "Trénerka má obväz a bielu pásku.", "level": "A1", "topic": "HAVE GOT", "answer": "The coach has got a bandage and white string."}
{"jid": "q0251", "slovak": "Jedna košeľa, jeden golier a dve červené kravaty.", "level": "A1", "topic": "Singular and plural", "answer": "A shirt, a collar, and two red neckties."}
{"jid": "q0252", "slovak": "Ten hmyz je drobný, tak ona by mala skúmať ho lupou.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "The insect is tiny, so she should examine it with magnifying glass."}
{"jid": "q0253", "slovak": "Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt.", "level": "A2", "topic": "Basic conjunctions", "answer": "Dude, the door is already open, but it reveals the whole valley, really."}
{"jid": "q0254", "slovak": "Úprimne, dnes si hlasnejší než celý národný tím.", "level": "A2", "topic": "Adjective comparison", "answer": "Frankly, today you're noisier than the whole national squad."}
{"jid": "q0255", "slovak": "Útok je rýchly a hlasný na zelenom poli.", "level": "A1", "topic": "TO BE", "answer": "Attack is fast and loud on the green field."}
{"jid": "q0256", "slovak": "Táto váha ukazuje oveľa viac ako pred chvíľou.", "level": "A1", "topic": "This, That, These...", "answer": "This scale shows a lot more than a moment ago."}
{"jid": "q0257", "slovak": "Jedna košeľa, jeden golier a dve červené kravaty.", "level": "A1", "topic": "Singular and plural", "answer": "One shirt, one collar and one red tie."}
{"jid": "q0258", "slovak": "Poprosila ma, aby som nehýbal rukou, kým spí.", "level": "B2", "topic": "Reported speech", "answer": "I was asked by her not to move my arm while she was asleep."}
{"jid": "q0259", "slovak": "Tieto konzervy vyletujú z jeho papierovej tašky.", "level": "A1", "topic": "This, That, These...", "answer": "Out of his paper bag, these cans are flying."}
{"jid": "q0260", "slovak": "Na dunách je len jedna ťava.", "level": "A2", "topic": "There is, are", "answer": "There was only one camel on the dunes."}
{"jid": "q0261", "slovak": "Pred vhadzovaním si dala omotať hokejku páskou.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "Before the face-off, she had her hockey stick wrapped with tape."}
{"jid": "q0262", "slovak": "Muž obdivuje svoje luxusné auto už dvadsať minút.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The man has admired his luxury car for twenty minutes now."}
{"jid": "q0263", "slovak": "Približne štyridsať študentov žiada o členstvo na klubovom veľtrhu od obeda.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "About forty students had been applying for membership at the club fair since noon."}
{"jid": "q0264", "slovak": "Do obeda odovzdalo 200 voličov svoje volebné lístky, výrazne pred termínom.", "level": "B2", "topic": "All Past Tenses", "answer": "By lunchtime 200 voters submitted their ballots, significantly ahead of schedule."}
{"jid": "q0265", "slovak": "Pamätník zbožňoval, a samozrejme aj jeho fotoaparát.", "level": "B1", "topic": "So, Neither, Nor", "answer": "He adored monument, and so did his camera, of course."}
{"jid": "q0266", "slovak": "Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.", "level": "B2", "topic": "All Past Tenses", "answer": "By the time he reached the narrow path, he had been climbing down the rock ledges for an hour."}
{"jid": "q0267", "slovak": "Ten hmyz je drobný, tak ona by mala skúmať ho lupou.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "The insect is tiny, so he should examine it with a magnifying glass."}
{"jid": "q0268", "slovak": "Do obeda odovzdalo 200 voličov svoje volebné lístky, výrazne pred termínom.", "level": "B2", "topic": "All Past Tenses", "answer": "By noon, the ballots had been handed in, well ahead of the deadline."}
{"jid": "q0269", "slovak": "Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.", "level": "A2", "topic": "Present or Past Simple", "answer": "You normally hate lines, but yesterday evening you were waiting for the toilet. Respect."}
{"jid": "q0270", "slovak": "Takže mi povedal, že v meste nejazdí veľkou rýchlosťou.", "level": "A2", "topic": "Much, Many, Some...", "answer": "So he will tell me that he doesn't drive at high speed in the city."}
{"jid": "q0271", "slovak": "Mäkká guma môže vyčistiť celú stranu.", "level": "A1", "topic": "Modal verb CAN", "answer": "A hard eraser can clean a whole page."}
{"jid": "q0272", "slovak": "Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli!", "level": "B1", "topic": "Past Perfect Simple", "answer": "By the time the kettle had been switched on by him, everyone who was staring at his moustache fell completely silent!"}
{"jid": "q0273", "slovak": "Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo.", "level": "B1", "topic": "Modal verbs Probability", "answer": "The guard can't know about the cheese - the ramp is raised too quickly."}
{"jid": "q0274", "slovak": "Muž obdivuje svoje luxusné auto už dvadsať minút.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "His luxury car has been admired by the man for twenty minutes."}
{"jid": "q0275", "slovak": "Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach.", "level": "B2", "topic": "Modals in past", "answer": "You ought to have checked the pegs before that match; two of them worked loose within the first ten minutes."}
{"jid": "q0276", "slovak": "On kladie slaninu vedľa vajíčka do čiernej panvice.", "level": "B1", "topic": "Passive or Active", "answer": "He puts bacon beside the egg into the black frying pan."}
{"jid": "q0277", "slovak": "Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala.", "level": "B1", "topic": "Past Perfect Simple", "answer": "I won't lie, you were the most charming clerk; you had never smiled like that before."}
{"jid": "q0278", "slovak": "Ten most preklenuje celý desivý kaňon, však?", "level": "B1", "topic": "Question tags", "answer": "The entire scary canyon is spanned by the bridge, isn't it?"}
{"jid": "q0279", "slovak": "Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe.", "level": "B2", "topic": "All Present Tenses", "answer": "Status update: the wardrobe has stayed tidy for 3 weeks in a row."}
{"jid": "q0280", "slovak": "Do porady o 9:00 sa zotaví z takého vyčerpania.", "level": "B2", "topic": "All Future Tenses", "answer": "By the 9:00 meeting, he had recovered from such exhaustion."}
{"jid": "q0281", "slovak": "Poprosila ma, aby som nehýbal rukou, kým spí.", "level": "B2", "topic": "Reported speech", "answer": "I was asked not to move my arm while she was sleeping."}
{"jid": "q0282", "slovak": "Katastrofa! Ona nemá čas na dlhú návštevu!", "level": "A2", "topic": "Countable and uncountable", "answer": "Disaster! She doesn't have a time for a long visit!"}
{"jid": "q0283", "slovak": "Hore je vietor. Môžeš vidieť tú vlajku?", "level": "A1", "topic": "Modal verb CAN", "answer": "There's wind up there. Can you see that flag?"}
{"jid": "q0284", "slovak": "Katastrofa! Ona nemá čas na dlhú návštevu!", "level": "A2", "topic": "Countable and uncountable", "answer": "Disaster! She didn't have time for a long visit!"}
{"jid": "q0285", "slovak": "O šiestej už bude búchať do tých lap dve hodiny v kuse.", "level": "B2", "topic": "Future Perfect Continuous", "answer": "At six o'clock he had been pounding those mitts for two hours straight."}
{"jid": "q0286", "slovak": "Trénerka má obväz a bielu pásku.", "level": "A1", "topic": "HAVE GOT", "answer": "The coach had a bandage and white tape."}
{"jid": "q0287", "slovak": "O šiestej už bude búchať do tých lap dve hodiny v kuse.", "level": "B2", "topic": "Future Perfect Continuous", "answer": "By six o'clock he will already have been banging on those mitts for two hours non-stop."}
{"jid": "q0288", "slovak": "Už päť minút hľadá gumičku do vlasov a na zápästí má tri.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "She has been searching for a hair band for five minutes and has three of them on her wrist."}
{"jid": "q0289", "slovak": "Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala.", "level": "B1", "topic": "Past Perfect Simple", "answer": "I won't lie, you were the most charming clerk; she had often smiled like that before."}
{"jid": "q0290", "slovak": "Tieto konzervy vyletujú z jeho papierovej tašky.", "level": "A1", "topic": "This, That, These...", "answer": "These cans are flying out of his paper bag."}
{"jid": "q0291", "slovak": "Ten most preklenuje celý desivý kaňon, však?", "level": "B1", "topic": "Question tags", "answer": "That bridge crosses the whole frightening canyon, doesn't it?"}
{"jid": "q0292", "slovak": "Fanúšik má jednu pomaľovanú tvár a šálu.", "level": "A1", "topic": "A, AN, THE", "answer": "The fan has one painted face and scarf."}
{"jid": "q0293", "slovak": "Pred vhadzovaním si dala omotať hokejku páskou.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "Before the face-off, she had her hockey stick wrapped."}
{"jid": "q0294", "slovak": "Na dunách je len jedna ťava.", "level": "A2", "topic": "There is, are", "answer": "There's only a single camel on the dunes."}
{"jid": "q0295", "slovak": "Úprimne, dúha možno vybledne, ale zajtra v tomto čase budeš ukazovať svoje video všetkým.", "level": "B1", "topic": "Future Continuous", "answer": "Honestly, the rainbow may fade, but this time tomorrow you will be showing your photo to everyone."}
{"jid": "q0296", "slovak": "Táto váha ukazuje oveľa viac ako pred chvíľou.", "level": "A1", "topic": "This, That, These...", "answer": "This scale is showing much more than it did a little while ago."}
{"jid": "q0297", "slovak": "Žena mu na krk zavesí jednu zlatú medailu.", "level": "A1", "topic": "A, AN, THE", "answer": "Woman will hang a gold medal around his neck."}
