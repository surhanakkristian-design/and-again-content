from gen_7957_7958_7960_7961_lib import write
B = [(0.53,0.26,0.31,0.28),(0.58,0.26,0.21,0.28),(0.58,0.24,0.22,0.33),(0.60,0.24,0.31,0.30),
     (0.61,0.23,0.34,0.26),(0.61,0.22,0.30,0.25),(0.62,0.21,0.31,0.36),(0.70,0.20,0.28,0.40)]
D = [(0.68,0.55,0.32,0.20),(0.82,0.54,0.18,0.26),(0.58,0.66,0.42,0.29),(0.48,0.55,0.52,0.33),
     (0.48,0.50,0.52,0.46),(0.51,0.48,0.49,0.48),(0.57,0.58,0.43,0.42),(0.60,0.62,0.40,0.38)]
M = [(0.05,0.26,0.29,0.30),(0.08,0.26,0.28,0.30),(0.10,0.25,0.28,0.33),(0.11,0.25,0.28,0.32),
     (0.12,0.24,0.28,0.28),(0.15,0.22,0.29,0.24),(0.20,0.21,0.29,0.26),(0.22,0.21,0.29,0.24)]
write(7961, "B", "recovery", "female", [
  ("to pull back a curtain", "the blonde woman", "female", B),
  ("to sniff her face", "the beagle", "female", D),
  ("to clear a bedside table", "the man", "male", M)],
  3.2, [("a beagle", 0.85, 0.82, "female"), ("a mug", 0.80, 0.50, "female"),
        ("tulips", 0.10, 0.43, "female"), ("an arch", 0.33, 0.14, "female")],
  "What is the beagle doing?", "It is sniffing the woman's face.", "female",
  "selfie woman not used as a tap target (her box would cover most of the frame); blonde pulls the curtain only at 0.2-0.7 s, later stands; "
  "man is partly behind the selfie woman's head from 2.2 s; 'her face' in the dog phrase = the selfie woman; key word recovery is abstract")
