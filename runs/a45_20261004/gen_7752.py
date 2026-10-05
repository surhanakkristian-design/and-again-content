from gen_7747_7749_7750_7752_lib import write
W = [(0.37,0.37,0.78,0.77),(0.33,0.31,0.81,0.77),(0.24,0.29,0.78,0.79),(0.38,0.28,0.77,0.80),
     (0.37,0.28,0.78,0.81),(0.33,0.27,0.92,0.87),(0.36,0.31,0.89,0.89),(0.36,0.29,0.91,0.89)]
P = [(0.08,0.41,0.27,0.61),(0.08,0.41,0.28,0.62),(0.06,0.41,0.24,0.62),(0.12,0.40,0.32,0.64),
     (0.15,0.39,0.34,0.64),(0.15,0.40,0.33,0.64),(0.18,0.39,0.36,0.67),(0.18,0.38,0.36,0.67)]
write(7752, "A", "at last", "female", [
  ("to jump into his arms", "the woman", "female", W),
  ("to push the trolleys", "the man with the trolleys", "male", P),
  ("to hold some flowers", "the woman", "female", W)],
  2.2, [("a tree", 0.86, 0.25, "female"), ("a suitcase", 0.18, 0.77, "female"), ("cups", 0.22, 0.90, "female"), ("a coat", 0.83, 0.89, "female")],
  "What is the woman doing?", "She is jumping into his arms.", "female",
  "The hugging man and woman overlap completely, so the man is not a target; the woman's box necessarily covers much of him (at 1.7 s she is almost hidden behind him). Porter ('the man with the trolleys') is close to the bouquet at 1.2 / 2.7-3.7 s: boxes split between them.")
