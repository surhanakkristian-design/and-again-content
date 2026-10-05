import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
W=[(0.52,0.27,0.35,0.48),(0.10,0.26,0.61,0.49),(0.15,0.27,0.51,0.49),(0.10,0.26,0.60,0.50),(0.03,0.26,0.67,0.57),(0.01,0.25,0.71,0.64),(0.0,0.25,0.70,0.74),(0.03,0.24,0.79,0.76)]
C=[None,(0.71,0.21,0.26,0.53),(0.66,0.21,0.30,0.52),(0.70,0.20,0.29,0.52),(0.70,0.18,0.30,0.56),(0.72,0.18,0.28,0.25),(0.70,0.17,0.30,0.34),(0.82,0.15,0.18,0.42)]
wk=[k(t,b) for t,b in zip(T,W)]; ck=[k(t,b) for t,b in zip(T,C)]
d={"mediaId":7340,"level":"B","keyWord":"mate","defaultVoice":"female",
"taps":[{"phrase":"to lean over the railing","target":"the woman","voice":"female","keys":wk},
{"phrase":"to point at the tugboat","target":"the woman","voice":"female","keys":wk},
{"phrase":"to wear a peaked cap","target":"the captain","voice":"male","keys":ck}],
"stillS":2.2,
"nouns":[{"word":"a crane","x":0.36,"y":0.20,"voice":"female"},{"word":"a peaked cap","x":0.82,"y":0.25,"voice":"female"},
{"word":"a tugboat","x":0.22,"y":0.67,"voice":"female"},{"word":"a thermos flask","x":0.77,"y":0.76,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","speaking","into","a","walkie-talkie."],"answerVoice":"female",
"notes":"Captain hidden behind the woman at 0.2 (only cap top + one shoulder) -> off. Woman/captain boxes split along a vertical line; at 2.7-3.7 captain box only covers his upper body because the woman's back covers the rest. Tugboat not used as tap target: woman's pointing arm lies over it. Key word 'mate' is not a separate visible noun (she is the mate)."}
json.dump(d,open('content/7340.json','w'),indent=1)
