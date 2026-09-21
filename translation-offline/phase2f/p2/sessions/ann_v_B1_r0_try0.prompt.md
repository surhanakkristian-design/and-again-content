You are the annotation agent of a Czech->English translation-checking pipeline. For each row you get the
Czech sentence "src", the English reference "en", the exercise's stored key phrase "lk_supplied", the exercise topic, and
the three script-derived fields "person" / "number" / "perfective_present" (null = the script abstained; you must author it).

Write, per row:
1. v = 1-2 acceptable English translations of src; v[0] MUST be the reference en verbatim; add a second only if a clearly
   different acceptable translation exists.
2. lk = the key verb phrase of each v (one entry per v entry), each a VERBATIM span of the matching v.
   lk_supplied is the exercise's stored answer and is OFTEN WRONG: about one row in five needs the span trimmed or extended.
   DO NOT COPY lk_supplied BY DEFAULT. Judge it, then set lk[0] to the correct span of v[0] and report:
   lk_verdict = "exact" if lk[0] is character-for-character lk_supplied, "adjusted" if you changed it in any way;
   lk_reason = one clause (<= 8 words) saying why.
3. voice, subject, agent_nom, embedded_agents - for the MAIN clause of src.
4. gender, tf, tense_open, fragment, main_sentence_index.
5. person, number, perfective_present - ONLY on rows where the supplied value is null.

Definitions (Czech): tf = time frame of the MAIN clause: past / present / future (a perfective verb in
present form = future). person = person+number of the main-clause finite verb: 1sg 2sg 3sg 1pl 2pl 3pl.
subject = the overt NOMINATIVE subject NP of the main-clause finite verb, copied verbatim from the Czech
(it may stand anywhere in the clause, not only first), or null if the subject is dropped (pro-drop) or absent.
voice = active_agent (overt nominative subject) / active_prodrop (subject dropped, recoverable from the verb) /
impersonal (no subject possible, e.g. "je známo", "prší") / passive (být + passive participle, or reflexive passive).
agent_nom = true iff voice == active_agent. embedded_agents = overt nominative subjects of subordinate clauses (verbatim list).
number = number of the main-clause finite verb (sg / pl). gender = grammatical gender of the main-clause subject as the
sentence marks it (subject noun or pronoun, past participle, predicative adjective): m / f / n, or null if not marked.
tense_open = true iff more than one English tense is acceptable. perfective_present = true iff the main-clause finite verb
is perfective in present form. fragment = true iff the sentence has no finite main verb. main_sentence_index = if the item
contains more than one sentence, the 0-based index of the sentence whose main clause you labelled (0 otherwise).

Reply with ONLY a JSON array, one object per row, no prose, no fences:
{"n": int, "v": [str], "lk": [str], "lk_verdict": "exact"|"adjusted", "lk_reason": str, "voice": str,
 "subject": str|null, "agent_nom": bool, "embedded_agents": [str], "gender": "m"|"f"|"n"|null, "tf": str,
 "tense_open": bool, "fragment": bool, "main_sentence_index": int,
 "person": str (only if supplied null), "number": str (only if supplied null), "perfective_present": bool (only if supplied null)}
