from lib_7055_7056_7057_7058 import build
man = [(0.19,0.20,0.67,0.96),(0.19,0.20,0.69,0.97),(0.17,0.19,0.69,0.99),(0.16,0.19,0.71,1.0),
       (0.16,0.17,0.72,1.0),(0.16,0.16,0.72,1.0),(0.16,0.16,0.73,1.0),(0.16,0.16,0.72,1.0)]
cat = [(0.0,0.34,0.18,0.49),(0.0,0.34,0.18,0.49),(0.0,0.34,0.17,0.49),(0.0,0.34,0.16,0.49),
       (0.0,0.34,0.16,0.49),(0.0,0.34,0.16,0.49),(0.0,0.34,0.16,0.50),(0.0,0.34,0.16,0.50)]
slp = [(0.73,0.56,1.0,0.86),(0.72,0.56,1.0,0.87),(0.73,0.57,1.0,0.87),(0.74,0.58,1.0,0.90),
       (0.75,0.58,1.0,0.90),(0.75,0.59,1.0,0.92),(0.76,0.61,1.0,0.94),(0.77,0.61,1.0,0.95)]
build(7056, "A", "do the laundry", "male",
  [("to hold a basket", "the man with the basket", "male", man),
   ("to sit on a washing machine", "the cat", "male", cat),
   ("to sleep on a bench", "the man on the bench", "male", slp)],
  2.7,
  [("a window", 0.22, 0.27, "male"), ("a cat", 0.10, 0.42, "male"),
   ("a basket", 0.32, 0.56, "male"), ("a bench", 0.90, 0.76, "male")],
  "What is the cat doing?", "It is sitting on a washing machine.", "male",
  "Cat sits on top of the row of washing machines at the left. From 1.7 s the basket's left tip comes close to the cat: the man box starts at 0.16 and cuts the tip a little. Woman at the dryer not used (her box would overlap the man).")
