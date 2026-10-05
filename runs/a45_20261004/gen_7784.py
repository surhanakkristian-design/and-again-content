from gen_7781_7783_7784_7785_lib import *
wo=[(0.34,0.25,0.80,0.58),(0.34,0.27,0.82,0.58),(0.33,0.29,0.80,0.58),(0.33,0.27,0.82,0.58),(0.29,0.31,0.78,0.58),(0.31,0.32,0.82,0.58),(0.29,0.31,0.79,0.58),(0.30,0.31,0.82,0.58)]
mn=[(0.60,0.58,0.97,0.92),(0.62,0.58,0.98,0.91),(0.60,0.58,0.95,0.93),(0.60,0.58,0.97,0.93),(0.60,0.58,0.96,0.90),(0.62,0.58,0.98,0.91),(0.60,0.58,0.96,0.93),(0.62,0.58,0.98,0.93)]
write(7784,"B","comfortably","female",[
 ("to read a paperback","the woman","female",wo),
 ("to stretch out on the sofa","the woman","female",wo),
 ("to lift the lower end","the man at the bottom","male",mn)],
 2.2,[("a stained-glass window",0.52,0.17,"female"),("a potted palm",0.72,0.32,"female"),("moving boxes",0.82,0.46,"female"),("a sofa",0.30,0.48,"female")],
 "What is the woman doing?","She is reading a paperback on the sofa.","female",
 "The woman's feet touch the bottom man's shoulder: boxes split at y .57 (her feet and his head are cut a little). 'to lift the lower end' = of the sofa (the top man also carries, at the upper end). Top man not targeted. Answer avoids 'comfortably' because the adverb could stand in two places.")
