from gen_7968_7969_7970_7971_lib import write
wom = [(.34,.27,.42,.49),(.34,.27,.41,.49),(.34,.26,.41,.50),(.34,.27,.45,.41),(.33,.26,.47,.43),(.33,.25,.48,.44),(.32,.25,.48,.43),(.29,.30,.44,.45)]
man = [(0,.26,.34,.50),(0,.25,.34,.52),(0,.25,.34,.53),(0,.25,.34,.53),(0,.23,.33,.55),(0,.23,.33,.55),(0,.23,.32,.55),(0,.21,.29,.58)]
gul = [(.76,.66,.24,.26),(.75,.66,.25,.26),(.75,.66,.25,.23),(.68,.68,.32,.18),(.66,.69,.34,.17),(.66,.69,.34,.17),(.68,.68,.32,.20),(.73,.67,.27,.22)]
write(7970, "A", "sadly", "female",
 [("to hold an empty cone", "the woman", "female", wom),
  ("to touch her shoulder", "the man", "male", man),
  ("to eat the ice cream", "the seagull", "female", gul)],
 3.2,
 [("beach huts", .12, .22, "female"), ("a railing", .80, .40, "female"), ("a seagull", .86, .72, "female"), ("an ice cream", .64, .81, "female")],
 "What is the seagull eating?", "It is eating the ice cream.", "female",
 "The man holds a full cone, the woman an empty one, so 'empty cone' fits only her. Seagull pecks the ice cream clearly at 2.2-2.7, walks up to it before. Woman box shortened at the bottom (knees/shoes) where the seagull is close, 1.7-3.2; at 3.7 she leans into the man, split at x .29.")
