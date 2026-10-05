import json
times=[i*0.5 for i in range(24)]
carb={0.0:(.63,.27,.37,.18),0.5:(.31,.28,.52,.19),1.0:(.37,.29,.47,.21),1.5:(.33,.28,.54,.23),2.0:(.21,.30,.71,.25),2.5:(.21,.30,.79,.28),
3.0:(0,0,1,1),3.5:(0,0,1,1),4.0:(0,0,1,1),4.5:(0,0,1,1),5.0:(0,0,1,1),
5.5:(0,.32,1,.40),6.0:(0,.29,1,.41),6.5:(0,.29,1,.41),7.0:(0,.33,1,.40),7.5:(0,.36,1,.39),
8.0:(0,.15,1,.85),8.5:(0,.15,1,.85),9.0:(0,.15,1,.85),9.5:(0,.15,1,.85),10.0:(0,.16,1,.36),10.5:(0,0,1,.68)}
manb={1.0:(.06,.84,.38,.16),1.5:(.56,.78,.42,.22),2.0:(.48,.73,.52,.27),2.5:(.03,.66,.72,.34)}
def keys(b):
    return [({"t":t,"x":float(b[t][0]),"y":float(b[t][1]),"w":float(b[t][2]),"h":float(b[t][3])} if t in b else {"t":t,"off":True}) for t in times]
car=keys(carb); man=keys(manb)
d={"mediaId":4164,"level":"A","keyWord":"brake","defaultVoice":"female",
"taps":[
 {"phrase":"to drive around a corner","target":"the car","voice":"female","keys":car},
 {"phrase":"to have red back lights","target":"the car","voice":"female","keys":car},
 {"phrase":"to watch the green car","target":"the man","voice":"male","keys":man}],
"stillS":3.0,
"nouns":[{"word":"a brake","x":0.85,"y":0.50,"voice":"female"},
 {"word":"a wheel","x":0.38,"y":0.42,"voice":"female"},
 {"word":"a road","x":0.50,"y":0.94,"voice":"female"}],
"question":"What is the green car doing?",
"answer":["It","is","driving","around","a","corner."],
"answerVoice":"female",
"notes":"Many cuts. The brake (key word) is visible only in the wheel close-up at 3.0-3.5 s, too short for a tap target, so it is a noun on the still (red part on the right of the wheel) and not a tap phrase. The man is a spectator seen from behind (blurred dark head at the bottom, 1.0-2.5 s only); a second pinkish blur at the frame edge at 2.0 / 2.5 s may be another spectator but is not identifiable. Two phrases share the car; the second is a state (rear lights seen 5.5-7.5 s). Close-ups 3.0-5.0 s: the whole frame counts as the car. 11.0-11.5 s is pure blur: all off. 'a road' = the grey track at the bottom of the still."}
json.dump(d,open("content/4164.json","w"),indent=1,ensure_ascii=False)
