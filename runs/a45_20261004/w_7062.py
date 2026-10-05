from w_7060_7061_7062_7063_lib import write
woman = [(0.27, 0.15, 0.80, 0.90), (0.29, 0.15, 0.82, 0.90), (0.31, 0.16, 0.82, 0.93), (0.29, 0.16, 0.84, 0.93),
         (0.32, 0.22, 0.86, 0.94), (0.35, 0.21, 0.87, 0.97), (0.31, 0.07, 0.87, 1), (0.32, 0.07, 0.88, 1)]
waitress = [(0, 0.40, 0.27, 0.94), (0, 0.40, 0.29, 0.95), (0, 0.40, 0.29, 0.98), (0, 0.42, 0.28, 0.98),
            (0, 0.42, 0.29, 0.98), (0, 0.42, 0.30, 0.98), (0, 0.44, 0.29, 1), (0, 0.44, 0.27, 1)]
write(7062, "A", "down", "female", [
  ("to drink a big milkshake", "the woman in black", "female", woman),
  ("to hold a metal jug", "the waitress", "female", waitress),
  ("to raise her fist", "the woman in black", "female", woman)],
  2.7, [("a jug", 0.17, 0.66, "female"), ("a milkshake", 0.67, 0.58, "female"), ("a counter", 0.82, 0.76, "female")],
  "What is the woman in black doing?", "She is drinking a big milkshake.", "female",
  "Bikers are a crowd (many point/cheer) so no biker target. Woman drinks 0.2-1.7, lowers glass 2.2-2.7, fist up 3.2-3.7. Waitress holds the jug in every frame. Nouns: no stool/fan/burger (several of each visible). Key word 'down' is a verb, not placed as a noun.")
