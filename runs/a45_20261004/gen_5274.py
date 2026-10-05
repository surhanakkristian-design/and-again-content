import json
T=[round(i*0.5,1) for i in range(25)]
M={0.0:(0.0,0.18,0.50,0.82),0.5:(0.0,0.16,0.74,0.84),1.0:(0.0,0.15,0.86,0.85),1.5:(0.0,0.15,0.87,0.85),
2.0:(0.0,0.15,0.90,0.85),2.5:(0.0,0.12,0.88,0.88),
5.5:(0.0,0.08,0.74,0.70),6.0:(0.0,0.07,0.74,0.71),6.5:(0.0,0.07,0.74,0.71),7.0:(0.0,0.07,0.74,0.71),
7.5:(0.0,0.07,0.75,0.71),8.0:(0.0,0.03,0.76,0.74),8.5:(0.0,0.03,0.76,0.74),
9.0:(0.08,0.21,0.92,0.79),9.5:(0.05,0.21,0.95,0.79),10.0:(0.06,0.21,0.94,0.79),10.5:(0.08,0.21,0.92,0.79),
11.0:(0.08,0.21,0.92,0.79),11.5:(0.05,0.22,0.95,0.78),12.0:(0.08,0.22,0.92,0.78)}
H={0.0:(0.55,0.0,0.27,0.14),0.5:(0.53,0.0,0.28,0.14),1.0:(0.53,0.0,0.28,0.14),1.5:(0.53,0.0,0.28,0.14),
2.0:(0.54,0.0,0.27,0.14),2.5:(0.53,0.0,0.28,0.12),3.0:(0.36,0.06,0.34,0.21),3.5:(0.36,0.06,0.34,0.19),
4.0:(0.35,0.06,0.35,0.19),4.5:(0.35,0.06,0.33,0.19),5.0:(0.35,0.05,0.34,0.20)}
for t in (9.0,9.5,10.0,10.5,11.0,11.5,12.0): H[t]=(0.40,0.0,0.36,0.19)
def keys(D):
    return [({"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} if t in D else {"t":t,"off":True}) for t in T]
c={"mediaId":5274,"level":"B","keyWord":"soaked","defaultVoice":"male",
"taps":[{"phrase":"to test the water temperature","target":"the young man","voice":"male","keys":keys(M)},
{"phrase":"to lather his hair","target":"the young man","voice":"male","keys":keys(M)},
{"phrase":"to spray jets of water","target":"the shower head","voice":"male","keys":keys(H)}],
"stillS":10.0,
"nouns":[{"word":"a shower head","x":0.53,"y":0.07,"voice":"male"},{"word":"tiles","x":0.14,"y":0.16,"voice":"male"},
{"word":"lather","x":0.53,"y":0.29,"voice":"male"},{"word":"a shower hose","x":0.88,"y":0.80,"voice":"male"}],
"question":"What is the young man doing?","answer":["He","is","lathering","his","soaked","hair."],"answerVoice":"male",
"notes":"Only one person, so two phrases on the man + one on the shower head. 3.0-5.0 close-ups of the shower head without the man -> man off; 5.5-8.5 only his face at the left edge and his arm/hand under the stream (box covers face + arm). Shower head off 5.5-8.5 (only the jets visible); before 2.5 it is not spraying yet but is boxed where visible. Shower head box ends at y 0.19 above his foamy hair from 9.0. Key word 'soaked' (adjective) used in the answer."}
json.dump(c,open('content/5274.json','w'),indent=1)
