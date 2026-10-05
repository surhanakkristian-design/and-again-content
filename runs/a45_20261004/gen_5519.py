from gen_5515_5516_5518_5519_lib import write
M = [(.42,.23,.65,.53),(.42,.23,.66,.53),(.41,.23,.66,.535),(.43,.22,.68,.545),(.41,.22,.67,.565),(.40,.21,.68,.57),(.40,.21,.69,.56),(.39,.20,.70,.57)]
D = [(.42,.53,.68,.73),(.42,.53,.66,.73),(.41,.535,.66,.75),(.40,.545,.67,.76),(.41,.565,.66,.77),(.39,.57,.67,.76),(.39,.56,.64,.74),(.37,.57,.59,.73)]
write(5519, "B", "accessible", "male",
 [("to hold the door open", "the man", "male", M),
  ("to wear a green apron", "the man", "male", M),
  ("to trot down the ramp", "the dog", "male", D)],
 2.2,
 [("an apron", .54, .38, "male"), ("a flowerpot", .67, .53, "male"), ("a dachshund", .52, .66, "male"), ("a ramp", .55, .79, "male")],
 "What is the dog doing?", ["It", "is", "trotting", "down", "the", "ramp."], "male",
 "Man stands right above the dog: boxes split at the man's feet (dog's ears/tail touch that line). 'to hold the door open' = his hand rests on the open door's frame the whole clip. The wheelchair user's hands are not used as a target. defaultVoice male: no main on-screen person besides the man (evenId false).")
