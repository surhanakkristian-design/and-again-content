import json
T=[i*0.5 for i in range(19)]
W={0.0:(0,0.14,0.36,0.80),0.5:(0,0.14,0.33,0.80),1.0:(0,0.18,0.30,0.82),1.5:(0,0.20,0.38,0.80),
2.0:(0.08,0.19,0.39,0.60),2.5:(0.14,0.23,0.37,0.44),3.0:(0,0.24,0.46,0.60),3.5:(0,0.16,0.52,0.74),
4.0:(0,0.21,0.53,0.58),4.5:(0.18,0.22,0.41,0.54),5.0:(0.22,0.26,0.35,0.58),5.5:(0.26,0.28,0.33,0.52),
6.0:(0.28,0.24,0.33,0.40),6.5:(0.09,0.20,0.62,0.45),7.0:(0.14,0.33,0.52,0.49),7.5:(0.14,0.41,0.53,0.45),
8.0:(0.18,0.30,0.59,0.26),8.5:(0.29,0.39,0.42,0.25),9.0:(0.33,0.42,0.28,0.20)}
K={0.0:(0.53,0.27,0.18,0.14),0.5:(0.54,0.27,0.18,0.14),1.0:(0.52,0.27,0.18,0.14),1.5:(0.48,0.28,0.18,0.14),
2.0:(0.47,0.27,0.18,0.14),2.5:(0.51,0.28,0.18,0.15),3.0:(0.64,0.34,0.20,0.14)}
B={0.0:(0.57,0.43,0.18,0.14),0.5:(0.58,0.42,0.18,0.14),1.0:(0.57,0.42,0.18,0.14),1.5:(0.53,0.43,0.18,0.14),
2.0:(0.48,0.46,0.18,0.14),4.0:(0.80,0.33,0.18,0.14),4.5:(0.82,0.34,0.18,0.14),5.0:(0.82,0.37,0.18,0.14)}
def keys(D):
    return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else {"t":t,"off":True} for t in T]
d={"mediaId":4135,"level":"A","keyWord":"ball","defaultVoice":"female",
"taps":[
 {"phrase":"to kick the ball","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to stand in the goal","target":"the keeper","voice":"female","keys":keys(K)},
 {"phrase":"to lie on the grass","target":"the ball","voice":"female","keys":keys(B)}],
"stillS":0.0,
"nouns":[{"word":"a woman","x":0.14,"y":0.42,"voice":"female"},
 {"word":"a ball","x":0.66,"y":0.51,"voice":"female"},
 {"word":"a goal","x":0.63,"y":0.32,"voice":"female"},
 {"word":"grass","x":0.55,"y":0.80,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","kicking","a","ball."],
"answerVoice":"female",
"notes":"The keeper is a small far figure (gender not visible -> default voice); boxed 0-3.0 s (at 3.0 lying after the dive), gone afterwards. The ball lies on the spot 0-2.0 s; at 2.5-3.5 it is not findable (off); at 4.0-5.0 it is a tiny dot on the grass at the right edge and has a minimum-size box. The woman kicks at about 2.0-2.5 s, then runs and jumps off the edge. The noun 'a goal' sits on the goal frame, where the keeper also stands (no noun for the keeper). 'grass' pill is far from the others; the woman's shadow lies on the grass too."}
json.dump(d,open("content/4135.json","w"),indent=1,ensure_ascii=False)
