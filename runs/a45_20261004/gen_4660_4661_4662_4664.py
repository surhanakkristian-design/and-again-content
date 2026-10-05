import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4660
t=T(23)
F=(0,0,1,1)
w={0.0:F,0.5:F,1.0:(0,0,1,0.38),1.5:(0,0,1,0.72),2.0:F,2.5:F,3.0:(0,0.12,1,0.74),3.5:(0,0.05,0.95,0.66),
 4.0:(0.03,0,0.92,0.71),4.5:(0.08,0.06,0.88,0.74),5.0:(0.06,0.02,0.83,0.86),5.5:(0.08,0.04,0.78,0.86),
 6.0:(0.06,0.10,0.76,0.70),6.5:(0.2,0.11,0.66,0.69),7.0:(0.18,0.04,0.68,0.88),7.5:(0.2,0.04,0.66,0.88),
 8.0:(0.18,0.04,0.66,0.6),8.5:(0.2,0.02,0.64,0.6),9.0:(0.2,0.02,0.62,0.62),9.5:(0.22,0.02,0.6,0.6),
 10.0:(0.2,0.02,0.6,0.58),10.5:(0.22,0.02,0.58,0.58),11.0:(0.2,0.02,0.56,0.6)}
l={1.0:(0.47,0.48,0.18,0.14),1.5:(0.47,0.86,0.18,0.14),3.0:(0.38,0.86,0.18,0.14),3.5:(0.35,0.71,0.18,0.14),4.0:(0.36,0.71,0.18,0.14)}
save({"mediaId":4660,"level":"A","keyWord":"a pile","defaultVoice":"female",
 "taps":[{"phrase":"to carry many boxes","target":"the woman","voice":"female","keys":K(t,w)},
         {"phrase":"to drop the boxes","target":"the woman","voice":"female","keys":K(t,w)},
         {"phrase":"to roll on the floor","target":"the lipstick","voice":"female","keys":K(t,l)}],
 "stillS":10.0,
 "nouns":[{"word":"a woman","x":0.50,"y":0.30,"voice":"female"},{"word":"the floor","x":0.20,"y":0.44,"voice":"female"},
          {"word":"a hat","x":0.76,"y":0.78,"voice":"female"},{"word":"a pile","x":0.40,"y":0.88,"voice":"female"}],
 "question":"What is the woman carrying?",
 "answer":["She","is","carrying","a","pile","of","boxes."],"answerVoice":"female",
 "notes":"Lipstick is a small target: visible on the floor only at 1.0, 1.5, 3.0, 3.5, 4.0 s. At 0.0/0.5 s it is falling in front of the woman's boxes (inside her box) so it is set off there. At 3.0/3.5 s the woman's box is cut at the bag bottoms to leave room for the lipstick. 'a pile' pill sits on the heap of boxes at the end; 'a hat' is the black hat lying in the heap."})

# ---------- 4661
t=T(21)
top={0.0:0.43,0.5:0.46,1.0:0.59,1.5:0.66,2.0:0.52,2.5:0.42,3.0:0.40,3.5:0.69,4.0:0.86,4.5:0.68,5.0:0.47,5.5:0.41,
 6.0:0.39,6.5:0.38,7.0:0.38,7.5:0.39,8.0:0.38,8.5:0.39,9.0:0.59,9.5:0.56,10.0:0.34}
xs={0.0:(0.16,0.68),0.5:(0.16,0.68),1.0:(0.16,0.70),1.5:(0.20,0.66),2.0:(0.16,0.68),2.5:(0.18,0.64),3.0:(0.20,0.62),
 3.5:(0.20,0.66),4.0:(0.37,0.33),4.5:(0.2,0.66),5.0:(0.19,0.63),5.5:(0.19,0.63),6.0:(0.20,0.62),6.5:(0.21,0.61),
 7.0:(0.21,0.61),7.5:(0.23,0.64),8.0:(0.28,0.63),8.5:(0.2,0.66),9.0:(0.23,0.63),9.5:(0.23,0.64),10.0:(0.24,0.66)}
