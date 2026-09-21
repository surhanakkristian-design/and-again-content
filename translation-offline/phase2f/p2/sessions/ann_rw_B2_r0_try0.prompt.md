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
{"n": 6727, "lang": "cz", "sk": "Kdyby se té police nebyl dotkl, džbán by byl ještě celý.", "en": "If he hadn't touched the shelf, the jug would still be perfect."}
{"n": 3150, "lang": "cz", "sk": "Přála by si, aby zlato vypadalo naživo tak jasně jako na kameře.", "en": "She wishes the gold looked as bright in real life as it does on camera."}
{"n": 5620, "lang": "cz", "sk": "Musela si dokument nechat orazítkovat, než úřad zavřel.", "en": "She had to get the document stamped before the office closed."}
{"n": 10225, "lang": "cz", "sk": "Přeje si, aby se nit netrhala tak často.", "en": "She wishes the thread wouldn't snap so often."}
{"n": 3774, "lang": "cz", "sk": "V polovině schodů si přála, aby radši použila výtah.", "en": "Halfway up the stairs she wished she had taken the lift instead."}
{"n": 6687, "lang": "cz", "sk": "Do šesti budou toho průvodce nosit pět hodin.", "en": "By six they will have been carrying that guidebook around for five hours."}
{"n": 44608, "lang": "cz", "sk": "Noční můra! Do poledne já přečtu každý časopis v téhle čekárně.", "en": "Nightmare! By noon I will have read every magazine in this waiting room."}
{"n": 42154, "lang": "cz", "sk": "Zkouší se s kartičkami, aby si u zkoušky dokázal vybavit odpovědi.", "en": "He tests himself with cards so that he can recall the answers in the exam."}
{"n": 2985, "lang": "cz", "sk": "Do konce léta přeplave každé jezero v tomhle údolí.", "en": "By the end of the summer she will have swum every lake in this valley."}
{"n": 2954, "lang": "cz", "sk": "Firma si druhý den dala záběry zkontrolovat meteorologem.", "en": "The company had the footage checked by a weather expert the next day."}
{"n": 3857, "lang": "cz", "sk": "Podívej se na něj teď - utírá si obličej čistým bílým ručníkem.", "en": "Look at him now - he is drying his face with a clean white towel."}
{"n": 6649, "lang": "cz", "sk": "Kdyby nebyl vlezl tím oknem, nebyl by spadl.", "en": "If he hadn't climbed through the window, he wouldn't have fallen."}
{"n": 39092, "lang": "cz", "sk": "Nikdy neviděl ve své kuchyni tak naprostý neúspěch.", "en": "Never had he seen such a complete failure in his kitchen."}
{"n": 43403, "lang": "cz", "sk": "V důsledku třicetinásobného točení na židli nestihl termín.", "en": "As a result of spinning the chair 30 times, he was unable to meet the deadline."}
{"n": 3701, "lang": "cz", "sk": "Podívej se hned teď na obzor - slunce svítí přesně mezi dvěma paneláky.", "en": "Look at the horizon right now - the sun is shining straight between two blocks of flats."}
{"n": 109, "lang": "cz", "sk": "Stadion, jehož sedadla byla úplně plná, se rozléhal jásotem rodin.", "en": "The stadium, whose seats were completely full, echoed with cheering families."}
{"n": 2791, "lang": "cz", "sk": "Do září budou hrávat tuhle hru v té zahradě dva roky.", "en": "By September they will have been playing this game in that garden for two years."}
{"n": 42883, "lang": "cz", "sk": "Gauč, který přesunula po podlaze, je teď otočený k oknu.", "en": "The sofa, which she shifted across the floor, now faces the window."}