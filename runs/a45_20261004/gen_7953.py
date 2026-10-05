import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [ ({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}) for t,b in zip(T,l)]
man=K([(0.31,0.06,0.69,0.94),(0.29,0.10,0.71,0.90),(0.24,0.16,0.66,0.84),(0.20,0.20,0.66,0.80),(0.12,0.22,0.64,0.78),(0.12,0.24,0.57,0.76),(0.11,0.26,0.47,0.74),(0.11,0.26,0.47,0.66)])
wom=K([None,None,(0.90,0.42,0.10,0.28),(0.86,0.40,0.14,0.30),(0.76,0.42,0.24,0.26),(0.69,0.39,0.19,0.28),(0.58,0.40,0.21,0.27),(0.58,0.40,0.20,0.27)])
c={"mediaId":7953,"level":"B","keyWord":"public holiday","defaultVoice":"male",
"taps":[{"phrase":"to tug at a locked door","target":"the man","voice":"male","keys":man},
{"phrase":"to twirl in a red skirt","target":"the woman","voice":"female","keys":wom},
{"phrase":"to carry a black briefcase","target":"the man","voice":"male","keys":man}],
"stillS":2.2,
"nouns":[{"word":"a briefcase","x":0.28,"y":0.59,"voice":"male"},{"word":"bunting","x":0.78,"y":0.33,"voice":"male"},{"word":"a skirt","x":0.84,"y":0.57,"voice":"male"},{"word":"the sky","x":0.68,"y":0.12,"voice":"male"}],
"question":"What is the businessman doing?",
"answer":["He","is","tugging","at","a","locked","door."],"answerVoice":"male",
"notes":"woman is cut at the right edge at 1.2/1.7 (narrow boxes); boxes of man and woman split along the line between them from 2.2 on (his flying tie reaches into her area). Frisbee man and cyclist left out (too small, overlap the woman)."}
json.dump(c,open('content/7953.json','w'),indent=1)
