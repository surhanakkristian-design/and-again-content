from w_7772_7774_7775_7776_lib import build
D = [(0.18,0.31,0.32,0.42),(0.16,0.29,0.37,0.44),(0.15,0.28,0.37,0.45),(0.13,0.26,0.40,0.48),
     (0.10,0.24,0.42,0.52),(0.04,0.22,0.50,0.55),(0.03,0.24,0.48,0.56),(0.01,0.22,0.50,0.57)]
W = [(0.51,0.25,0.49,0.70),(0.54,0.23,0.46,0.72),(0.53,0.22,0.47,0.73),(0.54,0.18,0.46,0.77),
     (0.53,0.17,0.47,0.80),(0.55,0.17,0.45,0.82),(0.52,0.18,0.48,0.82),(0.52,0.17,0.48,0.83)]
build(7775, "A", "chemical", "female",
  [("to pour from a jug", "the dog", "female", D),
   ("to laugh out loud", "the woman", "female", W),
   ("to stand next to the dog", "the woman", "female", W)],
  0.2,
  [("a lamp", 0.47, 0.08, "female"), ("a window", 0.12, 0.25, "female"),
   ("a dog", 0.42, 0.37, "female"), ("a table", 0.60, 0.82, "female")],
  "What is the dog doing?", "It is pouring from a jug.", "female",
  "Flask (turns purple) not used as a target: it sits between dog and woman and a min-size box would overlap both. Woman used twice. Woman's hand/forearm on the flask falls inside the dog's box; dog's ear tip cut at the woman's box edge. Dog pours only until about 1.7 s, then holds the jug.")
