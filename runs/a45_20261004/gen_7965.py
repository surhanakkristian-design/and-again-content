from gen_7963_7964_7965_7967_lib import build
man = [(0,0.32,0.24,0.68),(0,0.32,0.26,0.52),(0,0.31,0.27,0.58),(0,0.30,0.37,0.58),
       (0,0.29,0.43,0.50),(0,0.30,0.50,0.53),(0,0.33,0.62,0.58),(0,0.31,0.62,0.58)]
cat = [(0.24,0.34,0.53,0.48),(0.08,0.52,0.32,0.70),(0,0.58,0.24,0.75),(0,0.58,0.20,0.74),None,None,None,None]
wom = [(0.24,0.48,1.0,0.90),(0.32,0.40,1.0,0.90),(0.27,0.40,1.0,0.90),(0.37,0.40,1.0,0.90),
       (0.24,0.50,1.0,0.90),(0.24,0.53,1.0,0.90),(0.24,0.58,1.0,0.90),(0.24,0.58,1.0,0.90)]
build(7965, "B", "rough day", "female",
  [("to sprawl across the sofa", "the woman", "female", wom),
   ("to leap off the sofa", "the cat", "female", cat),
   ("to set down his mug", "the man", "male", man)],
  2.2,
  [("a lampshade", 0.59, 0.21, "female"), ("bookshelves", 0.74, 0.33, "female"),
   ("a sofa", 0.84, 0.72, "female"), ("a tote bag", 0.66, 0.89, "female")],
  "What is the woman doing?", "She is sprawling across the velvet sofa.", "female",
  "Man, cat and woman overlap heavily in the picture: boxes are split. Woman box leaves out her hands on the rug (left, x<0.24) and, from 3.2 s, her raised legs on the sofa (above y 0.58) where the man leans over her; man box loses his legs at 0.7-2.7 s. Cat only 0.2-1.7 s (leaps at 0.2, then walks off left). Man puts the mug on the side table around 1.7-2.7 s, then reaches over to pat her.")
