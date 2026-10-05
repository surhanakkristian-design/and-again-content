from gen_7026_7027_7028_7029_lib import write
M = [(0,0,1,.95),(0,0,1,.95),(.22,.27,.48,.49),(.21,.24,.47,.51),(.22,.20,.47,.53),(.22,.20,.47,.53),(.22,.20,.47,.53),(.23,.30,.44,.43)]
B = [None,None,(0,.40,.21,.22),(0,.37,.21,.27),(0,.35,.22,.30),(0,.35,.22,.30),(0,.36,.22,.30),(0,.36,.23,.30)]
write(7028, "B", "delete", "female",
 [("to clutch her phone", "the woman in pink", "female", M),
  ("to collapse onto the sofa", "the woman in pink", "female", M),
  ("to clasp her hands nervously", "the curly-haired woman", "female", B)],
 2.2,
 [("fairy lights", .18, .25, "female"), ("a flat-screen TV", .80, .24, "female"), ("a pizza box", .82, .44, "female"), ("popcorn", .52, .63, "female")],
 "What is the woman in pink doing?", "She is clutching her phone in shock.", "female",
 "Collapse onto the sofa only at 3.7 (blurred). Friend with braids not used (covers face at 1.2, laughs at 3.7). Curly-haired friend off in the close-up 0.2-0.7, only her blurry head at 1.2.")
