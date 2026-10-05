# writes content/4111..4114.json (helper of the writer for 4111-4114)
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

def keys(times, boxes):
    out = []
    for t in times:
        b = boxes.get(t)
        if b is None: out.append({"t": t, "off": True})
        else: out.append({"t": t, "x": b[0], "y": b[1], "w": round(b[2], 2), "h": round(b[3], 2)})
    return out

def span(d, ts, b):
    for t in ts: d[t] = b

def write(vid, obj):
    json.dump(obj, open(f'{HERE}/content/{vid}.json', 'w'), indent=1, ensure_ascii=False)

def times(n): return [i * 0.5 for i in range(n)]

# ---------------- 4111 ----------------
T = times(20)
man, sheep = {}, {}
span(man, [0.0, 0.5, 1.0, 1.5, 2.0], (0.25, 0.27, 0.57, 0.52))
sheep[2.0] = (0.83, 0.34, 0.17, 0.26)
man[2.5] = (0.0, 0.30, 0.50, 0.44);  sheep[2.5] = (0.50, 0.33, 0.50, 0.47)
man[3.0] = (0.0, 0.32, 0.37, 0.44);  sheep[3.0] = (0.37, 0.36, 0.63, 0.56)
man[3.5] = (0.0, 0.32, 0.37, 0.44);  sheep[3.5] = (0.37, 0.34, 0.63, 0.58)
man[4.0] = (0.0, 0.33, 0.18, 0.37);  sheep[4.0] = (0.18, 0.36, 0.82, 0.46)
man[4.5] = (0.0, 0.33, 0.33, 0.41);  sheep[4.5] = (0.33, 0.29, 0.67, 0.53)
man[5.0] = (0.05, 0.31, 0.44, 0.45); sheep[5.0] = (0.49, 0.30, 0.51, 0.65)
man[5.5] = (0.10, 0.33, 0.35, 0.43); sheep[5.5] = (0.45, 0.40, 0.55, 0.55)
man[6.0] = (0.0, 0.32, 0.29, 0.40);  sheep[6.0] = (0.29, 0.37, 0.71, 0.43)
man[6.5] = (0.10, 0.33, 0.36, 0.43); sheep[6.5] = (0.46, 0.35, 0.54, 0.45)
man[7.0] = (0.10, 0.34, 0.40, 0.42); sheep[7.0] = (0.50, 0.37, 0.50, 0.45)
man[7.5] = (0.03, 0.35, 0.35, 0.41); sheep[7.5] = (0.38, 0.42, 0.62, 0.50)
man[8.0] = (0.05, 0.35, 0.45, 0.40); sheep[8.0] = (0.50, 0.38, 0.50, 0.42)
man[8.5] = (0.15, 0.37, 0.66, 0.41); sheep[8.5] = (0.81, 0.40, 0.19, 0.38)
man[9.0] = (0.08, 0.38, 0.70, 0.40); sheep[9.0] = (0.78, 0.46, 0.22, 0.32)
man[9.5] = (0.08, 0.38, 0.74, 0.40); sheep[9.5] = (0.82, 0.46, 0.18, 0.32)
km, ks = keys(T, man), keys(T, sheep)
write(4111, {
 "mediaId": 4111, "level": "A", "keyWord": "annoying", "defaultVoice": "male",
 "taps": [
  {"phrase": "to hold a hammer", "target": "the man", "voice": "male", "keys": km},
  {"phrase": "to push the man", "target": "the big sheep", "voice": "male", "keys": ks},
  {"phrase": "to wear sunglasses", "target": "the man", "voice": "male", "keys": km}],
 "stillS": 6.5,
 "nouns": [
  {"word": "a man", "x": 0.30, "y": 0.47, "voice": "male"},
  {"word": "a sheep", "x": 0.76, "y": 0.55, "voice": "male"},
  {"word": "a hammer", "x": 0.18, "y": 0.64, "voice": "male"},
  {"word": "the sky", "x": 0.80, "y": 0.15, "voice": "male"}],
 "question": "What is the sheep doing?",
 "answer": ["The", "annoying", "sheep", "is", "pushing", "the", "man."],
 "answerVoice": "male",
 "notes": "The animal is a ram; level A so 'sheep'. Target named 'the big sheep' because a tiny flock stands far away in the background. Man and sheep overlap in most frames (his legs lie under the sheep): boxes split along a vertical line at the sheep's head; at 4.0 s the man is almost hidden behind the sheep's head, his box is the narrow strip on the left (hand, hammer). Third phrase is a state (sunglasses) because the man's other actions (kneel, shout) are less clear at level A."
})

