import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
man=K([(0.34,0.11,0.27,0.72),(0.33,0.11,0.28,0.73),(0.31,0.10,0.29,0.76),(0.30,0.10,0.31,0.79),
       (0.21,0.09,0.39,0.80),(0.20,0.09,0.40,0.82),(0.20,0.08,0.41,0.84),(0.18,0.06,0.47,0.87)])
pen=K([(0.62,0.50,0.21,0.37),(0.62,0.50,0.21,0.38),(0.61,0.51,0.22,0.39),(0.62,0.52,0.21,0.40),
       (0.61,0.52,0.21,0.40),(0.61,0.51,0.22,0.41),(0.62,0.52,0.22,0.41),(0.65,0.52,0.22,0.43)])
d={"mediaId":7302,"level":"A","keyWord":"lock the door","defaultVoice":"male",
 "taps":[
  {"phrase":"to lock the door","target":"the man at the door","voice":"male","keys":man},
  {"phrase":"to turn around","target":"the man at the door","voice":"male","keys":man},
  {"phrase":"to look up","target":"the penguin by the door","voice":"male","keys":pen}],
 "stillS":0.2,
 "nouns":[{"word":"a lamp","x":0.60,"y":0.07,"voice":"male"},
  {"word":"a door","x":0.85,"y":0.25,"voice":"male"},
  {"word":"penguins","x":0.22,"y":0.50,"voice":"male"},
  {"word":"boots","x":0.48,"y":0.76,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["The","man","is","locking","the","green","door."],
 "answerVoice":"male",
 "notes":"Man box split vertically from the penguin by the door (his hands at the lock lie outside his box where they would overlap the penguin column). 'to turn around' = he turns towards the penguins at 3.2-3.7. Keeper with wheelbarrow only visible at 0.2-0.7, not used."}
json.dump(d,open('content/7302.json','w'),indent=1)
