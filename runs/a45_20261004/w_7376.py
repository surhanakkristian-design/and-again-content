from w_7372_7373_7376_7377_lib import write
woman = [(.18,.43,.56,.20),(.29,.43,.45,.21),(.36,.43,.50,.22),(.47,.44,.35,.17),(.40,.43,.50,.17),(.36,.43,.57,.18),(.35,.42,.57,.20),(.34,.43,.62,.18)]
boat = [(.27,.02,.32,.14),(.27,.02,.32,.14),(.27,.02,.32,.14),(.29,.02,.32,.14),(.30,.02,.33,.14),(.33,.02,.33,.14),(.37,.02,.33,.15),(.38,.02,.35,.15)]
write(7376, "B", "move through", "female",
 [("to glide through the shoal", "the woman", "female", woman),
  ("to kick with long fins", "the woman", "female", woman),
  ("to float on the surface", "the boat", "female", boat)],
 2.2,
 [("a boat", .48, .10, "female"), ("a dolphin", .66, .42, "female"), ("a diver", .56, .53, "female"), ("a shoal", .30, .80, "female")],
 "What is the woman doing?", "She is gliding through a shoal of fish.", "female",
 "Dolphins swap and cross, so none is used as a tap target; woman used twice. Woman box includes fins and overlaps dolphins and fish (not targets).")
