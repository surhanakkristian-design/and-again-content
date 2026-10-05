import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(bs): return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,bs)]
woman=[(.02,.49,.72,.92),(.03,.42,.80,.90),(.12,.41,.86,.93),(.04,.37,.86,.95),(.03,.35,.93,.92),(0,.31,1.0,.97),(0,.28,1.0,1.0),(0,.24,1.0,1.0)]
whale=[(.17,.34,.80,.49)]+[None]*7
c={"mediaId":7744,"level":"B","keyWord":"all of a sudden","defaultVoice":"female",
"taps":[
{"phrase":"to crash into the water","target":"the whale","voice":"female","keys":keys(whale)},
{"phrase":"to grip a paddle","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to gasp in shock","target":"the woman","voice":"female","keys":keys(woman)}],
"stillS":0.2,
"nouns":[{"word":"a whale","x":0.55,"y":0.40,"voice":"female"},{"word":"a boathouse","x":0.18,"y":0.48,"voice":"female"},{"word":"a paddle","x":0.76,"y":0.58,"voice":"female"},{"word":"a life jacket","x":0.38,"y":0.74,"voice":"female"}],
"question":"What is the whale doing?",
"answer":["It","is","crashing","into","the","water."],
"answerVoice":"female",
"notes":"WEAK SPOT: the whale itself is visible only in the first frame (0.2 s); from 0.7 s on there is only the white splash, so its tap region is off there - the tap window for phrase 1 is short. Whale and the woman's hat touch at 0.2: boxes split at y 0.49. Still frame is 0.2 because it is the only frame with the whale; the boathouse is small."}
json.dump(c,open('content/7744.json','w'),indent=1)
