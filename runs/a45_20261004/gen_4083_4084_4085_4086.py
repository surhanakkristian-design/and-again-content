import json, os
RUN = os.path.dirname(os.path.abspath(__file__))
def times(i): return json.load(open(f"{RUN}/frames/{i}/packet.json"))["times"]
def keys(i, d):
    out = []
    for t in times(i):
        b = d.get(t)
        if b is None: out.append({"t": t, "off": True})
        else: out.append({"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out
def rng(a, b): 
    r = []; t = a
    while t <= b + 1e-9: r.append(round(t, 1)); t += 0.5
    return r
def fill(d, a, b, box):
    for t in rng(a, b): d[t] = box
def save(c): json.dump(c, open(f"{RUN}/content/{c['mediaId']}.json", "w"), indent=1, ensure_ascii=False)

# ---------------- 4083
dog, wom, man = {}, {}, {}
fill(wom, 0, 2.5, (0.0, 0.23, 0.36, 0.29)); fill(dog, 0, 2.5, (0.36, 0.32, 0.24, 0.21)); fill(man, 0, 2.5, (0.60, 0.20, 0.40, 0.36))
fill(wom, 3.0, 6.5, (0.0, 0.23, 0.34, 0.29))
fill(dog, 3.0, 4.0, (0.34, 0.34, 0.21, 0.20)); fill(man, 3.0, 4.0, (0.55, 0.20, 0.45, 0.36))
dog[4.5] = (0.34, 0.35, 0.24, 0.18); man[4.5] = (0.58, 0.20, 0.42, 0.36)
dog[5.0] = (0.34, 0.36, 0.25, 0.17); man[5.0] = (0.59, 0.20, 0.41, 0.36)
dog[5.5] = (0.34, 0.36, 0.27, 0.17); man[5.5] = (0.61, 0.20, 0.39, 0.36)
dog[6.0] = (0.34, 0.35, 0.29, 0.18); man[6.0] = (0.63, 0.20, 0.37, 0.36)
dog[6.5] = (0.34, 0.35, 0.31, 0.18); man[6.5] = (0.66, 0.20, 0.34, 0.36)
wom[7.0] = (0.0, 0.25, 0.33, 0.29); dog[7.0] = (0.33, 0.38, 0.30, 0.18); man[7.0] = (0.72, 0.33, 0.28, 0.27)
wom[7.5] = (0.0, 0.25, 0.32, 0.28); dog[7.5] = (0.32, 0.37, 0.33, 0.20); man[7.5] = (0.82, 0.40, 0.18, 0.24)
wom[8.0] = (0.0, 0.24, 0.28, 0.29); dog[8.0] = (0.29, 0.36, 0.34, 0.18)
wom[8.5] = (0.0, 0.25, 0.18, 0.27); dog[8.5] = (0.30, 0.36, 0.36, 0.19)
wom[9.0] = (0.0, 0.33, 0.18, 0.20); dog[9.0] = (0.38, 0.37, 0.26, 0.21)
dog[9.5] = (0.38, 0.37, 0.24, 0.21)
fill(dog, 10, 11.5, (0.30, 0.35, 0.38, 0.25))
wom[12.0] = (0.0, 0.47, 0.50, 0.25); man[12.0] = (0.58, 0.50, 0.42, 0.22)
wom[12.5] = (0.0, 0.39, 0.52, 0.33); man[12.5] = (0.53, 0.40, 0.47, 0.32)
wom[13.0] = (0.0, 0.40, 0.56, 0.32); man[13.0] = (0.57, 0.40, 0.43, 0.32)
wom[13.5] = (0.0, 0.39, 0.52, 0.33); man[13.5] = (0.53, 0.40, 0.47, 0.32)
fill(dog, 14, 15, (0.30, 0.34, 0.38, 0.25)); fill(wom, 14, 15, (0.0, 0.30, 0.18, 0.38)); fill(man, 14, 15, (0.82, 0.32, 0.18, 0.43))
save({"mediaId": 4083, "level": "A", "keyWord": "middle", "defaultVoice": "male",
 "taps": [
  {"phrase": "to lie in the middle", "target": "the dog", "voice": "male", "keys": keys(4083, dog)},
  {"phrase": "to wear purple pyjamas", "target": "the woman", "voice": "female", "keys": keys(4083, wom)},
  {"phrase": "to have a beard", "target": "the man", "voice": "male", "keys": keys(4083, man)}],
 "stillS": 0.0,
 "nouns": [{"word": "a woman", "x": 0.20, "y": 0.33, "voice": "female"}, {"word": "a dog", "x": 0.47, "y": 0.44, "voice": "male"},
           {"word": "a man", "x": 0.78, "y": 0.33, "voice": "male"}, {"word": "a blanket", "x": 0.50, "y": 0.70, "voice": "male"}],
 "question": "Where is the dog lying?",
 "answer": ["The", "dog", "is", "lying", "in", "the", "middle."], "answerVoice": "male",
 "notes": "Woman and man have no action of their own (both sleep), so their phrases are states. At 12.0-13.5 the two people peek over the bed edge (woman left, man right); at 14.0-15.0 only their hands grip the bed sides (woman's left edge, man's right edge) - boxes kept on the hands. 7.0-7.5 the man is a blur at the right edge."})

# ---------------- 4084
man, cat, liz = {}, {}, {}
fill(liz, 0, 1.5, (0.07, 0.0, 0.28, 0.17))
fill(man, 0, 0.5, (0.14, 0.20, 0.80, 0.32)); fill(cat, 0, 0.5, (0.10, 0.52, 0.38, 0.38))
fill(man, 1.0, 1.5, (0.14, 0.20, 0.80, 0.32)); fill(cat, 1.0, 1.5, (0.08, 0.52, 0.40, 0.44))
fill(man, 2.0, 4.0, (0.0, 0.0, 1.0, 1.0)); fill(cat, 4.5, 6.0, (0.0, 0.0, 1.0, 1.0)); fill(man, 6.5, 7.5, (0.0, 0.0, 1.0, 1.0))
man[8.0] = (0.0, 0.05, 1.0, 0.47); cat[8.0] = (0.08, 0.52, 0.82, 0.48)
fill(man, 8.5, 9.5, (0.0, 0.03, 1.0, 0.45)); fill(cat, 8.5, 9.5, (0.0, 0.48, 1.0, 0.52))
fill(man, 10, 11, (0.0, 0.03, 1.0, 0.46)); fill(cat, 10, 11, (0.0, 0.49, 1.0, 0.51))
man[11.5] = (0.07, 0.23, 0.83, 0.29); cat[11.5] = (0.04, 0.52, 0.46, 0.47); liz[11.5] = (0.02, 0.04, 0.22, 0.15)
fill(man, 12, 12.5, (0.06, 0.22, 0.90, 0.31)); fill(cat, 12, 12.5, (0.04, 0.53, 0.45, 0.37)); fill(liz, 12, 13, (0.02, 0.05, 0.22, 0.15))
man[13.0] = (0.06, 0.21, 0.86, 0.33); cat[13.0] = (0.04, 0.54, 0.46, 0.37)
fill(man, 13.5, 14.5, (0.06, 0.09, 0.94, 0.37)); fill(cat, 13.5, 14.5, (0.01, 0.46, 0.56, 0.53))
save({"mediaId": 4084, "level": "A", "keyWord": "head", "defaultVoice": "male",
 "taps": [
  {"phrase": "to touch his head", "target": "the man", "voice": "male", "keys": keys(4084, man)},
  {"phrase": "to grow yellow hair", "target": "the cat", "voice": "male", "keys": keys(4084, cat)},
  {"phrase": "to sit on the mirror", "target": "the lizard", "voice": "male", "keys": keys(4084, liz)}],
 "stillS": 0.0,
 "nouns": [{"word": "a mirror", "x": 0.68, "y": 0.19, "voice": "male"}, {"word": "a man", "x": 0.38, "y": 0.40, "voice": "male"},
           {"word": "a cat", "x": 0.32, "y": 0.68, "voice": "male"}, {"word": "a tap", "x": 0.70, "y": 0.80, "voice": "male"}],
 "question": "What is the man touching?",
 "answer": ["He", "is", "touching", "his", "head."], "answerVoice": "male",
 "notes": "The man is seen as a reflection in the mirror; where the cat sits in front of him the boxes are split at the top of the cat (man above, cat below). 2.0-4.0 only the man's hands and chest (full frame). The lizard (a small green chameleon on top of the mirror frame) is visible only 0-1.5 and 11.5-13.0. 'a head' not used as a noun: two heads (man, cat) in the still."})

# ---------------- 4085
man, wom = {}, {}
fill(wom, 0, 2.5, (0.04, 0.12, 0.44, 0.40)); fill(man, 0, 2.5, (0.48, 0.24, 0.52, 0.64))
man[3.0] = (0.0, 0.18, 1.0, 0.72)
wom[3.5] = (0.18, 0.20, 0.44, 0.78); wom[4.0] = (0.18, 0.15, 0.50, 0.75)
wom[4.5] = (0.14, 0.23, 0.24, 0.50); man[4.5] = (0.38, 0.14, 0.54, 0.61)
man[5.0] = (0.0, 0.60, 1.0, 0.36); man[5.5] = (0.16, 0.46, 0.84, 0.48); man[6.0] = (0.08, 0.14, 0.84, 0.77); man[6.5] = (0.10, 0.12, 0.74, 0.80)
fill(man, 7.0, 9.5, (0.16, 0.14, 0.62, 0.76)); man[12.0] = (0.16, 0.14, 0.62, 0.76)
fill(wom, 10, 10.5, (0.15, 0.10, 0.70, 0.70)); fill(wom, 11, 11.5, (0.0, 0.0, 1.0, 1.0))
wom[12.5] = (0.24, 0.26, 0.32, 0.65); man[12.5] = (0.56, 0.17, 0.36, 0.72)
wom[13.0] = (0.25, 0.34, 0.28, 0.50); man[13.0] = (0.53, 0.26, 0.45, 0.52)
wom[13.5] = (0.26, 0.28, 0.24, 0.35); man[13.5] = (0.50, 0.26, 0.24, 0.37)
wom[14.0] = (0.60, 0.10, 0.34, 0.42); man[14.0] = (0.0, 0.22, 0.60, 0.66)
wom[14.5] = (0.63, 0.17, 0.34, 0.36); man[14.5] = (0.0, 0.22, 0.63, 0.66)
wom[15.0] = (0.60, 0.19, 0.33, 0.36); man[15.0] = (0.0, 0.23, 0.60, 0.66)
mk = keys(4085, man)
save({"mediaId": 4085, "level": "A", "keyWord": "change", "defaultVoice": "male",
 "taps": [
  {"phrase": "to play a video game", "target": "the man", "voice": "male", "keys": mk},
  {"phrase": "to wear a blue suit", "target": "the man", "voice": "male", "keys": mk},
  {"phrase": "to push the man inside", "target": "the woman in purple", "voice": "female", "keys": keys(4085, wom)}],
 "stillS": 7.0,
 "nouns": [{"word": "a door", "x": 0.31, "y": 0.22, "voice": "male"}, {"word": "a man", "x": 0.47, "y": 0.50, "voice": "male"},
           {"word": "a woman", "x": 0.84, "y": 0.62, "voice": "female"}, {"word": "stairs", "x": 0.20, "y": 0.72, "voice": "male"}],
 "question": "What is the man playing?",
 "answer": ["He", "is", "playing", "a", "video", "game."], "answerVoice": "male",
 "notes": "The man is one person before and after the change (grey T-shirt, then blue suit); two phrases share him. The women on the street are not targets (several, all alike). 3.5-4.0 the man is a grey blur dragged behind the woman: off. Indoors the two overlap, boxes split left/right (the man's box loses part of his body). 10.0-11.5 the eye / face in the door gap is the woman in purple. Key word 'change' is not in the texts: nothing visible fits a simple A-level sentence with it better than the phrases used."})

# ---------------- 4086
mos, per, hou = {}, {}, {}
mos[0.0] = (0.40, 0.43, 0.22, 0.17); mos[0.5] = (0.35, 0.43, 0.28, 0.17)
mos[1.0] = (0.02, 0.33, 0.50, 0.38); mos[1.5] = (0.04, 0.33, 0.58, 0.37)
fill(mos, 2.0, 3.0, (0.02, 0.35, 0.63, 0.36)); mos[3.5] = (0.10, 0.30, 0.64, 0.30)
mos[4.0] = (0.0, 0.28, 0.55, 0.34); mos[4.5] = (0.0, 0.29, 0.60, 0.42); mos[5.0] = (0.04, 0.30, 0.60, 0.30)
mos[6.0] = (0.0, 0.27, 0.26, 0.16); per[6.0] = (0.0, 0.46, 1.0, 0.54)
mos[6.5] = (0.42, 0.35, 0.26, 0.15); per[6.5] = (0.0, 0.50, 1.0, 0.50)
fill(mos, 7.0, 7.5, (0.42, 0.36, 0.26, 0.15)); fill(per, 7.0, 7.5, (0.0, 0.51, 1.0, 0.49))
mos[8.0] = (0.22, 0.30, 0.68, 0.32); fill(mos, 8.5, 9.0, (0.06, 0.34, 0.90, 0.28)); mos[9.5] = (0.06, 0.10, 0.90, 0.52); mos[10.0] = (0.02, 0.06, 0.96, 0.56)
fill(per, 8.0, 10.0, (0.0, 0.62, 1.0, 0.38))
mos[10.5] = (0.0, 0.28, 1.0, 0.36); per[10.5] = (0.0, 0.64, 1.0, 0.36)
fill(mos, 11, 12.5, (0.0, 0.27, 1.0, 0.39)); fill(per, 11, 12.5, (0.0, 0.66, 1.0, 0.34))
mos[13.0] = (0.0, 0.27, 1.0, 0.43); per[13.0] = (0.0, 0.70, 1.0, 0.30)
hou[13.5] = (0.0, 0.30, 1.0, 0.42); fill(hou, 14, 15, (0.0, 0.13, 1.0, 0.59))
save({"mediaId": 4086, "level": "B", "keyWord": "bite", "defaultVoice": "female",
 "taps": [
  {"phrase": "to bite a bald head", "target": "the mosquito", "voice": "female", "keys": keys(4086, mos)},
  {"phrase": "to sleep under a blanket", "target": "the sleeping person", "voice": "female", "keys": keys(4086, per)},
  {"phrase": "to let out a scream", "target": "the house", "voice": "female", "keys": keys(4086, hou)}],
 "stillS": 7.0,
 "nouns": [{"word": "the moon", "x": 0.14, "y": 0.26, "voice": "female"}, {"word": "a mosquito", "x": 0.55, "y": 0.45, "voice": "female"},
           {"word": "a pillow", "x": 0.86, "y": 0.64, "voice": "female"}, {"word": "a blanket", "x": 0.28, "y": 0.88, "voice": "female"}],
 "question": "What is the mosquito doing?",
 "answer": ["It", "is", "biting", "a", "bald", "head."], "answerVoice": "female",
 "notes": "The sleeper's gender is not shown, so the target is 'the sleeping person' and the voice is the default. 8.0-13.0 close-up: the pale dome under the mosquito is the sleeper's head, boxes split along the top of the head (the mosquito's leg ends fall into the head's box). The house screams (mouth wide open, tongue out) only 14.0-15.0; at 13.5 it has no face yet. The mosquito is small at 0-0.5 and 6.0-7.5."})
