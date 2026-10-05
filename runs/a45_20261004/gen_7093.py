import sys; sys.path.insert(0,'.')
from gen_7090_7091_7092_7093_lib import write
W=[(0.00,0.11,0.36,0.89),(0.00,0.11,0.37,0.89),(0.00,0.11,0.37,0.89),(0.00,0.10,0.46,0.90),
   (0.00,0.08,0.56,0.92),(0.00,0.06,0.57,0.94),(0.00,0.05,0.57,0.95),(0.00,0.04,0.57,0.96)]
U=[(0.63,0.27,0.20,0.27),(0.65,0.28,0.20,0.27),(0.68,0.29,0.20,0.27),(0.70,0.29,0.21,0.27),
   (0.73,0.29,0.21,0.28),(0.75,0.29,0.22,0.29),(0.78,0.30,0.22,0.28),(0.78,0.31,0.22,0.29)]
write(7093,"B","extra","female",
 [("to lower her gaze","the woman in front","female",W),
  ("to close her eyes","the woman in front","female",W),
  ("to hold up an umbrella","the man with the umbrella","male",U)],
 0.2,
 [("a tarpaulin",0.62,0.10,"female"),("an extra",0.14,0.60,"female"),("an umbrella",0.72,0.30,"female"),("cobblestones",0.70,0.72,"female")],
 "What is the woman in front doing?","She is standing behind a thick rope.","female",
 "only two targets: the second extra in a brown hat stands right behind the front woman and overlaps her box; umbrella man is small (min-size box covers the three men under the umbrella); 'lower her gaze' 0.7-1.7 s, 'close her eyes' 2.2-3.2 s")
