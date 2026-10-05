import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
M={0.0:(0,0.22,0.64,0.78),0.5:(0,0.22,0.66,0.78),1.0:(0,0.22,0.66,0.78),1.5:(0,0.22,0.69,0.78),2.0:(0,0.22,0.69,0.78),
 2.5:(0,0.12,0.74,0.88),3.0:(0,0.13,0.72,0.87),3.5:(0,0.13,0.72,0.87),4.0:(0,0.12,0.69,0.88),4.5:(0,0.12,0.72,0.88),
 5.0:(0,0.14,0.72,0.86),5.5:(0,0.14,0.74,0.86),6.0:(0,0.15,0.69,0.85),6.5:(0,0.15,0.70,0.85),7.0:(0,0.15,0.76,0.85),
 7.5:(0,0,0.86,1.0),8.0:(0,0,0.74,1.0),8.5:(0,0.02,0.82,0.98),9.0:(0,0.08,1.0,0.92),9.5:(0,0.06,1.0,0.94),10.0:(0,0.03,1.0,0.97)}
N={0.0:(0.65,0.04,0.35,0.92),0.5:(0.67,0.04,0.33,0.92),1.0:(0.68,0.04,0.32,0.92),1.5:(0.70,0.04,0.30,0.92),2.0:(0.71,0.06,0.29,0.92),
 2.5:(0.76,0.0,0.24,0.82),3.0:(0.74,0.0,0.26,0.78),3.5:(0.74,0.0,0.26,0.80),4.0:(0.70,0.0,0.30,0.82),4.5:(0.73,0.0,0.27,0.80),
 5.0:(0.74,0.0,0.26,0.78),5.5:(0.76,0.0,0.24,0.75),6.0:(0.70,0.0,0.30,0.75),6.5:(0.72,0.48,0.28,0.26)}
c={"mediaId":5451,"level":"B","keyWord":"injection","defaultVoice":"male",
"taps":[{"phrase":"to hold up a vial","target":"the nurse","voice":"female","keys":keys(N)},
{"phrase":"to give an injection","target":"the nurse","voice":"female","keys":keys(N)},
{"phrase":"to flex his bicep proudly","target":"the young man","voice":"male","keys":keys(M)}],
"stillS":3.5,
"nouns":[{"word":"patients","x":0.56,"y":0.30,"voice":"male"},{"word":"a syringe","x":0.73,"y":0.57,"voice":"male"},
{"word":"a green T-shirt","x":0.24,"y":0.76,"voice":"male"}],
"question":"What is the nurse doing?","answer":["She","is","giving","him","an","injection."],"answerVoice":"female",
"notes":"Nurse and man overlap (her arm crosses his arm during the injection); boxes split at x~0.65-0.76, so the nurse's hands on his arm fall in the man's box. 'patients' = the people waiting in the background (description calls them patients)."}
json.dump(c,open('content/5451.json','w'),indent=1)
