from gen_5664_5665_5667_5668_lib import write
R=[(0.42,0.47,0.37,0.45),(0.46,0.34,0.30,0.57),(0.46,0.35,0.23,0.57),(0.46,0.28,0.28,0.64),(0.44,0.35,0.29,0.58),(0.43,0.31,0.31,0.63),(0.42,0.34,0.31,0.62),(0.42,0.34,0.31,0.62)]
B=[(0.55,0.30,0.38,0.17),(0.76,0.30,0.19,0.19),(0.69,0.30,0.23,0.19),(0.74,0.30,0.21,0.19),(0.73,0.29,0.22,0.18),(0.74,0.29,0.22,0.18),(0.73,0.30,0.22,0.18),(0.73,0.30,0.24,0.18)]
C=[(0,0.38,0.27,0.15),(0,0.38,0.26,0.15),(0,0.38,0.25,0.15),(0,0.38,0.25,0.15),(0,0.37,0.24,0.15),(0,0.36,0.23,0.15),(0,0.34,0.21,0.15),(0,0.28,0.19,0.14)]
write(5667,"B","boo","male",[
 ("to jump to his feet","the man in orange","male",R),
 ("to give two thumbs down","the man in black","male",B),
 ("to lean forward on stage","the comedian","male",C)],
 0.2,[("a spotlight",0.81,0.09,"male"),("a paper plane",0.39,0.17,"male"),("a waitress",0.30,0.55,"female"),("a glass of beer",0.82,0.78,"male")],
 "What is the man in orange doing?","He is booing the comedian on stage.","male",
 "Man in orange (rust shirt) and man in black overlap: at 0.2 split horizontally at y 0.47 (orange man seated below), later split vertically at x~0.69-0.76 between their heads, so the man in black's left arm and the orange man's right shoulder fall outside both boxes. 'Booing' inferred from cupped hand + thumb down (sound not needed). Camera drifts slightly; comedian rises at 3.7.")
