from gen_7741_7742_7743_7746_lib import write
W = [(0.31,0.30,0.27,0.60),(0.08,0.31,0.40,0.64),(0.11,0.31,0.37,0.67),(0.10,0.31,0.34,0.66),
     (0.08,0.30,0.39,0.68),(0.08,0.31,0.46,0.67),(0.04,0.29,0.46,0.71),(0.02,0.29,0.50,0.71)]
D = [None,(0.49,0.57,0.20,0.19),(0.48,0.56,0.23,0.39),(0.45,0.63,0.30,0.37),None,None,None,None]
M = [None,(0.73,0.36,0.19,0.38),(0.73,0.36,0.19,0.40),(0.76,0.35,0.17,0.41),
     (0.74,0.34,0.20,0.44),(0.74,0.34,0.20,0.44),(0.73,0.34,0.22,0.45),(0.73,0.34,0.23,0.45)]
write(7741, "B", "ahead of time", "female",
  [("to jump back in surprise", "the woman in the bathrobe", "female", W),
   ("to rush into the hallway", "the dog", "female", D),
   ("to carry a wrapped present", "the man in the orange jacket", "male", M)],
  2.2,
  [("a lantern", 0.53, 0.09, "female"), ("sunflowers", 0.56, 0.47, "female"),
   ("a bathrobe", 0.30, 0.62, "female"), ("tiles", 0.62, 0.90, "female")],
  "What is the woman in lilac doing?", "She is jumping back in surprise.", "female",
  "Dog only 0.7-1.7; its box is split from the woman's (her raised hand / snout cut a little at 0.7-1.7) and from the present man's at 1.7. Guests off at 0.2 (door closed). Woman with sunflowers not a target.")
