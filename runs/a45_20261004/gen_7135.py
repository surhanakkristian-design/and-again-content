from gen_7135_7136_7137_7138_lib import write
man = [(.44,.38,.53,.62),(.47,.38,.51,.62),(.52,.38,.44,.62),(.56,.37,.42,.63),(.31,.38,.60,.62),(.31,.38,.56,.62),(.31,.38,.54,.62),(.31,.37,.48,.63)]
woman = [(0,.56,.27,.42),(0,.56,.28,.42),(0,.57,.29,.43),(0,.53,.31,.47),(.02,.51,.28,.46),(.03,.49,.27,.44),(.04,.48,.26,.43),(.04,.48,.26,.42)]
ball = [(.19,.31,.24,.15),(.24,.35,.22,.15),(.27,.41,.24,.15),(.34,.46,.21,.15),None,None,None,(.80,.52,.19,.16)]
write(7135, "B", "force", "male",
  [("to grip a red lever", "the curly-haired man", "male", man),
   ("to film with a tablet", "the woman in the lab coat", "female", woman),
   ("to smash into the watermelons", "the wrecking ball", "male", ball)],
  3.7,
  [("a crane", .30, .22, "male"), ("the sky", .72, .12, "male"), ("a tablet", .25, .55, "male"), ("watermelons", .80, .84, "male")],
  "What is the curly-haired man doing?", "He is gripping a red lever.", "male",
  "Wrecking ball swings behind the man after 1.7 s: off at 2.2-3.2 (mostly hidden behind him), only its right half visible at 3.7. "
  "Ball box and man box split at 0.2-1.7, so the man's box leaves out his lever hand there. Key word force is abstract, not a noun slot.")
