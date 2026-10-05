from gen_5664_5665_5667_5668_lib import write
W=[(0.17,0.24,0.39,0.47),(0.17,0.22,0.39,0.49),(0.15,0.22,0.42,0.52),(0.08,0.20,0.52,0.55),(0.07,0.21,0.50,0.58),(0,0.19,0.58,0.60),(0,0.18,0.62,0.64),(0,0.17,0.63,0.65)]
G=[(0.56,0.29,0.43,0.29),(0.56,0.29,0.43,0.29),(0.57,0.30,0.42,0.29),(0.60,0.30,0.39,0.28),(0.58,0.30,0.41,0.28),(0.59,0.30,0.41,0.28),(0.62,0.31,0.38,0.28),(0.63,0.31,0.37,0.28)]
write(5665,"B","bold","female",[
 ("to cross a rope bridge","the woman","female",W),
 ("to hold a steel cable","the woman","female",W),
 ("to watch from the ledge","the group on the ledge","female",G)],
 0.2,[("a harness",0.39,0.42,"female"),("mist",0.10,0.55,"female"),("a cliff",0.80,0.66,"female"),("a rope bridge",0.20,0.80,"female")],
 "What is the climber doing?","She is crossing a narrow rope bridge.","female",
 "Woman walks toward the camera (packet says toward the rock). Group target = all people on the ledge incl. the standing man with the red rope; woman's right hand near him is cut at the split line. Key word 'bold' (adjective) not used as a noun.")
