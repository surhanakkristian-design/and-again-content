import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=x0,y=y0,w=round(x1-x0,2),h=round(y1-y0,2)) for t,(x0,y0,x1,y1) in zip(T,b)]
split=[.43,.44,.44,.45,.44,.44,.44,.45]
tops=[.09,.08,.08,.07,.04,.04,.05,.05]
woman=K([(s+.01,tp,1.0,1.0) for s,tp in zip(split,tops)])
man=K([(0.0,.15,s,.58) for s in split])
c={"mediaId":7817,"level":"B","keyWord":"electronics","defaultVoice":"female",
"taps":[{"phrase":"to solder a wire","target":"the woman","voice":"female","keys":woman},
{"phrase":"to frown in concentration","target":"the woman","voice":"female","keys":woman},
{"phrase":"to hold a glass valve","target":"the man","voice":"male","keys":man}],
"stillS":0.2,
"nouns":[{"word":"cabinets","x":0.30,"y":0.08,"voice":"female"},{"word":"a valve","x":0.17,"y":0.40,"voice":"female"},
{"word":"electronics","x":0.30,"y":0.60,"voice":"female"},{"word":"a jumper","x":0.80,"y":0.45,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","soldering","a","wire","inside","an","amplifier."],"answerVoice":"female",
"notes":"'electronics' labels the open amplifier chassis. The frown is clearest at 2.2-3.2 s; she smiles at the start and the end. Woman and man are split along x ~0.44 where her soldering hand comes near his shirt."}
json.dump(c,open('content/7817.json','w'),indent=1)
