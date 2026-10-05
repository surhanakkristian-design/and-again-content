from w_7372_7373_7376_7377_lib import write
young = [(.39,.26,.23,.29),(.39,.26,.23,.31),(.38,.26,.23,.45),(.33,.27,.28,.45),(.31,.30,.29,.35),(.29,.34,.30,.33),(.24,.34,.34,.35),(.24,.35,.34,.35)]
chef = [(.63,.03,.28,.34),(.63,.05,.28,.33),(.62,.07,.27,.30),(.62,.10,.28,.29),(.61,.12,.28,.30),(.60,.14,.27,.29),(.59,.16,.30,.27),(.59,.18,.30,.25)]
write(7377, "B", "move up", "male",
 [("to climb a spiral staircase", "the young man", "male", young),
  ("to reach up for the jacket", "the young man", "male", young),
  ("to hold out a chef's jacket", "the older chef", "male", chef)],
 2.2,
 [("a chef's jacket", .71, .31, "male"), ("a spiral staircase", .30, .56, "male"), ("a stockpot", .76, .88, "male")],
 "What is the young man doing?", "He is climbing a spiral staircase.", "male",
 "Boxes split along x between the young man and the older chef; the young man's raised hand often pokes past his box into the jacket area. Cheering cooks and balcony waiters not used as targets (several do the same). Copper pans hang on both sides, so not used as a noun.")
