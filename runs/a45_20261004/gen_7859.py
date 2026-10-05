from gen_7855_7856_7857_7859_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
M=[(0.04,0.31,0.21,0.20),(0.06,0.33,0.20,0.22),(0.08,0.35,0.21,0.22),(0.10,0.36,0.22,0.22),(0.10,0.38,0.22,0.20),(0.10,0.38,0.22,0.21),(0.10,0.39,0.22,0.21),(0.10,0.39,0.22,0.21)]
B=[(0.02,0.51,0.49,0.49),(0.02,0.55,0.49,0.45),(0.02,0.57,0.49,0.43),(0.02,0.58,0.49,0.42),(0.02,0.58,0.48,0.42),(0.02,0.59,0.48,0.41),(0.02,0.60,0.50,0.40),(0.02,0.60,0.50,0.40)]
Y=[(0.51,0.40,0.49,0.60),(0.51,0.43,0.49,0.57),(0.51,0.45,0.49,0.55),(0.52,0.46,0.48,0.54),(0.50,0.45,0.50,0.55),(0.50,0.45,0.50,0.55),(0.52,0.47,0.48,0.53),(0.52,0.47,0.48,0.53)]
build(7859,"A","happily","female",[
 ("to take a selfie","the woman in yellow","female",Y),
 ("to wear a blue top","the woman in blue","female",B),
 ("to sit on a friend's shoulders","the man with his fist up","male",M)],
 2.2,[("the sky",0.25,0.10,"female"),("confetti",0.62,0.24,"female"),("a stage",0.82,0.40,"female"),("a blue top",0.30,0.72,"female")],
 "What are the two women doing?","They are laughing at a festival.","female",
 "Woman in blue box starts below the man's box (he is right above her head), so it covers her lower face and body only. 'to wear a blue top' is a state: both women laugh, so no action is unique to her. Key word happily is not used in the answer to keep one word order.",T)
