import json
T=[0.2,0.7,1.2,1.7]
def K(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
man=K([(0.00,0.16,0.43,0.68),(0.00,0.15,0.43,0.72),(0.00,0.14,0.43,0.76),(0.00,0.13,0.43,0.78)])
wom=K([(0.44,0.36,0.56,0.32),(0.44,0.36,0.56,0.32),(0.44,0.36,0.56,0.34),(0.44,0.36,0.56,0.33)])
dog=K([(0.60,0.69,0.40,0.27),(0.60,0.69,0.40,0.28),(0.50,0.71,0.50,0.29),(0.55,0.70,0.45,0.30)])
c={"mediaId":5621,"level":"B","keyWord":"be in trouble","defaultVoice":"male",
"taps":[{"phrase":"to tiptoe in his socks","target":"the man","voice":"male","keys":man},
{"phrase":"to sit with folded arms","target":"the woman","voice":"female","keys":wom},
{"phrase":"to sit beside the armchair","target":"the dog","voice":"male","keys":dog}],
"stillS":0.7,
"nouns":[{"word":"framed prints","x":0.48,"y":0.28,"voice":"male"},{"word":"a floor lamp","x":0.77,"y":0.38,"voice":"male"},
{"word":"shoes","x":0.10,"y":0.60,"voice":"male"},{"word":"a rug","x":0.30,"y":0.93,"voice":"male"}],
"question":"What is the woman doing?",
"answer":["She","is","sitting","with","folded","arms."],"answerVoice":"female",
"notes":"woman's lower legs/socks fall partly in the dog's box (split at y ~0.69); defaultVoice male = the man is the main person (walking subject)."}
json.dump(c,open('content/5621.json','w'),indent=1)
