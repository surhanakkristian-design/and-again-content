import json
def b(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
times=[i*0.5 for i in range(20)]
R={0.0:b(0.28,0.40,0.38,0.36),0.5:b(0.29,0.38,0.37,0.38),1.0:b(0.27,0.39,0.38,0.36),1.5:b(0.21,0.22,0.43,0.51),2.0:b(0.12,0.24,0.49,0.50),2.5:b(0.18,0.26,0.43,0.49),
3.0:b(0.16,0.26,0.44,0.50),3.5:b(0.25,0.22,0.36,0.54),4.0:b(0.18,0.45,0.48,0.37),4.5:b(0.17,0.49,0.57,0.33),5.0:b(0.27,0.48,0.47,0.31),5.5:b(0.38,0.48,0.37,0.32),
6.0:b(0.26,0.45,0.42,0.33),6.5:b(0.22,0.46,0.52,0.31),7.0:b(0.26,0.48,0.47,0.30),7.5:b(0.29,0.47,0.39,0.30),8.0:b(0.28,0.40,0.38,0.35),8.5:b(0.28,0.35,0.37,0.39),9.0:b(0.28,0.33,0.38,0.42),9.5:b(0.28,0.33,0.37,0.42)}
G={0.0:b(0.67,0.50,0.22,0.20),0.5:b(0.67,0.49,0.22,0.21),1.0:b(0.66,0.49,0.23,0.22),1.5:b(0.65,0.49,0.22,0.21),2.0:b(0.62,0.52,0.25,0.20),2.5:b(0.62,0.53,0.25,0.19),
3.0:b(0.61,0.55,0.25,0.19),3.5:b(0.62,0.56,0.25,0.19),4.0:b(0.67,0.56,0.20,0.19),4.5:b(0.75,0.55,0.18,0.19),5.0:b(0.75,0.53,0.18,0.17),5.5:b(0.76,0.52,0.18,0.19),
6.0:b(0.69,0.52,0.20,0.21),6.5:b(0.75,0.56,0.18,0.16),7.0:b(0.74,0.54,0.18,0.18),7.5:b(0.69,0.53,0.20,0.18),8.0:b(0.67,0.52,0.21,0.18),8.5:b(0.66,0.52,0.21,0.18),9.0:b(0.67,0.52,0.21,0.18),9.5:b(0.66,0.52,0.22,0.18)}
B={t:b(0,0,1.0,0.18 if 3.0<=t<=5.5 else 0.13) for t in times}
def keys(d): return [dict(t=t,**d[t]) for t in times]
c={"mediaId":4143,"level":"B","keyWord":"bin","defaultVoice":"male",
"taps":[{"phrase":"to try to climb out","target":"the raccoon","voice":"male","keys":keys(R)},
{"phrase":"to lie crumpled up","target":"the green bag","voice":"male","keys":keys(G)},
{"phrase":"to grow behind the bin","target":"the bushes","voice":"male","keys":keys(B)}],
"stillS":9.0,
"nouns":[{"word":"a raccoon","x":0.48,"y":0.47,"voice":"male"},{"word":"a rubbish bag","x":0.76,"y":0.60,"voice":"male"},{"word":"a bin","x":0.50,"y":0.84,"voice":"male"},{"word":"bushes","x":0.75,"y":0.05,"voice":"male"}],
"question":"What is the raccoon trying to do?","answer":["It","is","trying","to","climb","out","of","the","bin."],"answerVoice":"male",
"notes":"Raccoon and bag touch: boxes split along the line between them, so the raccoon's spread right paw (2.0-3.5) and part of its head (6.0, 6.5) fall outside its box. Bushes = thin strip at the top edge (includes a bit of bin rim). The bin itself is not a tap target because it surrounds the raccoon."}
json.dump(c,open('content/4143.json','w'),indent=1)
