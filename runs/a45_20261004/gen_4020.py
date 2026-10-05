import json
times=[i*0.5 for i in range(31)]
def keys(d):
    return [dict(t=t, **({"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"off":True})) for t in times]
D={0.0:(.43,.09,.40,.34),0.5:(.43,.09,.40,.34),1.0:(.45,.09,.39,.34),1.5:(.46,.09,.38,.34),2.0:(.46,.08,.40,.35),2.5:(.47,.08,.40,.35),
3.0:(.47,.10,.42,.35),3.5:(.46,.10,.44,.35),4.0:(.40,.08,.50,.36),4.5:(.36,.08,.54,.36),5.0:(.34,.09,.57,.36),5.5:(.37,.09,.52,.36),
6.0:(.33,.06,.49,.39),6.5:(.31,.05,.49,.41),7.0:(.31,.05,.48,.42),7.5:(.29,.06,.52,.42),8.0:(.26,.04,.58,.42),8.5:(.18,.08,.68,.40),
9.0:(.06,.07,.73,.42),9.5:(.0,.04,.76,.47),10.0:(.0,.02,.70,.51),10.5:(.0,.0,.65,.53),11.0:(.0,.0,.60,.58),11.5:(.0,.0,.60,.58),
12.0:(.0,.0,.56,.57),12.5:(.0,.0,.54,.58),13.0:(.0,.03,.41,.54),13.5:(.0,.07,.34,.49),14.0:(.0,.10,.27,.46),14.5:(.0,.15,.22,.39),15.0:(.0,.28,.18,.24)}
F={0.0:(.33,.47,.20,.14),0.5:(.29,.47,.20,.14),1.0:(.27,.48,.20,.14),1.5:(.25,.48,.20,.14),2.0:(.24,.48,.20,.14),2.5:(.24,.49,.20,.14),
3.0:(.26,.52,.20,.14),3.5:(.27,.52,.21,.14),4.0:(.27,.51,.25,.14),4.5:(.30,.51,.23,.14),5.0:(.34,.52,.23,.14),5.5:(.35,.52,.21,.14),
6.0:(.36,.52,.21,.14),6.5:(.33,.52,.23,.14),7.0:(.22,.53,.37,.14),7.5:(.32,.53,.30,.15),8.0:(.32,.52,.36,.15),8.5:(.38,.52,.36,.16),
9.0:(.43,.51,.33,.14),9.5:(.42,.52,.35,.14),10.0:(.36,.54,.44,.14),10.5:(.38,.54,.46,.14),11.0:(.61,.47,.27,.17),11.5:(.61,.47,.29,.17),
12.0:(.57,.44,.32,.16),12.5:(.57,.42,.30,.16),13.0:(.51,.43,.35,.15),13.5:(.59,.42,.28,.14),14.0:(.58,.42,.30,.14),14.5:(.61,.42,.27,.14),15.0:(.59,.42,.29,.14)}
c={"mediaId":4020,"level":"A","keyWord":"to watch","defaultVoice":"female",
"taps":[
 {"phrase":"to watch a small frog","target":"the dog","voice":"female","keys":keys(D)},
 {"phrase":"to swim in the water","target":"the frog","voice":"female","keys":keys(F)},
 {"phrase":"to stand in the water","target":"the dog","voice":"female","keys":keys(D)}],
"stillS":8.0,
"nouns":[{"word":"trees","x":0.22,"y":0.05,"voice":"female"},
 {"word":"a dog","x":0.55,"y":0.22,"voice":"female"},
 {"word":"a frog","x":0.50,"y":0.60,"voice":"female"},
 {"word":"water","x":0.25,"y":0.82,"voice":"female"}],
"question":"What is the dog doing?",
"answer":["The","dog","is","watching","a","small","frog."],
"answerVoice":"female",
"notes":"Only two possible targets (dog, frog), the dog carries two phrases. Dog box = the dog itself, not its reflection. At 10.0-11.5 s the dog's chin is right above / beside the frog: boxes are split there (10.0-10.5 s horizontally under the chin, 11.0-11.5 s vertically at x 0.60, the frog's stretched hind leg falls outside its box). From 13.0 s only the dog's muzzle is left at the left edge."}
json.dump(c,open("content/4020.json","w"),indent=1)
