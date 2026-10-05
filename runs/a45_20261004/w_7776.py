from w_7772_7774_7775_7776_lib import build
W = [(0.41,0.32,0.27,0.54),(0.43,0.32,0.24,0.53),(0.44,0.32,0.19,0.52),(0.49,0.36,0.15,0.49),
     (0.48,0.33,0.19,0.53),(0.42,0.31,0.23,0.55),(0.45,0.33,0.20,0.53),(0.47,0.34,0.21,0.52)]
M = [(0.16,0.32,0.24,0.30),(0.18,0.31,0.24,0.29),(0.21,0.30,0.22,0.28),(0.23,0.26,0.25,0.34),
     (0.23,0.16,0.24,0.41),(0.23,0.18,0.18,0.38),(0.24,0.19,0.20,0.40),(0.24,0.19,0.22,0.40)]
D = [(0.69,0.52,0.18,0.24),(0.68,0.51,0.18,0.26),(0.64,0.57,0.19,0.22),(0.65,0.52,0.18,0.29),
     (0.68,0.56,0.18,0.25),(0.66,0.51,0.18,0.24),(0.66,0.51,0.18,0.31),(0.69,0.54,0.18,0.25)]
build(7776, "A", "childhood", "female",
  [("to drive a red toy car", "the woman", "female", W),
   ("to lift up a drum", "the man", "male", M),
   ("to walk beside the car", "the dog", "female", D)],
  2.2,
  [("a picture", 0.18, 0.19, "female"), ("a teddy bear", 0.66, 0.54, "female"),
   ("a dog", 0.76, 0.65, "female"), ("a toy car", 0.35, 0.75, "female")],
  "What is the woman doing?", "She is driving a red toy car.", "female",
  "Man stands right behind the woman, so her box is cut on the left (her left leg/shoe and the left half of the car fall outside) and on the right at the dog. Man takes the drum out of the chest 0.2-1.2 s and lifts it over his head from 1.7 s.")
