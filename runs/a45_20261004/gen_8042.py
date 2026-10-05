from gen_8038_8041_8042_8043_lib import *
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
split = {0.2: 0.68, 0.7: 0.70, 1.2: 0.72, 1.7: 0.74, 2.2: 0.76, 2.7: 0.80, 3.2: 0.80, 3.7: 0.82}
top = {0.2: 0.21, 0.7: 0.19, 1.2: 0.19, 1.7: 0.18, 2.2: 0.16, 2.7: 0.15, 3.2: 0.13, 3.7: 0.12}
man = keys(T, lambda t: (0.0, top[t], split[t], 1.0))
woman = keys(T, lambda t: (split[t] + 0.01, 0.25, 1.0, 0.72))
write(8042, {
 "mediaId": 8042, "level": "B", "keyWord": "well up", "defaultVoice": "male",
 "taps": [
  {"phrase": "to burst into tears", "target": "the man", "voice": "male", "keys": man},
  {"phrase": "to cuddle a beagle puppy", "target": "the man", "voice": "male", "keys": man},
  {"phrase": "to beam with delight", "target": "the woman", "voice": "female", "keys": woman},
 ],
 "stillS": 0.2,
 "nouns": [
  {"word": "a stained glass window", "x": 0.55, "y": 0.12, "voice": "male"},
  {"word": "balloons", "x": 0.22, "y": 0.30, "voice": "male"},
  {"word": "a beagle", "x": 0.55, "y": 0.52, "voice": "male"},
  {"word": "a wicker basket", "x": 0.86, "y": 0.70, "voice": "male"},
 ],
 "question": "What is the man doing?",
 "answer": ["He", "is", "cuddling", "a", "beagle", "puppy."],
 "answerVoice": "male",
 "notes": "The puppy is held against the man's chest, so it is not a separate target (its box would overlap his). Man/woman boxes split along the woman's left edge, moving right as the man leans in; his knees at the bottom right fall outside his box. Eyes fill with tears 0.2-1.7 s, open crying 2.7-3.7 s. 'a wicker basket' is pinned on the open basket beside the woman; a second wicker basket edge shows at the very bottom right.",
})
