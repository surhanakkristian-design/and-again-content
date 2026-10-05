import json
O={"off":True}
def b(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
def keys(times,d): return [dict(t=t,**d[t]) for t in times]
T21=[i*0.5 for i in range(21)]; T15=[i*0.5 for i in range(15)]
def dump(c): json.dump(c,open('content/%d.json'%c["mediaId"],'w'),indent=1)

# ---------- 579
M={0.0:b(0,0.21,0.32,0.34),0.5:b(0,0.22,0.32,0.33),1.0:b(0,0.24,0.38,0.31),1.5:b(0,0.24,0.38,0.31),2.0:b(0,0.24,0.40,0.29),
2.5:b(0,0.19,0.30,0.33),3.0:b(0,0.25,0.28,0.30),3.5:b(0,0.28,0.30,0.27),4.0:b(0,0.26,0.30,0.27),4.5:b(0,0.23,0.30,0.30),
5.0:b(0,0.25,0.40,0.39),5.5:b(0,0.25,0.38,0.39),6.0:b(0,0.25,0.39,0.29),6.5:b(0,0.24,0.37,0.30),7.0:b(0,0.20,0.33,0.32),
7.5:b(0,0.16,0.35,0.36),8.0:b(0,0.02,0.50,0.56),8.5:b(0,0.16,0.44,0.38),9.0:b(0,0.19,0.47,0.39),9.5:b(0,0.20,0.34,0.44),10.0:O}
W={0.0:b(0.48,0.20,0.52,0.42),0.5:b(0.50,0.21,0.50,0.41),1.0:b(0.50,0.24,0.50,0.42),1.5:b(0.52,0.24,0.48,0.42),2.0:b(0.52,0.21,0.48,0.42),
2.5:b(0.58,0.22,0.42,0.44),3.0:b(0.62,0.25,0.38,0.47),3.5:b(0.60,0.26,0.40,0.46),4.0:b(0.50,0.23,0.50,0.42),4.5:b(0.56,0.24,0.44,0.40),
5.0:b(0.50,0.26,0.50,0.46),5.5:b(0.46,0.26,0.54,0.46),6.0:b(0.55,0.25,0.45,0.39),6.5:b(0.54,0.25,0.46,0.29),7.0:b(0.63,0.18,0.37,0.58),
7.5:b(0.70,0.10,0.30,0.60),8.0:b(0.54,0.02,0.46,0.57),8.5:b(0.45,0.18,0.55,0.36),9.0:b(0.48,0.22,0.52,0.36),9.5:b(0.50,0.22,0.50,0.36),10.0:O}
R={0.0:b(0.08,0.56,0.34,0.16),0.5:b(0.08,0.56,0.34,0.16),1.0:b(0.08,0.57,0.34,0.17),1.5:b(0.09,0.56,0.34,0.16),2.0:b(0.14,0.535,0.32,0.14),
2.5:b(0.12,0.53,0.32,0.14),3.0:b(0.11,0.555,0.32,0.15),3.5:b(0.11,0.555,0.32,0.15),4.0:b(0.12,0.54,0.32,0.14),4.5:b(0.12,0.54,0.32,0.14),
5.0:b(0.11,0.65,0.33,0.14),5.5:b(0.12,0.65,0.32,0.14),6.0:b(0.16,0.55,0.32,0.14),6.5:b(0.38,0.545,0.32,0.14),7.0:b(0.34,0.53,0.28,0.15),
7.5:b(0.40,0.53,0.29,0.15),8.0:b(0.39,0.60,0.30,0.14),8.5:b(0.38,0.555,0.32,0.14),9.0:b(0.40,0.59,0.26,0.15),9.5:b(0.45,0.59,0.32,0.15),10.0:b(0.43,0.59,0.32,0.15)}
dump({"mediaId":579,"level":"B","keyWord":"programming","defaultVoice":"male",
"taps":[{"phrase":"to type new code","target":"the woman","voice":"female","keys":keys(T21,W)},
{"phrase":"to gesture towards the laptop","target":"the man","voice":"male","keys":keys(T21,M)},
{"phrase":"to follow the drawn track","target":"the robot","voice":"male","keys":keys(T21,R)}],
"stillS":4.5,
"nouns":[{"word":"a robot","x":0.27,"y":0.62,"voice":"male"},{"word":"a laptop","x":0.36,"y":0.50,"voice":"male"},
{"word":"a ponytail","x":0.88,"y":0.35,"voice":"male"},{"word":"a beard","x":0.16,"y":0.38,"voice":"male"}],
"question":"What is the woman doing?","answer":["She","is","programming","a","small","robot."],"answerVoice":"female",
"notes":"Couple (mixed) -> defaultVoice male (odd id). The man's gesture is short (5.0-5.5 he points down towards the laptop/keyboard); weakest phrase. At 8.5-9.0 the woman's hands rest on the robot: her box is cut at the robot's top edge. At 10.0 only forearms of both people remain at the frame edges -> off. Two mugs on the table, so no 'a mug' noun."})
