from gen_7982_7983_7984_7985_lib import write
W = [(0.30,0.27,0.32,0.20),(0.22,0.25,0.50,0.41),(0.20,0.24,0.54,0.45),(0.13,0.23,0.60,0.47),
     (0.18,0.22,0.55,0.48),(0.18,0.21,0.57,0.49),(0.16,0.20,0.60,0.51),(0.17,0.20,0.60,0.51)]
M = [(0.0,0.47,0.62,0.53),(0.0,0.67,0.72,0.33),(0.0,0.70,0.75,0.30),(0.0,0.71,0.77,0.29),
     (0.10,0.76,0.67,0.24),(0.15,0.82,0.64,0.18),(0.20,0.84,0.60,0.16),(0.20,0.84,0.60,0.16)]
C = [(0.62,0.36,0.20,0.15),(0.72,0.32,0.18,0.18),(0.74,0.35,0.18,0.16),(0.73,0.35,0.19,0.16),
     (0.73,0.34,0.18,0.17),(0.75,0.33,0.18,0.18),(0.76,0.33,0.18,0.18),(0.77,0.33,0.18,0.18)]
write(7982, "B", "sharply", "female",
  [("to snatch the box away", "the woman", "female", W),
   ("to reach across the table", "the man", "male", M),
   ("to perch on the counter", "the cat", "female", C)],
  2.2,
  [("a pizza box", 0.47, 0.53, "female"), ("a cat", 0.81, 0.43, "female"),
   ("a napkin", 0.35, 0.73, "female"), ("a pendant lamp", 0.52, 0.06, "female")],
  "What is the woman holding?", "She is clutching the pizza box to her chest.", "female",
  "The man is only seen as green sleeves/hands at the bottom; at 0.2 his raised hands cover her torso, so her box is cut at y 0.47. Woman box cut on the right at 1.7-3.7 to stay clear of the cat (her arm/box edge). Key word 'sharply' (adverb) not a noun.")
