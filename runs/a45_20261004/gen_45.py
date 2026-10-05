import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2],2),"h":round(d[t][3],2)} if d.get(t) else {"t":t,"off":True}) for t in T]
W={0.0:(0.20,0.24,0.75,0.76),0.5:(0.05,0.18,0.95,0.82),1.0:(0.03,0.16,0.97,0.84),1.5:(0.02,0.15,0.98,0.85),2.0:(0.34,0.12,0.66,0.88),
2.5:(0.56,0.20,0.44,0.80),3.0:(0.55,0.19,0.45,0.81),3.5:(0.52,0.38,0.48,0.38),4.0:(0.34,0.20,0.66,0.80),4.5:(0.44,0.17,0.56,0.83),
5.0:(0.39,0.18,0.61,0.82),5.5:(0.37,0.18,0.63,0.82),6.0:(0.33,0.18,0.67,0.82),6.5:(0.38,0.18,0.62,0.82),7.0:(0.34,0.19,0.66,0.81),
7.5:(0.25,0.20,0.75,0.80),8.0:(0.30,0.18,0.70,0.82),8.5:(0.27,0.16,0.73,0.84),9.0:(0.25,0.18,0.75,0.82),9.5:(0.20,0.18,0.80,0.82),10.0:(0.22,0.20,0.78,0.80)}
C={2.0:(0,0.73,0.33,0.22),2.5:(0.08,0.67,0.47,0.24),3.0:(0.22,0.69,0.33,0.28),3.5:(0.42,0.77,0.40,0.18)}
M={3.0:(0,0.25,0.18,0.75),3.5:(0,0.22,0.19,0.78),4.0:(0,0.20,0.24,0.80),4.5:(0,0.28,0.27,0.72),5.0:(0,0.34,0.38,0.66),5.5:(0,0.05,0.36,0.95),
6.0:(0,0.38,0.31,0.62),6.5:(0,0.38,0.24,0.62),7.0:(0,0.38,0.26,0.62),7.5:(0,0.40,0.24,0.60),8.0:(0,0.46,0.27,0.54),8.5:(0,0.68,0.20,0.32),
9.0:(0,0.72,0.22,0.28),9.5:(0,0.70,0.19,0.30),10.0:(0,0.48,0.21,0.52)}
c={"mediaId":45,"level":"A","keyWord":"angry","defaultVoice":"female",
"taps":[{"phrase":"to shout at the man","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to lie on the floor","target":"the clothes","voice":"female","keys":keys(C)},
{"phrase":"to wear a grey jacket","target":"the man","voice":"male","keys":keys(M)}],
"stillS":3.0,
"nouns":[{"word":"bottles","x":0.73,"y":0.20,"voice":"female"},{"word":"a washing machine","x":0.22,"y":0.50,"voice":"female"},
{"word":"a woman","x":0.76,"y":0.47,"voice":"female"},{"word":"clothes","x":0.40,"y":0.79,"voice":"female"}],
"question":"What is the angry woman doing?",
"answer":["She","is","shouting","at","the","man."],"answerVoice":"female",
"notes":"The man is only seen from behind at the left edge (grey jacket shoulder/arm), so his phrase is a state. At 5.5 his hand reaches across the woman: his box is the left column only, the hand lies inside the woman's box. At 3.5 the woman bends over the clothes: boxes split at y 0.76/0.77, her legs fall outside her box. A second, tiny blurred person sits on a bench in the background (not used); the question says 'the angry woman' to be clear. Clothes are off from 4.0 on (in her hand / in the machine). 'bottles' = the row on the right shelf; two more bottles stand on the left shelf."}
json.dump(c,open('content/45.json','w'),indent=1)
