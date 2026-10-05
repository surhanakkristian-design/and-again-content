import json
def T(n): return [round(i*0.5,1) for i in range(n)]
def keys(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    assert len(out)==len(times)==len(boxes)
    return out
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 688
t=T(21)
F=(0,0.08,1,0.92); A=(0,0,1,1)
w=keys(t,[F]*6+[(0,0.22,1,0.66)]*2+[(0,0.06,1,0.94)]+[A]*5+[(0,0.12,1,0.88)]*2+[A]*2+[(0,0.25,0.82,0.75),(0,0.24,1,0.76),(0,0.22,0.93,0.78)])
save({"mediaId":688,"level":"A","keyWord":"skin","defaultVoice":"female",
 "taps":[{"phrase":"to put cream on her face","target":"the woman","voice":"female","keys":w},
         {"phrase":"to rub her arm","target":"the woman","voice":"female","keys":w},
         {"phrase":"to touch her cheeks","target":"the woman","voice":"female","keys":w}],
 "stillS":10.0,
 "nouns":[{"word":"skin","x":0.42,"y":0.52,"voice":"female"},{"word":"the sky","x":0.70,"y":0.18,"voice":"female"},
          {"word":"plants","x":0.82,"y":0.78,"voice":"female"},{"word":"a T-shirt","x":0.35,"y":0.86,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","putting","cream","on","her","skin."],"answerVoice":"female",
 "notes":"Only one target (the woman); t=3.0-8.5 are close-ups of her hands and arm, the box covers the visible parts of her. 'skin' slot sits on her cheek at 10.0 s."})

# 689
w=keys(t,[A]*7+[(0.03,0,0.94,1),(0.08,0,0.86,0.97),(0.15,0,0.80,0.90),(0.15,0,0.75,0.92),(0.15,0,0.63,0.96),(0,0,0.95,0.88),(0,0,1,0.88),A,(0,0,0.84,1),(0.2,0,0.75,1),(0.17,0,0.83,0.94),(0.18,0,0.82,1),(0.34,0.08,0.60,0.84),(0.30,0.02,0.50,0.75)])
save({"mediaId":689,"level":"A","keyWord":"skirt","defaultVoice":"female",
 "taps":[{"phrase":"to hold her skirt","target":"the woman","voice":"female","keys":w},
         {"phrase":"to turn around","target":"the woman","voice":"female","keys":w},
         {"phrase":"to wear white shoes","target":"the woman","voice":"female","keys":w}],
 "stillS":8.0,
 "nouns":[{"word":"a skirt","x":0.58,"y":0.58,"voice":"female"},{"word":"a T-shirt","x":0.55,"y":0.20,"voice":"female"},
          {"word":"birds","x":0.84,"y":0.45,"voice":"female"},{"word":"trees","x":0.20,"y":0.08,"voice":"female"}],
 "question":"What is the woman wearing?","answer":["She","is","wearing","a","yellow","skirt."],"answerVoice":"female",
 "notes":"All three phrases on the woman: the man in dark blue is only a cut-off edge figure (also walks down the steps, so that phrase was avoided) and the pigeons do nothing distinct. One pigeon stands apart at the left at 8.0 s; the 'birds' slot is on the group at the right."})

# 691
t=T(25)
S=[(0.50,0.39,0.36,0.35),(0.36,0.37,0.40,0.37),(0.23,0.37,0.44,0.50),(0.19,0.37,0.42,0.50),(0.40,0.39,0.44,0.36),(0.43,0.37,0.41,0.38),
   (0.31,0.35,0.38,0.52),(0.07,0.34,0.42,0.55),(0.05,0.38,0.48,0.38),(0.08,0.36,0.56,0.40),(0.28,0.37,0.61,0.50),(0.40,0.37,0.45,0.50),
   (0.37,0.37,0.32,0.38),(0.45,0.38,0.45,0.36),(0.53,0.39,0.41,0.47),(0.48,0.37,0.34,0.50),(0.43,0.37,0.29,0.37),(0.40,0.34,0.37,0.31),
   (0.25,0.39,0.54,0.32),(0.21,0.56,0.63,0.20),(0.20,0.58,0.74,0.24),(0.33,0.50,0.64,0.33),(0.28,0.47,0.66,0.50),(0,0.08,1,0.92),(0,0.08,1,0.92)]
C=[(0,0.40,0.42,0.31),(0.77,0.40,0.23,0.31),(0.68,0.42,0.32,0.30),(0.62,0.42,0.38,0.30),(0,0.41,0.39,0.31),(0,0.41,0.42,0.31),
   (0.70,0.42,0.30,0.30),(0.50,0.42,0.50,0.30),(0.54,0.42,0.46,0.29),(0.65,0.42,0.35,0.29),(0,0.42,0.27,0.30),(0,0.42,0.39,0.30),
   (0.70,0.42,0.30,0.29),(0,0.42,0.44,0.29),(0,0.42,0.52,0.28),(0,0.42,0.47,0.28),(0,0.42,0.42,0.29),(0,0.42,0.39,0.28),
   (0.80,0.41,0.20,0.28),(0,0.39,1,0.17),(0,0.39,1,0.19),(0,0.40,0.32,0.28),(0,0.40,0.27,0.30),None,None]
s=keys(t,S); c=keys(t,C)
save({"mediaId":691,"level":"B","keyWord":"guard","defaultVoice":"male",
 "taps":[{"phrase":"to guard a grey car","target":"the soldier","voice":"male","keys":s},
         {"phrase":"to swing a wooden stick","target":"the soldier","voice":"male","keys":s},
         {"phrase":"to be parked beside a wall","target":"the car","voice":"male","keys":c}],
 "stillS":4.0,
 "nouns":[{"word":"a soldier","x":0.22,"y":0.52,"voice":"male"},{"word":"barbed wire","x":0.30,"y":0.27,"voice":"male"},
          {"word":"a concrete wall","x":0.70,"y":0.36,"voice":"male"},{"word":"a dirt road","x":0.50,"y":0.82,"voice":"male"}],
 "question":"What is the soldier doing?","answer":["He","is","guarding","the","car","with","a","stick."],"answerVoice":"male",
 "notes":"The soldier stands in front of the car in every frame, so the car box is only the part of the car beside (or, at 9.5-10.0 s, above) him. The man in black is visible only at 0.0-0.5 s and was not used as a target. 11.5-12.0 s: close-up of the laughing soldier (camouflage shirt), car off."})

# 692
t=T(21)
M=[(0.33,0.07,0.67,0.77),(0.50,0.03,0.50,0.80),(0.61,0.04,0.39,0.86),(0.63,0.05,0.37,0.82),(0.42,0.13,0.58,0.48),(0.24,0.37,0.76,0.40),
   (0.33,0.26,0.67,0.68),(0.08,0.41,0.92,0.47),(0,0.36,1,0.44),(0,0.37,1,0.50),(0,0.40,1,0.58),(0,0.41,1,0.57),(0,0.38,1,0.58),
   (0,0.39,1,0.58),(0,0.41,1,0.57),(0,0.42,1,0.56),(0,0.39,1,0.59),(0,0.41,1,0.57),(0,0.43,1,0.55),(0,0.43,1,0.55),(0,0.40,1,0.58)]
W=[(0,0.44,0.22,0.30),(0,0.43,0.33,0.31),(0.09,0.43,0.38,0.38),(0.14,0.43,0.38,0.37),(0.16,0.39,0.25,0.26),None,None,
   (0.28,0.18,0.24,0.22),(0.30,0.15,0.25,0.20),(0.28,0.15,0.34,0.21),(0.30,0.15,0.34,0.24),(0.30,0.15,0.36,0.25),(0.30,0.15,0.32,0.22),
   (0.32,0.15,0.32,0.23),(0.32,0.15,0.30,0.25),(0.30,0.14,0.32,0.27),(0.32,0.13,0.30,0.25),(0.30,0.13,0.32,0.27),(0.32,0.13,0.30,0.29),
   (0.30,0.13,0.32,0.29),(0.32,0.12,0.30,0.27)]
m=keys(t,M); w=keys(t,W)
save({"mediaId":692,"level":"A","keyWord":"sleeping","defaultVoice":"male",
 "taps":[{"phrase":"to stretch his arms","target":"the man","voice":"male","keys":m},
         {"phrase":"to sleep under a blanket","target":"the man","voice":"male","keys":m},
         {"phrase":"to read a book","target":"the woman","voice":"female","keys":w}],
 "stillS":8.5,
 "nouns":[{"word":"a cat","x":0.86,"y":0.28,"voice":"male"},{"word":"a lamp","x":0.36,"y":0.17,"voice":"male"},
          {"word":"a blanket","x":0.70,"y":0.62,"voice":"male"},{"word":"a pillow","x":0.17,"y":0.78,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","sleeping","under","a","blanket."],"answerVoice":"male",
 "notes":"The cat only sits and looks, no action that fits only it, so it is a noun, not a tap target. The woman is hidden behind the man at 2.5-3.0 s (off). From about 7.5 s her book is hard to see in the dark background."})
