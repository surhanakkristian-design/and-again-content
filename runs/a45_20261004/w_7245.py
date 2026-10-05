from w_7245_7246_7247_7248_lib import write
woman = [(0.18,0.34,0.50,0.60),(0.17,0.34,0.50,0.59),(0.16,0.33,0.47,0.59),(0.16,0.33,0.45,0.58),
         (0.17,0.34,0.47,0.58),(0.17,0.33,0.47,0.56),(0.17,0.32,0.46,0.55),(0.15,0.33,0.45,0.55)]
dog =   [(0.19,0.60,0.86,0.90),(0.29,0.59,0.94,0.91),(0.12,0.59,0.95,0.91),(0.12,0.58,0.92,0.90),
         (0.08,0.58,0.85,0.91),(0.14,0.56,0.82,0.90),(0.11,0.55,0.81,0.92),(0.00,0.55,0.80,0.92)]
man =   [(0.84,0.34,1.00,0.60),(0.80,0.34,1.00,0.59),(0.77,0.34,0.98,0.59),(0.72,0.34,0.96,0.58),
         (0.68,0.34,0.95,0.58),(0.66,0.34,0.96,0.56),(0.64,0.33,0.96,0.55),(0.64,0.33,0.96,0.55)]
write(7245, "B", "inn", "female",
  [("to drag a suitcase", "the woman", "female", woman),
   ("to carry a glowing lantern", "the dog", "female", dog),
   ("to wait in the doorway", "the man", "male", man)],
  2.2,
  [("an inn", 0.70, 0.12, "female"), ("skis", 0.52, 0.50, "female"),
   ("a lantern", 0.80, 0.70, "female"), ("a suitcase", 0.12, 0.76, "female")],
  "What is the woman doing?", ["She", "is", "dragging", "a", "suitcase", "through", "the", "snow."], "female",
  "Woman's legs and man's legs sit behind/next to the dog, so their boxes are cut at the dog's back line to avoid overlap. Dog is a St Bernard.")
