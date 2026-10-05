import json
OFF=None
def keys(times, boxes):
    assert len(times)==len(boxes), (len(times),len(boxes))
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            assert b[0]+b[2]<=1.0001 and b[1]+b[3]<=1.0001, (t,b)
            out.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
t=[round(i*0.5,2) for i in range(21)]
def save(d):
    json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 394
M=[(0.05,0.18,0.90,0.82),(0.0,0.20,0.95,0.80),(0.0,0.20,0.95,0.80),
   (0.10,0.27,0.52,0.73),(0.24,0.25,0.42,0.75),(0.21,0.25,0.43,0.75),(0.16,0.25,0.46,0.75),(0.20,0.23,0.45,0.77),
   (0.11,0.21,0.53,0.79),(0.10,0.19,0.55,0.81),(0.08,0.21,0.57,0.79),(0.18,0.22,0.48,0.78),
   (0.12,0.27,0.26,0.70),(0.08,0.28,0.50,0.19),(0.08,0.21,0.48,0.25),(0.0,0.20,1.0,0.27),
   (0.0,0.19,1.0,0.28),(0.0,0.19,1.0,0.29),(0.22,0.34,0.54,0.14),(0.60,0.48,0.24,0.42),(0.58,0.42,0.24,0.48)]
F=[OFF,OFF,OFF,
   (0.62,0.50,0.33,0.40),(0.66,0.50,0.27,0.34),(0.64,0.48,0.30,0.38),(0.62,0.47,0.31,0.45),(0.65,0.50,0.29,0.40),
   (0.64,0.49,0.29,0.38),(0.65,0.49,0.29,0.38),(0.65,0.49,0.28,0.42),(0.66,0.50,0.28,0.42),
   (0.38,0.40,0.38,0.40),(0.29,0.47,0.52,0.48),(0.25,0.46,0.50,0.52),(0.22,0.47,0.54,0.53),
   (0.22,0.47,0.52,0.50),(0.22,0.48,0.52,0.48),(0.22,0.48,0.54,0.50),(0.22,0.44,0.38,0.54),(0.22,0.42,0.36,0.56)]
