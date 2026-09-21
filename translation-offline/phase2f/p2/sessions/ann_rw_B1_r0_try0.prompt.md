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
{"n": 394, "lang": "cz", "sk": "Jsou promočení a bez dechu, protože se od svítání prodírali nahoru tím hřebenem.", "en": "They are soaked through and out of breath because they have been pushing up that ridge since sunrise."}
{"n": 4689, "lang": "cz", "sk": "Když ten lavor teď překlopí, všechna mýdlová voda skončí v záhonu.", "en": "If she tips that basin now, all the soapy water will end up in the flower bed."}
{"n": 867, "lang": "cz", "sk": "Když zamává dost silně, přeletí celou zátoku, aniž by se dotkl vody.", "en": "If it flaps hard enough, it will cross the whole bay without touching the water."}
{"n": 36598, "lang": "cz", "sk": "Kdyby se muži v kanduře nelíbily návrhy, dnes by nebyla žádná dohoda.", "en": "If the man in the kandura disliked the designs, there would be no agreement today."}
{"n": 1413, "lang": "cz", "sk": "Když na ten krajíc natře ještě víc másla, rozpadne se.", "en": "If she spreads any more butter on that slice, it will fall apart."}
{"n": 9497, "lang": "cz", "sk": "Nervózní nemůže být — koukni, jak má na pultu klidné ruce.", "en": "She can't be nervous — look how steady her hands are on the podium."}
{"n": 43284, "lang": "cz", "sk": "Poslední místo na ulici bylo obsazeno malinkým modrým autem! Naprosto neuvěřitelné!", "en": "The last space on the street was taken by a tiny blue car! Absolutely unbelievable!"}
{"n": 9902, "lang": "cz", "sk": "Její styl je porazil, že?", "en": "Her style beat theirs, didn't it?"}
{"n": 2384, "lang": "cz", "sk": "Než se dostala k přepážce, na ovoce v kufru už úplně zapomněla", "en": "By the time she reached the counter, she had forgotten completely about the fruit in her suitcase."}
{"n": 9250, "lang": "cz", "sk": "Když půjdeš ještě blíž, kočky seskočí z kvádru.", "en": "If you walk any closer, the cats will jump off the block."}
{"n": 861, "lang": "cz", "sk": "Pustil se kamenného stropu, roztáhl křídla a dvakrát mávl, aby se udržel ve vzduchu.", "en": "It let go of the stone roof, opened its wings and flapped twice to stay in the air."}
{"n": 8580, "lang": "cz", "sk": "Zatímco se knihy nahoře kývaly, šel chodbou.", "en": "While the books were wobbling on top, he walked down the hallway."}
{"n": 8371, "lang": "cz", "sk": "Když kostky ujedou, všechny tři skončí na žíněnce.", "en": "If the blocks slip, all three will end up on the mat."}