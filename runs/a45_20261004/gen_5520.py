import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip('xywh',r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
W=K([(0.0,0.32,0.29,0.64),(0.0,0.32,0.29,0.64),(0.0,0.32,0.31,0.65),(0.0,0.33,0.32,0.64),(0.0,0.31,0.38,0.67),(0.0,0.31,0.40,0.67),(0.02,0.30,0.44,0.69),(0.03,0.30,0.47,0.69)])
M=K([(0.29,0.34,0.31,0.53),(0.29,0.33,0.33,0.54),(0.32,0.35,0.30,0.53),(0.32,0.33,0.33,0.56),(0.38,0.32,0.28,0.58),(0.40,0.32,0.32,0.59),(0.46,0.31,0.30,0.63),(0.50,0.31,0.31,0.64)])
F=K([(0.60,0.50,0.28,0.26),(0.62,0.50,0.27,0.26),(0.62,0.50,0.28,0.26),(0.65,0.51,0.28,0.26),(0.67,0.49,0.29,0.29),(0.72,0.49,0.27,0.29),(0.76,0.50,0.24,0.30),(0.81,0.50,0.19,0.32)])
c={"mediaId":5520,"level":"B","keyWord":"accurate","defaultVoice":"female",
"taps":[{"phrase":"to draw a longbow","target":"the woman","voice":"female","keys":W},
{"phrase":"to look on in surprise","target":"the man","voice":"male","keys":M},
{"phrase":"to burn in an iron basket","target":"the fire","voice":"female","keys":F}],
"stillS":0.7,
"nouns":[{"word":"a breastplate","x":0.17,"y":0.50,"voice":"female"},{"word":"a target","x":0.88,"y":0.42,"voice":"female"},
{"word":"a fire","x":0.72,"y":0.63,"voice":"female"},{"word":"the sky","x":0.60,"y":0.06,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","shooting","arrows","at","a","target."],"answerVoice":"female",
"notes":"Woman and man overlap (her arm crosses him after 2.2 s); boxes split at her torso edge. Key word 'accurate' is an adjective, not used as noun."}
json.dump(c,open('content/5520.json','w'),indent=1)
