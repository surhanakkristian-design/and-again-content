import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
sub={1.5:(0.34,0.0,0.3,0.14),2.0:(0.28,0.0,0.44,0.14),2.5:(0.3,0.02,0.44,0.14),3.0:(0.26,0.05,0.52,0.14),3.5:(0.28,0.1,0.48,0.14),
 4.0:(0.28,0.14,0.36,0.15),4.5:(0.28,0.18,0.34,0.17),5.0:(0.15,0.24,0.68,0.24),5.5:(0.06,0.26,0.86,0.3),6.0:(0.38,0.31,0.62,0.34),
 6.5:(0.08,0.36,0.86,0.36),7.0:(0.04,0.45,0.78,0.38),7.5:(0.0,0.47,0.82,0.37),8.0:(0.0,0.5,0.64,0.33),8.5:(0.0,0.6,0.5,0.16),9.0:(0.0,0.51,0.36,0.14)}
whale={6.0:(0.0,0.41,0.38,0.15),6.5:(0.0,0.08,1.0,0.27),7.0:(0.06,0.02,0.78,0.42),7.5:(0.0,0.03,1.0,0.44),8.0:(0.0,0.14,1.0,0.36),8.5:(0.0,0.22,1.0,0.38),9.0:(0.0,0.3,0.68,0.21)}
c={"mediaId":4902,"level":"B","keyWord":"submarine","defaultVoice":"male",
"taps":[
 {"phrase":"to surface slowly","target":"the submarine","voice":"male","keys":keys(sub)},
 {"phrase":"to leap into the air","target":"the whale","voice":"male","keys":keys(whale)},
 {"phrase":"to crash back down","target":"the whale","voice":"male","keys":keys(whale)}],
"stillS":5.5,
"nouns":[{"word":"the sky","x":0.35,"y":0.12,"voice":"male"},{"word":"the horizon","x":0.15,"y":0.39,"voice":"male"},
 {"word":"a submarine","x":0.50,"y":0.48,"voice":"male"},{"word":"water","x":0.35,"y":0.64,"voice":"male"}],
"question":"What is the whale doing?",
"answer":["The","whale","is","leaping","out","of","the","water."],
"answerVoice":"male",
"notes":"Swimmers (young man + girls) all do the same things (burst up, laugh, swim), so no swimmer phrase fits only one target; whale used for two phrases. Submarine box starts at 1.5 s as a far dark hump on the horizon. Whale and submarine overlap from 6.5 s: boxes split horizontally (whale above, conning tower + hull below). At 6.0 s only the whale's head shows behind the hull on the left."}
json.dump(c,open('content/4902.json','w'),indent=1)
