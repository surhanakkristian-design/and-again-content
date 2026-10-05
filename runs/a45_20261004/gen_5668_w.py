from gen_5664_5665_5667_5668_lib import write
W=[(0.24,0.26,0.26,0.51),(0.25,0.26,0.26,0.52),(0.25,0.26,0.25,0.52),(0.27,0.25,0.39,0.55),(0.28,0.24,0.41,0.56),(0.28,0.22,0.41,0.64),(0.24,0.22,0.41,0.78),(0.24,0.21,0.43,0.79)]
V=[(0.50,0.27,0.19,0.35),(0.51,0.27,0.19,0.35),(0.50,0.27,0.18,0.36),None,None,None,None,None]
H=[(0.80,0.69,0.20,0.24)]*8
write(5668,"A","book a table","female",[
 ("to point at a table","the woman","female",W),
 ("to pull out a chair","the waiter","male",V),
 ("to hold a pen","the hand with the pen","female",H)],
 0.2,[("a plant",0.49,0.24,"female"),("flowers",0.77,0.37,"female"),("a table",0.72,0.49,"female"),("a book",0.62,0.85,"female")],
 "Where is the woman pointing?","She is pointing at a table by the window.","female",
 "Woman's pointing arm crosses in front of the waiter at 0.2-1.2; boxes split at x~0.50, so her pointing hand lies in the waiter's region/outside. Waiter set off from 1.7 on: only his head shows beside the woman's head, inside her box area. Hand with the pen (lower right) - owner unclear. Man in black (back to camera) not used as a target.")
