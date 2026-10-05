import json
T=[i*0.5 for i in range(31)]
def mk(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
S={0.0:(.60,.34,.40,.31),0.5:(.60,.34,.40,.31),1.0:(.55,.35,.45,.31),1.5:(.55,.37,.45,.28),2.0:(.60,.35,.40,.30),
2.5:(.54,.45,.32,.18),3.0:(.50,.54,.18,.14),3.5:(.47,.53,.18,.14)}
H={5.5:(0,0,1,.50),6.0:(.10,.30,.90,.70),6.5:(.42,0,.58,.30),7.0:(.44,0,.52,.20),7.5:(.38,0,.55,.18),8.0:(.47,0,.41,.16),
8.5:(.57,0,.31,.16),9.0:(.61,0,.21,.18),9.5:(.63,.02,.24,.17),10.0:(.66,.05,.20,.15),10.5:(.71,.08,.18,.14),
11.0:(.73,.12,.18,.14),11.5:(.75,.13,.18,.14)}
C={12.0:(.36,.34,.24,.14),12.5:(.35,.33,.27,.14),13.0:(.33,.33,.33,.14),13.5:(.31,.33,.42,.14),14.0:(.28,.34,.56,.15),
14.5:(.14,.37,.86,.30),15.0:(0,.42,1,.58)}
d={"mediaId":4081,"level":"B","keyWord":"peak","defaultVoice":"male",
"taps":[{"phrase":"to crouch on the skid","target":"the skydiver in black","voice":"male","keys":mk(S)},
{"phrase":"to hover above the mountains","target":"the helicopter","voice":"male","keys":mk(H)},
{"phrase":"to mark the landing spot","target":"the orange cross","voice":"male","keys":mk(C)}],
"stillS":7.0,
"nouns":[{"word":"the sun","x":.16,"y":.10,"voice":"male"},{"word":"a helicopter","x":.64,"y":.08,"voice":"male"},
{"word":"a peak","x":.28,"y":.35,"voice":"male"},{"word":"a valley","x":.60,"y":.53,"voice":"male"}],
"question":"What is the helicopter doing?","answer":["It","is","hovering","above","the","snowy","peaks."],"answerVoice":"male",
"notes":"POV clip: the main person shows only as white-suited legs (no gender visible), so the legs are not a target and defaultVoice follows the odd id. The skydiver in black crouches on the skid at 0-2.0 s, has jumped at 2.5 s and is a tiny falling figure at 3.0-3.5 s (minimum box). The helicopter is boxed only from 5.5 s, when it is seen from outside; at 0-5.0 s only its skid, door frame and rotor blade show from inside, so it is off there (doubt: a learner might tap those parts). Orange cross 12.0-15.0 s. Still 7.0 s: 'a peak' sits on the snowy summits of the ridge at the left (several peaks in the range); the small black speck in the sky is ignored."}
json.dump(d,open("content/4081.json","w"),indent=1)
