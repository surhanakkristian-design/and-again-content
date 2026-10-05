from gen_5156_5157_5158_5161_lib import build
T = [i*0.5 for i in range(25)]
young = {0.0:(0.05,0.35,0.46,0.56),0.5:(0.03,0.35,0.55,0.58),1.0:(0,0.37,0.37,0.57),1.5:(0,0.36,0.32,0.54),2.0:(0,0.36,0.33,0.53)}
apron = {2.5:(0.28,0.32,0.2,0.35),3.0:(0.3,0.38,0.3,0.43),3.5:(0.28,0.38,0.34,0.6),4.0:(0.16,0.57,0.44,0.43),4.5:(0.62,0.35,0.38,0.65)}
dread = {0.0:(0.52,0.26,0.48,0.74),0.5:(0.68,0.26,0.32,0.74),1.0:(0.48,0.24,0.52,0.76),1.5:(0.58,0.25,0.42,0.75),
 2.0:(0.5,0.28,0.5,0.72),2.5:(0.48,0.2,0.52,0.8),3.0:(0.74,0.42,0.26,0.58),3.5:(0.62,0.2,0.38,0.8),
 4.0:(0.24,0.25,0.76,0.32),4.5:(0.12,0.2,0.5,0.52),5.0:(0,0.26,0.64,0.68),5.5:(0,0.18,0.43,0.75),
 6.0:(0,0.21,0.2,0.69),6.5:(0,0.36,0.21,0.34),7.0:(0.09,0.39,0.33,0.28),7.5:(0.2,0.39,0.25,0.29),
 8.0:(0.19,0.38,0.2,0.27),9.5:(0.29,0.35,0.2,0.27),10.0:(0.42,0.41,0.2,0.2)}
build(5157,"B","neighbourhood","male",[
 ("to juggle a football","the young man in yellow","male",young),
 ("to hurry into the street","the woman in an apron","female",apron),
 ("to double up with laughter","the man with dreadlocks","male",dread)],
 7.0,[("a hill",0.55,0.25,"male"),("a parked car",0.8,0.49,"male"),("a football",0.43,0.73,"male"),("cobblestones",0.5,0.9,"male")],
 "What are the men doing?",["They","are","playing","football","on","a","cobbled","street."],"male",
 "Young man in the yellow vest boxed only 0-2 s (a player in yellow later may be him, not certain). Apron woman 2.5-4.5 only. Dreadlock man off at 8.5-9.0 and inside the huddle from 10.5. At 4.0/4.5 dreadlock man and apron woman overlap: boxes split.",T)
