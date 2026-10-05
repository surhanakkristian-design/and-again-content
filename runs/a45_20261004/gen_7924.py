from gen_7922_7923_7924_7926_lib import keys, write
woman = keys([(0.29,0.18,0.46,0.66),(0.05,0.22,0.49,0.63),(0.30,0.28,0.36,0.55),(0.22,0.30,0.39,0.53),
              (0.03,0.31,0.54,0.53),(0.20,0.31,0.37,0.53),(0.22,0.32,0.34,0.52),(0.22,0.32,0.34,0.52)])
green = keys([(0.76,0.31,0.13,0.40),(0.72,0.31,0.15,0.39),(0.67,0.32,0.16,0.39),(0.62,0.34,0.18,0.37),
              (0.58,0.34,0.14,0.37),(0.58,0.34,0.15,0.37),(0.57,0.34,0.14,0.37),(0.57,0.34,0.11,0.37)])
write({"mediaId": 7924, "level": "B", "keyWord": "on the spot", "defaultVoice": "female",
 "taps": [
  {"phrase": "to spin round in the street", "target": "the woman in the blazer", "voice": "female", "keys": woman},
  {"phrase": "to swing a leather handbag", "target": "the woman in the blazer", "voice": "female", "keys": woman},
  {"phrase": "to wear green tracksuit bottoms", "target": "the man in green trousers", "voice": "male", "keys": green}],
 "stillS": 2.7,
 "nouns": [{"word": "bunting", "x": 0.35, "y": 0.11, "voice": "female"},
           {"word": "a handbag", "x": 0.27, "y": 0.69, "voice": "female"},
           {"word": "a speaker", "x": 0.68, "y": 0.72, "voice": "female"},
           {"word": "cobbles", "x": 0.50, "y": 0.90, "voice": "female"}],
 "question": "What is the woman in blue doing?",
 "answer": ["She", "is", "dancing", "on the spot."],
 "answerVoice": "female",
 "notes": "busy frame: the green-trousers dancer stands right next to the other shell-suit dancer, his box is narrow (cut at the neighbour); at t=0.2/1.2 the swung handbag reaches his area and is cut from the woman's box. State phrase for him because both dancers move alike."})
