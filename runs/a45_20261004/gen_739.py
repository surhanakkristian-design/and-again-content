import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [dict(t=t, **dict(zip("xywh", d[t]))) if t in d else dict(t=t, off=True) for t in T]
man={0:(.44,.41,.25,.30),.5:(.44,.39,.23,.29),1:(.43,.40,.24,.31),1.5:(.39,.40,.24,.31),
2:(0,.30,.39,.70),2.5:(0,.47,.90,.53),
4:(.02,.25,.83,.75),4.5:(0,.25,1,.75),5:(.02,.25,.76,.75),5.5:(0,.23,.85,.77),
6:(0,.23,.56,.77),6.5:(0,.20,.48,.80),7:(0,.25,.80,.75),7.5:(.02,.26,.74,.74),8:(0,.25,.70,.75),8.5:(0,.26,.66,.74),9:(.07,.28,.64,.72)}
sign={2:(.40,.17,.40,.28),2.5:(.30,.17,.60,.29),3:(0,.20,1,.63),3.5:(0,.20,1,.63)}
c={"mediaId":739,"level":"A","keyWord":"stop","defaultVoice":"male",
"taps":[
{"phrase":"to walk down the street","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to show the word stop","target":"the sign","voice":"male","keys":keys(sign)},
{"phrase":"to eat a slice of pizza","target":"the man","voice":"male","keys":keys(man)}],
"stillS":7.0,
"nouns":[{"word":"a man","x":.22,"y":.60,"voice":"male"},{"word":"an oven","x":.72,"y":.36,"voice":"male"},
{"word":"a pizza","x":.74,"y":.66,"voice":"male"},{"word":"a wheel","x":.58,"y":.93,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","eating","a","slice","of","pizza."],
"answerVoice":"male",
"notes":"Two targets only (man, stop sign); the seller is visible in one frame only. At 2.0 s the man's head touches the sign: split vertically at x 0.40; at 2.5 s the head overlaps the sign: split horizontally at y 0.47 (man box = body below the sign). 'to eat a slice of pizza' is 5 words after 'to'. Key word 'stop' (verb) appears in the sign phrase."}
json.dump(c,open("content/739.json","w"),indent=1)
