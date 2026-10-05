import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
b=[(0.18,0.31,0.55,0.49),(0.13,0.10,0.75,0.76),(0.11,0.16,0.79,0.75),(0.13,0.19,0.70,0.73),(0.11,0.18,0.76,0.73),(0.12,0.20,0.77,0.72)]
keys=[{"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]} for t,v in zip(T,b)]
taps=[{"phrase":p,"target":"the graduate","voice":"male","keys":keys} for p in ["to spring to his feet","to hold up a diploma","to punch the air"]]
c={"mediaId":7192,"level":"B","keyWord":"graduate","defaultVoice":"male","taps":taps,"stillS":1.7,
"nouns":[{"word":"a diploma","x":0.72,"y":0.23,"voice":"male"},{"word":"balloons","x":0.90,"y":0.44,"voice":"male"},
{"word":"a graduate","x":0.48,"y":0.52,"voice":"male"},{"word":"a podium","x":0.10,"y":0.65,"voice":"male"}],
"question":"What is the graduate doing?","answer":["He","is","holding","a","diploma","above","his","head."],"answerVoice":"male",
"notes":"Only one clear target (the jumping graduate); the crowd also cheers and claps and several caps lie on the lawn, so no unique phrase for them - all three phrases use the man. 'to spring to his feet' = crouch at 0.2 -> standing from 0.7. 'a graduate' (noun, male voice) is the man."}
json.dump(c,open('content/7192.json','w'),indent=1)
