import json
T=[i*0.5 for i in range(21)]
d={0.0:(.37,.42,.46,.27),0.5:(.34,.43,.49,.28),1.0:(.26,.43,.57,.43),1.5:(.16,.43,.67,.46),2.0:(.07,.43,.76,.38)}
h={2.5:.43,3.0:.56,3.5:.57,4.0:.50,4.5:.42,5.0:.57,5.5:.52,6.0:.46,6.5:.52,7.0:.55,7.5:.57,8.0:.48,8.5:.50,9.0:.56,9.5:.57,10.0:.48}
for t,v in h.items(): d[t]=(0.0,.43,.83,v)
ho={t:(.72,.17,.28,.19) for t in T}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":4009,"level":"A","keyWord":"line","defaultVoice":"male",
"taps":[
 {"phrase":"to walk in a line","target":"the ducks on the path","voice":"male","keys":keys(d)},
 {"phrase":"to walk down a path","target":"the ducks on the path","voice":"male","keys":keys(d)},
 {"phrase":"to have a brown roof","target":"the houses","voice":"male","keys":keys(ho)}],
"stillS":10.0,
"nouns":[{"word":"ducks","x":.45,"y":.58,"voice":"male"},{"word":"a tree","x":.18,"y":.30,"voice":"male"},{"word":"flowers","x":.78,"y":.88,"voice":"male"},{"word":"mountains","x":.40,"y":.07,"voice":"male"}],
"question":"How are the ducks walking?",
"answer":["They","are","walking","in","a","line."],
"answerVoice":"male",
"notes":"Only one moving target group (the line of ducks), so two phrases share it; the third is a state on the two farmhouses (both in one box). A small duck stands apart in the grass from 1.5 s; it lies inside the rectangle of the line box (the line is diagonal), so it could not get its own box and a tap on it counts for the line. Key word 'line' is in phrase 1 and the answer, not among the nouns (it would sit on the same place as 'ducks')."}
json.dump(c,open("content/4009.json","w"),indent=1)
