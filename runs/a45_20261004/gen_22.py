# writes content/22.json, 23.json, 24.json, 25.json
import json, os
H = os.path.dirname(os.path.abspath(__file__))
def keys(n, d):
    out = []
    for i in range(n):
        t = i * 0.5
        b = d.get(t)
        out.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": round(min(b[2], 1 - b[0]), 2), "h": round(min(b[3], 1 - b[1]), 2)})
    return out
def save(c):
    json.dump(c, open(f'{H}/content/{c["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)

# ---- 22
stu = {0.0: (0.08, 0.24, 0.70, 0.76), 0.5: (0, 0.25, 1, 0.75), 1.0: (0.15, 0.28, 0.52, 0.72), 1.5: (0, 0.58, 0.18, 0.42)}
sci = {2.5: (0, 0.35, 0.42, 0.6), 3.0: (0.07, 0.35, 0.58, 0.65), 3.5: (0, 0.03, 0.62, 0.97), 4.0: (0, 0.05, 0.72, 0.95),
       4.5: (0, 0.07, 0.66, 0.93), 5.0: (0, 0.05, 0.82, 0.95), 5.5: (0, 0.3, 0.97, 0.7), 6.0: (0, 0.27, 0.97, 0.73),
       6.5: (0, 0.19, 0.64, 0.81), 7.0: (0, 0.25, 0.88, 0.75), 7.5: (0, 0.25, 0.82, 0.75), 8.0: (0, 0.24, 0.83, 0.76)}
save({"mediaId": 22, "level": "A", "keyWord": "scientist", "defaultVoice": "male",
 "taps": [
  {"phrase": "to walk past the poster", "target": "the student", "voice": "male", "keys": keys(17, stu)},
  {"phrase": "to write some notes", "target": "the scientist", "voice": "male", "keys": keys(17, sci)},
  {"phrase": "to point at a line", "target": "the scientist", "voice": "male", "keys": keys(17, sci)}],
 "stillS": 7.5,
 "nouns": [{"word": "a scientist", "x": 0.22, "y": 0.62, "voice": "male"}, {"word": "glasses", "x": 0.28, "y": 0.33, "voice": "male"},
           {"word": "a pen", "x": 0.62, "y": 0.91, "voice": "male"}, {"word": "a poster", "x": 0.76, "y": 0.22, "voice": "male"}],
 "question": "What is the scientist doing?",
 "answer": ["The", "scientist", "is", "writing", "some", "notes."], "answerVoice": "male",
 "notes": "Two men, never in the same frame (student 0-1.5 s, scientist 2.5-8 s; 2.0 s shows only the poster). The student also glances at the poster, so no 'look at' phrase. Writing is visible 5.5-6.0 s, pointing 4.0-5.0 s. 'glasses' = safety glasses pushed up on his forehead."})

# ---- 23
wom = {0.0: (0.35, 0.1, 0.65, 0.9), 0.5: (0.17, 0.05, 0.83, 0.95), 1.0: (0.07, 0, 0.93, 1), 1.5: (0, 0, 1, 1), 2.0: (0, 0, 1, 1),
       2.5: (0.17, 0, 0.83, 1), 3.0: (0.55, 0, 0.45, 1), 3.5: (0.55, 0.03, 0.45, 0.97), 4.0: (0.3, 0.03, 0.7, 0.97),
       4.5: (0.58, 0.03, 0.42, 0.97), 5.0: (0.6, 0.03, 0.4, 0.97), 5.5: (0.58, 0.05, 0.42, 0.95), 6.0: (0.56, 0.03, 0.44, 0.97),
       6.5: (0.56, 0.03, 0.44, 0.97), 7.0: (0.56, 0.03, 0.44, 0.97), 7.5: (0.57, 0.05, 0.43, 0.95), 8.0: (0.56, 0, 0.44, 1),
       8.5: (0.56, 0, 0.44, 1), 9.0: (0.56, 0, 0.44, 1), 9.5: (0.57, 0.07, 0.43, 0.93), 10.0: (0.55, 0.05, 0.45, 0.95)}
man = {3.5: (0, 0.6, 0.14, 0.38), 4.0: (0, 0.46, 0.27, 0.5), 4.5: (0, 0.45, 0.32, 0.5), 5.0: (0, 0.47, 0.32, 0.53),
       5.5: (0.05, 0.47, 0.3, 0.53), 6.0: (0.03, 0.45, 0.3, 0.5), 6.5: (0.05, 0.45, 0.3, 0.5), 7.0: (0.05, 0.47, 0.3, 0.53),
       7.5: (0.05, 0.47, 0.3, 0.53), 8.0: (0.05, 0.45, 0.3, 0.5), 8.5: (0.05, 0.45, 0.3, 0.5), 9.0: (0.07, 0.47, 0.32, 0.53),
       9.5: (0.05, 0.33, 0.35, 0.67), 10.0: (0.05, 0.33, 0.35, 0.62)}
save({"mediaId": 23, "level": "A", "keyWord": "speech", "defaultVoice": "female",
 "taps": [
  {"phrase": "to give a speech", "target": "the woman in green", "voice": "female", "keys": keys(21, wom)},
  {"phrase": "to drink some water", "target": "the woman in green", "voice": "female", "keys": keys(21, wom)},
  {"phrase": "to wear a grey suit", "target": "the man in grey", "voice": "male", "keys": keys(21, man)}],
 "stillS": 2.0,
 "nouns": [{"word": "windows", "x": 0.30, "y": 0.15, "voice": "female"}, {"word": "a woman", "x": 0.80, "y": 0.50, "voice": "female"},
           {"word": "a microphone", "x": 0.33, "y": 0.56, "voice": "female"}, {"word": "a glass", "x": 0.50, "y": 0.68, "voice": "female"}],
 "question": "What is the woman in green doing?",
 "answer": ["She", "is", "giving", "a", "speech."], "answerVoice": "female",
 "notes": "The key word 'speech' is not a placeable thing, so it is in a phrase and the answer. Phrase 3 is a state: the bearded man's only action (clapping, 9.0-10.0 s) is shared with the grey-haired woman next to him. At 4.0 s the speaker's outstretched hand lies in front of the man; the boxes are split at x 0.27-0.30, her hand falls in his box. Drinking is brief (6.0-6.5 s). 'a microphone' may be a little hard for level A."})

# ---- 24
girl = {0.0: (0, 0, 0.58, 0.76), 0.5: (0, 0, 0.55, 0.83), 1.0: (0.24, 0.56, 0.52, 0.44), 1.5: (0.26, 0.58, 0.52, 0.42),
        2.0: (0.62, 0.21, 0.38, 0.35), 2.5: (0.78, 0.34, 0.22, 0.32), 3.0: (0, 0, 1, 1), 3.5: (0, 0, 1, 1), 4.0: (0, 0, 1, 1),
        4.5: (0, 0.13, 1, 0.7), 5.0: (0, 0.12, 1, 0.8), 5.5: (0, 0.15, 1, 0.8), 6.0: (0, 0.13, 1, 0.72), 6.5: (0, 0, 1, 0.78),
        7.0: (0, 0, 1, 0.92), 7.5: (0, 0, 1, 0.92), 8.0: (0, 0, 1, 0.85)}
save({"mediaId": 24, "level": "A", "keyWord": "spoon", "defaultVoice": "female",
 "taps": [
  {"phrase": "to open a drawer", "target": "the girl", "voice": "female", "keys": keys(17, girl)},
  {"phrase": "to take a spoon", "target": "the girl", "voice": "female", "keys": keys(17, girl)},
  {"phrase": "to eat some soup", "target": "the girl", "voice": "female", "keys": keys(17, girl)}],
 "stillS": 5.0,
 "nouns": [{"word": "a window", "x": 0.78, "y": 0.18, "voice": "female"}, {"word": "a spoon", "x": 0.42, "y": 0.585, "voice": "female"},
           {"word": "a bowl", "x": 0.50, "y": 0.74, "voice": "female"}, {"word": "a table", "x": 0.50, "y": 0.90, "voice": "female"}],
 "question": "What is the girl doing?",
 "answer": ["She", "is", "eating", "soup", "with", "a", "spoon."], "answerVoice": "female",
 "notes": "Only one possible target (the girl); spoon, pot and bowl always overlap her hands, so all three phrases are hers. In several shots only her hand or arm is visible (0-2.5 s) and the box is that hand/arm; at 3.0-4.0 s face left and hand right, box = whole frame; 6.5-8.0 s sweater and hands around the bowl. At 1.5 s her face is mirrored in the spoon (not boxed)."})

# ---- 25
m = {0.0: (0.1, 0.19, 0.8, 0.58), 0.5: (0.13, 0.19, 0.75, 0.57), 1.0: (0.09, 0.17, 0.82, 0.58), 1.5: (0.09, 0.17, 0.82, 0.58),
     2.0: (0.02, 0.02, 0.98, 0.48), 2.5: (0.29, 0, 0.71, 0.17), 3.0: (0.17, 0.19, 0.75, 0.58), 3.5: (0.12, 0.07, 0.88, 0.66),
     4.0: (0.13, 0.17, 0.87, 0.42), 4.5: (0.26, 0.03, 0.48, 0.48), 5.0: (0.24, 0.17, 0.55, 0.4), 5.5: (0.22, 0.17, 0.6, 0.4),
     6.0: (0.21, 0.12, 0.56, 0.38), 6.5: (0, 0, 1, 0.74), 7.0: (0, 0, 1, 0.87), 7.5: (0.18, 0.12, 0.64, 0.5),
     8.0: (0.18, 0.25, 0.64, 0.37), 8.5: (0.03, 0.35, 0.86, 0.65), 9.0: (0.02, 0.42, 0.87, 0.58)}
save({"mediaId": 25, "level": "A", "keyWord": "stapler", "defaultVoice": "male",
 "taps": [
  {"phrase": "to use a red stapler", "target": "the man", "voice": "male", "keys": keys(19, m)},
  {"phrase": "to lift the paper up", "target": "the man", "voice": "male", "keys": keys(19, m)},
  {"phrase": "to wear a purple shirt", "target": "the man", "voice": "male", "keys": keys(19, m)}],
 "stillS": 1.0,
 "nouns": [{"word": "a man", "x": 0.50, "y": 0.36, "voice": "male"}, {"word": "a plant", "x": 0.83, "y": 0.46, "voice": "male"},
           {"word": "a stapler", "x": 0.50, "y": 0.63, "voice": "male"}, {"word": "paper", "x": 0.50, "y": 0.78, "voice": "male"}],
 "question": "What is the man doing?",
 "answer": ["He", "is", "using", "a", "red", "stapler."], "answerVoice": "male",
 "notes": "Only one possible target (the man); stapler and paper always overlap him. Third phrase is a state. At 2.0-2.5 s only his hand/arm is in the picture (box = hand). At 3.0-4.0 s a second red stapler lies at the left edge. Still 1.0 s: 'a man' on the face, 'a stapler' on the stapler he holds, 'paper' on the pile below it (pills stacked at x 0.5, 0.14 apart)."})
