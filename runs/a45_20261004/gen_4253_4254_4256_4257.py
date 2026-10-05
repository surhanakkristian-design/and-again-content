import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T24=[i*0.5 for i in range(24)]; T14=[i*0.5 for i in range(14)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4253
R={0.0:(0.02,0.05,0.65,0.90),0.5:(0.15,0.07,0.68,0.88),1.0:(0.03,0.03,0.87,0.97),1.5:(0.05,0,0.95,1),
 2.0:(0,0,0.85,1),2.5:(0.02,0,0.82,1),3.0:(0.08,0,0.62,1),3.5:(0.24,0,0.48,1),4.0:(0.36,0,0.44,1),
 4.5:(0.38,0,0.38,1),5.0:(0.43,0,0.37,1),5.5:(0.45,0,0.37,1),6.0:(0.42,0,0.30,1),6.5:(0.34,0,0.48,1),
 7.0:(0.37,0,0.52,1),7.5:(0.33,0,0.63,1),8.0:(0.35,0,0.60,1),8.5:(0.25,0,0.75,1),9.0:(0.29,0,0.71,1),
 9.5:(0.32,0,0.68,1),10.0:(0.10,0.05,0.90,0.95),10.5:(0.28,0.03,0.72,0.97),11.0:(0.33,0,0.67,1)}
S={3.5:(0,0,0.24,0.56),4.0:(0,0.04,0.36,0.30),4.5:(0,0.06,0.38,0.30),5.0:(0.05,0.10,0.38,0.30),
 5.5:(0.12,0.08,0.33,0.32),6.0:(0.08,0.09,0.34,0.30),6.5:(0,0.10,0.34,0.32),7.0:(0,0.09,0.37,0.34),
 7.5:(0,0.17,0.33,0.32),8.0:(0,0.13,0.35,0.28),8.5:(0,0.18,0.25,0.40),9.0:(0,0.20,0.29,0.42),9.5:(0.02,0.20,0.30,0.21)}
Kn={3.0:(0.70,0.36,0.30,0.64),3.5:(0.72,0.44,0.28,0.56),4.0:(0.80,0.66,0.20,0.34),4.5:(0.76,0.48,0.24,0.52),
 5.0:(0.80,0.48,0.20,0.52),5.5:(0.82,0.50,0.18,0.50),6.0:(0.72,0.50,0.28,0.50),6.5:(0.82,0.48,0.18,0.52)}
save({"mediaId":4253,"level":"A","keyWord":"to wash","defaultVoice":"male",
 "taps":[{"phrase":"to sit on a bike","target":"the man on the bike","voice":"male","keys":K(T24,R)},
  {"phrase":"to clean the helmet","target":"the standing man","voice":"male","keys":K(T24,S)},
  {"phrase":"to wash the bike","target":"the kneeling man","voice":"male","keys":K(T24,Kn)}],
 "stillS":9.0,
 "nouns":[{"word":"a helmet","x":0.52,"y":0.12,"voice":"male"},{"word":"a cap","x":0.20,"y":0.26,"voice":"male"},{"word":"a bike","x":0.45,"y":0.86,"voice":"male"}],
 "question":"What is happening to the bike?","answer":["Two","men","are","washing","the","bike."],"answerVoice":"male",
 "notes":"Three men close together: boxes are split by vertical lines, so the rider's box is a narrow column while the helpers are in frame and misses his elbow. Standing man set off at 3.0 (sliver at the edge) and at 10.0/10.5 (mostly hidden behind the rider). Kneeling man rubs the mud off the bike in the water spray; the standing man only wipes the helmet. Answer says 'two men' although only one works on the bike itself the whole time."})

# 4254
P={}; C={}; F={}
for t in (0.0,0.5,1.0,2.0,2.5,3.0,3.5): P[t]=(0,0.34,0.40,0.50); C[t]=(0.48,0.19,0.52,0.58)
P[1.5]=(0,0.34,0.49,0.50); C[1.5]=(0.51,0.19,0.49,0.58)
for t in (4.0,4.5,5.0,5.5): P[t]=(0,0.18,1,0.82)
for t in (6.0,6.5,7.0,7.5): C[t]=(0,0,1,1)
P[8.0]=(0.08,0.07,0.60,0.66); C[8.0]=(0.68,0.14,0.32,0.30)
P[8.5]=(0.05,0.36,0.70,0.50); C[8.5]=(0.76,0.55,0.24,0.22); F[8.5]=(0.36,0.19,0.34,0.17)
F[9.0]=(0.46,0,0.34,0.23)
F[9.5]=(0,0.14,0.31,0.16); C[9.5]=(0.31,0.05,0.69,0.95)
F[10.0]=(0,0.14,0.29,0.17); C[10.0]=(0.29,0.04,0.71,0.96)
F[10.5]=(0.03,0.21,0.27,0.16); C[10.5]=(0.30,0.05,0.70,0.95)
F[11.0]=(0,0.28,0.22,0.16); C[11.0]=(0.24,0.05,0.76,0.95)
F[11.5]=(0,0.38,0.24,0.16); C[11.5]=(0.26,0.05,0.74,0.95)
save({"mediaId":4254,"level":"B","keyWord":"counter","defaultVoice":"female",
 "taps":[{"phrase":"to perch on the counter","target":"the pigeon","voice":"female","keys":K(T24,P)},
  {"phrase":"to glare at the pigeon","target":"the cat","voice":"female","keys":K(T24,C)},
  {"phrase":"to float through the air","target":"the feather","voice":"female","keys":K(T24,F)}],
 "stillS":3.0,
 "nouns":[{"word":"a pigeon","x":0.18,"y":0.52,"voice":"female"},{"word":"a chef's hat","x":0.80,"y":0.29,"voice":"female"},
  {"word":"an apron","x":0.73,"y":0.66,"voice":"female"},{"word":"a counter","x":0.45,"y":0.88,"voice":"female"}],
 "question":"Where is the pigeon?","answer":["The","pigeon","is","perched","on","the","metal","counter."],"answerVoice":"female",
 "notes":"Feather exists only from 8.5 s on. At 8.0/8.5 only the cat's paw is in the shot (small box). Pigeon is in the fryer from 9.0 on -> off. Cat off at 9.0 (sliver of paw at the right edge). The fryer is set into the counter, so no 'a fryer' noun next to 'a counter'."})

# 4256
H={0.0:(0,0.42,0.58,0.58),0.5:(0,0.39,0.56,0.61),1.0:(0,0.37,0.56,0.63),1.5:(0,0.37,0.58,0.63),2.0:(0,0.37,0.58,0.63),
 2.5:(0,0.39,0.60,0.61),3.0:(0,0.39,0.59,0.61),3.5:(0,0.43,0.62,0.57),4.0:(0,0.45,0.62,0.55),4.5:(0,0.47,0.62,0.53),
 5.0:(0,0.60,0.32,0.40),5.5:(0,0.56,0.30,0.44),6.0:(0,0.45,0.26,0.50),6.5:(0,0.41,0.30,0.50)}
Kg={0.0:(0.28,0.09,0.60,0.33),0.5:(0.26,0.07,0.62,0.32),1.0:(0.25,0.02,0.58,0.35),1.5:(0.28,0.03,0.58,0.34),2.0:(0.28,0.07,0.58,0.30),
 2.5:(0.28,0.03,0.64,0.36),3.0:(0.59,0.03,0.41,0.97),3.5:(0.24,0,0.76,0.43),4.0:(0.20,0,0.80,0.45),4.5:(0.15,0.05,0.85,0.42),
 5.0:(0.32,0.28,0.68,0.72),5.5:(0.30,0.28,0.62,0.70),6.0:(0.26,0.22,0.74,0.70),6.5:(0.30,0.18,0.70,0.76)}
save({"mediaId":4256,"level":"B","keyWord":"scratch","defaultVoice":"female",
 "taps":[{"phrase":"to scratch the kangaroo's chest","target":"the hand","voice":"female","keys":K(T14,H)},
  {"phrase":"to stretch out on the grass","target":"the kangaroo","voice":"female","keys":K(T14,Kg)},
  {"phrase":"to lean into the hand","target":"the kangaroo","voice":"female","keys":K(T14,Kg)}],
 "stillS":1.5,
 "nouns":[{"word":"a kangaroo","x":0.55,"y":0.27,"voice":"female"},{"word":"a sleeve","x":0.20,"y":0.72,"voice":"female"},
  {"word":"the sky","x":0.22,"y":0.10,"voice":"female"},{"word":"grass","x":0.82,"y":0.52,"voice":"female"}],
 "question":"What is the hand doing?","answer":["It","is","scratching","the","kangaroo's","chest."],"answerVoice":"female",
 "notes":"Hand and sleeve lie across the kangaroo, so the two cannot both be boxed whole: while it stands (0-2.5, 3.5-4.5 s) the kangaroo's box is only the part ABOVE the hand (head, ears, shoulders / back) and the hand's box is hand + sleeve below, which also covers the belly behind the hand; lying down (5.0 s on) the split is vertical. Only a hand of the person is seen -> evenId voice (female). 'to lean into the hand' is subtle (2.5-3.5 s)."})

# 4257
P={}; T={}; F={}
for t in (0.0,0.5,1.0): P[t]=(0,0.25,0.50,0.63)
T[0.0]=(0.50,0.41,0.50,0.42); T[0.5]=(0.54,0.41,0.46,0.42); T[1.0]=(0.50,0.40,0.50,0.44)
P[1.5]=(0,0.26,0.52,0.62); T[1.5]=(0.55,0.40,0.45,0.45)
P[2.0]=(0,0.26,0.50,0.60); T[2.0]=(0.54,0.40,0.46,0.42)
P[2.5]=(0,0.26,0.50,0.60); T[2.5]=(0.52,0.40,0.48,0.42)
P[3.0]=(0,0.26,0.50,0.60); T[3.0]=(0.54,0.39,0.46,0.48)
P[3.5]=(0,0.26,0.44,0.60); T[3.5]=(0.62,0.37,0.38,0.50); F[3.5]=(0.44,0.50,0.18,0.14)
F[4.0]=(0,0.07,1,0.90)
P[4.5]=(0,0.05,0.31,0.95); F[4.5]=(0.31,0.32,0.40,0.40); T[4.5]=(0.73,0.27,0.27,0.73)
P[5.0]=(0.03,0.22,0.50,0.70); T[5.0]=(0.57,0.45,0.40,0.47)
P[5.5]=(0,0.04,0.58,0.42); T[5.5]=(0.58,0.14,0.40,0.34)
P[6.0]=(0,0.04,0.56,0.40); T[6.0]=(0.56,0.14,0.44,0.34)
P[6.5]=(0.15,0.17,0.40,0.44); T[6.5]=(0.55,0.29,0.38,0.33)
for t in (7.0,7.5,9.0): P[t]=(0.12,0.24,0.42,0.40); T[t]=(0.54,0.33,0.34,0.31)
F[7.0]=(0.34,0.65,0.32,0.17); F[7.5]=(0.34,0.65,0.32,0.17)
for t in (8.0,8.5): P[t]=(0.12,0.24,0.42,0.39); T[t]=(0.54,0.33,0.34,0.30)
F[8.0]=(0.34,0.63,0.32,0.20); F[8.5]=(0.34,0.64,0.32,0.19)
P[9.5]=(0.12,0.23,0.44,0.41); T[9.5]=(0.56,0.33,0.33,0.31)
for t in (10.0,10.5,11.0): P[t]=(0,0.19,0.57,0.61); T[t]=(0.57,0.33,0.43,0.47)
P[11.5]=(0,0.19,0.61,0.61); T[11.5]=(0.61,0.33,0.39,0.47)
save({"mediaId":4257,"level":"A","keyWord":"tight","defaultVoice":"male",
 "taps":[{"phrase":"to hug the turtle tight","target":"the panda","voice":"male","keys":K(T24,P)},
  {"phrase":"to get a big hug","target":"the turtle","voice":"male","keys":K(T24,T)},
  {"phrase":"to watch from the water","target":"the fish","voice":"male","keys":K(T24,F)}],
 "stillS":8.0,
 "nouns":[{"word":"a panda","x":0.32,"y":0.37,"voice":"male"},{"word":"a turtle","x":0.70,"y":0.52,"voice":"male"},
  {"word":"a fish","x":0.50,"y":0.74,"voice":"male"},{"word":"water","x":0.75,"y":0.87,"voice":"male"}],
 "question":"What is the panda doing?","answer":["The","panda","is","hugging","the","turtle","tight."],"answerVoice":"male",
 "notes":"Fish off at 3.0 (faint shape far behind); small box between the two heads at 3.5. 5.0 is a motion-blurred shot, boxes are rough. In the hug the panda's arm lies over the turtle: split by a vertical line. 'tight' used as adverb (hug tight)."})
