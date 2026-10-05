import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man=K([(0.13,0.25,0.57,0.57),(0.20,0.28,0.53,0.55),(0.17,0.22,0.55,0.60),(0.11,0.22,0.60,0.62),
       (0.08,0.22,0.62,0.60),(0.06,0.20,0.64,0.62),(0.02,0.19,0.64,0.63),(0.00,0.16,0.66,0.66)])
wom=K([None,None,None,(0.82,0.19,0.18,0.34),(0.76,0.28,0.24,0.45),(0.72,0.30,0.28,0.42),(0.67,0.32,0.33,0.45),(0.67,0.32,0.33,0.45)])
d={"mediaId":7847,"level":"B","keyWord":"geology","defaultVoice":"male",
"taps":[{"phrase":"to split a stone open","target":"the young man","voice":"male","keys":man},
{"phrase":"to uncover a fossil","target":"the young man","voice":"male","keys":man},
{"phrase":"to peer through a magnifier","target":"the woman in yellow","voice":"female","keys":wom}],
"stillS":3.2,
"nouns":[{"word":"a cliff","x":0.50,"y":0.10,"voice":"male"},{"word":"a magnifier","x":0.72,"y":0.50,"voice":"male"},
{"word":"a fossil","x":0.55,"y":0.65,"voice":"male"},{"word":"a clipboard","x":0.86,"y":0.85,"voice":"male"}],
"question":"What is the young man doing?",
"answer":["He","is","splitting","a","stone","with","a","hammer."],
"answerVoice":"male",
"notes":"Only two clear targets (background pair both measure the cliff, so not usable alone). Woman enters at 1.7 s at the right edge. 'geology' is not a visible noun."}
json.dump(d,open("content/7847.json","w"),indent=1)
