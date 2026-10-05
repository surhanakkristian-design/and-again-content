import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x1,x2,y1,y2=b; out.append({"t":t,"x":x1,"y":y1,"w":round(x2-x1,2),"h":round(y2-y1,2)})
    return out
robin=K([(.21,.89,.20,.71),(.21,.93,.19,.73),(.19,.94,.19,.77),(.18,.97,.18,.79),(.17,.97,.15,.82),(.19,.99,.16,.84),(.18,.99,.16,.89),(.16,.99,.18,.92)])
ice=K([(.58,.98,.74,.93),(.58,.99,.78,.97),(.58,.99,.80,.99),(.59,.99,.82,.99),(.60,.99,.84,.99),(.62,.99,.85,.99),None,None])
c={"mediaId":6899,"level":"B","keyWord":"breast","defaultVoice":"male",
"taps":[{"phrase":"to perch on an icy railing","target":"the robin","voice":"male","keys":robin},
{"phrase":"to puff out its breast","target":"the robin","voice":"male","keys":robin},
{"phrase":"to hang beneath the railing","target":"the icicles","voice":"male","keys":ice}],
"stillS":0.2,
"nouns":[{"word":"a breast","x":0.33,"y":0.40,"voice":"male"},{"word":"a wing","x":0.70,"y":0.50,"voice":"male"},
{"word":"a railing","x":0.25,"y":0.73,"voice":"male"},{"word":"icicles","x":0.85,"y":0.81,"voice":"male"}],
"question":"What is the robin doing?",
"answer":["The","robin","is","perching","on","an","icy","railing."],
"answerVoice":"male",
"notes":"Only one animal; robin is target of two phrases, icicles the third (off at 3.2/3.7 when they leave the bottom edge). Key word noun given as 'a breast' (the bird's orange breast)."}
json.dump(c,open('content/6899.json','w'),indent=1)
