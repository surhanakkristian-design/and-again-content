import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
wom=K([(.33,.55,.74,.82),(.29,.58,.81,.81),(.40,.53,.86,.84),(.48,.53,.88,.89),(.44,.59,.92,.87),(.33,.54,.86,.89),(.30,.60,.82,.96),(.17,.57,.82,.99)])
yel=K([(.21,.40,.40,.54),(.24,.42,.42,.56),(.26,.38,.44,.52),(.31,.37,.49,.51),(.35,.36,.53,.50),(.40,.34,.58,.48),(.44,.32,.62,.46),(.48,.31,.66,.45)])
c={"mediaId":7395,"level":"B","keyWord":"opening","defaultVoice":"female",
"taps":[{"phrase":"to paddle a red kayak","target":"the woman","voice":"female","keys":wom},
{"phrase":"to float in the distance","target":"the kayaker in yellow","voice":"female","keys":yel},
{"phrase":"to burst through the opening","target":"the woman","voice":"female","keys":wom}],
"stillS":2.2,
"nouns":[{"word":"an opening","x":0.47,"y":0.18,"voice":"female"},{"word":"a lighthouse","x":0.52,"y":0.31,"voice":"female"},
{"word":"a helmet","x":0.62,"y":0.64,"voice":"female"},{"word":"foam","x":0.40,"y":0.82,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","paddling","through","a","narrow","opening."],
"answerVoice":"female",
"notes":"Seals avoided as targets/nouns: there are two groups (left and right) doing the same. 'a kayak' avoided as a noun (two kayaks). Yellow kayaker is tiny: minimum-size box above the woman's box. 'an opening' pill sits in the bright gap between the cliffs; lighthouse is tiny."}
json.dump(c,open('content/7395.json','w'),indent=1)
