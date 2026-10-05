from gen_6944_6945_6946_6947_lib import write
M = [(.46,.03,.94,.87),(.47,.01,.98,.88),(.47,0,1,.90),(.49,0,1,.92),(.48,.21,1,1),(.47,.18,1,1),(.44,.15,1,1),(.42,.12,1,1)]
O = [(.29,.40,.45,.71),(.29,.40,.46,.72),(.29,.41,.46,.71),(.28,.41,.48,.73),(.25,.40,.47,.76),(.14,.43,.46,.81),(.04,.51,.43,.89),(.01,.51,.41,.87)]
write(6946, "B", "chile", "male",
 [("to raise a bunch of chiles", "the man in the neckerchief", "male", M),
  ("to chew a hot chile", "the man in the neckerchief", "male", M),
  ("to pour water over himself", "the older man", "male", O)],
 0.2,
 [("dried chiles", .37, .18, "male"), ("a basket", .18, .70, "male"), ("a referee", .10, .48, "male"), ("a neckerchief", .62, .44, "male")],
 "What is the young man doing?", "He is chewing a hot chile.", "male",
 "Older man's pouring: he holds a glass/jug over his head and water splashes at 2.7-3.2 s; check it reads as pouring over himself. Board and plates also hold chiles; only the hanging string is labelled 'dried chiles'. Main man's left arm on the table is partly outside his box where it crosses the older man.")
