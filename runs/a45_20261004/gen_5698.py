from gen_5698_5699_5700_5701_lib import write
man = [(0,.30,.38,.65),(0,.28,.39,.67),(0,.28,.37,.71),(.02,.19,.36,.80),(0,.24,.40,.76),(0,.22,.37,.78),(0,.20,.39,.80),(0,.17,.42,.83)]
wom = [(.39,.31,.42,.62),(.40,.30,.44,.64),(.38,.29,.53,.68),(.38,.26,.48,.72),(.40,.25,.53,.75),(.37,.22,.52,.78),(.39,.22,.52,.78),(.42,.19,.56,.81)]
write(5698, "B", "call for", "female",
 [("to call for the ball", "the woman", "female", wom),
  ("to try to block his shot", "the woman", "female", wom),
  ("to hold the ball overhead", "the man", "male", man)],
 0.2,
 [("a basketball", .12, .37, "female"), ("a hoop", .55, .10, "female"), ("a crop top", .66, .52, "female"), ("a fence", .86, .70, "female")],
 "What is the woman doing?", "She is calling for the ball.", "female",
 "Woman's raised hand overlaps the man's arms from 1.7 s; split at the line between them. Bystanders by the fence not used.")
