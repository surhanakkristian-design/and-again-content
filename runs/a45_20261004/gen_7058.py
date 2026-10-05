from lib_7055_7056_7057_7058 import build
doe = [(0.10,0.40,0.60,0.84),(0.10,0.40,0.60,0.84),(0.08,0.40,0.59,0.85),(0.05,0.40,0.59,0.87),
       (0.0,0.40,0.62,0.91),(0.0,0.40,0.61,0.94),(0.0,0.40,0.60,0.98),(0.0,0.40,0.62,1.0)]
bak = [(0.60,0.20,0.92,0.80),(0.60,0.20,0.92,0.80),(0.59,0.20,0.95,0.80),(0.59,0.20,0.97,0.83),
       (0.62,0.19,0.95,0.86),(0.61,0.19,0.95,0.88),(0.60,0.17,1.0,0.92),(0.62,0.16,1.0,0.95)]
cyc = [(0.0,0.24,0.21,0.40),(0.0,0.24,0.21,0.40),(0.0,0.25,0.22,0.39),(0.0,0.25,0.24,0.39),
       (0.02,0.22,0.25,0.39),(0.05,0.22,0.26,0.39),(0.06,0.22,0.27,0.39),(0.04,0.22,0.25,0.39)]
build(7058, "B", "doe", "female",
  [("to snatch a croissant", "the doe", "female", doe),
   ("to hold a baking tray", "the baker", "female", bak),
   ("to snap a photo", "the cyclist", "male", cyc)],
  2.7,
  [("a doe", 0.28, 0.55, "female"), ("an oven glove", 0.70, 0.44, "female"),
   ("an apron", 0.70, 0.60, "female"), ("a paper bag", 0.13, 0.92, "female")],
  "What is the doe doing?", "It is snatching a croissant from the tray.", "female",
  "Doe head reaches into the baker's area: split at x ~0.60, so the doe's muzzle and the baker's left side are cut. Doe box starts at y 0.40 (ears cut) to stay clear of the cyclist box at the window. Cyclist only takes the photo from about 2.7 s; before that he rides/looks in. An older woman peeks from the back, tiny, not used.")
