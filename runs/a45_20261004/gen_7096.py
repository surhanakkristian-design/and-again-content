import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
woman=K([(0.50,0.39,0.19,0.15),(0.51,0.39,0.18,0.15),(0.51,0.39,0.18,0.15),(0.51,0.39,0.18,0.15),(0.51,0.37,0.19,0.16),(0.53,0.37,0.19,0.17),(0.51,0.37,0.20,0.17),(0.52,0.37,0.21,0.18)])
man=K([(0.28,0.39,0.22,0.16),(0.29,0.39,0.22,0.16),(0.27,0.39,0.23,0.16),(0.27,0.39,0.23,0.17),(0.25,0.37,0.25,0.19),(0.27,0.37,0.26,0.19),(0.24,0.36,0.26,0.20),(0.26,0.36,0.26,0.21)])
c={"mediaId":7096,"level":"A","keyWord":"fail an exam","defaultVoice":"female",
"taps":[{"phrase":"to cover her face","target":"the woman","voice":"female","keys":woman},
{"phrase":"to sit at the wheel","target":"the woman","voice":"female","keys":woman},
{"phrase":"to hold a paper","target":"the man","voice":"male","keys":man}],
"stillS":2.7,
"nouns":[{"word":"houses","x":0.80,"y":0.15,"voice":"female"},{"word":"a fountain","x":0.50,"y":0.24,"voice":"female"},
{"word":"a paper","x":0.37,"y":0.52,"voice":"female"},{"word":"a car","x":0.50,"y":0.66,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","covering","her","face."],"answerVoice":"female",
"notes":"Woman covers her face 0.2-2.2 s, then lowers her hands and stares ahead (answer describes the first half). Both people sit inside the car, so the car is not a tap target (its box would contain theirs). The two boxes meet at x ~0.51 between the seats. 'a paper' = the sheet with the red cross the man holds. Key word 'fail an exam' is not a visible noun."}
json.dump(c,open('content/7096.json','w'),indent=1)
