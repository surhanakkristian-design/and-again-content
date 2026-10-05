from w_7841_7842_7843_7846_lib import write
B = [(.09,.22,.30,.55),(.10,.25,.29,.50),(.09,.24,.29,.50),(.09,.23,.28,.51),(.11,.24,.27,.53),(.10,.27,.31,.52),(.10,.30,.28,.54),(.09,.34,.29,.55)]
M = [(.40,.38,.31,.26),(.40,.38,.36,.29),(.44,.32,.26,.29),(.38,.44,.28,.21),(.43,.48,.24,.17),(.42,.50,.24,.18),(.42,.55,.24,.16),(.41,.58,.25,.15)]
R = [(.72,.37,.26,.33),(.77,.37,.23,.31),(.71,.37,.29,.33),(.67,.36,.33,.32),(.68,.36,.32,.32),(.67,.38,.33,.31),(.67,.42,.33,.33),(.67,.45,.33,.33)]
write(7846, "B", "geography", "female",
 [("to hold a measuring pole", "the woman in blue", "female", B),
  ("to lose his balance", "the man", "male", M),
  ("to stretch a measuring tape", "the woman in the beige hat", "female", R)],
 2.7,
 [("clouds", .50, .10, "female"), ("a glacier", .52, .33, "female"), ("a float", .50, .76, "female"), ("a clipboard", .76, .89, "female")],
 "What is the woman in blue holding?", "She is holding a tall measuring pole.", "female",
 "The woman in the beige hat stretches one leg towards the man: boxes split vertically, her foot is cut out of her box (inside or near the man's box). The man loses his balance 0.2-1.2 and sits in the water from 1.7. The float flies from the man's hand at 0.2 and lands in the water.")
