from gen_8045_8046_8047_8048_lib import write
WO = [(.06,.27,.74,.71),(.04,.27,.78,.71),(.04,.27,.77,.71),(.02,.27,.80,.71),(.02,.26,.81,.72),(.02,.25,.81,.73),(.02,.25,.60,.73),(.02,.24,.56,.74)]
MA = [(.80,.26,.20,.53),(.82,.24,.18,.54),(.81,.23,.19,.56),(.82,.23,.18,.56),(.83,.22,.17,.57),(.83,.20,.17,.59),(.62,.21,.38,.62),(.58,.19,.42,.62)]
write(8046, "A", "yard", "female",
 [("to touch her nose", "the woman", "female", WO),
  ("to cut the blue cloth", "the man", "male", MA),
  ("to wear a dark red jumper", "the woman", "female", WO)],
 1.2,
 [("a lamp", .53, .05, "female"), ("a man", .88, .37, "male"), ("a woman", .25, .55, "female"), ("scissors", .43, .79, "female")],
 "What is the woman doing?", "She is holding the blue cloth to her nose.", "female",
 "The man cuts only at 3.7 (scissors in his hand); before that his hands rest on the cloth roll. Woman/man boxes split at x~0.81-0.83 where her hand meets his head (0.2-2.7) and at 0.62/0.58 at 3.2-3.7, where his forearm and the scissors reach into the woman's box. Key word 'yard' (measure) is not a visible noun.")
