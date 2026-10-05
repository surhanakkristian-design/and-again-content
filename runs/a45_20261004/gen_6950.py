from gen_6950_6951_6953_6954_lib import write
W=[(0.38,0.38,0.25,0.32),(0.46,0.38,0.20,0.34),(0.51,0.34,0.34,0.45),(0.64,0.32,0.36,0.53),(0.60,0.30,0.40,0.58),(0.38,0.28,0.43,0.64)]
C=[(0.15,0.56,0.19,0.14),(0.15,0.56,0.19,0.14),(0.14,0.56,0.19,0.14),(0.12,0.57,0.19,0.14),(0.12,0.57,0.19,0.14),(0.10,0.57,0.19,0.14)]
write(6950,"B","chuck","female",[
 ("to chuck her jacket aside","the woman","female",W),
 ("to curl up on the sofa","the cat","female",C),
 ("to push up her sunglasses","the woman","female",W)],
 2.2,[("a lampshade",0.27,0.46,"female"),("a cat",0.21,0.645,"female"),("a trainer",0.13,0.81,"female"),("a water bottle",0.855,0.52,"female")],
 "What is the woman doing?","She is chucking her jacket aside.","female",
 "Jacket is thrown at 0.2-0.7 s only; cat is curled on the sofa all clip.")
