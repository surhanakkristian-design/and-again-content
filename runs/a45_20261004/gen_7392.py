import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
man=K([(.40,.17,.86,.55),(.38,.19,.87,.55),(.37,.22,.88,.57),(.38,.24,.91,.57),(.38,.28,.92,.60),(.38,.35,.98,.61),(.38,.35,.94,.70),(.38,.22,.98,.68)])
cat=K([(.43,.56,.94,.82),(.43,.56,.96,.82),(.43,.58,.94,.86),(.43,.58,.94,.86),(.47,.61,.96,.80),(.45,.62,.92,.81),(.56,.71,.94,.94),None])
tin=K([(.12,.66,.33,.80),(.12,.65,.33,.79),(.12,.64,.33,.78),(.12,.63,.33,.77),(.12,.62,.33,.76),(.12,.61,.33,.75),(.12,.60,.33,.74),(.12,.60,.33,.74)])
c={"mediaId":7392,"level":"B","keyWord":"oil","defaultVoice":"male",
"taps":[{"phrase":"to oil a wooden table","target":"the man in front","voice":"male","keys":man},
{"phrase":"to stroll across the table","target":"the cat","voice":"male","keys":cat},
{"phrase":"to stand in a puddle","target":"the tin","voice":"male","keys":tin}],
"stillS":0.7,
"nouns":[{"word":"a tin","x":0.22,"y":0.72,"voice":"male"},{"word":"gloves","x":0.23,"y":0.86,"voice":"male"},
{"word":"a cat","x":0.68,"y":0.70,"voice":"male"},{"word":"a chair","x":0.78,"y":0.10,"voice":"male"}],
"question":"What is the man in front doing?",
"answer":["He","is","oiling","a","long","wooden","table."],
"answerVoice":"male",
"notes":"Two men: the target is the man at the front in the apron; the man at the back is only partly visible behind the chair. The cat walks, crouches and slides off the edge at 3.2, gone at 3.7 (only a sliver bottom-right). Man/cat boxes split on y where hands and tail meet (2.7, 3.2)."}
json.dump(c,open('content/7392.json','w'),indent=1)
