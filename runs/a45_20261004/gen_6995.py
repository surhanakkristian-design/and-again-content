from gen_6993_6994_6995_6996_lib import build
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
woman = [(0.19,0.44,0.25,0.36),(0.19,0.44,0.25,0.36),(0.17,0.45,0.25,0.37),(0.15,0.45,0.27,0.38),
         (0.12,0.53,0.26,0.34),(0.05,0.59,0.23,0.33),(0.0,0.57,0.23,0.40),(0.0,0.59,0.18,0.41)]
man = [(0.51,0.63,0.18,0.15),(0.50,0.63,0.20,0.16),(0.50,0.64,0.20,0.17),(0.50,0.65,0.20,0.18),
       (0.48,0.68,0.20,0.16),(0.47,0.71,0.21,0.17),(0.44,0.74,0.20,0.22),(0.40,0.76,0.22,0.22)]
car = [(0.86,0.48,0.14,0.14),(0.83,0.48,0.17,0.14),(0.82,0.49,0.18,0.14),(0.79,0.49,0.21,0.16),
       (0.77,0.49,0.23,0.17),(0.75,0.50,0.25,0.18),(0.73,0.50,0.27,0.19),(0.73,0.50,0.27,0.18)]
build(6995, "B", "course", "female", T,
  [("to raise both arms overhead", "the woman", "female", woman),
   ("to point at the tornado", "the young man", "male", man),
   ("to kick up dust", "the dark car", "female", car)],
  1.7,
  [("a tornado", 0.50, 0.34, "female"), ("wheat", 0.74, 0.45, "female"),
   ("a dirt road", 0.78, 0.80, "female"), ("a pickup truck", 0.30, 0.92, "female")],
  "Where is the woman standing?", "She is standing on a pickup truck.", "female",
  "Woman raises both arms 0.2-1.7, then turns towards the car (2.2+) and drifts out at the left edge (3.7 partly visible). The young man points at the tornado; he sits on the cab. Key word 'course' is not a visible noun. The flattened track in the wheat is also a path, the 'a dirt road' pill sits on the wide road at the bottom right.")
