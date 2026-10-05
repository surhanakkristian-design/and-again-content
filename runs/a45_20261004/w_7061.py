from w_7060_7061_7062_7063_lib import write
man = [(0.26, 0.36, 1, 1), (0.23, 0.33, 1, 0.95), (0.35, 0.16, 1, 1), (0.46, 0.10, 1, 1),
       (0.49, 0.11, 1, 1), (0.42, 0.12, 1, 0.91), (0.36, 0.15, 1, 0.88), (0.31, 0.13, 1, 0.86)]
write(7061, "B", "dot", "male", [
  ("to paint a tiny red dot", "the young man", "male", man),
  ("to step back from the wall", "the young man", "male", man),
  ("to inspect his work", "the young man", "male", man)],
  3.7, [("dots", 0.18, 0.30, "male"), ("a harness", 0.56, 0.40, "male"), ("a bucket", 0.72, 0.62, "male"), ("paint pots", 0.38, 0.76, "male")],
  "What is the young man painting?", "He is painting a tiny red dot.", "male",
  "Only one real target: the painter (0.2-0.7 only his hand and forearm with the brush), so all three phrases use him. Tiny cyclists/pedestrians below at 2.7-3.7 too small for a tap target. He steps back between 1.2 and 2.2 and squints at the wall from 1.7 on.")
