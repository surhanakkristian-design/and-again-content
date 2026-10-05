import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(zip(("t","x","y","w","h"),(t,)+d[t]))) for t in T]
W={0.0:(0.0,0.53,0.62,0.47),0.5:(0.0,0.53,0.62,0.47),1.0:(0.0,0.53,0.62,0.47),1.5:(0.0,0.53,0.62,0.47),
 2.0:(0.0,0.38,0.64,0.62),2.5:(0.01,0.38,0.68,0.62),3.0:(0.0,0.38,0.60,0.62),3.5:(0.0,0.38,0.74,0.62),
 4.0:(0.0,0.39,0.71,0.61),4.5:(0.0,0.40,0.82,0.60),5.0:(0.0,0.40,0.81,0.60),5.5:(0.0,0.42,0.82,0.58),
 6.0:(0.0,0.41,0.77,0.59),6.5:(0.0,0.41,0.83,0.59),7.0:(0.0,0.41,0.81,0.59),7.5:(0.0,0.41,0.81,0.59),
 8.0:(0.0,0.40,0.56,0.60),8.5:(0.0,0.36,0.64,0.64),9.0:(0.0,0.40,0.49,0.60),9.5:(0.0,0.44,0.62,0.56),
 10.0:(0.0,0.44,0.50,0.56),10.5:(0.0,0.47,0.62,0.53),11.0:(0.02,0.47,0.62,0.53),11.5:(0.05,0.47,0.62,0.53),
 12.0:(0.03,0.46,0.61,0.54)}
F={3.5:(0.76,0.14,0.24,0.86),4.0:(0.71,0.12,0.29,0.88),4.5:(0.55,0.08,0.45,0.32),5.0:(0.40,0.12,0.60,0.28),
 5.5:(0.52,0.12,0.48,0.30),6.0:(0.50,0.15,0.50,0.26),6.5:(0.55,0.15,0.45,0.26),7.0:(0.50,0.15,0.50,0.26),
 7.5:(0.52,0.15,0.48,0.26),8.0:(0.56,0.0,0.34,0.56),8.5:(0.42,0.02,0.36,0.34),9.0:(0.35,0.04,0.33,0.36),
 9.5:(0.36,0.09,0.30,0.35),10.0:(0.36,0.12,0.31,0.32),10.5:(0.36,0.09,0.32,0.38),11.0:(0.34,0.06,0.33,0.41),
 11.5:(0.35,0.05,0.33,0.42),12.0:(0.34,0.02,0.34,0.44)}
c={"mediaId":5173,"level":"A","keyWord":"raincoat","defaultVoice":"female",
"taps":[{"phrase":"to fill a bottle","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to touch the water","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to fall from the rocks","target":"the waterfall","voice":"female","keys":keys(F)}],
"stillS":10.0,
"nouns":[{"word":"a waterfall","x":0.52,"y":0.25,"voice":"female"},{"word":"a backpack","x":0.10,"y":0.66,"voice":"female"},
{"word":"a raincoat","x":0.30,"y":0.85,"voice":"female"},{"word":"rocks","x":0.84,"y":0.84,"voice":"female"}],
"question":"What is the woman wearing?",
"answer":["She","is","wearing","a","red","raincoat."],"answerVoice":"female",
"notes":"One person (selfie clip), so two phrases use the woman: she fills the metal bottle 0-1.5 s (only her red-sleeved arm is visible, boxed) and holds her hand in the falling water 4.5-7.5 s. Third target = the waterfall (small waterfall 3.5-7.5 s, big waterfall 8-12 s; the thin side fall at the left of the big shot is not boxed). While her hand is in the water (4.0-7.5 s) the two boxes are split: the waterfall box is the part above / beside her so the boxes never overlap. The thin trickle at 0-1.5 s is not counted as the waterfall (off). Answer uses the key word; 'wearing' is a state but it is true in every shot."}
json.dump(c,open('content/5173.json','w'),indent=1)