Rows:
{"n": 37932, "src": "Křičela, že někdo posunul kompas a výlet je zničený!", "en": "She screamed that someone had moved the compass and the trip was ruined!", "lk_supplied": "had moved", "topic": "Reported speech", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 394, "src": "Jsou promočení a bez dechu, protože se od svítání prodírali nahoru tím hřebenem.", "en": "They are soaked through and out of breath because they have been pushing up that ridge since sunrise.", "lk_supplied": "have been pushing", "topic": "Present Perfect Simple or Continuos", "level": "B1", "person": "3pl", "number": "pl", "perfective_present": null}
{"n": 4689, "src": "Když ten lavor teď překlopí, všechna mýdlová voda skončí v záhonu.", "en": "If she tips that basin now, all the soapy water will end up in the flower bed.", "lk_supplied": "tips", "topic": "1. Conditional", "level": "B1", "person": null, "number": null, "perfective_present": null}
{"n": 867, "src": "Když zamává dost silně, přeletí celou zátoku, aniž by se dotkl vody.", "en": "If it flaps hard enough, it will cross the whole bay without touching the water.", "lk_supplied": "flaps", "topic": "1. Conditional", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": true}
{"n": 3840, "src": "„Dobrá hygiena není těžká, že jo?“ říká s palcem nahoře.", "en": "'Good hygiene isn't hard, is it?' he says with a big thumbs up.", "lk_supplied": "is it", "topic": "Question tags", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": null}
{"n": 596, "src": "Koule byla hozena skoro patnáct metrů do pole.", "en": "The shot put was thrown nearly fifteen metres down the field.", "lk_supplied": "was thrown", "topic": "Passive", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 36598, "src": "Kdyby se muži v kanduře nelíbily návrhy, dnes by nebyla žádná dohoda.", "en": "If the man in the kandura disliked the designs, there would be no agreement today.", "lk_supplied": "would be", "topic": "2. Conditional", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 1413, "src": "Když na ten krajíc natře ještě víc másla, rozpadne se.", "en": "If she spreads any more butter on that slice, it will fall apart.", "lk_supplied": "spreads", "topic": "1. Conditional", "level": "B1", "person": null, "number": null, "perfective_present": false}
{"n": 43995, "src": "Takže, řekla mi, že se rozbrečela, protože A+ nestačilo.", "en": "Ok so, she told me she had burst into tears because the A+ was not enough.", "lk_supplied": "had burst", "topic": "Reported speech", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 3326, "src": "Všechno odmítnuté oblečení je věšeno zpátky na ramínka prodavačkou.", "en": "All the rejected clothes are put back on the hangers by a shop assistant.", "lk_supplied": "are put", "topic": "Passive", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 9497, "src": "Nervózní nemůže být — koukni, jak má na pultu klidné ruce.", "en": "She can't be nervous — look how steady her hands are on the podium.", "lk_supplied": "can't", "topic": "Modal verbs Probability", "level": "B1", "person": null, "number": null, "perfective_present": null}
{"n": 43284, "src": "Poslední místo na ulici bylo obsazeno malinkým modrým autem! Naprosto neuvěřitelné!", "en": "The last space on the street was taken by a tiny blue car! Absolutely unbelievable!", "lk_supplied": "was taken", "topic": "Passive", "level": "B1", "person": null, "number": null, "perfective_present": null}
{"n": 9902, "src": "Její styl je porazil, že?", "en": "Her style beat theirs, didn't it?", "lk_supplied": "didn't it", "topic": "Question tags", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 2384, "src": "Než se dostala k přepážce, na ovoce v kufru už úplně zapomněla", "en": "By the time she reached the counter, she had forgotten completely about the fruit in her suitcase.", "lk_supplied": "had forgotten", "topic": "Past Perfect Simple", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 9250, "src": "Když půjdeš ještě blíž, kočky seskočí z kvádru.", "en": "If you walk any closer, the cats will jump off the block.", "lk_supplied": "will jump", "topic": "1. Conditional", "level": "B1", "person": null, "number": null, "perfective_present": null}
{"n": 4813, "src": "Každé léto jejího dětství babička právala košile na tomhle dvoře.", "en": "Every summer of her childhood her grandmother would wash the shirts in this courtyard.", "lk_supplied": "would", "topic": "Used to, Would", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 44145, "src": "Kdyby byla poleva kyselá, její jazyk by zůstal v puse.", "en": "If the frosting were sour, her tongue would stay inside her mouth.", "lk_supplied": "would stay", "topic": "2. Conditional", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 861, "src": "Pustil se kamenného stropu, roztáhl křídla a dvakrát mávl, aby se udržel ve vzduchu.", "en": "It let go of the stone roof, opened its wings and flapped twice to stay in the air.", "lk_supplied": "flapped", "topic": "Past Simple or Continuos", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 8580, "src": "Zatímco se knihy nahoře kývaly, šel chodbou.", "en": "While the books were wobbling on top, he walked down the hallway.", "lk_supplied": "were wobbling", "topic": "Past Simple or Continuos", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": true}
{"n": 38285, "src": "Tenhle přechod býval součástí jejího 20minutového dojíždění, než se oddělení přestěhovalo.", "en": "This crossing used to be part of her 20-minute commute before the department moved.", "lk_supplied": "used to", "topic": "Used to, Would", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 8371, "src": "Když kostky ujedou, všechny tři skončí na žíněnce.", "en": "If the blocks slip, all three will end up on the mat.", "lk_supplied": "will end up", "topic": "1. Conditional", "level": "B1", "person": null, "number": null, "perfective_present": true}
{"n": 3126, "src": "Zítra touhle dobou bude mít na sobě ten zlatý odstín na pódiu, pod opravdovými světly.", "en": "This time tomorrow she will be wearing that gold shade on stage, under real lights.", "lk_supplied": "will be wearing", "topic": "Future Continuous", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": null}
{"n": 1132, "src": "Zatímco ostatní cestující čekali ve frontě, ona už kráčela nástupním mostem.", "en": "While the other passengers were waiting in the queue, she was already walking down the jet bridge.", "lk_supplied": "were waiting", "topic": "Past Continuous", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 6161, "src": "Tiše vzdychala, když autobus zastavil na červenou.", "en": "She was sighing quietly when the bus stopped at the red light.", "lk_supplied": "stopped", "topic": "Past Simple or Continuos", "level": "B1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 7354, "src": "Když dýcháš zhluboka, tvoje plíce nabírají víc vzduchu.", "en": "If you breathe deeply, your lungs fill with more air.", "lk_supplied": "fill", "topic": "0 Conditional", "level": "B1", "person": "3pl", "number": "pl", "perfective_present": null}