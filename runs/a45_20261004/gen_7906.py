from gen_7905_7906_7908_7909_lib import write
red = [(.05,.21,.90,.53),(.13,.37,.72,.51),(0,.46,1,.54),(0,.56,1,.44),(0,.64,1,.36),(.15,.73,.75,.27),(0,.79,1,.21),(.05,.80,.95,.20)]
blu = [(.62,0,.32,.21),(.62,0,.32,.37),(.61,0,.34,.46),(.62,.09,.33,.47),(.61,.19,.35,.45),(.61,.28,.33,.45),(.60,.33,.35,.46),(.61,.36,.35,.44)]
write(7906, "B", "mindset", "female",
 [("to make a snow angel", "the woman in red", "female", red),
  ("to fold her arms", "the woman at the bus stop", "female", blu),
  ("to lie back in the snow", "the woman in red", "female", red)],
 2.2,
 [("a double-decker bus", .17, .25, "female"), ("bicycles", .50, .37, "female"),
  ("snow", .25, .55, "female"), ("a puffer jacket", .72, .73, "female")],
 "What is the woman in red doing?", "She is making a snow angel.", "female",
 "Boxes split along y where the lying woman's head meets the standing woman's legs (rect overlap), so the red woman's face is partly cut at 0.2-1.7 s. Key word 'mindset' not shown as a noun. Bus not a target (camera moves, unclear if it drives).")
