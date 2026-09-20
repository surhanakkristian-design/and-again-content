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

Write ONE file, judge/verdicts_part1.json, and nothing else. Exact JSON shape:
[{"jid": "q0001", "judged": "wrong", "type": "M", "borderline": false, "confidence": 4}, ...]
All 99 items, in the order given. No commentary; the file must parse as JSON.

THE PACKET:
{"jid": "q0001", "slovak": "Ryby majú plán. Idú uplávať preč od žraloka.", "level": "A2", "topic": "Future BE GOING TO", "answer": "The fish have a plan. They will swim away from the shark."}
{"jid": "q0002", "slovak": "Vločky sú v miske – hneď ich zje", "level": "A2", "topic": "Going to or Will", "answer": "The flakes are in the bowl – I'm going to eat them right away."}
{"jid": "q0003", "slovak": "Tieto konzervy vyletujú z jeho papierovej tašky.", "level": "A1", "topic": "This, That, These...", "answer": "These cans are flying out of his bag."}
{"jid": "q0004", "slovak": "Žena mu na krk zavesí jednu zlatú medailu.", "level": "A1", "topic": "A, AN, THE", "answer": "The woman is going to hang one gold medal on his neck."}
{"jid": "q0005", "slovak": "Hore je vietor. Môžeš vidieť tú vlajku?", "level": "A1", "topic": "Modal verb CAN", "answer": "It is windy up above. Are you able to see the flag?"}
{"jid": "q0006", "slovak": "Už päť minút hľadá gumičku do vlasov a na zápästí má tri.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "She has been looking for a hair tie for five minutes and has three."}
{"jid": "q0007", "slovak": "Poprosila ma, aby som nehýbal rukou, kým spí.", "level": "B2", "topic": "Reported speech", "answer": "She asks me not to move my arm while she is sleeping."}
{"jid": "q0008", "slovak": "Už päť minút hľadá gumičku do vlasov a na zápästí má tri.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "For five minutes now she's been looking for a hair elastic, and she has got three on her wrist."}
{"jid": "q0009", "slovak": "Vraj sa rúti dolu tou riekou každé leto, kamoška.", "level": "B2", "topic": "All Present Tenses", "answer": "Apparently he hurtles down that river every summer, girl."}
{"jid": "q0010", "slovak": "Správa: oni zvyčajne dávajú pohľadnice, ale včera jej oni dali 12 darčekov.", "level": "A2", "topic": "Present or Past Simple", "answer": "Message: they usually give postcards, but today they are giving her 12 gifts."}
{"jid": "q0011", "slovak": "Muž obdivuje svoje luxusné auto už dvadsať minút.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The man has been admiring his luxury car for twenty minutes."}
{"jid": "q0012", "slovak": "Kamarát tvrdil, že sa ho celý večer nikto nedotkol.", "level": "B2", "topic": "Reported speech", "answer": "A friend claimed that no one touched him the whole evening."}
{"jid": "q0013", "slovak": "Dvaja kamaráti potrebujú dva hrebene", "level": "A1", "topic": "Singular and plural", "answer": "Two friends need a comb."}
{"jid": "q0014", "slovak": "Stroj by si mal tlačiť veľmi pomaly.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "You ought to push the machine very slowly."}
{"jid": "q0015", "slovak": "Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky.", "level": "A2", "topic": "Basic conjunctions", "answer": "Listen, she said they have the same dresses, but they're still friends."}
{"jid": "q0016", "slovak": "Žena mu na krk zavesí jednu zlatú medailu.", "level": "A1", "topic": "A, AN, THE", "answer": "One gold medal will be hung around his neck by the woman."}
{"jid": "q0017", "slovak": "On spal. Preto nič videl.", "level": "A2", "topic": "Past Simple", "answer": "He was sleeping. That's why she saw nothing."}
{"jid": "q0018", "slovak": "Vločky sú v miske – hneď ich zje", "level": "A2", "topic": "Going to or Will", "answer": "The flakes are in the bowl – he'll eat them straight away."}
{"jid": "q0019", "slovak": "Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt.", "level": "A2", "topic": "Basic conjunctions", "answer": "Dude, the door was already open, so it revealed the whole valley, really."}
{"jid": "q0020", "slovak": "Mäkká guma môže vyčistiť celú stranu.", "level": "A1", "topic": "Modal verb CAN", "answer": "A whole page can be cleaned."}
{"jid": "q0021", "slovak": "Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt.", "level": "A2", "topic": "Basic conjunctions", "answer": "Dude, the door is already open, so it reveals the whole valley, really."}
{"jid": "q0022", "slovak": "Do obeda odovzdalo 200 voličov svoje volebné lístky, výrazne pred termínom.", "level": "B2", "topic": "All Past Tenses", "answer": "By noon, 200 voters had handed in their ballots."}
{"jid": "q0023", "slovak": "Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.", "level": "A2", "topic": "Present or Past Simple", "answer": "You normally hate lines, but yesterday evening you were waiting for the toilet. Respect."}
{"jid": "q0024", "slovak": "Vločky sú v miske – hneď ich zje", "level": "A2", "topic": "Going to or Will", "answer": "The flakes are in the bowl – he ate them right away."}
{"jid": "q0025", "slovak": "Kámo, dvere sú už otvorené, tak odhaľujú celé údolie, fakt.", "level": "A2", "topic": "Basic conjunctions", "answer": "Dude, the door is already open, so it reveals the valley, really."}
{"jid": "q0026", "slovak": "Trénerka má obväz a bielu pásku.", "level": "A1", "topic": "HAVE GOT", "answer": "The coach has got a bandage and white tape."}
{"jid": "q0027", "slovak": "Stále ukladal ďalšie knihy na kopu, kým sa nezakývala.", "level": "B1", "topic": "Gerund vs Infinitive", "answer": "He keeps putting more books on the pile until it wobbles."}
{"jid": "q0028", "slovak": "On kladie slaninu vedľa vajíčka do čiernej panvice.", "level": "B1", "topic": "Passive or Active", "answer": "The bacon is being put next to the egg in the black pan."}
{"jid": "q0029", "slovak": "Jedna košeľa, jeden golier a dve červené kravaty.", "level": "A1", "topic": "Singular and plural", "answer": "One shirt, one collar and two red ties."}
{"jid": "q0030", "slovak": "Mäkká guma môže vyčistiť celú stranu.", "level": "A1", "topic": "Modal verb CAN", "answer": "A soft eraser can clean a whole page."}
{"jid": "q0031", "slovak": "Pred vhadzovaním si dala omotať hokejku páskou.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "Before the puck drop, she got her hockey stick wrapped with tape."}
{"jid": "q0032", "slovak": "Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala.", "level": "B1", "topic": "Past Perfect Simple", "answer": "I won't lie, you were the most charming clerk; she had never smiled like that before."}
{"jid": "q0033", "slovak": "On kladie slaninu vedľa vajíčka do čiernej panvice.", "level": "B1", "topic": "Passive or Active", "answer": "He puts bacon beside the egg into the black frying pan."}
{"jid": "q0034", "slovak": "Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.", "level": "A2", "topic": "Present or Past Simple", "answer": "Usually you hate queues, but last night you did wait for the toilet. Respect."}
{"jid": "q0035", "slovak": "Stroj by si mal tlačiť veľmi pomaly.", "level": "A2", "topic": "Modal verb SHOULD", "answer": "You should push the machine slowly."}
{"jid": "q0036", "slovak": "Žena mu na krk zavesí jednu zlatú medailu.", "level": "A1", "topic": "A, AN, THE", "answer": "The woman hung a gold medal around his neck."}
{"jid": "q0037", "slovak": "Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo.", "level": "B1", "topic": "Modal verbs Probability", "answer": "The guard can't know about the cheese - he raises the ramp too quickly."}
{"jid": "q0038", "slovak": "Mäkká guma môže vyčistiť celú stranu.", "level": "A1", "topic": "Modal verb CAN", "answer": "Soft eraser can clean a whole page."}
{"jid": "q0039", "slovak": "Fakt, tvoje dve baterky pekne osvetľujú tú tmavú rímsu.", "level": "A1", "topic": "Singular and plural", "answer": "Really, your two flashlights light up that dark ledge nicely."}
{"jid": "q0040", "slovak": "Model stíhačky opeká chlieb približne tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The model fighter jet had been toasting the bread for about three minutes."}
{"jid": "q0041", "slovak": "Kdeže, gekón práve teraz chrlí oheň, lebo papričky sú také pálivé.", "level": "B2", "topic": "All Present Tenses", "answer": "Nonsense — right now the gecko is breathing fire, since the peppers are so spicy."}
{"jid": "q0042", "slovak": "Počúvaj, povedala, že majú rovnaké šaty, ale sú stále kamarátky.", "level": "A2", "topic": "Basic conjunctions", "answer": "Listen, she said they have the same dress, but they're friends."}
{"jid": "q0043", "slovak": "Stojí bosý na teplom piesku.", "level": "A1", "topic": "Prepositions of place/time", "answer": "He stands barefoot on the warm sand."}
{"jid": "q0044", "slovak": "Úprimne, dúha možno vybledne, ale zajtra v tomto čase budeš ukazovať svoje video všetkým.", "level": "B1", "topic": "Future Continuous", "answer": "Honestly, the rainbow may fade, but this time tomorrow you will be showing your video."}
{"jid": "q0045", "slovak": "Ten most preklenuje celý desivý kaňon, však?", "level": "B1", "topic": "Question tags", "answer": "The bridge spans the terrifying canyon, doesn't it?"}
{"jid": "q0046", "slovak": "Pri ľade kráčajú ďalšie dva tučniaky", "level": "A1", "topic": "Singular and plural", "answer": "Two other penguins walk next to the ice."}
{"jid": "q0047", "slovak": "Ten most preklenuje celý desivý kaňon, však?", "level": "B1", "topic": "Question tags", "answer": "The bridge spanned the whole terrifying canyon, didn't it?"}
{"jid": "q0048", "slovak": "Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach.", "level": "B2", "topic": "Modals in past", "answer": "The pegs should have been checked before that match - two came loose in the first ten minutes."}
{"jid": "q0049", "slovak": "Úprimne, dnes si hlasnejší než celý národný tím.", "level": "A2", "topic": "Adjective comparison", "answer": "Honestly, you are louder than the entire national team today."}
{"jid": "q0050", "slovak": "Pri ľade kráčajú ďalšie dva tučniaky", "level": "A1", "topic": "Singular and plural", "answer": "One more penguin is walking by the ice."}
{"jid": "q0051", "slovak": "O šiestej už bude búchať do tých lap dve hodiny v kuse.", "level": "B2", "topic": "Future Perfect Continuous", "answer": "By six o'clock he will have been hitting those mitts for two hours straight."}
{"jid": "q0052", "slovak": "Kdeže, gekón práve teraz chrlí oheň, lebo papričky sú také pálivé.", "level": "B2", "topic": "All Present Tenses", "answer": "No way, gecko is spitting fire right now, because the peppers are so hot."}
{"jid": "q0053", "slovak": "Na dunách je len jedna ťava.", "level": "A2", "topic": "There is, are", "answer": "On the dunes there is just one camel."}
{"jid": "q0054", "slovak": "Dvaja kamaráti potrebujú dva hrebene", "level": "A1", "topic": "Singular and plural", "answer": "Two combs are needed."}
{"jid": "q0055", "slovak": "Stojí bosý na teplom piesku.", "level": "A1", "topic": "Prepositions of place/time", "answer": "He stood barefoot on the warm sand."}
{"jid": "q0056", "slovak": "On spal. Preto nič videl.", "level": "A2", "topic": "Past Simple", "answer": "He was sleeping. That's why he saw nothing."}
{"jid": "q0057", "slovak": "On spal. Preto nič videl.", "level": "A2", "topic": "Past Simple", "answer": "He slept. That is why he didn't see anything."}
{"jid": "q0058", "slovak": "Do porady o 9:00 sa zotaví z takého vyčerpania.", "level": "B2", "topic": "All Future Tenses", "answer": "By 9:00 meeting, he will have recovered from such exhaustion."}
{"jid": "q0059", "slovak": "Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach.", "level": "B2", "topic": "Modals in past", "answer": "You should have checked the pegs before that match - two came loose in the first ten minutes."}
{"jid": "q0060", "slovak": "Takže mi povedal, že v meste nejazdí veľkou rýchlosťou.", "level": "A2", "topic": "Much, Many, Some...", "answer": "So he told me he does not travel at high speed in the city."}
{"jid": "q0061", "slovak": "Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe.", "level": "B2", "topic": "All Present Tenses", "answer": "Status update: the closet will stay tidy for 3 weeks in a row."}
{"jid": "q0062", "slovak": "Model stíhačky opeká chlieb približne tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The model of the fighter jet toasts the bread for approximately three minutes."}
{"jid": "q0063", "slovak": "Úprimne, dnes si hlasnejší než celý národný tím.", "level": "A2", "topic": "Adjective comparison", "answer": "Honestly, today you're louder than the national team."}
{"jid": "q0064", "slovak": "Na dunách je len jedna ťava.", "level": "A2", "topic": "There is, are", "answer": "On the dunes there is just one camel."}
{"jid": "q0065", "slovak": "Vločky sú v miske – hneď ich zje", "level": "A2", "topic": "Going to or Will", "answer": "The flakes are in the bowl – they're going to be eaten by him right away."}
{"jid": "q0066", "slovak": "Stojí bosý na teplom piesku.", "level": "A1", "topic": "Prepositions of place/time", "answer": "He is standing on the warm sand."}
{"jid": "q0067", "slovak": "Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.", "level": "A2", "topic": "Present or Past Simple", "answer": "You usually hate queues, but last night she waited for the toilet. Respect."}
{"jid": "q0068", "slovak": "Stojí bosý na teplom piesku.", "level": "A1", "topic": "Prepositions of place/time", "answer": "Barefoot, he is standing on the warm sand."}
{"jid": "q0069", "slovak": "Mal si skontrolovať kolíky pred tým zápasom - dva sa uvoľnili už v prvých desiatich minútach.", "level": "B2", "topic": "Modals in past", "answer": "The pegs should have been checked by you before that match - two came loose in the first ten minutes."}
{"jid": "q0070", "slovak": "Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa!", "level": "A1", "topic": "Prepositions of place/time", "answer": "The dirty floor is cleaned on Monday morning. An absolute disaster!"}
{"jid": "q0071", "slovak": "Nebudem klamať, bol si ten najšarmantnejší úradník; ona sa nikdy predtým tak neusmievala.", "level": "B1", "topic": "Past Perfect Simple", "answer": "I'm not going to lie, you were the most charming official; never before had she smiled like that."}
{"jid": "q0072", "slovak": "Hore je vietor. Môžeš vidieť tú vlajku?", "level": "A1", "topic": "Modal verb CAN", "answer": "It's cold up there. Can you see the flag?"}
{"jid": "q0073", "slovak": "Úprimne, dnes si hlasnejší než celý národný tím.", "level": "A2", "topic": "Adjective comparison", "answer": "Honestly, today you're faster than the whole national team."}
{"jid": "q0074", "slovak": "Táto váha ukazuje oveľa viac ako pred chvíľou.", "level": "A1", "topic": "This, That, These...", "answer": "This scale shows way more than it did a moment ago."}
{"jid": "q0075", "slovak": "Vraj sa rúti dolu tou riekou každé leto, kamoška.", "level": "B2", "topic": "All Present Tenses", "answer": "They say he races down that river every summer, bestie."}
{"jid": "q0076", "slovak": "Špinavú dlážku čistí v pondelok ráno. Absolútna katastrofa!", "level": "A1", "topic": "Prepositions of place/time", "answer": "She cleaned the dirty floor on Monday morning. An absolute disaster!"}
{"jid": "q0077", "slovak": "Táto ceruzka je ostrejšia ako tá tupá.", "level": "A2", "topic": "Adjective comparison", "answer": "This pencil is sharper than that blunt one."}
{"jid": "q0078", "slovak": "Pri ľade kráčajú ďalšie dva tučniaky", "level": "A1", "topic": "Singular and plural", "answer": "Two more penguins walked by the ice."}
{"jid": "q0079", "slovak": "Katastrofa! Ona nemá čas na dlhú návštevu!", "level": "A2", "topic": "Countable and uncountable", "answer": "Catastrophe! She has no time for a long visit!"}
{"jid": "q0080", "slovak": "Potrebuje si dať starý akordeón opraviť, kým klávesy úplne neprestanú fungovať.", "level": "B2", "topic": "Causative HAVE/GET", "answer": "Before the keys stop working completely, they need to have the old accordion repaired."}
{"jid": "q0081", "slovak": "Model stíhačky opeká chlieb približne tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The model fighter jet has been toasting the bread for about three minutes."}
{"jid": "q0082", "slovak": "Táto váha ukazuje oveľa viac ako pred chvíľou.", "level": "A1", "topic": "This, That, These...", "answer": "This scale shows a lot more than a moment ago."}
{"jid": "q0083", "slovak": "Už päť minút hľadá gumičku do vlasov a na zápästí má tri.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "She looked for a hair tie for five minutes and had three on her wrist."}
{"jid": "q0084", "slovak": "Ten strážnik o syre nemôže vedieť — rampu dvíha príliš rýchlo.", "level": "B1", "topic": "Modal verbs Probability", "answer": "That guard cannot know about the cheese - the ramp is being raised by him too fast."}
{"jid": "q0085", "slovak": "Ty zvyčajne nenávidíš rady, ale včera večer si čakala na záchod. Rešpekt.", "level": "A2", "topic": "Present or Past Simple", "answer": "You usually hate queues, but last night you waited for the toilet. Respect."}
{"jid": "q0086", "slovak": "Kým došiel k úzkemu chodníku, on zliezal hodinu dolu po skalných rímsach.", "level": "B2", "topic": "All Past Tenses", "answer": "He had been coming down the rocky ledges for an hour by the time he got to the narrow footpath."}
{"jid": "q0087", "slovak": "Pri ľade kráčajú ďalšie dva tučniaky", "level": "A1", "topic": "Singular and plural", "answer": "Two more penguins are walking by the ice."}
{"jid": "q0088", "slovak": "Vraj sa rúti dolu tou riekou každé leto, kamoška.", "level": "B2", "topic": "All Present Tenses", "answer": "Apparently he goes hurtling down that river every summer, girl."}
{"jid": "q0089", "slovak": "Stíhačkový hriankovač ohrieva tie isté dva krajce už tri minúty.", "level": "B1", "topic": "Present Perfect Continuous", "answer": "The same two slices have been heated for three minutes."}
{"jid": "q0090", "slovak": "Kým spustil kanvicu, všetci, čo zízali na jeho fúzy, úplne stíchli!", "level": "B1", "topic": "Past Perfect Simple", "answer": "By the time he switched on the kettle, everyone who was staring at his moustache had fallen completely silent!"}
{"jid": "q0091", "slovak": "Napíše svoje meno na poslednú stranu zmluvy na novú prácu a kancelária tlieska.", "level": "B2", "topic": "Articles advanced", "answer": "They write their name on the last page of the new job contract and the office claps."}
{"jid": "q0092", "slovak": "Stojí bosý na teplom piesku.", "level": "A1", "topic": "Prepositions of place/time", "answer": "Barefoot, he is standing on the warm sand."}
{"jid": "q0093", "slovak": "Pri ľade kráčajú ďalšie dva tučniaky", "level": "A1", "topic": "Singular and plural", "answer": "Two more penguins are walking by ice."}
{"jid": "q0094", "slovak": "Poprosila ma, aby som nehýbal rukou, kým spí.", "level": "B2", "topic": "Reported speech", "answer": "She asked me not to move my arm."}
{"jid": "q0095", "slovak": "Kdeže, gekón práve teraz chrlí oheň, lebo papričky sú také pálivé.", "level": "B2", "topic": "All Present Tenses", "answer": "No way, the gecko is going to spit fire right now, because the peppers are so hot."}
{"jid": "q0096", "slovak": "Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe.", "level": "B2", "topic": "All Present Tenses", "answer": "Status update: the closet will stay tidy for 3 weeks in a row."}
{"jid": "q0097", "slovak": "Aktualizácia stavu: skriňa zostala uprataná 3 týždne po sebe.", "level": "B2", "topic": "All Present Tenses", "answer": "Status update: the closet has stayed empty for 3 weeks in a row."}
{"jid": "q0098", "slovak": "Hore je vietor. Môžeš vidieť tú vlajku?", "level": "A1", "topic": "Modal verb CAN", "answer": "It's windy up there. Can you see the flag?"}
{"jid": "q0099", "slovak": "V momente, keď barla dopadla na mokrú podlahu, chytil ju pevne a šiel ďalej.", "level": "B1", "topic": "Past Simple or Continuos", "answer": "The moment the crutch hit wet floor, he grabbed it firmly and went on."}
