from gen_6993_6994_6995_6996_lib import build
T = [0.2, 0.7, 1.2]
man = [(0.46,0.18,0.34,0.47),(0.52,0.18,0.28,0.47),(0.54,0.18,0.26,0.54)]
cheer = [(0.19,0.30,0.22,0.38),(0.20,0.29,0.21,0.39),(0.19,0.36,0.25,0.32)]
sari = [(0.82,0.28,0.18,0.36),(0.81,0.27,0.19,0.36),(0.82,0.27,0.18,0.37)]
build(6994, "B", "cotton", "male", T,
  [("to toss a roll of cotton", "the young man in white", "male", man),
   ("to cheer with raised arms", "the cheering woman", "female", cheer),
   ("to watch from a doorway", "the woman in the sari", "female", sari)],
  1.2,
  [("cotton", 0.58, 0.79, "male"), ("a staircase", 0.17, 0.91, "male"),
   ("a sari", 0.90, 0.46, "male"), ("a stone wall", 0.13, 0.14, "male")],
  "What is the young man doing?", "He is tossing a roll of cotton.", "male",
  "Short clip (3 frames). 'cotton' pill sits on the billowing fabric; the stacked rolls along the walls are cotton too. The cheering woman stands next to two men who do not raise their arms.")
