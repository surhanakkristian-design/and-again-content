import json
T=[i*0.5 for i in range(21)]
Wd={0.0:(0.62,0.03,0.38,0.97),0.5:(0.64,0.03,0.36,0.97),1.0:(0.64,0.11,0.36,0.89),1.5:(0.65,0.29,0.35,0.71),
 2.0:(0.63,0.27,0.37,0.73),2.5:(0.64,0.19,0.36,0.81),3.0:(0.63,0.06,0.37,0.94),3.5:(0.60,0.04,0.40,0.96),
 4.0:(0.55,0.07,0.45,0.93),4.5:(0.43,0.12,0.57,0.88),5.0:(0.55,0.13,0.45,0.87),5.5:(0.56,0.11,0.44,0.89),
 6.0:(0.62,0.06,0.38,0.94),6.5:(0.63,0.10,0.37,0.90),7.0:(0.66,0.14,0.34,0.86),7.5:(0.62,0.14,0.38,0.86),
 8.0:(0.57,0.11,0.43,0.50),8.5:(0.68,0.09,0.32,0.91),9.0:(0.73,0.09,0.27,0.91),9.5:(0.69,0.29,0.31,0.71),10.0:(0.68,0.35,0.32,0.65)}
Od={0.0:(0.04,0.44,0.57,0.53),0.5:(0.04,0.43,0.59,0.54),1.0:(0.04,0.41,0.59,0.57),1.5:(0.07,0.36,0.57,0.56),
 2.0:(0.09,0.31,0.53,0.53),2.5:(0.07,0.28,0.56,0.51),3.0:(0.06,0.28,0.56,0.53),3.5:(0.05,0.30,0.54,0.52),
 4.0:(0.05,0.31,0.49,0.50),4.5:(0.05,0.30,0.37,0.51),5.0:(0.05,0.31,0.49,0.52),5.5:(0.04,0.30,0.51,0.53),
 6.0:(0.04,0.29,0.57,0.53),6.5:(0.02,0.29,0.60,0.52),7.0:(0.05,0.28,0.60,0.62),7.5:(0.04,0.26,0.57,0.64),
 8.0:(0.07,0.24,0.49,0.66),8.5:(0.04,0.24,0.63,0.65),9.0:(0.07,0.26,0.65,0.54),9.5:(0.06,0.26,0.62,0.54),10.0:(0.04,0.23,0.63,0.53)}
def keys(d): return [{"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
w=keys(Wd); o=keys(Od)
c={"mediaId":5179,"level":"B","keyWord":"to reach","defaultVoice":"female",
"taps":[
 {"phrase":"to reach towards the oven","target":"the woman","voice":"female","keys":w},
 {"phrase":"to carry a baking tray","target":"the woman","voice":"female","keys":w},
 {"phrase":"to glow orange inside","target":"the oven","voice":"female","keys":o}],
"stillS":4.5,
"nouns":[{"word":"a cupboard","x":0.25,"y":0.12,"voice":"female"},
 {"word":"an oven","x":0.28,"y":0.56,"voice":"female"},
 {"word":"a headscarf","x":0.84,"y":0.22,"voice":"female"},
 {"word":"dough","x":0.86,"y":0.60,"voice":"female"}],
"question":"Where is she reaching with her hand?",
"answer":["She","is","reaching","towards","the","hot","oven."],
"answerVoice":"female",
"notes":"Oven door is closed until ~6.0 (opened then), oven light on from 0.5 (off at 0.0). Woman/oven split where her hand reaches in front of the oven (4.0-5.5) and where she slides the tray in (7.0-9.0): the hand/tray inside the oven belongs to the oven box. At 8.0 the woman box covers only head+arm (body is low right edge)."}
json.dump(c,open('content/5179.json','w'),indent=1)
