from gen_6851_6852_6853_6854_lib import write
wom = [(0.16,0.19,0.4,0.71),(0.15,0.18,0.42,0.72),(0.13,0.17,0.45,0.72),(0.12,0.16,0.48,0.74),(0.11,0.15,0.47,0.75),(0.09,0.14,0.49,0.77),(0.07,0.14,0.47,0.78),(0.12,0.15,0.44,0.77)]
dog = [(0.56,0.59,0.26,0.28),(0.57,0.59,0.31,0.29),(0.58,0.6,0.37,0.3),(0.6,0.64,0.24,0.26),(0.58,0.63,0.26,0.3),(0.58,0.64,0.33,0.3),(0.54,0.61,0.4,0.33),(0.56,0.58,0.32,0.37)]
brd = [(0.17,0.05,0.81,0.14),(0.18,0.04,0.8,0.14),(0.18,0.03,0.8,0.14),(0.25,0.02,0.73,0.14),(0.2,0.01,0.77,0.14),(0.22,0.0,0.72,0.14),(0.24,0.0,0.74,0.14),(0.25,0.0,0.72,0.14)]
write(6853, "A", "bag", "female",
 [("to carry some ducks", "the woman", "female", wom),
  ("to wag its tail", "the dog", "female", dog),
  ("to fly across the sky", "the flying birds", "female", brd)],
 0.2,
 [("a cap", 0.55, 0.25, "female"), ("ducks", 0.27, 0.6, "female"), ("a dog", 0.7, 0.72, "female"), ("a bag", 0.45, 0.92, "female")],
 "What is the woman carrying?", "She is carrying some ducks.", "female",
 "Key word 'bag' is the hunting verb (to bag ducks); A-level texts use 'carry some ducks'. Woman/dog boxes split vertically at the dog's head; her reaching hand (1.7, 3.2) is cut. Tail wag is clear at 0.7, 1.2, 2.7. Flying geese named 'the flying birds' to keep them apart from the ducks she carries. Noun 'a bag' = the canvas bag on the grass (not the key-word verb sense).")
