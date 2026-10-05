import json
K=[(0,0.45,0.42,0.55),(0,0.47,0.36,0.53),(0,0.50,0.30,0.50),(0,0.48,0.38,0.52),(0,0.47,0.44,0.53),(0,0.48,0.36,0.52),
(0,0.52,0.26,0.48),(0,0.51,0.26,0.49),(0,0.47,0.36,0.53),(0,0.47,0.38,0.53),(0,0.49,0.33,0.51),(0,0.51,0.31,0.49),(0,0.49,0.34,0.51)]
keys=[dict(t=i*0.5,x=x,y=y,w=w,h=h) for i,(x,y,w,h) in enumerate(K)]
d={"mediaId":4828,"level":"A","keyWord":"wall","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to paint the wall green","to hold a long roller","to wear a green T-shirt"]],
"stillS":3.0,
"nouns":[{"word":"a wall","x":0.35,"y":0.30,"voice":"male"},{"word":"a man","x":0.12,"y":0.66,"voice":"male"},
{"word":"a roller","x":0.52,"y":0.84,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","painting","the","wall","green."],"answerVoice":"male",
"notes":"Only one person, so all three phrases share the man. Box covers his body and the hand on the roller handle, not the roller head. 'a roller' is slightly above A level but is the clearest object; pill on the roller head at the bottom of the green paint at 3.0 s."}
json.dump(d,open("content/4828.json","w"),indent=1)
