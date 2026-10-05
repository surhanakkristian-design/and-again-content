import json
T=[i*0.5 for i in range(25)]
M={0.0:(.15,.20,.68,.80),0.5:(.15,.20,.66,.80),1.0:(.16,.21,.66,.79),1.5:(.17,.20,.64,.80),2.0:(.17,.20,.64,.80),2.5:(.17,.20,.66,.80),
3.0:(.17,.22,.68,.78),3.5:(.17,.22,.68,.78),4.0:(.17,.21,.71,.79)}
for t in T:
    if t>4.0 and t<10.0: M[t]=(.17,.21,.70,.79)
M.update({10.0:(.15,.20,.75,.80),10.5:(.12,.20,.80,.80),11.0:(.08,.19,.88,.81),11.5:(.04,.19,.94,.81),12.0:(.01,.17,.99,.83)})
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else {"t":t,"off":True} for t in T]
k=keys(M)
c={"mediaId":5189,"level":"A","keyWord":"weather","defaultVoice":"male",
"taps":[{"phrase":"to hold out his hand","target":"the old man","voice":"male","keys":k},
{"phrase":"to open a red umbrella","target":"the old man","voice":"male","keys":k},
{"phrase":"to smile at the camera","target":"the old man","voice":"male","keys":k}],
"stillS":6.0,
"nouns":[{"word":"a cap","x":0.52,"y":0.27,"voice":"male"},{"word":"an umbrella","x":0.74,"y":0.38,"voice":"male"},
{"word":"a coat","x":0.50,"y":0.72,"voice":"male"},{"word":"a street","x":0.15,"y":0.85,"voice":"male"}],
"question":"What is the old man holding?","answer":["He","is","holding","a","red","umbrella."],"answerVoice":"male",
"notes":"Only one usable target (background people are small, blurred and change); all three phrases on the old man. Key word 'weather' is abstract, not used as noun or in the answer. 'to hold out his hand' = 0.0-1.0, umbrella opens 1.5-3.0, he smiles at the camera from about 3.0 on."}
json.dump(c,open('content/5189.json','w'),indent=1)
