import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
M={0.0:(0,0.27,0.56,0.73),0.5:(0,0.28,0.56,0.72),1.0:(0,0.29,0.55,0.71),1.5:(0,0.30,0.55,0.70),2.0:(0,0.30,0.57,0.70),
 2.5:(0,0.30,0.58,0.70),3.0:(0,0.31,0.58,0.69),3.5:(0,0.31,0.60,0.69),4.0:(0,0.31,0.60,0.69),4.5:(0,0.31,0.60,0.69),
 5.0:(0,0.33,0.60,0.67),5.5:(0,0.34,0.60,0.66),6.0:(0,0.35,0.58,0.65),6.5:(0,0.37,0.58,0.63),7.0:(0,0.38,0.57,0.62),
 7.5:(0,0.39,0.57,0.61),8.0:(0,0.40,0.58,0.60),8.5:(0,0.42,0.58,0.58),9.0:(0,0.44,0.58,0.56),9.5:(0,0.45,0.58,0.55),
 10.0:(0,0.46,0.58,0.54),10.5:(0,0.47,0.58,0.53),11.0:(0,0.48,0.58,0.52),11.5:(0,0.48,0.58,0.52),12.0:(0,0.48,0.58,0.52)}
H={4.0:0.22,4.5:0.22,5.0:0.22,5.5:0.22,6.0:0.27,6.5:0.30,7.0:0.33,7.5:0.36,8.0:0.36,8.5:0.36,9.0:0.40,9.5:0.40,
 10.0:0.42,10.5:0.42,11.0:0.44,11.5:0.44,12.0:0.44}
MT={t:(0,0,1.0,h) for t,h in H.items()}
c={"mediaId":5452,"level":"A","keyWord":"peaceful","defaultVoice":"male",
"taps":[{"phrase":"to drink from a cup","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to look at the mountains","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to have snow on it","target":"the mountain","voice":"male","keys":keys(MT)}],
"stillS":10.0,
"nouns":[{"word":"a mountain","x":0.45,"y":0.15,"voice":"male"},{"word":"trees","x":0.65,"y":0.36,"voice":"male"},
{"word":"a lake","x":0.68,"y":0.62,"voice":"male"},{"word":"a cup","x":0.47,"y":0.84,"voice":"male"}],
"question":"What is the man holding?","answer":["He","is","holding","a","cup."],"answerVoice":"male",
"notes":"Only one person; the mountain is the second target, hidden by mist until ~4.0 s (marked off before). The cup is a metal enamel mug; 'cup' chosen for level A. Snow on the mountain is light patches, mostly at its foot (left)."}
json.dump(c,open('content/5452.json','w'),indent=1)
