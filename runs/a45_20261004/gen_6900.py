import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x1,x2,y1,y2=b; out.append({"t":t,"x":x1,"y":y1,"w":round(x2-x1,2),"h":round(y2-y1,2)})
    return out
woman=K([(.11,.69,.21,.87),(.10,.71,.21,.87),(.08,.70,.21,.90),(.07,.72,.19,.90),(.06,.74,.17,.92),(.06,.63,.16,.92),(.04,.50,.16,.95),(.01,.49,.14,.95)])
man=K([(.72,1.0,.21,.63),(.73,1.0,.20,.63),(.73,1.0,.20,.64),(.74,1.0,.19,.64),(.82,1.0,.19,.64),(.76,1.0,.22,.64),(.72,1.0,.28,.64),(.71,1.0,.29,.64)])
c={"mediaId":6900,"level":"B","keyWord":"bring back","defaultVoice":"female",
"taps":[{"phrase":"to lower a heavy stone slab","target":"the young woman","voice":"female","keys":woman},
{"phrase":"to dust off her hands","target":"the young woman","voice":"female","keys":woman},
{"phrase":"to peer closely at the stone","target":"the man in the flat cap","voice":"male","keys":man}],
"stillS":3.2,
"nouns":[{"word":"a crowd","x":0.60,"y":0.25,"voice":"female"},{"word":"a flat cap","x":0.84,"y":0.34,"voice":"female"},
{"word":"a stone slab","x":0.60,"y":0.61,"voice":"female"},{"word":"gloves","x":0.42,"y":0.75,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","lowering","a","heavy","stone","slab."],
"answerVoice":"female",
"notes":"Lowering happens 0.2-2.0 s, hand-brushing 2.7-3.7 s. The man in the flat cap is at the right edge throughout (hands helping first, leans in from 2.7 s); several men in the crowd also wear caps but only he leans over the stone. Key word phrase not a noun."}
json.dump(c,open('content/6900.json','w'),indent=1)