# ---------------- 4112 ----------------
T = times(21)
drill, hand, bottle = {}, {}, {}
for t in times(15):   # 0.0 .. 7.0
    drill[t] = (0.0, 0.38, 0.40, 0.28); bottle[t] = (0.40, 0.49, 0.24, 0.17); hand[t] = (0.0, 0.66, 0.64, 0.20)
drill[7.5] = (0.0, 0.37, 0.34, 0.17); bottle[7.5] = (0.39, 0.47, 0.25, 0.19); hand[7.5] = (0.0, 0.66, 0.66, 0.20)
bottle[8.0] = (0.38, 0.45, 0.26, 0.21); hand[8.0] = (0.0, 0.66, 0.66, 0.20)
bottle[8.5] = (0.34, 0.43, 0.29, 0.21); hand[8.5] = (0.0, 0.64, 0.64, 0.18)
bottle[9.0] = (0.18, 0.29, 0.34, 0.24); hand[9.0] = (0.0, 0.53, 0.58, 0.26)
bottle[9.5] = (0.18, 0.32, 0.44, 0.31); hand[9.5] = (0.0, 0.63, 0.68, 0.37)
bottle[10.0] = (0.11, 0.29, 0.52, 0.33); hand[10.0] = (0.0, 0.62, 0.68, 0.32)
write(4112, {
 "mediaId": 4112, "level": "A", "keyWord": "block", "defaultVoice": "female",
 "taps": [
  {"phrase": "to make a hole", "target": "the drill", "voice": "female", "keys": keys(T, drill)},
  {"phrase": "to hold a bottle", "target": "the hand", "voice": "female", "keys": keys(T, hand)},
  {"phrase": "to catch the dust", "target": "the bottle", "voice": "female", "keys": keys(T, bottle)}],
 "stillS": 9.0,
 "nouns": [
  {"word": "a window", "x": 0.62, "y": 0.15, "voice": "female"},
  {"word": "a bottle", "x": 0.36, "y": 0.42, "voice": "female"},
  {"word": "a glove", "x": 0.28, "y": 0.63, "voice": "female"},
  {"word": "a block", "x": 0.66, "y": 0.82, "voice": "female"}],
 "question": "What is the drill doing?",
 "answer": ["It", "is", "making", "a", "hole", "in", "the", "block."],
 "answerVoice": "female",
 "notes": "Only a gloved hand is shown, no person: defaultVoice from evenId (female). Drill, bottle and hand touch: the drill box ends at x 0.40, so the tip of the drill bit (above the bottle, x 0.40-0.55) lies in no box; the hand box starts under the bottle (the thumb reaches a little into the bottle box). The drill leaves the picture after 7.5 s. 'a block' is placed on one block of the wall (the wall is made of several). 'dust' and 'glove' are A2."
})

# ---------------- 4113 ----------------
T = times(30)
grey, white, big = {}, {}, {}
grey[0.0] = (0.0, 0.22, 0.66, 0.78); white[0.0] = (0.67, 0.11, 0.33, 0.82)
grey[0.5] = (0.0, 0.22, 0.68, 0.78); white[0.5] = (0.69, 0.09, 0.31, 0.85)
grey[1.0] = (0.0, 0.23, 0.69, 0.77); white[1.0] = (0.70, 0.08, 0.30, 0.92)
grey[1.5] = (0.0, 0.47, 0.55, 0.48); white[1.5] = (0.55, 0.41, 0.45, 0.54); big[1.5] = (0.10, 0.0, 0.90, 0.41)
for t in (2.0, 2.5, 3.0, 3.5):
    grey[t] = (0.0, 0.46, 0.55, 0.46); white[t] = (0.55, 0.41, 0.45, 0.51); big[t] = (0.03, 0.05, 0.97, 0.36)
