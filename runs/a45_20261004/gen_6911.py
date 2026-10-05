from gen_6907_6909_6910_6911_lib import keys, write
man = keys([(0.42,0.25,0.87,0.78),(0.42,0.24,0.85,0.78),(0.41,0.24,0.84,0.79),(0.41,0.23,0.83,0.79),
            (0.41,0.23,0.80,0.79),(0.40,0.22,0.80,0.80),(0.36,0.22,0.80,0.80),(0.36,0.21,0.81,0.81)])
woman = keys([(0.0,0.31,0.17,0.76),(0.0,0.31,0.19,0.76),(0.0,0.31,0.17,0.76),(0.0,0.31,0.19,0.76),
              (0.0,0.31,0.15,0.76),(0.0,0.31,0.16,0.76),(0.0,0.31,0.13,0.76),(0.0,0.31,0.14,0.76)])
bike = keys([(0.17,0.29,0.33,0.76),(0.19,0.29,0.35,0.76),(0.17,0.29,0.33,0.76),(0.19,0.29,0.35,0.76),
             (0.15,0.28,0.33,0.77),(0.16,0.28,0.33,0.77),(0.13,0.27,0.31,0.78),(0.14,0.27,0.32,0.78)])
write({"mediaId": 6911, "level": "B", "keyWord": "bunch", "defaultVoice": "male",
 "taps": [
  {"phrase": "to shield his head", "target": "the man in the T-shirt", "voice": "male", "keys": man},
  {"phrase": "to clutch a cake box", "target": "the woman with the cake", "voice": "female", "keys": woman},
  {"phrase": "to grip the handlebars", "target": "the man with the bicycle", "voice": "male", "keys": bike}],
 "stillS": 0.2,
 "nouns": [{"word": "a bus shelter", "x": 0.32, "y": 0.17, "voice": "male"},
           {"word": "a paper bag", "x": 0.78, "y": 0.30, "voice": "male"},
           {"word": "a cake box", "x": 0.12, "y": 0.43, "voice": "male"},
           {"word": "a double-decker", "x": 0.86, "y": 0.52, "voice": "male"}],
 "question": "What is the soaked man doing?",
 "answer": ["He", "is", "shielding", "his", "head", "with", "a", "paper", "bag."],
 "answerVoice": "male",
 "notes": "Key word bunch is a verb (people bunch together), not placed as a noun. The bus is right behind the soaked man's back, so it is not a tap target (boxes would overlap). Woman box and bicycle-man box split around x 0.13-0.19; the bicycle's front wheel partly falls in the woman's box. Soaked man's leg reaches x 0.37 from 3.2 s, close to the woman in the black jacket (not a target)."})
