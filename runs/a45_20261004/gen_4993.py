import json
B=[(0.0,0.21,1.0,0.62),(0.10,0.22,0.90,0.60),(0.02,0.25,0.98,0.55),(0.12,0.30,0.78,0.48),(0.13,0.37,0.62,0.32),
(0.30,0.42,0.40,0.22),(0.37,0.46,0.26,0.18),(0.39,0.46,0.24,0.17),(0.39,0.48,0.24,0.15),(0.39,0.48,0.24,0.15),
(0.39,0.49,0.22,0.15),(0.41,0.50,0.20,0.14),(0.40,0.49,0.20,0.14),(0.39,0.45,0.19,0.14),(0.41,0.45,0.18,0.14),
(0.42,0.45,0.18,0.14),(0.42,0.44,0.18,0.14),(0.42,0.44,0.18,0.14),(0.41,0.44,0.18,0.14),(0.42,0.44,0.18,0.14),
(0.41,0.43,0.18,0.14),(0.41,0.43,0.18,0.14),(0.41,0.43,0.18,0.14),(0.41,0.43,0.18,0.14),(0.41,0.43,0.18,0.14)]
keys=[dict(t=i*0.5,x=x,y=y,w=w,h=h) for i,(x,y,w,h) in enumerate(B)]
d={"mediaId":4993,"level":"A","keyWord":"alone","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to paddle a red boat","to step onto a rock","to stand next to a tree"]],
"stillS":12.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"female"},
{"word":"a tree","x":0.58,"y":0.38,"voice":"female"},
{"word":"a boat","x":0.37,"y":0.56,"voice":"female"},
{"word":"a lake","x":0.50,"y":0.80,"voice":"female"}],
"question":"Where is the woman standing?","answer":["She","is","standing","next","to","a","tree."],"answerVoice":"female",
"notes":"Description says she is the only person, but 0.0-2.5 show a crowded beach in the background; phrases are unique to her anyway. From 5.5 on she is tiny (min-size boxes). Boat = red canoe; 'boat' chosen as A-level word. Key word 'alone' is an adjective, not a noun."}
json.dump(d,open("content/4993.json","w"),indent=1)
