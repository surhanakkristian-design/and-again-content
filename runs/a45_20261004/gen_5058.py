import json
T=[i*0.5 for i in range(25)]
BOY={0.0:(0.02,0.19,0.60,0.81),0.5:(0.06,0.13,0.62,0.87),1.0:(0,0.16,0.66,0.84),1.5:(0,0.31,0.67,0.69),2.0:(0,0.34,0.70,0.66),
2.5:(0,0.30,0.71,0.70),3.0:(0,0.22,0.68,0.78),3.5:(0,0.09,0.67,0.91),4.0:(0,0.05,0.68,0.95),
8.0:(0.04,0.26,0.40,0.69),8.5:(0.04,0.25,0.56,0.75),9.0:(0.09,0.23,0.58,0.77),9.5:(0,0.16,0.71,0.84),10.0:(0.01,0.17,0.75,0.83),
10.5:(0,0.15,0.66,0.85),11.0:(0,0.11,0.61,0.89),11.5:(0,0.12,0.64,0.88),12.0:(0,0.11,0.66,0.89)}
PM={4.5:(0.53,0.11,0.47,0.89),5.0:(0.32,0.12,0.68,0.88),5.5:(0.33,0.12,0.67,0.88),6.0:(0.38,0.10,0.62,0.90),
6.5:(0.29,0.10,0.71,0.90),7.0:(0.39,0.11,0.61,0.89),7.5:(0.53,0.10,0.47,0.90)}
def keys(B): return [({"t":t,"x":B[t][0],"y":B[t][1],"w":B[t][2],"h":B[t][3]} if t in B else {"t":t,"off":True}) for t in T]
c={"mediaId":5058,"level":"A","keyWord":"postman","defaultVoice":"male",
"taps":[{"phrase":"to make a sad face","target":"the boy","voice":"male","keys":keys(BOY)},
{"phrase":"to deliver the letters","target":"the postman","voice":"male","keys":keys(PM)},
{"phrase":"to take out the letters","target":"the boy","voice":"male","keys":keys(BOY)}],
"stillS":6.0,
"nouns":[{"word":"a postman","x":0.66,"y":0.25,"voice":"male"},{"word":"a car","x":0.32,"y":0.34,"voice":"male"},
{"word":"a mailbox","x":0.18,"y":0.45,"voice":"male"},{"word":"grass","x":0.40,"y":0.64,"voice":"male"}],
"question":"What is the postman doing?",
"answer":["He","is","putting","letters","in","the","mailbox."],"answerVoice":"male",
"notes":"Boy and postman are never in the same shot (postman 4.5-7.5 s only). Sad face 3.0-4.0 s; letters taken out 10.0-12.0 s. Continuity glitch: the boy already carries a brown parcel at 8.0-9.5 s before he opens the box, so the parcel is not used in any text. 'a car' = the grey car parked behind the mailbox."}
json.dump(c,open('content/5058.json','w'),indent=1)
