from gen_6944_6945_6946_6947_lib import write
C = [(.31,.26,.72,.70),(.30,.25,.72,.70),(.27,.25,.72,.70),(.27,.25,.71,.70),(.27,.23,.71,.70),(.26,.23,.71,.70),(.26,.24,.70,.70),(.27,.23,.71,.70)]
WO = [(0,.43,.27,.74),(0,.43,.27,.74),(0,.44,.26,.74),(0,.44,.26,.74),(0,.42,.26,.72),(0,.42,.25,.74),(0,.43,.25,.74),(0,.43,.25,.74)]
M = [(.73,.44,1,1),(.73,.44,1,1),(.73,.44,1,1),(.73,.44,1,1),(.73,.43,1,1),(.73,.43,1,1),(.72,.45,1,1),(.72,.43,1,1)]
write(6945, "B", "charlotte", "male",
 [("to remove a metal ring", "the chef", "male", C),
  ("to cover her mouth", "the woman", "female", WO),
  ("to grip the tablecloth", "the man in the bow tie", "male", M)],
 2.7,
 [("a charlotte", .45, .71, "male"), ("a chef", .55, .42, "male"), ("a tablecloth", .30, .88, "male"), ("a velvet top", .12, .60, "male")],
 "What is the chef doing?", "He is removing a metal ring from the charlotte.", "male",
 "Woman's phrase 'to cover her mouth' is fairly basic for B; alternatives (gasp/stare) would also fit the man. Background man in grey suit is why the target is 'the man in the bow tie'.")
