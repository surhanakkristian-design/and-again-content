from gen_7935_7936_7937_7938_lib import write
W = [(0.44,0.20,0.44,0.72),(0.42,0.20,0.46,0.72),(0.41,0.20,0.47,0.72),(0.41,0.20,0.47,0.72),
     (0.41,0.20,0.47,0.72),(0.41,0.20,0.47,0.72),(0.41,0.22,0.47,0.70),(0.41,0.21,0.46,0.71)]
M = [(0.00,0.47,0.42,0.47),(0.00,0.47,0.41,0.47),(0.00,0.48,0.40,0.46),(0.00,0.48,0.40,0.46),
     (0.00,0.47,0.40,0.47),(0.00,0.47,0.40,0.47),(0.00,0.47,0.40,0.47),(0.00,0.47,0.40,0.47)]
write(7937, "B", "physics", "female", [
  ("to touch the metal dome", "the woman", "female", W),
  ("to crank a brass handle", "the man", "male", M),
  ("to gasp in surprise", "the woman", "female", W)],
  2.2, [("a steel beam", 0.50, 0.10, "female"), ("a brick wall", 0.12, 0.30, "female"),
        ("a metal dome", 0.45, 0.62, "female"), ("white trainers", 0.70, 0.89, "female")],
  "What is the woman touching?", "She is touching a metal dome.", "female",
  "Key word 'physics' is abstract, not placed. Woman's and man's boxes are split at x 0.40/0.41: her hand on the dome and his hands on the handle are close. The woman's spread hair (x 0.3-0.95 at the top) is only partly inside her box. 'to gasp in surprise': her mouth is wide open at 1.2-3.2 while she touches her hair; the man only smiles.")
