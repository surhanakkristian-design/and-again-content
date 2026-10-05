from gen_7963_7964_7965_7967_lib import build
man = [(0.10,0.35,0.45,0.83),(0.10,0.35,0.45,0.83),(0.10,0.34,0.45,0.83),(0.10,0.33,0.50,0.84),
       (0.08,0.32,0.50,0.84),(0.08,0.32,0.50,0.85),(0.06,0.31,0.50,0.86),(0.03,0.30,0.50,0.86)]
wom = [(0.45,0.38,0.92,0.80),(0.45,0.38,0.92,0.80),(0.45,0.37,0.93,0.80),(0.50,0.36,0.94,0.82),
       (0.50,0.35,0.94,0.82),(0.50,0.35,0.97,0.83),(0.50,0.35,0.99,0.84),(0.50,0.34,1.0,0.84)]
build(7967, "A", "run out of battery", "female",
  [("to shake a white torch", "the woman", "female", wom),
   ("to lean against the wall", "the man", "male", man),
   ("to wear a blue jacket", "the woman", "female", wom)],
  2.2,
  [("a wall", 0.15, 0.20, "female"), ("a rope", 0.42, 0.86, "female"),
   ("a bag", 0.88, 0.79, "female"), ("a rock", 0.72, 0.94, "female")],
  "What is the woman holding?", "She is holding a white torch.", "female",
  "Only two people; man/woman boxes split at x 0.45-0.50 where her torch hand reaches towards him (her torch tip at 0.2-1.2 s falls in the man box). Shake is short (~1.7 s). No 'torch' noun because both hold one. Phrase 3 is a state (no other action fits only one person).")
