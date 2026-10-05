import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
W=K([(0.00,0.25,0.53,0.40),(0.08,0.25,0.48,0.42),(0.00,0.24,0.56,0.42),(0.00,0.23,0.55,0.43),
     (0.00,0.22,0.54,0.44),(0.00,0.21,0.55,0.45),(0.00,0.18,0.55,0.48),(0.00,0.16,0.55,0.50)])
Y=K([(0.53,0.23,0.35,0.24),(0.61,0.24,0.24,0.23),(0.60,0.23,0.25,0.24),(0.62,0.23,0.23,0.22),
     (0.55,0.15,0.36,0.29),(0.56,0.10,0.40,0.33),(0.56,0.08,0.41,0.33),(0.56,0.06,0.44,0.35)])
M=K([(0.57,0.47,0.43,0.33),(0.60,0.47,0.40,0.36),(0.57,0.47,0.43,0.36),(0.59,0.45,0.41,0.39),
     (0.57,0.44,0.43,0.42),(0.58,0.44,0.42,0.44),(0.58,0.42,0.42,0.48),(0.58,0.42,0.42,0.52)])
c={"mediaId":7950,"level":"B","keyWord":"preserve","defaultVoice":"female",
 "taps":[{"phrase":"to lean over the dome","target":"the woman in white","voice":"female","keys":W},
  {"phrase":"to cheer with raised arms","target":"the woman in yellow","voice":"female","keys":Y},
  {"phrase":"to peer into the dome","target":"the man","voice":"male","keys":M}],
 "stillS":2.7,
 "nouns":[{"word":"the sky","x":0.40,"y":0.06,"voice":"female"},
  {"word":"a sandcastle","x":0.50,"y":0.66,"voice":"female"},
  {"word":"foam","x":0.45,"y":0.88,"voice":"female"}],
 "question":"What is the woman in yellow doing?",
 "answer":["She","is","cheering","with","raised","arms."],
 "answerVoice":"female",
 "notes":"key word 'preserve' is a verb, not placed; yellow woman's legs are behind the man's head, her box stops above his head; yellow woman's arms are down 0.7-1.7 but she is still the cheering one; the man's hands rest on the sand at the dome's base."}
json.dump(c,open("content/7950.json","w"),indent=1)
