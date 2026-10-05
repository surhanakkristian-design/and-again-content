import json
def K(rows):
    out=[]
    for r in rows:
        if len(r)==1: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
cut=[(4.0,),(4.5,),(5.0,),(5.5,),(6.0,)]
P=K([(0.0,0,0.15,0.72,0.85),(0.5,0,0.15,0.73,0.85),(1.0,0,0.15,0.70,0.85),(1.5,0,0.15,0.66,0.85),(2.0,0,0.14,0.64,0.86),
(2.5,0,0.14,0.58,0.86),(3.0,0,0.17,0.55,0.83),(3.5,0,0.14,0.43,0.86)]+cut+[(6.5,0,0.20,0.66,0.80),(7.0,0,0.20,0.70,0.80),
(7.5,0,0.20,0.72,0.80),(8.0,0,0.20,0.70,0.80),(8.5,0,0.20,0.72,0.80),(9.0,0,0.20,0.72,0.80),(9.5,0,0.20,0.74,0.80),
(10.0,0,0.20,0.72,0.80),(10.5,0,0.20,0.74,0.80),(11.0,0,0.20,0.72,0.80),(11.5,0,0.20,0.74,0.80),(12.0,0,0.20,0.74,0.80)])
F=K([(0.0,0.73,0.17,0.19,0.19),(0.5,0.74,0.15,0.18,0.19),(1.0,0.71,0.15,0.18,0.19),(1.5,0.68,0.14,0.18,0.19),(2.0,0.66,0.11,0.18,0.19),
(2.5,0.60,0.10,0.18,0.19),(3.0,0.56,0.09,0.18,0.19),(3.5,0.44,0.09,0.18,0.19)]+cut+[(6.5,0.61,0.02,0.18,0.17),(7.0,0.61,0.03,0.18,0.16),
(7.5,0.61,0.03,0.18,0.16),(8.0,0.61,0.02,0.18,0.17),(8.5,0.63,0.02,0.18,0.17),(9.0,0.66,0.02,0.18,0.17),(9.5,0.68,0.02,0.18,0.17),
(10.0,0.66,0.01,0.18,0.16),(10.5,0.66,0.0,0.18,0.16),(11.0,0.65,0.01,0.18,0.17),(11.5,0.66,0.01,0.18,0.17),(12.0,0.67,0.0,0.18,0.17)])
C=K([(t/2,) for t in range(0,8)]+[(4.0,0,0.15,1,0.80),(4.5,0,0.08,1,0.82),(5.0,0,0.10,1,0.90),(5.5,0,0.08,1,0.92),(6.0,0,0.02,1,0.96)]+[(t/2,) for t in range(13,25)])
d={"mediaId":4309,"level":"B","keyWord":"anthem","defaultVoice":"female",
"taps":[{"phrase":"to sing through her tears","target":"the blonde player","voice":"female","keys":P},
{"phrase":"to flutter on a flagpole","target":"the flag","voice":"female","keys":F},
{"phrase":"to pack the stands","target":"the crowd","voice":"female","keys":C}],
"stillS":8.0,
"nouns":[{"word":"a flag","x":0.70,"y":0.11,"voice":"female"},{"word":"a flagpole","x":0.76,"y":0.42,"voice":"female"},
{"word":"a braid","x":0.16,"y":0.62,"voice":"female"},{"word":"a jersey","x":0.25,"y":0.84,"voice":"female"}],
"question":"What is the blonde player doing?","answer":["She","is","singing","through","her","tears."],"answerVoice":"female",
"notes":"Key word 'anthem' is not a visible thing, so not a noun and not in the answer (it would need the sound). The crowd is boxed only in the stand shots (4.0-6.0 s); in the close-ups it is an out-of-focus background behind the players, left off. The player's box stops left of the flag / the team-mates, so the right edge of her shirt is outside. The team-mates also sing with a hand on the chest, so no phrase uses that. 'a flag' and 'a flagpole' are two slots on one mast (cloth at the top, pole in the middle) - drop 'a flagpole' if that is too close."}
json.dump(d,open("content/4309.json","w"),indent=1,ensure_ascii=False)
