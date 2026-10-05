from gen_5702_5703_5704_5705_lib import write
W = [(0.2,0.03,0.24,0.55,0.76),(0.7,0.01,0.23,0.58,0.77),(1.2,0.0,0.24,0.58,0.76),(1.7,0.08,0.35,0.47,0.65),
     (2.2,0.17,0.36,0.46,0.64),(2.7,0.16,0.36,0.49,0.64),(3.2,0.21,0.37,0.38,0.63),(3.7,0.18,0.37,0.39,0.63)]
C = [(0.2,0.77,0.44,0.20,0.14),(0.7,0.78,0.44,0.20,0.14),(1.2,0.79,0.44,0.20,0.14),(1.7,0.79,0.44,0.20,0.14),
     (2.2,0.76,0.43,0.20,0.14),(2.7,0.71,0.43,0.19,0.15),(3.2,0.68,0.44,0.19,0.15),(3.7,0.67,0.44,0.19,0.15)]
write(5705, "A", "car park", "female",
  [("to hold up her car key", "the woman", "female", W),
   ("to walk between the cars", "the woman", "female", W),
   ("to sit on a car", "the cat", "female", C)],
  3.7,
  [("a light", 0.49, 0.24, "female"), ("a pillar", 0.86, 0.34, "female"), ("a cat", 0.78, 0.50, "female"), ("a woman", 0.38, 0.62, "female")],
  "What is the woman doing?", "She is walking between the cars.", "female",
  "Key word 'car park' is the whole scene, so it is not placed as a noun. Car with headlights at the far end not used as a target (too close to the woman's head in the later frames). Question covers the second half (walking); first half she holds the key up.")
