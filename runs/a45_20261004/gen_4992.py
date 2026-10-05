import json
B=[(0.10,0.22,0.80,0.78),(0.08,0.22,0.86,0.78),(0.08,0.23,0.90,0.77),(0.05,0.21,0.95,0.79),(0.01,0.20,0.93,0.80),
(0.36,0.31,0.64,0.69),(0.37,0.31,0.63,0.69),(0.36,0.33,0.64,0.67),(0.53,0.27,0.47,0.73),(0.58,0.17,0.42,0.83),
(0.50,0.03,0.50,0.97),(0.62,0.0,0.38,0.98),(0.55,0.0,0.45,0.82),(0.33,0.0,0.67,0.78),(0.38,0.0,0.62,0.90),
(0.21,0.26,0.70,0.74),(0.20,0.27,0.80,0.73),(0.18,0.26,0.80,0.74),(0.10,0.27,0.82,0.73),(0.14,0.25,0.82,0.75),
(0.22,0.24,0.74,0.76),(0.12,0.24,0.88,0.76),(0.08,0.25,0.86,0.75),(0.08,0.25,0.92,0.75),(0.15,0.24,0.80,0.76)]
keys=[dict(t=i*0.5,x=x,y=y,w=w,h=h) for i,(x,y,w,h) in enumerate(B)]
d={"mediaId":4992,"level":"A","keyWord":"busy","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to carry a lot of clothes","to open a cupboard","to hold up a blue shirt"]],
"stillS":12.0,
"nouns":[{"word":"a window","x":0.78,"y":0.25,"voice":"female"},
{"word":"a woman","x":0.50,"y":0.48,"voice":"female"},
{"word":"an iron","x":0.12,"y":0.70,"voice":"female"},
{"word":"a shirt","x":0.55,"y":0.88,"voice":"female"}],
"question":"What is the woman carrying?","answer":["She","is","carrying","a","lot","of","clothes."],"answerVoice":"female",
"notes":"Only one person, so all three phrases target the woman (6.0-7.0 she is only partly visible behind the board). Key word 'busy' is an adjective. Shirt at 10.5 is pale blue."}
json.dump(d,open("content/4992.json","w"),indent=1)
