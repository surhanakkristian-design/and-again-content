import json
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2]-d[t][0],2),"h":round(d[t][3]-d[t][1],2)} for t in T]
M={0.0:(0,0.17,0.52,0.64),0.5:(0,0.16,0.53,0.63),1.0:(0,0.12,0.52,0.63),1.5:(0,0.08,0.53,0.64),2.0:(0,0.02,0.51,0.62),
 2.5:(0,0,0.52,0.60),3.0:(0,0,0.50,0.60),3.5:(0,0,0.47,0.60),4.0:(0,0,0.52,0.60),4.5:(0,0,0.53,0.58),5.0:(0,0.07,0.52,0.63),
 5.5:(0,0,0.47,0.73),6.0:(0.01,0.02,0.44,0.76),6.5:(0.04,0.11,0.53,0.76),7.0:(0.06,0.16,0.53,0.76),7.5:(0.05,0.21,0.43,0.75),
 8.0:(0.0,0.23,0.31,0.74),8.5:(0.02,0.32,0.22,0.69)}
W={0.0:(0.54,0.17,1,0.65),0.5:(0.54,0.16,1,0.67),1.0:(0.53,0.13,1,0.63),1.5:(0.54,0.08,1,0.63),2.0:(0.53,0.02,1,0.61),
 2.5:(0.53,0,1,0.61),3.0:(0.51,0,1,0.62),3.5:(0.48,0,1,0.65),4.0:(0.61,0.15,1,0.61),4.5:(0.60,0,1,0.61),5.0:(0.55,0,1,0.64),
 5.5:(0.49,0,1,0.72),6.0:(0.55,0.05,1,0.76),6.5:(0.54,0.13,0.97,0.76),7.0:(0.55,0.19,0.94,0.76),7.5:(0.66,0.23,0.98,0.76),
 8.0:(0.74,0.25,1.0,0.74),8.5:(0.82,0.34,1.0,0.70)}
c={"mediaId":4780,"level":"A","keyWord":"separate","defaultVoice":"female",
"taps":[
 {"phrase":"to wear a dark shirt","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to wear a white blouse","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to have long brown hair","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":9.0,
"nouns":[{"word":"a wall","x":0.50,"y":0.06,"voice":"female"},
 {"word":"rings","x":0.48,"y":0.76,"voice":"female"},
 {"word":"a table","x":0.50,"y":0.92,"voice":"female"}],
"question":"How are they leaving the room?",
"answer":["They","are","leaving","through","separate","doors."],
"answerVoice":"female",
"notes":"Both people do the same actions (sign, take off rings, walk out), so the phrases are states that fit only one of them. Hands of both are close at 3.0-3.5 s (woman puts her ring down near the man's elbow): split at x~0.48-0.51. At 8.5 s both are only partly visible at the edges. Still 9.0 s: two doors, two pens, two papers -> only unique nouns (wall, the two rings together, table). 'They' answer: mixed pair -> defaultVoice."}
json.dump(c,open("content/4780.json","w"),indent=1)
