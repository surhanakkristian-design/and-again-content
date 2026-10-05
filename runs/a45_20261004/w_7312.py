from w_7310_7311_7312_7313_lib import build
man = [(.19,.13,.45,.83),(.19,.12,.48,.86),(.18,.12,.50,.87),(.15,.11,.53,.88),(.05,.08,.62,.92),(0,.06,.84,.94),(0,.03,.72,.97),(0,.03,.64,.97)]
cust = [(.70,.46,.30,.20),(.70,.46,.30,.21),(.71,.49,.29,.18),(.80,.55,.20,.16),None,None,(.73,.61,.27,.20),(.64,.60,.36,.20)]
pig = [(0,.41,.19,.15),(0,.42,.19,.14),(0,.41,.18,.14),(0,.44,.15,.15),None,None,None,None]
build(7312, "A", "magazine", "male",
  [("to look through magazines", "the man", "male", man),
   ("to take a magazine", "the customer", "male", cust),
   ("to walk on the street", "the pigeons", "male", pig)],
  0.2,
  [("a bus", .10, .30, "male"), ("a bell", .88, .15, "male"), ("newspapers", .22, .64, "male"), ("a magazine", .20, .78, "male")],
  "What is the man doing?", "He is looking through magazines.", "male",
  "The customer is only an arm/hand reaching in from the right (gender unknown, default voice); at 1.7 only a sliver at the right edge, off at 2.2-2.7. The man's stack of magazines reaches into the customer box (split at the hand). Pigeons small at the left, off from 2.2. 'a magazine' = the single magazine lying on the pavement.")
