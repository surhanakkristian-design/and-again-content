import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [i*0.5 for i in range(19)]
def keys(boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]} for t, b in zip(T, boxes)]
man = [(.03,.28,.95,.72)]*3 + [(.03,.29,.95,.71),(0,.23,1,.77),(.04,.32,.94,.68),(.03,.32,.95,.68),(.03,.32,.95,.68),
       (.03,.32,.95,.68),(.03,.32,.95,.68),(.03,.31,.95,.69)] + [None]*8
light = [(.40,.02,.22,.25)]*4 + [(.41,.02,.2,.2)] + [(.30,.02,.40,.22),(.29,.02,.42,.23),(.29,.02,.42,.23),(.29,.02,.42,.23),(.29,.02,.42,.23),(.29,.02,.42,.23),
         (.40,.43,.19,.20),(.40,.45,.19,.2),(.40,.45,.19,.21),(.40,.46,.19,.22),(.40,.47,.18,.23),(.40,.49,.19,.21),(.40,.51,.18,.2),(.40,.51,.18,.21)]
km = keys(man)
c = {"mediaId": 5415, "level": "A", "keyWord": "red", "defaultVoice": "male",
 "taps": [
  {"phrase": "to look up at the light", "target": "the man", "voice": "male", "keys": km},
  {"phrase": "to smile at the green light", "target": "the man", "voice": "male", "keys": km},
  {"phrase": "to turn red", "target": "the traffic light", "voice": "male", "keys": keys(light)}],
 "stillS": 3.0,
 "nouns": [{"word": "a traffic light", "x": .5, "y": .12, "voice": "male"},
           {"word": "trees", "x": .13, "y": .25, "voice": "male"},
           {"word": "a helmet", "x": .5, "y": .36, "voice": "male"},
           {"word": "a motorbike", "x": .5, "y": .9, "voice": "male"}],
 "question": "What is the man looking at?",
 "answer": ["He", "is", "looking", "at", "the", "traffic", "light."],
 "answerVoice": "male",
 "notes": "From 2.5 s the traffic light is a cluster (main light + pedestrian lights); box covers the cluster. In the wide shot (5.5-9.0) the man is off and the light box follows the big light on the middle strip, which turns from red to green. The man smiles only at 4.5-5.0 s."}
json.dump(c, open(f"{HERE}/content/5415.json", "w"), indent=1)
