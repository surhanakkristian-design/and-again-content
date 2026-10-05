from w_7060_7061_7062_7063_lib import write
splits = [0.73, 0.74, 0.74, 0.75, 0.76, 0.75, 0.76, 0.77]
man = [(s, 0.35, 0.92, 0.87) for s in splits]
woman = [(0.61, 0.35, s, 0.76) for s in splits]
mover = [(0, 0.34, 0.24, 0.86)] * 6 + [(0, 0.34, 0.27, 0.86), (0, 0.34, 0.24, 0.86)]
write(7060, "B", "donor", "male", [
  ("to hand over a key", "the young man", "male", man),
  ("to accept a key", "the red-haired woman", "female", woman),
  ("to remove a padded blanket", "the mover", "male", mover)],
  2.2, [("a van", 0.12, 0.27, "male"), ("a grand piano", 0.45, 0.56, "male"), ("a ramp", 0.38, 0.74, "male"), ("lifting straps", 0.33, 0.87, "male")],
  "What is the red-haired woman doing?", "She is accepting a key from him.", "female",
  "Man and woman stand overlapping (his arm crosses her at 0.2-0.7): boxes split at his left shoulder. Key handover visible 0.2-1.2; afterwards she holds her hand to her chest. Mover pulls the blanket up only at 3.2-3.7. Answer 'from him' refers to the young man (question names only the woman).")
