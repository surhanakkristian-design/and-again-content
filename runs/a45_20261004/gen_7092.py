import sys; sys.path.insert(0,'.')
from gen_7090_7091_7092_7093_lib import write
M=[(0.68,0.00,0.32,0.65),(0.73,0.00,0.27,0.64),(0.71,0.00,0.29,0.70),(0.71,0.00,0.29,0.76),
   (0.68,0.00,0.32,0.86),(0.64,0.00,0.36,0.96),(0.64,0.02,0.36,0.98),(0.62,0.10,0.38,0.90)]
S=[(0.01,0.00,0.66,0.50),(0.01,0.00,0.66,0.51),(0.01,0.00,0.66,0.55),(0.01,0.00,0.66,0.62),
   (0.01,0.00,0.66,0.72),(0.01,0.00,0.63,0.82),(0.01,0.00,0.63,1.00),(0.01,0.00,0.61,1.00)]
write(7092,"B","expose","male",
 [("to hold a black cloth","the young man","male",M),
  ("to grin at the statue","the young man","male",M),
  ("to melt in the hot sun","the ice statue","male",S)],
 3.7,
 [("an ice statue",0.30,0.45,"male"),("a flat cap",0.88,0.15,"male"),("a waistcoat",0.88,0.38,"male"),("a tourist",0.58,0.68,"male")],
 "What is the young man doing?","He is grinning at the melting statue.","male",
 "young man is only legs until ~2.2 s (camera tilts up), cloth in his hands from 2.7 s, grin clearest at 3.2-3.7 s; tourists left out as targets because they stand behind the statue's arm; statue box at 0.2 s includes the black cloth still on it")
