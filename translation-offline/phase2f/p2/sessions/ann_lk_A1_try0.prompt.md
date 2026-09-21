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
{"n": 14800, "en": "She stops the spinning globe with her hand.", "correct_answer_en": "the"}
{"n": 11258, "en": "He shouts and his finger is right in her face.", "correct_answer_en": "his"}
{"n": 28191, "en": "He sits on a long wooden bench in the park.", "correct_answer_en": "sits"}
{"n": 17949, "en": "The fisherman teaches her his own words.", "correct_answer_en": "his"}
{"n": 21420, "en": "Can you climb through the ropes too?", "correct_answer_en": "Can"}
{"n": 19545, "en": "She dips her bread into her favourite olive oil.", "correct_answer_en": "her"}
{"n": 24340, "en": "Who is she? A student in a red beret.", "correct_answer_en": "Who"}
{"n": 32425, "en": "One look and the expert ruins the whole family's dream!", "correct_answer_en": "ruins"}
{"n": 25750, "en": "Five hundred students can sit in this lecture hall.", "correct_answer_en": "can"}
{"n": 34429, "en": "She writes her plan in a planner.", "correct_answer_en": "her"}
{"n": 29958, "en": "The clouds hide the roads and the cities below.", "correct_answer_en": "cities"}
{"n": 33795, "en": "With the key, she can open the lock.", "correct_answer_en": "can"}
{"n": 20725, "en": "The jar of powder stands on the small table.", "correct_answer_en": "on"}
{"n": 34157, "en": "Two huge lines are on opposite sides, and nobody crosses!", "correct_answer_en": "are"}
{"n": 13785, "en": "These cookies on the tray smell amazing.", "correct_answer_en": "These"}
{"n": 14936, "en": "The elephant has got two long white tusks.", "correct_answer_en": "has got"}
{"n": 28437, "en": "Deadline Friday: we need a photo of the blue sea.", "correct_answer_en": "a"}
{"n": 16471, "en": "She puts her goggles on before every swim.", "correct_answer_en": "puts"}
{"n": 31264, "en": "These dunes in the desert are very high.", "correct_answer_en": "These"}
{"n": 16286, "en": "The giraffe drinks with two front legs wide apart.", "correct_answer_en": "two"}
{"n": 15695, "en": "The sky above the clouds is totally golden.", "correct_answer_en": "is"}
{"n": 33585, "en": "This kiss is on his cheek, so it is a cheek kiss.", "correct_answer_en": "This"}
{"n": 22494, "en": "Two barbers work in this small barbershop.", "correct_answer_en": "barbers"}
{"n": 19346, "en": "He puts his hand on his chest and breathes.", "correct_answer_en": "his"}
{"n": 34193, "en": "The owner is in her cafe, so she is not outside it.", "correct_answer_en": "in"}