import json
T=[i*0.5 for i in range(9)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)})
    return out
G={0.0:(0,.44,.60,.86),0.5:(0,.45,.56,.87),1.0:(0,.42,.33,1),1.5:(0,.22,.56,1),2.0:(0,.20,.56,1),2.5:(0,.18,.62,1),3.0:(0,.17,.70,1),3.5:(0,.17,.77,1),4.0:(0,.15,.77,1)}
F={0.0:(.66,.48,1,.92),0.5:(.66,.47,1,.93),1.0:(.62,.42,1,1),1.5:(.57,.30,1,1),2.0:(.57,.28,1,.95),2.5:(.63,.28,1,.97),3.0:(.78,.30,1,1),3.5:(.82,.42,1,.92),4.0:(.82,.36,1,.94)}
L={0.0:(.22,0,.78,.27),0.5:(.22,0,.78,.27),1.0:(.17,0,.74,.24),1.5:(.08,0,.66,.14),2.0:(.08,0,.64,.14),2.5:(.16,0,.74,.14),3.0:(.42,0,.70,.14),3.5:None,4.0:None}
c={"mediaId":814,"level":"A","keyWord":"turn off","defaultVoice":"female",
"taps":[{"phrase":"to turn off the fan","target":"the girl","voice":"female","keys":keys(G)},
{"phrase":"to blow a pink ribbon","target":"the fan","voice":"female","keys":keys(F)},
{"phrase":"to hang from the roof","target":"the lamp","voice":"female","keys":keys(L)}],
"stillS":1.0,
"nouns":[{"word":"a lamp","x":.45,"y":.13,"voice":"female"},{"word":"a window","x":.45,"y":.36,"voice":"female"},
{"word":"a fan","x":.82,"y":.60,"voice":"female"},{"word":"a girl","x":.13,"y":.62,"voice":"female"}],
"question":"What is the girl doing?","answer":["She","is","turning off","the","fan."],"answerVoice":"female",
"notes":"At 0.0-0.5 only the girl's arm is in the picture (box on the arm). At 1.5-2.5 her hand reaches the fan's base, so her box is cut at the line between her body and the fan. The lamp leaves the top of the frame: only the bulb's lower edge at 3.0, off from 3.5. 'turning off' kept as one chip so 'turning the fan off' is not a second order. Still at 1.0 s is dark but all four things are visible; the girl is at the left edge."}
json.dump(c,open('content/814.json','w'),indent=1)
