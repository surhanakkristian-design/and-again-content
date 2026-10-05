import json
O={"off":True}
def r(x0,y0,x1,y1): return {"x":x0,"y":y0,"w":round(x1-x0,2),"h":round(y1-y0,2)}
times=[i*0.5 for i in range(21)]
A={};Wt={};V={t:O for t in times}
def s(t,a,w,v=None):
    A[t]=r(*a);Wt[t]=r(*w)
    if v: V[t]=r(*v)
s(0.0,(0,0.21,0.41,1),(0.54,0.22,1,1),(0,0.04,1,0.21))
s(0.5,(0,0.21,0.43,1),(0.52,0.19,1,1),(0,0.03,1,0.19))
s(1.0,(0,0.22,0.44,1),(0.54,0.26,1,1),(0,0.03,1,0.22))
s(1.5,(0,0.33,0.46,1),(0.54,0.28,1,1),(0,0.03,1,0.28))
s(2.0,(0,0.33,0.48,1),(0.52,0.31,1,1),(0,0.02,1,0.31))
s(2.5,(0,0.30,0.48,1),(0.50,0.25,1,1),(0,0.02,1,0.25))
s(3.0,(0,0.28,0.48,1),(0.55,0.28,1,1),(0,0.03,1,0.28))
s(3.5,(0,0.28,0.47,1),(0.55,0.28,1,1),(0,0.03,1,0.28))
s(4.0,(0,0.28,0.47,1),(0.54,0.28,1,1),(0,0.02,1,0.28))
s(4.5,(0,0.33,0.47,1),(0.53,0.30,1,1),(0,0.02,1,0.30))
s(5.0,(0,0.44,0.50,1),(0.52,0.42,1,1),(0,0.03,1,0.42))
s(5.5,(0.03,0.44,0.49,1),(0.53,0.44,1,1),(0,0.05,1,0.44))
s(6.0,(0.02,0.31,0.49,0.93),(0.53,0.30,1,0.97),(0.08,0.07,0.94,0.30))
s(6.5,(0.07,0.28,0.45,0.78),(0.53,0.31,0.90,0.81),(0.16,0.12,0.88,0.28))
s(7.0,(0.05,0.33,0.48,0.74),(0.60,0.33,0.93,0.74),(0.24,0.19,0.78,0.33))
s(7.5,(0,0.39,0.47,0.95),(0.59,0.39,1,0.98),(0.28,0.25,0.72,0.39))
s(8.0,(0,0.36,0.44,1),(0.63,0.30,1,1),(0.44,0.30,0.63,0.56))
s(8.5,(0,0.20,0.38,1),(0.71,0.20,1,1),(0.39,0.34,0.69,0.57))
s(9.0,(0,0.20,0.38,1),(0.69,0.20,1,1),(0.40,0.38,0.68,0.58))
s(9.5,(0,0.19,0.40,1),(0.58,0.17,1,1),(0.40,0.36,0.58,0.50))
s(10.0,(0,0.19,0.55,1),(0.55,0.19,1,1))
def keys(d): return [dict(t=t,**d[t]) for t in times]
c={"mediaId":592,"level":"A","keyWord":"pushing","defaultVoice":"male",
"taps":[{"phrase":"to have a dark beard","target":"the man in blue","voice":"male","keys":keys(A)},
{"phrase":"to wear a white T-shirt","target":"the man in white","voice":"male","keys":keys(Wt)},
{"phrase":"to roll down the road","target":"the van","voice":"male","keys":keys(V)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":0.35,"y":0.10,"voice":"male"},{"word":"a van","x":0.52,"y":0.42,"voice":"male"},{"word":"a road","x":0.55,"y":0.72,"voice":"male"}],
"question":"What are the two men doing?","answer":["They","are","pushing","a","white","van."],"answerVoice":"male",
"notes":"Both men do exactly the same things (push, laugh, high-five), so no action fits only one of them: the two men get state phrases (beard / white T-shirt), the van the action. The beard is not visible from behind (5.0-7.0, 10.0); the man in blue is still the only other man. In 0.0-5.5 the men stand in front of the van, which fills the picture: the van box is the strip above their heads; at 6.0-7.5 the strip above them; from 8.0 the van between them. At 9.5 only the top of the van shows above their hands (small box, partly sky). At 10.0 the van is hidden: off. Only 3 nouns: houses, shoes and T-shirts each appear twice apart."}
json.dump(c,open('content/592.json','w'),indent=1)
