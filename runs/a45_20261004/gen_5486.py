import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
man={0.0:(0,0,.48,.55),0.5:(0,0,.48,.53),1.0:(0,0,.48,.53),1.5:(0,0,.56,.55),2.0:(0,0,.23,1.0),
2.5:(0,0,.58,.50),3.0:(0,0,.58,.62),3.5:(0,0,.58,.66),4.0:(.04,0,.52,.78),4.5:(0,0,.53,.80),
5.0:(.30,.11,.33,.33),5.5:(.37,.10,.30,.36),6.0:(.42,.09,.28,.36),6.5:(.38,.10,.30,.36),7.0:(.35,.11,.28,.31),
7.5:(.35,.11,.28,.31),8.0:(.37,.11,.26,.33),8.5:(.37,.12,.31,.33),9.0:(.37,.12,.34,.31),9.5:(.38,.12,.34,.31),10.0:(.38,.12,.33,.33)}
pot={0.0:(.22,.55,.63,.42),0.5:(.22,.55,.63,.42),1.0:(.22,.55,.63,.42),1.5:(.22,.55,.63,.42),2.0:(.23,.53,.62,.44)}
c={"mediaId":5486,"level":"A","keyWord":"flowerpot","defaultVoice":"male",
"taps":[
 {"phrase":"to water the flowers","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to get water from the can","target":"the big flowerpot","voice":"male","keys":keys(pot)},
 {"phrase":"to wear a cap","target":"the man","voice":"male","keys":keys(man)}],
"stillS":1.0,
"nouns":[{"word":"a window","x":0.72,"y":0.20,"voice":"male"},
 {"word":"a watering can","x":0.20,"y":0.38,"voice":"male"},
 {"word":"a plant","x":0.52,"y":0.64,"voice":"male"},
 {"word":"a flowerpot","x":0.52,"y":0.82,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","watering","the","flowers."],
"answerVoice":"male",
"notes":"Flowerpot only visible 0-2 s (then off). Man and pot overlap at 0-2 s: man box cut at the pot top, so his lower body at bottom-left is outside his box. A small second pot stands behind the big one at 1.0-2.0 s, hence 'the big flowerpot' and a phrase only the watered pot fits."}
json.dump(c,open('content/5486.json','w'),indent=1)
