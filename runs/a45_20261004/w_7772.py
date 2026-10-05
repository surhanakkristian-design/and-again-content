from w_7772_7774_7775_7776_lib import build
W = [(0.23,0.24,0.35,0.60),(0.22,0.24,0.36,0.60),(0.21,0.23,0.39,0.62),(0.20,0.23,0.41,0.62),
     (0.17,0.20,0.45,0.67),(0.18,0.20,0.47,0.68),(0.22,0.19,0.51,0.73),(0.26,0.19,0.47,0.74)]
R = [(0.04,0.23,0.18,0.24),(0.03,0.22,0.18,0.24),(0.02,0.23,0.18,0.24),(0.00,0.22,0.19,0.25),
     (0.00,0.18,0.16,0.28),(0.00,0.15,0.17,0.31),(0.00,0.14,0.21,0.37),(0.00,0.13,0.25,0.41)]
M = [(0.59,0.23,0.41,0.67),(0.58,0.22,0.42,0.68),(0.61,0.22,0.39,0.68),(0.62,0.21,0.38,0.70),
     (0.63,0.18,0.37,0.75),(0.66,0.17,0.34,0.83),(0.74,0.18,0.26,0.82),(0.74,0.17,0.26,0.83)]
build(7772, "B", "cardiac", "female",
  [("to perform chest compressions", "the woman in yellow", "female", W),
   ("to jog across the wet sand", "the running woman", "female", R),
   ("to gesture with both hands", "the man", "male", M)],
  0.2,
  [("a lifeguard tower", 0.12, 0.19, "female"), ("waves", 0.62, 0.22, "female"),
   ("the sky", 0.55, 0.07, "female"), ("a training dummy", 0.42, 0.80, "female")],
  "What is the woman in yellow doing?", "She is performing chest compressions on a dummy.", "female",
  "Woman-in-yellow box starts right of the running woman (her jacket's left edge is cut off at 2.2-3.7 s to avoid overlap). Man's box starts at his lower hand; his far hand reaches near her hands.")
