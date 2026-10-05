import json
B=[(0.0,0.0,0.08,0.96,0.92),(0.5,0.07,0.09,0.92,0.91),(1.0,0.0,0.06,0.92,0.94),(1.5,0.05,0.10,0.78,0.90),
(2.0,0.03,0.09,0.70,0.91),(2.5,0.03,0.07,0.78,0.93),(3.0,0.0,0.10,0.87,0.90),(3.5,0.12,0.10,0.84,0.90),
(4.0,0.0,0.11,0.60,0.89),(4.5,0.03,0.09,0.72,0.91),(5.0,0.0,0.13,0.80,0.87),(5.5,0.06,0.11,0.94,0.89),
(6.0,0.0,0.11,0.82,0.89),(6.5,0.0,0.14,0.74,0.86),(7.0,0.03,0.10,0.74,0.90),(7.5,0.0,0.09,0.75,0.91),
(8.0,0.08,0.14,0.88,0.86),(8.5,0.03,0.13,0.82,0.87),(9.0,0.05,0.13,0.93,0.87),(9.5,0.0,0.11,0.97,0.89),
(10.0,0.0,0.17,0.87,0.83),(10.5,0.0,0.11,0.72,0.89),(11.0,0.03,0.11,0.86,0.89),(11.5,0.13,0.13,0.85,0.87),
(12.0,0.0,0.13,0.84,0.87)]
keys=[dict(t=t,x=x,y=y,w=w,h=h) for t,x,y,w,h in B]
d={"mediaId":4990,"level":"A","keyWord":"iron","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to iron a shirt","to fold a shirt","to put clothes on a pile"]],
"stillS":4.0,
"nouns":[{"word":"a washing machine","x":0.72,"y":0.28,"voice":"male"},
{"word":"clothes","x":0.80,"y":0.52,"voice":"male"},
{"word":"an iron","x":0.38,"y":0.66,"voice":"male"},
{"word":"an ironing board","x":0.40,"y":0.80,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","ironing","a","shirt."],"answerVoice":"male",
"notes":"Only one person, so all three phrases target the man. Iron visible at 4.0 under his hand."}
json.dump(d,open("content/4990.json","w"),indent=1)
