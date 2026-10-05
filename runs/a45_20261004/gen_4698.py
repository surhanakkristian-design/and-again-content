import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0.28,0,0.72,0.60),0.5:(0.25,0,0.75,0.62),1.0:(0.30,0,0.70,0.78),1.5:(0.36,0,0.64,0.78),2.0:(0.36,0,0.64,0.66),
2.5:(0.30,0.15,0.68,0.50),3.0:(0.28,0.17,0.66,0.60),3.5:(0.28,0.17,0.66,0.60),4.0:(0.42,0.11,0.54,0.48),
6.5:(0.08,0.14,0.32,0.27),7.0:(0.08,0.14,0.32,0.27),7.5:(0.08,0.14,0.32,0.27),
8.0:(0,0.17,0.39,0.24),8.5:(0,0.19,0.39,0.24),9.0:(0,0.19,0.34,0.25)}
bon={4.0:(0,0,0.41,0.42),4.5:(0,0,0.97,0.28),5.0:(0,0,1,0.31),5.5:(0,0,1,0.30),6.0:(0,0,1,0.30)}
mot={6.5:(0.19,0.42,0.81,0.32),7.0:(0.17,0.42,0.83,0.32),7.5:(0.19,0.42,0.81,0.32),
8.0:(0.19,0.42,0.81,0.32),8.5:(0.20,0.44,0.80,0.30),9.0:(0.20,0.45,0.80,0.29)}
j={"mediaId":4698,"level":"B","keyWord":"motor","defaultVoice":"male",
"taps":[
{"phrase":"to clutch his head","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to stay propped open","target":"the car bonnet","voice":"male","keys":keys(bon)},
{"phrase":"to gleam in the sunshine","target":"the huge motor","voice":"male","keys":keys(mot)}],
"stillS":3.5,
"nouns":[{"word":"shelves","x":0.30,"y":0.20,"voice":"male"},{"word":"a headlight","x":0.16,"y":0.37,"voice":"male"},
{"word":"overalls","x":0.72,"y":0.48,"voice":"male"},{"word":"a motor","x":0.45,"y":0.70,"voice":"male"}],
"question":"What is the man working on?",
"answer":["He","is","working","on","a","scooter","motor."],
"answerVoice":"male",
"notes":"Three shots: scooter in the workshop (0-3.5), open car bonnet (4.0-6.0, man visible only at 4.0), huge V8 on a stand outside (6.5-9.0). He clutches his head only from 8.0. In the last shot man and motor overlap (he leans on it / stands beside it): split along y - the man's box is head, arms and chest, the motor box is the engine block below; the chrome air scoop on top (right of his head) and his legs are in neither box. At 4.0 the bonnet box is only its big panel left of the man. 'the huge motor' is named so to tell it from the scooter and car motors, which are not targets."}
json.dump(j,open("content/4698.json","w"),indent=1)
