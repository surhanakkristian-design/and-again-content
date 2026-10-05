import json
H={0.0:(.68,0,.32,.92),0.5:(.30,0,.70,.90),1.0:(.22,0,.78,.98),1.5:(.18,0,.82,.92),2.0:(.28,0,.72,.90),
2.5:(.50,0,.50,.74),3.0:(.30,0,.70,.84),3.5:(.36,0,.64,.75),4.0:(.34,0,.66,.63),4.5:(.48,0,.52,.76),
5.0:(.55,0,.45,.68),5.5:(.48,0,.52,.72),6.0:(.66,.23,.34,.45),6.5:(.68,.48,.32,.23),7.0:(.60,.52,.40,.45),7.5:(.72,.53,.28,.47)}
P={6.5:(0,.48,.30,.20),7.0:(.02,.48,.55,.52),7.5:(.05,.47,.65,.53),8.0:(.10,.50,.55,.50),8.5:(.20,.55,.55,.45),9.0:(.25,.62,.45,.38)}
T=[i*0.5 for i in range(19)]
def ks(D): return [({"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} if t in D else {"t":t,"off":True}) for t in T]
hk=ks(H); pk=ks(P)
c={"mediaId":4887,"level":"B","keyWord":"narrow","defaultVoice":"male",
"taps":[{"phrase":"to clamber down the rocks","target":"the hiker","voice":"male","keys":hk},
{"phrase":"to grin at the camera","target":"the hiker","voice":"male","keys":hk},
{"phrase":"to descend into the gorge","target":"the narrow path","voice":"male","keys":pk}],
"stillS":8.0,
"nouns":[{"word":"cliffs","x":0.25,"y":0.2,"voice":"male"},{"word":"the sky","x":0.8,"y":0.1,"voice":"male"},
{"word":"a path","x":0.38,"y":0.62,"voice":"male"},{"word":"a boulder","x":0.15,"y":0.74,"voice":"male"}],
"question":"What is the hiker doing?","answer":["He","is","climbing","down","a","narrow","path."],"answerVoice":"male",
"notes":"Hiker is seen only partly (head/torso from above, legs and boots), OFF from 8.0 s. The narrow path is boxed only 6.5-9.0 s where its stone steps are clearly visible ahead; before that the camera looks at his boots on rocky ground. Grin: 0.5-2.0 s he smiles down at the camera."}
json.dump(c,open('content/4887.json','w'),indent=1)
