import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
man=[(0,.18,.52,.82),(0,.18,.83,.82),(0,.25,.31,.75),(0,.24,.37,.76),(0,.22,.49,.78),(0,.30,.54,.70),(0,.35,.57,.65),(0,.36,.56,.64)]
wom=[None,None,(.31,.27,.30,.73),(.38,.25,.30,.75),(.50,.23,.42,.77),(.56,.26,.44,.74),(.59,.27,.41,.73),(.60,.29,.40,.71)]
d={"mediaId":5529,"level":"B","keyWord":"admission","defaultVoice":"male",
"taps":[{"phrase":"to unhook a velvet rope","target":"the doorman","voice":"male","keys":K(man)},
{"phrase":"to stride up the steps","target":"the woman","voice":"female","keys":K(wom)},
{"phrase":"to glance over her shoulder","target":"the woman","voice":"female","keys":K(wom)}],
"stillS":2.2,
"nouns":[{"word":"a neon sign","x":0.42,"y":0.08,"voice":"male"},
{"word":"a doorman","x":0.15,"y":0.42,"voice":"male"},
{"word":"a velvet rope","x":0.18,"y":0.78,"voice":"male"}],
"question":"What is the doorman doing?",
"answer":["He","is","unhooking","a","velvet","rope."],
"answerVoice":"male",
"notes":"Woman hidden behind the doorman at 0.2/0.7 (only bits of legs) -> off. From 1.2 the doorman's outstretched arm crosses in front of her; boxes split at the line between their bodies. 'stride up the steps' fits 1.7-3.7."}
json.dump(d,open("content/5529.json","w"),indent=1)
