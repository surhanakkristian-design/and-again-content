from w_7841_7842_7843_7846_lib import write
W = [(0,.28,.50,.41),(0,.29,.50,.42),(0,.29,.50,.41),(0,.29,.50,.40),(0,.29,.50,.39),(0,.29,.50,.39),(0,.29,.50,.38),(0,.29,.50,.38)]
B = [(.50,.32,.18,.14),(.50,.30,.18,.14),(.50,.32,.18,.14),None,None,None,None,None]
H = [(.60,.47,.40,.53),(.58,.45,.42,.55),(.57,.50,.43,.50),(.54,.56,.46,.44),(.53,.59,.47,.41),(.53,.58,.47,.42),(.52,.60,.48,.40),(.52,.59,.48,.41)]
write(7842, "A", "free time", "female",
 [("to eat a berry", "the woman", "female", W),
  ("to swim on the lake", "the bird", "female", B),
  ("to hold a fishing rod", "the right hand", "female", H)],
 2.2,
 [("trees", .84, .20, "female"), ("a lake", .80, .45, "female"), ("an apple", .34, .69, "female"), ("a bag", .49, .82, "female")],
 "What is the woman eating?", "She is eating a berry.", "female",
 "Bird (loon) is small and only visible 0.2-1.2, then dives (splash at 1.7) -> off. Right-hand box covers hand, arm and reel, not the whole rod (the rod tip would overlap the bird box at 0.7/1.2). The left hand (apple) is not a target. Berry is small and dark (could read as a cherry).")
