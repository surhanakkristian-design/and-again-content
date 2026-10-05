import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
G={0.0:(0.28,0.09,0.62,0.68),0.5:(0.30,0.09,0.58,0.72),1.0:(0.26,0.08,0.56,0.76),1.5:(0.33,0.15,0.58,0.74),2.0:(0.33,0.11,0.50,0.64),
2.5:(0.31,0.10,0.66,0.60),3.0:(0.21,0.07,0.76,0.80),3.5:(0.22,0.07,0.68,0.74),4.0:(0.33,0.12,0.49,0.54),4.5:(0.31,0.09,0.66,0.62),
5.0:(0.30,0.12,0.56,0.70),5.5:(0.30,0.15,0.46,0.66),6.0:(0.32,0.12,0.42,0.57),6.5:(0.34,0.12,0.42,0.50),7.0:(0.37,0.09,0.43,0.60),
7.5:(0.34,0.10,0.40,0.77),8.0:(0.38,0.02,0.50,0.84),8.5:(0.33,0,0.57,0.90),9.0:(0.33,0.08,0.59,0.87),9.5:(0.36,0.20,0.26,0.80),
10.0:(0.38,0.14,0.30,0.84)}
Y={0.0:(0.06,0.11,0.22,0.40),0.5:(0.08,0.10,0.22,0.39),1.0:(0.05,0.12,0.21,0.50),1.5:(0.12,0.12,0.21,0.50),2.0:(0.13,0.12,0.20,0.36),
2.5:(0.10,0.11,0.21,0.35),3.0:(0,0.05,0.18,0.32),3.5:(0.02,0.03,0.20,0.30),4.0:(0.14,0.03,0.19,0.29),4.5:(0.12,0.04,0.19,0.27),
5.0:(0.11,0.06,0.19,0.27),5.5:(0.08,0.09,0.20,0.27),6.0:(0.10,0.11,0.21,0.28),6.5:(0.14,0.11,0.20,0.30),7.0:(0.15,0.11,0.21,0.40),
7.5:(0.10,0.16,0.24,0.42),8.0:(0.10,0.18,0.28,0.36),8.5:(0.08,0.20,0.25,0.56),9.0:(0.03,0.12,0.30,0.84),9.5:(0,0.12,0.36,0.88)}
d={"mediaId":333,"level":"A","keyWord":"girl","defaultVoice":"female",
"taps":[{"phrase":"to jump over a rope","target":"the girl in jeans","voice":"female","keys":keys(G)},
{"phrase":"to wear a yellow T-shirt","target":"the girl in the yellow T-shirt","voice":"female","keys":keys(Y)},
{"phrase":"to put her hands up","target":"the girl in jeans","voice":"female","keys":keys(G)}],
"stillS":4.0,
"nouns":[{"word":"a woman","x":0.47,"y":0.07,"voice":"female"},{"word":"a wall","x":0.88,"y":0.07,"voice":"female"},{"word":"a girl","x":0.53,"y":0.38,"voice":"female"}],
"question":"What is the girl in jeans doing?","answer":["She","is","jumping","over","a","rope."],"answerVoice":"female",
"notes":"Two targets: the main girl and the girl in the yellow T-shirt (phrase 2 is a state: the other girls only watch, no action fits only one of them). The woman at the back is mostly behind the main girl's head, so she is not a target. The main girl's left arm/hand reaches over the yellow girl in many frames; her box is cut there (8.0-8.5 s: her raised left arm is outside her box). 10.0 s: the yellow girl is almost fully hidden in the hug (no yellow visible) -> off. Rope jumping is only 0-2.5 s, then she hops through chalk squares. 'a girl' pill sits on the main girl; several girls are in the picture."}
json.dump(d,open("content/333.json","w"),indent=1)
