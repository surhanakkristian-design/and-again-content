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
{"n": 30786, "lang": "cz", "sk": "Vole, jeden výkřik nadělá fakt hodně hluku.", "en": "Bruh, one cry lowkey makes so much noise."}
{"n": 32988, "lang": "cz", "sk": "Pravidlo oslavy: každý musí dát dárek, protože dárek je na dávání.", "en": "Party rule: everyone has to give a gift, because a gift is for giving."}
{"n": 29898, "lang": "cz", "sk": "Hele, snažil se zavřít bránu, ale zámek se zasekl.", "en": "Yo, he was tryna close the gate, but the lock got stuck."}
{"n": 16738, "lang": "cz", "sk": "Podívej! Právě si češe vlasy kartáčem.", "en": "Look! She is brushing her hair with the brush right now."}
{"n": 15288, "lang": "cz", "sk": "Hračka se naklání, ale nespadne.", "en": "The toy leans, but it does not fall over."}
{"n": 15746, "lang": "cz", "sk": "Z mlhy se vrátil najednou", "en": "He came back suddenly out of the mist."}
{"n": 32356, "lang": "cz", "sk": "Normálně jen čte, ale dnes sbírá důkazy. Vole, šílený.", "en": "Normally she just reads, but today she is collecting evidence. Bruh, unhinged."}
{"n": 25316, "lang": "cz", "sk": "Podívej! Právě teď mu podává kolík.", "en": "Look! She is passing the baton to him now."}