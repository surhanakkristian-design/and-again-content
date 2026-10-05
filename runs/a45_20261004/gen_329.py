import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
M={0.0:(0,0,0.54,0.48),0.5:(0,0,0.54,0.48),1.0:(0,0,0.54,0.56),1.5:(0,0,0.58,0.47),2.0:(0.03,0,0.52,0.50),2.5:(0,0,0.50,0.47),
3.0:(0,0,0.48,0.50),3.5:(0,0,0.50,0.42),4.0:(0,0,0.50,0.38),4.5:(0,0,0.48,0.38),5.0:(0,0,0.47,0.48),5.5:(0,0,0.54,0.42),
6.0:(0,0,0.52,0.42),6.5:(0,0,0.63,0.42),7.0:(0,0,0.56,0.52),7.5:(0,0,0.56,0.52),8.0:(0,0,0.40,0.50),8.5:(0,0,0.42,0.50),
9.0:(0,0,0.40,0.58),9.5:(0,0,0.25,0.62),10.0:(0,0,0.24,0.52)}
W={0.0:(0.54,0,0.46,0.56),0.5:(0.54,0,0.46,0.56),1.0:(0.54,0,0.46,0.60),1.5:(0.58,0,0.42,0.60),2.0:(0.55,0,0.45,0.58),2.5:(0.50,0,0.50,0.52),
3.0:(0.48,0,0.52,0.60),3.5:(0.50,0,0.50,0.48),4.0:(0.50,0,0.50,0.46),4.5:(0.48,0,0.52,0.47),5.0:(0.47,0,0.53,0.58),5.5:(0.56,0,0.44,0.52),
6.0:(0.60,0,0.40,0.52),6.5:(0.66,0,0.34,0.52),7.0:(0.66,0,0.34,0.66),7.5:(0.70,0,0.30,0.68),8.0:(0.50,0,0.50,0.50),8.5:(0.50,0,0.50,0.50),
9.0:(0.50,0,0.50,0.60),9.5:(0.30,0,0.70,0.70),10.0:(0.32,0,0.68,0.48)}
d={"mediaId":329,"level":"A","keyWord":"gas","defaultVoice":"male",
"taps":[{"phrase":"to hold a white kettle","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to turn on the gas","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to pour oil into the pan","target":"the man","voice":"male","keys":keys(M)}],
"stillS":7.5,
"nouns":[{"word":"a woman","x":0.84,"y":0.22,"voice":"female"},{"word":"a pot","x":0.12,"y":0.44,"voice":"male"},
{"word":"a kettle","x":0.53,"y":0.49,"voice":"male"},{"word":"fire","x":0.50,"y":0.61,"voice":"male"}],
"question":"What is the man holding?","answer":["He","is","holding","a","white","kettle."],"answerVoice":"male",
"notes":"Only two usable targets (man, woman): the cat sits between the woman's arm and body in many frames, so it cannot get a box that does not overlap hers; it is not a target. Key word gas is not a visible thing: it is in phrase 2 (she turns the knob, the flame lights); the blue flame is labelled 'fire', not 'gas'. No 'turn on the gas' answer because the chips would allow two word orders. Man and woman stand close; boxes split between them, her left hand is slightly cut in a few frames."}
json.dump(d,open("content/329.json","w"),indent=1)
