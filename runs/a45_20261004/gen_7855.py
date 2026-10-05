from gen_7855_7856_7857_7859_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
W=[(0.54,0.0,0.20,0.50),(0.53,0.10,0.20,0.47),(0.53,0.19,0.18,0.44),(0.53,0.24,0.18,0.46),(0.53,0.25,0.18,0.46),(0.53,0.25,0.18,0.46),(0.53,0.25,0.18,0.46),(0.53,0.25,0.18,0.46)]
P=[(0.12,0.12,0.42,0.26),(0.12,0.21,0.41,0.25),(0.14,0.29,0.39,0.24),(0.14,0.34,0.39,0.23),(0.14,0.35,0.39,0.23),(0.14,0.35,0.39,0.23),(0.14,0.35,0.39,0.23),(0.14,0.35,0.39,0.23)]
build(7855,"B","growth","female",[
 ("to measure a giant pumpkin","the woman on the ladder","female",W),
 ("to balance on a stepladder","the woman on the ladder","female",W),
 ("to hang against a broken window","the pumpkin","female",P)],
 3.7,[("a pumpkin",0.34,0.46,"female"),("a stepladder",0.60,0.74,"female"),("a watering can",0.80,0.86,"female"),("vines",0.22,0.88,"female")],
 "What is the woman inside doing?","She is measuring a giant pumpkin.","female",
 "Camera pushes in during first 1.5 s. Pumpkin box and woman box split at x=0.53 (her arm reaches over the pumpkin). Key word growth is not a visible noun.",T)
