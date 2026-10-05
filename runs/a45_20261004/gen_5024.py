import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
cur={0.0:(0,0.14,0.60,0.86),0.5:(0,0.16,0.66,0.84),1.0:(0,0.16,0.62,0.84),1.5:(0,0.17,0.64,0.83),2.0:(0,0.14,0.62,0.86),
2.5:(0,0.11,0.62,0.89),3.0:(0,0.07,0.55,0.93),3.5:(0.26,0.15,0.68,0.85),4.0:(0,0.19,0.62,0.81),4.5:(0,0.25,0.66,0.75),
5.0:(0,0.22,0.64,0.78),5.5:(0,0.16,0.58,0.84),6.0:(0,0.21,0.58,0.60),6.5:(0,0.23,0.84,0.70),7.0:(0,0.22,0.60,0.76),
7.5:(0,0.16,0.60,0.72),8.0:(0,0.23,0.70,0.70),8.5:(0.03,0,0.97,1.0),9.0:(0.14,0.09,0.80,0.91),9.5:(0.24,0.19,0.58,0.81),
10.0:(0.30,0.24,0.48,0.76),10.5:(0.32,0.26,0.37,0.74),11.0:(0.36,0.28,0.34,0.72),11.5:(0.37,0.28,0.33,0.72),12.0:(0.37,0.29,0.31,0.60)}
kim={4.5:(0.68,0.28,0.32,0.72),5.0:(0.64,0.27,0.36,0.73),5.5:(0.62,0.26,0.38,0.74),6.0:(0.60,0.25,0.40,0.75),
10.0:(0.79,0.39,0.21,0.22),10.5:(0.72,0.38,0.20,0.17)}
d={"mediaId":5024,"level":"A","keyWord":"dictionary","defaultVoice":"female",
"taps":[{"phrase":"to wave at the camera","target":"the curly-haired woman","voice":"female","keys":keys(cur)},
{"phrase":"to put her hands together","target":"the woman in black","voice":"female","keys":keys(kim)},
{"phrase":"to carry many books","target":"the curly-haired woman","voice":"female","keys":keys(cur)}],
"stillS":1.5,
"nouns":[{"word":"dictionaries","x":0.42,"y":0.73,"voice":"female"},{"word":"a flag","x":0.20,"y":0.62,"voice":"female"},
{"word":"a cup","x":0.86,"y":0.63,"voice":"female"}],
"question":"What is the curly-haired woman carrying?","answer":["She","is","carrying","many","dictionaries."],"answerVoice":"female",
"notes":"Many cuts and extra people; only two targets used (curly-haired woman twice: wave 0-0.5 s, book tower 8.5-12 s). Woman in black (kimono) set off at 6.5 s (hidden behind the curly-haired woman) and from 11.0 s (behind other guests); at 10.0-10.5 s she is a small background figure. 'dictionaries' pill sits between the two stacked dictionaries on the table."}
json.dump(d,open("content/5024.json","w"),indent=1)
