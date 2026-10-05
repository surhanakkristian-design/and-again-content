from gen_7982_7983_7984_7985_lib import write
M = [(0.56,0.44,0.44,0.32),(0.55,0.46,0.45,0.28),(0.53,0.45,0.47,0.31),(0.55,0.42,0.45,0.34),
     (0.54,0.41,0.46,0.34),(0.57,0.40,0.43,0.36),(0.55,0.40,0.45,0.36),(0.54,0.40,0.46,0.36)]
G = [(0.0,0.21,0.42,0.30),(0.0,0.23,0.42,0.28),(0.0,0.22,0.40,0.29),(0.0,0.24,0.47,0.24),
     (0.0,0.19,0.44,0.30),(0.0,0.15,0.44,0.33),(0.0,0.17,0.44,0.32),(0.0,0.14,0.44,0.33)]
C = [(0.68,0.30,0.27,0.14),(0.78,0.32,0.22,0.14),(0.79,0.31,0.21,0.14),(0.80,0.26,0.20,0.15),
     (0.80,0.25,0.20,0.15),(0.80,0.25,0.20,0.15),(0.80,0.25,0.20,0.15),(0.80,0.25,0.20,0.15)]
write(7985, "A", "sit", "male",
  [("to yawn on the sofa", "the man", "male", M),
   ("to stand behind the sofa", "the woman in green", "female", G),
   ("to walk on the shelf", "the cat", "male", C)],
  2.2,
  [("a lamp", 0.59, 0.05, "male"), ("a picture", 0.28, 0.18, "male"),
   ("books", 0.88, 0.20, "male"), ("a cup", 0.38, 0.83, "male")],
  "What are the friends doing?", "They are sitting on the sofa.", "male",
  "Man yawns clearly at 1.2-3.2 (resting with eyes closed at 0.2-0.7). Woman in green box covers her upper body; her back leg at the far left and the head of the woman in burgundy are close below the box. Cat: leaping/walking on the cabinet at 0.2-1.2, then on a bookshelf shelf at 1.7-3.7 (small, partly hidden). Answer uses key word 'sit'; subject 'They' = mixed group -> defaultVoice male (evenId false).")
