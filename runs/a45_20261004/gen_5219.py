from gen_5217 import build
H={0.0:(0,0.18,0.47,0.82),0.5:(0,0.17,0.47,0.83),1.0:(0,0.18,0.47,0.82),1.5:(0,0.18,0.47,0.82),2.0:(0,0.16,0.47,0.84),
 2.5:(0,0.16,0.51,0.84),3.0:(0,0.23,0.56,0.77),3.5:(0.53,0.16,0.42,0.44),4.0:(0.51,0.17,0.47,0.44),4.5:(0.51,0.17,0.47,0.42),
 5.0:(0.51,0.16,0.49,0.44),5.5:(0,0.2,0.5,0.8),6.0:(0,0.2,0.5,0.8),6.5:(0,0.2,0.49,0.8),7.0:(0,0.2,0.49,0.8),7.5:(0,0.18,0.49,0.82),
 8.0:(0,0.18,0.49,0.82),8.5:(0,0.18,0.49,0.82),9.0:(0,0.19,0.49,0.81),9.5:(0,0.22,0.49,0.78),10.0:(0,0.21,0.49,0.79)}
C={0.0:(0.56,0.22,0.44,0.78),0.5:(0.48,0.22,0.52,0.78),1.0:(0.49,0.21,0.51,0.79),1.5:(0.48,0.21,0.52,0.79),2.0:(0.49,0.21,0.51,0.79),
 2.5:(0.52,0.21,0.48,0.79),3.0:(0.6,0.23,0.4,0.77),3.5:(0,0.01,0.52,0.99),4.0:(0,0.02,0.5,0.98),4.5:(0,0.06,0.5,0.94),
 5.0:(0,0.06,0.5,0.94),5.5:(0.5,0.22,0.5,0.78),6.0:(0.5,0.22,0.5,0.78),6.5:(0.5,0.18,0.5,0.82),7.0:(0.5,0.2,0.5,0.8),7.5:(0.5,0.2,0.5,0.8),
 8.0:(0.5,0.21,0.5,0.79),8.5:(0.5,0.21,0.5,0.79),9.0:(0.5,0.21,0.5,0.79),9.5:(0.5,0.24,0.5,0.76),10.0:(0.5,0.21,0.5,0.79)}
build(5219,{"keyWord":"roommate","dv":"male","boxes":{"H":H,"C":C},
 "taps":[("to stir the pasta","the curly-haired man","male","C"),("to wave his hand excitedly","the curly-haired man","male","C"),("to snack on crisps","the man in the hoodie","male","H")],
 "still":10.0,"nouns":[("the ceiling",0.6,0.07,"male"),("a T-shirt",0.72,0.44,"male"),("a hoodie",0.2,0.52,"male"),("crisps",0.53,0.61,"male")],
 "q":"What is the curly-haired man doing?","a":"He is stirring the pasta with a wooden spoon.","av":"male",
 "notes":"Two young men: the curly-haired man (grey T-shirt) and the man in the hoodie. Cuts at 3.5 (kitchen) and 5.5 (sofa). Stirring at 3.5-5.0; hand waving at 6.5-7.0 (open hand raised, slightly blurry - weakest phrase); hoodie man takes crisps at 8.0-9.0. In the kitchen shot the curly man's arm reaches across to the pot handle, his box is cut at x 0.50-0.52 to stay clear of the hoodie man behind him (who holds a plate). At 2.5 the two hands are close over the bag, split at x 0.52. Plates avoided: both seem to hold one at 4.0-5.0. Key word roommate is a person (two of them), not used as a pill."})
