from w_7372_7373_7376_7377_lib import write
ship = [(.09,.02,.70,.55),(.08,.02,.71,.55),(.06,.01,.73,.56),(.06,.01,.73,.56),(.03,.01,.76,.56),(.02,.01,.77,.56),(.00,.00,.79,.57),(.00,.00,.79,.57)]
worker = [(.61,.58,.18,.14),(.61,.58,.18,.14),(.61,.58,.18,.15),(.62,.58,.18,.15),(.66,.60,.18,.15),(.69,.61,.18,.15),(.72,.60,.18,.16),None]
crowd = [(.80,.40,.20,.17)]*8
write(7373, "B", "move into", "male",
 [("to squeeze into a narrow lock", "the cruise ship", "male", ship),
  ("to stride along the quayside", "the worker in front", "male", worker),
  ("to wave at the huge ship", "the crowd on the quay", "male", crowd)],
 1.2,
 [("a cruise ship", .40, .45, "male"), ("spectators", .88, .52, "male"), ("a railing", .22, .71, "male"), ("a stone hut", .89, .72, "male")],
 "What is the cruise ship doing?", "It is squeezing into a narrow lock.", "male",
 "Ship box stops at y 0.57 and x 0.79 to stay clear of the worker and crowd boxes (bow tip ~0.62 and upper decks to ~0.86 fall outside). Worker in front hidden behind the hut at 3.7. Second hi-vis worker stands inside the crowd box. Crowd box covers the upper part of the crowd only.")
