from gen_6957_6958_6959_6960_lib import write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman=[(0.26,0.07,0.38,0.74),(0.25,0.08,0.44,0.73),(0.24,0.08,0.46,0.75),(0.20,0.16,0.38,0.82),(0.16,0.26,0.43,0.62),(0.12,0.25,0.47,0.65),(0.13,0.26,0.46,0.66),(0.13,0.28,0.48,0.64)]
friend=[(0.04,0.48,0.21,0.17),(0.02,0.49,0.22,0.16),(0.0,0.49,0.23,0.18),(0.0,0.50,0.19,0.17),(0.0,0.50,0.15,0.18),(0.0,0.49,0.11,0.17),(0.0,0.49,0.12,0.18),(0.0,0.49,0.12,0.18)]
write(6960,"B","collector","female",[
 ("to reach for a teapot","the woman with the bob","female",woman),
 ("to spread her arms proudly","the woman with the bob","female",woman),
 ("to giggle behind her hand","the friend on the left","female",friend)],
 2.7,[("a standing mirror",0.30,0.08,"female"),("teapots",0.82,0.52,"female"),("bubble wrap",0.10,0.89,"female"),("a cardboard box",0.50,0.90,"female")],
 "What does the standing woman collect?","She collects old porcelain teapots.","female",
 "friend on the left sits right next to the main woman: her box is narrow (0.11-0.15 wide) from 2.2 s to avoid overlap; the second friend lying on the sofa is mostly hidden by the woman's hand, not used; question in present simple (habit, fits key word collector)",T)
