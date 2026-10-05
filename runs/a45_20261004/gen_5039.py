import json
T=[i*0.5 for i in range(19)]
M={0.0:(0.00,0.25,0.73,0.75),0.5:(0.00,0.27,0.73,0.73),1.0:(0.02,0.30,0.74,0.70),1.5:(0.04,0.30,0.75,0.70),
2.0:(0.07,0.33,0.74,0.67),2.5:(0.05,0.35,0.76,0.65),3.0:(0.00,0.35,0.71,0.65),3.5:(0.00,0.33,0.72,0.67),
4.0:(0.00,0.33,0.69,0.67),4.5:(0.06,0.32,0.63,0.68),5.0:(0.10,0.32,0.60,0.68),5.5:(0.18,0.49,0.34,0.51),
6.0:(0.06,0.52,0.48,0.48),6.5:(0.06,0.55,0.50,0.45),7.0:(0.08,0.60,0.52,0.40),7.5:(0.10,0.62,0.50,0.38),
8.0:(0.10,0.67,0.52,0.33),8.5:(0.10,0.67,0.52,0.33),9.0:(0.10,0.70,0.52,0.30)}
F={6.0:(0.00,0.00,1.00,0.50),6.5:(0.00,0.00,1.00,0.50),7.0:(0.00,0.00,1.00,0.50),7.5:(0.00,0.00,1.00,0.50),
8.0:(0.00,0.03,1.00,0.45),8.5:(0.00,0.08,1.00,0.38),9.0:(0.00,0.18,1.00,0.34)}
def keys(d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":5039,"level":"B","keyWord":"cage","defaultVoice":"male",
"taps":[{"phrase":"to unlatch a cage door","target":"the old man","voice":"male","keys":keys(M)},
{"phrase":"to hold an empty cage","target":"the old man","voice":"male","keys":keys(M)},
{"phrase":"to circle over the city","target":"the flock","voice":"male","keys":keys(F)}],
"stillS":8.0,
"nouns":[{"word":"a flock","x":0.50,"y":0.25,"voice":"male"},{"word":"the sun","x":0.27,"y":0.51,"voice":"male"},
{"word":"a crowd","x":0.80,"y":0.62,"voice":"male"},{"word":"a cage","x":0.20,"y":0.86,"voice":"male"}],
"question":"What is the old man holding?","answer":["He","is","holding","an","empty","cage."],"answerVoice":"male",
"notes":"The flock is boxed only 6.0-9.0 s, when the sky is full of birds; before that only single birds fly past (off). 'a cage' pill sits on the empty cage the old man holds, but more cages are stacked at the bottom right of the still - verifier please check the slot is unambiguous enough. Old man box at 4.0 s also covers a younger man standing behind him (no other target there)."}
json.dump(c,open('content/5039.json','w'),indent=1)
