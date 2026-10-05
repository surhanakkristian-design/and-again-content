import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
woman=K([(.18,.38,.52,.57),(.28,.15,.50,.83),(.22,.30,.55,.68),(.03,.50,.85,.49),(.02,.48,.72,.50),(.02,.44,.70,.52),(.02,.44,.70,.50),(.02,.44,.70,.52)])
man=K([None,None,None,(.25,.30,.32,.19),(.24,.30,.32,.18),(.27,.30,.26,.14),(.28,.30,.26,.14),(.28,.30,.26,.14)])
d={"mediaId":7080,"level":"A","keyWord":"elevator","defaultVoice":"female",
"taps":[{"phrase":"to carry a big plant","target":"the woman","voice":"female","keys":woman},
{"phrase":"to leave the elevator","target":"the woman","voice":"female","keys":woman},
{"phrase":"to hold up his bag","target":"the man","voice":"male","keys":man}],
"stillS":3.7,
"nouns":[{"word":"a plant","x":0.13,"y":0.36,"voice":"female"},{"word":"an elevator","x":0.55,"y":0.31,"voice":"female"},
{"word":"a dog","x":0.63,"y":0.49,"voice":"female"},{"word":"stairs","x":0.87,"y":0.16,"voice":"female"}],
"question":"What is the woman carrying?","answer":["She","is","carrying","a","big","plant."],"answerVoice":"female",
"notes":"Man in suit hidden behind gate/plant at 0.2-1.2 (off). Woman's head overlaps man's chest at 2.7-3.7; split at the woman's hairline. Briefcase called 'bag' for level A."}
json.dump(d,open("content/7080.json","w"),indent=1)
