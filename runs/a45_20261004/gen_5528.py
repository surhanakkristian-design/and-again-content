import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
wy=[.26,.25,.25,.24,.24,.23,.23,.22]; ww=[.46,.47,.47,.50,.49,.50,.49,.44]
my=[.21,.21,.21,.21,.20,.19,.17,.17]; mx=[.47,.48,.48,.51,.50,.51,.50,.45]
woman=K([(0.0,y,w,1-y) for y,w in zip(wy,ww)])
man=K([(x,y,round(1-x,2),round(1-y,2)) for x,y in zip(mx,my)])
woman=K([(0.0,y,w,round(1-y,2)) for y,w in zip(wy,ww)])
d={"mediaId":5528,"level":"B","keyWord":"adjacent","defaultVoice":"female",
"taps":[{"phrase":"to sit by the window","target":"the woman","voice":"female","keys":woman},
{"phrase":"to cross her legs","target":"the woman","voice":"female","keys":woman},
{"phrase":"to hold a champagne flute","target":"the man","voice":"male","keys":man}],
"stillS":0.2,
"nouns":[{"word":"a window","x":0.12,"y":0.27,"voice":"female"},{"word":"a lamp","x":0.54,"y":0.34,"voice":"female"},
{"word":"a champagne flute","x":0.80,"y":0.58,"voice":"female"},{"word":"an armrest","x":0.40,"y":0.70,"voice":"female"}],
"question":"Where are the two passengers sitting?","answer":["They","are","sitting","in","adjacent","seats."],"answerVoice":"female",
"notes":"only two targets; boxes split on the line between the two seats (man's legs at x<.47 and his raised hand at 3.7 s reaching over to x .37 are partly outside his box). Both laugh, so no laughing phrase. Woman's phrases are states/positions because both people do the same actions."}
json.dump(d,open("content/5528.json","w"),indent=1)
