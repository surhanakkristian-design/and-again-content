from gen_7935_7936_7937_7938_lib import write
W = [(0.14,0.42,0.46,0.46),(0.17,0.42,0.43,0.46),(0.14,0.42,0.46,0.47),(0.16,0.42,0.44,0.47),
     (0.14,0.41,0.46,0.47),(0.13,0.42,0.47,0.47),(0.12,0.41,0.40,0.48),(0.12,0.41,0.36,0.48)]
M = [(0.62,0.22,0.38,0.64),(0.63,0.21,0.37,0.64),(0.63,0.20,0.37,0.66),(0.63,0.20,0.37,0.66),
     (0.63,0.20,0.37,0.65),(0.62,0.21,0.38,0.64),(0.53,0.20,0.47,0.66),(0.49,0.20,0.51,0.67)]
write(7938, "A", "please", "female", [
  ("to put her hands together", "the woman on the ground", "female", W),
  ("to hold out a plate", "the man", "male", M),
  ("to take a croissant", "the woman on the ground", "female", W)],
  2.2, [("the sky", 0.25, 0.06, "female"), ("trees", 0.14, 0.28, "female"),
        ("a croissant", 0.72, 0.46, "female"), ("a paper bag", 0.14, 0.75, "female")],
  "What is the man doing?", "He is giving her a croissant.", "male",
  "Key word 'please' is an adverb, not placed. The sweeping woman in the background is too small and sits between the two targets, so she is not a target; the kneeling woman is named 'the woman on the ground'. Her stretched leg reaches the man's feet, so her box stops at x 0.60 (foot outside); at 3.2/3.7 the boxes split at the handover (plate/croissant between their hands). She takes the croissant at 3.2-3.7.")
