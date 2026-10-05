from gen_6831_6832_6833_6834_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman=[(0.10,0.39,0.81,0.89),(0.09,0.40,0.83,0.90),(0.06,0.41,0.80,0.93),(0.03,0.41,0.78,0.94),
       (0.01,0.42,0.67,1.0),(0.03,0.40,0.75,1.0),(0.30,0.17,0.92,1.0),(0.31,0.14,0.85,1.0)]
men=[(0.0,0.19,0.45,0.39),(0.0,0.19,0.45,0.40),(0.0,0.20,0.43,0.41),(0.0,0.20,0.46,0.41),
     (0.0,0.20,0.41,0.42),(0.02,0.21,0.34,0.40),(0.04,0.23,0.30,0.42),(0.08,0.23,0.31,0.42)]
build(6832,"B","ambassador","female",[
 ("to grin at the camera","the woman","female",woman),
 ("to carry a sealed envelope","the woman","female",woman),
 ("to line the palace steps","the men in dark suits","female",men)],
 0.7,[("steps",0.20,0.44,"female"),("horses",0.62,0.30,"female"),("an envelope",0.38,0.59,"female"),("a wheel",0.82,0.69,"female")],
 "What is the woman holding?","She is holding a sealed envelope.","female",
 "Key word 'ambassador' not used as a noun: nothing in the picture proves she is one. Third target is a group (the men in dark suits on the steps). Their box sits beside/behind the woman's head: until 2.7 the woman's box starts below the men's line (her hat/head partly outside), from 3.2 her box starts right of the men (left coat edge outside). Pushing the wheel avoided as a phrase because the footmen push it too.",T)
