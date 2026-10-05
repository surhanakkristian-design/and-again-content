import json
def keys(d,n):
    out=[]
    for i in range(n):
        t=i*0.5
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
def save(d): json.dump(d,open("content/%d.json"%d["mediaId"],"w"),indent=1)

# 341 goat
G={0.0:(0.04,0.06,0.62,0.72),0.5:(0.08,0,0.62,0.67),1.0:(0,0.02,0.92,0.62),1.5:(0,0.10,0.82,0.57),2.0:(0,0.14,0.80,0.47),
2.5:(0,0.14,0.82,0.52),3.0:(0,0.12,0.80,0.70),3.5:(0,0.08,0.76,0.84),4.0:(0,0.05,0.68,0.80),4.5:(0.03,0,0.70,0.92),
5.0:(0,0.09,0.68,0.91),5.5:(0,0.23,0.85,0.77),6.0:(0,0.14,0.88,0.82),6.5:(0,0.17,0.85,0.78),7.0:(0.03,0,0.97,0.68),
7.5:(0,0.08,1,0.76),8.0:(0,0,0.93,0.63),8.5:(0,0.02,1,0.63),9.0:(0,0.07,0.95,0.73),9.5:(0,0.08,0.98,0.70),10.0:(0,0.20,0.93,0.47)}
k=keys(G,21)
save({"mediaId":341,"level":"A","keyWord":"goat","defaultVoice":"male",
"taps":[{"phrase":"to climb a stone wall","target":"the goat","voice":"male","keys":k},
{"phrase":"to bite a white shirt","target":"the goat","voice":"male","keys":k},
{"phrase":"to stand on the roof","target":"the goat","voice":"male","keys":k}],
"stillS":9.5,
"nouns":[{"word":"the sky","x":0.25,"y":0.08,"voice":"male"},{"word":"a goat","x":0.30,"y":0.36,"voice":"male"},
{"word":"a roof","x":0.72,"y":0.58,"voice":"male"},{"word":"a wall","x":0.60,"y":0.86,"voice":"male"}],
"question":"What is the goat biting?","answer":["It","is","biting","a","white","shirt."],"answerVoice":"male",
"notes":"Only one real target (the goat); the hens are tiny and visible for a few frames only, the washing does nothing. All three phrases use the goat. At 9.5 s a red tiled roof is also visible bottom left (0.10,0.60); the 'a roof' pill sits on the slate roof under the goat. The goat bites/pulls the white shirt at 4.0-5.0 s."})

# 342 goggles
W={0.0:(0,0.08,1,0.86),0.5:(0,0.10,1,0.84),1.0:(0,0.10,1,0.86),1.5:(0,0.10,1,0.86),3.0:(0,0.12,1,0.86),3.5:(0,0.12,1,0.86),
4.0:(0.18,0,0.66,0.88),4.5:(0,0.18,1,0.62),5.0:(0,0.20,1,0.80),5.5:(0.05,0.18,0.95,0.78),6.5:(0,0.05,1,0.90),7.0:(0,0.08,1,0.90),
8.5:(0.08,0.12,0.92,0.82),9.0:(0.08,0.12,0.86,0.86)}
M={2.0:(0.02,0.05,0.98,0.95),2.5:(0.02,0.05,0.98,0.95),7.5:(0.12,0.02,0.86,0.98),8.0:(0,0.02,0.96,0.98)}
kw=keys(W,19); km=keys(M,19)
save({"mediaId":342,"level":"A","keyWord":"goggles","defaultVoice":"female",
"taps":[{"phrase":"to put on blue goggles","target":"the girl","voice":"female","keys":kw},
{"phrase":"to point a finger","target":"the man","voice":"male","keys":km},
{"phrase":"to swim under the water","target":"the girl","voice":"female","keys":kw}],
"stillS":1.5,
"nouns":[{"word":"a cap","x":0.50,"y":0.20,"voice":"female"},{"word":"goggles","x":0.50,"y":0.41,"voice":"female"},
{"word":"water","x":0.14,"y":0.55,"voice":"female"},{"word":"a swimsuit","x":0.50,"y":0.85,"voice":"female"}],
"question":"What is the girl putting on?","answer":["She","is","putting","on","blue","goggles."],"answerVoice":"female",
"notes":"Two targets, never in the same shot (cuts), so boxes fill most of each shot. Girl is off at 6.0 s (only the pool wall and bubbles). The man points his finger at 8.0 s only; he also holds a stopwatch (not A-level word, not used). 'a cap' = her swimming cap."})

