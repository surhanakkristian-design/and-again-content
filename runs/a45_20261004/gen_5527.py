import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
woman=K([(.40,.30,.25,.33),(.41,.30,.25,.33),(.40,.30,.25,.33),(.40,.29,.26,.35),(.39,.28,.27,.37),(.45,.28,.21,.39),(.48,.28,.18,.45),(.48,.29,.18,.49)])
rooster=K([(.45,.64,.20,.17),(.43,.63,.22,.17),(.44,.64,.21,.18),(.44,.65,.21,.19),(.43,.66,.22,.14),(.38,.68,.27,.14),(.19,.74,.35,.20),(.03,.73,.38,.19)])
hand=K([(.67,.41,.33,.59)]*5+[(.67,.52,.33,.48),None,None])
d={"mediaId":5527,"level":"A","keyWord":"address","defaultVoice":"female",
"taps":[{"phrase":"to take a parcel","target":"the woman","voice":"female","keys":woman},
{"phrase":"to walk across the street","target":"the rooster","voice":"female","keys":rooster},
{"phrase":"to knock on the door","target":"the hand on the right","voice":"female","keys":hand}],
"stillS":3.7,
"nouns":[{"word":"a lamp","x":0.52,"y":0.15,"voice":"female"},{"word":"a door","x":0.86,"y":0.40,"voice":"female"},
{"word":"a bench","x":0.14,"y":0.58,"voice":"female"},{"word":"a rooster","x":0.22,"y":0.82,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","holding","a","parcel."],"answerVoice":"female",
"notes":"key word 'address' is not visible (no address label shown). Knocking hand leaves the frame after 2.7 s. Rooster stands by the door first and crosses left from 3.2 s."}
json.dump(d,open("content/5527.json","w"),indent=1)
