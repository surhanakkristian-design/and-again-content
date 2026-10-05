import json
def K(times, rows):
    out=[]
    for t,r in zip(times,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    assert len(times)==len(rows)
    return out
def T(n): return [round(i*0.5,1) for i in range(n)]
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4210
t=T(20)
ham=K(t,[(0.15,0.17,0.70,0.80)]*15+[(0.0,0.17,1.0,0.80)]*5)
save({"mediaId":4210,"level":"B","keyWord":"hold","defaultVoice":"female",
 "taps":[{"phrase":"to grip two wooden sticks","target":"the hamster","voice":"female","keys":ham},
         {"phrase":"to conceal its face","target":"the hamster","voice":"female","keys":ham},
         {"phrase":"to grin at the camera","target":"the hamster","voice":"female","keys":ham}],
 "stillS":9.5,
 "nouns":[{"word":"an ice cream bar","x":0.76,"y":0.45,"voice":"female"},
          {"word":"a hamster","x":0.45,"y":0.75,"voice":"female"},
          {"word":"a counter","x":0.50,"y":0.95,"voice":"female"}],
 "question":"What is the hamster doing?",
 "answer":["It","is","holding","up","two","ice","cream","bars."],
 "answerVoice":"female",
 "notes":"Only one possible target (the hamster; the bars overlap it), so all three phrases use it. From 7.5 s the box is the full width because the arms with the bars reach both edges. Two ice cream bars are visible at 9.5 s; the pill sits on the right one (bitten), the left one is at the frame edge. 'a counter' pill is on the wooden surface under the feet."})

# 402
t=T(21)
W=[(0,0.17,0.50,0.55),(0,0.17,0.51,0.55),(0,0.16,0.45,0.72),(0,0.05,0.42,0.82),(0,0.02,0.42,0.73),(0,0.02,0.45,0.72),
   (0,0.05,0.45,0.73),(0,0.03,0.47,0.62),(0,0,0.46,0.48),(0,0,0.45,0.44),(0,0,0.47,0.42),(0,0,0.35,0.35),
   (0,0.24,0.20,0.16),(0,0,0.18,0.48),(0,0,0.25,0.84),(0,0.10,0.37,0.90),(0,0.22,0.31,0.58),(0.07,0.33,0.50,0.40),
   (0.15,0.37,0.34,0.40),(0.25,0.37,0.30,0.37),(0.30,0.40,0.23,0.22)]
M=[(0.52,0.15,0.48,0.53),(0.52,0.17,0.48,0.50),(0.52,0.25,0.48,0.58),(0.52,0.10,0.48,0.75),(0.52,0.08,0.48,0.65),(0.52,0.08,0.48,0.63),
   (0.52,0,0.48,0.76),(0.50,0.03,0.50,0.70),(0.48,0,0.52,0.44),(0.46,0,0.54,0.42),(0.49,0,0.51,0.42),(0.48,0,0.52,0.46),
   (0.35,0,0.65,0.58),(0.76,0,0.24,0.72),(0.76,0,0.24,0.92),(0.80,0.03,0.20,0.97),(0.57,0.07,0.43,0.75),(0.67,0.12,0.33,0.70),
   (0.74,0.27,0.26,0.68),(0.74,0.17,0.26,0.78),(0.72,0.19,0.28,0.66)]
wk=K(t,W); mk=K(t,M)
save({"mediaId":402,"level":"A","keyWord":"ice","defaultVoice":"female",
 "taps":[{"phrase":"to slide on the ice","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to wear a green hat","target":"the man","voice":"male","keys":mk},
         {"phrase":"to wear a red jacket","target":"the woman","voice":"female","keys":wk}],
 "stillS":9.5,
 "nouns":[{"word":"the sky","x":0.45,"y":0.12,"voice":"female"},
          {"word":"trees","x":0.18,"y":0.36,"voice":"female"},
          {"word":"a woman","x":0.45,"y":0.50,"voice":"female"},
          {"word":"ice","x":0.40,"y":0.85,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","sliding","on","the","ice."],
 "answerVoice":"female",
 "notes":"Two of the phrases are states (hat, jacket): both people crouch and touch the ice, so few actions fit only one. At 6.0-6.5 s the woman is only partly in the picture (glove / face at the left edge), box kept small. The man is cut by the right edge from 6.5 s. A black bird stands on the ice from 6.5 s; not used."})

# 4190
t=T(24)
C=[(0,0.45,0.50,0.50),(0,0.46,0.50,0.50),(0,0.47,0.50,0.50),(0,0.48,0.52,0.48),(0,0.50,0.49,0.46),(0,0.52,0.50,0.45),
   (0,0.50,0.53,0.48),(0,0.48,0.55,0.50),(0.03,0.46,0.62,0.50),(0,0.42,0.70,0.54),(0,0.42,0.72,0.58),(0.03,0.43,0.68,0.57),
   (0.08,0.42,0.62,0.55),(0,0.43,0.70,0.54),(0.08,0.43,0.61,0.55),(0.08,0.42,0.60,0.56),(0.03,0.43,0.64,0.54),(0.02,0.43,0.66,0.55),
   (0,0.52,0.63,0.48),(0,0.52,0.74,0.48),(0,0.52,0.68,0.45),(0,0.50,0.70,0.47),(0,0.51,0.72,0.49),(0,0.51,0.72,0.49)]
L=[(0.51,0.14,0.41,0.48),(0.36,0.12,0.54,0.34),(0.25,0.10,0.60,0.37),(0.53,0.08,0.47,0.75),(0.20,0,0.80,0.49),(0.13,0,0.87,0.51),
   (0.54,0.02,0.46,0.80),(0.56,0.03,0.44,0.82),(0.28,0,0.72,0.46),(0.32,0,0.68,0.41),(0.36,0,0.64,0.41),(0.38,0,0.62,0.42),
   (0.44,0,0.56,0.41),(0.47,0.05,0.53,0.37),(0.48,0.09,0.52,0.33),(0.69,0.17,0.31,0.50),(0.68,0.22,0.32,0.45),(0.69,0.25,0.31,0.38),
   (0.64,0.29,0.36,0.45),(0.55,0.29,0.36,0.23),(0.55,0.28,0.30,0.23),(0.53,0.30,0.26,0.19),(0.53,0.30,0.26,0.19),(0.52,0.30,0.26,0.19)]
ck=K(t,C); lk=K(t,L)
save({"mediaId":4190,"level":"A","keyWord":"meet","defaultVoice":"female",
 "taps":[{"phrase":"to sit on a wall","target":"the cat","voice":"female","keys":ck},
         {"phrase":"to have long dark hair","target":"the male lion","voice":"female","keys":lk},
         {"phrase":"to look at the camera","target":"the cat","voice":"female","keys":ck}],
 "stillS":11.5,
 "nouns":[{"word":"trees","x":0.45,"y":0.18,"voice":"female"},
          {"word":"a lion","x":0.70,"y":0.38,"voice":"female"},
          {"word":"grass","x":0.82,"y":0.50,"voice":"female"},
          {"word":"a cat","x":0.35,"y":0.78,"voice":"female"}],
 "question":"What is the cat doing?",
 "answer":["It","is","meeting","a","big","lion."],
 "answerVoice":"female",
 "notes":"The lion phrase is a state (the mane, in A-level words): everything the male lion does (come to the bars, show teeth, walk away) the lioness does too. The lioness is not a target. The cat sits in front of the lion, so the boxes are split: in most frames the lion box is the mane and eyes above the cat's ears, in some the part right of the cat. 'a lion' pill sits on the male lion in the distance at 11.5 s; the lioness is close to its left (also a lion, so no wrong reading). 'grass' is the green strip on the right."})

# 5652
t=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
D=[(0.04,0.54,0.36,0.23),(0.04,0.54,0.39,0.23),(0.02,0.54,0.38,0.23),(0,0.53,0.36,0.24),(0.02,0.57,0.41,0.20),
   (0.15,0.57,0.41,0.20),(0.10,0.57,0.48,0.20),(0.13,0.56,0.42,0.21)]
B=[(0.41,0.34,0.54,0.40),(0.44,0.34,0.51,0.40),(0.41,0.34,0.54,0.40),(0.37,0.34,0.58,0.40),(0.44,0.34,0.51,0.40),
   (0.30,0.34,0.65,0.23),(0.30,0.34,0.65,0.23),(0.30,0.34,0.65,0.22)]
S=[(0.11,0.77,0.18,0.14)]*8
save({"mediaId":5652,"level":"A","keyWord":"big","defaultVoice":"female",
 "taps":[{"phrase":"to smell the big ball","target":"the dog","voice":"female","keys":K(t,D)},
         {"phrase":"to be taller than the dog","target":"the big ball","voice":"female","keys":K(t,B)},
         {"phrase":"to be the smallest ball","target":"the small ball","voice":"female","keys":K(t,S)}],
 "stillS":1.7,
 "nouns":[{"word":"trees","x":0.35,"y":0.18,"voice":"female"},
          {"word":"a ball","x":0.65,"y":0.50,"voice":"female"},
          {"word":"a dog","x":0.18,"y":0.66,"voice":"female"},
          {"word":"grass","x":0.60,"y":0.90,"voice":"female"}],
 "question":"What is the dog doing?",
 "answer":["It","is","smelling","a","big","ball."],
 "answerVoice":"female",
 "notes":"The two ball phrases are states (the balls do nothing). 'to be taller than the dog' is 6 words with 'to'. The dog stands in front of the big ball: until 2.2 s the ball box starts right of the dog's nose, from 2.7 s it is the part of the ball above the dog. 'a ball' pill is on the giant ball; the small ball lies bottom left and has no noun."})