grey[4.0] = (0.0, 0.46, 0.45, 0.46); white[4.0] = (0.45, 0.43, 0.55, 0.49); big[4.0] = (0.03, 0.05, 0.97, 0.37)
for t in (4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5):
    grey[t] = (0.0, 0.47, 0.35, 0.45); white[t] = (0.35, 0.43, 0.65, 0.49); big[t] = (0.03, 0.05, 0.97, 0.37)
for t in (9.0, 9.5):
    grey[t] = (0.0, 0.49, 0.27, 0.45); white[t] = (0.27, 0.40, 0.73, 0.54); big[t] = (0.03, 0.05, 0.97, 0.34)
for t in (10.0, 10.5, 11.0, 11.5):
    grey[t] = (0.0, 0.49, 0.26, 0.45); white[t] = (0.26, 0.35, 0.74, 0.57); big[t] = (0.22, 0.05, 0.78, 0.29)
grey[12.0] = (0.0, 0.49, 0.26, 0.45); white[12.0] = (0.26, 0.35, 0.74, 0.57); big[12.0] = (0.22, 0.0, 0.78, 0.30)
grey[12.5] = (0.0, 0.49, 0.26, 0.45); white[12.5] = (0.26, 0.35, 0.74, 0.57); big[12.5] = (0.22, 0.0, 0.78, 0.34)
grey[13.0] = (0.0, 0.46, 0.43, 0.50); white[13.0] = (0.43, 0.36, 0.57, 0.60)
grey[13.5] = (0.0, 0.45, 0.49, 0.51); white[13.5] = (0.49, 0.36, 0.51, 0.60)
grey[14.0] = (0.0, 0.43, 0.52, 0.49); white[14.0] = (0.52, 0.36, 0.48, 0.56)
grey[14.5] = (0.0, 0.43, 0.46, 0.49); white[14.5] = (0.46, 0.41, 0.54, 0.51)
write(4113, {
 "mediaId": 4113, "level": "A", "keyWord": "jewellery", "defaultVoice": "male",
 "taps": [
  {"phrase": "to hold a pink ring", "target": "the grey bird", "voice": "male", "keys": keys(T, grey)},
  {"phrase": "to shout at another bird", "target": "the white bird", "voice": "male", "keys": keys(T, white)},
  {"phrase": "to look down at them", "target": "the big black bird", "voice": "male", "keys": keys(T, big)}],
 "stillS": 13.0,
 "nouns": [
  {"word": "jewellery", "x": 0.22, "y": 0.66, "voice": "male"},
  {"word": "a white bird", "x": 0.68, "y": 0.58, "voice": "male"},
  {"word": "buildings", "x": 0.35, "y": 0.15, "voice": "male"},
  {"word": "a street", "x": 0.65, "y": 0.93, "voice": "male"}],
 "question": "What is the grey bird holding?",
 "answer": ["It", "is", "holding", "a", "pink", "ring."],
 "answerVoice": "male",
 "notes": "Level A: 'bird' instead of 'pigeon'. Animals only: defaultVoice from evenId (male). The key word 'jewellery' labels the ring in the nouns (so 'a ring' is not a noun), the ring itself appears in a phrase and in the answer. 10.0-12.5 s: the white bird's raised wing reaches over the grey bird's head; the white bird's box starts at x 0.26, so the wing tip (x 0.10-0.26, y 0.20-0.49) lies in no box - the big bird's box was narrowed there so that a tap on the wing is not counted for the big bird. The big black bird is in the background behind both; its box is the area above the two small birds. 14.0-14.5 s the two small birds lean together, split along the line between them (the ring sits on that line). 'to shout' is read from the wide open beak at 10-11 s."
})

