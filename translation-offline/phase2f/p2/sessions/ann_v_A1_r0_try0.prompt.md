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
{"n": 14800, "src": "Rukou zastaví ten točící se globus.", "en": "She stops the spinning globe with her hand.", "lk_supplied": "the", "topic": "A, AN, THE", "level": "A1", "person": null, "number": null, "perfective_present": true}
{"n": 11258, "src": "Křičí a jeho prst má přímo u jejího obličeje.", "en": "He shouts and his finger is right in her face.", "lk_supplied": "his", "topic": "My, Your, His,...", "level": "A1", "person": "3sg", "number": "sg", "perfective_present": null}
{"n": 28191, "src": "On sedí na dlouhé dřevěné lavičce v parku.", "en": "He sits on a long wooden bench in the park.", "lk_supplied": "sits", "topic": "Present Simple", "level": "A1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 17949, "src": "Rybář ji učí svoje vlastní slova.", "en": "The fisherman teaches her his own words.", "lk_supplied": "his", "topic": "My, Your, His,...", "level": "A1", "person": null, "number": null, "perfective_present": false}
{"n": 21420, "src": "Dokážeš projít mezi lany taky?", "en": "Can you climb through the ropes too?", "lk_supplied": "Can", "topic": "Modal verb CAN", "level": "A1", "person": "2sg", "number": "sg", "perfective_present": true}
{"n": 19545, "src": "Namáčí chleba do svého oblíbeného olivového oleje.", "en": "She dips her bread into her favourite olive oil.", "lk_supplied": "her", "topic": "My, Your, His,...", "level": "A1", "person": null, "number": null, "perfective_present": true}
{"n": 24340, "src": "Kdo to je? Studentka v červeném baretu.", "en": "Who is she? A student in a red beret.", "lk_supplied": "Who", "topic": "Wh- questions", "level": "A1", "person": null, "number": null, "perfective_present": false}
{"n": 32425, "src": "Jeden pohled a odborník ničí sen celé rodiny!", "en": "One look and the expert ruins the whole family's dream!", "lk_supplied": "ruins", "topic": "Present Simple", "level": "A1", "person": null, "number": null, "perfective_present": null}
{"n": 25750, "src": "Pět set studentů může sedět v této přednáškové síni.", "en": "Five hundred students can sit in this lecture hall.", "lk_supplied": "can", "topic": "Modal verb CAN", "level": "A1", "person": "3sg", "number": "sg", "perfective_present": null}
{"n": 34429, "src": "Ona píše svůj plán do diáře.", "en": "She writes her plan in a planner.", "lk_supplied": "her", "topic": "My, Your, His,...", "level": "A1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 29958, "src": "Mraky skrývají silnice a města dole.", "en": "The clouds hide the roads and the cities below.", "lk_supplied": "cities", "topic": "Singular and plural", "level": "A1", "person": "3pl", "number": "pl", "perfective_present": null}
{"n": 33795, "src": "S klíčem ona může odemknout zámek.", "en": "With the key, she can open the lock.", "lk_supplied": "can", "topic": "Modal verb CAN", "level": "A1", "person": "3sg", "number": "sg", "perfective_present": null}
{"n": 20725, "src": "Dóza s pudrem stojí na malém stolku.", "en": "The jar of powder stands on the small table.", "lk_supplied": "on", "topic": "Prepositions of place/time", "level": "A1", "person": null, "number": null, "perfective_present": false}
{"n": 34157, "src": "Dvě obrovské řady jsou na protilehlých stranách a nikdo nepřechází!", "en": "Two huge lines are on opposite sides, and nobody crosses!", "lk_supplied": "are", "topic": "TO BE", "level": "A1", "person": "3pl", "number": "pl", "perfective_present": null}
{"n": 13785, "src": "Tyhle sušenky na plechu voní úžasně.", "en": "These cookies on the tray smell amazing.", "lk_supplied": "These", "topic": "This, That, These...", "level": "A1", "person": null, "number": null, "perfective_present": null}
{"n": 14936, "src": "Slon má dva dlouhé bílé kly.", "en": "The elephant has got two long white tusks.", "lk_supplied": "has got", "topic": "HAVE GOT", "level": "A1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 28437, "src": "Termín pátek: potřebujeme fotku modrého moře.", "en": "Deadline Friday: we need a photo of the blue sea.", "lk_supplied": "a", "topic": "A, AN, THE", "level": "A1", "person": "1pl", "number": "pl", "perfective_present": true}
{"n": 16471, "src": "Před každým plaváním si nandá brýle.", "en": "She puts her goggles on before every swim.", "lk_supplied": "puts", "topic": "Present Simple", "level": "A1", "person": null, "number": null, "perfective_present": null}
{"n": 31264, "src": "Tyhle duny v poušti jsou velmi vysoké.", "en": "These dunes in the desert are very high.", "lk_supplied": "These", "topic": "This, That, These...", "level": "A1", "person": "3pl", "number": "pl", "perfective_present": null}
{"n": 16286, "src": "Žirafa pije se dvěma předníma nohama od sebe.", "en": "The giraffe drinks with two front legs wide apart.", "lk_supplied": "two", "topic": "Cardinal numbers", "level": "A1", "person": null, "number": null, "perfective_present": null}
{"n": 15695, "src": "Nebe nad mraky je úplně zlaté.", "en": "The sky above the clouds is totally golden.", "lk_supplied": "is", "topic": "TO BE", "level": "A1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 33585, "src": "Tenhle polibek je na jeho tváři, takže je to polibek na tvář.", "en": "This kiss is on his cheek, so it is a cheek kiss.", "lk_supplied": "This", "topic": "This, That, These...", "level": "A1", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 22494, "src": "V tomhle malém holičství pracují dva holiči", "en": "Two barbers work in this small barbershop.", "lk_supplied": "barbers", "topic": "Singular and plural", "level": "A1", "person": "3pl", "number": "pl", "perfective_present": null}
{"n": 19346, "src": "Položí si svou ruku na hruď a dýchá.", "en": "He puts his hand on his chest and breathes.", "lk_supplied": "his", "topic": "My, Your, His,...", "level": "A1", "person": null, "number": null, "perfective_present": true}
{"n": 34193, "src": "Majitelka je v své kavárně, takže není mimo ni.", "en": "The owner is in her cafe, so she is not outside it.", "lk_supplied": "in", "topic": "Prepositions of place/time", "level": "A1", "person": "3sg", "number": "sg", "perfective_present": false}