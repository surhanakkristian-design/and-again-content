import json
T=[i*0.5 for i in range(31)]
def mk(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
man={0.0:(.54,.42,.18,.18),0.5:(.53,.43,.19,.18),1.0:(.53,.43,.21,.22),1.5:(.54,.43,.22,.25),2.0:(.52,.42,.27,.31),2.5:(.50,.41,.33,.38),
3.0:(.53,.37,.34,.51),3.5:(.55,.32,.36,.68),4.0:(.57,.29,.43,.71),4.5:(.57,.26,.43,.74),5.0:(.52,.24,.48,.76),5.5:(.50,.23,.50,.77),
6.0:(.42,.23,.58,.77),6.5:(.42,.23,.58,.77),7.0:(.42,.24,.58,.76),7.5:(.42,.24,.58,.76),8.0:(.46,.25,.54,.75),8.5:(.42,.25,.58,.75),
9.0:(.42,.25,.58,.75),9.5:(.38,.21,.62,.79),
10.0:(.47,.25,.53,.75),10.5:(.45,.28,.55,.72),11.0:(.60,.25,.40,.75),11.5:(.43,.25,.57,.75),12.0:(.17,.24,.83,.76),12.5:(.07,.24,.86,.76),
13.0:(.07,.24,.83,.76),13.5:(.08,.24,.83,.76),14.0:(.09,.23,.83,.77),14.5:(.08,.23,.84,.77),15.0:(.08,.22,.83,.78)}
bike={0.0:(.36,.42,.18,.16),0.5:(.35,.43,.18,.16),1.0:(.35,.43,.18,.17),1.5:(.36,.43,.18,.19),2.0:(.32,.44,.20,.21),2.5:(.27,.45,.23,.23),
3.0:(.22,.43,.31,.30),3.5:(.12,.44,.43,.32),4.0:(.05,.45,.52,.35),4.5:(0,.45,.57,.39),5.0:(0,.46,.52,.41),5.5:(0,.57,.50,.40),
6.0:(0,.48,.42,.45),6.5:(0,.48,.42,.42),7.0:(0,.48,.42,.41),7.5:(0,.48,.42,.41),8.0:(0,.48,.46,.41),8.5:(0,.48,.42,.41),9.0:(0,.48,.42,.41),9.5:(0,.49,.38,.41)}
truck={0.0:(.15,.26,.70,.16),0.5:(.11,.24,.78,.18),1.0:(.07,.19,.85,.24),1.5:(.05,.18,.91,.25),2.0:(0,.14,1,.28),2.5:(0,.10,1,.31),
3.0:(0,.07,1,.30),3.5:(0,.04,1,.28),4.0:(0,.02,1,.27),4.5:(0,.01,1,.25),5.0:(0,.02,1,.22),5.5:(0,.02,1,.21),6.0:(0,.02,1,.21),6.5:(0,.02,1,.21),
7.0:(0,.03,1,.21),7.5:(0,.03,1,.21),8.0:(0,.02,1,.23),8.5:(0,.02,1,.23),9.0:(0,.02,1,.23),9.5:(0,.05,1,.16)}
d={"mediaId":4051,"level":"B","keyWord":"motorcycle","defaultVoice":"male",
"taps":[{"phrase":"to stroke a fluffy cat","target":"the man","voice":"male","keys":mk(man)},
{"phrase":"to rest on a metal rack","target":"the motorcycle","voice":"male","keys":mk(bike)},
{"phrase":"to tower over the cars","target":"the truck","voice":"male","keys":mk(truck)}],
"stillS":8.5,
"nouns":[{"word":"a motorcycle","x":.22,"y":.70,"voice":"male"},{"word":"a truck","x":.25,"y":.34,"voice":"male"},{"word":"a cap","x":.68,"y":.30,"voice":"male"},{"word":"a T-shirt","x":.72,"y":.58,"voice":"male"}],
"question":"What is the truck carrying?","answer":["It","is","carrying","a","motorcycle","on","a","rack."],"answerVoice":"male",
"notes":"Man, motorcycle and truck overlap in the picture, so the boxes are split: the truck box is only the band of the truck above the man and the motorcycle (its lower body and wheels behind them fall into the other boxes or outside). Man/motorcycle split along the line between his body and the bike; his hand resting on the bike (4-5 s) lies in the motorcycle box. Two cats inside, so no cat is a target or a noun. Nouns are fairly basic words for level B (key word included); 'a cap' and 'a T-shirt' are on the same, large, man at clearly different places."}
json.dump(d,open("content/4051.json","w"),indent=1)
