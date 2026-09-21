You judge the "lk" field of a translation-checking pipeline. lk = the key verb phrase of an English translation:
the span of the English sentence that the exercise practises (the phrase the learner must produce), verbatim from the sentence.
For each row you see the English sentence "en" and the exercise's stored answer "correct_answer_en". Classify correct_answer_en as lk:
exact = usable as lk as is (a verbatim span of en that is the practised phrase);
adjust = overlaps the practised phrase but needs trimming or extension (give the corrected verbatim span of en);
unusable = not a span of en, or does not identify the practised phrase.
Reply with ONLY a JSON array, one object per row:
{"n": int, "class": "exact"|"adjust"|"unusable", "lk": str|null (the corrected span for adjust, else null), "reason": str (<= 8 words), "lk_fixed": str (the correct key verb phrase, a verbatim span of en)}
Always fill lk_fixed with the span of en you consider correct, copied verbatim from en (equal to correct_answer_en when the class is exact).
No prose, no fences.
Rows:
{"n": 18549, "en": "There is one big palette on the table.", "correct_answer_en": "is"}
{"n": 30786, "en": "Bruh, one cry lowkey makes so much noise.", "correct_answer_en": "noise."}
{"n": 32988, "en": "Party rule: everyone has to give a gift, because a gift is for giving.", "correct_answer_en": "has to"}
{"n": 24314, "en": "Yesterday she tied the box with string too.", "correct_answer_en": "tied"}
{"n": 33220, "en": "Very smart, obviously. Right now he is wearing a fur hat in the sauna.", "correct_answer_en": "is wearing"}
{"n": 26623, "en": "Yesterday she sheared the same sheep.", "correct_answer_en": "sheared"}
{"n": 31546, "en": "You do not need much water for a dirty floor. Impressed.", "correct_answer_en": "water"}
{"n": 24161, "en": "He lights the burners very quickly.", "correct_answer_en": "quickly"}
{"n": 34672, "en": "You record it again because the first shot is bad? Respect.", "correct_answer_en": "because"}
{"n": 13902, "en": "She coughs less today, but she coughed a lot yesterday.", "correct_answer_en": "coughs"}
{"n": 29898, "en": "Yo, he was tryna close the gate, but the lock got stuck.", "correct_answer_en": "but"}
{"n": 21456, "en": "They come here every autumn, but yesterday they came late.", "correct_answer_en": "came"}
{"n": 16738, "en": "Look! She is brushing her hair with the brush right now.", "correct_answer_en": "is brushing"}
{"n": 15288, "en": "The toy leans, but it does not fall over.", "correct_answer_en": "but"}
{"n": 15746, "en": "He came back suddenly out of the mist.", "correct_answer_en": "suddenly"}
{"n": 32356, "en": "Normally she just reads, but today she is collecting evidence. Bruh, unhinged.", "correct_answer_en": "is collecting"}
{"n": 33263, "en": "Flawless. He usually packs light, but yesterday he carried a heavy tower.", "correct_answer_en": "carried"}
{"n": 12067, "en": "How many empty chairs are in the room?", "correct_answer_en": "many"}
{"n": 14385, "en": "She usually works in bed, but today she is sitting at a desk.", "correct_answer_en": "is sitting"}
{"n": 16437, "en": "The goal is very heavy. You must carry it together!", "correct_answer_en": "must"}
{"n": 33132, "en": "She aims her gun at the target. She is going to fire.", "correct_answer_en": "is going to fire"}
{"n": 16661, "en": "He laid the vegetables neatly on the white plate.", "correct_answer_en": "neatly"}
{"n": 25316, "en": "Look! She is passing the baton to him now.", "correct_answer_en": "is passing"}
{"n": 24018, "en": "There is one small camera above the door.", "correct_answer_en": "is"}
{"n": 29546, "en": "Your kitchen is cheap, but your food looks amazing. Respect.", "correct_answer_en": "but"}