from gen_8038_8041_8042_8043_lib import *
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
man = keys(T, (0.40, 0.14, 0.84, 0.47))
dog = keys(T, (0.20, 0.26, 0.40, 0.45))
woman = keys(T, (0.26, 0.47, 1.0, 1.0))
write(8038, {
 "mediaId": 8038, "level": "A", "keyWord": "waste of time", "defaultVoice": "female",
 "taps": [
  {"phrase": "to laugh very hard", "target": "the man", "voice": "male", "keys": man},
  {"phrase": "to hold a small spoon", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to sit behind the man", "target": "the dog", "voice": "female", "keys": dog},
 ],
 "stillS": 0.7,
 "nouns": [
  {"word": "the sky", "x": 0.50, "y": 0.07, "voice": "female"},
  {"word": "a dog", "x": 0.31, "y": 0.32, "voice": "female"},
  {"word": "a spoon", "x": 0.35, "y": 0.55, "voice": "female"},
  {"word": "a rope", "x": 0.30, "y": 0.88, "voice": "female"},
 ],
 "question": "What is the woman holding?",
 "answer": ["She", "is", "holding", "a", "small", "spoon."],
 "answerVoice": "female",
 "notes": "The woman is seen only by her arm, hand and knees (bottom right); her box is the lower right area from y 0.47, the man's box ends at 0.47 so they do not overlap (his legs are outside his box). Key word 'waste of time' is not a visible noun. Her face shows briefly at the top right at 1.2 s, outside her box.",
})
