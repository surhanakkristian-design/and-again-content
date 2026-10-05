from gen_7741_7742_7743_7746_lib import write
W = [(0.0,0.34,0.45,0.66),(0.0,0.33,0.44,0.67),(0.0,0.31,0.46,0.69),(0.0,0.30,0.45,0.70),
     (0.0,0.30,0.47,0.70),(0.0,0.29,0.46,0.71),(0.0,0.26,0.44,0.74),(0.0,0.26,0.45,0.74)]
M = [(0.45,0.33,0.45,0.67),(0.44,0.32,0.50,0.68),(0.46,0.31,0.47,0.69),(0.45,0.29,0.50,0.71),
     (0.47,0.28,0.48,0.72),(0.46,0.27,0.50,0.73),(0.44,0.26,0.52,0.74),(0.45,0.25,0.53,0.75)]
L = [(0.22,0.02,0.34,0.24),(0.22,0.0,0.34,0.24),(0.21,0.0,0.34,0.22),(0.21,0.0,0.35,0.21),
     (0.20,0.0,0.36,0.20),(0.20,0.0,0.36,0.18),(0.19,0.0,0.37,0.18),(0.20,0.0,0.36,0.17)]
write(7746, "A", "anniversary", "female",
  [("to wear a white dress", "the woman", "female", W),
   ("to wear a light jacket", "the man", "male", M),
   ("to hang on the wall", "the lamp", "female", L)],
  2.2,
  [("a lamp", 0.38, 0.06, "female"), ("a window", 0.86, 0.25, "female"),
   ("roses", 0.91, 0.49, "female"), ("a cake", 0.62, 0.74, "female")],
  "What are they cutting?", "They are cutting a white cake.", "female",
  "Woman and man do the same actions (laugh, cut the cake together), so their phrases are states (dress / jacket). Their boxes are split between their touching heads; their shared hands on the knife are split too. Third target is the wall lamp.")
