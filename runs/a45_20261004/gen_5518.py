from gen_5515_5516_5518_5519_lib import write
W = [(.20,.18,.43,.54),(.20,.18,.44,.52),(.18,.18,.43,.55),(.14,.17,.43,.56),(.12,.15,.42,.55),(.09,.14,.43,.52),(.14,.12,.80,.30),(.18,.12,.84,.31)]
M = [(.43,.29,1,.99),(.44,.29,1,.99),(.43,.28,1,.99),(.43,.29,1,.99),(.42,.28,1,.99),(.43,.28,1,.99),(.10,.30,1,.99),(.12,.31,1,.99)]
write(5518, "A", "acceptable", "male",
 [("to make an OK sign", "the man", "male", M),
  ("to hold a mirror", "the woman", "female", W),
  ("to brush his neck", "the woman", "female", W)],
 2.2,
 [("a mirror", .70, .27, "male"), ("a woman", .30, .27, "female"), ("a man", .56, .40, "male"), ("a chair", .45, .82, "male")],
 "What is the man doing?", ["He", "is", "making", "an", "OK", "sign."], "male",
 "Woman stands directly behind the seated man: vertical split at the man's head until 2.7 s, so the mirror she holds falls in the man's box there; at 3.2-3.7 s her face shows above his head, so the split is horizontal (woman box = her head + mirror band). OK sign visible about 1.2-2.2 s.")
