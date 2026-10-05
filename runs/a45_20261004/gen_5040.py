import json
T=[i*0.5 for i in range(21)]
W={0.0:(0.33,0.00,0.67,0.62),0.5:(0.36,0.00,0.64,1.00),1.0:(0.14,0.17,0.86,0.83),1.5:(0.24,0.18,0.76,0.82),
2.0:(0.53,0.08,0.47,0.92),2.5:(0.33,0.04,0.67,0.60),3.0:(0.43,0.26,0.57,0.50),3.5:(0.50,0.10,0.50,0.70),
4.0:(0.48,0.18,0.52,0.82),4.5:(0.50,0.18,0.50,0.82),5.0:(0.45,0.19,0.55,0.81),5.5:(0.62,0.06,0.38,0.92),
6.0:(0.68,0.19,0.32,0.72),6.5:(0.76,0.13,0.24,0.85),7.0:(0.80,0.28,0.20,0.72),7.5:(0.68,0.25,0.32,0.75),
8.0:(0.62,0.26,0.38,0.74),8.5:(0.57,0.25,0.43,0.75),9.0:(0.50,0.21,0.50,0.79),9.5:(0.48,0.21,0.52,0.79),10.0:(0.44,0.21,0.56,0.79)}
B={0.0:(0.00,0.05,0.28,0.40),0.5:(0.00,0.38,0.18,0.25),1.5:(0.00,0.60,0.20,0.40),2.0:(0.00,0.46,0.52,0.46),
4.0:(0.20,0.60,0.27,0.27),4.5:(0.02,0.60,0.47,0.35),5.0:(0.00,0.62,0.44,0.36),7.0:(0.08,0.55,0.70,0.32),
7.5:(0.15,0.47,0.52,0.47),8.0:(0.18,0.48,0.43,0.48),8.5:(0.12,0.50,0.44,0.46),9.0:(0.00,0.42,0.49,0.56),
9.5:(0.00,0.42,0.47,0.56),10.0:(0.00,0.45,0.43,0.52)}
def keys(d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":5040,"level":"B","keyWord":"armchair","defaultVoice":"female",
"taps":[{"phrase":"to hold a brass lamp","target":"the woman in the jacket","voice":"female","keys":keys(W)},
{"phrase":"to heave a wooden crate","target":"the woman in the jacket","voice":"female","keys":keys(W)},
{"phrase":"to carry a velvet armchair","target":"the cargo bike","voice":"female","keys":keys(B)}],
"stillS":9.5,
"nouns":[{"word":"an armchair","x":0.22,"y":0.30,"voice":"female"},{"word":"a crate","x":0.22,"y":0.61,"voice":"female"},
{"word":"a cargo bike","x":0.20,"y":0.85,"voice":"female"},{"word":"a jacket","x":0.80,"y":0.45,"voice":"female"}],
"question":"What are the two women lifting?","answer":["They","are","lifting","a","velvet","armchair."],"answerVoice":"female",
"notes":"Second woman (green jumper) has no action of her own (she only helps lift the armchair, which the jacket woman also does), so she is not a target. Cargo bike box is off where it is hidden or only a sliver (1.0, 2.5-3.5, 5.5-6.5); at 0.0/0.5 only its black box shows at the left edge. Bike carries the armchair only from ~8.0 s; earlier it carries the crate. Bike box is cut where the woman's legs overlap it."}
json.dump(c,open('content/5040.json','w'),indent=1)
