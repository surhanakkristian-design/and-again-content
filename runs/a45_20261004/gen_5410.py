import json
T=[i*0.5 for i in range(25)]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
man={0.0:(0.74,0.17,0.26,0.50),0.5:(0.76,0.17,0.24,0.50),1.0:(0.76,0.28,0.24,0.50),1.5:(0.78,0.28,0.22,0.58),
2.0:(0.0,0.0,0.66,1.0),2.5:(0.03,0.04,0.97,0.96),
3.0:(0,0.15,1,0.85),3.5:(0,0.15,1,0.85),4.0:(0,0.15,1,0.85),4.5:(0,0.15,1,0.85),5.0:(0,0.15,1,0.85),5.5:(0,0.15,1,0.85),
6.0:(0,0.13,1,0.87),6.5:(0,0.13,1,0.87),7.0:(0,0.15,1,0.85),7.5:(0,0.15,1,0.85),
8.0:(0.53,0.34,0.47,0.66),8.5:(0.50,0.38,0.50,0.62),9.0:(0.55,0.32,0.45,0.68),9.5:(0.46,0.30,0.54,0.70),
10.0:(0.20,0.24,0.80,0.76),10.5:(0.25,0.11,0.75,0.89),11.0:(0.48,0.04,0.52,0.96),11.5:(0.50,0.05,0.50,0.95),12.0:(0.50,0.0,0.50,1.0)}
cup={8.0:(0.0,0.54,0.20,0.25),8.5:(0.0,0.54,0.20,0.25),9.0:(0.0,0.56,0.20,0.24),9.5:(0.0,0.56,0.20,0.24),
10.0:(0.0,0.57,0.19,0.23),10.5:(0.0,0.59,0.19,0.22),11.0:(0.0,0.63,0.20,0.22),11.5:(0.0,0.64,0.22,0.22),12.0:(0.0,0.66,0.22,0.22)}
M=[k(t,man[t]) for t in T]; C=[k(t,cup.get(t)) for t in T]
c={"mediaId":5410,"level":"A","keyWord":"toothbrush","defaultVoice":"male",
"taps":[{"phrase":"to brush his teeth","target":"the man","voice":"male","keys":M},
{"phrase":"to smile at the mirror","target":"the man","voice":"male","keys":M},
{"phrase":"to stand in a white cup","target":"the toothbrush in the cup","voice":"male","keys":C}],
"stillS":8.0,
"nouns":[{"word":"a toothbrush","x":0.13,"y":0.62,"voice":"male"},
{"word":"a cup","x":0.12,"y":0.72,"voice":"male"},
{"word":"a tap","x":0.57,"y":0.62,"voice":"male"},
{"word":"a towel","x":0.16,"y":0.87,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","brushing","his","teeth."],"answerVoice":"male",
"notes":"From 8.0 s the man's reflection is visible in the mirror; boxes cover only the real man (reflection is the same person, at 10.0 s the boxes overlap part of it). 0.0-1.5 s only his hand is visible (box on the hand). A second green toothbrush already stands in the cup from 8.0 s; his own brush ends lying on the towel, not in the cup (description says otherwise). 'to stand in a white cup' targets the brush in the cup."}
json.dump(c,open("content/5410.json","w"),indent=1)
