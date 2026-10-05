from lib_7896_7897_7898_7900 import write
man = [(.02,.47,.43,.51),(.07,.47,.4,.51),(.05,.46,.4,.52),(.03,.45,.4,.53),(.01,.44,.39,.54),(.01,.44,.39,.54),(.01,.45,.4,.53),(.01,.45,.4,.53)]
wom = [(.46,.48,.2,.26),(.47,.48,.19,.26),(.45,.52,.19,.23),(.45,.51,.2,.23),(.40,.49,.24,.24),(.40,.49,.24,.25),(.41,.5,.22,.24),(.41,.5,.22,.24)]
old = [(.14,.06,.2,.22),(.15,.06,.2,.22),(.15,.05,.2,.22),(.16,.05,.21,.22),(.16,.04,.28,.24),(.15,.04,.28,.24),(.16,.04,.24,.24),(.16,.04,.24,.24)]
write(7896, "A", "loudly", "male",
 [("to sneeze into his hand", "the man in white", "male", man),
  ("to watch from upstairs", "the old woman", "female", old),
  ("to open her mouth wide", "the woman in green", "female", wom)],
 2.2,
 [("a window", .52, .2, "male"), ("books", .6, .42, "male"), ("papers", .55, .75, "male"), ("a table", .7, .88, "male")],
 "What is the man in white doing?", "He is sneezing into his hand.", "male",
 "Key word 'loudly' left out of the answer: as a chip it could stand in two places. Man in red behind also reacts (hands on head), not a target.")
