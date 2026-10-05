from gen_7781_7783_7784_7785_lib import *
com=[(0.05,0.15,0.52,0.51),(0.07,0.14,0.54,0.51),(0.10,0.16,0.56,0.55),(0.12,0.14,0.60,0.55),(0.15,0.14,0.63,0.55),(0.19,0.12,0.68,0.55),(0.23,0.13,0.72,0.56),(0.26,0.13,0.74,0.56)]
blu=[(0.27,0.51,0.61,0.77),(0.27,0.51,0.62,0.74),(0.27,0.55,0.62,0.78),(0.28,0.55,0.62,0.78),(0.26,0.55,0.63,0.78),(0.27,0.55,0.66,0.80),(0.25,0.56,0.64,0.80),(0.27,0.56,0.66,0.80)]
man=[(0.62,0.44,1.0,0.78),(0.63,0.45,1.0,0.75),(0.63,0.50,1.0,0.80),(0.63,0.49,1.0,0.78),(0.64,0.53,1.0,0.82),(0.70,0.57,1.0,0.82),None,None]
write(7785,"B","comic","female",[
 ("to grip the microphone","the woman on stage","female",com),
 ("to spill her drink","the woman in blue","female",blu),
 ("to slide off his chair","the man in the cream jumper","male",man)],
 1.2,[("a brick wall",0.22,0.12,"female"),("curtains",0.76,0.22,"female"),("a microphone",0.33,0.30,"female"),("a candle",0.48,0.81,"female")],
 "What is the woman on stage doing?","She is performing a comic routine on stage.","female",
 "defaultVoice female: main person is the comedian. Drink spills at 2.7 (glass falls). Man in cream jumper slides out of frame to the right from 2.7: only his cream back at the right edge at 2.7, off at 3.2-3.7 (a cream sleeve at the right edge there may be him or the clapping person in front). Comedian/woman-in-blue boxes split at her head (comedian's legs cut a little).")
