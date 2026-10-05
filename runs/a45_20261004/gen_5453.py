import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
V={0.0:(0.10,0.0,0.68,0.54),0.5:(0.10,0.0,0.84,0.77),1.0:(0.07,0.08,0.86,0.73),1.5:(0.20,0.30,0.62,0.62),
 2.0:(0.22,0.37,0.54,0.54),2.5:(0.23,0.45,0.50,0.48),3.0:(0.25,0.49,0.46,0.46),3.5:(0.25,0.50,0.46,0.46),
 4.0:(0.29,0.57,0.38,0.40),4.5:(0.28,0.57,0.40,0.40),5.0:(0.28,0.59,0.40,0.39),5.5:(0.27,0.56,0.38,0.41),
 6.0:(0.26,0.57,0.38,0.39),6.5:(0.28,0.59,0.38,0.37),7.0:(0.28,0.59,0.38,0.38),7.5:(0.28,0.60,0.38,0.37),
 8.0:(0.28,0.60,0.38,0.37),8.5:(0.34,0.55,0.34,0.27),9.0:(0.35,0.56,0.33,0.29),9.5:(0.35,0.55,0.33,0.31),
 10.0:(0.34,0.57,0.34,0.32),10.5:(0.34,0.57,0.34,0.34),11.0:(0.31,0.60,0.37,0.36),11.5:(0.30,0.60,0.38,0.38),
 12.0:(0.31,0.62,0.36,0.37)}
W={0.0:(0.80,0.0,0.20,0.45),1.5:(0,0,1.0,0.29),2.0:(0,0,1.0,0.36),2.5:(0,0,1.0,0.44),3.0:(0,0,1.0,0.48),3.5:(0,0,1.0,0.49),
 4.0:(0.12,0.0,0.88,0.56),4.5:(0.04,0.0,0.96,0.56),5.0:(0.04,0.0,0.92,0.58),5.5:(0,0,1.0,0.55),6.0:(0,0,1.0,0.56),
 6.5:(0,0,1.0,0.58),7.0:(0,0,1.0,0.58),7.5:(0,0,1.0,0.59),8.0:(0,0,1.0,0.59),8.5:(0,0,1.0,0.54),9.0:(0,0,1.0,0.55),
 9.5:(0,0,1.0,0.54),10.0:(0,0,1.0,0.56),10.5:(0,0,1.0,0.56),11.0:(0,0,1.0,0.59),11.5:(0,0,1.0,0.59),12.0:(0,0,1.0,0.61)}
c={"mediaId":5453,"level":"B","keyWord":"vase","defaultVoice":"female",
"taps":[{"phrase":"to pour in some water","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to arrange the flowers","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to have a glossy surface","target":"the vase","voice":"female","keys":keys(V)}],
"stillS":2.5,
"nouns":[{"word":"a glass jug","x":0.14,"y":0.38,"voice":"female"},{"word":"a blouse","x":0.62,"y":0.28,"voice":"female"},
{"word":"sunflowers","x":0.86,"y":0.72,"voice":"female"},{"word":"a vase","x":0.48,"y":0.82,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","arranging","flowers","in","a","vase."],"answerVoice":"female",
"notes":"The vase stands in front of the woman, so her box is the area above the vase (from 4.0 s her hands/arms beside the vase fall partly in the vase box or outside). At 0.5-1.0 s only her hands on the vase and slivers of her shirt show: marked off. At 0.0 her box is the visible right part of her shirt."}
json.dump(c,open('content/5453.json','w'),indent=1)
