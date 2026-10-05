import json
OFF=None
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(c): json.dump(c, open(f"content/{c['mediaId']}.json","w"), indent=1, ensure_ascii=False)

# ---------- 4461
t=T(13)
man={0.0:(0.08,0.40,0.92,0.60),1.5:(0.13,0.14,0.62,0.30),2.0:(0.10,0.18,0.85,0.80),2.5:(0.20,0.25,0.52,0.37),
     3.0:(0.34,0.27,0.53,0.37),3.5:(0.26,0.27,0.53,0.37),4.0:(0.28,0.26,0.50,0.38),4.5:(0.26,0.29,0.53,0.39),
     5.0:(0.29,0.28,0.50,0.39),5.5:(0.28,0.30,0.51,0.37),6.0:(0.27,0.29,0.50,0.39)}
hand={1.0:(0.0,0.0,0.78,0.36),1.5:(0.05,0.45,0.95,0.45),5.0:(0.0,0.27,0.29,0.24),5.5:(0.0,0.58,0.27,0.15),6.0:(0.0,0.58,0.26,0.16)}
save({"mediaId":4461,"level":"B","keyWord":"dig","defaultVoice":"male",
 "taps":[{"phrase":"to lie buried in sand","target":"the buried man","voice":"male","keys":keys(t,man)},
         {"phrase":"to burst out laughing","target":"the buried man","voice":"male","keys":keys(t,man)},
         {"phrase":"to pat down the sand","target":"the hand","voice":"male","keys":keys(t,hand)}],
 "stillS":4.5,
 "nouns":[{"word":"the sky","x":0.50,"y":0.12,"voice":"male"},{"word":"sunglasses","x":0.52,"y":0.485,"voice":"male"},
          {"word":"waves","x":0.14,"y":0.565,"voice":"male"},{"word":"sand","x":0.50,"y":0.85,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","lying","buried","in","the","sand."],"answerVoice":"male",
 "notes":"Only two targets: the clip is the buried man plus loose hands. The buried man is boxed at 0.0 (not yet buried, lying between two friends) and as feet+mound at 1.5/2.0. At 0.0 the two friends also grin (0.5 s) - 'to burst out laughing' is meant for the open-mouthed laugh at 4.0-5.0. 'the hand': at 1.5 only the big foreground hand is boxed; two smaller patting hands lie near the feet inside the man's box. Hand at 1.0 holds/throws sand rather than pats. Friends' hands at 0.0 not boxed. Key word 'dig' is not used: nobody is clearly seen digging."})

# ---------- 4462
t=T(25)
wom={0.0:(0.36,0.23,0.25,0.24),0.5:(0.36,0.22,0.25,0.25),1.0:(0.37,0.23,0.24,0.25),1.5:(0.37,0.22,0.24,0.26),2.0:(0.36,0.22,0.25,0.27),
     2.5:(0.15,0.13,0.57,0.63),3.0:(0.13,0.22,0.58,0.55),3.5:(0.12,0.25,0.60,0.52),4.0:(0.12,0.21,0.56,0.55),4.5:(0.19,0.14,0.52,0.62),
     5.0:(0.11,0.16,0.58,0.59),6.0:(0.0,0.12,0.11,0.73),6.5:(0.0,0.12,0.13,0.73),7.0:(0.0,0.12,0.13,0.73),7.5:(0.0,0.19,0.12,0.42),
     8.0:(0.40,0.23,0.19,0.30),8.5:(0.39,0.24,0.21,0.30),9.0:(0.38,0.24,0.23,0.30),9.5:(0.38,0.28,0.16,0.26),10.0:(0.37,0.28,0.16,0.26),
     10.5:(0.38,0.28,0.16,0.26),11.0:(0.36,0.29,0.17,0.25),11.5:(0.38,0.29,0.16,0.25),12.0:(0.36,0.28,0.17,0.26)}
old={3.0:(0.30,0.11,0.30,0.11),3.5:(0.36,0.12,0.30,0.13),4.0:(0.26,0.09,0.28,0.12),
     5.5:(0.10,0.09,0.63,0.71),6.0:(0.11,0.09,0.63,0.69),6.5:(0.13,0.10,0.61,0.68),7.0:(0.13,0.10,0.62,0.68),7.5:(0.12,0.12,0.61,0.66),
     9.5:(0.54,0.28,0.12,0.26),10.0:(0.53,0.28,0.11,0.26),10.5:(0.54,0.28,0.11,0.26),11.0:(0.53,0.29,0.11,0.25),11.5:(0.54,0.29,0.11,0.25),12.0:(0.53,0.28,0.11,0.26)}
cof={0.0:(0.18,0.47,0.64,0.50),0.5:(0.19,0.47,0.64,0.51),1.0:(0.21,0.48,0.64,0.50),1.5:(0.21,0.48,0.64,0.51),2.0:(0.20,0.49,0.64,0.50),
     2.5:(0.02,0.76,0.95,0.24),3.0:(0.01,0.77,0.97,0.23),3.5:(0.0,0.77,0.97,0.23),4.0:(0.0,0.76,0.95,0.24),4.5:(0.0,0.76,0.95,0.24),
     5.0:(0.0,0.75,0.95,0.25),5.5:(0.02,0.80,0.93,0.20),6.0:(0.13,0.78,0.82,0.22),6.5:(0.13,0.78,0.82,0.22),7.0:(0.13,0.78,0.82,0.22),
     7.5:(0.12,0.78,0.83,0.22),8.0:(0.24,0.53,0.60,0.45),8.5:(0.25,0.54,0.58,0.44),9.0:(0.23,0.54,0.60,0.46),9.5:(0.28,0.54,0.54,0.46),
     10.0:(0.28,0.54,0.52,0.43),10.5:(0.28,0.54,0.52,0.43),11.0:(0.28,0.54,0.52,0.43),11.5:(0.28,0.54,0.52,0.43),12.0:(0.28,0.54,0.52,0.43)}
save({"mediaId":4462,"level":"B","keyWord":"funeral","defaultVoice":"female",
 "taps":[{"phrase":"to lay a white rose","target":"the woman in the headscarf","voice":"female","keys":keys(t,wom)},
         {"phrase":"to scatter earth by hand","target":"the elderly man","voice":"male","keys":keys(t,old)},
         {"phrase":"to be covered with earth","target":"the coffin","voice":"female","keys":keys(t,cof)}],
 "stillS":10.5,
 "nouns":[{"word":"bare branches","x":0.60,"y":0.10,"voice":"female"},{"word":"mourners","x":0.50,"y":0.40,"voice":"female"},
          {"word":"a rose","x":0.50,"y":0.58,"voice":"female"},{"word":"a coffin","x":0.52,"y":0.87,"voice":"female"}],
 "question":"What are the mourners attending?","answer":["They","are","attending","a","funeral."],"answerVoice":"female",
 "notes":"The elderly man is 'off' in the wide shots 0.0-2.0 and 8.0-9.0 and at 2.5, 4.5, 5.0: only his bald head shows behind the woman, no room for a box that does not overlap hers. At 3.0-4.0 his box is only the head above the woman's box; at 9.5-12.0 a narrow strip between the woman and the tall man. At 7.0/7.5 a second hand (wrist watch, owner out of frame) also drops earth. The woman is 'off' at 5.5 (hidden behind the dark-haired man). The rose pill sits on the earth mound on the coffin lid. Mixed group, evenId true -> defaultVoice female."})

# ---------- 4464
t=T(19)
w={0.0:(0.28,0.50,0.60,0.50),0.5:(0.28,0.50,0.60,0.50),1.0:(0.28,0.51,0.60,0.49),1.5:(0.24,0.51,0.62,0.49),2.0:(0.15,0.52,0.62,0.48),
   2.5:(0.09,0.52,0.62,0.48),3.0:(0.09,0.53,0.62,0.47),3.5:(0.12,0.52,0.62,0.48),4.0:(0.17,0.52,0.61,0.48),
   4.5:(0.36,0.45,0.34,0.47),5.0:(0.37,0.53,0.33,0.40),5.5:(0.38,0.52,0.30,0.41),6.0:(0.43,0.51,0.28,0.42),
   6.5:(0.43,0.50,0.20,0.50),7.0:(0.38,0.51,0.21,0.49),7.5:(0.30,0.52,0.23,0.48),8.0:(0.24,0.51,0.22,0.49),8.5:(0.20,0.52,0.19,0.48),9.0:(0.12,0.52,0.17,0.45)}
m={4.5:(0.83,0.44,0.15,0.38),5.0:(0.76,0.47,0.22,0.32),5.5:(0.74,0.53,0.22,0.28),6.0:(0.72,0.52,0.17,0.28),
   6.5:(0.18,0.49,0.25,0.51),7.0:(0.08,0.49,0.30,0.51),7.5:(0.05,0.50,0.25,0.50),8.0:(0.0,0.50,0.24,0.50),8.5:(0.0,0.50,0.20,0.50),9.0:(0.0,0.49,0.12,0.51)}
b={6.5:(0.65,0.36,0.35,0.44),7.0:(0.61,0.38,0.39,0.42),7.5:(0.55,0.40,0.45,0.40),8.0:(0.49,0.38,0.51,0.42),8.5:(0.42,0.37,0.58,0.43),9.0:(0.31,0.38,0.69,0.45)}
save({"mediaId":4464,"level":"A","keyWord":"read","defaultVoice":"female",
 "taps":[{"phrase":"to read a book","target":"the woman with the book","voice":"female","keys":keys(t,w)},
         {"phrase":"to wear a green cap","target":"the man in the cap","voice":"male","keys":keys(t,m)},
         {"phrase":"to stop for the people","target":"the big bus","voice":"female","keys":keys(t,b)}],
 "stillS":1.0,
 "nouns":[{"word":"the sky","x":0.65,"y":0.33,"voice":"female"},{"word":"a road","x":0.80,"y":0.64,"voice":"female"},
          {"word":"a book","x":0.70,"y":0.78,"voice":"female"},{"word":"grass","x":0.17,"y":0.88,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","reading","a","book","by","the","road."],"answerVoice":"female",
 "notes":"Three shots. 'the big bus' is the blue city bus of the last shot (6.5-9.0); the tiny bus far down the road in shot 1 is not boxed (named 'big' to exclude it). The bus box is the part to the right of the woman, with other passengers standing in front of it. 'to wear a green cap' is a state: the man in the cap does nothing only he does. In the queue the woman is the one in the beige cardigan next to the man in the cap; at 8.5/9.0 she is seen from behind. Man in the cap at 9.0 is cut by the left edge (narrow box)."})

# ---------- 4465
t=T(19)
man={0.0:(0.56,0.27,0.44,0.73),0.5:(0.53,0.27,0.47,0.73),1.0:(0.32,0.41,0.66,0.59),1.5:(0.27,0.44,0.68,0.56),2.0:(0.0,0.42,0.43,0.58),
     2.5:(0.22,0.43,0.41,0.56),3.0:(0.14,0.35,0.68,0.65),3.5:(0.40,0.39,0.60,0.61),4.0:(0.42,0.47,0.58,0.53),
     6.0:(0.27,0.30,0.56,0.68),6.5:(0.27,0.32,0.56,0.68),7.0:(0.10,0.32,0.90,0.68),7.5:(0.18,0.28,0.82,0.72),8.0:(0.15,0.32,0.85,0.68),
     8.5:(0.15,0.33,0.80,0.67),9.0:(0.16,0.35,0.74,0.65)}
drv={3.5:(0.02,0.47,0.36,0.36),4.0:(0.0,0.64,0.24,0.28),5.5:(0.52,0.47,0.22,0.18)}
save({"mediaId":4465,"level":"A","keyWord":"upstairs","defaultVoice":"male",
 "taps":[{"phrase":"to go upstairs","target":"the man in the cap","voice":"male","keys":keys(t,man)},
         {"phrase":"to open his arms wide","target":"the man in the cap","voice":"male","keys":keys(t,man)},
         {"phrase":"to drive the bus","target":"the bus driver","voice":"male","keys":keys(t,drv)}],
 "stillS":8.5,
 "nouns":[{"word":"buildings","x":0.50,"y":0.15,"voice":"male"},{"word":"a cap","x":0.55,"y":0.43,"voice":"male"},
          {"word":"a bag","x":0.45,"y":0.63,"voice":"male"},{"word":"shorts","x":0.52,"y":0.79,"voice":"male"}],
 "question":"Where is the man going?","answer":["He","is","going","upstairs","on","the","bus."],"answerVoice":"male",
 "notes":"Two targets only: the man in the cap fills the clip. 'the bus driver' is short: 3.5 (blue shirt at the wheel), 4.0 (only his arm on the wheel, bottom left) and 5.5 (small figure behind the windscreen of the red bus). The van driver in the red shirt (0.5-1.5) is not boxed - he drives a van, not a bus. At 1.0-1.5 the man steps into the grey van, not into a bus. The red bus itself was not used as a target because from 6.0 on it fills the whole frame around the man."})
