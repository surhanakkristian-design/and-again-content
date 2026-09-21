You are the arm-B rewrite agent (1J rule) of a Slovak/Czech->English translation-checking pipeline.
For each sentence ("lang": sk = Slovak, cz = Czech; the text is in field "sk" for both): if the MAIN clause has a dropped (pro-drop) subject, insert exactly ONE nominative
personal pronoun (Slovak: ja, ty, on, ona, ono, my, vy, oni, ony; Czech: já, ty, on, ona, ono, my, vy, oni, ony) agreeing with the finite verb, at the natural
position; change NOTHING else (no other word added, removed or altered). If the main clause already has an
overt subject but a subordinate clause has a dropped subject, you may insert the pronoun there (where="embedded").
If the subject is overt or the clause is impersonal, leave the sentence untouched. Use the English reference
only to choose gender/person. Machine check afterwards: new tokens = old tokens + exactly the pronoun.
Reply with ONLY a JSON array, one object per sentence:
{"n": int, "action": "R"|"U", "sk_new": str, "pronoun": str|null, "where": "main"|"embedded"|null, "reason": str}
(reason for U: explicit_subject | impersonal | other). No prose, no code fences.
Sentences:
{"n": 14800, "lang": "cz", "sk": "Rukou zastaví ten točící se globus.", "en": "She stops the spinning globe with her hand."}
{"n": 17949, "lang": "cz", "sk": "Rybář ji učí svoje vlastní slova.", "en": "The fisherman teaches her his own words."}
{"n": 19545, "lang": "cz", "sk": "Namáčí chleba do svého oblíbeného olivového oleje.", "en": "She dips her bread into her favourite olive oil."}
{"n": 24340, "lang": "cz", "sk": "Kdo to je? Studentka v červeném baretu.", "en": "Who is she? A student in a red beret."}
{"n": 32425, "lang": "cz", "sk": "Jeden pohled a odborník ničí sen celé rodiny!", "en": "One look and the expert ruins the whole family's dream!"}
{"n": 20725, "lang": "cz", "sk": "Dóza s pudrem stojí na malém stolku.", "en": "The jar of powder stands on the small table."}
{"n": 13785, "lang": "cz", "sk": "Tyhle sušenky na plechu voní úžasně.", "en": "These cookies on the tray smell amazing."}
{"n": 16471, "lang": "cz", "sk": "Před každým plaváním si nandá brýle.", "en": "She puts her goggles on before every swim."}
{"n": 16286, "lang": "cz", "sk": "Žirafa pije se dvěma předníma nohama od sebe.", "en": "The giraffe drinks with two front legs wide apart."}
{"n": 22494, "lang": "cz", "sk": "V tomhle malém holičství pracují dva holiči", "en": "Two barbers work in this small barbershop."}
{"n": 19346, "lang": "cz", "sk": "Položí si svou ruku na hruď a dýchá.", "en": "He puts his hand on his chest and breathes."}