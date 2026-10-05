from gen_5702_5703_5704_5705_lib import write
S = [(0.2,0.0,0.43,0.55,0.57),(0.7,0.15,0.42,0.50,0.58),(1.2,0.08,0.40,0.48,0.55),(1.7,0.10,0.40,0.43,0.50),
     (2.2,0.12,0.40,0.38,0.42),(2.7,0.12,0.40,0.35,0.42),(3.2,0.08,0.41,0.35,0.42),(3.7,0.07,0.42,0.36,0.42)]
T = [(0.2,0.71,0.17,0.29,0.83),(0.7,0.74,0.17,0.26,0.83),(1.2,0.66,0.20,0.34,0.74),(1.7,0.53,0.22,0.47,0.68),
     (2.2,0.50,0.23,0.47,0.63),(2.7,0.47,0.24,0.44,0.60),(3.2,0.43,0.25,0.42,0.58),(3.7,0.51,0.26,0.31,0.55)]
write(5703, "B", "cancel plans", "female",
  [("to dig into her ice cream", "the woman in pyjamas", "female", S),
   ("to gesture in disbelief", "the woman in the sequined top", "female", T),
   ("to snuggle under a blanket", "the woman in pyjamas", "female", S)],
  2.7,
  [("a pendant lamp", 0.33, 0.20, "female"), ("a handbag", 0.64, 0.52, "female"), ("a blanket", 0.35, 0.66, "female"), ("a sofa", 0.22, 0.84, "female")],
  "What is the woman in pyjamas doing?", "She is digging into her ice cream.", "female",
  "Standing woman's spread hand reaches close to the sofa woman at 1.7-3.2; boxes split vertically. Sofa-woman boxes include the blanket over her legs in the early close frames.")
