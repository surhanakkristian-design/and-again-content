import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2]-d[t][0],2),"h":round(d[t][3]-d[t][1],2)} for t in T]
W={0.0:(0.09,0.36,0.67,0.91),0.5:(0.07,0.23,0.80,0.83),1.5:(0.0,0.20,1.0,0.78),2.0:(0.0,0.20,1.0,0.76),
   2.5:(0.80,0.58,1.0,0.82),3.0:(0.80,0.58,1.0,0.82),3.5:(0.10,0.27,0.90,0.50),4.0:(0.05,0.27,0.97,0.50),
   4.5:(0.0,0.20,0.61,1.0),6.0:(0.20,0.35,0.94,0.70),6.5:(0.36,0.35,0.99,0.70),7.0:(0.28,0.34,0.95,0.70),
   7.5:(0.30,0.0,1.0,0.82),8.0:(0.05,0.15,0.93,0.84),8.5:(0.32,0.26,1.0,0.85)}
M={5.0:(0.12,0.26,1.0,1.0),5.5:(0.10,0.26,1.0,1.0),8.5:(0.0,0.45,0.18,0.72)}
C={3.5:(0.24,0.61,0.70,0.88),4.0:(0.24,0.61,0.74,0.86),4.5:(0.62,0.36,0.86,0.50)}
c={"mediaId":4932,"level":"B","keyWord":"to steer","defaultVoice":"female",
 "taps":[
  {"phrase":"to steer through the traffic","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to laugh in the back seat","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to wait at the crossing","target":"the grey car","voice":"female","keys":keys(C)}],
 "stillS":8.0,
 "nouns":[{"word":"a flat cap","x":0.68,"y":0.30,"voice":"female"},
          {"word":"a street sign","x":0.14,"y":0.26,"voice":"female"},
          {"word":"a waistcoat","x":0.62,"y":0.60,"voice":"female"},
          {"word":"a door handle","x":0.28,"y":0.87,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","steering","the","taxi","through","the","traffic."],
 "answerVoice":"female",
 "notes":"Description misses the laughing male passenger (5.0-5.5, faint behind her at 6.0 = off, back window at 8.5). Woman at 3.5/4.0 = her reflection in the rear-view mirror; 2.5/3.0 = only her hand on the wheel. Hand patting the taxi sign at 1.0 left off (owner unclear). 7.5: blurred raised hand in front of her, box covers both."}
json.dump(c,open('content/4932.json','w'),indent=1)
