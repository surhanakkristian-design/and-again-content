from gen_6907_6909_6910_6911_lib import keys, write
beetle = keys([(0.12,0.31,0.67,0.61),(0.12,0.30,0.69,0.61),(0.11,0.30,0.68,0.59),(0.12,0.29,0.76,0.61),
               (0.11,0.28,0.78,0.62),(0.13,0.27,0.80,0.63),(0.12,0.25,0.81,0.63),(0.13,0.26,0.84,0.65)])
mantis = keys([(0.72,0.39,0.88,0.61),(0.74,0.39,0.88,0.61),(0.75,0.39,0.91,0.62),(0.78,0.39,0.93,0.62),
               (0.80,0.39,0.95,0.62),(0.82,0.39,0.98,0.62),(0.82,0.38,1.0,0.63),(0.86,0.38,1.0,0.63)])
lamp = keys([(0.11,0.15,0.30,0.31),(0.12,0.14,0.31,0.30),(0.10,0.14,0.29,0.30),(0.11,0.15,0.30,0.29),
             (0.09,0.12,0.28,0.28),(0.10,0.10,0.29,0.27),(0.08,0.10,0.26,0.25),(0.07,0.10,0.25,0.26)])
write({"mediaId": 6909, "level": "A", "keyWord": "bug", "defaultVoice": "male",
 "taps": [
  {"phrase": "to walk across the sheet", "target": "the big beetle", "voice": "male", "keys": beetle},
  {"phrase": "to sit on the pole", "target": "the green insect", "voice": "male", "keys": mantis},
  {"phrase": "to shine in the dark", "target": "the lamp", "voice": "male", "keys": lamp}],
 "stillS": 0.2,
 "nouns": [{"word": "a lamp", "x": 0.21, "y": 0.27, "voice": "male"},
           {"word": "a beetle", "x": 0.33, "y": 0.43, "voice": "male"},
           {"word": "bugs", "x": 0.36, "y": 0.72, "voice": "male"},
           {"word": "a box", "x": 0.17, "y": 0.92, "voice": "male"}],
 "question": "What is the big beetle doing?",
 "answer": ["It", "is", "walking", "across", "the", "sheet."],
 "answerVoice": "male",
 "notes": "Mantis named 'the green insect' (A level); it clings to the pole and barely moves. 'bugs' slot on the crowd of small insects in the lower sheet, well away from the big beetle. Camera slowly pushes in, boxes follow."})
