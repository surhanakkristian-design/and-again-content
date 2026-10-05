from gen_6971_6972_6973_6975_lib import write
P = [(0.17,0.49,0.35,0.42),(0.17,0.49,0.35,0.43),(0.16,0.45,0.36,0.48),(0.17,0.43,0.40,0.53),
     (0.16,0.42,0.47,0.58),(0.16,0.40,0.50,0.60),(0.12,0.36,0.58,0.64),(0.12,0.36,0.60,0.64)]
G = [(0.30,0.36,0.28,0.13),(0.27,0.35,0.24,0.14),(0.18,0.29,0.28,0.16),(0.15,0.27,0.24,0.16),
     (0.08,0.23,0.28,0.19),(0.08,0.19,0.30,0.21),(0.06,0.17,0.29,0.19),(0.06,0.18,0.31,0.18)]
write(6975, "B", "company", "male",
  [("to fry eggs on a stove", "the man in pyjamas", "male", P),
   ("to stare blankly ahead", "the man in pyjamas", "male", P),
   ("to carry an acoustic guitar", "the man with the guitar", "male", G)],
  3.2,
  [("a lemon tree", 0.42, 0.14, "male"), ("a dog", 0.18, 0.43, "male"),
   ("sunflowers", 0.58, 0.53, "male"), ("a frying pan", 0.62, 0.66, "male")],
  "What is the man in pyjamas doing?", "He is frying eggs on a camping stove.", "male",
  "Guitar man and pyjama man overlap vertically at 0.2-0.7 (guitar man jumps just behind the pyjama man's head): split along y 0.49, guitar man's feet partly cut. From 1.2 split under the guitar man's feet. The sunflower woman was avoided as a target: continuity glitches (sunflowers pass between two women, cake appears). Two dogs at 3.7 (glitch), so the still is 3.2 with one dog.")
