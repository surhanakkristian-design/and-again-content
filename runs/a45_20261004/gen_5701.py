from gen_5698_5699_5700_5701_lib import write
wom = [(.04,.13,.83,.58),(.04,.14,.96,.62),(.04,.18,.96,.65),(.05,.19,.95,.69),(.03,.22,.93,.67),(.03,.23,.97,.65),(.02,.24,.98,.66),(.03,.24,.95,.66)]
write(5701, "B", "call out", "female",
 [("to hold out a slate", "the woman", "female", wom),
  ("to call out excitedly", "the woman", "female", wom),
  ("to kneel on the steep roof", "the woman", "female", wom)],
 2.2,
 [("storm clouds", .40, .08, "female"), ("the sea", .15, .31, "female"), ("a slate", .86, .39, "female"), ("roof tiles", .55, .86, "female")],
 "What is the woman holding out?", "She is holding out a slate.", "female",
 "All three phrases on the woman: the two workers below are tiny, side by side and barely visible at 0.2 s, so no clean second target. Woman's box is large (slate in her outstretched hand) and covers the workers, who are not targets.")
