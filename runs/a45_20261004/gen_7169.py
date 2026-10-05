from gen_7167_7168_7169_7170_lib import write
mid = [(0,.28,.28,.20),(0,.27,.28,.21),(0,.26,.27,.23),(0,.24,.28,.24),(0,.21,.26,.25),(0,.20,.26,.25),(0,.18,.22,.28),(0,.17,.22,.25)]
wom = [(.02,.48,.50,.41),(.01,.48,.52,.41),(0,.49,.53,.50),(.01,.48,.52,.45),(0,.46,.52,.50),(0,.45,.53,.50),(0,.46,.58,.54),(0,.42,.58,.58)]
man = [(.52,.44,.48,.50),(.53,.42,.47,.52),(.53,.40,.47,.56),(.53,.39,.47,.56),(.52,.36,.48,.60),(.53,.34,.47,.62),(.58,.31,.42,.62),(.58,.31,.42,.66)]
write(7169, "B", "give birth", "female",
 [("to kneel in the pool", "the pregnant woman", "female", wom),
  ("to lean over the pool", "the man", "male", man),
  ("to hold a small torch", "the midwife", "female", mid)],
 0.2,
 [("fairy lights", .72, .10, "female"), ("a birthing ball", .35, .42, "female"),
  ("a medical kit", .86, .45, "female"), ("a birth pool", .45, .88, "female")],
 "What is the pregnant woman doing?", ["She", "is", "kneeling", "in", "a", "birth", "pool."], "female",
 "Pregnant woman and man touch (foreheads, clasped hands): boxes split at the hands, x ~.52-.58. Midwife sits top-left right above the woman's head: midwife box ends at y ~.42-.49 and the woman's box starts there, so the top of the woman's bun is outside her box. Man's lower arm left of x .58 is cut at 3.2-3.7 s. 'to lean over the pool' = he leans over the inflatable rim from outside.")
