from gen_6957_6958_6959_6960_lib import write
T=[0.2,0.7,1.2,1.7,2.2]
woman=[(0.0,0.30,0.47,0.43),(0.0,0.30,0.47,0.43),(0.0,0.32,0.46,0.41),(0.0,0.31,0.48,0.43),(0.0,0.31,0.50,0.45)]
man=[(0.51,0.35,0.49,0.65),(0.51,0.35,0.49,0.65),(0.51,0.36,0.49,0.64),(0.51,0.35,0.49,0.65),(0.52,0.35,0.48,0.65)]
gull=[None,(0.0,0.09,0.20,0.16),(0.54,0.02,0.29,0.19),(0.32,0.0,0.49,0.17),None]
write(6957,"B","coffee break","female",[
 ("to clutch a metal flask","the woman","female",woman),
 ("to bite into a croissant","the man","male",man),
 ("to soar past the turbine","the seagull","female",gull)],
 1.2,[("a seagull",0.68,0.10,"female"),("a turbine blade",0.35,0.20,"female"),("a flask",0.22,0.57,"female"),("a lunch box",0.43,0.75,"female")],
 "What are the two workers having?","They are having a coffee break.","female",
 "seagull visible only 0.7-1.7 (partly cut at frame edge at 0.7); several flasks on the roof, pill sits on the one the woman holds; man's box includes his legs reaching to x .5",T)
