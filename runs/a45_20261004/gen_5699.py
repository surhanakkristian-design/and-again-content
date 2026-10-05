from gen_5698_5699_5700_5701_lib import write
man = [(0,.25,.43,.73),(.05,.28,.38,.67),(.12,.30,.30,.60),(.15,.31,.28,.55),(.15,.32,.24,.52),(.04,.34,.40,.49),(.13,.37,.34,.41),(.29,.38,.24,.38)]
wom = [(.46,.38,.26,.40),(.43,.38,.27,.40),(.43,.38,.27,.38),(.44,.38,.28,.38),(.52,.38,.21,.38),(.53,.38,.21,.38),(.47,.38,.30,.38),(.53,.38,.25,.41)]
boat = [(.72,.52,.28,.48),(.70,.51,.30,.49),(.70,.52,.30,.48),(.72,.52,.28,.48),(.73,.52,.27,.48),(.74,.51,.26,.49),(.77,.52,.23,.48),(.78,.52,.22,.48)]
write(5699, "B", "call in", "male",
 [("to wave her over", "the man", "male", man),
  ("to stroll towards him", "the woman", "female", wom),
  ("to lie on the sand", "the boat", "male", boat)],
 2.2,
 [("the sky", .50, .12, "male"), ("a lamp post", .86, .32, "male"), ("a boat", .86, .72, "male"), ("sand", .40, .88, "male")],
 "What is the man doing?", "He is waving her over.", "male",
 "Man's outstretched arm at 0.2-1.7 s reaches over the woman's area, so his box covers his body only (arm cut off at about x 0.43). Woman's and boat's boxes split along the boat's edge. Answer fits 0.2-1.7 s; later he points towards the game.")
