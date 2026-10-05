from lib_w_7137_7138_7140_7141 import write
wave = [(.53,.20,.45,.50),(.53,.18,.47,.54),(.53,.15,.47,.59),(.53,.16,.47,.58),(.53,.29,.47,.53),(.53,.37,.47,.46),(.55,.52,.45,.42),(.56,.52,.44,.39)]
sold = [(0,.47,.52,.17),(0,.48,.52,.17),(.03,.50,.49,.16),(.04,.51,.48,.17),(.01,.55,.51,.17),(.03,.56,.49,.16),(.01,.60,.51,.16),(.03,.60,.49,.16)]
boat = [(.22,.81,.26,.14),(.24,.82,.26,.14),(.26,.84,.25,.14),(.27,.85,.24,.14),(.28,.85,.24,.15),(.28,.86,.24,.14),(.28,.86,.24,.14),None]
write(7138, "B", "fort", "female", [
  ("to crash over the thick walls", "the huge wave", "female", wave),
  ("to stand in formation", "the soldiers in rows", "female", sold),
  ("to rock in the rough sea", "the small boat", "female", boat)],
  2.7, [("a sunbeam", .28, .28, "female"), ("smoke", .12, .45, "female"), ("soldiers", .28, .64, "female"), ("a fort", .75, .84, "female")],
  "What is the huge wave doing?", "It is crashing over the thick walls.", "female",
  "camera tilts down slowly; wave box at the end covers the water pouring back off the walls; boat leaves frame at 3.7")
