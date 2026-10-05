from gen_7855_7856_7857_7859_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
M=[(0.16,0.34,0.47,0.56),(0.16,0.34,0.48,0.57),(0.14,0.34,0.48,0.58),(0.14,0.34,0.50,0.58),(0.12,0.32,0.52,0.64),(0.12,0.32,0.53,0.64),(0.10,0.32,0.56,0.66),(0.10,0.32,0.56,0.66)]
B=[(0.63,0.19,0.37,0.40),(0.64,0.18,0.36,0.44),(0.63,0.18,0.37,0.42),(0.64,0.17,0.36,0.43),(0.65,0.15,0.35,0.43),(0.66,0.14,0.34,0.46),(0.67,0.14,0.33,0.46),(0.67,0.14,0.33,0.46)]
build(7857,"B","half","male",[
 ("to take a mirror selfie","the man in the cape","male",M),
 ("to mix shaving foam","the barber","female",B),
 ("to hold a straight razor","the barber","female",B)],
 2.2,[("posters",0.20,0.28,"male"),("a light bulb",0.57,0.10,"male"),("a beard",0.47,0.50,"male"),("a barber's chair",0.13,0.61,"male")],
 "What is the man doing?","He is taking a mirror selfie.","male",
 "Man box stops at x~0.64 so it does not overlap the barber box (her lower body is behind his cape on the right). Barber mixes foam only around 0.2-1.2 s; razor visible from 0.7 s.",T)
