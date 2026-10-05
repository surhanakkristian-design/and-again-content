#!/usr/bin/env python3
# writes content/259.json, 260.json, 261.json, 262.json
import json, os
RUN = os.path.dirname(os.path.abspath(__file__))
OFF = None


def keys(times, boxes):
    out = []
    for t in times:
        b = boxes[t] if isinstance(boxes, dict) else boxes
        if b is None:
            out.append({"t": t, "off": True})
        else:
            out.append({"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out


def times(n):
    return [i * 0.5 for i in range(n)]


def save(d):
    with open(os.path.join(RUN, "content", f"{d['mediaId']}.json"), "w") as f:
        json.dump(d, f, indent=1, ensure_ascii=False)


# ---------------- 259 eerie (B), static shot
T = times(31)
save({
    "mediaId": 259, "level": "B", "keyWord": "eerie", "defaultVoice": "male",
    "taps": [
        {"phrase": "to spread across the sky", "target": "the red glow", "voice": "male",
         "keys": keys(T, (0.08, 0.18, 0.84, 0.29))},
        {"phrase": "to fill the freight yard", "target": "the freight wagons", "voice": "male",
         "keys": keys(T, (0.0, 0.50, 1.0, 0.16))},
        {"phrase": "to form a dark silhouette", "target": "the trees", "voice": "male",
         "keys": keys(T, (0.12, 0.77, 0.88, 0.23))},
    ],
    "stillS": 10.0,
    "nouns": [
        {"word": "clouds", "x": 0.50, "y": 0.22, "voice": "male"},
        {"word": "a fireball", "x": 0.52, "y": 0.44, "voice": "male"},
        {"word": "freight wagons", "x": 0.45, "y": 0.57, "voice": "male"},
        {"word": "treetops", "x": 0.62, "y": 0.88, "voice": "male"},
    ],
    "question": "What is spreading across the night sky?",
    "answer": ["An", "eerie", "red", "glow", "is", "spreading", "across", "the", "sky."],
    "answerVoice": "male",
    "notes": "Static shot, no people or animals: targets are the red glow in the sky, the rows of freight wagons and the dark trees in the foreground, boxes constant. The glow is faint at 0-2 s and 14-15 s but always visible; its box covers the lit clouds and the bright ball on the horizon. The small lit cabin (x .5-.7, y .66-.74) belongs to no target. 'a fireball' = the bright burning ball at 8-12.5 s.",
})

# ---------------- 260 egg (A)
T = times(21)
man = {
    0.0: (0.38, 0.0, 0.62, 0.70), 0.5: (0.58, 0.0, 0.42, 0.75),
    1.0: (0.50, 0.08, 0.50, 0.92), 1.5: (0.46, 0.04, 0.54, 0.96),
    2.0: (0.46, 0.04, 0.54, 0.90), 2.5: (0.46, 0.06, 0.54, 0.90),
    3.0: (0.46, 0.08, 0.54, 0.88),
    3.5: OFF, 4.0: OFF, 4.5: OFF, 5.0: OFF, 5.5: OFF, 6.0: OFF,
    6.5: (0.28, 0.03, 0.72, 0.43), 7.0: (0.71, 0.0, 0.29, 0.49),
    7.5: (0.58, 0.0, 0.42, 0.62), 8.0: (0.40, 0.0, 0.60, 0.63),
    8.5: (0.50, 0.05, 0.50, 0.58), 9.0: (0.50, 0.15, 0.50, 0.54),
    9.5: (0.50, 0.17, 0.50, 0.52), 10.0: (0.47, 0.17, 0.53, 0.51),
}
cat = {
    0.0: OFF, 0.5: (0.38, 0.24, 0.19, 0.17),
    1.0: (0.27, 0.30, 0.22, 0.19), 1.5: (0.25, 0.33, 0.20, 0.17),
    2.0: (0.24, 0.33, 0.21, 0.17), 2.5: (0.24, 0.33, 0.21, 0.17),
    3.0: (0.24, 0.33, 0.21, 0.17), 3.5: (0.68, 0.16, 0.32, 0.23),
    4.0: OFF, 4.5: OFF, 5.0: OFF, 5.5: OFF, 6.0: OFF, 6.5: OFF,
    7.0: (0.33, 0.17, 0.37, 0.17), 7.5: (0.28, 0.26, 0.28, 0.14),
    8.0: OFF, 8.5: (0.18, 0.35, 0.30, 0.16), 9.0: (0.15, 0.35, 0.30, 0.17),
    9.5: (0.15, 0.36, 0.30, 0.18), 10.0: (0.15, 0.35, 0.30, 0.18),
}
egg = {
    0.0: OFF, 0.5: OFF, 1.0: OFF, 1.5: OFF, 2.0: OFF, 2.5: OFF, 3.0: OFF,
    3.5: (0.26, 0.45, 0.30, 0.18), 4.0: (0.36, 0.43, 0.28, 0.18),
    4.5: (0.36, 0.37, 0.30, 0.18), 5.0: (0.15, 0.38, 0.80, 0.32),
    5.5: (0.14, 0.38, 0.78, 0.31), 6.0: (0.14, 0.40, 0.84, 0.40),
    6.5: (0.18, 0.47, 0.68, 0.28), 7.0: (0.08, 0.50, 0.74, 0.30),
    7.5: (0.10, 0.63, 0.76, 0.30), 8.0: (0.04, 0.64, 0.58, 0.26),
    8.5: (0.06, 0.64, 0.76, 0.27), 9.0: (0.0, 0.70, 0.58, 0.24),
    9.5: (0.06, 0.70, 0.76, 0.25), 10.0: (0.02, 0.69, 0.56, 0.24),
}
save({
    "mediaId": 260, "level": "A", "keyWord": "egg", "defaultVoice": "male",
    "taps": [
        {"phrase": "to eat some bread", "target": "the man", "voice": "male", "keys": keys(T, man)},
        {"phrase": "to sit by the window", "target": "the cat", "voice": "male", "keys": keys(T, cat)},
        {"phrase": "to cook in a pan", "target": "the egg", "voice": "male", "keys": keys(T, egg)},
    ],
    "stillS": 10.0,
    "nouns": [
        {"word": "a man", "x": 0.78, "y": 0.36, "voice": "male"},
        {"word": "a cat", "x": 0.28, "y": 0.44, "voice": "male"},
        {"word": "tomatoes", "x": 0.14, "y": 0.60, "voice": "male"},
        {"word": "an egg", "x": 0.33, "y": 0.79, "voice": "male"},
    ],
    "question": "What is the man eating?",
    "answer": ["He", "is", "eating", "bread", "with", "an", "egg."],
    "answerVoice": "male",
    "notes": "Many cuts and a moving camera. 'the egg' = the egg that is cracked into the pan (3.5-4.5 in his hand over the pan, 5.0-6.0 frying, 6.5-10 fried on the toast); it is off at 0-3 s, where only the broken shell in the bowl and a whole egg on the worktop are seen (a different egg). 'the man' is off at 3.5-6.0 (only his hands in the picture); his box is face and body, the near hand that holds bowl / toast is left out. The cat is off where it is hidden behind his hand or the curtain (0.0, 4.0-6.5, 8.0); it sits at 0.5-3.5 and stands on the sill later. The man eats from 7.5 on.",
})

# ---------------- 261 electrician (A)
el = {}
for t in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
    el[t] = (0.0, 0.08, 0.62, 0.92)
el.update({
    3.5: (0.0, 0.10, 0.70, 0.90), 4.0: (0.0, 0.05, 0.80, 0.95),
    4.5: (0.0, 0.08, 0.85, 0.92), 5.0: (0.0, 0.08, 0.86, 0.92),
    5.5: (0.0, 0.08, 0.74, 0.92), 6.0: (0.0, 0.08, 0.74, 0.92),
    6.5: (0.0, 0.08, 0.74, 0.92), 7.0: (0.0, 0.10, 0.80, 0.90),
    7.5: (0.0, 0.10, 0.21, 0.90), 8.0: (0.0, 0.14, 0.30, 0.86),
    8.5: (0.0, 0.17, 0.40, 0.83), 9.0: (0.0, 0.20, 0.49, 0.80),
    9.5: (0.0, 0.22, 0.52, 0.78), 10.0: (0.0, 0.22, 0.52, 0.78),
})
girl = {t: OFF for t in T if t < 7.5}
girl.update({
    7.5: (0.22, 0.44, 0.18, 0.30), 8.0: (0.31, 0.46, 0.21, 0.29),
    8.5: (0.41, 0.46, 0.20, 0.27), 9.0: (0.50, 0.46, 0.18, 0.27),
    9.5: (0.53, 0.46, 0.18, 0.27), 10.0: (0.53, 0.47, 0.18, 0.27),
})
dad = {t: OFF for t in T if t < 7.5}
dad.update({
    7.5: (0.34, 0.30, 0.18, 0.14), 8.0: (0.40, 0.32, 0.22, 0.14),
    8.5: (0.50, 0.32, 0.20, 0.14), 9.0: (0.55, 0.32, 0.20, 0.14),
    9.5: (0.58, 0.32, 0.20, 0.14), 10.0: (0.58, 0.33, 0.20, 0.14),
})
save({
    "mediaId": 261, "level": "A", "keyWord": "electrician", "defaultVoice": "female",
    "taps": [
        {"phrase": "to cut a wire", "target": "the electrician", "voice": "female", "keys": keys(T, el)},
        {"phrase": "to wear a pink T-shirt", "target": "the girl", "voice": "female", "keys": keys(T, girl)},
        {"phrase": "to have a beard", "target": "the man", "voice": "male", "keys": keys(T, dad)},
    ],
    "stillS": 10.0,
    "nouns": [
        {"word": "a door", "x": 0.88, "y": 0.75, "voice": "female"},
        {"word": "a man", "x": 0.69, "y": 0.41, "voice": "male"},
        {"word": "a girl", "x": 0.60, "y": 0.57, "voice": "female"},
        {"word": "an electrician", "x": 0.28, "y": 0.72, "voice": "female"},
    ],
    "question": "What is the electrician doing?",
    "answer": ["She", "is", "cutting", "a", "wire."],
    "answerVoice": "female",
    "notes": "Dark part 0-7.0: the family stands far back in the dark behind the electrician's arms (the girl is faintly visible at about x .05-.28, y .40-.62), so the girl and the man are OFF there and the electrician's box covers that area; please judge. Lights come on at 7.5. The girl stands in front of the man, so from 7.5 the man's box is only his head and chest above the girl's box (split at y about .45). The mother (second woman, between them) belongs to no target; the phrases for girl and man are states because all three clap / hold phone lights. The wire cutting with pliers is at 0-3 s; later she fits and flips a breaker.",
})

# ---------------- 262 elephant (A)
ele = {
    0.0: (0.0, 0.15, 0.84, 0.71), 0.5: (0.0, 0.15, 0.86, 0.71),
    1.0: (0.0, 0.14, 0.90, 0.72), 1.5: (0.0, 0.13, 0.96, 0.73),
    2.0: (0.0, 0.12, 0.98, 0.74), 2.5: (0.0, 0.13, 0.97, 0.73),
    3.0: (0.0, 0.14, 0.96, 0.72), 3.5: (0.0, 0.14, 1.0, 0.72),
    4.0: (0.0, 0.13, 1.0, 0.73), 4.5: (0.0, 0.13, 1.0, 0.73),
    5.0: (0.0, 0.14, 0.96, 0.72), 5.5: (0.0, 0.14, 0.92, 0.72),
    6.0: (0.0, 0.15, 1.0, 0.71), 6.5: (0.0, 0.13, 1.0, 0.73),
    7.0: (0.0, 0.15, 1.0, 0.71), 7.5: (0.0, 0.15, 1.0, 0.71),
    8.0: (0.02, 0.16, 0.95, 0.70), 8.5: (0.0, 0.09, 0.87, 0.77),
    9.0: (0.0, 0.12, 0.85, 0.74), 9.5: (0.0, 0.15, 0.85, 0.71),
    10.0: (0.0, 0.16, 0.91, 0.70),
}
birds = (0.0, 0.87, 1.0, 0.13)
save({
    "mediaId": 262, "level": "A", "keyWord": "elephant", "defaultVoice": "female",
    "taps": [
        {"phrase": "to drink with its trunk", "target": "the elephant", "voice": "female", "keys": keys(T, ele)},
        {"phrase": "to raise its trunk", "target": "the elephant", "voice": "female", "keys": keys(T, ele)},
        {"phrase": "to have white feathers", "target": "the white birds", "voice": "female", "keys": keys(T, birds)},
    ],
    "stillS": 6.0,
    "nouns": [
        {"word": "a tree", "x": 0.40, "y": 0.09, "voice": "female"},
        {"word": "an elephant", "x": 0.52, "y": 0.50, "voice": "female"},
        {"word": "a bird", "x": 0.16, "y": 0.92, "voice": "female"},
        {"word": "water", "x": 0.62, "y": 0.93, "voice": "female"},
    ],
    "question": "What is the elephant doing?",
    "answer": ["It", "is", "drinking", "water", "with", "its", "trunk."],
    "answerVoice": "female",
    "notes": "Only two kinds of target: the elephant (two phrases) and the white birds in the water in front. The birds are a group of 2-3, so their box is one strip over the whole width at the bottom (y .87-1.0); the elephant's box ends at y .86, its feet / trunk tip are cut there. One more tiny white bird far back on the bank (about x .72, y .70-.75, 2.0-9.0) lies inside the elephant's box. The elephant drinks at about 2.0-5.0 and raises its trunk at 8.0-9.5. Nouns: 'a bird' is on the left bird; a second bird stands at the right edge (x .92) with no noun on it.",
})
print("ok")
