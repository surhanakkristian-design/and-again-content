from gen_7502_7529_7738_7740_lib import write
wo={0.2:(0.44,0.40,0.19,0.20),0.7:(0.45,0.40,0.19,0.20),1.2:(0.46,0.40,0.19,0.19),1.7:(0.47,0.39,0.19,0.19),
    2.2:(0.47,0.39,0.19,0.20),2.7:(0.47,0.39,0.19,0.20),3.2:(0.46,0.38,0.19,0.21),3.7:(0.46,0.38,0.20,0.21)}
man={0.2:(0.08,0.57,0.21,0.35),0.7:(0.07,0.57,0.22,0.36),1.2:(0.03,0.58,0.23,0.40),1.7:(0.01,0.58,0.23,0.42),
     2.2:(0.0,0.59,0.20,0.41),2.7:(0.0,0.60,0.18,0.40),3.2:(0.0,0.64,0.18,0.36)}
hawk={0.2:(0.72,0.65,0.21,0.19),0.7:(0.73,0.65,0.21,0.20),1.2:(0.73,0.66,0.23,0.21),1.7:(0.72,0.69,0.28,0.20),
      2.2:(0.38,0.64,0.60,0.15),2.7:(0.34,0.60,0.43,0.20),3.2:(0.27,0.67,0.33,0.14),3.7:(0.11,0.67,0.46,0.14)}
write(7740,"B","agricultural","female",[
 ("to plough the field","the woman","female",wo),
 ("to examine the soil","the man","male",man),
 ("to spread its wings","the hawk","female",hawk)],
 0.2,[("trees",0.70,0.18,"female"),("a tractor",0.70,0.52,"female"),("a plough",0.38,0.58,"female"),("a hawk",0.82,0.74,"female")],
 "What is the man doing?","He is examining a handful of soil.","male",
 "Woman target = the woman in the tractor cab (she drives the tractor that pulls the plough); the tractor itself is not a target so her box does not clash with a tractor box. The man examines the soil in his hands at 0.2-1.2, then walks; at 3.2 only his edge is visible (box at the left edge), off at 3.7. Hawk sits on the post 0.2-1.2, wings spread from 1.7, flies across the field 2.2-3.7. Key word 'agricultural' is an adjective, not used as a noun.")
