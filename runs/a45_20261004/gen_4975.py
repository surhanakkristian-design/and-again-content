import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
W={1.0:(0.48,0.35,0.24,0.62),1.5:(0.34,0.34,0.42,0.58),2.0:(0.26,0.31,0.44,0.69),2.5:(0.30,0.31,0.50,0.68),3.0:(0.30,0.32,0.46,0.68),
 3.5:(0.28,0.32,0.47,0.68),4.0:(0.25,0.32,0.50,0.64),4.5:(0.28,0.30,0.40,0.62),5.0:(0,0.24,0.70,0.76),5.5:(0,0.23,0.67,0.77),
 6.0:(0,0.22,0.67,0.78),6.5:(0.13,0.13,0.72,0.87),7.0:(0.03,0.16,0.84,0.84),7.5:(0.03,0.21,0.90,0.79),8.0:(0.13,0.22,0.82,0.78),
 8.5:(0.12,0.22,0.88,0.78),9.0:(0.06,0.26,0.92,0.74)}
M={5.0:(0.72,0.10,0.28,0.80),5.5:(0.68,0.09,0.32,0.91),6.0:(0.68,0.08,0.32,0.84)}
c={"mediaId":4975,"level":"A","keyWord":"different","defaultVoice":"female",
 "taps":[
  {"phrase":"to drink orange juice","target":"the woman in blue","voice":"female","keys":K(W)},
  {"phrase":"to smile at the camera","target":"the woman in blue","voice":"female","keys":K(W)},
  {"phrase":"to pour orange juice","target":"the juice machine","voice":"female","keys":K(M)}],
 "stillS":6.0,
 "nouns":[{"word":"a hat","x":0.38,"y":0.28,"voice":"female"},{"word":"a cup","x":0.60,"y":0.55,"voice":"female"},
  {"word":"a coat","x":0.22,"y":0.72,"voice":"female"},{"word":"a machine","x":0.88,"y":0.35,"voice":"female"}],
 "question":"What is the woman drinking?",
 "answer":["She","is","drinking","orange","juice."],"answerVoice":"female",
 "notes":"Key word 'different' is an adjective, not used as a noun. Woman hidden behind suits at 0.0-0.5 (off). Juice machine only visible 5.0-6.0; split line between her hands and the machine at x~0.68-0.72. Coat colour is turquoise; target named 'the woman in blue' (A level) - every other woman wears grey."}
json.dump(c,open('content/4975.json','w'),indent=1)
