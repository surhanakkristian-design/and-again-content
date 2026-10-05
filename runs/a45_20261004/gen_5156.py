from gen_5156_5157_5158_5161_lib import build
T = [i*0.5 for i in range(19)]
p10 = {0.0:(0,0,0.82,0.83),0.5:(0.06,0,0.65,0.72),1.0:(0,0,0.62,0.74),1.5:(0.14,0.02,0.64,0.78),
 2.0:(0.35,0.27,0.24,0.26),2.5:(0.6,0.27,0.27,0.25),3.0:(0.34,0.28,0.3,0.27),3.5:(0.45,0.3,0.33,0.28),
 4.0:(0.48,0.27,0.34,0.34),4.5:(0.43,0.24,0.46,0.42),5.0:(0.6,0.23,0.4,0.49),5.5:(0.72,0.1,0.28,0.54),
 6.0:(0.37,0.13,0.63,0.56),6.5:(0.48,0.21,0.5,0.52),7.0:(0.1,0.16,0.58,0.59),7.5:(0.28,0.15,0.7,0.82),
 8.0:(0.22,0.11,0.51,0.89),8.5:(0.13,0.15,0.49,0.85),9.0:(0,0.26,0.33,0.4)}
mate = {8.0:(0.74,0.05,0.26,0.82),8.5:(0.63,0,0.37,0.95),9.0:(0.34,0,0.66,0.97)}
build(5156,"B","kneel","male",[
 ("to dribble past a defender","the player in number 10","male",p10),
 ("to kneel on the pitch","the player in number 10","male",p10),
 ("to hug the goal scorer","the teammate","male",mate)],
 6.0,[("a goal",0.22,0.42,"male"),("a footballer",0.72,0.42,"male"),("spectators",0.82,0.12,"male"),("a white line",0.82,0.8,"male")],
 "What is the scorer doing?",["He","is","kneeling","on","the","pitch."],"male",
 "Teammate box only from 8.0 (other yellow players earlier cannot be identified as him). At 9.0 two teammates hug the scorer; box covers the front hugger and the one behind; scorer's box = his face at left. Defender is not a target.",T)
