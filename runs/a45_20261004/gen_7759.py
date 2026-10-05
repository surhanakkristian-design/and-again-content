from gen_7758_7759_7760_7762_lib import write
couple = [(0.46,0.07,0.47,0.27)]*8
woman = [(0.21,0.41,0.60,0.51),(0.27,0.40,0.52,0.52),(0.38,0.39,0.27,0.58),(0.22,0.41,0.55,0.54),
         (0.42,0.42,0.24,0.50),(0.26,0.41,0.55,0.50),(0.23,0.40,0.58,0.53),(0.21,0.40,0.60,0.52)]
write(7759, "B", "barrels", "female",
 [("to tip barrels over the railing", "the couple on the balcony", "female", couple),
  ("to get drenched by water", "the woman in the street", "female", woman),
  ("to spread her arms wide", "the woman in the street", "female", woman)],
 3.2,
 [("the sky", 0.25, 0.12, "female"), ("barrels", 0.56, 0.30, "female"),
  ("paper lanterns", 0.22, 0.42, "female"), ("cobblestones", 0.22, 0.88, "female")],
 "What are the people above doing?", "They are tipping barrels over the railing.", "female",
 "couple on balcony treated as one target (both tip the barrels); woman in street used for two phrases; at 1.2/2.2 she has her back/side to camera")
