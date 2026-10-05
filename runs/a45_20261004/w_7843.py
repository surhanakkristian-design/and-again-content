from w_7841_7842_7843_7846_lib import write
M = [(.31,.22,.47,.65),(.31,.22,.50,.65),(.31,.20,.50,.67),(.31,.19,.47,.70),(.31,.19,.42,.74),(.31,.19,.43,.75),(.31,.18,.58,.75),(.31,.17,.65,.82)]
J = [(.79,.27,.21,.70),(.82,.27,.18,.70),(.82,.27,.18,.70),(.79,.27,.21,.73),(.74,.28,.26,.72),(.75,.28,.25,.72),None,None]
S = [(.06,.39,.24,.29),(.06,.39,.24,.29),(.04,.38,.26,.32),(.03,.38,.26,.33),(.03,.37,.27,.32),(.02,.37,.27,.32),(.01,.34,.28,.36),(.03,.33,.25,.38)]
write(7843, "B", "freezing", "male",
 [("to hold up a frozen towel", "the man", "male", M),
  ("to reach for the towel", "the woman in the jacket", "female", J),
  ("to climb up the ladder", "the woman in the swimsuit", "female", S)],
 3.7,
 [("a cabin", .82, .21, "male"), ("a towel", .45, .40, "male"), ("a swimsuit", .14, .48, "male"), ("a bathrobe", .75, .70, "male")],
 "What is the man holding?", "He is holding a frozen towel.", "male",
 "Woman in the jacket overlaps the man (her arm reaches across his robe): boxes split vertically, her arm stays in the man's box, the man's right robe edge is cut at 0.7-2.7. She is only a thin sliver at the right edge at 3.2/3.7 -> off. Swimsuit woman climbs the ladder 0.2-2.7, stands and hugs herself at 3.2-3.7.")
