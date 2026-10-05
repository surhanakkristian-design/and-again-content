import json
T=[i*0.5 for i in range(31)]
def mk(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
van={0.0:(0,0,1,.80),0.5:(0,0,1,.52),1.0:(0,0,1,.26),1.5:(0,0,1,.21),2.0:(0,0,1,.22),2.5:(0,0,1,.24),3.0:(0,0,1,.21),
3.5:(.48,.44,.39,.20),4.0:(.31,.45,.56,.23),4.5:(.20,.45,.48,.21),5.0:(.33,.43,.34,.18),5.5:(.37,.43,.29,.17)}
dog={6.0:(0,.36,.42,.34),6.5:(.04,.35,.48,.36),7.0:(.08,.35,.54,.37),7.5:(.05,.34,.69,.45),8.0:(0,.34,.84,.53),8.5:(.02,.32,.85,.56)}
fire={}
for t in [9.0,9.5,10.0,10.5,11.0,11.5]:
    van[t]=(.20,.06,.80,.36); dog[t]=(.49,.44,.19,.14); fire[t]=(.36,.58,.30,.15)
for t in [12.0,12.5,13.0,13.5,14.0,14.5,15.0]:
    dog[t]=(.51,.48,.18,.24)
d={"mediaId":4050,"level":"A","keyWord":"friend","defaultVoice":"male",
"taps":[{"phrase":"to drive along the road","target":"the van","voice":"male","keys":mk(van)},
{"phrase":"to lie on a bed","target":"the dog","voice":"male","keys":mk(dog)},
{"phrase":"to burn in the sand","target":"the fire","voice":"male","keys":mk(fire)}],
"stillS":12.0,
"nouns":[{"word":"the sky","x":.50,"y":.15,"voice":"male"},{"word":"friends","x":.30,"y":.66,"voice":"male"},{"word":"a dog","x":.61,"y":.57,"voice":"male"}],
"question":"Where are the friends sitting at night?","answer":["They","are","sitting","by","the","fire."],"answerVoice":"male",
"notes":"Several similar young men across five shots, so no person is a tap target; targets are the van, the dog and the fire. Van: boxed as the rear door in the first shot (0-3 s), the driving van (3.5-5.5 s) and the parked van at night (its box covers the men's heads, who are not targets); off inside the van (6-8.5 s) and in the last shot where only two slivers of its doors show at the edges. The last shot shows three people and the dog (the packet says four). 'friends' pill sits on the two men sitting close together on the left; the third man sits apart on the right."}
json.dump(d,open("content/4050.json","w"),indent=1)
