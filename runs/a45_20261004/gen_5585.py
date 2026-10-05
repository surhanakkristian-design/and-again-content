from gen_5585_5587_5588_5589_lib import *
# woman left / man right, split on a vertical line between them
split = [0.41, 0.40, 0.39, 0.36, 0.33, 0.31, 0.32, 0.30]
wtop = [0.27, 0.27, 0.27, 0.27, 0.22, 0.22, 0.21, 0.21]
mtop = [0.18, 0.17, 0.17, 0.15, 0.12, 0.12, 0.13, 0.13]
W = keys([(0, wtop[i], split[i], 1) for i in range(8)])
M = keys([(split[i], mtop[i], 1, 1) for i in range(8)])
write({
 "mediaId": 5585, "level": "B", "keyWord": "authentic", "defaultVoice": "male",
 "taps": [
  {"phrase": "to peer through a loupe", "target": "the man", "voice": "male", "keys": M},
  {"phrase": "to shine a small torch", "target": "the woman", "voice": "female", "keys": W},
  {"phrase": "to burst out laughing", "target": "the woman", "voice": "female", "keys": W},
 ],
 "stillS": 0.2,
 "nouns": [
  {"word": "a loupe", "x": 0.69, "y": 0.37, "voice": "male"},
  {"word": "a torch", "x": 0.40, "y": 0.54, "voice": "male"},
  {"word": "a satin blouse", "x": 0.18, "y": 0.70, "voice": "male"},
  {"word": "a gilded frame", "x": 0.82, "y": 0.88, "voice": "male"},
 ],
 "question": "What is the man doing?",
 "answer": ["He", "is", "peering", "through", "a", "loupe."],
 "answerVoice": "male",
 "notes": "Woman's torch hand crosses into the man's chest area; split line set between her face and his. 'to burst out laughing' only at 3.2-3.7 s; man only smiles."
})
