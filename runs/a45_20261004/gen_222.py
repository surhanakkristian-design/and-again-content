import json
T=[i*0.5 for i in range(19)]
W={0.0:(0,.27,.40,.73),0.5:(0,.30,.38,.70),2.0:(.82,.26,.18,.50),4.5:(.22,.39,.42,.61),5.0:(.22,.40,.46,.60),5.5:(.17,.52,.56,.46),
6.0:(.22,.49,.48,.46),6.5:(.30,.50,.35,.38),7.0:(.32,.49,.30,.38),7.5:(.31,.49,.29,.38),8.0:(.32,.49,.26,.34),8.5:(.24,.36,.56,.44),9.0:(0,.65,.80,.35)}
D={0.5:(.39,.25,.19,.23),1.0:(.03,.22,.87,.76),1.5:(.15,.22,.68,.76),2.5:(.32,.28,.62,.31),3.0:(.30,.38,.56,.22),3.5:(.37,.38,.44,.22),
7.5:(.61,.42,.21,.14),8.0:(.59,.40,.23,.15)}
C={4.0:(.04,.18,.92,.82),4.5:(0,.16,.38,.22),5.0:(.02,.19,.37,.20),5.5:(.02,.19,.37,.21),6.0:(.04,.20,.36,.21),6.5:(.13,.23,.30,.19),
7.0:(.17,.25,.28,.18),7.5:(.18,.25,.27,.18),8.0:(.18,.26,.28,.16),8.5:(.08,0,.42,.25),9.0:(.09,0,.43,.26)}
def k(D):
    return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else {"t":t,"off":True} for t in T]
d={"mediaId":222,"level":"B","keyWord":"delay","defaultVoice":"female",
"taps":[{"phrase":"to block the bus door","target":"the driver","voice":"male","keys":k(D)},
{"phrase":"to collapse onto her suitcase","target":"the woman","voice":"female","keys":k(W)},
{"phrase":"to display the time","target":"the clock","voice":"female","keys":k(C)}],
"stillS":8.0,
"nouns":[{"word":"a clock","x":.32,"y":.34,"voice":"female"},{"word":"a suitcase","x":.57,"y":.76,"voice":"female"},
{"word":"neon signs","x":.86,"y":.15,"voice":"female"},{"word":"a driver","x":.70,"y":.49,"voice":"male"}],
"question":"What is the driver doing?","answer":["He","is","blocking","the","bus","door."],"answerVoice":"male",
"notes":"Key word 'delay' is abstract and not in the texts (shown by the clock and the waiting). Driver: on at 0.5 (face between two passengers, small box), 1.0-1.5 (blocking the door), 2.5 (under the hood), 3.0-3.5 (only his legs), 7.5-8.0 (behind the hood); off at 4.5-7.0 where only his shoes show in the windscreen. Woman at 2.0 is only a sliver at the right edge (boxed). 0.0-0.5 she is seen from behind. Clock box = the clock face (the pole is left out where the woman stands beside it). Other waiting men are not targets. 'a suitcase' pill is on the grey upright case; she sits on a second blue one right beside it."}
json.dump(d,open("content/222.json","w"),indent=1)
