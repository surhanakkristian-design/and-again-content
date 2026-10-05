import json
T=[i*0.5 for i in range(25)]
W={0.0:(0.04,0.22,0.72,0.78),0.5:(0.13,0.23,0.57,0.77),1.0:(0.15,0.23,0.85,0.77),1.5:(0.30,0.22,0.65,0.78),
2.0:(0.19,0.24,0.56,0.76),2.5:(0.30,0.26,0.54,0.72),3.0:(0.33,0.28,0.48,0.70),3.5:(0.34,0.28,0.44,0.64),
4.0:(0.35,0.30,0.41,0.60),4.5:(0.32,0.31,0.46,0.66),5.0:(0.32,0.32,0.50,0.68),5.5:(0.30,0.33,0.52,0.67),
6.0:(0.25,0.29,0.52,0.70),6.5:(0.18,0.25,0.58,0.75),7.0:(0.26,0.25,0.56,0.75),7.5:(0.25,0.25,0.56,0.75),
8.0:(0.25,0.23,0.53,0.77),8.5:(0.15,0.22,0.63,0.78),9.0:(0.08,0.30,0.64,0.70),9.5:(0.36,0.26,0.64,0.74),
10.0:(0.29,0.29,0.43,0.62),10.5:(0.24,0.29,0.50,0.67),11.0:(0.17,0.26,0.70,0.74),11.5:(0.28,0.24,0.70,0.76),12.0:(0.00,0.25,0.78,0.75)}
R={2.0:(0.00,0.30,0.18,0.20),2.5:(0.00,0.31,0.20,0.20),10.0:(0.00,0.32,0.20,0.18),10.5:(0.00,0.30,0.20,0.20)}
def keys(d):
    out=[]
    for t in T:
        if t in d: x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":5037,"level":"A","keyWord":"sidewalk","defaultVoice":"female",
"taps":[{"phrase":"to pull a suitcase","target":"the woman in the coat","voice":"female","keys":keys(W)},
{"phrase":"to open a door","target":"the woman in the coat","voice":"female","keys":keys(W)},
{"phrase":"to smile at the woman","target":"the woman at the desk","voice":"female","keys":keys(R)}],
"stillS":7.0,
"nouns":[{"word":"a building","x":0.50,"y":0.12,"voice":"female"},{"word":"a woman","x":0.50,"y":0.50,"voice":"female"},
{"word":"a suitcase","x":0.22,"y":0.92,"voice":"female"},{"word":"a sidewalk","x":0.85,"y":0.79,"voice":"female"}],
"question":"Where is the woman in the coat?","answer":["She","is","standing","on","the","sidewalk."],"answerVoice":"female",
"notes":"Receptionist (the woman at the desk) is visible only at 2.0-2.5 and 10.0-10.5 s, small at the left edge; she smiles toward the coat woman. Two women: targets named 'the woman in the coat' / 'the woman at the desk'. Question names the woman in the coat because the receptionist is also a woman."}
json.dump(c,open('content/5037.json','w'),indent=1)
