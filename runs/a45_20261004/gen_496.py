import json
T=[i*0.5 for i in range(21)]
W={0.0:(0,0,1,0.60),0.5:(0,0,1,0.62),1.0:(0,0.15,1,0.72),1.5:(0,0,0.68,1),2.0:(0,0.03,0.69,0.97),2.5:(0,0.08,0.75,0.92),
 3.0:(0,0.14,0.70,0.86),3.5:(0,0.14,0.68,0.86),4.0:(0,0.16,0.68,0.84),4.5:(0,0.16,0.67,0.84),5.0:(0,0.20,0.66,0.80),5.5:(0,0.20,0.73,0.80),
 6.0:(0,0.18,0.74,0.82),6.5:(0,0.16,0.70,0.84),7.0:(0,0.16,0.70,0.84),7.5:(0,0.16,0.73,0.84),8.0:(0,0.16,0.76,0.84),8.5:(0,0.16,0.78,0.84),
 9.0:(0,0.18,0.75,0.82),9.5:(0,0.21,0.59,0.79),10.0:(0,0.23,0.60,0.70)}
B={1.0:(0.58,0,0.42,0.14),1.5:(0.70,0,0.30,0.21),2.0:(0.70,0,0.30,0.42),2.5:(0.76,0,0.24,0.40),3.0:(0.72,0,0.28,0.38),3.5:(0.70,0,0.30,0.40),
 4.0:(0.70,0.02,0.30,0.44),4.5:(0.69,0.03,0.31,0.44),5.0:(0.68,0.06,0.32,0.42),5.5:(0.75,0.06,0.25,0.44),6.0:(0.76,0.08,0.24,0.66),
 6.5:(0.72,0.22,0.28,0.32),7.0:(0.72,0.20,0.28,0.38),7.5:(0.75,0.25,0.25,0.28),8.0:(0.78,0.18,0.22,0.36),8.5:(0.80,0.20,0.20,0.40),
 9.0:(0.77,0.18,0.23,0.74),9.5:(0.60,0.15,0.40,0.50),10.0:(0.62,0.15,0.38,0.52)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":496,"level":"A","keyWord":"necklace","defaultVoice":"female",
"taps":[{"phrase":"to put on a necklace","target":"the woman in white","voice":"female","keys":keys(W)},
{"phrase":"to stand behind her friend","target":"the woman in brown","voice":"female","keys":keys(B)},
{"phrase":"to wear a white shirt","target":"the woman in white","voice":"female","keys":keys(W)}],
"stillS":7.5,
"nouns":[{"word":"a necklace","x":0.42,"y":0.65,"voice":"female"},{"word":"a mirror","x":0.78,"y":0.56,"voice":"female"},
{"word":"flowers","x":0.60,"y":0.15,"voice":"female"},{"word":"a shirt","x":0.45,"y":0.85,"voice":"female"}],
"question":"What is the woman in white wearing?",
"answer":["She","is","wearing","a","colourful","necklace."],"answerVoice":"female",
"notes":"Only two people are visible (the packet says 'friends'). The woman in brown stands behind and partly overlaps the woman in white in every frame from 1.0 s: split vertically at the edge of the white woman's head, so the right shoulder / sleeve of the white shirt is often outside her box; at 1.0 s split horizontally (the brown woman is only a mouth and shoulder at the top). At 9.5 and 10.0 the brown woman's left hand rests on the white woman's far shoulder and lies in the white box. The brown woman is only a strip of brown top at the right edge at 6.5-8.5. 0.0-0.5 s: close-up of hands and necklace, taken as the woman in white. Third phrase is a state (no second action fits only her for long; she holds the mirror only at 7.5-8.0). 'a necklace' and 'a shirt' are both on the woman in white but far apart on a large figure."}
json.dump(c,open("content/496.json","w"),indent=1)
