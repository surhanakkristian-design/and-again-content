from gen_5217 import build
W={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,1,1),1.5:(0,0,1,1),2.0:(0.03,0.12,0.97,0.88),2.5:(0.06,0.18,0.94,0.82),
 3.0:(0.06,0.28,0.38,0.72),3.5:(0.11,0.32,0.37,0.68),4.0:(0.13,0.31,0.42,0.6),4.5:(0.06,0.37,0.38,0.48),5.0:(0.07,0.35,0.45,0.58),
 5.5:(0.27,0.35,0.36,0.64),6.0:(0.25,0.29,0.31,0.38),6.5:(0,0.57,0.24,0.25),7.0:(0.06,0.54,0.21,0.3),7.5:(0.2,0.31,0.62,0.69),
 8.0:(0.01,0.21,0.89,0.79),8.5:(0,0.08,1,0.92),9.0:(0,0.05,1,0.95)}
build(5222,{"keyWord":"steps","dv":"female","boxes":{"W":W},
 "taps":[("to trace a route","the hiker","female","W"),("to run past a boulder","the hiker","female","W"),("to climb the stone steps","the hiker","female","W")],
 "still":6.0,"nouns":[("the sky",0.55,0.12,"female"),("a rucksack",0.40,0.36,"female"),("steps",0.55,0.57,"female"),("grass",0.86,0.45,"female")],
 "q":"What is the hiker climbing?","a":"She is climbing a long flight of stone steps.","av":"female",
 "notes":"Only one person (the hiker), so all three taps use her. 0.0-1.5 are close-ups of her hands, the map and her torso/face filling the frame, so the box is the whole frame there (the map she holds is inside it). 'to trace a route' = finger along the red line at 0.0-1.0 (and again 8.0-8.5). Boulder with the red-and-white waymark at 4.5-5.0. The stone steps are only seen at 6.0 (one frame) - the answer relies on that shot; the steps go up out of frame, 'long flight' per the description. She is small at 6.5-7.0 (cairn shot), boxes padded to the minimum size."})
