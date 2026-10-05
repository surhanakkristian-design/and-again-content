import json
def keys(times, boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": round(b[2], 2), "h": round(b[3], 2)} for t, b in zip(times, boxes)]
T = [i * 0.5 for i in range(21)]
wom = [(0,0,.58,.70),(0,0,.74,.68),(0,0,.82,.64),(0,0,.84,.64),(0,0,.64,.62),(0,0,.68,.62),(0,.01,.69,.62),(0,.02,.74,.62),(0,0,.72,.62),(0,0,.70,.60),
       (0,0,.69,.60),(0,0,.82,.60),(0,0,.86,.52),(0,0,.86,.47),(0,0,.54,.72),(0,0,.82,.86),(0,0,.82,.80),(0,0,.87,.80),(0,0,.89,.84),(0,0,.92,.84),(0,0,.92,.84)]
kw = keys(T, wom)
d = {"mediaId": 5115, "level": "A", "keyWord": "study", "defaultVoice": "female",
 "taps": [{"phrase": "to study an insect", "target": "the young woman", "voice": "female", "keys": kw},
          {"phrase": "to use a magnifying glass", "target": "the young woman", "voice": "female", "keys": kw},
          {"phrase": "to draw in a notebook", "target": "the young woman", "voice": "female", "keys": kw}],
 "stillS": 4.5,
 "nouns": [{"word": "a cap", "x": 0.45, "y": 0.18, "voice": "female"}, {"word": "flowers", "x": 0.85, "y": 0.40, "voice": "female"},
           {"word": "a magnifying glass", "x": 0.38, "y": 0.53, "voice": "female"}, {"word": "a log", "x": 0.50, "y": 0.72, "voice": "female"}],
 "question": "What is the young woman doing?",
 "answer": ["She", "is", "studying", "a", "small", "insect."], "answerVoice": "female",
 "notes": "Only one person; the insect is a tiny green bug on the log right next to her hand / face (would overlap her box), the notebook lies under her writing hand, so all three phrases are on the woman. Magnifying glass appears from 3.0; drawing with a pencil from 7.5. Her box grows to cover the writing hand and the notebook at 7.5-10.0."}
json.dump(d, open('content/5115.json', 'w'), indent=1, ensure_ascii=False)
