from w_7372_7373_7376_7377_lib import write
woman = [(.13,.24,.36,.49),(.15,.24,.36,.52),(.16,.26,.34,.54),(.19,.26,.32,.56),(.18,.28,.33,.57),(.17,.30,.39,.57),(.19,.33,.38,.53),(.18,.31,.32,.53)]
monkey = [(.29,.05,.20,.15),(.30,.06,.20,.15),(.30,.09,.20,.15),(.31,.10,.20,.15),(.31,.12,.20,.15),(.31,.12,.20,.15),(.31,.12,.20,.15),(.32,.12,.20,.15)]
man = [(.72,.74,.24,.26),(.74,.76,.22,.24),(.73,.80,.23,.20),(.76,.83,.22,.17),(.76,.86,.23,.14),(.77,.86,.23,.14),(.77,.86,.23,.14),(.79,.86,.21,.14)]
write(7372, "B", "move in", "female",
 [("to hoist a heavy bundle", "the woman", "female", woman),
  ("to crouch beside a lantern", "the monkey", "female", monkey),
  ("to steady the rope from below", "the man", "male", man)],
 2.2,
 [("a monkey", .38, .20, "female"), ("a sleeping mat", .66, .46, "female"), ("a cardboard box", .54, .59, "female")],
 "What is the woman doing?", "She is hoisting a heavy bundle onto the porch.", "female",
 "Man below is small and partly cut at the bottom edge; his phrase 'steady the rope from below' - he holds the rope's lower end. Lantern omitted as a noun because it sits right next to the monkey.")
