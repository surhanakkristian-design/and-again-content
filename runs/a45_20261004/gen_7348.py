import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
R={0.2:(0.45,0.15,0.32,0.57),0.7:(0.47,0.13,0.31,0.58),1.2:(0.44,0.12,0.33,0.61),1.7:(0.41,0.10,0.35,0.68),
   2.2:(0.40,0.19,0.35,0.74),2.7:(0.36,0.35,0.40,0.65),3.2:(0.28,0.33,0.48,0.67),3.7:(0.26,0.30,0.53,0.70)}
S={0.2:(0.77,0.44,0.18,0.29),0.7:(0.78,0.45,0.18,0.29),1.2:(0.77,0.44,0.19,0.30),1.7:(0.76,0.44,0.20,0.31),
   2.2:(0.75,0.43,0.22,0.30),2.7:(0.76,0.40,0.21,0.33),3.2:(0.76,0.39,0.20,0.31),3.7:(0.79,0.37,0.19,0.31)}
C={0.2:(0.26,0.66,0.19,0.17),0.7:(0.26,0.66,0.19,0.17),1.2:(0.25,0.67,0.19,0.17),1.7:(0.23,0.67,0.18,0.17),
   2.2:(0.21,0.67,0.19,0.17),2.7:(0.17,0.67,0.19,0.17),3.2:(0.09,0.67,0.19,0.17),3.7:(0.07,0.67,0.19,0.17)}
c={"mediaId":7348,"level":"B","keyWord":"a miller","defaultVoice":"female",
 "taps":[
  {"phrase":"to slide down a thick rope","target":"the woman on the rope","voice":"female","keys":[k(t,R[t]) for t in T]},
  {"phrase":"to grip the shutter latch","target":"the woman at the window","voice":"female","keys":[k(t,S[t]) for t in T]},
  {"phrase":"to pour flour into a sack","target":"the wooden chute","voice":"female","keys":[k(t,C[t]) for t in T]}],
 "stillS":1.2,
 "nouns":[{"word":"a cogwheel","x":0.35,"y":0.10,"voice":"female"},
          {"word":"a window","x":0.12,"y":0.46,"voice":"female"},
          {"word":"a miller","x":0.56,"y":0.47,"voice":"female"},
          {"word":"millstones","x":0.22,"y":0.63,"voice":"female"}],
 "question":"What is the miller doing?",
 "answer":["She","is","sliding","down","a","thick","rope."],
 "answerVoice":"female",
 "notes":"Single shot, camera tilts down at the end. The young man on the ladder is left out because he stands behind the rope woman. Rope-woman box is cut at x 0.76-0.79 next to the woman at the window (her knee/boot reaches past it at 0.2-1.2), and at the left next to the chute at 3.2/3.7 (her left elbow). 'the wooden chute' = the small wooden spout pouring flour into the sack, small target. 'millstones': two stones in one wooden case, pill on the left one. 'a miller' pill on the flour-covered rope woman."}
json.dump(c,open('content/7348.json','w'),indent=1)
