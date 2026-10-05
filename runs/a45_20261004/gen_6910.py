from gen_6907_6909_6910_6911_lib import keys, write
bullet = keys([(0.59,0.40,0.88,0.54),(0.63,0.40,0.93,0.54),(0.65,0.40,0.97,0.54),(0.70,0.40,1.0,0.54),
               (0.73,0.39,1.0,0.53),(0.80,0.39,1.0,0.53),(0.82,0.39,1.0,0.53),None])
apple = keys([(0.0,0.34,0.57,0.60),(0.0,0.34,0.58,0.60),(0.0,0.33,0.59,0.61),(0.0,0.33,0.63,0.61),
              (0.0,0.32,0.66,0.61),(0.0,0.31,0.70,0.62),(0.0,0.30,0.71,0.64),(0.0,0.29,0.71,0.64)])
ice = keys([(0.15,0.70,0.62,0.88),(0.15,0.71,0.63,0.89),(0.14,0.72,0.63,0.89),(0.13,0.72,0.64,0.90),
            (0.11,0.74,0.65,0.92),(0.11,0.74,0.66,0.92),(0.10,0.76,0.66,0.95),(0.10,0.76,0.67,0.96)])
write({"mediaId": 6910, "level": "B", "keyWord": "bullet", "defaultVoice": "female",
 "taps": [
  {"phrase": "to shoot out of the apple", "target": "the bullet", "voice": "female", "keys": bullet},
  {"phrase": "to burst open", "target": "the apple", "voice": "female", "keys": apple},
  {"phrase": "to give off mist", "target": "the block of ice", "voice": "female", "keys": ice}],
 "stillS": 0.7,
 "nouns": [{"word": "gold foil", "x": 0.16, "y": 0.29, "voice": "female"},
           {"word": "an apple", "x": 0.36, "y": 0.45, "voice": "female"},
           {"word": "a bullet", "x": 0.80, "y": 0.47, "voice": "female"},
           {"word": "ice", "x": 0.40, "y": 0.80, "voice": "female"}],
 "question": "What is the bullet doing?",
 "answer": ["It", "is", "shooting", "out", "of", "the", "red", "apple."],
 "answerVoice": "female",
 "notes": "Bullet leaves the frame on the right: visible 0.2-3.2 s (only its tip at 3.2), off at 3.7. Apple box includes the juice splash to the left edge. Bullet already outside the apple at 0.2 s, so the phrase is 'shoot out of', not 'hit'."})
