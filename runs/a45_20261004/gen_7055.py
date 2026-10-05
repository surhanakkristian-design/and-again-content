from lib_7055_7056_7057_7058 import build
man = [(0.11,0.15,0.61,0.87),(0.20,0.22,0.63,0.87),(0.18,0.19,0.63,0.86),(0.16,0.18,0.63,0.91),
       (0.09,0.14,0.64,0.93),(0.08,0.12,0.66,0.93),(0.05,0.11,0.67,0.96),(0.06,0.11,0.69,0.95)]
wom = [(0.62,0.43,0.92,0.63),(0.64,0.44,0.92,0.63),(0.64,0.43,0.93,0.63),(0.64,0.42,0.95,0.65),
       (0.65,0.44,0.99,0.67),(0.67,0.45,0.99,0.67),(0.68,0.48,0.99,0.70),(0.70,0.48,0.99,0.70)]
build(7055, "A", "do the laundry", "male",
  [("to hold a basket", "the man", "male", man),
   ("to look at a sock", "the man", "male", man),
   ("to sleep on a bench", "the woman on the bench", "female", wom)],
  2.7,
  [("a basket", 0.27, 0.45, "male"), ("a sheet", 0.79, 0.38, "male"),
   ("a box", 0.72, 0.94, "male")],
  "What is the man looking at?", "He is looking at a sock.", "male",
  "Man boxes cut a little where his right arm is near the sleeping woman. Two women in the back hold the sheet together, so no phrase for them. Nouns: no a sock (socks also lie on the floor), no a washing machine (many machines).")
