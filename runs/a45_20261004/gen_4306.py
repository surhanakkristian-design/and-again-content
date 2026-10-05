import json
def K(rows):
    out=[]
    for r in rows:
        if len(r)==1: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
late=[(t/2,) for t in range(9,19)]
man=K([(0.0,),(0.5,0.35,0.39,0.38,0.61),(1.0,0.26,0.38,0.37,0.62),(1.5,0.18,0.37,0.46,0.63),(2.0,0.12,0.30,0.56,0.70),
(2.5,0.08,0.26,0.60,0.74),(3.0,0.03,0.28,0.57,0.72),(3.5,0.08,0.31,0.59,0.69),(4.0,0.10,0.27,0.51,0.73)]+late)
wom=K([(0.0,0.63,0.42,0.19,0.55),(0.5,),(1.0,0.64,0.43,0.18,0.26),(1.5,0.65,0.42,0.19,0.15),(2.0,0.69,0.42,0.28,0.38),
(2.5,0.69,0.39,0.31,0.42),(3.0,0.61,0.38,0.27,0.62),(3.5,0.68,0.42,0.26,0.58),(4.0,0.62,0.38,0.29,0.62)]+late)
d={"mediaId":4306,"level":"B","keyWord":"prison","defaultVoice":"male",
"taps":[{"phrase":"to carry a cardboard box","target":"the grey-bearded man","voice":"male","keys":man},
{"phrase":"to embrace the grey-bearded man","target":"the woman with long hair","voice":"female","keys":wom},
{"phrase":"to step through the gate","target":"the grey-bearded man","voice":"male","keys":man}],
"stillS":8.0,
"nouns":[{"word":"razor wire","x":0.28,"y":0.22,"voice":"male"},{"word":"a gate","x":0.72,"y":0.33,"voice":"male"},
{"word":"a crowd","x":0.45,"y":0.55,"voice":"male"},{"word":"asphalt","x":0.50,"y":0.88,"voice":"male"}],
"question":"What is the grey-bearded man carrying?","answer":["He","is","carrying","a","cardboard","box."],"answerVoice":"male",
"notes":"Key word 'prison' is not a single visible thing to label (only its gate), so it is not among the nouns. Only two targets: after 4.0 s everybody hugs, nothing fits one person only; the officer is too small to tap. The man and the woman overlap from 2.5 s (hug): boxes split along the line between their heads. 1.0-2.5 s: the cardboard box lies below the woman, so it is in neither box. Woman at 0.5 s hidden behind him (off). Both off from 4.5 s: the couple in the wide shots (man in a beige T-shirt, dark jeans) is another pair - the grey-bearded man wears khaki trousers. defaultVoice male = the main person (the released man)."}
json.dump(d,open("content/4306.json","w"),indent=1,ensure_ascii=False)