m={k:(xs[k][0],top[k],xs[k][1],round(1-top[k],2)) for k in t}
tr={k:(0,0,1,top[k]) for k in t}
save({"mediaId":4661,"level":"B","keyWord":"fall","defaultVoice":"male",
 "taps":[{"phrase":"to catch drifting leaves","target":"the man","voice":"male","keys":K(t,m)},
         {"phrase":"to rub his head","target":"the man","voice":"male","keys":K(t,m)},
         {"phrase":"to shed its yellow leaves","target":"the yellow tree","voice":"male","keys":K(t,tr)}],
 "stillS":6.0,
 "nouns":[{"word":"a trunk","x":0.47,"y":0.35,"voice":"male"},{"word":"a beard","x":0.52,"y":0.50,"voice":"male"},
          {"word":"a jacket","x":0.50,"y":0.74,"voice":"male"},{"word":"leaves","x":0.22,"y":0.88,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","catching","drifting","leaves","under","a","tree."],"answerVoice":"male",
 "notes":"Key word 'fall' (autumn) is not a visible noun, so it is not among the nouns. The big yellow tree stands behind the man: its box is everything above his head (split along the top of his head); the red tree on the right falls inside that box but is no target. An apple hits his head at 7.0 s and he rubs his head at 7.5-8.0 s (the description does not mention the apple). 'leaves' pill is on the leaf-covered ground; the canopy is also leaves, the trunk pill is set on the thick lower trunk to stay apart. 'a beard' and 'a jacket' are both on the man but at clearly different places."})

# ---------- 4662
t=T(19)
p={0.0:(0.38,0.08,0.48,0.20),0.5:(0.25,0.10,0.63,0.27),1.0:(0,0,0.88,0.25),4.0:(0.36,0.25,0.54,0.19),
   4.5:(0.07,0,0.81,0.38),8.5:(0.24,0.09,0.60,0.25),9.0:(0.37,0.22,0.47,0.18)}
w={0.0:(0.545,0.46,0.36,0.54),0.5:(0.55,0.84,0.32,0.16),2.0:(0.63,0.54,0.37,0.46),2.5:(0.63,0.33,0.37,0.38),
   3.0:(0.49,0.37,0.45,0.52),3.5:(0.45,0.39,0.47,0.57),4.0:(0.48,0.80,0.32,0.20),5.5:(0.60,0.86,0.30,0.14),
   6.0:(0.48,0.71,0.42,0.29),8.5:(0.35,0.47,0.58,0.53),9.0:(0.30,0.46,0.70,0.54)}
h={0.0:(0.29,0.41,0.25,0.14),0.5:(0.30,0.70,0.25,0.14),1.0:(0.30,0.86,0.27,0.14),1.5:(0.34,0.84,0.27,0.14),
   2.5:(0.42,0.22,0.21,0.14),3.0:(0.43,0.23,0.20,0.14),3.5:(0.43,0.25,0.20,0.14),4.0:(0.31,0.66,0.24,0.14),
   4.5:(0.31,0.84,0.26,0.14),5.0:(0.33,0.86,0.27,0.14),5.5:(0.36,0.75,0.24,0.14),6.0:(0.38,0.57,0.23,0.14)}
save({"mediaId":4662,"level":"B","keyWord":"to supply","defaultVoice":"female",
 "taps":[{"phrase":"to drop wooden crates","target":"the plane","voice":"female","keys":K(t,p)},
         {"phrase":"to gaze at the sky","target":"the woman in the striped robe","voice":"female","keys":K(t,w)},
         {"phrase":"to graze near the tents","target":"the horses","voice":"female","keys":K(t,h)}],
 "stillS":2.0,
 "nouns":[{"word":"straps","x":0.61,"y":0.29,"voice":"female"},{"word":"a crate","x":0.50,"y":0.43,"voice":"female"},
          {"word":"tents","x":0.17,"y":0.53,"voice":"female"},{"word":"a robe","x":0.80,"y":0.74,"voice":"female"}],
 "question":"What is the plane doing?",
 "answer":["It","is","dropping","wooden","crates","on","parachutes."],"answerVoice":"female",
 "notes":"Clip with cuts. Horses are small and far (box at minimum size); at 0.0 s they stand right beside the woman's head, so the woman's box there starts at x 0.545 and leaves out her left arm. From 6.5 s the horses are only dots on the horizon or hidden: off. The villagers (6.5-8.0 s) are other people, not the woman in the striped robe: she is off there. Key word 'supply' is a verb, used neither as noun nor in the answer ('village' is not clearly shown)."})

# ---------- 4664
t=T(19)
sp={0.0:0.53,0.5:0.55,1.0:0.60,1.5:0.63,2.0:0.62,2.5:0.62,3.0:0.62,3.5:0.63,4.0:0.63,4.5:0.58,5.0:0.56,5.5:0.56}
bx={0.0:(0.34,0.30),0.5:(0.34,0.30),1.0:(0.27,0.29),1.5:(0.15,0.28),2.0:(0.04,0.28),2.5:(0.01,0.28),3.0:(0,0.26),
    3.5:(0,0.26),4.0:(0,0.28),4.5:(0,0.29),5.0:(0.01,0.29),5.5:(0.03,0.29)}
bb={0.0:0.86,0.5:0.87,1.0:0.97,1.5:0.96,2.0:0.94,2.5:0.94,3.0:0.94,3.5:0.93,4.0:0.94,4.5:0.94,5.0:0.98,5.5:0.96}
w={k:(0,0,1,sp[k]) for k in sp}
b={k:(bx[k][0],sp[k],bx[k][1],round(bb[k]-sp[k],2)) for k in sp}
w[6.0]=(0.24,0,0.76,0.82); b[6.0]=(0,0.60,0.24,0.38)
w[6.5]=(0,0,1,0.81); b[6.5]=(0.02,0.81,0.22,0.19)
for k in (7.0,7.5,8.0,8.5,9.0): w[k]=(0,0,1,1)
save({"mediaId":4664,"level":"B","keyWord":"a dose","defaultVoice":"female",
 "taps":[{"phrase":"to measure out a dose","target":"the woman","voice":"female","keys":K(t,w)},
         {"phrase":"to sip from a glass","target":"the woman","voice":"female","keys":K(t,w)},
         {"phrase":"to have a white label","target":"the brown bottle","voice":"female","keys":K(t,b)}],
 "stillS":2.0,
 "nouns":[{"word":"a pipette","x":0.57,"y":0.25,"voice":"female"},{"word":"a jumper","x":0.78,"y":0.42,"voice":"female"},
          {"word":"a glass","x":0.60,"y":0.66,"voice":"female"},{"word":"a bottle","x":0.18,"y":0.80,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","measuring","out","a","dose","of","oil."],"answerVoice":"female",
 "notes":"Only one person; the second target is the brown bottle with a state phrase (no action fits a thing here). The bottle stands in front of the woman's jumper, so her box is cut at the top of the bottle (split line) and the lower part of her jumper/sleeve is left out; at 6.0 s the split is vertical. Bottle off from 7.0 s (out of frame). 'a dose' is not a visible noun, it is used in a phrase and in the answer. 'oil' is read from the golden beads that do not mix with the water."})
