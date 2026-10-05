import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OFF = None
def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        if b is None: out.append({"t": t, "off": True})
        else: out.append({"t": t, "x": b[0], "y": b[1], "w": round(b[2], 2), "h": round(b[3], 2)})
    return out
def T(n): return [i * 0.5 for i in range(n)]
def save(c):
    json.dump(c, open(f'{HERE}/content/{c["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)

only = sys.argv[1:]

# ---------------- 4240 ----------------
t = T(25)
puppy = {0.0: (0.10, 0.38, 0.90, 0.47), 0.5: (0.06, 0.42, 0.94, 0.50), 1.0: (0.05, 0.46, 0.85, 0.50), 1.5: (0.0, 0.42, 0.72, 0.51),
         2.0: (0.13, 0.46, 0.87, 0.42), 2.5: (0.05, 0.48, 0.77, 0.35), 3.0: (0.15, 0.46, 0.85, 0.44), 3.5: (0.08, 0.47, 0.80, 0.37)}
big = {0.0: (0.22, 0.0, 0.68, 0.38), 0.5: (0.25, 0.0, 0.65, 0.42), 1.0: (0.28, 0.0, 0.58, 0.46), 1.5: (0.25, 0.0, 0.67, 0.42),
       2.0: (0.30, 0.0, 0.65, 0.46), 2.5: (0.35, 0.0, 0.65, 0.48), 3.0: (0.36, 0.0, 0.64, 0.46), 3.5: (0.38, 0.0, 0.62, 0.47)}
right = {4.0: (0.47, 0.27, 0.40, 0.56), 4.5: (0.47, 0.21, 0.49, 0.70), 5.0: (0.48, 0.15, 0.52, 0.82), 5.5: (0.50, 0.13, 0.50, 0.84),
         6.0: (0.51, 0.13, 0.49, 0.77), 6.5: (0.51, 0.13, 0.49, 0.77), 7.0: (0.53, 0.14, 0.47, 0.78), 7.5: (0.53, 0.15, 0.47, 0.77),
         8.0: (0.51, 0.20, 0.49, 0.70), 8.5: (0.45, 0.17, 0.55, 0.73), 9.0: (0.46, 0.17, 0.54, 0.75), 9.5: (0.46, 0.17, 0.54, 0.75),
         10.0: (0.47, 0.17, 0.53, 0.73)}
c4240 = {"mediaId": 4240, "level": "B", "keyWord": "identical", "defaultVoice": "female",
 "taps": [
  {"phrase": "to roll on its back", "target": "the puppy", "voice": "female", "keys": keys(t, puppy)},
  {"phrase": "to tower over the puppy", "target": "the big dog", "voice": "female", "keys": keys(t, big)},
  {"phrase": "to touch its companion's chest", "target": "the dog on the right", "voice": "female", "keys": keys(t, right)}],
 "stillS": 0.0,
 "nouns": [{"word": "a curtain", "x": 0.16, "y": 0.14, "voice": "female"},
           {"word": "a puppy", "x": 0.42, "y": 0.47, "voice": "female"},
           {"word": "a carpet", "x": 0.80, "y": 0.33, "voice": "female"},
           {"word": "a smartphone", "x": 0.22, "y": 0.85, "voice": "female"}],
 "question": "What is the puppy doing?",
 "answer": ["The", "puppy", "is", "rolling", "on", "its", "back."],
 "answerVoice": "female",
 "notes": "Packet description does not mention the first shot's puppy and phone (0-3.5 s): a puppy steps on a phone, then rolls on its back under an adult husky. 'the big dog' = the adult husky standing over the puppy in shot 1 only (cannot tell which of the two dogs of shot 2 it is, so it is off there). 'the dog on the right' = shot 2 (4-10 s), lifts a paw at 8 s and lays it on the other dog's chest 8.5-10 s; the close-up 10.5-12 s is off (unclear which dog). In shot 1 the puppy lies in front of the big dog's legs, boxes split along a horizontal line. At 0.0 s the puppy has not rolled yet (rolls from 1.0 s)."}

# ---------------- 4241 ----------------
pilot = {x: (0.0, 0.12, 1.0, 0.88) for x in (0.0, 0.5, 1.0, 1.5)}
clouds = {2.0: (0.0, 0.44, 1.0, 0.50), 2.5: (0.0, 0.41, 1.0, 0.53), 3.0: (0.0, 0.39, 1.0, 0.55), 3.5: (0.0, 0.33, 1.0, 0.61),
          4.0: (0.0, 0.30, 1.0, 0.64), 4.5: (0.0, 0.28, 1.0, 0.66), 5.0: (0.0, 0.25, 1.0, 0.69)}
runway = {9.0: (0.31, 0.36, 0.22, 0.17), 9.5: (0.29, 0.28, 0.23, 0.25), 10.0: (0.26, 0.27, 0.25, 0.26), 10.5: (0.0, 0.44, 1.0, 0.50),
          11.0: (0.0, 0.45, 1.0, 0.50), 11.5: (0.0, 0.44, 1.0, 0.52), 12.0: (0.0, 0.45, 1.0, 0.47)}
c4241 = {"mediaId": 4241, "level": "B", "keyWord": "pilot", "defaultVoice": "male",
 "taps": [
  {"phrase": "to wear a green headset", "target": "the pilot", "voice": "male", "keys": keys(t, pilot)},
  {"phrase": "to float below the aircraft", "target": "the white clouds", "voice": "male", "keys": keys(t, clouds)},
  {"phrase": "to have painted markings", "target": "the runway", "voice": "male", "keys": keys(t, runway)}],
 "stillS": 0.0,
 "nouns": [{"word": "a headset", "x": 0.74, "y": 0.38, "voice": "male"},
           {"word": "a microphone", "x": 0.55, "y": 0.555, "voice": "male"},
           {"word": "a seat belt", "x": 0.22, "y": 0.72, "voice": "male"},
           {"word": "a tie", "x": 0.55, "y": 0.88, "voice": "male"}],
 "question": "What is the man doing?",
 "answer": ["He", "is", "piloting", "the", "aircraft."],
 "answerVoice": "male",
 "notes": "The pilot only looks into the camera (0-1.5 s), so his phrase is a state. The white clouds = the cloud deck below the aircraft 2-5 s; off 5.5-8.5 s (inside the cloud / haze, nothing to tap) and off from 10.5 s (grey overcast sky above the runway is not the white deck). The runway is tiny and far away 9-10 s, full width from 10.5 s. The answer uses the key word as a verb; the piloting is inferred from uniform + cockpit + the landing, his hands on the controls are never shown. Both dark straps are the seat belt; the pill sits on the left one."}

# ---------------- 4242 ----------------
t2 = T(24)
gate = {0.0: (0.05, 0.0, 0.88, 0.14), 0.5: (0.05, 0.0, 0.90, 0.13), 1.0: (0.06, 0.0, 0.88, 0.15), 1.5: (0.05, 0.0, 0.90, 0.13),
        2.0: (0.05, 0.0, 0.90, 0.17), 2.5: (0.05, 0.0, 0.85, 0.25), 3.0: (0.0, 0.32, 0.92, 0.26), 3.5: (0.03, 0.16, 0.37, 0.50),
        4.0: (0.0, 0.09, 0.52, 0.50), 4.5: (0.0, 0.0, 1.0, 0.51), 5.0: (0.08, 0.0, 0.92, 0.46), 5.5: (0.20, 0.0, 0.80, 0.36),
        6.0: (0.20, 0.0, 0.80, 0.31), 6.5: (0.20, 0.0, 0.80, 0.31), 7.0: (0.30, 0.0, 0.70, 0.31), 7.5: (0.30, 0.0, 0.70, 0.32),
        8.0: (0.32, 0.0, 0.68, 0.32), 8.5: (0.33, 0.0, 0.67, 0.33), 9.0: (0.35, 0.0, 0.65, 0.36), 9.5: (0.37, 0.0, 0.63, 0.33),
        10.0: (0.38, 0.0, 0.62, 0.28), 10.5: (0.40, 0.0, 0.60, 0.29), 11.0: (0.40, 0.0, 0.60, 0.34), 11.5: (0.38, 0.0, 0.62, 0.52)}
orange = {0.0: (0.0, 0.36, 0.50, 0.41), 0.5: (0.0, 0.36, 0.52, 0.41), 1.0: (0.0, 0.36, 0.52, 0.42), 1.5: (0.0, 0.37, 0.52, 0.41),
          2.0: (0.0, 0.23, 0.50, 0.49), 2.5: (0.24, 0.25, 0.40, 0.30), 3.0: (0.34, 0.0, 0.32, 0.32), 3.5: (0.40, 0.28, 0.26, 0.30),
          4.0: (0.52, 0.20, 0.22, 0.28)}
grey = {0.0: (0.55, 0.38, 0.42, 0.39), 0.5: (0.56, 0.36, 0.44, 0.41), 1.0: (0.57, 0.36, 0.43, 0.41), 1.5: (0.57, 0.37, 0.43, 0.40),
        2.0: (0.52, 0.39, 0.48, 0.40), 2.5: (0.36, 0.56, 0.56, 0.44), 3.0: (0.26, 0.69, 0.62, 0.31), 3.5: (0.26, 0.73, 0.64, 0.27),
        4.0: (0.26, 0.68, 0.74, 0.32), 4.5: (0.26, 0.52, 0.74, 0.48), 5.0: (0.29, 0.46, 0.50, 0.42), 5.5: (0.21, 0.36, 0.45, 0.34),
        6.0: (0.17, 0.31, 0.43, 0.32), 6.5: (0.17, 0.31, 0.43, 0.32), 7.0: (0.20, 0.31, 0.43, 0.33), 7.5: (0.26, 0.32, 0.41, 0.32),
        8.0: (0.28, 0.32, 0.42, 0.31), 8.5: (0.26, 0.33, 0.45, 0.30), 9.0: (0.23, 0.36, 0.44, 0.24), 9.5: (0.23, 0.33, 0.39, 0.26),
        10.0: (0.24, 0.28, 0.38, 0.30), 10.5: (0.24, 0.29, 0.36, 0.29), 11.0: (0.25, 0.34, 0.33, 0.24)}
c4242 = {"mediaId": 4242, "level": "A", "keyWord": "pass", "defaultVoice": "female",
 "taps": [
  {"phrase": "to jump over the gate", "target": "the orange cat", "voice": "female", "keys": keys(t2, orange)},
  {"phrase": "to pass through a door", "target": "the grey cat", "voice": "female", "keys": keys(t2, grey)},
  {"phrase": "to block the way", "target": "the gate", "voice": "female", "keys": keys(t2, gate)}],
 "stillS": 8.0,
 "nouns": [{"word": "a gate", "x": 0.74, "y": 0.15, "voice": "female"},
           {"word": "a wall", "x": 0.17, "y": 0.22, "voice": "female"},
           {"word": "a cat", "x": 0.47, "y": 0.46, "voice": "female"},
           {"word": "the floor", "x": 0.50, "y": 0.80, "voice": "female"}],
 "question": "What is the grey cat doing?",
 "answer": ["It", "is", "passing", "through", "a", "small", "door."],
 "answerVoice": "female",
 "notes": "The packet description is wrong about the orange cat: frame 3.0 s shows it on top of the gate with its tail hanging down in front of the bars, at 3.5 s it is coming down behind the bars - it jumps OVER the gate, it does not slip between the bars. So the key word 'pass' goes to the grey (tabby) cat, which passes through the small cat door in the wall (8.5-11 s). Orange cat off from 4.5 s (only a faint bit behind the bars). At 3.5 and 4.0 s the orange cat is seen through the gate: the gate box is the left part of the gate only. From 5.5 s the grey cat's tail stands in front of the gate: gate box = the part above the cat. 'to block the way' is a state and the least simple of the three phrases (block ~A2/B1)."}

# ---------------- 4244 ----------------
bull = {0.0: (0.42, 0.28, 0.58, 0.36), 0.5: (0.35, 0.28, 0.65, 0.32), 1.0: (0.40, 0.32, 0.44, 0.25), 1.5: (0.39, 0.33, 0.40, 0.23),
        2.0: (0.26, 0.35, 0.46, 0.19), 2.5: (0.23, 0.43, 0.43, 0.14), 3.0: (0.26, 0.33, 0.44, 0.21), 3.5: (0.34, 0.32, 0.48, 0.22),
        4.0: (0.38, 0.43, 0.43, 0.14), 4.5: (0.36, 0.42, 0.48, 0.15), 6.5: (0.36, 0.41, 0.50, 0.16), 7.0: (0.36, 0.32, 0.56, 0.28),
        7.5: (0.26, 0.31, 0.72, 0.28), 8.0: (0.26, 0.28, 0.55, 0.33), 8.5: (0.21, 0.26, 0.47, 0.39), 9.0: (0.08, 0.26, 0.57, 0.45),
        9.5: (0.0, 0.25, 0.66, 0.62), 10.0: (0.0, 0.13, 1.0, 0.62), 10.5: (0.0, 0.14, 1.0, 0.60), 11.0: (0.0, 0.10, 1.0, 0.76),
        11.5: (0.0, 0.08, 1.0, 0.80)}
goat = {0.0: (0.08, 0.34, 0.20, 0.15), 0.5: (0.14, 0.34, 0.19, 0.14), 1.0: (0.19, 0.35, 0.20, 0.15), 1.5: (0.20, 0.37, 0.18, 0.14),
        2.5: (0.37, 0.29, 0.20, 0.14), 4.0: (0.42, 0.29, 0.19, 0.14), 4.5: (0.46, 0.28, 0.18, 0.14), 6.5: (0.45, 0.27, 0.18, 0.14),
        8.5: (0.68, 0.36, 0.18, 0.14), 9.0: (0.65, 0.37, 0.19, 0.15), 9.5: (0.66, 0.37, 0.19, 0.14)}
man = {5.0: (0.0, 0.05, 0.50, 0.95), 5.5: (0.0, 0.08, 0.42, 0.92), 6.0: (0.0, 0.10, 0.37, 0.90)}
c4244 = {"mediaId": 4244, "level": "B", "keyWord": "charge", "defaultVoice": "female",
 "taps": [
  {"phrase": "to charge towards the car", "target": "the bull", "voice": "female", "keys": keys(t2, bull)},
  {"phrase": "to watch from a distance", "target": "the goat", "voice": "female", "keys": keys(t2, goat)},
  {"phrase": "to throw his head back", "target": "the man in front", "voice": "male", "keys": keys(t2, man)}],
 "stillS": 9.0,
 "nouns": [{"word": "a tree", "x": 0.22, "y": 0.15, "voice": "female"},
           {"word": "a goat", "x": 0.72, "y": 0.44, "voice": "female"},
           {"word": "a bull", "x": 0.36, "y": 0.56, "voice": "female"},
           {"word": "gravel", "x": 0.66, "y": 0.69, "voice": "female"}],
 "question": "What is the bull doing?",
 "answer": ["It", "is", "charging", "towards", "the", "car."],
 "answerVoice": "female",
 "notes": "The packet calls the small white animal a dog; the frames (0.0 s and 9.5 s enlarged) show a white GOAT (long neck, goat ears, short upright tail), so the target and noun are 'the goat' / 'a goat'. The goat watches from a distance at 8.5-9.5 s; earlier it walks beside the bull and is on / behind the rolling bull (2.5-6.5 s, box = the part above the bull's back, split line at the bull's back). Goat off at 2.0, 3.0, 3.5, 7.0-8.0 and from 10.0 s (hidden in dust / behind the bull). 'to throw his head back': the man in front (hoodie, seat belt) laughs with his head thrown back 5-6 s; the man behind him also laughs but leans forward / sideways - the verifier should check that this is distinct enough. defaultVoice by evenId (main subject is the bull)."}

for c in (c4240, c4241, c4242, c4244):
    if not only or str(c["mediaId"]) in only: save(c)
