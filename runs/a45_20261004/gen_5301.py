import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
y={0.0:(0,.06,.83,.94),0.5:(0,.07,.82,.93),1.0:(0,.11,.89,.89),1.5:(0,.05,.76,.95),2.0:(0,.05,.70,.95),2.5:(0,.04,.76,.96),
3.0:(0,.07,.76,.93),3.5:(.18,.11,.74,.89),4.0:(0,.09,.80,.91),4.5:(0,.05,.62,.95),5.0:(0,.07,.58,.93),5.5:(0,.09,.25,.91)}
b={3.5:(0,.17,.17,.22),5.5:(.27,.22,.22,.23),6.0:(.02,.21,.30,.27),6.5:(0,.26,.18,.22)}
d={"mediaId":5301,"level":"A","keyWord":"allergy","defaultVoice":"female",
"taps":[{"phrase":"to sneeze into her hands","target":"the woman in yellow","voice":"female","keys":keys(y)},
{"phrase":"to touch her chest","target":"the woman in yellow","voice":"female","keys":keys(y)},
{"phrase":"to carry a backpack","target":"the woman with the backpack","voice":"female","keys":keys(b)}],
"stillS":2.0,
"nouns":[{"word":"the sky","x":0.72,"y":0.07,"voice":"female"},{"word":"a hand","x":0.58,"y":0.57,"voice":"female"},
{"word":"flowers","x":0.80,"y":0.80,"voice":"female"},{"word":"a dress","x":0.20,"y":0.88,"voice":"female"}],
"question":"What is the woman in yellow doing?","answer":["She","is","sneezing","into","her","hands."],"answerVoice":"female",
"notes":"Woman in yellow visible 0-5.5 only (6.0 shows just an arm fragment at the left edge, marked off); 6.0-9.0 are field shots with far people. Backpack woman passes behind at 3.5, 5.5-6.5; at 3.5 her box is split from the yellow woman's hair along x=0.18. Key word allergy is not a visible noun."}
json.dump(d,open("content/5301.json","w"),indent=1)
