from w_7245_7246_7247_7248_lib import write
woman = [(0.25,0.40,0.76,0.92),(0.24,0.40,0.78,0.93),(0.27,0.39,0.80,0.96),(0.32,0.42,0.95,0.98),
         (0.30,0.37,0.99,1.00),(0.30,0.34,1.00,1.00),(0.28,0.32,0.95,1.00),(0.09,0.32,0.97,1.00)]
kids =  [(0.77,0.26,1.00,0.62),(0.79,0.24,1.00,0.60),(0.81,0.30,1.00,0.62),(0.66,0.27,1.00,0.42),
         (0.68,0.21,1.00,0.37),(0.70,0.19,1.00,0.34),(0.64,0.17,1.00,0.32),(0.62,0.17,1.00,0.32)]
mach =  [(0.00,0.04,0.24,0.94),(0.00,0.00,0.23,0.94),(0.00,0.00,0.26,0.97),(0.00,0.00,0.26,0.96),
         (0.00,0.00,0.25,0.97),(0.00,0.00,0.24,0.97),(0.00,0.00,0.22,0.97),(0.00,0.00,0.08,0.97)]
write(7246, "B", "innovation", "female",
  [("to kneel in the sand", "the woman", "female", woman),
   ("to hold up metal cups", "the children", "female", kids),
   ("to pour out clean water", "the machine", "female", mach)],
  0.2,
  [("solar panels", 0.12, 0.28, "female"), ("a workbench", 0.36, 0.50, "female"),
   ("a clay pot", 0.36, 0.82, "female"), ("a crowd", 0.84, 0.36, "female")],
  "What is the woman catching?", ["She", "is", "catching", "clean", "water", "in", "her", "hands."], "female",
  "Children box: right column in early frames, then the band above the woman's head (she fills the right side later). At 3.7 the woman's hand reaches the tap, machine box shrunk to the panel edge. Key word innovation is abstract, not a noun slot.")
