from gen_6944_6945_6946_6947_lib import write
W = [(0,.10,.52,.82),(0,.08,.54,.82),(0,.09,.53,.82),(0,.08,.51,.82),(0,.08,.48,.82),(0,.03,.56,.82),(0,.08,.50,.82),(0,.28,.41,.82)]
D = [(.53,.35,.92,.79),(.55,.35,.92,.79),(.54,.34,.92,.79),(.52,.33,.92,.79),(.49,.34,.92,.80),(.57,.32,.92,.80),(.51,.32,.75,.47),(.42,.32,.66,.46)]
C = [None]*6 + [(.51,.48,1,1),(.45,.47,1,1)]
write(6947, "A", "chili", "female",
 [("to serve hot chili", "the woman", "female", W),
  ("to sit on a box", "the dog", "female", D),
  ("to take the bowl", "the customer", "female", C)],
 0.7,
 [("a woman", .15, .45, "female"), ("a pot", .45, .70, "female"), ("a dog", .74, .57, "female"), ("chili", .73, .89, "female")],
 "What is the woman doing?", "She is serving hot chili.", "female",
 "Dog is mostly hidden behind the bowl and the customer at 3.2-3.7 s (only hat and eyes), boxes kept small there. Customer only appears at 3.2 s (gloved hands and sleeve), off before.")
