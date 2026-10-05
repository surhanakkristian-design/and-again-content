from gen_6851_6852_6853_6854_lib import write
scr = [(0.2,0.05,0.62,0.25),(0.2,0.04,0.63,0.19),(0.19,0.04,0.64,0.17),(0.19,0.03,0.65,0.17),(0.18,0.02,0.67,0.18),(0.18,0.02,0.66,0.16),(0.17,0.03,0.67,0.15),(0.17,0.03,0.69,0.16)]
man = [(0.32,0.3,0.46,0.26),(0.33,0.23,0.48,0.33),(0.32,0.21,0.5,0.35),(0.32,0.2,0.5,0.36),(0.32,0.2,0.52,0.36),(0.32,0.18,0.52,0.38),(0.31,0.18,0.53,0.39),(0.31,0.19,0.53,0.39)]
wom = [(0.51,0.56,0.49,0.44),(0.52,0.56,0.48,0.44),(0.51,0.56,0.49,0.44),(0.51,0.56,0.49,0.44),(0.51,0.56,0.49,0.44),(0.52,0.56,0.48,0.44),(0.49,0.57,0.51,0.43),(0.5,0.58,0.5,0.42)]
write(6852, "B", "bacteria", "male",
 [("to raise a petri dish", "the man", "male", man),
  ("to gasp in surprise", "the woman", "female", wom),
  ("to show magnified bacteria", "the screen", "male", scr)],
 2.2,
 [("bacteria", 0.5, 0.1, "male"), ("a petri dish", 0.55, 0.3, "male"), ("a lab coat", 0.53, 0.78, "male"), ("a tracksuit top", 0.84, 0.9, "male")],
 "What is the man holding up?", "He is holding up a petri dish.", "male",
 "The woman stands in front of the man: man box = upper body, arms, dish and head (y<0.56); woman box = from her raised hand down (y>=0.56), so her head top and the man's lower coat are cut. Woman's mouth opens in surprise from 1.2 (at 0.2-0.7 only staring). 'bacteria' pill on the screen with the magnified cells; the glowing colonies in the dish could also be read as bacteria.")
