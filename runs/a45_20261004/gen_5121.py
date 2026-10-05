import json
W = {0.0:(0,0,0.6,0.72),0.5:(0,0,0.36,0.72),1.0:(0,0.19,0.42,0.65),1.5:(0,0.23,0.7,0.5),2.0:(0,0.22,0.58,0.48),
2.5:(0,0.24,0.44,0.46),3.0:(0,0.24,0.44,0.48),3.5:(0,0.23,0.44,0.48)}
M = {4.0:(0.6,0.03,0.4,0.62),4.5:(0.52,0.05,0.48,0.82),5.0:(0.48,0.08,0.52,0.92),5.5:(0.58,0.07,0.42,0.93),6.0:(0.66,0.03,0.34,0.94),
6.5:(0.66,0.03,0.34,0.94),7.0:(0.74,0.02,0.26,0.98)}
K = {7.5:(0.42,0.27,0.58,0.73),8.0:(0.58,0.24,0.42,0.76),8.5:(0.48,0.25,0.52,0.75),9.0:(0.43,0.26,0.57,0.74),9.5:(0.63,0.27,0.37,0.73),
10.0:(0.56,0.27,0.44,0.73),10.5:(0.72,0.24,0.28,0.76),11.0:(0.62,0.24,0.38,0.76),11.5:(0.58,0.24,0.42,0.76),12.0:(0.55,0.23,0.45,0.77)}
times=[i/2 for i in range(25)]
def ks(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"t":t,"off":True}) for t in times]
c={"mediaId":5121,"level":"B","keyWord":"remove","defaultVoice":"male",
"taps":[{"phrase":"to remove a tray of muffins","target":"the woman","voice":"female","keys":ks(W)},
{"phrase":"to slide out a roasting tin","target":"the man in the dark jumper","voice":"male","keys":ks(M)},
{"phrase":"to carry freshly baked loaves","target":"the baker","voice":"male","keys":ks(K)}],
"stillS":12.0,
"nouns":[{"word":"loaves","x":0.2,"y":0.45,"voice":"male"},{"word":"a rack","x":0.4,"y":0.33,"voice":"male"},
{"word":"a baker","x":0.75,"y":0.65,"voice":"male"}],
"question":"What is the woman removing?","answer":["She","is","removing","a","tray","of","muffins."],"answerVoice":"female",
"notes":"Three shots, one person each: woman 0-3.5, man in dark jumper 4.0-7.0 (only head and arms visible), baker 7.5-12.0. Baker shows 4 loaves (two stacks), not six as in the description. Background bakery workers at 7.5-12.0 are small and not targets. Three people of mixed gender -> defaultVoice male (evenId false). Only 3 nouns; 'a rack' = the trolley rack with loaves behind the baker."}
json.dump(c,open('content/5121.json','w'),indent=1)
