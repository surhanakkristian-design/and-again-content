import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
woman=K([(0,.04,.43,.54),(0,.17,.47,.49),(0,.31,.50,.41),(0,.38,.50,.42),(0,.42,.50,.38),(0,.39,.49,.33),(0,.37,.49,.35),(0,.36,.44,.37)])
ball=K([(.43,0,.22,.18),(.47,0,.25,.27),(.2,0,.7,.31),(.08,0,.92,.38),(0,0,1,.42),(0,0,1,.39),(0,0,1,.37),(0,0,1,.36)])
c={"mediaId":6965,"level":"B","keyWord":"come down","defaultVoice":"female",
"taps":[{"phrase":"to touch the still water","target":"the woman","voice":"female","keys":woman},
{"phrase":"to lean out of a basket","target":"the woman","voice":"female","keys":woman},
{"phrase":"to descend towards the lake","target":"the hot-air balloon","voice":"female","keys":ball}],
"stillS":3.7,
"nouns":[{"word":"a hot-air balloon","x":0.5,"y":0.12,"voice":"female"},{"word":"pine trees","x":0.85,"y":0.52,"voice":"female"},
{"word":"a lake","x":0.72,"y":0.72,"voice":"female"},{"word":"grass","x":0.75,"y":0.94,"voice":"female"}],
"question":"What is the hot-air balloon doing?","answer":["It","is","coming","down","over","the","lake."],"answerVoice":"female",
"notes":"Camera tilts up while the balloon sinks. From 1.2 s the balloon basket and the woman's head are at the same height: boxes split along a horizontal line at her head, so the bottom of the balloon basket is cut off at 1.7-3.7 (envelope fully inside). 0.2/0.7 split vertically next to her head. The woman's foreground basket is part of her box. 'the lake' noun pill on the reflection area right of her arm."}
json.dump(c,open('content/6965.json','w'),indent=1)
