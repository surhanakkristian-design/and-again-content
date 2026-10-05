import json
T=[i*0.5 for i in range(31)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
M={3.5:(.48,.35,.52,.25),4.0:(.48,.33,.52,.27),4.5:(.48,.33,.52,.27),5.0:(.48,.35,.52,.25)}
W={3.5:(0,.36,.44,.24),4.0:(0,.34,.44,.26),4.5:(0,.34,.44,.26),5.0:(0,.36,.44,.24)}
for t in T:
    if 5.5<=t<=11.0:
        M[t]=(.40,.14,.60,.49); W[t]=(0,.15,.39,.82)
top={11.5:.33,12.0:.25,12.5:.20,13.0:.22,13.5:.24,14.0:.33,14.5:.36,15.0:.34}
for t,y in top.items():
    M[t]=(0,y,.50,round(1-y,2)); W[t]=(.51,y,.49,round(1-y,2))
d={"mediaId":4038,"level":"A","keyWord":"love","defaultVoice":"female",
"taps":[{"phrase":"to drive the car","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to hold out his hand","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to take his hand","target":"the woman","voice":"female","keys":K(W)}],
"stillS":4.0,
"nouns":[{"word":"a woman","x":.22,"y":.46,"voice":"female"},{"word":"a man","x":.74,"y":.41,"voice":"male"},
{"word":"a wheel","x":.74,"y":.55,"voice":"female"},{"word":"trees","x":.45,"y":.14,"voice":"female"}],
"question":"What are they doing in the car?",
"answer":["They","are","holding","hands","in","the","car."],"answerVoice":"female",
"notes":"0-3.0 s shows only the road and houses from the car: both targets off. Only two targets (man, woman), so two phrases share the man. It is the MAN who holds his hand out palm up (6.0-9.5 s) and the woman who lays hers on it (10.0 s) - the packet description has it the other way round. Side view 5.5-11.0 s: the two overlap, the woman's box is the left column (head, body), her legs on the right are in no box; the man's box is the upper right. Close-up 11.5-15.0 s: only the two arms with interlocked hands - man's bare arm left, woman's yellow sleeve right, split at x = 0.50 through the hands. defaultVoice: a couple, no single main person -> evenId -> female. 'a wheel' = the steering wheel in front of the man; dark still."}
json.dump(d,open("content/4038.json","w"),indent=1)
