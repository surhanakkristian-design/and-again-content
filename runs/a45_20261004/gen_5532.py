import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
cos=[(.12,.30,.42,.60),(.12,.31,.47,.59),(.11,.30,.45,.59),(.08,.33,.47,.58),(.11,.29,.47,.61),(.11,.31,.46,.59),(.08,.31,.47,.58),(.06,.32,.48,.59)]
blu=[(.60,.36,.20,.52),(.59,.35,.28,.53),(.57,.36,.20,.53),(.56,.37,.23,.52),(.58,.37,.19,.52),(.57,.37,.20,.52),(.55,.37,.18,.52),(.54,.37,.18,.52)]
wom=[(.80,.37,.20,.61),(.87,.38,.13,.60),(.77,.33,.23,.67),(.79,.34,.21,.66),(.77,.35,.23,.64),(.77,.34,.23,.64),(.82,.34,.18,.62),(.72,.34,.28,.62)]
d={"mediaId":5532,"level":"B","keyWord":"advertising","defaultVoice":"male",
"taps":[{"phrase":"to jog on the spot","target":"the man in the costume","voice":"male","keys":K(cos)},
{"phrase":"to accept a hot dog","target":"the man in the blue shirt","voice":"male","keys":K(blu)},
{"phrase":"to hand over a hot dog","target":"the woman","voice":"female","keys":K(wom)}],
"stillS":3.2,
"nouns":[{"word":"the sky","x":0.84,"y":0.08,"voice":"male"},
{"word":"a fire escape","x":0.48,"y":0.22,"voice":"male"},
{"word":"a food cart","x":0.84,"y":0.32,"voice":"male"},
{"word":"a hot-dog costume","x":0.24,"y":0.62,"voice":"male"}],
"question":"What is the woman doing?",
"answer":["She","is","handing","the","man","a","hot","dog."],
"answerVoice":"female",
"notes":"Woman only a sliver at the right edge at 0.2/0.7 (box narrow at 0.7 to keep clear of the blue-shirt man). From 1.2 her arm reaches across the blue-shirt man; boxes split at his right side. Costume man's foam hand nearly touches the blue-shirt man at 2.2/3.2/3.7; split there."}
json.dump(d,open("content/5532.json","w"),indent=1)
