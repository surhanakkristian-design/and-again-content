from gen_5217 import build
g={0.0:(0,0.21,0.69,0.79),0.5:(0,0.13,0.67,0.87),1.0:(0,0.13,0.79,0.87),1.5:(0,0.17,0.93,0.83),2.0:(0,0.2,0.98,0.8),
 2.5:(0,0.16,1.0,0.84),3.0:(0,0.30,0.67,0.70),3.5:(0,0.26,0.80,0.74),4.0:(0,0.28,1.0,0.72),4.5:(0,0.27,0.97,0.73),
 5.0:(0.03,0.32,0.62,0.68),5.5:(0,0.23,0.76,0.77),6.0:(0,0.20,0.82,0.80),6.5:(0,0.23,0.53,0.77),7.0:(0.34,0.35,0.34,0.65),
 7.5:(0.31,0.32,0.36,0.68),8.0:(0.28,0.31,0.44,0.69),8.5:(0.14,0.30,0.71,0.70),9.0:(0.0,0.31,0.98,0.69),9.5:(0.13,0.34,0.71,0.66),
 10.0:(0.29,0.37,0.39,0.63),10.5:(0.35,0.39,0.32,0.59),11.0:(0.28,0.42,0.50,0.55),11.5:(0.38,0.43,0.30,0.53),12.0:(0.38,0.44,0.31,0.53)}
build(5218,{"keyWord":"room","dv":"female","boxes":{"g":g},
 "taps":[("to open a door","the girl","female","g"),("to walk into a big room","the girl","female","g"),("to look up at the ceiling","the girl","female","g")],
 "still":11.0,"nouns":[("the ceiling",0.5,0.12,"female"),("windows",0.52,0.34,"female"),("a girl",0.53,0.62,"female"),("the floor",0.2,0.86,"female")],
 "q":"What is the girl doing?","a":"She is looking up at the ceiling.","av":"female",
 "notes":"Only one person, so all three taps use the girl. Many cuts (study, kitchen, bedroom, hall); she is visible in every frame, at 2.0-2.5 mostly her face plus the arm on the door handle at the bottom, so the box spans the frame. 'to walk into a big room' fits 7.0-10.0 (vaulted hall). Key word 'room' is not a placeable noun (the whole space), so it is not a pill. 'windows' = the group of three arched windows, pill on the middle one."})
