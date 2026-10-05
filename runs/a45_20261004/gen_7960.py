from gen_7957_7958_7960_7961_lib import write
L = [(0.0,0.30,0.19,0.45),(0.0,0.28,0.18,0.45),(0.0,0.25,0.16,0.50),(0.0,0.28,0.16,0.48),
     (0.0,0.22,0.15,0.50),(0.0,0.20,0.14,0.50),(0.0,0.30,0.16,0.45),None]
M = [(0.19,0.16,0.35,0.80),(0.18,0.10,0.36,0.86),(0.16,0.08,0.39,0.88),(0.16,0.04,0.39,0.92),
     (0.15,0.10,0.42,0.86),(0.14,0.18,0.45,0.80),(0.16,0.17,0.43,0.83),(0.12,0.14,0.47,0.86)]
C = [(0.54,0.37,0.18,0.36),(0.54,0.35,0.18,0.38),(0.55,0.34,0.18,0.38),(0.55,0.33,0.18,0.40),
     (0.57,0.31,0.18,0.40),(0.59,0.29,0.18,0.40),(0.59,0.28,0.18,0.40),(0.59,0.27,0.18,0.40)]
write(7960, "B", "ratio", "male", [
  ("to wear a patterned shirt", "the man in the patterned shirt", "male", M),
  ("to tip a juice carton", "the man on the left", "male", L),
  ("to clap her hands excitedly", "the curly-haired woman", "female", C)],
  1.2, [("a jug", 0.46, 0.84, "male"), ("lemons", 0.69, 0.76, "male"),
        ("fairy lights", 0.65, 0.14, "male"), ("a bottle", 0.20, 0.12, "male")],
  "What is the curly-haired woman doing?", "She is clapping her hands with excitement.", "female",
  "main man gets a state phrase: the man on the left also has a hand on the raised water bottle, so 'pour water' is not unique to him; "
  "the man on the left is mostly cut off (face only at the left edge, later only arms), off at 3.7 s; boxes split along x to avoid overlap "
  "(his carton arm crosses in front of the main man); a second carton is held upright in the centre, so no 'carton' noun; key word ratio is abstract; question about the main man was not possible in 7 words without ambiguity (two men pour)")
