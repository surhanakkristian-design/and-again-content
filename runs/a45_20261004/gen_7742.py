from gen_7741_7742_7743_7746_lib import write
C = [(0.06,0.12,0.56,0.49),(0.18,0.16,0.44,0.46),(0.44,0.16,0.18,0.55),(0.42,0.17,0.58,0.45),
     (0.43,0.18,0.57,0.44),(0.37,0.19,0.25,0.55),(0.37,0.19,0.22,0.56),(0.40,0.19,0.27,0.56)]
N = [(0.63,0.54,0.25,0.34),(0.63,0.56,0.23,0.33),(0.63,0.57,0.25,0.33),(0.62,0.62,0.25,0.29),
     (0.60,0.62,0.28,0.30),(0.63,0.57,0.22,0.35),(0.61,0.58,0.25,0.36),(0.68,0.58,0.19,0.36)]
V = [(0.20,0.61,0.30,0.27),(0.20,0.62,0.30,0.28),(0.18,0.62,0.26,0.30),(0.18,0.63,0.27,0.29),
     (0.16,0.53,0.26,0.40),(0.17,0.53,0.20,0.41),(0.17,0.58,0.20,0.36),(0.16,0.57,0.23,0.37)]
write(7742, "B", "aim", "female",
  [("to dangle from a yellow hold", "the climber", "female", C),
   ("to clutch his head in disbelief", "the man in the navy T-shirt", "male", N),
   ("to crouch on the blue mat", "the man in the white vest", "male", V)],
  0.2,
  [("a skylight", 0.30, 0.08, "female"), ("a braid", 0.38, 0.33, "female"),
   ("a climbing wall", 0.80, 0.30, "female"), ("a crash mat", 0.55, 0.93, "female")],
  "What is the climber doing?", "She is dangling from a yellow hold.", "female",
  "The climber's legs swing in front of both men from 1.2 on: boxes split (her lower legs/feet cut at 1.7, 2.2, 2.7, 3.2; navy man's head partly cut at 1.7/2.2). White-vest man crouches 0.2-1.7, then stands and cheers. Navy man has hands on his head 0.2-3.2.")
