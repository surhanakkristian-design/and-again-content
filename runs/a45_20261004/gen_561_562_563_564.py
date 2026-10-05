import json
T=[i*0.5 for i in range(21)]
OFF=None
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
def xyxy(x0,y0,x1,y1): return (round(x0,2),round(y0,2),round(x1-x0,2),round(y1-y0,2))
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 561
W={t:(0,0,1,1) for t in T if t<=5.0}; M={t:None for t in T if t<=5.0}
sp={5.5:(0.43,0.13,0.20),6.0:(0.44,0.15,0.20),6.5:(0.45,0.15,0.22),7.0:(0.47,0.2,0.22),7.5:(0.47,0.2,0.22),
    8.0:(0.5,0.17,0.23),8.5:(0.5,0.19,0.24),9.0:(0.48,0.2,0.25),9.5:(0.5,0.2,0.25),10.0:(0.49,0.2,0.25)}
for t,(s,my,wy) in sp.items():
    M[t]=xyxy(0,my,s,1); W[t]=xyxy(s+0.01,wy,1,1)
kw,km=keys(W),keys(M)
save({"mediaId":561,"level":"B","keyWord":"pleasure","defaultVoice":"female",
 "taps":[{"phrase":"to offer him a piece","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to accept a small piece","target":"the man","voice":"male","keys":km},
         {"phrase":"to clutch a paper bag","target":"the woman","voice":"female","keys":kw}],
 "stillS":6.0,
 "nouns":[{"word":"dreadlocks","x":0.16,"y":0.24,"voice":"female"},
          {"word":"a beanie","x":0.77,"y":0.27,"voice":"female"},
          {"word":"a croissant","x":0.72,"y":0.52,"voice":"female"},
          {"word":"a scarf","x":0.68,"y":0.76,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","eating","a","croissant","with","great","pleasure."],
 "answerVoice":"female",
 "notes":"Key word 'pleasure' is abstract, so it is only in the answer. Woman fills the frame until 5.0 s (man off). From 6.5 s her arm reaches into the man's box (split is a vertical line between the bodies). 'to clutch a paper bag': she holds the bag with the croissant all clip long. Both people eat croissant, so no 'to eat/bite' phrase."})

# ---------- 562
L={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0.2,0,0.6,1),1.5:xyxy(0.1,0,0.62,0.24),2.0:xyxy(0,0,0.52,0.22),2.5:xyxy(0.08,0,0.6,0.17),
   8.5:xyxy(0.17,0.15,0.45,0.75),9.0:xyxy(0.18,0.14,0.48,0.27),9.5:xyxy(0.17,0.14,0.47,0.29),10.0:xyxy(0.17,0.14,0.47,0.31)}
Wo={1.5:xyxy(0,0.25,0.6,1),2.0:xyxy(0,0.23,0.5,1),2.5:xyxy(0,0.18,0.54,1),3.0:xyxy(0,0,0.66,1),3.5:xyxy(0.15,0,1,0.4),4.0:xyxy(0.8,0,1,0.16),
    5.5:xyxy(0,0.03,0.66,1),6.0:xyxy(0,0,0.62,1),6.5:xyxy(0,0,0.64,1),
    8.5:xyxy(0,0.15,0.16,0.95),9.0:xyxy(0,0.28,0.56,0.97),9.5:xyxy(0.03,0.3,0.69,0.97),10.0:xyxy(0.02,0.32,0.71,0.97)}
Ma={1.5:xyxy(0.66,0.2,1,1),2.0:xyxy(0.52,0.23,1,1),2.5:xyxy(0.56,0.19,1,1),3.0:xyxy(0.67,0,1,0.62),
    5.5:xyxy(0.67,0.1,1,1),6.0:xyxy(0.63,0.1,1,1),6.5:xyxy(0.65,0.1,1,1),
    8.5:xyxy(0.47,0.27,1,1),9.0:xyxy(0.57,0.32,1,1),9.5:xyxy(0.7,0.33,1,1),10.0:xyxy(0.72,0.3,1,1)}
save({"mediaId":562,"level":"A","keyWord":"plug","defaultVoice":"female",
 "taps":[{"phrase":"to hold up a plug","target":"the woman","voice":"female","keys":keys(Wo)},
         {"phrase":"to hold a blue cup","target":"the man","voice":"male","keys":keys(Ma)},
         {"phrase":"to light up the room","target":"the lamp","voice":"female","keys":keys(L)}],
 "stillS":6.0,
 "nouns":[{"word":"a woman","x":0.25,"y":0.22,"voice":"female"},
          {"word":"a plug","x":0.48,"y":0.56,"voice":"female"},
          {"word":"a cup","x":0.78,"y":0.68,"voice":"female"},
          {"word":"a hand","x":0.28,"y":0.86,"voice":"female"}],
 "question":"What is the woman holding up?",
 "answer":["She","is","holding","up","a","white","plug."],
 "answerVoice":"female",
 "notes":"Clip with cuts. The hand holding the cable (3.5-4.0 s) and the plug (5.5-6.5 s) is taken as the woman's (grey cardigan sleeve). Hands at the socket 7.0-8.0 s: owner not visible, all targets off. Plug alone on the floor 4.5-5.0 s: all off. Lamp is lit at 0.0 s and from 8.5 s, dark in between; from 9.0 s only the shade/top is boxed because the woman sits in front of the pole. At 10.0 s the woman's bun is cut by the split to the man."})

# ---------- 563
bird={0.0:(0.29,0.16),0.5:(0.31,0.15),1.0:(0.30,0.14),1.5:(0.31,0.12),2.0:(0.30,0.11),2.5:(0.28,0.10),3.0:(0.27,0.09),3.5:(0.30,0.12),
 4.0:(0.27,0.11),4.5:(0.25,0.10),5.0:(0.23,0.10),5.5:(0.24,0.09),6.0:(0.22,0.08),6.5:(0.25,0.09),7.0:(0.27,0.11),7.5:(0.29,0.12),
 8.0:(0.29,0.13),8.5:(0.31,0.14),9.0:(0.31,0.15),9.5:(0.31,0.15),10.0:(0.30,0.16)}
split={0.0:.28,0.5:.27,1.0:.28,1.5:.26,2.0:.33,2.5:.28,3.0:.28,3.5:.28,4.0:.30,4.5:.27,5.0:.24,5.5:.22,6.0:.20,6.5:.23,7.0:.27,7.5:.29,8.0:.30,8.5:.32,9.0:.33,9.5:.29,10.0:.31}
jtop={0.0:.21,0.5:.2,1.0:.19,1.5:.17,2.0:.16,2.5:.18,3.0:.17,3.5:.17,4.0:.19,4.5:.15,5.0:.2,5.5:.18,6.0:.17,6.5:.17,7.0:.18,7.5:.17,8.0:.18,8.5:.2,9.0:.25,9.5:.24,10.0:.24}
B={};S={};J={}
for t in T:
    bx,by=bird[t]; y0=max(0,by-0.09); y1=y0+0.14
    B[t]=xyxy(bx-0.09,y0,bx+0.09,y1)
    S[t]=xyxy(0,y1+0.01,split[t],1)
    J[t]=xyxy(split[t]+0.01,max(jtop[t],y1+0.01),1,1)
save({"mediaId":563,"level":"A","keyWord":"pocket","defaultVoice":"male",
 "taps":[{"phrase":"to look in his pockets","target":"the red-haired man","voice":"male","keys":keys(J)},
         {"phrase":"to hold two coffee cups","target":"the dark-haired man","voice":"male","keys":keys(S)},
         {"phrase":"to sit on a wall","target":"the bird","voice":"male","keys":keys(B)}],
 "stillS":6.5,
 "nouns":[{"word":"a bird","x":0.25,"y":0.09,"voice":"male"},
          {"word":"keys","x":0.70,"y":0.46,"voice":"male"},
          {"word":"a cup","x":0.15,"y":0.54,"voice":"male"},
          {"word":"a pocket","x":0.80,"y":0.76,"voice":"male"}],
 "question":"What is the red-haired man doing?",
 "answer":["He","is","looking","in","his","pockets."],
 "answerVoice":"male",
 "notes":"The dark-haired man holds two takeaway cups (clear at 0.0, 2.0, 4.0 s). The bird sits on the stone gate post of the wall the whole clip. 'a pocket' pill is on the lower jacket pocket at 6.5 s; the jacket has several pockets. At 1.5 s the red-haired man's elbow crosses in front of the other man (vertical split)."})

# ---------- 564
R={0.0:(0.1,0.27,0.37,0.47),0.5:(0.05,0.27,0.35,0.49),1.0:(0,0.3,0.3,0.54),1.5:(0,0.28,0.3,0.57),2.0:(0.01,0.26,0.32,0.55),2.5:(0.1,0.2,0.31,0.55),
   3.5:(0.41,0.32,0.59,0.62),4.0:(0.4,0.32,0.59,0.52),4.5:(0.4,0.33,0.59,0.54),5.0:(0.39,0.34,0.58,0.54),5.5:(0.4,0.37,0.59,0.55),6.0:(0.39,0.33,0.59,0.55),
   6.5:(0.38,0.2,0.64,0.62),7.0:(0.36,0.06,0.66,0.66),7.5:(0.37,0.08,0.66,0.69),8.0:(0.38,0.15,0.66,0.68),8.5:(0.37,0.14,0.64,0.67),9.0:(0.37,0.12,0.65,0.67),
   9.5:(0.35,0.23,0.63,0.76),10.0:(0.4,0.3,0.63,0.62)}
Mn={0.0:(0.38,0.17,0.63,0.57),0.5:(0.37,0.16,0.65,0.6),1.0:(0.33,0.17,0.68,0.37),1.5:(0.32,0.25,0.70,0.47),2.0:(0.33,0.2,0.64,0.45),2.5:(0.32,0.17,0.57,0.47),
    3.0:(0.05,0.18,0.52,0.70),3.5:(0,0.08,0.40,0.74),4.0:(0.05,0.06,0.38,0.66),4.5:(0.04,0.07,0.38,0.68),5.0:(0,0.07,0.37,0.67),5.5:(0,0.07,0.37,0.67),
    6.0:(0.01,0.09,0.37,0.69),6.5:(0,0.12,0.37,0.72),7.0:(0.02,0.17,0.35,0.88),7.5:(0.02,0.19,0.36,0.89),8.0:(0.04,0.2,0.37,0.77),8.5:(0,0.19,0.36,0.77),
    9.0:(0,0.15,0.36,0.87),9.5:(0,0.21,0.34,0.84),10.0:(0.02,0.34,0.39,0.72)}
G={0.0:(0.65,0.27,0.9,0.47),0.5:(0.67,0.28,0.97,0.5),1.0:(0.72,0.31,1,0.57),1.5:(0.74,0.27,1,0.58),2.0:(0.65,0.26,1,0.6),2.5:(0.6,0.27,1,0.61),
   3.0:(0.58,0.31,0.98,0.73),3.5:(0.6,0.21,1,0.73),4.0:(0.6,0.17,0.96,0.7),4.5:(0.6,0.17,0.96,0.72),5.0:(0.62,0.17,0.98,0.72),5.5:(0.62,0.17,0.98,0.72),
   6.0:(0.63,0.18,0.96,0.72),6.5:(0.66,0.21,0.98,0.75),7.0:(0.67,0.27,0.97,0.92),7.5:(0.67,0.29,0.97,0.94),8.0:(0.67,0.29,0.97,0.82),8.5:(0.65,0.26,1,0.8),
   9.0:(0.66,0.2,1,0.89),9.5:(0.64,0.28,1,0.88),10.0:(0.64,0.41,1,0.76)}
f=lambda d:{t:xyxy(*v) for t,v in d.items()}
save({"mediaId":564,"level":"B","keyWord":"podium","defaultVoice":"female",
 "taps":[{"phrase":"to shove the tallest block","target":"the man","voice":"male","keys":keys(f(Mn))},
         {"phrase":"to give a military salute","target":"the woman in green","voice":"female","keys":keys(f(G))},
         {"phrase":"to occupy the top step","target":"the woman in dark red","voice":"female","keys":keys(f(R))}],
 "stillS":7.5,
 "nouns":[{"word":"the ceiling","x":0.30,"y":0.06,"voice":"female"},
          {"word":"a tracksuit","x":0.20,"y":0.50,"voice":"female"},
          {"word":"a leotard","x":0.80,"y":0.56,"voice":"female"},
          {"word":"a podium","x":0.50,"y":0.86,"voice":"female"}],
 "question":"Where is the winner standing?",
 "answer":["She","is","standing","on","top","of","the","podium."],
 "answerVoice":"female",
 "notes":"Man pushes the tall yellow block 0.0-1.5 s (the women push the low ones). Woman in green salutes at 4.0-4.5 s. Woman in dark red is hidden behind the man at 3.0 s (off) and stands on the top step from 6.5 s. The woman in dark red also wears a tracksuit: the 'a tracksuit' pill sits on the man's. Raised fists / spread arms of the winner stick slightly out of her box at 7.0-8.0 s where they pass over the others."})
