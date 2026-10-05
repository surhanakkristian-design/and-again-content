import json
T=[i*0.5 for i in range(24)]
def keys(bs): return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,bs)]
g=[(.16,.31,.92,.87),(.10,.30,.96,.87),(.02,.30,.95,.88),(0,.28,1.0,.89),(0,.28,1.0,.87),(0,.21,1.0,.87),(0,.20,1.0,.88),(.15,.29,.86,.71),
(.26,.42,.74,.73),(.27,.37,.78,.71),(.26,.37,.70,.72),(.18,.37,.79,.75),(.22,.36,.66,.79),(.21,.34,.90,.85),(0,.30,.88,.90),(.17,.28,.89,.90),
(.11,.24,.94,.88),(.06,.24,.97,.88),(0,.23,.99,.90),(0,.21,1.0,.90),(0,.17,1.0,.88),(0,.15,1.0,.90),(0,.15,1.0,.90),(0,.15,1.0,.90)]
c={"mediaId":4222,"level":"B","keyWord":"wave","defaultVoice":"female",
"taps":[
{"phrase":"to wave at the camera","target":"the gecko","voice":"female","keys":keys(g)},
{"phrase":"to fold its arms","target":"the gecko","voice":"female","keys":keys(g)},
{"phrase":"to lean towards the lens","target":"the gecko","voice":"female","keys":keys(g)}],
"stillS":6.5,
"nouns":[{"word":"eyes","x":0.45,"y":0.41,"voice":"female"},{"word":"a tongue","x":0.33,"y":0.51,"voice":"female"},{"word":"a belly","x":0.42,"y":0.62,"voice":"female"},{"word":"a tail","x":0.74,"y":0.71,"voice":"female"}],
"question":"What is the gecko doing?",
"answer":["It","is","waving","at","the","camera."],
"answerVoice":"female",
"notes":"Only one possible target (the gecko alone in a spotlight), so all three phrases share it and the same keys. The nouns are its body parts on the 6.5 s frame because nothing else is in the picture; 'eyes' sits between the two eyes. The waving is at 0.0-1.0 s only; the question does not say 'at first'."}
json.dump(c,open('content/4222.json','w'),indent=1)
