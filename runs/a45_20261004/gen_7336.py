import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def same(b): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t in T]
man=same((0.30,0.38,0.50,0.40)); old=same((0.81,0.26,0.19,0.19))
c={"mediaId":7336,"level":"B","keyWord":"marina","defaultVoice":"male",
"taps":[
 {"phrase":"to paddle with an oar","target":"the man in sunglasses","voice":"male","keys":man},
 {"phrase":"to balance a breakfast tray","target":"the man in sunglasses","voice":"male","keys":man},
 {"phrase":"to lean over the railing","target":"the older man","voice":"male","keys":old}],
"stillS":2.2,
"nouns":[{"word":"a yacht","x":0.15,"y":0.27,"voice":"male"},{"word":"a jetty","x":0.52,"y":0.37,"voice":"male"},
 {"word":"a tray","x":0.68,"y":0.48,"voice":"male"},{"word":"an oar","x":0.22,"y":0.685,"voice":"male"}],
"question":"What is the man in sunglasses doing?",
"answer":["He","is","paddling","across","the","marina."],"answerVoice":"male",
"notes":"marina is the whole scene, so it is in the answer, not a noun pill. Dog (walks along the jetty) skipped as a target: its box overlaps the main man's head/shoulder box in early frames. Flamingo is an inflatable, not labelled."}
json.dump(c,open('content/7336.json','w'),indent=1)
