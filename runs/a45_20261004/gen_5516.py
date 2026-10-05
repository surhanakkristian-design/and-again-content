from gen_5515_5516_5518_5519_lib import write
M = [(0,.06,1,1),(0,0,.80,1),(0,.04,.66,1),(0,.04,.55,1),(0,.16,.46,.98),(0,.20,.42,.98),(0,.28,.38,1),(0,.26,.38,1)]
F = [None,(.80,.40,1,.84),(.66,.40,1,.98),(.55,.39,1,.95),(.46,.37,.90,.86),(.42,.36,.83,.82),(.38,.37,.76,.79),(.38,.36,.77,.78)]
write(5516, "B", "abusive", "male",
 [("to shake his fist", "the man", "male", M),
  ("to shout at a cyclist", "the man", "male", M),
  ("to cycle past the taxi", "the woman", "female", F)],
 3.2,
 [("neon signs", .80, .14, "male"), ("a food stall", .85, .48, "male"), ("a bicycle", .62, .65, "male"), ("a driver", .15, .45, "male")],
 "What is the man doing?", ["He", "is", "shaking", "his", "fist", "at", "the", "cyclist."], "male",
 "Raised arm/fist of the man reaches over the woman's region at 0.7-2.7 s; split vertically so the fist is partly outside the man box. Woman marked off at 0.2 s (only a blurred sliver at the edge). 'a driver' assumes he drives the three-wheeled taxi.")
