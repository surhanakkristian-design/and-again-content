from gen_5585_5587_5588_5589_lib import *
Wm = keys([(0.23,0.26,0.49,0.93),(0.24,0.26,0.53,0.92),(0.22,0.26,0.53,0.89),(0.07,0.27,0.37,0.89),
           (0.07,0.29,0.42,0.86),(0.09,0.29,0.53,0.85),(0.15,0.29,0.55,0.85),(0.21,0.33,0.55,0.85)])
M = keys([(0.01,0.35,0.22,0.81),(0.07,0.34,0.24,0.80),(0.10,0.41,0.22,0.79),(0.37,0.34,0.53,0.79),
          (0.42,0.34,0.65,0.61),(0.56,0.32,0.80,0.61),(0.74,0.33,0.94,0.61),None])
P = keys([(0.49,0.49,0.73,0.67),(0.53,0.61,0.77,0.78),(0.53,0.62,0.76,0.79),(0.53,0.61,0.77,0.78),
          (0.53,0.61,0.76,0.77),(0.53,0.61,0.75,0.76),(0.55,0.61,0.75,0.75),(0.55,0.61,0.74,0.75)])
write({
 "mediaId": 5589, "level": "A", "keyWord": "average", "defaultVoice": "female",
 "taps": [
  {"phrase": "to shrug and laugh", "target": "the woman", "voice": "female", "keys": Wm},
  {"phrase": "to push a wheelbarrow", "target": "the man", "voice": "male", "keys": M},
  {"phrase": "to fall onto the hay", "target": "the middle pumpkin", "voice": "female", "keys": P},
 ],
 "stillS": 2.2,
 "nouns": [
  {"word": "the sky", "x": 0.15, "y": 0.15, "voice": "female"},
  {"word": "a tree", "x": 0.70, "y": 0.20, "voice": "female"},
  {"word": "a big pumpkin", "x": 0.85, "y": 0.68, "voice": "female"},
  {"word": "hay", "x": 0.70, "y": 0.80, "voice": "female"},
 ],
 "question": "What is the woman doing?",
 "answer": ["She", "is", "shrugging", "and", "laughing."],
 "answerVoice": "female",
 "notes": "Pumpkin falls only at 0.2 s (in the air), then rests on the bale. Man walks behind the woman at 1.2-1.7 s (partly hidden; narrow box) and behind the pumpkins from 2.2 s, so his box stops above the pumpkin; off at 3.7 s (only an arm at the edge). Woman's outstretched hand is cut at 0.2-0.7 s and 3.7 s to keep clear of the pumpkin."
})
