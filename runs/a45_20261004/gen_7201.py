import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(d): return [dict(t=t,**d[t]) if t in d else {"t":t,"off":True} for t in T]
guru=K({0.2:dict(x=.10,y=.12,w=.90,h=.88),0.7:dict(x=.09,y=.10,w=.91,h=.90),1.2:dict(x=.04,y=.10,w=.96,h=.90),
 1.7:dict(x=.05,y=.10,w=.95,h=.90),2.2:dict(x=.02,y=.07,w=.98,h=.93),2.7:dict(x=.02,y=.06,w=.98,h=.94),
 3.2:dict(x=.48,y=.48,w=.44,h=.31),3.7:dict(x=.48,y=.48,w=.46,h=.31)})
bell=K({3.2:dict(x=.56,y=.33,w=.18,h=.14),3.7:dict(x=.58,y=.33,w=.18,h=.14)})
pot=K({3.2:dict(x=.51,y=.79,w=.18,h=.14),3.7:dict(x=.51,y=.79,w=.18,h=.14)})
c={"mediaId":7201,"level":"B","keyWord":"guru","defaultVoice":"male",
 "taps":[{"phrase":"to hold up a dry leaf","target":"the old man","voice":"male","keys":guru},
  {"phrase":"to hang from a branch","target":"the bell","voice":"male","keys":bell},
  {"phrase":"to stand on the dusty ground","target":"the brass pot","voice":"male","keys":pot}],
 "stillS":3.7,
 "nouns":[{"word":"roots","x":.25,"y":.20,"voice":"male"},{"word":"a bell","x":.66,"y":.40,"voice":"male"},
  {"word":"a guru","x":.82,"y":.62,"voice":"male"},{"word":"a brass pot","x":.60,"y":.86,"voice":"male"}],
 "question":"What is the guru holding up?","answer":["He","is","holding","up","a","dry","leaf."],"answerVoice":"male",
 "notes":"Bell and brass pot only in the wide shot (3.2-3.7 s). Old man box cut at y .79 where the pot stands in front of his knee. 'roots' = hanging banyan roots, top left."}
json.dump(c,open('content/7201.json','w'),indent=1)
