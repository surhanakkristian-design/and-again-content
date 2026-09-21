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
{"n": 18549, "src": "Na stole je jedna velká paletka.", "en": "There is one big palette on the table.", "lk_supplied": "is", "topic": "There is, are", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 30786, "src": "Vole, jeden výkřik nadělá fakt hodně hluku.", "en": "Bruh, one cry lowkey makes so much noise.", "lk_supplied": "noise.", "topic": "Countable and uncountable", "level": "A2", "person": null, "number": null, "perfective_present": true}
{"n": 32988, "src": "Pravidlo oslavy: každý musí dát dárek, protože dárek je na dávání.", "en": "Party rule: everyone has to give a gift, because a gift is for giving.", "lk_supplied": "has to", "topic": "Must, Have to...", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 24314, "src": "Včera krabici taky zavázala provázkem.", "en": "Yesterday she tied the box with string too.", "lk_supplied": "tied", "topic": "Past Simple", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 33220, "src": "Velmi chytré, samozřejmě. Právě teď on má na hlavě v sauně kožešinovou čepici.", "en": "Very smart, obviously. Right now he is wearing a fur hat in the sauna.", "lk_supplied": "is wearing", "topic": "Present Continuous", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 26623, "src": "Včera ostříhala tu samou ovci.", "en": "Yesterday she sheared the same sheep.", "lk_supplied": "sheared", "topic": "Past Simple", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 31546, "src": "Nepotřebuješ hodně vody na špinavou podlahu. Klobouk dolů.", "en": "You do not need much water for a dirty floor. Impressed.", "lk_supplied": "water", "topic": "Countable and uncountable", "level": "A2", "person": "2sg", "number": "sg", "perfective_present": true}
{"n": 24161, "src": "Hořáky zapaluje velmi rychle", "en": "He lights the burners very quickly.", "lk_supplied": "quickly", "topic": "Adverb formation", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": true}
{"n": 34672, "src": "Nahráváš to znovu, protože první záběr je špatný? Klobouk dolů.", "en": "You record it again because the first shot is bad? Respect.", "lk_supplied": "because", "topic": "Basic conjunctions", "level": "A2", "person": "2sg", "number": "sg", "perfective_present": true}
{"n": 13902, "src": "Dneska kašle míň, ale včera kašlala hodně.", "en": "She coughs less today, but she coughed a lot yesterday.", "lk_supplied": "coughs", "topic": "Present or Past Simple", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 29898, "src": "Hele, snažil se zavřít bránu, ale zámek se zasekl.", "en": "Yo, he was tryna close the gate, but the lock got stuck.", "lk_supplied": "but", "topic": "Basic conjunctions", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 21456, "src": "Chodí sem každý podzim, ale včera přišli pozdě.", "en": "They come here every autumn, but yesterday they came late.", "lk_supplied": "came", "topic": "Present or Past Simple", "level": "A2", "person": "3pl", "number": "pl", "perfective_present": false}
{"n": 16738, "src": "Podívej! Právě si češe vlasy kartáčem.", "en": "Look! She is brushing her hair with the brush right now.", "lk_supplied": "is brushing", "topic": "Present Continuous", "level": "A2", "person": null, "number": null, "perfective_present": null}
{"n": 15288, "src": "Hračka se naklání, ale nespadne.", "en": "The toy leans, but it does not fall over.", "lk_supplied": "but", "topic": "Basic conjunctions", "level": "A2", "person": null, "number": null, "perfective_present": true}
{"n": 15746, "src": "Z mlhy se vrátil najednou", "en": "He came back suddenly out of the mist.", "lk_supplied": "suddenly", "topic": "Adverb formation", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 32356, "src": "Normálně jen čte, ale dnes sbírá důkazy. Vole, šílený.", "en": "Normally she just reads, but today she is collecting evidence. Bruh, unhinged.", "lk_supplied": "is collecting", "topic": "Present Continuous or Simple", "level": "A2", "person": null, "number": null, "perfective_present": null}
{"n": 33263, "src": "Dokonalé. On se obvykle balí nalehko, ale včera nesl těžkou věž.", "en": "Flawless. He usually packs light, but yesterday he carried a heavy tower.", "lk_supplied": "carried", "topic": "Present or Past Simple", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 12067, "src": "Kolik prázdných židlí je v místnosti?", "en": "How many empty chairs are in the room?", "lk_supplied": "many", "topic": "Much, Many, Some...", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 14385, "src": "Obvykle pracuje v posteli, ale dneska sedí u stolu.", "en": "She usually works in bed, but today she is sitting at a desk.", "lk_supplied": "is sitting", "topic": "Present Continuous or Simple", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 16437, "src": "Branka je hrozně těžká. Musíte ji nést spolu!", "en": "The goal is very heavy. You must carry it together!", "lk_supplied": "must", "topic": "Must, Have to...", "level": "A2", "person": "2pl", "number": "pl", "perfective_present": false}
{"n": 33132, "src": "Ona míří puškou na terč. Ona se chystá vystřelit.", "en": "She aims her gun at the target. She is going to fire.", "lk_supplied": "is going to fire", "topic": "Going to or Will", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": null}
{"n": 16661, "src": "Zeleninu úhledně naskládal na bílý talíř.", "en": "He laid the vegetables neatly on the white plate.", "lk_supplied": "neatly", "topic": "Adverb formation", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 25316, "src": "Podívej! Právě teď mu podává kolík.", "en": "Look! She is passing the baton to him now.", "lk_supplied": "is passing", "topic": "Present Continuous", "level": "A2", "person": null, "number": null, "perfective_present": true}
{"n": 24018, "src": "Nade dveřmi je jedna malá kamera.", "en": "There is one small camera above the door.", "lk_supplied": "is", "topic": "There is, are", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}
{"n": 29546, "src": "Tvoje kuchyně je levná, ale tvoje jídlo vypadá úžasně. Respekt.", "en": "Your kitchen is cheap, but your food looks amazing. Respect.", "lk_supplied": "but", "topic": "Basic conjunctions", "level": "A2", "person": "3sg", "number": "sg", "perfective_present": false}