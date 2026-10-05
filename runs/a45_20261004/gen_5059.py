import json
T=[i*0.5 for i in range(21)]
MAN={0.0:(0.40,0.13,0.60,0.87),0.5:(0.19,0.15,0.81,0.85),1.0:(0.46,0.0,0.54,1.0),1.5:(0.42,0.12,0.58,0.88),2.0:(0.45,0.01,0.55,0.99),
2.5:(0.54,0,0.46,1.0),3.0:(0.71,0.01,0.29,0.99),3.5:(0.66,0.04,0.34,0.96),4.0:(0.54,0.13,0.46,0.87),4.5:(0.48,0.21,0.48,0.25),
7.0:(0.69,0.30,0.31,0.31),7.5:(0.65,0.23,0.35,0.65),8.0:(0.15,0.16,0.85,0.84),8.5:(0.15,0.02,0.85,0.98),9.0:(0.20,0.06,0.80,0.94),
9.5:(0.02,0.10,0.98,0.90),10.0:(0,0.05,1.0,0.95)}
PM={4.5:(0.49,0.46,0.51,0.54),5.0:(0.29,0,0.71,1.0),5.5:(0.19,0,0.81,1.0),6.0:(0.39,0,0.61,1.0),6.5:(0.47,0,0.53,1.0),7.0:(0.46,0.62,0.54,0.38)}
def keys(B): return [({"t":t,"x":B[t][0],"y":B[t][1],"w":B[t][2],"h":B[t][3]} if t in B else {"t":t,"off":True}) for t in T]
c={"mediaId":5059,"level":"A","keyWord":"letter","defaultVoice":"male",
"taps":[{"phrase":"to open the mailbox","target":"the man","voice":"male","keys":keys(MAN)},
{"phrase":"to bring the letters","target":"the postman","voice":"male","keys":keys(PM)},
{"phrase":"to run to the mailbox","target":"the man","voice":"male","keys":keys(MAN)}],
"stillS":10.0,
"nouns":[{"word":"a letter","x":0.20,"y":0.30,"voice":"male"},{"word":"a box","x":0.66,"y":0.69,"voice":"male"},
{"word":"a mailbox","x":0.18,"y":0.76,"voice":"male"},{"word":"a hoodie","x":0.80,"y":0.86,"voice":"male"}],
"question":"What is the man holding?",
"answer":["He","is","holding","a","lot","of","letters."],"answerVoice":"male",
"notes":"Man in the navy hoodie vs postman in the blue jacket. Man opens the box 0.5-1.5 s and again 8.0 s, runs back 7.0-7.5 s. The man is set off at 5.0-6.5 s (only a sliver behind the postman); at 4.5 s and 7.0 s the two boxes are split (man above / postman's stack and arm below). Postman's raised hand at 7.0 s is left out of his box because it overlaps the running man. 'a letter' = the single envelope in his left hand at 10.0 s; the big stack in his arms is not labelled to avoid a second 'letters' slot. 'a box' = the brown parcel."}
json.dump(c,open('content/5059.json','w'),indent=1)
