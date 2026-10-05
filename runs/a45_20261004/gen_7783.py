from gen_7781_7783_7784_7785_lib import *
w=[(0.0,0.55,0.86,0.84),(0.0,0.54,0.88,0.84),(0.0,0.53,0.90,0.84),(0.0,0.52,0.90,0.84),(0.0,0.52,0.82,0.84),(0.0,0.51,0.88,0.84),(0.0,0.52,0.84,0.84),(0.0,0.50,0.90,0.84)]
lad=[(0.80,0.37,1.0,0.51),(0.82,0.34,1.0,0.50),(0.80,0.32,1.0,0.48),(0.80,0.31,1.0,0.47),(0.80,0.27,1.0,0.43),(0.82,0.26,1.0,0.41),(0.80,0.24,1.0,0.40),(0.82,0.22,1.0,0.38)]
dv=[(0.29,0.28,0.51,0.43),(0.33,0.26,0.56,0.41),(0.34,0.24,0.56,0.42),(0.32,0.24,0.55,0.38),(0.30,0.32,0.48,0.51),None,None,None]
write(7783,"B","comfort zone","female",[
 ("to sip an iced drink","the woman in sunglasses","female",w),
 ("to climb the diving tower","the man on the ladder","male",lad),
 ("to dive head first","the woman in blue","female",dv)],
 3.2,[("a diving tower",0.70,0.17,"female"),("beach huts",0.55,0.43,"female"),("a drink",0.42,0.58,"female"),("an inflatable ring",0.28,0.83,"female")],
 "What is the woman in sunglasses doing?","She is lounging on an inflatable ring.","female",
 "Diver in the blue swimsuit visible 0.2-2.2 (flip in the air, then entering the water), off after the splash. Man on ladder is small at the right edge: boxes padded to the 0.18 minimum. Star-jump man (0.2-0.7) left untargeted. Woman sips at 1.2-2.7 and holds the drink the rest.")
