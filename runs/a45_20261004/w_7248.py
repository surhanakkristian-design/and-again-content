from w_7245_7246_7247_7248_lib import write
man = [(0.02,0.31,0.43,0.89),(0.02,0.31,0.44,0.89),(0.02,0.31,0.48,0.89),(0.05,0.29,0.48,0.90),
       (0.03,0.29,0.51,0.91),(0.03,0.28,0.46,0.92),(0.01,0.27,0.43,0.92),(0.02,0.26,0.43,0.92)]
off = [(0.67,0.43,0.89,0.78),(0.65,0.43,0.86,0.79),(0.59,0.41,0.83,0.80),(0.58,0.40,0.83,0.82),
       (0.53,0.40,0.79,0.85),(0.47,0.37,0.74,0.87),(0.43,0.36,0.74,0.88),(0.43,0.35,0.74,0.88)]
brg = [(0.02,0.03,0.42,0.18),(0.02,0.03,0.40,0.17),(0.01,0.03,0.40,0.17),(0.02,0.03,0.40,0.17),
       (0.01,0.02,0.41,0.16),(0.01,0.02,0.39,0.16),(0.00,0.02,0.40,0.16),(0.01,0.01,0.40,0.15)]
write(7248, "B", "inspector", "male",
  [("to point straight ahead", "the man in the coat", "male", man),
   ("to carry an evidence bag", "the young officer", "male", off),
   ("to watch from the bridge", "the people on the bridge", "male", brg)],
  0.2,
  [("an inspector", 0.18, 0.45, "male"), ("a bridge", 0.55, 0.20, "male"),
   ("a car", 0.60, 0.47, "male"), ("police tape", 0.42, 0.57, "male")],
  "What is the young officer carrying?", ["He", "is", "carrying", "an", "evidence", "bag."], "male",
  "Man points only 0.2-2.2 s, then takes the bag. At 2.7-3.7 the bag is passed between the two, boxes split at the line between them. People on the bridge are a man and a woman, so default voice.")
