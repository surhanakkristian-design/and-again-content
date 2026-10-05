from w_7060_7061_7062_7063_lib import write
man = [(0.38, 0.15, 1, 1), (0.37, 0.14, 1, 1), (0.33, 0.12, 1, 1), (0.32, 0.09, 1, 1),
       (0.30, 0.05, 1, 1), (0.27, 0.01, 1, 1), (0.27, 0.01, 1, 1), (0.40, 0, 1, 1)]
woman = [(0, 0.30, 0.23, 0.46), (0, 0.30, 0.23, 0.46), (0, 0.31, 0.23, 0.47), (0, 0.30, 0.26, 0.47),
         (0, 0.30, 0.27, 0.48), (0, 0.29, 0.27, 0.50), (0, 0.30, 0.27, 0.49), (0.02, 0.28, 0.40, 0.50)]
cat = [(0, 0.46, 0.27, 0.61), (0, 0.46, 0.28, 0.61), (0, 0.47, 0.23, 0.63), (0, 0.47, 0.23, 0.63),
       (0, 0.48, 0.23, 0.64), (0, 0.50, 0.23, 0.67), (0, 0.49, 0.26, 0.68), (0.04, 0.50, 0.37, 0.68)]
write(7063, "A", "down", "male", [
  ("to blow soft feathers", "the young man", "male", man),
  ("to wear glasses", "the old woman", "female", woman),
  ("to sit on a table", "the black cat", "male", cat)],
  2.2, [("a window", 0.13, 0.20, "male"), ("a cat", 0.10, 0.56, "male"), ("down", 0.12, 0.73, "male"), ("pillows", 0.55, 0.69, "male")],
  "What is the young man doing?", "He is blowing soft feathers.", "male",
  "The black cat sits in front of the old woman: their boxes are split horizontally (woman = head/shoulders above, cat below). The man's open hand crosses in front of the woman at 3.2-3.7, so his box starts right of her (hand partly cut, at 3.7 only from x 0.40). Woman: 'to wear glasses' is a state; both she and the man laugh, so laughing is not unique. Noun 'down' (key word, mass noun) sits on the fluff in the front sack; other sacks also hold down. Cat reaches up with a paw only at 0.2-0.7.")
