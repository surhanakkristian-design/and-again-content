import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 369
t=T(15)
bike={x:(0,0.62,1,0.38) for x in t}; bike[6.5]=(0,0.69,1,0.31)
car={4.0:(0.25,0.36,0.18,0.14),4.5:(0.30,0.38,0.20,0.14),5.0:(0.34,0.40,0.30,0.16),5.5:(0.36,0.40,0.18,0.14),
     6.0:(0.40,0.41,0.20,0.15),6.5:(0.42,0.42,0.58,0.26),7.0:(0.48,0.41,0.36,0.20)}
cl={x:(0,0.03,1,0.32) for x in t}
for x in (3.0,3.5,4.0,4.5): cl[x]=(0.2,0.03,0.8,0.32)
save({"mediaId":369,"level":"A","keyWord":"ride","defaultVoice":"male",
 "taps":[{"phrase":"to drive past the motorbike","target":"the car","voice":"male","keys":K(t,car)},
         {"phrase":"to have two mirrors","target":"the motorbike","voice":"male","keys":K(t,bike)},
         {"phrase":"to hang in the sky","target":"the clouds","voice":"male","keys":K(t,cl)}],
 "stillS":7.0,
 "nouns":[{"word":"a car","x":0.66,"y":0.51,"voice":"male"},{"word":"a road","x":0.28,"y":0.63,"voice":"male"},
          {"word":"a motorbike","x":0.32,"y":0.88,"voice":"male"},{"word":"the sky","x":0.40,"y":0.12,"voice":"male"}],
 "question":"What is the car doing?","answer":["It","is","driving","past","the","motorbike."],"answerVoice":"male",
 "notes":"Helmet-camera view: the rider is never visible, so the key verb 'ride' has no tappable doer; the motorbike phrase is a state (two mirrors). Several different cars come the other way from 4.0 s; target 'the car' = whichever oncoming car(s) are visible (5.0 and 6.5 show two, one box around both). Small car reflections in the right mirror at 6.0-7.0 lie inside the motorbike box."})

# ---------- 370
t=T(21)
girl={0.0:(0.02,0.14,0.90,0.86),0.5:(0.03,0.14,0.94,0.86),1.0:(0.04,0.15,0.94,0.85),1.5:(0,0.03,1,0.97),2.0:(0,0.14,1,0.86),
 2.5:(0,0,1,1),3.0:(0,0,1,1),3.5:(0,0.05,1,0.95),4.0:(0,0.10,1,0.90),4.5:(0,0.09,0.94,0.91),5.0:(0,0.06,0.86,0.94),
 5.5:(0.04,0.10,0.77,0.80),6.0:(0,0.08,0.75,0.70),6.5:(0.11,0.18,0.89,0.55),7.0:(0.11,0.41,0.89,0.53),7.5:(0.03,0.34,0.85,0.32),
 8.0:(0.35,0.30,0.51,0.37),8.5:(0.40,0.32,0.50,0.37),9.0:(0.42,0.32,0.52,0.40),9.5:(0.40,0.37,0.56,0.39),10.0:(0.04,0.47,0.96,0.37)}
hood={7.0:(0,0.06,0.10,0.54),7.5:(0,0,0.28,0.33),8.0:(0,0.02,0.34,0.50),8.5:(0,0.05,0.39,0.51),9.0:(0,0.09,0.40,0.56),
 9.5:(0,0.11,0.38,0.51),10.0:(0,0.09,0.34,0.37)}
bald={7.0:(0.10,0.08,0.18,0.32),7.5:(0.28,0.05,0.18,0.28),8.0:(0.34,0.06,0.18,0.23),8.5:(0.39,0.10,0.18,0.21),
 9.0:(0.40,0.13,0.18,0.18),9.5:(0.38,0.16,0.18,0.20),10.0:(0.34,0.14,0.18,0.32)}
save({"mediaId":370,"level":"A","keyWord":"helmet","defaultVoice":"female",
 "taps":[{"phrase":"to put on a helmet","target":"the girl","voice":"female","keys":K(t,girl)},
         {"phrase":"to hold a skateboard","target":"the man in the hood","voice":"male","keys":K(t,hood)},
         {"phrase":"to hold a cup","target":"the man at the back","voice":"male","keys":K(t,bald)}],
 "stillS":6.0,
 "nouns":[{"word":"a helmet","x":0.34,"y":0.17,"voice":"female"},{"word":"trousers","x":0.45,"y":0.55,"voice":"female"},
          {"word":"a skateboard","x":0.42,"y":0.75,"voice":"female"},{"word":"the sky","x":0.70,"y":0.05,"voice":"female"}],
 "question":"What is the girl putting on?","answer":["She","is","putting","on","a","red","helmet."],"answerVoice":"female",
 "notes":"From 7.0 s the three people stand close: boxes are split, the girl's legs/shoes (left of her body) are cut off at 8.0-9.5 so her box does not overlap the men, and the lower legs of the man at the back are cut at 8.0-9.5. The hooded man is cut by the frame edge at 7.0 (narrow box). He holds the girl's skateboard by his side (small, at his left hand) - check it is clear enough; the girl only rides it (5.0-6.5), never holds it."})

