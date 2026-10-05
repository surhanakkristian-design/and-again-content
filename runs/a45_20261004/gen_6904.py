import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
woman=K([(0.46,0.22,0.44,0.52),(0.46,0.22,0.44,0.52),(0.46,0.21,0.44,0.53),(0.46,0.21,0.47,0.53),
         (0.44,0.20,0.48,0.54),(0.34,0.30,0.64,0.44),(0.41,0.27,0.55,0.47),(0.40,0.26,0.57,0.48)])
man=K([(0.08,0.55,0.37,0.21),(0.08,0.55,0.37,0.21),(0.07,0.55,0.38,0.22),(0.07,0.55,0.38,0.22),
       (0.08,0.52,0.35,0.24),(0.08,0.52,0.25,0.25),(0.10,0.47,0.30,0.30),(0.10,0.47,0.29,0.30)])
cook=K([(0.13,0.35,0.24,0.19),(0.13,0.35,0.24,0.19),(0.12,0.36,0.22,0.18),(0.12,0.36,0.24,0.18),
        (0.12,0.32,0.20,0.19),(0.12,0.31,0.21,0.20),(0.09,0.32,0.21,0.14),(0.07,0.32,0.21,0.14)])
d={"mediaId":6904,"level":"B","keyWord":"bring to","defaultVoice":"female",
 "taps":[{"phrase":"to wrinkle her nose","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to sprawl across a table","target":"the man","voice":"male","keys":man},
         {"phrase":"to clutch a tea towel","target":"the cook","voice":"male","keys":cook}],
 "stillS":0.2,
 "nouns":[{"word":"a cherry pie","x":0.22,"y":0.82,"voice":"female"},
          {"word":"a jug","x":0.76,"y":0.86,"voice":"female"},
          {"word":"bunting","x":0.28,"y":0.19,"voice":"female"},
          {"word":"a piano","x":0.86,"y":0.40,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","holding","a","pie","under","his","nose."],
 "answerVoice":"female",
 "notes":"Woman and man overlap (her hands rest on him): split vertically at about x 0.45 (0.33-0.41 late), so her arm with the pie box lies partly in the man's box and his chest partly in hers. Cook kneels behind, box kept above the man's. 'wrinkle her nose' holds 0.2-2.2 s, then she smiles."}
json.dump(d,open("content/6904.json","w"),indent=1)
