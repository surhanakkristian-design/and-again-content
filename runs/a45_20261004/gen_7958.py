from gen_7957_7958_7960_7961_lib import write
W = [(0.14,0.29,0.65,0.61),(0.23,0.28,0.58,0.64),(0.34,0.29,0.48,0.70),(0.30,0.28,0.51,0.72),
     (0.26,0.26,0.54,0.74),(0.22,0.25,0.59,0.75),(0.13,0.25,0.73,0.75),(0.22,0.25,0.67,0.75)]
M = [(0.79,0.37,0.19,0.16),(0.81,0.37,0.18,0.16),(0.82,0.38,0.16,0.16),(0.81,0.38,0.18,0.15),
     (0.80,0.38,0.18,0.14),(0.81,0.37,0.18,0.14),None,None]
write(7958, "A", "quit", "female", [
  ("to carry a box", "the woman", "female", W),
  ("to open a glass door", "the woman", "female", W),
  ("to stand behind a desk", "the man", "male", M)],
  2.2, [("a box", 0.62, 0.56, "female"), ("a lamp", 0.70, 0.43, "female"),
        ("a bin", 0.15, 0.68, "female"), ("a desk", 0.88, 0.66, "female")],
  "What is the woman carrying?", "She is carrying a box.", "female",
  "man is hidden behind her lamp from 3.2 s (off); man boxes trimmed at the left to avoid the woman's box; key word quit not used in texts")
