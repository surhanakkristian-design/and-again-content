import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":round(r[2]-r[0],2),"h":round(r[3]-r[1],2)}) for t,r in zip(T,rows)]
man=K([(.18,.06,.80,.56),(.18,.05,.81,.58),(.17,.06,.80,.59),(.19,.05,.81,.64),(.28,0,.81,.64),(.28,.05,.81,.68),(.23,.03,.81,.74),(0,.03,.81,.77)])
farmer=K([(.81,.21,.99,.42),(.82,.22,1,.42),(.81,.23,.99,.43),(.82,.23,1,.44),(.82,.23,1,.44),(.82,.25,1,.46),(.82,.27,1,.47),(.82,.28,1,.49)])
c={"mediaId":7012,"level":"B","keyWord":"cylinder","defaultVoice":"male",
"taps":[{"phrase":"to balance on a hay bale","target":"the man in sunglasses","voice":"male","keys":man},
{"phrase":"to spread his arms wide","target":"the man in sunglasses","voice":"male","keys":man},
{"phrase":"to clutch his head","target":"the farmer","voice":"male","keys":farmer}],
"stillS":0.2,
"nouns":[{"word":"sunglasses","x":0.60,"y":0.14,"voice":"male"},{"word":"a farmer","x":0.86,"y":0.31,"voice":"male"},
{"word":"a sheepdog","x":0.88,"y":0.66,"voice":"male"},{"word":"a cylinder","x":0.45,"y":0.76,"voice":"male"}],
"question":"What is the man in sunglasses doing?",
"answer":["He","is","balancing","on","a","hay","bale."],"answerVoice":"male",
"notes":"Only two clear targets: the sheepdog runs, but so do the sheep near the bale, so no dog phrase fits only the dog; the young man takes two phrases. Man and farmer boxes are split by a vertical line at about x 0.81, so the man's outstretched right hand falls outside his box at most frames. The farmer is small and far away (min-width box). 'a cylinder' pill sits on the front face of the big bale; the row of bales on the left is also cylindrical, check whether that is confusing."}
json.dump(c,open('content/7012.json','w'),indent=1)
