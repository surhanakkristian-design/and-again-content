from gen_7905_7906_7908_7909_lib import write
wom = [(.48,.35,.49,.48),(.48,.33,.52,.54),(.48,.31,.49,.62),(.41,.30,.47,.69),(.37,.29,.52,.71),(.33,.27,.56,.73),(.26,.25,.65,.75),(.21,.23,.76,.77)]
man = [(.31,.39,.17,.26),(.28,.38,.20,.27),(.21,.38,.25,.29),(.18,.37,.22,.31),(.14,.38,.22,.31),(.09,.38,.23,.32),(.04,.38,.22,.35),(0,.38,.21,.36)]
write(7908, "B", "miss", "female",
 [("to drag a suitcase", "the woman", "female", wom),
  ("to stare in shock", "the woman", "female", wom),
  ("to blow a whistle", "the station worker", "male", man)],
 1.2,
 [("a globe lamp", .51, .19, "female"), ("a train", .88, .42, "female"),
  ("clothes", .15, .69, "female"), ("a suitcase", .40, .79, "female")],
 "What has just happened to the woman?", "She has just missed her train.", "female",
 "Whistle: worker holds a small object to his mouth at 0.2-0.7 s (looks like a whistle, blurry). Present perfect answer for the result state. Train not a tap target (behind the woman). Boxes of woman/worker split at x .26/.21 at 3.2/3.7 s where her coat meets his body.")
