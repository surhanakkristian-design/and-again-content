from gen_7963_7964_7965_7967_lib import build
# boxes as (x0,y0,x1,y1)
dog = [(0.11,0.30,0.42,0.75),(0.11,0.30,0.42,0.75),(0.10,0.30,0.42,0.78),(0.10,0.30,0.41,0.78),
       (0.13,0.27,0.40,0.78),(0.08,0.26,0.38,0.77),(0.04,0.26,0.37,0.81),(0.02,0.26,0.36,0.82)]
wom = [(0.42,0.18,0.76,0.93),(0.42,0.18,0.78,0.93),(0.42,0.18,0.77,0.96),(0.42,0.16,0.80,0.97),
       (0.40,0.13,0.79,1.0),(0.39,0.12,0.82,1.0),(0.38,0.12,0.84,1.0),(0.37,0.12,0.86,1.0)]
man = [(0.80,0.26,1.0,0.76),(0.80,0.26,1.0,0.76),(0.80,0.26,1.0,0.76),(0.81,0.26,1.0,0.76),
       (0.83,0.26,1.0,0.78),(0.84,0.26,1.0,0.78),(0.86,0.30,1.0,0.78),(0.87,0.30,1.0,0.78)]
build(7963, "B", "resemble", "female",
  [("to balance on a bench", "the poodle", "female", dog),
   ("to jog along the path", "the curly-haired woman", "female", wom),
   ("to cover his face", "the man", "male", man)],
  1.2,
  [("a lamp post", 0.20, 0.13, "female"), ("a poodle", 0.27, 0.47, "female"),
   ("leggings", 0.58, 0.68, "female"), ("a bench", 0.14, 0.88, "female")],
  "What is the poodle doing?", "The poodle is balancing on a bench.", "female",
  "Man covers his face with his hand only from ~2.7 s (laughing); before that he points. Woman in green jacket not used (also laughs/points). Man box narrow (0.13-0.14 wide) at 3.2-3.7 because the woman's hair reaches x 0.84.")
