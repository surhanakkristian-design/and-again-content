from w_7245_7246_7247_7248_lib import write
woman = [(0.18,0.28,0.78,1.00),(0.18,0.29,0.78,1.00),(0.21,0.27,0.79,1.00),(0.39,0.29,0.92,1.00),
         (0.39,0.25,0.87,1.00),(0.38,0.25,0.80,0.98),(0.37,0.18,0.75,0.95),(0.37,0.18,0.74,0.95)]
cat =   [(0.07,0.09,0.36,0.28),(0.10,0.10,0.37,0.28),(0.10,0.11,0.39,0.27),(0.10,0.11,0.38,0.29),
         (0.10,0.09,0.38,0.27),(0.08,0.09,0.36,0.27),(0.08,0.08,0.35,0.27),(0.09,0.08,0.35,0.27)]
couple = [(0.79,0.58,1.00,0.95),(0.79,0.58,1.00,0.95),(0.80,0.59,1.00,0.96),None,
          (0.88,0.58,1.00,0.94),(0.81,0.58,1.00,0.95),(0.76,0.57,1.00,0.94),(0.75,0.57,1.00,0.94)]
write(7247, "B", "insert", "female",
  [("to insert a heavy book", "the woman", "female", woman),
   ("to watch from above", "the cat", "female", cat),
   ("to cover their mouths", "the couple", "female", couple)],
  3.2,
  [("a cat", 0.22, 0.18, "female"), ("bookshelves", 0.16, 0.48, "female"),
   ("a ladder", 0.46, 0.64, "female"), ("a couple", 0.88, 0.72, "female")],
  "Where is the woman standing?", ["She", "is", "standing", "on", "a", "wooden", "ladder."], "female",
  "Couple covers mouths only in 0.2-1.2 s, then claps; hidden behind the woman at 1.7 (off) and only the man's edge at 2.2. Woman's box cut where her skirt meets the couple. Book insertion happens 0.2-0.7 s.")
