from gen_8038_8041_8042_8043_lib import *
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
split = {0.2: 0.51, 0.7: 0.48, 1.2: 0.43, 1.7: 0.40, 2.2: 0.33, 2.7: 0.29, 3.2: 0.27, 3.7: 0.28}
redL = {0.2: 0.27, 0.7: 0.17, 1.2: 0.07, 1.7: 0.03, 2.2: 0.09, 2.7: 0.08, 3.2: 0.06, 3.7: 0.07}
redB = {0.2: 0.60, 0.7: 0.61, 1.2: 0.62, 1.7: 0.64, 2.2: 0.66, 2.7: 0.67, 3.2: 0.67, 3.7: 0.67}
whR = {0.2: 0.68, 0.7: 0.66, 1.2: 0.62, 1.7: 0.60, 2.2: 0.58, 2.7: 0.60, 3.2: 0.58, 3.7: 0.59}
whY = {0.2: (0.34, 0.53), 0.7: (0.34, 0.53), 1.2: (0.35, 0.55), 1.7: (0.36, 0.56), 2.2: (0.40, 0.57), 2.7: (0.43, 0.58), 3.2: (0.44, 0.59), 3.7: (0.44, 0.60)}
ball = {0.2: (0.86, 0.31), 0.7: (0.85, 0.36), 1.2: (0.84, 0.43), 1.7: (0.82, 0.38), 2.2: (0.80, 0.43), 2.7: (0.81, 0.41), 3.2: (0.84, 0.44), 3.7: (0.90, 0.44)}
red = keys(T, lambda t: (redL[t], 0.29, split[t], redB[t]))
white = keys(T, lambda t: (split[t] + 0.01, whY[t][0], whR[t], whY[t][1]))
def bb(t):
    cx, cy = ball[t]; x0 = min(cx - 0.09, 0.81)
    return (x0, cy - 0.07, x0 + 0.18, cy + 0.07)
bk = keys(T, bb)
write(8043, {
 "mediaId": 8043, "level": "A", "keyWord": "wide", "defaultVoice": "male",
 "taps": [
  {"phrase": "to cover his face", "target": "the man in red", "voice": "male", "keys": red},
  {"phrase": "to fall on the grass", "target": "the man in white", "voice": "male", "keys": white},
  {"phrase": "to fly past the goal", "target": "the ball", "voice": "male", "keys": bk},
 ],
 "stillS": 0.2,
 "nouns": [
  {"word": "trees", "x": 0.30, "y": 0.10, "voice": "male"},
  {"word": "a ball", "x": 0.86, "y": 0.30, "voice": "male"},
  {"word": "a dog", "x": 0.86, "y": 0.46, "voice": "male"},
  {"word": "a glove", "x": 0.42, "y": 0.74, "voice": "male"},
 ],
 "question": "What is the man in red doing?",
 "answer": ["He", "is", "covering", "his", "face."],
 "answerVoice": "male",
 "notes": "Man in red holds his head (0.2, 2.2 s), throws out his arms (0.7-1.7 s) and covers his face (2.7-3.7 s); the answer fits the second half. Man in white kneels, then falls back onto the grass from 2.2 s. The ball flies past the goal in the air until ~1.7 s, then lands and rolls near the dog; its box is the minimum 0.18 x 0.14 and covers part of the dog at 1.2-3.2 s (dog is not a target). Red/white boxes split at a vertical line between them that moves left as the man in red steps back. Only one glove is visible at 0.2 s.",
})
