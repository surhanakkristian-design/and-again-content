from gen_7935_7936_7937_7938_lib import write
man = [(0.05,0.28,0.40,0.44),(0.05,0.28,0.38,0.44),(0.03,0.27,0.41,0.45),(0.04,0.27,0.40,0.45),
       (0.00,0.21,0.30,0.51),(0.00,0.21,0.29,0.51),(0.00,0.20,0.29,0.52),(0.00,0.21,0.30,0.52)]
red = [(0.46,0.58,0.18,0.15),(0.44,0.60,0.23,0.14),(0.45,0.60,0.24,0.14),(0.45,0.60,0.22,0.14),
       (0.31,0.61,0.36,0.13),(0.31,0.61,0.37,0.13),(0.30,0.61,0.34,0.13),(0.30,0.61,0.31,0.13)]
wom = [(0.65,0.38,0.22,0.43),(0.68,0.37,0.22,0.44),(0.70,0.37,0.19,0.44),(0.68,0.37,0.22,0.44),
       (0.68,0.34,0.24,0.50),(0.69,0.34,0.26,0.50),(0.65,0.35,0.29,0.51),(0.62,0.35,0.32,0.51)]
write(7935, "B", "percentage", "male", [
  ("to empty a metal bowl", "the man", "male", man),
  ("to lower the clear lid", "the woman", "female", wom),
  ("to form a thin layer", "the red balls", "male", red)],
  2.2, [("a metal bowl", 0.12, 0.49, "male"), ("a plastic lid", 0.53, 0.42, "male"),
        ("a cloth sack", 0.10, 0.80, "male"), ("a houseplant", 0.78, 0.29, "male")],
  "What is the man doing?", "He is tipping red balls out of a bowl.", "male",
  "Key word 'percentage' is abstract, not placed as a noun. Red-balls box covers the layer in the box only (not the stray balls on the floor); at 0.7-1.7 its left part is cut to keep clear of the man's box. Woman's hands on the lid are partly outside her box at 3.2/3.7 to avoid the red layer box.")
