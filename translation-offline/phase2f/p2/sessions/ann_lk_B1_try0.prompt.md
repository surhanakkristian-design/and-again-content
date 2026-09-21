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
{"n": 37932, "en": "She screamed that someone had moved the compass and the trip was ruined!", "correct_answer_en": "had moved"}
{"n": 394, "en": "They are soaked through and out of breath because they have been pushing up that ridge since sunrise.", "correct_answer_en": "have been pushing"}
{"n": 4689, "en": "If she tips that basin now, all the soapy water will end up in the flower bed.", "correct_answer_en": "tips"}
{"n": 867, "en": "If it flaps hard enough, it will cross the whole bay without touching the water.", "correct_answer_en": "flaps"}
{"n": 3840, "en": "'Good hygiene isn't hard, is it?' he says with a big thumbs up.", "correct_answer_en": "is it"}
{"n": 596, "en": "The shot put was thrown nearly fifteen metres down the field.", "correct_answer_en": "was thrown"}
{"n": 36598, "en": "If the man in the kandura disliked the designs, there would be no agreement today.", "correct_answer_en": "would be"}
{"n": 1413, "en": "If she spreads any more butter on that slice, it will fall apart.", "correct_answer_en": "spreads"}
{"n": 43995, "en": "Ok so, she told me she had burst into tears because the A+ was not enough.", "correct_answer_en": "had burst"}
{"n": 3326, "en": "All the rejected clothes are put back on the hangers by a shop assistant.", "correct_answer_en": "are put"}
{"n": 9497, "en": "She can't be nervous — look how steady her hands are on the podium.", "correct_answer_en": "can't"}
{"n": 43284, "en": "The last space on the street was taken by a tiny blue car! Absolutely unbelievable!", "correct_answer_en": "was taken"}
{"n": 9902, "en": "Her style beat theirs, didn't it?", "correct_answer_en": "didn't it"}
{"n": 2384, "en": "By the time she reached the counter, she had forgotten completely about the fruit in her suitcase.", "correct_answer_en": "had forgotten"}
{"n": 9250, "en": "If you walk any closer, the cats will jump off the block.", "correct_answer_en": "will jump"}
{"n": 4813, "en": "Every summer of her childhood her grandmother would wash the shirts in this courtyard.", "correct_answer_en": "would"}
{"n": 44145, "en": "If the frosting were sour, her tongue would stay inside her mouth.", "correct_answer_en": "would stay"}
{"n": 861, "en": "It let go of the stone roof, opened its wings and flapped twice to stay in the air.", "correct_answer_en": "flapped"}
{"n": 8580, "en": "While the books were wobbling on top, he walked down the hallway.", "correct_answer_en": "were wobbling"}
{"n": 38285, "en": "This crossing used to be part of her 20-minute commute before the department moved.", "correct_answer_en": "used to"}
{"n": 8371, "en": "If the blocks slip, all three will end up on the mat.", "correct_answer_en": "will end up"}
{"n": 3126, "en": "This time tomorrow she will be wearing that gold shade on stage, under real lights.", "correct_answer_en": "will be wearing"}
{"n": 1132, "en": "While the other passengers were waiting in the queue, she was already walking down the jet bridge.", "correct_answer_en": "were waiting"}
{"n": 6161, "en": "She was sighing quietly when the bus stopped at the red light.", "correct_answer_en": "stopped"}
{"n": 7354, "en": "If you breathe deeply, your lungs fill with more air.", "correct_answer_en": "fill"}