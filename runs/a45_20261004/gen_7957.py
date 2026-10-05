from gen_7957_7958_7960_7961_lib import write
W = [(0.02,0.40,0.86,0.52),(0.0,0.45,0.88,0.40),(0.0,0.42,0.82,0.45),(0.0,0.42,0.83,0.45),
     (0.0,0.42,0.82,0.46),(0.0,0.34,0.82,0.54),(0.0,0.31,0.72,0.59),(0.0,0.27,0.70,0.64)]
M = [(0.61,0.11,0.20,0.20),(0.60,0.08,0.18,0.21),(0.60,0.07,0.19,0.20),(0.60,0.06,0.18,0.21),
     (0.60,0.05,0.19,0.21),(0.61,0.03,0.19,0.20),(0.62,0.03,0.18,0.20),(0.64,0.02,0.18,0.20)]
write(7957, "A", "quietly", "female", [
  ("to lift heavy books", "the woman", "female", W),
  ("to climb a ladder", "the man", "male", M),
  ("to kneel on the floor", "the woman", "female", W)],
  1.7, [("books", 0.66, 0.72, "female"), ("a ladder", 0.74, 0.25, "female"),
        ("a table", 0.40, 0.37, "female"), ("the floor", 0.55, 0.93, "female")],
  "What is the woman doing?", "She is lifting heavy books.", "female",
  "quietly is an adverb, not used as a noun; 'kneel' may be slightly above A; several students also sit at the table (not used as targets)")
