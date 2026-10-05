from gen_7249_7250_7251_7252_lib import build
T = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman = [(0.58,0.13,0.42,0.62),(0.59,0.12,0.41,0.62),(0.58,0.14,0.42,0.62),(0.57,0.15,0.43,0.6),
         (0.55,0.15,0.45,0.6),(0.55,0.15,0.45,0.6),(0.56,0.11,0.44,0.65),(0.56,0.12,0.44,0.65)]
man = [(0.36,0.24,0.21,0.26),(0.36,0.24,0.22,0.26),(0.3,0.25,0.27,0.24),(0.28,0.24,0.28,0.3),
       (0.25,0.23,0.29,0.32),(0.25,0.23,0.29,0.32),(0.24,0.23,0.31,0.3),(0.25,0.23,0.3,0.3)]
build(7250,"B","insulin","female",
 [("to check the dose","the woman","female",woman),
  ("to give herself an injection","the woman","female",woman),
  ("to spoon up his food","the man","male",man)],
 2.7,
 [("a window",0.1,0.3,"female"),("beans",0.27,0.65,"female"),("insulin",0.15,0.77,"female"),("a notebook",0.6,0.74,"female")],
 "What is the woman doing?","She is injecting insulin into her belly.","female",
 "The woman's hands with the pen cross in front of the man (0.2-1.2, 3.2-3.7); the boxes are split at his right shoulder, so her hands/pen sit partly outside her box or inside his. 'insulin' pill sits on the two vials in the cool bag. Injection is at 1.7-2.7.",T)