km=keys(t,M)
save({"mediaId":394,"level":"A","keyWord":"hot","defaultVoice":"male",
 "taps":[
  {"phrase":"to wipe his face","target":"the man","voice":"male","keys":km},
  {"phrase":"to hold a water bottle","target":"the man","voice":"male","keys":km},
  {"phrase":"to blow air on him","target":"the fan","voice":"male","keys":keys(t,F)}],
 "stillS":3.5,
 "nouns":[{"word":"a roof","x":0.35,"y":0.13,"voice":"male"},{"word":"a wall","x":0.80,"y":0.32,"voice":"male"},
          {"word":"a fan","x":0.80,"y":0.57,"voice":"male"},{"word":"a towel","x":0.38,"y":0.67,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","wiping","his","face","with","a","towel."],"answerVoice":"male",
 "notes":"Key word 'hot' is an adjective, not used as a noun; the answer uses phrase 1 + the noun towel. From 6.0 s the man stands behind the fan, the bodies overlap: boxes split (6.0 vertical, 6.5-9.0 the man = band above the fan head, 9.5-10.0 the man = the part right of the fan head); parts of the man's body behind the fan grille belong to the fan box. 'to hold a water bottle': he presses the bottle to his forehead 4.0-5.5 (pouring is not clearly visible in the frames, so not claimed). 'wipe' is A2. The fan is behind him and not turned to him at 1.5-5.5; it blows on him from 6.0."})

# ---------- 396
M=[(0.10,0.16,0.82,0.84),(0.03,0.17,0.94,0.83),(0.08,0.0,0.92,1.0),OFF,
   OFF,OFF,(0.70,0.30,0.30,0.70),(0.45,0.25,0.45,0.75),
   (0.33,0.21,0.42,0.79),(0.52,0.21,0.46,0.79),(0.0,0.20,0.39,0.80),(0.61,0.20,0.30,0.22),
   (0.52,0.16,0.43,0.84),(0.17,0.21,0.61,0.30),(0.46,0.16,0.36,0.84),(0.58,0.14,0.42,0.86),
   (0.57,0.13,0.43,0.87),(0.37,0.14,0.45,0.86),(0.03,0.14,0.79,0.39),(0.0,0.14,0.78,0.48),(0.0,0.18,0.80,0.33)]
W=[OFF,OFF,OFF,OFF,
   (0.22,0.32,0.30,0.45),(0.18,0.34,0.52,0.45),(0.19,0.36,0.51,0.40),(0.10,0.30,0.35,0.70),
   (0.02,0.25,0.31,0.75),(0.10,0.24,0.42,0.76),(0.39,0.22,0.61,0.37),(0.03,0.22,0.58,0.78),
   (0.02,0.22,0.48,0.75),(0.05,0.51,0.39,0.46),(0.03,0.26,0.43,0.74),(0.0,0.26,0.58,0.74),
   (0.0,0.24,0.57,0.76),(0.0,0.24,0.37,0.76),(0.03,0.53,0.45,0.47),(0.0,0.62,0.50,0.38),(0.0,0.51,0.50,0.49)]
D=[OFF,OFF,OFF,OFF,
   (0.0,0.48,0.18,0.15),(0.0,0.48,0.18,0.14),(0.0,0.50,0.19,0.15),OFF,
   OFF,OFF,OFF,OFF,
   OFF,(0.78,0.52,0.19,0.14),(0.82,0.50,0.18,0.15),OFF,
   OFF,(0.82,0.49,0.18,0.15),(0.82,0.49,0.18,0.15),(0.82,0.46,0.18,0.16),(0.82,0.46,0.18,0.16)]
save({"mediaId":396,"level":"A","keyWord":"hug","defaultVoice":"female",
 "taps":[
  {"phrase":"to hold a small gift","target":"the man","voice":"male","keys":keys(t,M)},
  {"phrase":"to run to the man","target":"the young woman","voice":"female","keys":keys(t,W)},
  {"phrase":"to walk on four legs","target":"the dog","voice":"female","keys":keys(t,D)}],
 "stillS":10.0,
 "nouns":[{"word":"windows","x":0.55,"y":0.10,"voice":"female"},{"word":"a hug","x":0.30,"y":0.56,"voice":"female"},
          {"word":"a dog","x":0.90,"y":0.55,"voice":"female"},{"word":"the floor","x":0.72,"y":0.90,"voice":"female"}],
 "question":"What are the man and woman doing?",
 "answer":["They","are","giving","each","other","a","hug."],"answerVoice":"female",
 "notes":"defaultVoice female: mixed pair, evenId true. 1.5 s is a blurred pan with a stranger in black (all off). An older woman walks in the background at 2.0-2.5, so the target is named 'the young woman'. From 3.5 the two hug and overlap: boxes split along the line between them, in the spin frames (5.0, 5.5, 6.5, 9.0-10.0) one of the two only gets the band with the head / the visible side, so parts of a body lie in no box or in the partner's box - verifier please look at 5.0, 5.5, 6.5, 9.0. 'a hug' (key word) is labelled on the hugging pair at 10.0. Dog: small in the background at 2.0-3.0, 6.5-7.0, 8.5-10.0; hidden or doubtful at 3.5 and 7.5 (off). Dog phrase is a little riddle-like but fits only the dog (people walk too)."})

# ---------- 397
M=[OFF]*7+[(0.0,0.10,0.53,0.67),(0.0,0.18,0.58,0.55),(0.0,0.08,1.0,0.92),(0.0,0.03,1.0,0.97)]+[OFF]*8+[(0.48,0.56,0.52,0.44),OFF]
W=[OFF]*7+[(0.53,0.12,0.47,0.62),(0.58,0.18,0.42,0.54),OFF,OFF,OFF,OFF,(0,0,1,1),(0,0,1,1),(0,0,1,1),OFF,OFF,OFF,(0.0,0.38,0.48,0.62),OFF]
S=[OFF]*11+[(0.20,0.36,0.50,0.24),(0.21,0.37,0.48,0.24),OFF,OFF,OFF,(0.22,0.27,0.42,0.34),(0.21,0.28,0.43,0.33),(0.23,0.40,0.43,0.31),(0.58,0.32,0.26,0.22),(0.62,0.33,0.24,0.21)]
save({"mediaId":397,"level":"B","keyWord":"hunting","defaultVoice":"male",
 "taps":[
  {"phrase":"to peer through binoculars","target":"the man","voice":"male","keys":keys(t,M)},
  {"phrase":"to wear a knitted beanie","target":"the woman","voice":"female","keys":keys(t,W)},
  {"phrase":"to graze among the trees","target":"the stag","voice":"male","keys":keys(t,S)}],
 "stillS":8.0,
 "nouns":[{"word":"tree trunks","x":0.55,"y":0.20,"voice":"male"},{"word":"a stag","x":0.38,"y":0.46,"voice":"male"},
          {"word":"fallen leaves","x":0.55,"y":0.66,"voice":"male"}],
 "question":"What are the man and woman doing?",
 "answer":["They","are","hunting","a","stag","in","the","forest."],"answerVoice":"male",
 "notes":"defaultVoice male: mixed pair, evenId false. 0.0-3.0 show only hands, boots and the dog (owner of hands/boots not identifiable): man and woman off there. The woman gets a state phrase: every action she does (crouching, staring) the man does too. The stag grazes (head down) only at 6.0; later it stands and walks. No weapon is shown; 'hunting' in the answer rests on the key word, camouflage, tracks and binoculars. 9.5: the man's head top (x>0.85, y 0.45-0.56) is outside his box because the stag box is next to it. Only 3 nouns: binoculars are not in the stag shot."})

# ---------- 398
B=[(0.30,0.06,0.70,0.94),(0.29,0.06,0.71,0.94),(0.29,0.08,0.71,0.92),(0.24,0.06,0.76,0.94),
   (0.17,0.22,0.83,0.78),(0.26,0.14,0.74,0.86),(0.26,0.15,0.74,0.85),(0.30,0.08,0.70,0.92),
   (0.23,0.08,0.77,0.92),(0.03,0.08,0.97,0.92),(0.12,0.12,0.88,0.88),(0.22,0.10,0.78,0.90),
   (0.10,0.08,0.90,0.92),(0.08,0.11,0.92,0.89),(0.12,0.13,0.88,0.87),(0.15,0.13,0.85,0.87),
   (0.14,0.14,0.86,0.86),(0.15,0.15,0.85,0.85),(0.05,0.15,0.95,0.85),(0.0,0.19,1.0,0.81),(0.0,0.22,1.0,0.78)]
kb=keys(t,B)
save({"mediaId":398,"level":"B","keyWord":"hygiene","defaultVoice":"male",
 "taps":[
  {"phrase":"to rinse out his mouth","target":"the boy","voice":"male","keys":kb},
  {"phrase":"to lather up his hands","target":"the boy","voice":"male","keys":kb},
  {"phrase":"to pat his face dry","target":"the boy","voice":"male","keys":kb}],
 "stillS":4.0,
 "nouns":[{"word":"a mirror","x":0.17,"y":0.31,"voice":"male"},{"word":"pyjamas","x":0.66,"y":0.50,"voice":"male"},
          {"word":"foam","x":0.40,"y":0.72,"voice":"male"},{"word":"a basin","x":0.26,"y":0.90,"voice":"male"}],
 "question":"What is the boy doing?",
 "answer":["He","is","lathering","his","hands","over","the","basin."],"answerVoice":"male",
 "notes":"Only one possible target (the boy; the second figure is his reflection in the wall mirror), used for all three phrases. Key word 'hygiene' is abstract: not a noun slot and not forced into the answer. The small round mirror is the labelled one (the big wall mirror behind it also shows his reflection). British spelling 'pyjamas'. 'to pat his face dry': he presses the towel to his face 6.5-7.5."})
