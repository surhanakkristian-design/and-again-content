import json
O={"off":True}
def b(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
def keys(times,d): return [dict(t=t,**d[t]) for t in times]
T21=[i*0.5 for i in range(21)]
def dump(c): json.dump(c,open('content/%d.json'%c["mediaId"],'w'),indent=1)
W={0.0:b(0.36,0.04,0.64,0.96),0.5:b(0.36,0.06,0.64,0.94),1.0:b(0.33,0.07,0.67,0.93),1.5:b(0.25,0.07,0.75,0.93),2.0:b(0.22,0.07,0.78,0.93),
2.5:b(0.10,0.23,0.72,0.57),3.0:b(0.09,0.25,0.72,0.65),3.5:b(0.11,0.22,0.71,0.68),4.0:b(0.18,0.17,0.58,0.60),4.5:b(0.17,0.17,0.59,0.60),
5.0:b(0.14,0.05,0.61,0.85),5.5:b(0.29,0,0.71,0.78),6.0:b(0.37,0,0.63,0.77),6.5:b(0.08,0,0.78,1.0),7.0:b(0.03,0.15,0.87,0.85),
7.5:b(0.02,0.18,0.87,0.82),8.0:b(0,0.18,0.86,0.80),8.5:b(0,0.18,0.80,0.80),9.0:b(0,0.18,0.80,0.80),9.5:b(0,0.18,0.81,0.80),10.0:b(0,0.16,0.88,0.80)}
Mn={t:O for t in T21}
Mn[8.5]=b(0.81,0,0.19,0.75); Mn[9.0]=b(0.81,0,0.19,0.78); Mn[9.5]=b(0.82,0,0.18,0.45)
dump({"mediaId":582,"level":"A","keyWord":"proud","defaultVoice":"female",
"taps":[{"phrase":"to sit on a chair","target":"the woman","voice":"female","keys":keys(T21,W)},
{"phrase":"to cross her arms","target":"the woman","voice":"female","keys":keys(T21,W)},
{"phrase":"to touch her shoulder","target":"the man","voice":"male","keys":keys(T21,Mn)}],
"stillS":6.0,
"nouns":[{"word":"a chair","x":0.40,"y":0.60,"voice":"female"},{"word":"a woman","x":0.70,"y":0.24,"voice":"female"},
{"word":"a window","x":0.20,"y":0.10,"voice":"female"},{"word":"a table","x":0.14,"y":0.34,"voice":"female"}],
"question":"How does the woman feel?","answer":["She","is","proud","of","her","new","chair."],"answerVoice":"female",
"notes":"The man is in the picture only at 8.5-9.5 (at 8.0 just an arm at the right edge -> off; gone at 10.0); he stands at the right edge with his hand on her shoulder, so his box is a narrow strip and the woman's box ends left of it. The chair changes shape between the shots (armrests appear from 6.5). 'a table' = the workbench on the left. Question asks for a feeling (key word 'proud') rather than an action."})
