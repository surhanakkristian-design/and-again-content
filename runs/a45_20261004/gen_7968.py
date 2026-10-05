from gen_7968_7969_7970_7971_lib import write
man = [(.45,.22,.33,.74),(.45,.21,.35,.75),(.45,.24,.34,.73),(.41,.20,.52,.78),(.39,.19,.48,.80),(.36,.18,.49,.81),(.39,.18,.48,.82),(.39,.18,.48,.82)]
wom = [(0,.41,.45,.57),(0,.41,.45,.57),(0,.42,.45,.56),(0,.42,.40,.56),(0,.39,.38,.61),(0,.39,.35,.61),(0,.42,.32,.58),(0,.42,.32,.58)]
write(7968, "B", "run out of time", "female",
 [("to gaze up at the ceiling", "the man", "male", man),
  ("to snatch the exam paper", "the man", "male", man),
  ("to scribble on the exam paper", "the woman", "female", wom)],
 3.2,
 [("a clock", .82, .15, "female"), ("wood panelling", .32, .37, "female"), ("an exam paper", .63, .51, "female"), ("a rucksack", .80, .81, "female")],
 "What is the man doing?", "He is snatching her exam paper.", "male",
 "Two phrases on the man (gaze up at the ceiling 0.2-1.2, eyes closed after; snatches paper 0.7-1.7). Woman and man overlap at the paper 0.2-1.2: split at x 0.45, the man's left leg and the paper's left edge fall slightly in the woman's box. Rucksack = the black bag on the floor right.")
