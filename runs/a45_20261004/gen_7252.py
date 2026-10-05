from gen_7249_7250_7251_7252_lib import build
T = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman = [(0.33,0.18,0.39,0.68),(0.33,0.16,0.41,0.72),(0.3,0.16,0.44,0.84),(0.3,0.12,0.48,0.88),
         (0.26,0.09,0.46,0.91),(0.27,0.06,0.53,0.94),(0.2,0.04,0.53,0.96),(0.23,0.02,0.57,0.98)]
man = [None,None,None,None,(0.73,0.15,0.27,0.55),(0.81,0.12,0.19,0.6),(0.74,0.1,0.26,0.7),(0.81,0.08,0.19,0.72)]
build(7252,"B","investigator","female",
 [("to hold up an ice core","the woman","female",woman),
  ("to squint into the sun","the woman","female",woman),
  ("to point at the ice","the man in the dark hat","male",man)],
 0.2,
 [("an ice core",0.43,0.28,"female"),("an investigator",0.6,0.45,"female"),("a tent",0.7,0.62,"female"),("a sledge",0.4,0.93,"female")],
 "What is the woman doing?","She is holding up a long ice core.","female",
 "Man in the dark hat: only a gloved arm/hand at the edge at 0.2 and 1.7 -> off until 2.2; he points at the ice at 3.2-3.7 and his pointing glove reaches into the woman's box (split at his shoulder). She squints mainly at 2.2-3.7. 'an investigator' (key word) labels the woman scientist. Men on the left not used.",T)
