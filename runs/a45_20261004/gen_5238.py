import json
T=[i*0.5 for i in range(25)]
man={0.0:(0.12,0.53,0.58,0.47),0.5:(0.06,0.45,0.72,0.55),1.0:(0.0,0.46,1.0,0.54),1.5:(0.03,0.45,0.97,0.55),
2.0:(0.03,0.43,0.76,0.57),2.5:(0.05,0.44,0.74,0.56),3.0:(0.08,0.46,0.82,0.54),3.5:(0.03,0.43,0.97,0.57),
4.0:(0.0,0.45,0.97,0.55),4.5:(0.0,0.45,0.68,0.55),5.0:(0.0,0.37,0.88,0.63),5.5:(0.0,0.39,0.82,0.61),
6.0:(0.0,0.40,0.88,0.60),6.5:(0.0,0.40,0.89,0.60),7.0:(0.0,0.41,0.85,0.59),7.5:(0.0,0.44,0.91,0.56),
8.0:(0.0,0.42,1.0,0.58),8.5:(0.0,0.23,0.66,0.77),9.0:(0.0,0.24,0.66,0.76),9.5:(0.0,0.24,0.66,0.76),
10.0:(0.0,0.24,0.66,0.76),10.5:(0.0,0.24,0.68,0.76),11.0:(0.0,0.28,0.70,0.72),11.5:(0.0,0.28,0.73,0.72),12.0:(0.0,0.27,0.74,0.73)}
sun={0.0:(0.52,0.32,0.22,0.14),0.5:(0.49,0.31,0.22,0.14),1.0:(0.42,0.31,0.22,0.14),1.5:(0.46,0.31,0.22,0.14),
2.0:(0.56,0.29,0.24,0.14),2.5:(0.52,0.30,0.24,0.14),3.0:(0.51,0.32,0.22,0.14),3.5:(0.56,0.29,0.22,0.14),
4.0:(0.52,0.31,0.22,0.14),4.5:(0.50,0.31,0.22,0.14)}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":5238,"level":"B","keyWord":"dune","defaultVoice":"male",
"taps":[{"phrase":"to stroke the carved stone","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to set behind the dune","target":"the sun","voice":"male","keys":keys(sun)},
{"phrase":"to crouch by the campfire","target":"the man","voice":"male","keys":keys(man)}],
"stillS":0.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"male"},{"word":"the sun","x":0.63,"y":0.38,"voice":"male"},
{"word":"a dune","x":0.22,"y":0.50,"voice":"male"},{"word":"a headscarf","x":0.55,"y":0.61,"voice":"male"}],
"question":"What is he doing at the cliff?","answer":["He","is","stroking","the","carved","stone."],"answerVoice":"male",
"notes":"Selfie clip, 3 shots (dune 0-4.5, carved cliff 5-8, campfire 8.5-12). Only the man and the sun as targets; the pourer is only a hand. Sun box at 2.0/2.5/3.5 shifted upward so it does not overlap the man's head box. 'stroke the carved stone' = he runs his palm over the carved cliff."}
json.dump(c,open('content/5238.json','w'),indent=1)
