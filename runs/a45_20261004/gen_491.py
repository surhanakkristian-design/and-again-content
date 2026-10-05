import json
T=[i*0.5 for i in range(21)]
man={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,1,1),1.5:(0,0.05,1,0.95),2.0:(0,0.07,1,0.93),
 7.5:(0.70,0.05,0.30,0.75),8.0:(0.66,0.08,0.34,0.66),8.5:(0.67,0.09,0.33,0.64),9.0:(0.64,0.11,0.36,0.75),9.5:(0.60,0.13,0.40,0.87),10.0:(0.51,0.09,0.49,0.86)}
wom={2.5:(0.08,0,0.80,0.34),3.0:(0,0,1,0.52),3.5:(0,0,1,0.52),4.0:(0,0,1,0.42),4.5:(0,0,1,0.45),5.0:(0,0,1,0.58),
 5.5:(0,0,0.75,0.45),6.0:(0,0,0.52,0.34),6.5:(0,0,0.55,0.33),7.0:(0,0,0.57,0.44),
 7.5:(0,0.08,0.68,0.78),8.0:(0,0.09,0.63,0.68),8.5:(0,0.10,0.64,0.66),9.0:(0,0.14,0.62,0.68),9.5:(0.02,0.14,0.57,0.66),10.0:(0,0.10,0.50,0.56)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":491,"level":"A","keyWord":"mustard","defaultVoice":"male",
"taps":[{"phrase":"to taste the mustard","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to hold a brush","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to carry a tray","target":"the man","voice":"male","keys":keys(man)}],
"stillS":2.0,
"nouns":[{"word":"mustard","x":0.42,"y":0.72,"voice":"male"},{"word":"a bowl","x":0.45,"y":0.83,"voice":"male"},
{"word":"a man","x":0.50,"y":0.20,"voice":"male"},{"word":"a window","x":0.80,"y":0.32,"voice":"male"}],
"question":"What is the man tasting?",
"answer":["He","is","tasting","mustard","from","a","bowl."],"answerVoice":"male",
"notes":"2.5-7.0 s are close-ups of hands and an apron torso without a face: treated as the woman (same apron; she holds the brush at 5.5-7.0), the man is off there (only a sliver of dark shirt at 6.0-7.0). The packet description says the man whisks; the picture shows the apron wearer. Two phrases share the man; the dog (6.0-9.5) is small and does nothing clear, so no phrase for it. At 10.0 the hand on the tray's left edge is taken as the man's and lies in the woman's box area border."}
json.dump(c,open("content/491.json","w"),indent=1)
