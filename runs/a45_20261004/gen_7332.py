from gen_7328_7329_7332_7334_lib import write
S=[0.58,0.58,0.60,0.62,0.61,0.60,0.56,0.54]
L=[0.11,0.12,0.16,0.13,0.17,0.17,0.07,0.06]
woman=[(l,0.31,round(s-l,2),0.49) for l,s in zip(L,S)]
bike=[(s,0.12,round(0.93-s,2),0.57) for s in S]
write(7332,"B","manufacture","female",[
 ("to steady the front wheel","the woman","female",woman),
 ("to operate a cordless drill","the woman","female",woman),
 ("to hang from the assembly line","the hanging bicycle","female",bike)],
 3.2,[("bolts",0.14,0.82,"female"),("a drill",0.38,0.69,"female"),("tyres",0.62,0.92,"female"),("a saddle",0.85,0.81,"female")],
 "What is the woman doing?","She is operating a cordless drill.","female",
 "Only two clear targets (background workers do nothing identifiable): woman x2, bicycle x1. Woman's hand touches the wheel at 0.2 s and the drill reaches it 1.2-2.7 s: boxes split at the line between them; bike box starts right of the split, so the left end of the handlebar is outside it. Key word 'manufacture' is a verb, not placed. 'steady the front wheel' is only clear at 0.2 s.")
