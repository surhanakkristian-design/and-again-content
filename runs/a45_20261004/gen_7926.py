from gen_7922_7923_7924_7926_lib import keys, write
woman = keys([(0.12,0.36,0.41,0.45),(0.10,0.31,0.49,0.57),(0.21,0.29,0.58,0.67),(0.24,0.25,0.57,0.73),
              (0.18,0.24,0.64,0.75),(0.16,0.23,0.67,0.76),(0.15,0.24,0.68,0.75),(0.13,0.23,0.71,0.76)])
stag = keys([(0.55,0.29,0.37,0.38),(0.61,0.30,0.36,0.37),(0.00,0.41,0.20,0.30),(0.00,0.46,0.20,0.30),
             None, None, None, None])
write({"mediaId": 7926, "level": "B", "keyWord": "out of nowhere", "defaultVoice": "female",
 "taps": [
  {"phrase": "to leap across the path", "target": "the stag", "voice": "female", "keys": stag},
  {"phrase": "to skid to a halt", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to gasp in shock", "target": "the woman", "voice": "female", "keys": woman}],
 "stillS": 0.2,
 "nouns": [{"word": "a helmet", "x": 0.22, "y": 0.39, "voice": "female"},
           {"word": "a stag", "x": 0.70, "y": 0.47, "voice": "female"},
           {"word": "a mountain bike", "x": 0.38, "y": 0.66, "voice": "female"},
           {"word": "fallen leaves", "x": 0.55, "y": 0.90, "voice": "female"}],
 "question": "What is the stag doing?",
 "answer": ["It", "is", "leaping", "across", "the", "path."],
 "answerVoice": "female",
 "notes": "stag only visible 0.2-1.7 s (at the left edge, partly hidden, at 1.2/1.7); at 0.2/0.7 the stag's front overlaps the bike's rear wheel, split vertically (woman box cuts the rear wheel). Skid shown by dust at 0.2-0.7 s."})
