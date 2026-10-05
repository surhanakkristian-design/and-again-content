import sys; sys.path.insert(0,'.')
from gen_7090_7091_7092_7093_lib import write
L=[(0.52,0.24,0.40,0.67),(0.52,0.24,0.42,0.64),(0.55,0.24,0.40,0.59),(0.52,0.25,0.39,0.57),
   (0.50,0.26,0.40,0.52),(0.48,0.29,0.32,0.45),(0.49,0.30,0.30,0.42),(0.47,0.35,0.30,0.33)]
S=[(0.23,0.33,0.28,0.46),(0.16,0.33,0.31,0.46),(0.12,0.33,0.30,0.47),(0.14,0.33,0.31,0.46),
   (0.17,0.34,0.30,0.44),(0.14,0.34,0.27,0.43),(0.11,0.35,0.28,0.42),(0.12,0.35,0.28,0.42)]
M=[None,None,None,None,None,(0.80,0.29,0.20,0.20),(0.79,0.30,0.21,0.26),(0.80,0.33,0.20,0.21)]
write(7091,"B","exploit","female",
 [("to lead the race","the cyclist in front","female",L),
  ("to trail behind the leader","the second cyclist","female",S),
  ("to stretch out his arm","the man in the crowd","male",M)],
 2.2,
 [("poplar trees",0.27,0.20,"female"),("a helmet",0.71,0.32,"female"),("spectators",0.10,0.45,"female"),("hay bales",0.50,0.85,"female")],
 "What is the cyclist in front doing?","She is leading the race.","female",
 "man in the crowd only on screen from 2.7 s; his hand overlaps the leader's helmet at 2.7, boxes split at x .80; at 3.7 the box is on the man in sunglasses by the barrier (assumed same man, arm lowered)")
