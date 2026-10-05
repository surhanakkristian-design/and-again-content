from gen_7855_7856_7857_7859_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
M=[(0.12,0.31,0.24,0.58),(0.11,0.30,0.25,0.60),(0.11,0.30,0.25,0.64),(0.11,0.30,0.27,0.65),(0.10,0.28,0.29,0.70),(0.09,0.28,0.30,0.71),(0.09,0.28,0.30,0.72),(0.08,0.28,0.33,0.72)]
G=[(0.36,0.25,0.24,0.23),(0.36,0.24,0.24,0.24),(0.36,0.23,0.24,0.25),(0.38,0.23,0.23,0.25),(0.39,0.22,0.23,0.25),(0.39,0.20,0.24,0.27),(0.39,0.25,0.27,0.25),(0.41,0.26,0.25,0.24)]
D=[(0.50,0.49,0.38,0.40),(0.48,0.49,0.42,0.44),(0.48,0.49,0.44,0.49),(0.50,0.50,0.42,0.50),(0.48,0.50,0.47,0.50),(0.46,0.51,0.50,0.49),(0.44,0.52,0.52,0.48),(0.46,0.52,0.46,0.48)]
build(7856,"B","guessing","male",[
 ("to stroke the dog's face","the blindfolded man","male",M),
 ("to lick its lips","the white dog","male",D),
 ("to cover her face","the woman in green","female",G)],
 2.7,[("a sleep mask",0.22,0.37,"male"),("a lantern",0.48,0.07,"male"),("a wood stove",0.86,0.40,"male"),("a board game",0.82,0.53,"male")],
 "What is the blindfolded man doing?","He is stroking the dog's face.","male",
 "Man box cut at the green woman's left edge (she sits right behind his shoulder) so it misses his outstretched arms; dog box starts where his hands touch the dog. 'to cover her face' is plain vocabulary for B; she only covers it from 3.2 s (laughs before). The pink woman is not a target (mostly off-frame).",T)
