import json, os
RUN = os.path.dirname(os.path.abspath(__file__))

def keys(times, table):
    out = []
    for t in times:
        b = table.get(t)
        if b is None:
            out.append({"t": t, "off": True})
        else:
            out.append({"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out

def T(n):
    return [round(i * 0.5, 1) for i in range(n)]

def rng(a, b):
    return [round(a + i * 0.5, 1) for i in range(int(round((b - a) / 0.5)) + 1)]

def write(d):
    with open(os.path.join(RUN, "content", "%d.json" % d["mediaId"]), "w") as f:
        json.dump(d, f, indent=1, ensure_ascii=False)

# ---------------- 386 ----------------
t = T(21)
man = {}
for x in rng(0.0, 1.5): man[x] = (0.68, 0.0, 0.32, 0.66)
man[2.0] = (0.0, 0.0, 0.2, 0.32)
man[2.5] = (0.0, 0.0, 0.25, 0.42)
man[3.0] = (0.0, 0.08, 0.2, 0.55)
man[3.5] = (0.0, 0.28, 0.36, 0.72)
man[4.0] = (0.0, 0.23, 0.38, 0.77)
man[4.5] = (0.0, 0.13, 0.4, 0.87)
man[5.0] = (0.0, 0.15, 0.42, 0.85)
man[5.5] = (0.0, 0.18, 0.4, 0.82)
man[6.0] = (0.0, 0.58, 0.25, 0.3)
man[6.5] = (0.0, 0.6, 0.45, 0.4)
man[7.0] = (0.0, 0.35, 0.37, 0.65)
man[7.5] = (0.0, 0.2, 0.36, 0.8)
man[8.0] = (0.0, 0.22, 0.36, 0.63)
man[8.5] = (0.0, 0.28, 0.36, 0.54)
man[9.0] = (0.0, 0.27, 0.42, 0.53)
man[9.5] = (0.0, 0.27, 0.4, 0.52)
man[10.0] = (0.02, 0.27, 0.37, 0.5)
cat = {8.0: (0.2, 0.86, 0.4, 0.14), 8.5: (0.2, 0.83, 0.38, 0.15), 9.0: (0.25, 0.8, 0.29, 0.16),
       9.5: (0.26, 0.79, 0.28, 0.15), 10.0: (0.3, 0.78, 0.26, 0.14)}
km, kc = keys(t, man), keys(t, cat)
write({
 "mediaId": 386, "level": "A", "keyWord": "hobby", "defaultVoice": "male",
 "taps": [
  {"phrase": "to have a black beard", "target": "the man", "voice": "male", "keys": km},
  {"phrase": "to show her his boats", "target": "the man", "voice": "male", "keys": km},
  {"phrase": "to lie in a box", "target": "the cat", "voice": "male", "keys": kc},
 ],
 "stillS": 9.5,
 "nouns": [
  {"word": "a man", "x": 0.2, "y": 0.6, "voice": "male"},
  {"word": "a woman", "x": 0.72, "y": 0.6, "voice": "female"},
  {"word": "a cat", "x": 0.42, "y": 0.84, "voice": "male"},
  {"word": "boats", "x": 0.42, "y": 0.33, "voice": "male"},
 ],
 "question": "What is the man showing her?",
 "answer": ["He", "is", "showing", "her", "his", "small", "boats."],
 "answerVoice": "male",
 "notes": "AI clip with weak continuity: at 0-1.5 s only a bearded chin (right) and a nose (left) are in the picture and the brush is at the bearded face; from 2.5 s the bearded man is on the left and the woman holds the brush. So no phrase about painting / holding the brush. Man box at 0-1.5 = the bearded face on the right, at 2.0-3.0 = his face on the left edge (his hands holding the boat are not in the box), at 6.0-6.5 = only his hands/forearm. Both wear the same grey overalls and both cross their arms, so the woman got no phrase of her own; the cat (in the cardboard box, 8.0-10.0 s) is the second target. Man box is cut above the cat box at 8.0-10.0. Key word 'hobby' is abstract and is not a noun slot."
})

# ---------------- 387 ----------------
t = T(31)
dog, man = {}, {}
for x in (0.0, 0.5): dog[x] = (0.08, 0.68, 0.68, 0.32)
for x in (1.0, 1.5): dog[x] = (0.08, 0.64, 0.68, 0.36)
for x in rng(2.0, 3.5): dog[x] = (0.08, 0.6, 0.68, 0.4)
dog[4.0] = (0.14, 0.58, 0.62, 0.42)
dog[4.5] = (0.15, 0.58, 0.6, 0.4)
dog[5.0] = (0.15, 0.58, 0.55, 0.42)
dog[5.5] = (0.2, 0.58, 0.35, 0.42)
dog[6.0] = (0.22, 0.53, 0.3, 0.31)
dog[6.5] = (0.2, 0.53, 0.3, 0.27)
dog[7.0] = (0.18, 0.46, 0.32, 0.4)
dog[7.5] = (0.18, 0.42, 0.32, 0.43)
for x in rng(8.0, 9.5): dog[x] = (0.2, 0.4, 0.3, 0.34)
for x in rng(10.0, 13.5): dog[x] = (0.25, 0.38, 0.25, 0.33)
for x in rng(14.0, 15.0): dog[x] = (0.26, 0.38, 0.25, 0.33)
for x in rng(0.0, 5.5): man[x] = (0.4, 0.4, 0.6, 0.18)
for x in (6.0, 6.5): man[x] = (0.4, 0.38, 0.6, 0.14)
for x in rng(7.0, 13.5): man[x] = (0.5, 0.38, 0.5, 0.32)
for x in rng(14.0, 15.0): man[x] = (0.51, 0.36, 0.49, 0.34)
kd, km = keys(t, dog), keys(t, man)
write({
 "mediaId": 387, "level": "B", "keyWord": "security camera", "defaultVoice": "male",
 "taps": [
  {"phrase": "to rest on the rug", "target": "the dog", "voice": "male", "keys": kd},
  {"phrase": "to wake up its owner", "target": "the dog", "voice": "male", "keys": kd},
  {"phrase": "to sleep under a duvet", "target": "the man", "voice": "male", "keys": km},
 ],
 "stillS": 10.0,
 "nouns": [
  {"word": "a rug", "x": 0.45, "y": 0.82, "voice": "male"},
  {"word": "a duvet", "x": 0.75, "y": 0.58, "voice": "male"},
  {"word": "a pillow", "x": 0.63, "y": 0.44, "voice": "male"},
  {"word": "a bedside table", "x": 0.2, "y": 0.56, "voice": "male"},
 ],
 "question": "What is the dog doing?",
 "answer": ["The", "dog", "is", "trying", "to", "wake", "its", "owner."],
 "answerVoice": "male",
 "notes": "Dark, grainy fixed camera. The man box = his head plus the duvet-covered body on the bed; from 7.0 s it is split from the dog box along x = 0.5 (dog's head touches his head), so the left edge of his head may fall just outside. At 6.0-6.5 the man box is a thin strip (dog passes below). The pillow is a small dark shape behind the man's head - weakest noun. The key word (security camera) is the viewpoint, not visible, so it is not a noun slot. 'bedside table': it is a low chest with drawers beside the bed."
})

# ---------------- 388 ----------------
t = T(31)
kg = keys(t, {x: (0.0, 0.2, 0.96, 0.76) for x in t})
write({
 "mediaId": 388, "level": "A", "keyWord": "homework", "defaultVoice": "female",
 "taps": [
  {"phrase": "to do her homework", "target": "the girl", "voice": "female", "keys": kg},
  {"phrase": "to wear round glasses", "target": "the girl", "voice": "female", "keys": kg},
  {"phrase": "to write with a pen", "target": "the girl", "voice": "female", "keys": kg},
 ],
 "stillS": 5.0,
 "nouns": [
  {"word": "hair", "x": 0.3, "y": 0.3, "voice": "female"},
  {"word": "glasses", "x": 0.48, "y": 0.41, "voice": "female"},
  {"word": "a pen", "x": 0.8, "y": 0.84, "voice": "female"},
  {"word": "homework", "x": 0.42, "y": 0.93, "voice": "female"},
 ],
 "question": "What is the girl doing?",
 "answer": ["She", "is", "doing", "her", "homework."],
 "answerVoice": "female",
 "notes": "Only one possible target (the girl), used for all three phrases. She writes only from about 11.5 s; before that she rests her head on her hand. 'homework' labels the printed worksheets on the desk."
})

# ---------------- 389 ----------------
t = T(21)
wom = {0.0: (0.66, 0.0, 0.34, 0.55), 0.5: (0.64, 0.0, 0.36, 0.56), 1.0: (0.6, 0.0, 0.4, 0.75),
       1.5: (0.6, 0.0, 0.4, 0.78), 2.0: (0.57, 0.0, 0.43, 0.74), 2.5: (0.4, 0.0, 0.6, 0.74),
       3.0: (0.08, 0.08, 0.86, 0.78), 3.5: (0.3, 0.08, 0.52, 0.76),
       4.5: (0.6, 0.03, 0.4, 0.38), 5.0: (0.64, 0.0, 0.36, 0.4), 5.5: (0.68, 0.0, 0.32, 0.24),
       6.0: (0.82, 0.0, 0.18, 0.14), 7.0: (0.82, 0.0, 0.18, 0.14)}
man = {3.5: (0.82, 0.2, 0.18, 0.42), 4.0: (0.24, 0.18, 0.5, 0.52), 4.5: (0.08, 0.08, 0.52, 0.56),
       5.0: (0.0, 0.0, 0.64, 0.62), 5.5: (0.0, 0.0, 0.68, 0.6), 6.0: (0.0, 0.0, 0.82, 0.52),
       6.5: (0.0, 0.0, 1.0, 0.6), 7.0: (0.0, 0.0, 0.82, 0.72), 7.5: (0.03, 0.0, 0.97, 0.8),
       8.0: (0.03, 0.0, 0.97, 0.74), 8.5: (0.0, 0.08, 0.79, 0.7), 9.0: (0.1, 0.12, 0.69, 0.75),
       9.5: (0.0, 0.12, 0.82, 0.8), 10.0: (0.0, 0.1, 0.8, 0.78)}
cat = {8.5: (0.79, 0.28, 0.21, 0.14), 9.0: (0.79, 0.32, 0.21, 0.14), 9.5: (0.82, 0.32, 0.18, 0.14),
       10.0: (0.8, 0.34, 0.2, 0.14)}
write({
 "mediaId": 389, "level": "A", "keyWord": "honey", "defaultVoice": "male",
 "taps": [
  {"phrase": "to put honey on bread", "target": "the woman", "voice": "female", "keys": keys(t, wom)},
  {"phrase": "to eat bread with honey", "target": "the man", "voice": "male", "keys": keys(t, man)},
  {"phrase": "to lie on a wall", "target": "the cat", "voice": "male", "keys": keys(t, cat)},
 ],
 "stillS": 4.5,
 "nouns": [
  {"word": "a woman", "x": 0.84, "y": 0.3, "voice": "female"},
  {"word": "a man", "x": 0.3, "y": 0.52, "voice": "male"},
  {"word": "bread", "x": 0.68, "y": 0.77, "voice": "male"},
  {"word": "honey", "x": 0.13, "y": 0.86, "voice": "male"},
 ],
 "question": "What is the man eating?",
 "answer": ["He", "is", "eating", "bread", "with", "honey."],
 "answerVoice": "male",
 "notes": "The woman holds the honey dipper (0-5.5 s) and lets the honey run onto the bread at 4.5-6.5 s; after that only a sliver of her is at the right edge (off at 6.5 and from 7.5). AI glitch at 4.0 s: the face on the right has a beard for that one frame, so the woman is off at 4.0 and that face is in no box. The man is a sliver at 3.0 (off), enters at 3.5; where the two overlap (3.5-5.5) the boxes are split along a vertical line, so the man's right shoulder is outside his box. The cat lies (at 9.0-9.5 more loaf-like, head up) on the white wall behind the man from 8.5 s (at 8.0 only its back shows behind his hand: off); the man's box is cut left of the cat box. 'honey' pill is on the honey jar."
})
