import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def W(o): json.dump(o, open(f"content/{o['mediaId']}.json","w"), indent=1, ensure_ascii=False)
def T(n): return [round(i*0.5,1) for i in range(n)]

# 528
t=T(19)
cu=(0.05,0.08,0.95,0.92)
wom={0.0:cu,0.5:cu,1.0:(0.26,0.36,0.24,0.14),1.5:(0.50,0.36,0.24,0.15),2.0:cu,2.5:cu,
     3.5:(0.44,0.39,0.26,0.16),4.0:(0.48,0.38,0.26,0.16),4.5:(0.49,0.38,0.26,0.16),
     5.0:(0.0,0.45,0.76,0.32),5.5:(0.13,0.17,0.62,0.80),6.0:(0.02,0.07,0.60,0.91),
     6.5:(0.0,0.08,0.52,0.90),7.0:(0.10,0.11,0.53,0.87),7.5:(0.0,0.10,0.78,0.88)}
man={3.0:(0.19,0.29,0.55,0.57),8.0:(0.20,0.28,0.52,0.58)}
W({"mediaId":528,"level":"A","keyWord":"park","defaultVoice":"female",
 "taps":[
  {"phrase":"to park a car","target":"the woman","voice":"female","keys":K(t,wom)},
  {"phrase":"to sit on a wall","target":"the man","voice":"male","keys":K(t,man)},
  {"phrase":"to get out of the car","target":"the woman","voice":"female","keys":K(t,wom)}],
 "stillS":7.0,
 "nouns":[{"word":"a woman","x":0.33,"y":0.50,"voice":"female"},
          {"word":"a car","x":0.76,"y":0.70,"voice":"female"},
          {"word":"the sky","x":0.42,"y":0.06,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","parking","her","car."],
 "answerVoice":"female",
 "notes":"Cuts between woman close-up, street shots, the man on the wall (3.0, 8.0) and the empty parked car (8.5, 9.0: both off). At 5.0 only the woman's arm and hand with the key are visible; box is on the arm. At 1.0-4.5 the woman is a small figure behind the windscreen. Only 3 nouns: nothing else is clear and apart at 7.0."})

# 5288
t=T(17)
sk={0.0:(0.21,0.30,0.46,0.26),0.5:(0.33,0.31,0.37,0.25),1.0:(0.20,0.34,0.42,0.22),1.5:(0.24,0.33,0.43,0.26),
    2.0:(0.44,0.36,0.42,0.25),2.5:(0.29,0.34,0.35,0.25),3.0:(0.32,0.34,0.40,0.25),3.5:(0.38,0.39,0.48,0.24),
    4.0:(0.41,0.37,0.28,0.20),4.5:(0.21,0.38,0.33,0.22),5.0:(0.24,0.39,0.35,0.22),5.5:(0.32,0.38,0.38,0.24),
    6.0:(0.34,0.29,0.47,0.29),6.5:(0.38,0.23,0.46,0.32),7.0:(0.33,0.29,0.53,0.34),7.5:(0.25,0.42,0.48,0.25),
    8.0:(0.17,0.41,0.37,0.24)}
W({"mediaId":5288,"level":"A","keyWord":"ski","defaultVoice":"male",
 "taps":[
  {"phrase":"to ski down a hill","target":"the skier in red","voice":"male","keys":K(t,sk)},
  {"phrase":"to wear a red suit","target":"the skier in red","voice":"male","keys":K(t,sk)},
  {"phrase":"to jump in the air","target":"the skier in red","voice":"male","keys":K(t,sk)}],
 "stillS":7.0,
 "nouns":[{"word":"skis","x":0.58,"y":0.56,"voice":"male"},
          {"word":"mountains","x":0.40,"y":0.22,"voice":"male"},
          {"word":"the sky","x":0.50,"y":0.06,"voice":"male"},
          {"word":"snow","x":0.50,"y":0.86,"voice":"male"}],
 "question":"What is the person in red doing?",
 "answer":["He","is","skiing","down","a","hill."],
 "answerVoice":"male",
 "notes":"One clear target only (the skier in red); the other skiers are tiny dots far away, so all three phrases use him. Gender is not visible (helmet); 'He' follows the packet description. The jump is at about 6.5-7.0 s (skier off the snow, shadow apart). 'to wear a red suit' is a state."})

# 7811
t=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom={0.2:(0.30,0.33,0.36,0.48),0.7:(0.37,0.40,0.29,0.47),1.2:(0.30,0.56,0.38,0.38),1.7:(0.23,0.57,0.37,0.39),
     2.2:(0.13,0.55,0.45,0.40),2.7:(0.08,0.54,0.42,0.39),3.2:(0.03,0.54,0.45,0.39),3.7:(0.0,0.53,0.45,0.39)}
man={0.2:(0.02,0.45,0.27,0.32),0.7:(0.15,0.49,0.22,0.35),1.7:(0.61,0.56,0.22,0.40),2.2:(0.62,0.53,0.20,0.44),
     2.7:(0.62,0.51,0.20,0.44),3.2:(0.56,0.50,0.22,0.45),3.7:(0.51,0.49,0.24,0.46)}
mac={0.2:(0.78,0.20,0.22,0.63),0.7:(0.79,0.26,0.21,0.64),1.2:(0.79,0.33,0.21,0.62),1.7:(0.83,0.34,0.17,0.62),
     2.2:(0.82,0.34,0.18,0.62),2.7:(0.82,0.32,0.18,0.62),3.2:(0.78,0.32,0.22,0.62),3.7:(0.75,0.32,0.25,0.62)}
W({"mediaId":7811,"level":"B","keyWord":"dozens","defaultVoice":"female",
 "taps":[
  {"phrase":"to swing a tennis racket","target":"the woman in white","voice":"female","keys":K(t,wom)},
  {"phrase":"to grab the ball machine","target":"the man in green","voice":"male","keys":K(t,man)},
  {"phrase":"to launch dozens of balls","target":"the ball machine","voice":"female","keys":K(t,mac)}],
 "stillS":3.7,
 "nouns":[{"word":"clouds","x":0.45,"y":0.20,"voice":"female"},
          {"word":"a ball machine","x":0.82,"y":0.53,"voice":"female"},
          {"word":"a racket","x":0.12,"y":0.80,"voice":"female"},
          {"word":"tennis balls","x":0.45,"y":0.93,"voice":"female"}],
 "question":"What is the ball machine doing?",
 "answer":["It","is","launching","dozens","of","tennis","balls."],
 "answerVoice":"female",
 "notes":"At 1.2 the man is almost fully hidden behind the woman: off. From 1.7 the man stands in front of the ball machine and holds it; the two boxes are split along a vertical line, so the machine box covers only its right part. The machine fires balls only in the first ~2 s. Small players at the far fence are not targets."})

# 526
t=T(21)
full=(0.04,0.07,0.96,0.90)
wom={0.0:(0.24,0.24,0.76,0.76),0.5:(0.0,0.48,0.72,0.52),1.0:(0.0,0.48,0.40,0.52),
     4.0:(0.0,0.30,0.16,0.66),4.5:(0.0,0.24,0.37,0.73),5.0:(0.0,0.25,0.37,0.75),5.5:(0.0,0.30,0.34,0.70),
     6.0:(0.0,0.23,0.34,0.74),6.5:(0.0,0.24,0.29,0.73),7.0:(0.0,0.28,0.36,0.72),7.5:(0.0,0.27,0.39,0.69),
     8.0:(0.0,0.39,0.52,0.50),8.5:(0.05,0.62,0.55,0.26),9.0:(0.05,0.30,0.40,0.19),9.5:(0.08,0.27,0.40,0.22),
     10.0:(0.16,0.27,0.36,0.22)}
man={0.0:(0.0,0.10,0.24,0.82),0.5:(0.38,0.10,0.54,0.38),1.0:(0.40,0.10,0.60,0.86),
     2.0:full,2.5:full,3.0:full,3.5:full,
     4.0:(0.16,0.07,0.84,0.90),4.5:(0.37,0.07,0.63,0.90),5.0:(0.37,0.04,0.63,0.95),5.5:(0.34,0.07,0.66,0.90),
     6.0:(0.34,0.07,0.66,0.88),6.5:(0.29,0.07,0.71,0.88),7.0:(0.36,0.10,0.64,0.90),7.5:(0.39,0.14,0.61,0.80),
     8.0:(0.52,0.14,0.48,0.78),8.5:(0.0,0.27,1.0,0.35),9.0:(0.05,0.49,0.95,0.48),9.5:(0.05,0.49,0.95,0.48),
     10.0:(0.05,0.49,0.95,0.42)}
W({"mediaId":526,"level":"B","keyWord":"paralyze","defaultVoice":"female",
 "taps":[
  {"phrase":"to fire a ray gun","target":"the woman","voice":"female","keys":K(t,wom)},
  {"phrase":"to clutch a white mug","target":"the man","voice":"male","keys":K(t,man)},
  {"phrase":"to topple over backwards","target":"the man","voice":"male","keys":K(t,man)}],
 "stillS":10.0,
 "nouns":[{"word":"goggles","x":0.37,"y":0.38,"voice":"female"},
          {"word":"a cactus","x":0.72,"y":0.48,"voice":"female"},
          {"word":"a tracksuit","x":0.50,"y":0.62,"voice":"female"},
          {"word":"a pipe","x":0.50,"y":0.17,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","paralyzing","the","man","with","a","ray","gun."],
 "answerVoice":"female",
 "notes":"The two people overlap in many frames (0.5, 1.0, 5.0-8.0, 8.5-10.0), so the boxes are split and each misses a part of its target (e.g. the man's raised hand at 7.0-8.0, his feet at 8.5, the woman's legs at 9.0-10.0, her hair at 0.5). 1.5 is a close-up of the ray gun: both off. 'a pipe' = the big ventilation pipe under the ceiling; goggles and cactus pills are close (0.10 in y)."})
