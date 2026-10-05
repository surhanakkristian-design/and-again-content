from gen_7905_7906_7908_7909_lib import write
man = [(0,.34,.40,.52)]*6 + [(0,.34,.38,.52),(0,.34,.37,.52)]
mid = [(.40,.28,.30,.60)]*6 + [(.38,.28,.30,.60),(.37,.28,.30,.60)]
write(7905, "B", "middle", "female",
 [("to fold her arms", "the woman in yellow", "female", mid),
  ("to burst out laughing", "the woman in yellow", "female", mid),
  ("to wear a white T-shirt", "the man", "male", man)],
 2.2,
 [("a ceiling light", .50, .20, "female"), ("the rear window", .50, .32, "female"),
  ("denim shorts", .52, .59, "female"), ("a long skirt", .80, .67, "female")],
 "Where is the woman in yellow sitting?", "She is squeezed in the middle.", "female",
 "Man and woman in burgundy both stretch an arm and both touch their head at 3.2 s, so no unique action for them: man gets a state; woman in burgundy is not a target. Middle woman laughs loudly at 0.2-0.7 and 3.2-3.7; others only smile.")
