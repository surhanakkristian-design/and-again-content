from gen_5698_5699_5700_5701_lib import write
wom = [(.15,.36,.35,.47),(.15,.36,.35,.47),(.14,.36,.36,.49),(.14,.36,.36,.49),(.13,.35,.37,.52),(.13,.35,.37,.52),(.17,.36,.34,.44),(.11,.34,.41,.44)]
man = [(.53,.31,.38,.38),(.53,.31,.38,.38),(.53,.30,.38,.41),(.53,.29,.38,.42),(.52,.30,.39,.42),(.53,.29,.39,.44),(.53,.30,.39,.46),(.59,.29,.37,.47)]
dog = [(.50,.69,.18,.16),(.50,.69,.18,.16),(.50,.71,.18,.16),(.50,.71,.18,.16),(.50,.72,.18,.16),(.50,.73,.18,.16),(.36,.80,.29,.15),(.21,.78,.39,.18)]
write(5700, "B", "call on", "female",
 [("to hold the door open", "the woman", "female", wom),
  ("to grip the handlebars", "the man", "male", man),
  ("to wander across the porch", "the dog", "female", dog)],
 2.2,
 [("a lantern", .13, .29, "female"), ("a door", .47, .40, "female"), ("a bicycle", .72, .86, "female"), ("a flowerpot", .13, .88, "female")],
 "What is the man doing?", "He is gripping the handlebars.", "male",
 "Dog stands half hidden behind the bike wheel until 2.7 s, then walks out to the left; man's box stops above the dog (his legs are behind the bike anyway). Woman lets go of the door around 3.2 s.")
