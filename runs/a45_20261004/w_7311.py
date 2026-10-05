from w_7310_7311_7312_7313_lib import build
waiter = [(0,.29,.26,.47),(0,.29,.27,.47),(0,.30,.39,.46),(0,.28,.42,.50),(0,.27,.46,.49),(.11,.28,.38,.48),(.22,.30,.28,.53),(.29,.29,.26,.46)]
woman = [(.26,.29,.41,.51),(.27,.28,.44,.52),(.39,.29,.43,.61),(.47,.27,.53,.70),(.50,.26,.47,.68),(.52,.25,.48,.71),(.50,.26,.50,.72),(.55,.25,.45,.73)]
build(7311, "B", "madame", "female",
  [("to take her camel coat", "the young waiter", "male", waiter),
   ("to carry a straw basket", "the woman", "female", woman),
   ("to slip out of her coat", "the woman", "female", woman)],
  2.2,
  [("a waiter", .15, .42, "male"), ("a camel coat", .31, .58, "female"), ("a straw basket", .78, .66, "female"), ("a carafe", .15, .74, "female")],
  "What is the woman carrying?", "She is carrying a straw basket with a leek.", "female",
  "Key word madame is a form of address (only in the greeting), not placed as a noun. Two phrases on the woman (the bearded waiter is only partly visible at the edge and hard to follow). Young waiter = the one who takes the coat (left; at 3.2/3.7 the one holding the coat, a second waiter with a tray is beside him). Woman's coat edge at 0.2-0.7 and the basket at 3.2-3.7 cross the split line between the two boxes.")
