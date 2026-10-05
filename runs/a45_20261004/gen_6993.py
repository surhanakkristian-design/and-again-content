from gen_6993_6994_6995_6996_lib import build
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
woman = [(0.50,0.15,0.50,0.65),(0.62,0.13,0.38,0.67),(0.64,0.12,0.36,0.68),(0.65,0.11,0.35,0.69),
         (0.65,0.07,0.35,0.73),(0.66,0.01,0.34,0.79),(0.53,0.0,0.47,0.80),(0.69,0.0,0.31,0.80)]
cat = [(0.32,0.36,0.18,0.14),(0.33,0.35,0.29,0.14),(0.33,0.36,0.31,0.14),(0.33,0.35,0.31,0.14),
       (0.32,0.34,0.33,0.14),(0.30,0.32,0.35,0.14),(0.32,0.30,0.20,0.14),(0.40,0.28,0.29,0.14)]
build(6993, "B", "correspondent", "female", T,
  [("to write with a fountain pen", "the woman", "female", woman),
   ("to doze on the window seat", "the cat", "female", cat),
   ("to burst out laughing", "the woman", "female", woman)],
  0.7,
  [("a desk lamp", 0.13, 0.24, "female"), ("a cat", 0.47, 0.43, "female"),
   ("an inkwell", 0.31, 0.575, "female"), ("a bundle of letters", 0.66, 0.86, "female")],
  "What is the woman doing?", "She is writing a letter with a fountain pen.", "female",
  "Woman box covers head and body; her writing hand reaches left over the desk below the cat and is left out of the box so it never overlaps the cat box. Cat partly hidden behind her hand at 3.2; at 2.7 her pen hand passes in front of the cat inside the cat box. Key word 'correspondent' is not a visible noun.")
