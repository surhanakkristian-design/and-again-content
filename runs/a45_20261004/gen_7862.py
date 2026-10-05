import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
w=[(.24,.26,.48,.74),(.21,.26,.51,.74),(.17,.26,.53,.74),(.28,.24,.43,.76),(.16,.25,.58,.75),(.19,.25,.56,.75)]
k=[{"t":t,"x":a,"y":b,"w":c,"h":d} for t,(a,b,c,d) in zip(T,w)]
c={"mediaId":7862,"level":"A","keyWord":"have a problem","defaultVoice":"female",
"taps":[{"phrase":"to take a selfie","target":"the woman","voice":"female","keys":k},
{"phrase":"to touch her hair","target":"the woman","voice":"female","keys":k},
{"phrase":"to wear a silver dress","target":"the woman","voice":"female","keys":k}],
"stillS":2.2,
"nouns":[{"word":"a phone","x":0.62,"y":0.37,"voice":"female"},{"word":"a curtain","x":0.80,"y":0.55,"voice":"female"},
{"word":"a bag","x":0.24,"y":0.67,"voice":"female"},{"word":"shoes","x":0.23,"y":0.90,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","taking","a","selfie","with","her","phone."],"answerVoice":"female",
"notes":"Only one person in the clip, so all three phrases target the woman. 'to touch her hair' happens around 1.7 s only. 'shoes' = the pair of sandals on the floor."}
json.dump(c,open('content/7862.json','w'),indent=1)
