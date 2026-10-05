import json
times=[i*0.5 for i in range(31)]
def keys(d):
    return [dict(t=t, **({"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"off":True})) for t in times]
D={0.0:(.59,.18,.18,.14),0.5:(.59,.18,.18,.14),1.0:(.58,.19,.18,.14),1.5:(.58,.20,.18,.14),2.0:(.59,.23,.18,.14),
2.5:(.53,.24,.18,.15),3.0:(.51,.26,.18,.16),3.5:(.52,.26,.18,.16),4.0:(.56,.28,.23,.17),4.5:(.71,.38,.20,.19),
5.0:(.72,.42,.20,.24),5.5:(.57,.52,.25,.14),6.0:(.24,.23,.50,.45),6.5:(.13,.08,.76,.67),7.0:(.14,.07,.68,.80),
7.5:(.13,.06,.68,.80),8.0:(.11,.06,.62,.70),8.5:(.0,.21,.70,.52),9.0:(.0,.51,.58,.31),9.5:(.27,.55,.26,.14),
10.0:(.33,.48,.24,.19),10.5:(.64,.39,.20,.21),11.0:(.57,.30,.21,.25),11.5:(.56,.28,.20,.15),12.0:(.51,.27,.21,.15),
12.5:(.41,.26,.27,.16),13.0:(.31,.31,.25,.14),13.5:(.27,.36,.18,.14),14.0:(.33,.34,.18,.14),14.5:(.34,.34,.18,.15),15.0:(.34,.33,.18,.15)}
S={0.0:(.49,.33,.22,.14),0.5:(.50,.33,.20,.14),1.0:(.49,.34,.20,.14),1.5:(.47,.35,.22,.14),2.0:(.44,.38,.26,.14),
2.5:(.34,.40,.35,.14),3.0:(.27,.43,.42,.14),3.5:(.28,.43,.42,.14),4.0:(.29,.30,.26,.27),4.5:(.30,.27,.40,.30),
5.0:(.29,.28,.42,.29),5.5:(.28,.27,.44,.24),9.0:(.30,.28,.26,.22),9.5:(.28,.28,.43,.26),
10.0:(.28,.28,.45,.19),10.5:(.29,.27,.34,.30),11.0:(.30,.30,.25,.27),11.5:(.30,.44,.44,.14),12.0:(.22,.43,.50,.14),
12.5:(.13,.43,.56,.15),13.0:(.09,.46,.54,.14),13.5:(.46,.38,.23,.18),14.0:(.52,.38,.21,.20),14.5:(.53,.38,.23,.20),15.0:(.53,.38,.23,.20)}
c={"mediaId":4018,"level":"A","keyWord":"a scooter","defaultVoice":"female",
"taps":[
 {"phrase":"to wear a blue cap","target":"the white dog","voice":"female","keys":keys(D)},
 {"phrase":"to carry two dogs","target":"the scooter","voice":"female","keys":keys(S)},
 {"phrase":"to fall on its side","target":"the scooter","voice":"female","keys":keys(S)}],
"stillS":9.5,
"nouns":[{"word":"the sky","x":0.55,"y":0.08,"voice":"female"},
 {"word":"grass","x":0.15,"y":0.27,"voice":"female"},
 {"word":"a scooter","x":0.50,"y":0.44,"voice":"female"},
 {"word":"a car","x":0.50,"y":0.80,"voice":"female"}],
"question":"What are the dogs riding?",
"answer":["The","dogs","are","riding","a","scooter."],
"answerVoice":"female",
"notes":"At 0.0-1.5 s scooter and dogs are tiny and far away, boxes there are approximate (dog box over the heads, scooter box from the body down). Only two targets (white dog, scooter): the brown corgi is not a target, almost everything it does the white dog does too. While the dogs sit on the scooter the two boxes are split: dog box above, scooter box below (scooter box then misses handlebars/seat); after the fall (13.5-15.0 s) the split is left/right: dog box on the heads, scooter box on the rear half only. Scooter is OFF at 6.0-8.5 s: hidden behind the dogs on the bonnet (a small mint patch shows between the dogs at 8.5 s, inside the white dog's box). 'grass' = the tall dry reeds, chosen as the A-level word. 'a car' = the bonnet we film over."}
json.dump(c,open("content/4018.json","w"),indent=1)
