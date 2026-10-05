from gen_5664_5665_5667_5668_lib import write
W=[(0,0.24,0.34,0.40),(0,0.28,0.34,0.37),(0,0.31,0.35,0.37),(0,0.27,0.35,0.37),(0,0,0.35,0.66),(0,0,0.35,0.64),(0,0.08,0.36,0.62),(0,0.08,0.36,0.62)]
C=[(0.34,0.29,0.18,0.16),(0.34,0.29,0.18,0.17),(0.35,0.31,0.18,0.17),(0.35,0.31,0.18,0.18),(0.35,0.31,0.18,0.18),(0.35,0.32,0.18,0.17),(0.36,0.35,0.15,0.18),(0.36,0.35,0.15,0.18)]
M=[(0.52,0.26,0.20,0.36),(0.52,0.27,0.22,0.33),(0.53,0.28,0.21,0.36),(0.53,0.28,0.23,0.37),(0.53,0.27,0.23,0.37),(0.53,0.27,0.27,0.38),(0.51,0.29,0.33,0.40),(0.51,0.30,0.41,0.38)]
write(5664,"A","board game","female",[
 ("to raise her arms","the woman in purple","female",W),
 ("to move a piece","the man","male",M),
 ("to sit next to the lamp","the cat","female",C)],
 0.2,[("a board game",0.50,0.64,"female"),("a cat",0.43,0.37,"female"),("a lamp",0.53,0.18,"female"),("a plant",0.19,0.76,"female")],
 "What are the three friends doing?","They are playing a board game.","female",
 "Man/cat boxes split at the cat's right edge: man's knees/left hand partly outside his box early; at 3.2-3.7 his reaching hand (x~0.47) is cut so the cat box can stay. Woman's fist at 3.2-3.7 slightly cut at x 0.36.")
