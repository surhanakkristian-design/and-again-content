from lib_w_7137_7138_7140_7141 import write
woman = [(.38,.39,.32,.41),(.52,.39,.21,.41),(.50,.39,.23,.41),(.52,.38,.23,.43),(.53,.36,.23,.45),(.53,.36,.24,.45),(.53,.36,.25,.45),(.54,.36,.23,.45)]
suit = [(.71,.48,.29,.27),(.73,.48,.27,.27),(.73,.48,.27,.28),(.75,.48,.25,.28),(.76,.47,.24,.29),(.77,.47,.23,.29),(.78,.48,.22,.28),(.77,.48,.23,.29)]
grey = [(0,.55,.32,.25),(0,.55,.32,.25),(0,.56,.30,.24),(0,.56,.30,.24),(0,.55,.31,.25),(0,.56,.31,.24),(0,.55,.30,.26),(0,.55,.30,.26)]
write(7140, "B", "forum", "female", [
  ("to address the crowd", "the young woman", "female", woman),
  ("to gesture from his chair", "the man in the suit", "male", suit),
  ("to fold his arms", "the man in the grey shirt", "male", grey)],
  2.2, [("a street lamp", .85, .16, "female"), ("a scale model", .36, .60, "female"), ("a cushion", .32, .83, "female"), ("documents", .74, .83, "female")],
  "What is the young woman doing?", "She is addressing the crowd in the square.", "female",
  "key word forum (the meeting) not used as a noun pill: not a single placeable thing; man in grey folds his arms from about 1.2 s, earlier hand at mouth; suit man gestures mainly 2.2-3.7")
