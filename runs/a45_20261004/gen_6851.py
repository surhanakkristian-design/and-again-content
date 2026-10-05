from gen_6851_6852_6853_6854_lib import write
man = [(0,0.19,0.5,0.81),(0,0.16,0.52,0.84),(0,0.09,0.5,0.91),(0,0,0.45,0.72),(0,0.28,0.42,0.34),(0,0.22,0.55,0.51),(0,0.32,0.26,0.18),(0,0.52,0.2,0.16)]
lap = [(0.5,0.37,0.43,0.27),(0.52,0.35,0.45,0.28),(0.5,0.3,0.48,0.3),(0.45,0.26,0.54,0.32),(0.42,0.23,0.57,0.28),(0.55,0.19,0.45,0.32),(0.45,0.2,0.55,0.34),(0.52,0.27,0.48,0.3)]
write(6851, "B", "back up your files", "male",
 [("to label a hard drive", "the man", "male", man),
  ("to lean over the desk", "the man", "male", man),
  ("to display a progress bar", "the laptop", "male", lap)],
 2.2,
 [("a metal case", 0.22, 0.24, "male"), ("a mug", 0.75, 0.2, "male"), ("a laptop", 0.78, 0.36, "male"), ("a wooden desk", 0.5, 0.8, "male")],
 "What is the man doing?", "He is labelling a hard drive.", "male",
 "Camera moves; from 2.2 only the man's arm/hands are visible (3.7 only a blurred hand, weak). Two orange drives, so 'a hard drive' not used as noun. Man and laptop boxes split vertically where hands near keyboard.")
