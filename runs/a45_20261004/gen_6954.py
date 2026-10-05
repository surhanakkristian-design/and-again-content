from gen_6950_6951_6953_6954_lib import write
W=[(0.42,0.15,0.47,0.74),(0.44,0.15,0.47,0.74),(0.44,0.14,0.48,0.80),(0.44,0.14,0.54,0.82),(0.40,0.23,0.48,0.73),(0.42,0.21,0.58,0.79),(0.40,0.22,0.42,0.78),(0.40,0.21,0.47,0.79)]
M=[(0.06,0.42,0.36,0.37),(0.05,0.42,0.39,0.37),(0.03,0.42,0.41,0.39),(0.02,0.42,0.42,0.39),(0.0,0.42,0.40,0.42),(0.0,0.42,0.42,0.42),(0.0,0.42,0.40,0.45),(0.0,0.42,0.40,0.45)]
write(6954,"B","click","female",[
 ("to click her castanets","the woman","female",W),
 ("to strum a guitar","the man","male",M),
 ("to spin on the spot","the woman","female",W)],
 3.2,[("a bell tower",0.86,0.15,"female"),("a guitar",0.12,0.62,"female"),("geraniums",0.84,0.70,"female"),("a skirt",0.60,0.87,"female")],
 "What is the woman doing?","She is clicking her castanets.","female",
 "Woman and man boxes split along a vertical line (x 0.40-0.44); the swirling skirt and guitar neck cross it at some frames. Castanets clearly visible at 0.2-1.7 s, in her hands later.")
