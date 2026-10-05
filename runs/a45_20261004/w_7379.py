from w_7378_7379_7381_7382_lib import write
man = [(.24,.18,.84,.76),(.24,.19,.88,.80),(.25,.25,.87,.88),(.23,.26,.87,.88),(.23,.31,.85,.86),(.25,.33,.85,.86),(.24,.24,.86,.86),(.33,.07,.87,.88)]
wom = [(0,.51,.23,.80),(0,.52,.23,.80),(0,.52,.24,.82),(0,.52,.22,.82),(0,.50,.22,.78),(0,.49,.24,.78),(0,.49,.23,.80),(0,.48,.21,.80)]
write(7379, "B", "narrator", "male",
 [("to spread his arms wide", "the standing man", "male", man),
  ("to raise both arms high", "the standing man", "male", man),
  ("to clutch a metal mug", "the woman on the left", "female", wom)],
 0.2,
 [("a narrator", .55, .45, "male"), ("lanterns", .15, .24, "male"), ("a coiled rope", .15, .42, "male"), ("plates", .25, .79, "male")],
 "What is the standing man doing?", "He is spreading his arms wide.", "male",
 "storyteller is the only clear actor, so two phrases share him (arms spread wide 0.2-2.7, both arms raised high 3.7); dog at his feet is too dark/hidden to use; woman's mug hand clipped where her box meets his")
