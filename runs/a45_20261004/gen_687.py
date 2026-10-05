import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
B={0.0:(0.28,0.08,0.62,0.92),0.5:(0.20,0.05,0.80,0.95),1.0:(0.05,0.02,0.95,0.98),1.5:(0,0,1,1),2.0:(0,0.02,1,0.98),
2.5:(0,0,0.82,0.94),3.0:(0,0,0.68,0.85),3.5:(0,0,0.68,0.60),4.0:(0.02,0,0.52,0.60),4.5:(0.20,0,0.60,0.64),
5.0:(0.27,0.02,0.57,0.78),5.5:(0.25,0.13,0.63,0.72),6.0:(0.24,0.19,0.58,0.52),6.5:(0.15,0.05,0.63,0.55),
7.0:(0.26,0.28,0.56,0.42),7.5:(0.25,0.20,0.50,0.48),8.0:(0.23,0.24,0.40,0.49),8.5:(0.19,0.28,0.48,0.51),
9.0:(0.21,0.43,0.47,0.49),9.5:(0.33,0.36,0.38,0.56),10.0:(0.45,0.38,0.33,0.42)}
S={3.5:(0.70,0.10,0.26,0.14),4.0:(0.70,0.05,0.26,0.18),4.5:(0.81,0.06,0.19,0.16),6.0:(0.45,0.06,0.26,0.12),
7.0:(0.13,0.05,0.26,0.14),7.5:(0.08,0.04,0.26,0.14),8.0:(0.15,0.09,0.26,0.14),8.5:(0.26,0.13,0.26,0.14),
9.0:(0.32,0.17,0.26,0.14),9.5:(0.34,0.20,0.26,0.14),10.0:(0.36,0.21,0.26,0.14)}
c={"mediaId":687,"level":"A","keyWord":"skateboard","defaultVoice":"male",
"taps":[
{"phrase":"to ride a skateboard","target":"the boy","voice":"male","keys":keys(B)},
{"phrase":"to jump into the air","target":"the boy","voice":"male","keys":keys(B)},
{"phrase":"to shine over the city","target":"the sun","voice":"male","keys":keys(S)}],
"stillS":8.5,
"nouns":[{"word":"the sun","x":0.38,"y":0.20,"voice":"male"},{"word":"houses","x":0.74,"y":0.31,"voice":"male"},
{"word":"a boy","x":0.37,"y":0.45,"voice":"male"},{"word":"a skateboard","x":0.58,"y":0.64,"voice":"male"}],
"question":"What is the boy doing?",
"answer":["He","is","riding","a","skateboard."],
"answerVoice":"male",
"notes":"Only one person as a target (walkers with a dog are tiny background figures), so the boy has two phrases; third target is the sun. The sun is boxed only where its disc/glow is clearly in the picture (3.5-4.5, 6.0, 7.0-10.0); off where it is behind the lamp post or the boy's head (5.0, 5.5, 6.5) and in the early close-ups. The boy's box includes the skateboard he holds or rides. The jump is at 6.5. At 0.0-1.0 the camera person's hand is in front of the boy."}
json.dump(c,open("content/687.json","w"),indent=1)