# ---------- 371
woman={0.5:(0,0.28,0.60,0.38),1.0:(0,0.12,0.56,0.54),1.5:(0,0.46,0.62,0.54),2.0:(0,0.26,0.96,0.74),2.5:(0,0.04,0.90,0.96),
 3.0:(0,0.41,1,0.59),3.5:(0,0,1,1),4.0:(0,0,1,1),4.5:(0,0,1,1),5.0:(0,0.02,0.94,0.98),5.5:(0,0.06,0.55,0.94),
 6.0:(0,0.44,0.59,0.44),6.5:(0,0,0.74,0.50),7.0:(0,0,0.64,0.47),7.5:(0,0.13,0.70,0.50),8.0:(0,0.26,0.53,0.40)}
man={5.5:(0.55,0,0.45,1),6.0:(0.59,0,0.41,1),6.5:(0.82,0,0.18,0.78),7.0:(0.82,0.04,0.18,0.62),7.5:(0.82,0,0.18,0.48),
 8.0:(0.71,0,0.29,0.46),8.5:(0.38,0,0.62,0.58),9.0:(0.34,0,0.66,0.76),9.5:(0.34,0,0.66,0.76),10.0:(0.26,0.02,0.74,0.98)}
save({"mediaId":371,"level":"B","keyWord":"herb","defaultVoice":"male",
 "taps":[{"phrase":"to rub the basil leaves","target":"the woman","voice":"female","keys":K(t,woman)},
         {"phrase":"to sprinkle herbs over spaghetti","target":"the woman","voice":"female","keys":K(t,woman)},
         {"phrase":"to raise his eyebrows","target":"the man","voice":"male","keys":K(t,man)}],
 "stillS":9.5,
 "nouns":[{"word":"herbs","x":0.22,"y":0.47,"voice":"male"},{"word":"a beard","x":0.74,"y":0.43,"voice":"male"},
          {"word":"spaghetti","x":0.52,"y":0.82,"voice":"male"},{"word":"a plate","x":0.22,"y":0.92,"voice":"male"}],
 "question":"What is the woman doing?","answer":["She","is","sprinkling","herbs","over","the","spaghetti."],"answerVoice":"female",
 "notes":"Only two possible targets, so the woman has two phrases. In the picking shots (0.5-3.0) and the sprinkling shots (6.5-8.0) only hands/an arm are visible; I read them as the woman's (bare forearm, white robe sleeve at the left edge at 6.5, the man in grey stands on the right) - the verifier should confirm. The man also smells the leaves (5.5-6.0), so no 'smell' phrase. At 5.5-6.0 the two overlap: vertical split, the tip of the man's nose / the woman's fingertips are cut. 'a plate' sits on the left rim, 'spaghetti' on the pasta."})

# ---------- 372
t=T(20)
man={0.0:(0.18,0.37,0.76,0.40),0.5:(0.18,0.40,0.72,0.40),1.5:(0.31,0.43,0.28,0.16),2.0:(0.18,0.23,0.31,0.54),
 2.5:(0.14,0.30,0.66,0.43),3.0:(0,0.34,1,0.66),3.5:(0.21,0.21,0.48,0.63),4.0:(0.02,0.33,0.98,0.54),4.5:(0.16,0.28,0.68,0.46),
 5.0:(0.15,0.49,0.70,0.33),5.5:(0.14,0.32,0.30,0.54),6.0:(0,0.04,0.76,0.50),6.5:(0,0,1,0.88),7.0:(0.08,0.23,0.68,0.63),
 7.5:(0.26,0.20,0.41,0.70),8.0:(0.30,0.30,0.34,0.43),8.5:(0.24,0.38,0.56,0.40),9.0:(0.49,0.35,0.35,0.38),9.5:(0.50,0.36,0.26,0.35)}
ball={0.0:(0.19,0.22,0.22,0.14),0.5:(0.21,0.22,0.22,0.16),1.0:(0.32,0.09,0.54,0.34),1.5:(0.36,0.29,0.20,0.14),
 2.0:(0.49,0.38,0.22,0.16),2.5:(0.45,0,0.55,0.29),3.0:(0.11,0,0.87,0.34),3.5:(0.38,0.06,0.20,0.14),4.5:(0.38,0.03,0.22,0.17),
 5.0:(0.20,0.27,0.50,0.21),5.5:(0.44,0.42,0.24,0.19),6.0:(0.37,0.54,0.24,0.14),7.0:(0.50,0.09,0.23,0.14),
 7.5:(0.41,0.06,0.21,0.14),8.0:(0.35,0.15,0.20,0.15),8.5:(0.37,0,0.20,0.14),9.0:(0.37,0.12,0.20,0.14),9.5:(0.31,0.35,0.18,0.14)}
save({"mediaId":372,"level":"B","keyWord":"trick","defaultVoice":"male",
 "taps":[{"phrase":"to juggle a football","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to perform a handstand","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to spin through the air","target":"the ball","voice":"male","keys":K(t,ball)}],
 "stillS":1.5,
 "nouns":[{"word":"skyscrapers","x":0.28,"y":0.10,"voice":"male"},{"word":"a football","x":0.46,"y":0.39,"voice":"male"},
          {"word":"a shadow","x":0.55,"y":0.72,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","performing","tricks","with","a","football."],"answerVoice":"male",
 "notes":"Only the man and the ball are possible targets (many cuts). Where the ball is in front of the man the boxes are split and the man's box loses a part: 2.0 (raised foot), 2.5 (thighs), 5.0 (only his shoes/lower legs), 5.5 (ball in front of his chest: the man's box is the left half of his body), 6.0 (feet). The key word 'trick' is abstract, so it is not a noun slot; it is in the answer. In the still (1.5 s, drone shot) the football is small. No ball visible at 4.0 and 6.5."})
