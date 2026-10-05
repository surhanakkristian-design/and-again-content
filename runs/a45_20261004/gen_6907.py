from gen_6907_6909_6910_6911_lib import keys, write
dog = keys([(0.27,0.34,0.49,0.51)]*6 + [(0.25,0.34,0.47,0.51),(0.23,0.34,0.45,0.51)])
hood = keys([(0.65,0.42,0.95,0.77)]*6 + [(0.67,0.42,0.95,0.77)]*2)
lying = keys([(0.06,0.52,0.64,0.68)]*6 + [(0.06,0.52,0.66,0.68)]*2)
write({"mediaId": 6907, "level": "B", "keyWord": "buddy", "defaultVoice": "male",
 "taps": [
  {"phrase": "to balance on the sofa", "target": "the dog", "voice": "male", "keys": dog},
  {"phrase": "to spill a hot drink", "target": "the man in the hood", "voice": "male", "keys": hood},
  {"phrase": "to lie across their laps", "target": "the lying man", "voice": "male", "keys": lying}],
 "stillS": 0.7,
 "nouns": [{"word": "the sun", "x": 0.47, "y": 0.33, "voice": "male"},
           {"word": "a dog", "x": 0.37, "y": 0.43, "voice": "male"},
           {"word": "a flask", "x": 0.84, "y": 0.53, "voice": "male"},
           {"word": "ski poles", "x": 0.82, "y": 0.84, "voice": "male"}],
 "question": "What is the dog doing?",
 "answer": ["The", "dog", "is", "balancing", "on", "the", "sofa."],
 "answerVoice": "male",
 "notes": "Man in the hood spills the drink 0.2-1.7 s, then just holds the flask. Lying man's head is close to the hooded man's arm at 3.2-3.7 s; boxes split at x 0.66. Key word buddy not placed as a noun (five friends, no single slot)."})
