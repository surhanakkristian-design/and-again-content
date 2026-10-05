import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
W={0.0:(0.20,0.28,0.80,0.58),0.5:(0.20,0.23,0.80,0.64),1.0:(0.15,0.30,0.85,0.62),1.5:(0.35,0.48,0.65,0.52),2.0:(0.14,0.26,0.86,0.74),2.5:(0.17,0.25,0.83,0.75),
   3.0:(0.52,0.0,0.48,1.0),3.5:(0.60,0.0,0.40,1.0),4.0:(0.60,0.02,0.40,0.98),4.5:(0.37,0.10,0.63,0.90),5.0:(0.46,0.08,0.54,0.92),5.5:(0.40,0.10,0.60,0.90),
   6.0:(0.28,0.47,0.72,0.53),7.5:(0.44,0.60,0.56,0.40),8.0:(0.42,0.39,0.58,0.61),8.5:(0.41,0.34,0.59,0.66),9.0:(0.38,0.44,0.62,0.56),9.5:(0.28,0.37,0.72,0.63),10.0:(0.39,0.29,0.61,0.71)}
P={0.0:(0.08,0.03,0.54,0.15),0.5:(0.35,0.08,0.28,0.14),1.0:(0.30,0.14,0.33,0.14),1.5:(0.02,0.12,0.52,0.14),2.0:(0.0,0.11,0.49,0.14),2.5:(0.0,0.10,0.42,0.14),
   3.0:(0.0,0.10,0.48,0.14),3.5:(0.07,0.24,0.52,0.14),4.0:(0.10,0.28,0.49,0.14),4.5:(0.10,0.28,0.26,0.14),5.0:(0.19,0.32,0.26,0.14),5.5:(0.22,0.30,0.18,0.14),
   6.0:(0.08,0.66,0.19,0.14),7.5:(0.05,0.81,0.37,0.14),8.0:(0.07,0.63,0.34,0.14),8.5:(0.05,0.58,0.35,0.14),9.0:(0.03,0.53,0.34,0.14),9.5:(0.02,0.46,0.25,0.14),10.0:(0.02,0.40,0.36,0.14)}
B={5.0:(0.0,0.25,0.18,0.18),5.5:(0.21,0.44,0.18,0.14),6.5:(0.30,0.04,0.18,0.14),7.0:(0.30,0.27,0.18,0.14),7.5:(0.36,0.04,0.18,0.14)}
c={"mediaId":74,"level":"A","keyWord":"bat","defaultVoice":"female",
 "taps":[
  {"phrase":"to hold a bat","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to fly through the air","target":"the ball","voice":"female","keys":keys(B)},
  {"phrase":"to sit on the grass","target":"the people on the grass","voice":"female","keys":keys(P)}],
 "stillS":8.0,
 "nouns":[{"word":"a tree","x":0.35,"y":0.22,"voice":"female"},{"word":"a bat","x":0.75,"y":0.48,"voice":"female"},
          {"word":"a helmet","x":0.65,"y":0.64,"voice":"female"},{"word":"grass","x":0.20,"y":0.88,"voice":"female"}],
 "question":"What is the woman holding?",
 "answer":["She","is","holding","a","bat."],
 "answerVoice":"female",
 "notes":"PACKET MISMATCH: the description speaks of a fruit bat in a cave, but the frames show a young woman with a baseball bat in a park (cherry trees). Written for what the frames show; the key word 'bat' is here the baseball bat - check that this sense is the intended one. The people sitting on the grass are small and blurred in the background (far-away pair plus their things on a blanket). Where they are near the woman (2.0, 2.5, 6.0, 9.5, 10.0 s) the boxes are split: her head is outside her box at 2.0 and 2.5 s (box follows the hands on the bat), her left arm at 10.0 s. The ball is tiny at 6.5-7.5 s (minimum-size box). A person in a brown shirt is cut at the left edge at 5.5 s (no target)."}
json.dump(c,open('content/74.json','w'),indent=1)
