import json
T=[i*0.5 for i in range(19)]
W=[(0.10,0.26,0.90,0.74),(0.08,0.25,0.92,0.75),(0.03,0.25,0.97,0.75),(0.05,0.22,0.95,0.78),(0.08,0.19,0.92,0.81),(0,0,1.0,1.0),
(0,0,0.72,0.60),(0.02,0,0.96,0.78),(0.16,0.19,0.62,0.48),(0.06,0.22,0.60,0.32),(0.12,0.18,0.58,0.40),(0.04,0,0.62,0.63),
(0.10,0.03,0.78,0.74),(0.08,0,0.90,0.97),(0,0.17,0.66,0.83),(0.02,0.07,0.78,0.93),(0.08,0.09,0.70,0.91),(0,0.15,1.0,0.85),(0,0.17,1.0,0.83)]
ks=[{"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} for t,k in zip(T,W)]
taps=[{"phrase":p,"target":"the woman","voice":"female","keys":ks} for p in ["to lean on the barre","to crouch on the floor","to swing her ponytail"]]
c={"mediaId":4946,"level":"B","keyWord":"ponytail","defaultVoice":"female","taps":taps,"stillS":8.0,
"nouns":[{"word":"a mirror","x":0.80,"y":0.25,"voice":"female"},{"word":"a ponytail","x":0.64,"y":0.42,"voice":"female"},{"word":"a hoodie","x":0.30,"y":0.55,"voice":"female"},{"word":"sweatpants","x":0.38,"y":0.88,"voice":"female"}],
"question":"What is the woman wearing?","answer":["She","is","wearing","a","cropped","brown","hoodie."],"answerVoice":"female",
"notes":"Only one real person (a second person's arm grips the near barre at 0-2 s, never a full person; her reflections in the mirror are excluded from the box). All three phrases target the woman. 'barre' is a specialised word; the verifier may prefer 'to lean on the rail'."}
json.dump(c,open('content/4946.json','w'),indent=1)
