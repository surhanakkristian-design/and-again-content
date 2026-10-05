from gen_5644_5645_5646_5647_lib import write
wom = [(.40,.28,.36,.50),(.41,.29,.35,.49),(.40,.29,.37,.51),(.40,.29,.37,.51),(.40,.29,.37,.50),(.40,.29,.37,.49),(.41,.30,.36,.50),(.41,.30,.36,.50)]
bak = [(.00,.15,.29,.51),(.00,.15,.30,.51),(.00,.16,.32,.51),(.00,.17,.31,.50),(.02,.17,.34,.50),(.02,.17,.36,.50),(.03,.18,.38,.48),(.02,.18,.39,.49)]
man = [(.76,.10,.24,.48),(.76,.09,.24,.49),(.77,.09,.23,.49),(.77,.09,.23,.50),(.77,.09,.23,.50),(.77,.10,.23,.48),(.77,.10,.23,.48),(.77,.10,.23,.48)]
write(5647, "B", "beloved", "female",
 [("to cradle the dog's face", "the young woman", "female", wom),
  ("to hold out some bread", "the baker", "male", bak),
  ("to perch on a ladder", "the bearded man", "male", man)],
 2.2,
 [("an apron", .13, .42, "female"), ("a dog", .42, .55, "female"), ("a ladder", .88, .68, "female"), ("bowls", .22, .84, "female")],
 "What is the young woman doing?", "She is cradling the dog's face.", "female",
 "Dog overlaps the young woman, so it is only a noun. Bearded man's box starts at x=.76-.77, cutting a sliver of his hand holding the scraper and of her jacket edge. Baker only holds the bread out clearly from ~2.2 s. Key word 'beloved' is an adjective, not placed.")
