from gen_7221_7222_7223_7224_lib import write
man = [(0.08,0.36,0.89,0.24),(0.07,0.36,0.90,0.28),(0.07,0.36,0.92,0.30),(0.12,0.36,0.64,0.42),
       (0.10,0.36,0.68,0.43),(0.02,0.36,0.75,0.48),(0.00,0.37,0.78,0.53),(0.00,0.40,0.79,0.60)]
woman = [(0.29,0.22,0.18,0.14),(0.29,0.22,0.18,0.14),(0.29,0.21,0.18,0.15),(0.30,0.22,0.18,0.14),
         (0.27,0.22,0.18,0.14),(0.27,0.22,0.18,0.14),(0.24,0.23,0.18,0.14),(0.23,0.25,0.18,0.15)]
umb = [(0.68,0.22,0.18,0.14),(0.72,0.22,0.18,0.14),(0.74,0.21,0.18,0.15),(0.76,0.28,0.18,0.16),
       (0.78,0.29,0.18,0.15),(0.77,0.31,0.21,0.16),(0.78,0.33,0.21,0.14),(0.79,0.32,0.20,0.15)]
write(7221, "B", "hold on", "male",
  [("to lean into the wind", "the man", "male", man),
   ("to cling to a lamppost", "the woman", "female", woman),
   ("to be blown inside out", "the umbrella", "male", umb)],
  3.2,
  [("a lamppost", 0.30, 0.15, "male"), ("a pier", 0.78, 0.27, "male"),
   ("an umbrella", 0.88, 0.40, "male"), ("a raincoat", 0.40, 0.66, "male")],
  "What is the woman doing?", "She is holding on to a lamppost.", "female",
  "Man's legs cross the background people at 0.2-1.2: his box starts at y 0.36 (raised feet cut) and the woman/umbrella boxes stop there; from 1.7 his box stops at the umbrella's left edge, so his feet on the right are cut. Woman box only covers her upper body (her legs are behind/below the man's head line). Umbrella phrase is a passive state but nothing else is inside out.")
