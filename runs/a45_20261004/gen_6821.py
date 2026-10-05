from gen_6821_6823_6825_6826_lib import write
woman = [(0.02,0.41,0.45,0.59),(0.02,0.40,0.44,0.60),(0.0,0.37,0.40,0.63),(0.0,0.36,0.39,0.64),(0.0,0.34,0.38,0.66),(0.0,0.30,0.40,0.70),(0.0,0.28,0.44,0.72)]
tray  = [(0.47,0.25,0.32,0.40),(0.46,0.24,0.33,0.42),(0.41,0.18,0.42,0.52),(0.40,0.16,0.47,0.54),(0.39,0.13,0.55,0.57),(0.42,0.10,0.58,0.58),(0.50,0.08,0.50,0.62)]
pour  = [(0.80,0.22,0.20,0.42),(0.80,0.21,0.20,0.42),(0.84,0.24,0.16,0.42),(0.88,0.26,0.12,0.40),None,None,None]
write(6821,"B","afford","female",[
 ("to peek into her wallet","the woman","female",woman),
 ("to carry a seafood platter","the waiter with the platter","male",tray),
 ("to pour the champagne","the waiter with the bottle","male",pour)],
 0.7,[("a chandelier",0.68,0.08,"female"),("a lobster",0.58,0.34,"female"),("a menu",0.78,0.66,"female"),("a wallet",0.41,0.80,"female")],
 "What is the waiter bringing?","He is bringing a huge seafood platter.","male",
 "Camera pushes in, so boxes shift. The waiter with the bottle is only partly visible at the right edge from 1.2 s and gone from 2.2 s (only the bottle tip). The seafood stand is a three-tier tower; 'platter' used as the B-level noun. Key word 'afford' is a verb, not placed. Question names the waiter; the other waiter pours, not brings.")
