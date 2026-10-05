from gen_7922_7923_7924_7926_lib import keys, write
woman = keys([(0.49,0.11,0.50,0.78),(0.49,0.11,0.50,0.80),(0.49,0.11,0.50,0.84),(0.49,0.11,0.50,0.84),
              (0.49,0.10,0.50,0.89),(0.51,0.10,0.48,0.89),(0.58,0.11,0.41,0.88),(0.60,0.11,0.39,0.88)])
man = keys([(0.01,0.34,0.46,0.56),(0.01,0.34,0.46,0.58),(0.01,0.35,0.46,0.62),(0.01,0.35,0.46,0.62),
            (0.01,0.36,0.46,0.63),(0.01,0.37,0.48,0.62),(0.01,0.38,0.55,0.61),(0.01,0.38,0.57,0.61)])
write({"mediaId": 7922, "level": "B", "keyWord": "on purpose", "defaultVoice": "female",
 "taps": [
  {"phrase": "to pour juice on purpose", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to hold out a tea towel", "target": "the man", "voice": "male", "keys": man},
  {"phrase": "to stare up in disbelief", "target": "the man", "voice": "male", "keys": man}],
 "stillS": 0.2,
 "nouns": [{"word": "cupboards", "x": 0.30, "y": 0.28, "voice": "female"},
           {"word": "a kettle", "x": 0.61, "y": 0.46, "voice": "female"},
           {"word": "a tea towel", "x": 0.45, "y": 0.69, "voice": "female"},
           {"word": "a puddle", "x": 0.45, "y": 0.90, "voice": "female"}],
 "question": "What is the woman doing?",
 "answer": ["She", "is", "pouring", "juice", "on purpose."],
 "answerVoice": "female",
 "notes": "'on purpose' read from her calm smile while she pours onto the towel; the man's towel hands reach into the woman's area, man box cut at her left edge."})
