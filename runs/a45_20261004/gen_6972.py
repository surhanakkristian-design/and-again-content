from gen_6971_6972_6973_6975_lib import write
W = [(0.34,0.30,0.33,0.36),(0.33,0.27,0.32,0.40),(0.30,0.24,0.44,0.52),(0.19,0.21,0.59,0.67),
     (0.23,0.15,0.57,0.83),(0.23,0.12,0.57,0.85),(0.22,0.12,0.56,0.86),(0.24,0.13,0.56,0.85)]
write(6972, "A", "come", "female",
  [("to come towards the camera", "the woman", "female", W),
   ("to laugh out loud", "the woman", "female", W),
   ("to wave her hand", "the woman", "female", W)],
  3.2,
  [("the sky", 0.50, 0.07, "female"), ("a jacket", 0.36, 0.38, "female"),
   ("cars", 0.80, 0.79, "female"), ("shoes", 0.50, 0.88, "female")],
  "What is the woman doing?", "She is coming towards the camera.", "female",
  "Only one person in the clip, so all three phrases share the woman. She waves only at the end (3.7). Small target at 0.2-0.7 (far away).")
