from gen_6831_6832_6833_6834_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman=[(0.37,0.26,0.62,1.0),(0.36,0.24,0.63,1.0),(0.34,0.24,0.63,1.0),(0.31,0.24,0.63,1.0),
       (0.30,0.20,0.64,1.0),(0.28,0.19,0.64,1.0),(0.20,0.21,0.64,1.0),(0.16,0.15,0.68,1.0)]
parrot=[(0.62,0.44,0.80,0.58),(0.63,0.44,0.81,0.59),(0.63,0.45,0.81,0.62),(0.63,0.45,0.81,0.62),
        (0.64,0.47,0.84,0.64),(0.64,0.48,0.86,0.66),(0.64,0.49,0.90,0.67),(0.68,0.49,0.93,0.76)]
man=[(0.66,0.58,1.0,0.92),(0.66,0.59,1.0,0.92),(0.66,0.62,1.0,0.95),(0.66,0.62,1.0,0.98),
     (0.70,0.64,1.0,1.0),(0.74,0.66,1.0,1.0),(0.78,0.67,1.0,1.0),(0.82,0.76,1.0,1.0)]
build(6831,"B","amazon","female",[
 ("to raise a mango slice","the woman","female",woman),
 ("to perch on her shoulder","the parrot on her shoulder","female",parrot),
 ("to duck under a tray","the man","male",man)],
 0.7,[("an awning",0.18,0.31,"female"),("palm trees",0.72,0.12,"female"),("mangoes",0.18,0.64,"female"),("an amazon",0.70,0.52,"female")],
 "What is the man doing?","He is ducking under a tray.","male",
 "Key word 'amazon' = the parrot (Amazon parrot); several amazons fly around, the noun pill sits on the one perched on her shoulder. Shoulder parrot box overlaps the woman's shoulder/man's tray; split along the lines between them. Man is only partly visible behind the woman at 3.2-3.7.",T)
