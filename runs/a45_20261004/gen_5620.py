import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
man=K([(0.43,0.28,0.40,0.72),(0.08,0.28,0.40,0.72),(0.59,0.30,0.28,0.65),(0.61,0.25,0.39,0.75),(0.51,0.22,0.49,0.78),(0.53,0.15,0.47,0.85),(0.51,0.10,0.49,0.90),(0.49,0.02,0.51,0.60)])
wom=K([(0.00,0.24,0.42,0.63),(0.49,0.26,0.51,0.65),(0.03,0.24,0.55,0.76),(0.08,0.25,0.52,0.75),(0.00,0.34,0.50,0.66),(0.00,0.27,0.52,0.73),(0.00,0.24,0.50,0.76),(0.00,0.20,0.48,0.80)])
c={"mediaId":5620,"level":"A","keyWord":"be in love with","defaultVoice":"female",
"taps":[{"phrase":"to lift her up","target":"the man","voice":"male","keys":man},
{"phrase":"to touch his face","target":"the woman","voice":"female","keys":wom},
{"phrase":"to wear a red coat","target":"the woman","voice":"female","keys":wom}],
"stillS":1.7,
"nouns":[{"word":"a sign","x":0.80,"y":0.06,"voice":"female"},{"word":"a shop window","x":0.14,"y":0.52,"voice":"female"},
{"word":"a red coat","x":0.28,"y":0.82,"voice":"female"},{"word":"a man","x":0.80,"y":0.62,"voice":"male"}],
"question":"What is the woman wearing?",
"answer":["She","is","wearing","a","red","coat."],"answerVoice":"female",
"notes":"the couple overlap almost everywhere; boxes split along the line between them, so parts of her arms / his body fall in the other box. Description says he holds her face, but in the frames SHE holds HIS face (2.2-3.7). Only two targets."}
json.dump(c,open('content/5620.json','w'),indent=1)
