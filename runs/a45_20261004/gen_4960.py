import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
D={0.0:(0.02,0.25,0.40,0.75),0.5:(0.02,0.26,0.40,0.74),1.0:(0.0,0.26,0.38,0.74),1.5:(0.02,0.27,0.40,0.73),
   2.0:(0.0,0.26,0.40,0.74),2.5:(0.0,0.28,0.42,0.72),3.0:(0.02,0.30,0.36,0.70),3.5:(0.04,0.30,0.38,0.70),
   4.0:(0.20,0.30,0.43,0.70),4.5:(0.15,0.30,0.50,0.70),5.0:(0.22,0.30,0.40,0.70),5.5:(0.15,0.27,0.44,0.73),
   6.0:(0.08,0.30,0.44,0.30),6.5:(0.08,0.35,0.42,0.30),7.0:(0.15,0.34,0.38,0.30),7.5:(0.28,0.36,0.30,0.30),
   8.0:(0.30,0.37,0.30,0.30),8.5:(0.24,0.40,0.36,0.30),9.0:(0.18,0.43,0.38,0.30),9.5:(0.20,0.40,0.34,0.30),
   10.0:(0.22,0.40,0.32,0.30),10.5:(0.30,0.40,0.27,0.28),11.0:(0.26,0.40,0.24,0.30),11.5:(0.26,0.40,0.24,0.30),12.0:(0.22,0.40,0.27,0.30)}
R={0.0:(0.42,0.18,0.48,0.82),0.5:(0.42,0.18,0.48,0.82),1.0:(0.38,0.20,0.50,0.80),1.5:(0.42,0.20,0.48,0.80),
   2.0:(0.40,0.19,0.52,0.81),2.5:(0.42,0.20,0.50,0.80),3.0:(0.38,0.24,0.52,0.76),3.5:(0.42,0.24,0.50,0.76),
   4.0:(0.63,0.24,0.37,0.76),4.5:(0.66,0.27,0.34,0.73),5.0:(0.64,0.26,0.36,0.74),5.5:(0.60,0.26,0.40,0.74),
   6.0:(0.53,0.25,0.47,0.75),6.5:(0.50,0.27,0.50,0.73),7.0:(0.55,0.25,0.43,0.75),7.5:(0.60,0.28,0.38,0.72),
   8.0:(0.62,0.28,0.36,0.72),8.5:(0.63,0.29,0.35,0.71),9.0:(0.57,0.30,0.25,0.70),9.5:(0.55,0.28,0.30,0.72),
   10.0:(0.55,0.25,0.40,0.75),10.5:(0.58,0.25,0.38,0.75),11.0:(0.50,0.26,0.32,0.74),11.5:(0.50,0.28,0.30,0.72),12.0:(0.50,0.24,0.32,0.76)}
c={"mediaId":4960,"level":"B","keyWord":"cuddle","defaultVoice":"female",
 "taps":[
  {"phrase":"to wear a mustard jacket","target":"the red-haired woman","voice":"female","keys":keys(R)},
  {"phrase":"to bury her face","target":"the woman with the black bag","voice":"female","keys":keys(D)},
  {"phrase":"to beam with closed eyes","target":"the red-haired woman","voice":"female","keys":keys(R)}],
 "stillS":0.0,
 "nouns":[{"word":"a pillar","x":0.10,"y":0.18,"voice":"female"},
          {"word":"an arrivals sign","x":0.82,"y":0.23,"voice":"female"},
          {"word":"a mustard jacket","x":0.70,"y":0.68,"voice":"female"},
          {"word":"a handbag","x":0.28,"y":0.88,"voice":"female"}],
 "question":"What is the red-haired woman doing?",
 "answer":["She","is","cuddling","a","dark-haired","woman."],
 "answerVoice":"female",
 "notes":"Everyone in the group hugs, so phrase 1 and 3 share the red-haired woman (mustard jacket is unique; she beams with closed eyes at 0-3.5 s and 11-12 s; another woman on the right also smiles with closed eyes at 11.5 s - verifier please check). 'to bury her face' = dark-haired woman with the black bag, face pressed into the shoulder, back to camera; boxes split along the line between the two heads; from 6 s on only her head is boxed because the mustard back covers her body. Later several dark-haired women join, the target is the one in the middle with the black bag strap."}
json.dump(c,open('content/4960.json','w'),indent=1)
