from gen_7026_7027_7028_7029_lib import write
M = [(.27,.29,.47,.43),(.27,.29,.50,.44),(.26,.30,.53,.45),(.26,.30,.52,.48),(.22,.30,.55,.51),(.22,.30,.58,.53),(.20,.31,.58,.55),(.20,.31,.62,.57)]
write(7029, "A", "department store", "male",
 [("to carry a lot of gifts", "the man", "male", M),
  ("to go down the escalator", "the man", "male", M),
  ("to wear a green jacket", "the man", "male", M)],
 1.2,
 [("a Christmas tree", .48, .16, "male"), ("a lamp", .40, .36, "male"), ("a teddy bear", .48, .48, "male"), ("an escalator", .50, .85, "male")],
 "What is the man doing?", "He is carrying a lot of gifts.", "male",
 "Only one clear target (the man); shoppers are a crowd. Key word 'department store' is the whole place, not a noun at one spot, so not placed. 'Christmas' capitalised as a proper adjective.")