# ---------------- 4114 ----------------
T = times(30)
wom, man, mann = {}, {}, {}
wom[0.0] = (0.08, 0.21, 0.39, 0.74); man[0.0] = (0.47, 0.13, 0.53, 0.78)
wom[0.5] = (0.06, 0.20, 0.42, 0.80); man[0.5] = (0.48, 0.10, 0.52, 0.86)
wom[1.0] = (0.0, 0.19, 0.47, 0.81);  man[1.0] = (0.47, 0.10, 0.53, 0.90)
wom[1.5] = (0.0, 0.18, 0.47, 0.82);  man[1.5] = (0.47, 0.07, 0.53, 0.93)
wom[2.0] = (0.0, 0.15, 0.47, 0.85);  man[2.0] = (0.47, 0.04, 0.53, 0.96)
wom[2.5] = (0.0, 0.22, 0.70, 0.78);  man[2.5] = (0.70, 0.18, 0.30, 0.67)
wom[3.0] = (0.0, 0.24, 0.68, 0.76);  man[3.0] = (0.68, 0.16, 0.32, 0.68)
wom[3.5] = (0.13, 0.39, 0.33, 0.57); man[3.5] = (0.0, 0.31, 0.13, 0.64); mann[3.5] = (0.46, 0.27, 0.38, 0.47)
wom[4.0] = (0.66, 0.28, 0.34, 0.68); man[4.0] = (0.0, 0.19, 0.33, 0.76); mann[4.0] = (0.33, 0.28, 0.33, 0.54)
for t in (4.5, 5.0, 5.5):
    wom[t] = (0.67, 0.28, 0.33, 0.68); man[t] = (0.0, 0.18, 0.31, 0.77); mann[t] = (0.31, 0.28, 0.36, 0.54)
for t in (6.0, 6.5, 7.0, 7.5, 8.0): wom[t] = (0.0, 0.0, 1.0, 1.0)
for t in (8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5): man[t] = (0.0, 0.0, 1.0, 1.0)
wom[12.0] = (0.0, 0.11, 1.0, 0.89)
wom[12.5] = (0.37, 0.09, 0.63, 0.91); man[12.5] = (0.0, 0.32, 0.37, 0.66)
wom[13.0] = (0.47, 0.08, 0.53, 0.92); man[13.0] = (0.0, 0.33, 0.47, 0.67)
wom[13.5] = (0.60, 0.02, 0.40, 0.98); man[13.5] = (0.0, 0.31, 0.60, 0.69)
wom[14.0] = (0.70, 0.05, 0.30, 0.95); man[14.0] = (0.0, 0.30, 0.70, 0.67)
man[14.5] = (0.04, 0.27, 0.92, 0.70)
write(4114, {
 "mediaId": 4114, "level": "B", "keyWord": "mall", "defaultVoice": "female",
 "taps": [
  {"phrase": "to point at a mannequin", "target": "the woman", "voice": "female", "keys": keys(T, wom)},
  {"phrase": "to walk around barefoot", "target": "the man", "voice": "male", "keys": keys(T, man)},
  {"phrase": "to display a gold dress", "target": "the mannequin", "voice": "female", "keys": keys(T, mann)}],
 "stillS": 5.0,
 "nouns": [
  {"word": "a mannequin", "x": 0.54, "y": 0.37, "voice": "female"},
  {"word": "curtains", "x": 0.45, "y": 0.14, "voice": "female"},
  {"word": "shorts", "x": 0.14, "y": 0.68, "voice": "female"},
  {"word": "high heels", "x": 0.80, "y": 0.91, "voice": "female"}],
 "question": "What is the woman pointing at?",
 "answer": ["She", "is", "pointing", "at", "a", "mannequin", "in", "the", "mall."],
 "answerVoice": "female",
 "notes": "The key word 'mall' is the whole place, so it is not a noun slot; it is in the answer. The woman also wears a gold dress: 'to display' is meant to fit only the mannequin. Last shot (12.0-14.5 s): the woman's fan of bags covers the man; boxes are split along a vertical line, so part of her bags lies in his box. At 12.0 s the man is almost fully hidden behind her (off); at 14.5 s only the woman's bags are left in the picture (off). At 3.5 s (fast turn, blurred) the woman's skirt and the mannequin overlap; split at x 0.46."
})
print('written')
