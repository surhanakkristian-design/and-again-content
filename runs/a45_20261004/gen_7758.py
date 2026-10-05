from gen_7758_7759_7760_7762_lib import write
man = [(0.0,0.55,0.16,0.42),(0.0,0.42,0.25,0.53),(0.0,0.49,0.35,0.49),(0.0,0.50,0.46,0.48),
       (0.22,0.48,0.35,0.45),(0.28,0.48,0.35,0.42),(0.32,0.50,0.31,0.42),(0.31,0.50,0.31,0.41)]
woman = [None,None,None,(0.20,0.39,0.26,0.11),(0.07,0.38,0.15,0.40),(0.02,0.39,0.25,0.38),(0.14,0.40,0.18,0.36),(0.15,0.40,0.16,0.36)]
worker = [None,None,(0.0,0.34,0.18,0.14),(0.02,0.34,0.18,0.15),(0.22,0.35,0.18,0.13),(0.28,0.35,0.18,0.13),(0.32,0.37,0.20,0.13),(0.33,0.37,0.19,0.13)]
write(7758, "B", "backup", "male",
 [("to tug at a heavy suitcase", "the man", "male", man),
  ("to clutch a red suitcase", "the woman", "female", woman),
  ("to sort through the luggage", "the worker", "male", worker)],
 3.7,
 [("a yellow suitcase", 0.68, 0.39, "male"), ("a red suitcase", 0.30, 0.67, "male"),
  ("a baggage carousel", 0.84, 0.82, "male"), ("windows", 0.20, 0.25, "male")],
 "What is the young man doing?", "He is tugging at a heavy suitcase.", "male",
 "woman stands right behind the man: boxes split along the line between them (1.7 only her head/shoulders above him); man at 0.2 only a leg at the left edge")
