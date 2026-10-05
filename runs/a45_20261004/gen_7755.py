import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) for t,r in zip(T,rows)]
B=k([(0.17,0.28,0.65,0.72),(0.18,0.29,0.66,0.72),(0.20,0.40,0.67,0.72),(0.27,0.39,0.75,0.72),(0.27,0.38,0.72,0.72),(0.26,0.37,0.73,0.72),(0.25,0.37,0.74,0.75),(0.24,0.35,0.76,0.75)])
L=k([(0.66,0.39,1.0,0.77),(0.67,0.40,1.0,0.77),(0.68,0.39,1.0,0.76),(0.76,0.37,1.0,0.76),(0.73,0.34,1.0,0.73),(0.74,0.33,1.0,0.73),(0.75,0.31,1.0,0.73),(0.77,0.32,1.0,0.73)])
M=k([(0.0,0.47,0.17,0.82),(0.0,0.46,0.17,0.82),(0.0,0.45,0.18,0.82),(0.0,0.44,0.18,0.82),(0.0,0.41,0.18,0.80),(0.0,0.39,0.18,0.80),(0.0,0.39,0.18,0.80),(0.0,0.38,0.18,0.80)])
d={"mediaId":7755,"level":"B","keyWord":"attend","defaultVoice":"female",
 "taps":[{"phrase":"to sketch on the building plans","target":"the woman in the blue blazer","voice":"female","keys":B},
  {"phrase":"to lean over the table","target":"the woman in the lilac cardigan","voice":"female","keys":L},
  {"phrase":"to wear a denim shirt","target":"the man","voice":"male","keys":M}],
 "stillS":2.7,
 "nouns":[{"word":"a houseplant","x":0.67,"y":0.33,"voice":"female"},{"word":"a blazer","x":0.40,"y":0.58,"voice":"female"},
  {"word":"a jug","x":0.72,"y":0.67,"voice":"female"},{"word":"a blueprint","x":0.40,"y":0.78,"voice":"female"}],
 "question":"What is the woman in blue doing?","answer":["She","is","sketching","on","the","building","plans."],"answerVoice":"female",
 "notes":"Man phrase is a state (denim shirt): his only action (hand on the rolled plans) is shared by the woman in lilac. Man box covers his body only, not his long arm reaching into the blazer woman's area; from 2.2 s he is only half in frame at the left edge. She only starts drawing after she sits (~1.2 s); at 0.2-0.7 s she stands raising a pen."}
json.dump(d,open('content/7755.json','w'),indent=1)
