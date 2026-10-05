from gen_7747_7749_7750_7752_lib import write
# split x between woman (left) and man (right) per frame
W = [(0.15,0.44,0.53,0.82),(0.12,0.44,0.56,0.82),(0.11,0.44,0.56,0.82),(0.09,0.44,0.55,0.82),
     (0.05,0.42,0.53,0.80),(0.03,0.42,0.54,0.80),(0.01,0.42,0.52,0.80),(0.01,0.42,0.53,0.80)]
M = [(0.53,0.40,0.92,0.82),(0.56,0.40,0.94,0.82),(0.56,0.40,0.95,0.82),(0.55,0.40,0.96,0.82),
     (0.53,0.39,0.99,0.80),(0.54,0.39,0.99,0.80),(0.52,0.39,0.99,0.80),(0.53,0.39,0.99,0.80)]
write(7747, "A", "apart", "male", [
  ("to wear a brown jacket", "the woman", "female", W),
  ("to wear a dark blue jacket", "the man", "male", M),
  ("to wear white shoes", "the woman", "female", W)],
  2.2, [("the sky", 0.50, 0.22, "male"), ("houses", 0.13, 0.36, "male"), ("a boat", 0.55, 0.62, "male"), ("water", 0.55, 0.88, "male")],
  "Can their hands touch?", "No, they are too far apart.", "male",
  "Only two clear targets (woman, man); their reaching arms overlap in the middle, boxes split at the gap between the hands. No action fits only one person (both reach, laugh, hold the rail), so all three phrases are states. Answer subject 'they' (mixed) -> defaultVoice male.")
