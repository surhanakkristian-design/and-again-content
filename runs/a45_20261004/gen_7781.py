from gen_7781_7783_7784_7785_lib import *
fox=[(0.12,0.40,0.60,0.74)]+[(0.04,0.44,0.62,0.745)]*6+[(0.04,0.40,0.62,0.745)]
rh=[(0.60,0.56,0.99,0.99)]+[(0.62,0.66,0.99,0.99)]*7
lh=[(0.02,0.745,0.48,0.99)]*8
write(7781,"A","close","male",[
 ("to smell the hand","the fox","male",fox),
 ("to hold the tent door","the hand on the right","male",rh),
 ("to rest on the floor","the hand on the left","male",lh)],
 2.2,[("trees",0.40,0.18,"male"),("a lake",0.72,0.36,"male"),("a kettle",0.58,0.465,"male"),("a fox",0.36,0.56,"male")],
 "Where is the fox?","The fox is close to the tent.","male",
 "POV clip, no visible person: defaultVoice male (evenId false). Fox blurred behind the tent flap at 0.2. 'the hand on the left' rests on the tent floor the whole clip (weakest phrase). Fox box ends at x .62 to keep clear of the right hand at its nose.")
