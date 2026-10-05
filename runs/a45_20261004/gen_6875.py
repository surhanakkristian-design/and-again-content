import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip("xywh",r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=K([(0.27,0.34,0.44,0.47),(0.22,0.32,0.50,0.49),(0.18,0.29,0.53,0.50),(0.13,0.25,0.59,0.56),
         (0.03,0.22,0.70,0.70),(0.0,0.19,0.74,0.79),(0.0,0.14,0.74,0.86),(0.0,0.12,0.74,0.88)])
man=K([(0.72,0.34,0.28,0.44),(0.72,0.32,0.28,0.48),(0.71,0.30,0.29,0.52),(0.72,0.25,0.28,0.57),
       (0.73,0.20,0.27,0.72),(0.74,0.18,0.26,0.78),(0.74,0.14,0.26,0.84),(0.74,0.13,0.26,0.85)])
climber=K([(0.0,0.36,0.26,0.29),(0.0,0.36,0.21,0.28),(0.0,0.34,0.17,0.30),(0.0,0.32,0.12,0.30),None,None,None,None])
d={"mediaId":6875,"level":"B","keyWord":"blood pressure","defaultVoice":"female",
 "taps":[{"phrase":"to check his blood pressure","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to stretch out his arm","target":"the young man","voice":"male","keys":man},
         {"phrase":"to crouch in the doorway","target":"the climber","voice":"female","keys":climber}],
 "stillS":0.2,
 "nouns":[{"word":"a lantern","x":0.58,"y":0.18,"voice":"female"},
          {"word":"a gas bottle","x":0.37,"y":0.82,"voice":"female"},
          {"word":"an emergency blanket","x":0.78,"y":0.72,"voice":"female"},
          {"word":"an ice axe","x":0.72,"y":0.91,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","checking","his","blood","pressure."],
 "answerVoice":"female",
 "notes":"The young man's outstretched forearm lies across the woman's area; his box is cut at the cuff (x ~0.72) so his hand/forearm falls in her box. Climber only visible 0.2-1.7, at 1.7 just a sliver at the left edge (box narrower than 0.18 to avoid the woman). Climber gender unclear (hood), default voice."}
json.dump(d,open("content/6875.json","w"),indent=1)
