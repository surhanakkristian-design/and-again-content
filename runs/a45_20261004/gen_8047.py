from gen_8045_8046_8047_8048_lib import write
WO = [(.14,.29,.53,.58),(.24,.35,.43,.55),(.21,.35,.47,.59),(.28,.35,.42,.58),(.25,.33,.44,.64),(.27,.31,.44,.67),(.20,.30,.46,.70),(.06,.19,.56,.81)]
MA = [(.67,.27,.32,.26),(.67,.25,.33,.28),(.68,.25,.31,.28),(.70,.24,.29,.29),(.69,.23,.30,.30),(.71,.22,.29,.29),(.66,.21,.34,.34),(.62,.21,.22,.35)]
CA = [(.69,.56,.25,.14),(.70,.56,.26,.14),(.71,.57,.27,.14),(.72,.58,.28,.14),(.76,.59,.24,.14),(.78,.60,.22,.14),(.76,.62,.24,.14),(.80,.64,.20,.14)]
write(8047, "A", "yesterday", "female",
 [("to hold a paper crown", "the woman", "female", WO),
  ("to stand behind the sofa", "the man", "male", MA),
  ("to lie on a cushion", "the cat", "female", CA)],
 1.2,
 [("a lamp", .67, .11, "female"), ("a crown", .48, .50, "female"), ("a cat", .83, .63, "female"), ("a cake", .21, .65, "female")],
 "What is the woman holding?", "She is holding a paper crown.", "female",
 "Woman holds the crown 0.2-2.2, drops it onto the sofa at 2.7 and throws her arms up at 3.2-3.7. The man stands right behind her: woman/man boxes split at x~0.62-0.71; at 3.2-3.7 her raised right arm crosses the man's box area and is cut from her box. Man's action (pulling a streamer) is unclear in the frames, so a position phrase is used. Key word 'yesterday' is not a visible noun.")
