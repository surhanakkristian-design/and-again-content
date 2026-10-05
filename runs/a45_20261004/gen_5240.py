import json
T=[i*0.5 for i in range(25)]
man={0.0:(0.34,0.35,0.33,0.31),0.5:(0.35,0.32,0.37,0.34),1.0:(0.35,0.37,0.36,0.31),1.5:(0.35,0.37,0.34,0.31),
2.0:(0.34,0.38,0.38,0.31),2.5:(0.22,0.51,0.70,0.49),3.0:(0.0,0.50,0.97,0.50),3.5:(0.0,0.53,0.75,0.47),
4.0:(0.0,0.58,0.90,0.42),4.5:(0.0,0.53,0.64,0.47),5.0:(0.0,0.53,0.82,0.47),5.5:(0.0,0.55,0.88,0.45),
6.0:(0.0,0.52,0.99,0.48),6.5:(0.0,0.53,1.0,0.47),7.0:(0.0,0.37,0.95,0.63),7.5:(0.0,0.37,0.74,0.63),
8.0:(0.0,0.52,0.72,0.48),8.5:(0.0,0.48,0.68,0.52),9.0:(0.0,0.39,0.48,0.61),9.5:(0.0,0.35,0.53,0.65),
10.0:(0.0,0.29,0.53,0.71),10.5:(0.0,0.27,0.59,0.73),11.0:(0.0,0.23,0.56,0.77),11.5:(0.0,0.20,0.55,0.80),12.0:(0.0,0.16,0.62,0.84)}
fal={2.5:(0.56,0.29,0.25,0.16),3.0:(0.42,0.19,0.25,0.14),3.5:(0.67,0.07,0.24,0.14),4.0:(0.82,0.09,0.18,0.14),
4.5:(0.65,0.29,0.22,0.14),5.0:(0.39,0.37,0.19,0.14),5.5:(0.20,0.40,0.20,0.14),6.0:(0.12,0.37,0.20,0.14),
6.5:(0.21,0.28,0.30,0.14),7.0:(0.10,0.22,0.59,0.15),7.5:(0.17,0.06,0.68,0.31),8.0:(0.34,0.19,0.54,0.33),
8.5:(0.40,0.16,0.50,0.32),9.0:(0.48,0.34,0.51,0.40),9.5:(0.53,0.37,0.43,0.31),10.0:(0.53,0.35,0.44,0.32),
10.5:(0.59,0.35,0.41,0.32),11.0:(0.56,0.33,0.44,0.35),11.5:(0.55,0.31,0.45,0.32),12.0:(0.62,0.29,0.38,0.34)}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":5240,"level":"B","keyWord":"wing","defaultVoice":"male",
"taps":[{"phrase":"to swing a lure overhead","target":"the falconer","voice":"male","keys":keys(man)},
{"phrase":"to spread its wings wide","target":"the falcon","voice":"male","keys":keys(fal)},
{"phrase":"to feed meat to the falcon","target":"the falconer","voice":"male","keys":keys(man)}],
"stillS":7.5,
"nouns":[{"word":"a wing","x":0.27,"y":0.13,"voice":"male"},{"word":"a falcon","x":0.52,"y":0.26,"voice":"male"},
{"word":"a glove","x":0.60,"y":0.46,"voice":"male"},{"word":"a pickup truck","x":0.80,"y":0.72,"voice":"male"}],
"question":"What is the falconer doing?","answer":["He","is","feeding","meat","to","the","falcon."],"answerVoice":"male",
"notes":"Two shots (wide 0-2.0, close 2.5-12). Friends in background are not targets. Falcon off until it appears at 2.5 (the thing at 0.5 top-left is the lure). Where falcon sits on the glove (8.0-12.0) the boxes are split along the line between them, so the falcon's beak/feet are partly cut at 8.5-12.0."}
json.dump(c,open('content/5240.json','w'),indent=1)
