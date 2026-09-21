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
{"n": 6727, "en": "If he hadn't touched the shelf, the jug would still be perfect.", "correct_answer_en": "hadn't touched"}
{"n": 41466, "en": "Bro, that pup should have waited a bit longer, but patience ain't its vibe fr.", "correct_answer_en": "should have"}
{"n": 3150, "en": "She wishes the gold looked as bright in real life as it does on camera.", "correct_answer_en": "looked"}
{"n": 5620, "en": "She had to get the document stamped before the office closed.", "correct_answer_en": "get"}
{"n": 39380, "en": "If the cat had used only clippers, the top wouldn't have been so flat.", "correct_answer_en": "wouldn't have been"}
{"n": 10225, "en": "She wishes the thread wouldn't snap so often.", "correct_answer_en": "wouldn't"}
{"n": 3774, "en": "Halfway up the stairs she wished she had taken the lift instead.", "correct_answer_en": "had taken"}
{"n": 6687, "en": "By six they will have been carrying that guidebook around for five hours.", "correct_answer_en": "will have been carrying"}
{"n": 44608, "en": "Nightmare! By noon I will have read every magazine in this waiting room.", "correct_answer_en": "will have read"}
{"n": 42154, "en": "He tests himself with cards so that he can recall the answers in the exam.", "correct_answer_en": "so that"}
{"n": 42590, "en": "By tonight he will have sanded every birdhouse in the workshop, or it is the end!", "correct_answer_en": "will have sanded"}
{"n": 2985, "en": "By the end of the summer she will have swum every lake in this valley.", "correct_answer_en": "will have swum"}
{"n": 2954, "en": "The company had the footage checked by a weather expert the next day.", "correct_answer_en": "had"}
{"n": 5831, "en": "She had been waiting on that platform for an hour before she gave up standing.", "correct_answer_en": "had been waiting"}
{"n": 3857, "en": "Look at him now - he is drying his face with a clean white towel.", "correct_answer_en": "is drying"}
{"n": 6649, "en": "If he hadn't climbed through the window, he wouldn't have fallen.", "correct_answer_en": "hadn't climbed"}
{"n": 40098, "en": "She had been hoping for a long time before the sprout finally came up.", "correct_answer_en": "had been hoping"}
{"n": 39092, "en": "Never had he seen such a complete failure in his kitchen.", "correct_answer_en": "had he seen"}
{"n": 8813, "en": "The boxer, whose gloves are bright red, laughs at the final bell.", "correct_answer_en": "whose"}
{"n": 43403, "en": "As a result of spinning the chair 30 times, he was unable to meet the deadline.", "correct_answer_en": "As a result of"}
{"n": 3701, "en": "Look at the horizon right now - the sun is shining straight between two blocks of flats.", "correct_answer_en": "is shining"}
{"n": 109, "en": "The stadium, whose seats were completely full, echoed with cheering families.", "correct_answer_en": "whose"}
{"n": 10224, "en": "She wants to get more thread delivered before Friday.", "correct_answer_en": "to get"}
{"n": 2791, "en": "By September they will have been playing this game in that garden for two years.", "correct_answer_en": "will have been playing"}
{"n": 42883, "en": "The sofa, which she shifted across the floor, now faces the window.", "correct_answer_en": "which"}