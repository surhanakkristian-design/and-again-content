from gen_5702_5703_5704_5705_lib import write
man = [(0.2,0.24,0.29,0.54,0.71),(0.7,0.23,0.30,0.56,0.70),(1.2,0.22,0.32,0.55,0.68),(1.7,0.28,0.32,0.47,0.68),
       (2.2,0.28,0.33,0.40,0.63),(2.7,0.31,0.34,0.31,0.58),(3.2,0.32,0.35,0.26,0.53),(3.7,0.34,0.35,0.26,0.52)]
wom = [(0.2,0.0,0.35,0.24,0.65),(0.7,0.0,0.36,0.23,0.64),(1.2,0.0,0.37,0.22,0.63),(1.7,0.02,0.38,0.26,0.62),
       (2.2,0.06,0.37,0.22,0.59),(2.7,0.07,0.37,0.24,0.55),(3.2,0.10,0.38,0.22,0.51),(3.7,0.12,0.38,0.22,0.50)]
write(5702, "A", "calm down", "male",
  [("to close his eyes", "the man", "male", man),
   ("to touch his shoulder", "the woman", "female", wom),
   ("to breathe out slowly", "the man", "male", man)],
  3.7,
  [("a lantern", 0.46, 0.16, "male"), ("a man", 0.47, 0.50, "male"), ("a woman", 0.22, 0.62, "female"), ("a scooter", 0.80, 0.80, "male")],
  "What is the man doing?", "He is closing his eyes.", "male",
  "Woman's hand reaches onto the man's shoulder; boxes split vertically between them. Scooter not used as a tap target (overlaps the man's box).")
