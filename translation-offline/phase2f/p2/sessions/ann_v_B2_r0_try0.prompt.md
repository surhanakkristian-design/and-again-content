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
{"n": 6727, "src": "Kdyby se té police nebyl dotkl, džbán by byl ještě celý.", "en": "If he hadn't touched the shelf, the jug would still be perfect.", "lk_supplied": "hadn't touched", "topic": "3. Conditional", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 41466, "src": "Brácho, to štěně mělo počkat o chvilku dýl, ale trpělivost není jeho vibe, fakt.", "en": "Bro, that pup should have waited a bit longer, but patience ain't its vibe fr.", "lk_supplied": "should have", "topic": "Modals in past", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 3150, "src": "Přála by si, aby zlato vypadalo naživo tak jasně jako na kameře.", "en": "She wishes the gold looked as bright in real life as it does on camera.", "lk_supplied": "looked", "topic": "Wish clauses", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 5620, "src": "Musela si dokument nechat orazítkovat, než úřad zavřel.", "en": "She had to get the document stamped before the office closed.", "lk_supplied": "get", "topic": "Causative HAVE/GET", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 39380, "src": "Kdyby kočka použila jen strojek, vršek by nebyl tak plochý.", "en": "If the cat had used only clippers, the top wouldn't have been so flat.", "lk_supplied": "wouldn't have been", "topic": "3. Conditional", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 10225, "src": "Přeje si, aby se nit netrhala tak často.", "en": "She wishes the thread wouldn't snap so often.", "lk_supplied": "wouldn't", "topic": "Wish clauses", "level": "B2", "person": null, "number": null, "perfective_present": false}
{"n": 3774, "src": "V polovině schodů si přála, aby radši použila výtah.", "en": "Halfway up the stairs she wished she had taken the lift instead.", "lk_supplied": "had taken", "topic": "Wish clauses", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 6687, "src": "Do šesti budou toho průvodce nosit pět hodin.", "en": "By six they will have been carrying that guidebook around for five hours.", "lk_supplied": "will have been carrying", "topic": "Future Perfect Continuous", "level": "B2", "person": "3pl", "number": "pl", "perfective_present": null}
{"n": 44608, "src": "Noční můra! Do poledne já přečtu každý časopis v téhle čekárně.", "en": "Nightmare! By noon I will have read every magazine in this waiting room.", "lk_supplied": "will have read", "topic": "Future Perfect Simple", "level": "B2", "person": null, "number": null, "perfective_present": null}
{"n": 42154, "src": "Zkouší se s kartičkami, aby si u zkoušky dokázal vybavit odpovědi.", "en": "He tests himself with cards so that he can recall the answers in the exam.", "lk_supplied": "so that", "topic": "Advanced linkers", "level": "B2", "person": null, "number": null, "perfective_present": false}
{"n": 42590, "src": "Do večera obrousí všechny budky v dílně, jinak je konec!", "en": "By tonight he will have sanded every birdhouse in the workshop, or it is the end!", "lk_supplied": "will have sanded", "topic": "Future Perfect Simple", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": true}
{"n": 2985, "src": "Do konce léta přeplave každé jezero v tomhle údolí.", "en": "By the end of the summer she will have swum every lake in this valley.", "lk_supplied": "will have swum", "topic": "Future Perfect Simple", "level": "B2", "person": null, "number": null, "perfective_present": null}
{"n": 2954, "src": "Firma si druhý den dala záběry zkontrolovat meteorologem.", "en": "The company had the footage checked by a weather expert the next day.", "lk_supplied": "had", "topic": "Causative HAVE/GET", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 5831, "src": "Na tom nástupišti čekala hodinu, než to vzdala a sedla si.", "en": "She had been waiting on that platform for an hour before she gave up standing.", "lk_supplied": "had been waiting", "topic": "Past Perfect Continuous", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 3857, "src": "Podívej se na něj teď - utírá si obličej čistým bílým ručníkem.", "en": "Look at him now - he is drying his face with a clean white towel.", "lk_supplied": "is drying", "topic": "All Present Tenses", "level": "B2", "person": null, "number": null, "perfective_present": null}
{"n": 6649, "src": "Kdyby nebyl vlezl tím oknem, nebyl by spadl.", "en": "If he hadn't climbed through the window, he wouldn't have fallen.", "lk_supplied": "hadn't climbed", "topic": "3. Conditional", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 40098, "src": "Ona doufala dlouho, než klíček konečně vyrostl.", "en": "She had been hoping for a long time before the sprout finally came up.", "lk_supplied": "had been hoping", "topic": "All Past Tenses", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 39092, "src": "Nikdy neviděl ve své kuchyni tak naprostý neúspěch.", "en": "Never had he seen such a complete failure in his kitchen.", "lk_supplied": "had he seen", "topic": "Inversion basic", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 8813, "src": "Boxerka, jejíž rukavice jsou jasně červené, se při závěrečném gongu směje.", "en": "The boxer, whose gloves are bright red, laughs at the final bell.", "lk_supplied": "whose", "topic": "Relative clauses", "level": "B2", "person": "3pl", "number": "pl", "perfective_present": null}
{"n": 43403, "src": "V důsledku třicetinásobného točení na židli nestihl termín.", "en": "As a result of spinning the chair 30 times, he was unable to meet the deadline.", "lk_supplied": "As a result of", "topic": "Advanced linkers", "level": "B2", "person": null, "number": null, "perfective_present": null}
{"n": 3701, "src": "Podívej se hned teď na obzor - slunce svítí přesně mezi dvěma paneláky.", "en": "Look at the horizon right now - the sun is shining straight between two blocks of flats.", "lk_supplied": "is shining", "topic": "All Present Tenses", "level": "B2", "person": null, "number": null, "perfective_present": null}
{"n": 109, "src": "Stadion, jehož sedadla byla úplně plná, se rozléhal jásotem rodin.", "en": "The stadium, whose seats were completely full, echoed with cheering families.", "lk_supplied": "whose", "topic": "Relative clauses", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 10224, "src": "Chce si nechat dovézt víc nití do pátku.", "en": "She wants to get more thread delivered before Friday.", "lk_supplied": "to get", "topic": "Causative HAVE/GET", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 2791, "src": "Do září budou hrávat tuhle hru v té zahradě dva roky.", "en": "By September they will have been playing this game in that garden for two years.", "lk_supplied": "will have been playing", "topic": "Future Perfect Continuous", "level": "B2", "person": "3pl", "number": "pl", "perfective_present": false}
{"n": 42883, "src": "Gauč, který přesunula po podlaze, je teď otočený k oknu.", "en": "The sofa, which she shifted across the floor, now faces the window.", "lk_supplied": "which", "topic": "Relative clauses", "level": "B2", "person": "3sg", "number": "sg", "perfective_present": false}