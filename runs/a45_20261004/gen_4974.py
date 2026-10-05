import json
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
S={0.0:(0,0.09,0.66,0.91),0.5:(0,0.03,0.66,0.97),1.0:(0,0,0.66,1),1.5:(0,0,0.66,1),2.0:(0,0,0.66,1),2.5:(0,0,0.66,1),
 3.0:(0,0.26,0.70,0.74),3.5:(0,0.24,0.62,0.76),4.0:(0,0.23,0.66,0.77),4.5:(0,0.24,0.60,0.76),5.0:(0,0.24,0.70,0.76),
 5.5:(0,0.23,0.70,0.77),6.0:(0,0.09,0.66,0.91),6.5:(0,0.02,0.66,0.98),7.0:(0,0,0.66,1),7.5:(0,0.08,0.70,0.92),
 8.0:(0,0.27,0.72,0.73),8.5:(0,0.26,0.67,0.74),9.0:(0.02,0.25,0.73,0.75),9.5:(0.06,0.24,0.74,0.76),10.0:(0,0.21,0.48,0.79),
 10.5:(0,0.19,0.60,0.81),11.0:(0,0.19,0.58,0.81),11.5:(0,0.19,0.62,0.81),12.0:(0,0.18,0.60,0.82)}
C={0.0:(0.68,0.28,0.32,0.34),0.5:(0.68,0.30,0.32,0.32),1.0:(0.68,0.30,0.32,0.32),1.5:(0.68,0.30,0.32,0.32),2.0:(0.68,0.32,0.32,0.30),
 2.5:(0.68,0.32,0.32,0.30),3.0:(0.72,0.30,0.28,0.30),3.5:(0.64,0.30,0.36,0.30),4.0:(0.68,0.30,0.32,0.32),4.5:(0.62,0.28,0.38,0.32),
 5.0:(0.72,0.30,0.28,0.25),5.5:(0.72,0.30,0.28,0.28),6.0:(0.68,0.30,0.32,0.30),6.5:(0.68,0.30,0.32,0.30),7.0:(0.68,0.33,0.32,0.30),
 7.5:(0.72,0.33,0.28,0.30),8.0:(0.74,0.30,0.26,0.20),8.5:(0.69,0.30,0.31,0.28),9.0:(0.77,0.30,0.23,0.25),9.5:(0.82,0.28,0.18,0.22),
 10.0:(0.50,0.26,0.50,0.22),10.5:(0.62,0.28,0.38,0.22),11.0:(0.60,0.28,0.40,0.18),11.5:(0.64,0.27,0.36,0.25),12.0:(0.62,0.27,0.38,0.24)}
c={"mediaId":4974,"level":"B","keyWord":"a seller","defaultVoice":"male",
 "taps":[
  {"phrase":"to pour tea from above","target":"the seller","voice":"male","keys":K(S)},
  {"phrase":"to hand out small cups","target":"the seller","voice":"male","keys":K(S)},
  {"phrase":"to cheer him on","target":"the crowd","voice":"male","keys":K(C)}],
 "stillS":12.0,
 "nouns":[{"word":"a seller","x":0.22,"y":0.45,"voice":"male"},{"word":"a crowd","x":0.70,"y":0.31,"voice":"male"},
  {"word":"a garland","x":0.30,"y":0.10,"voice":"male"},{"word":"steel cups","x":0.52,"y":0.59,"voice":"male"}],
 "question":"What is the seller doing?",
 "answer":["He","is","pouring","tea","from","a","height."],"answerVoice":"male",
 "notes":"Target 3 is the group 'the crowd' of young men (no single crowd member does something only he does). Crowd box is the part right of / above the seller; the seller's outstretched arm/jug is cut off at the split line where they overlap (9.0-11.0). Phrases 1+2 share the seller."}
json.dump(c,open('content/4974.json','w'),indent=1)