# 344 gold
W={0.0:(0,0,1,0.75),0.5:(0,0,0.97,0.74),1.0:(0.16,0.08,0.68,0.68),1.5:(0.18,0.09,0.64,0.66),2.0:(0.17,0.15,0.66,0.63),
2.5:(0,0,0.88,1),3.0:(0,0,0.93,1),3.5:(0,0,1,1),4.0:(0,0,1,1),4.5:(0,0,1,1),5.0:(0,0.03,0.70,0.72),5.5:(0,0,0.82,0.78),
6.0:(0.12,0.10,0.70,0.66),6.5:(0.12,0.12,0.74,0.64),7.0:(0.05,0.12,0.72,0.62),7.5:(0.09,0.13,0.70,0.61),8.0:(0.05,0.13,0.82,0.62),
8.5:(0.21,0.19,0.58,0.58),9.0:(0.20,0.30,0.56,0.57)}
k=keys(W,19)
save({"mediaId":344,"level":"A","keyWord":"gold","defaultVoice":"female",
"taps":[{"phrase":"to lift something heavy","target":"the woman","voice":"female","keys":k},
{"phrase":"to clean a gold bar","target":"the woman","voice":"female","keys":k},
{"phrase":"to wear a gold chain","target":"the woman","voice":"female","keys":k}],
"stillS":6.0,
"nouns":[{"word":"glasses","x":0.52,"y":0.31,"voice":"female"},{"word":"a jacket","x":0.50,"y":0.56,"voice":"female"},
{"word":"a gold bar","x":0.78,"y":0.70,"voice":"female"},{"word":"a chain","x":0.42,"y":0.80,"voice":"female"}],
"question":"What is the woman cleaning?","answer":["She","is","cleaning","a","gold","bar."],"answerVoice":"female",
"notes":"Only one acting target (the woman); the gold bar is in her hands in almost every frame, so it cannot get its own box. All three phrases use the woman; her box includes the bar while she holds it. Key word 'gold' appears as 'a gold bar' (bare 'gold' would also fit the chain and the bangles). She has a second pair of glasses on her head at 6.0 s; the pill is on the pair she wears. The chain lies on the table at 6.0 s; she wears it from 7.0 s."})

# 346 golf
W={0.0:(0,0.33,0.48,0.67),0.5:(0,0.35,0.40,0.46),3.0:(0,0.22,0.33,0.62),3.5:(0.40,0.06,0.58,0.48),4.0:(0.38,0.06,0.56,0.66),
4.5:(0.42,0.05,0.56,0.70),5.0:(0.49,0.03,0.45,0.83),5.5:(0.49,0.30,0.20,0.22),6.0:(0.47,0.30,0.22,0.16),6.5:(0.47,0.30,0.22,0.18),
7.0:(0.48,0.30,0.22,0.19),7.5:(0.47,0.28,0.22,0.23),8.0:(0.49,0.21,0.22,0.30),8.5:(0.51,0.23,0.20,0.28),9.0:(0.47,0.29,0.21,0.23),
9.5:(0.47,0.30,0.20,0.22),10.0:(0.51,0.33,0.19,0.17)}
M={1.5:(0.54,0.50,0.46,0.50),2.0:(0.39,0.49,0.61,0.51),2.5:(0.34,0.44,0.66,0.56),5.5:(0.14,0.29,0.24,0.23),6.0:(0.13,0.29,0.24,0.22),
6.5:(0.13,0.29,0.24,0.22),7.0:(0.13,0.29,0.24,0.22),7.5:(0.13,0.29,0.24,0.22),8.0:(0.13,0.28,0.24,0.23),8.5:(0.17,0.22,0.25,0.29),
9.0:(0.22,0.23,0.24,0.29),9.5:(0.22,0.23,0.25,0.29),10.0:(0.32,0.25,0.19,0.25)}
B={0.0:(0.66,0.84,0.22,0.16),3.0:(0.33,0.66,0.18,0.14),3.5:(0.43,0.54,0.18,0.14),4.0:(0.40,0.72,0.20,0.14),4.5:(0.36,0.75,0.20,0.14),
5.0:(0.29,0.76,0.20,0.14),6.0:(0.42,0.46,0.18,0.14),6.5:(0.41,0.48,0.18,0.14),7.0:(0.39,0.49,0.24,0.14)}
save({"mediaId":346,"level":"A","keyWord":"golf","defaultVoice":"female",
"taps":[{"phrase":"to play golf","target":"the woman","voice":"female","keys":keys(W,21)},
{"phrase":"to hold a red flag","target":"the man","voice":"male","keys":keys(M,21)},
{"phrase":"to roll on the grass","target":"the ball","voice":"female","keys":keys(B,21)}],
"stillS":7.0,
"nouns":[{"word":"the sky","x":0.45,"y":0.12,"voice":"female"},{"word":"a flag","x":0.22,"y":0.34,"voice":"female"},
{"word":"a ball","x":0.50,"y":0.55,"voice":"female"},{"word":"a hole","x":0.55,"y":0.84,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","playing","golf."],"answerVoice":"female",
"notes":"Ball: at 0.0 s it sits on the tee (bottom right); in the air (1.0-2.0 s) it is a speck and is off; off at 5.5 s and after 7.0 s (it has dropped into the hole, not seen going in). Ball and woman are close at 3.0-5.0 s and 6.0-7.0 s: boxes split, at 3.5 s the woman's box stops at her knees, at 3.0 s it cuts her cap brim. Man and woman meet at 9.5-10.0 s: split along the line between them. The man holds the flagstick with the red flag from 5.5 s (in the first shot, 1.5-2.5 s, he only watches the ball). The red flag at 7.0 s is small; the pill also covers the man beside it."})
