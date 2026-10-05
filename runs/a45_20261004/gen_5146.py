import json
def keys(times, boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": round(b[0],2), "y": round(b[1],2), "w": round(b[2],2), "h": round(b[3],2)} for t, b in zip(times, boxes)]
T = [i*0.5 for i in range(25)]
N = None
wom = [(0,.04,1,.63),(0,.04,1,.63),(0,.04,1,.64),(0,.04,1,.64),(0,.04,.95,.61),(0,0,1,.60),(0,0,1,.60),(0,0,1,.58),(0,0,1,.55),(0,0,1,.55),(0,0,1,.55),(0,0,1,.55),
       (0,.02,1,.68),(0,.03,1,.67),(0,.03,1,.67),(0,.02,1,.66),(0,0,1,.62),(0,0,1,.56),(0,0,1,.50),(0,0,1,.45),(0,0,1,.42),(0,0,1,.42),(0,0,1,.45),(0,0,1,.47),(0,0,1,.50)]
bowl = [(.17,.67,.66,.25),(.17,.67,.66,.25),(.15,.68,.67,.25),(.16,.68,.68,.25),(.14,.65,.68,.27),(.08,.60,.84,.33),(.07,.60,.82,.33),(0,.58,.98,.38),(0,.55,.97,.42),(0,.55,1,.40),(0,.55,1,.44),(0,.55,1,.43),
        (.14,.70,.72,.27),(.14,.70,.74,.28),(.14,.70,.74,.28),(.14,.68,.74,.28),(.14,.62,.69,.24),(.16,.56,.63,.20),(.16,.50,.63,.20),(.19,.45,.60,.18),(.21,.42,.58,.16),(.21,.42,.56,.16),(.22,.45,.56,.16),(.22,.47,.57,.15),(.24,.50,.55,.14)]
peel = [N]*19 + [(.39,.63,.19,.23),(.36,.58,.20,.36),(.42,.58,.20,.42),(.40,.61,.18,.39),(.40,.62,.20,.38),(.41,.64,.17,.36)]
kw, kb, kp = keys(T, wom), keys(T, bowl), keys(T, peel)
d = {"mediaId": 5146, "level": "B", "keyWord": "strip", "defaultVoice": "female",
 "taps": [{"phrase": "to peel a red apple", "target": "the woman", "voice": "female", "keys": kw},
          {"phrase": "to rest on her lap", "target": "the bowl", "voice": "female", "keys": kb},
          {"phrase": "to dangle past her knees", "target": "the strip of peel", "voice": "female", "keys": kp}],
 "stillS": 11.0,
 "nouns": [{"word": "geraniums", "x": 0.20, "y": 0.15, "voice": "female"}, {"word": "an apron", "x": 0.40, "y": 0.39, "voice": "female"},
           {"word": "a bowl", "x": 0.32, "y": 0.52, "voice": "female"}, {"word": "a strip of peel", "x": 0.52, "y": 0.82, "voice": "female"}],
 "question": "What is the woman doing?",
 "answer": ["She", "is", "peeling", "an", "apple", "in", "one", "long", "strip."], "answerVoice": "female",
 "notes": "The woman holds the bowl on her lap, so the picture is split horizontally: the woman's box is everything above the bowl's rim (head, arms, apple, knife), the bowl's box is the bowl, the strip's box only the part hanging below the bowl (9.5-12.0; earlier the strip lies in the bowl or hangs in front of her hands and is off). Her legs below the bowl are not in her box. At 2.5-5.5 (close-up) the apple she peels is a pale one; from 6.0 a red one, so 'to peel a red apple' fits most of the clip. 'strip' = key word, in the noun 'a strip of peel' and the answer."}
json.dump(d, open('content/5146.json','w'), indent=1, ensure_ascii=False)
