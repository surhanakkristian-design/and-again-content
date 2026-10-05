from gen_7275_7276_7277_7278_lib import *
A=(0.12,0.24,0.51,0.31); B=(0.12,0.22,0.52,0.28)
sono=[A]*4+[B]*4
P1=(0,0.55,0.86,0.41); P2=(0,0.50,0.86,0.47)
pat=[P1]*4+[P2]*4
M1=(0.64,0.23,0.36,0.21); M2=(0.66,0.21,0.34,0.22)
mon=[M1]*4+[M2]*4
write(7275,"B","kidney","female",
 [("to point at the monitor","the woman in scrubs","female",sono),
  ("to lie on an examination couch","the woman with red hair","female",pat),
  ("to display a kidney","the monitor","female",mon)],
 1.2,
 [("a kidney",0.84,0.33,"female"),("a poster",0.60,0.44,"female"),("a bottle of gel",0.63,0.84,"female"),("red hair",0.12,0.72,"female")],
 "What is the woman in scrubs doing?","She is pointing at the kidney on the monitor.","female",
 "Woman in scrubs and patient overlap: boxes split horizontally at y .55 (later .50); the pointing hand reaches into the monitor box. Her probe hand lies inside the patient box.")
