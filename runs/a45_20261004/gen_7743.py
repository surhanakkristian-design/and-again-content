from gen_7741_7742_7743_7746_lib import write
S = [(0.08,0.31,0.45,0.69),(0.12,0.34,0.41,0.64),(0.19,0.36,0.34,0.58),(0.27,0.36,0.29,0.55),
     (0.29,0.40,0.30,0.44),(0.32,0.40,0.29,0.38),(0.37,0.39,0.22,0.37),(0.35,0.40,0.21,0.34)]
K = [(0.53,0.34,0.36,0.66),(0.54,0.36,0.31,0.62),(0.53,0.37,0.29,0.56),(0.56,0.37,0.27,0.52),
     (0.60,0.39,0.20,0.44),(0.61,0.39,0.19,0.40),(0.60,0.39,0.19,0.38),(0.57,0.40,0.18,0.35)]
M = [None,(0.00,0.33,0.12,0.65),(0.00,0.33,0.19,0.62),(0.00,0.35,0.26,0.56),
     (0.00,0.37,0.29,0.47),(0.06,0.37,0.26,0.44),(0.11,0.38,0.26,0.40),(0.10,0.38,0.25,0.38)]
write(7743, "B", "alike", "male",
  [("to carry a white surfboard", "the surfer", "male", S),
   ("to clutch her chef's hat", "the cook", "female", K),
   ("to fasten his cream jacket", "the man in the suit", "male", M)],
  3.7,
  [("a gull", 0.36, 0.24, "male"), ("a lamp post", 0.85, 0.21, "male"),
   ("a surfboard", 0.44, 0.57, "male"), ("fallen leaves", 0.55, 0.88, "male")],
  "What is the cook doing?", "She is clutching her chef's hat.", "female",
  "Suit man only a cut-off sliver at 0.2 (off) and half out of frame at 0.7; his box and the surfer's are split at the surfboard (board partly in front of him). He fastens / holds his jacket buttons from 1.2 on. Cook holds her hat 0.2-2.7, laughs at 3.2-3.7. Woman in lilac not a target.")
