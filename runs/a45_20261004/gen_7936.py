from gen_7935_7936_7937_7938_lib import write
cat = [(0.00,0.31,0.45,0.40),(0.00,0.30,0.46,0.40),(0.00,0.32,0.46,0.40),(0.00,0.31,0.46,0.40),
       (0.00,0.30,0.45,0.40),(0.00,0.30,0.45,0.42),(0.00,0.31,0.45,0.42),(0.00,0.31,0.45,0.43)]
hare = [(0.53,0.30,0.47,0.62),(0.53,0.29,0.47,0.63),(0.53,0.30,0.47,0.62),(0.53,0.30,0.47,0.62),
        (0.54,0.29,0.46,0.63),(0.54,0.29,0.46,0.63),(0.54,0.29,0.46,0.63),(0.54,0.29,0.46,0.63)]
write(7936, "B", "pharmaceutical", "female", [
  ("to count out tiny pills", "the cat", "female", cat),
  ("to lean on the counter", "the hare", "female", hare),
  ("to grab a medicine bottle", "the cat", "female", cat)],
  2.2, [("a snowy window", 0.80, 0.24, "female"), ("a striped scarf", 0.86, 0.60, "female"),
        ("a medicine bottle", 0.16, 0.68, "female"), ("a marble counter", 0.30, 0.86, "female")],
  "What is the cat doing?", "The cat is counting pills with a spatula.", "female",
  "Key word 'pharmaceutical' is an adjective, not placed. Cat has two phrases (counting pills on the tray, then lifting the brown bottle at 2.2-3.7; it holds the bottle from the start). Hare is blurred at 2.7 (shakes its head). 'to lean on the counter' fits the hare only: the cat stands behind the counter working.")
