from gen_6831_6832_6833_6834_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman=[(0.08,0.18,0.62,0.90),(0.11,0.21,0.62,0.92),(0.10,0.25,0.62,0.96),(0.11,0.25,0.63,0.97),
       (0.11,0.25,0.64,0.97),(0.10,0.25,0.65,0.97),(0.10,0.24,0.64,0.97),(0.11,0.24,0.64,0.97)]
man=[(0.70,0.46,1.0,1.0),(0.73,0.49,1.0,1.0),(0.73,0.51,1.0,1.0),(0.74,0.52,1.0,1.0),
     (0.72,0.52,1.0,1.0),(0.72,0.51,1.0,1.0),(0.69,0.51,1.0,1.0),(0.72,0.51,1.0,1.0)]
build(6834,"B","angle","female",[
 ("to measure the angle","the woman","female",woman),
 ("to stand on a ladder","the woman","female",woman),
 ("to prop up a beam","the young man","male",man)],
 1.2,[("an angle",0.49,0.20,"female"),("a set square",0.47,0.33,"female"),("a toolbox",0.38,0.81,"female"),("a safety vest",0.87,0.80,"female")],
 "What is the woman measuring?","She is measuring the angle.","female",
 "Woman on the balcony left out as a target: she stands behind the ladder woman's box at every frame. 'an angle' pill sits on the apex where the two beams meet (key word). Question says just 'the woman': the balcony woman is small in the background and measures nothing, the 7-word limit leaves no room for 'on the ladder'. Check it reads as concrete enough. The woman also grips the beam with one hand, but only the man pushes it up from below.",T)
