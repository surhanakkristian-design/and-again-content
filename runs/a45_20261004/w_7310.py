from w_7310_7311_7312_7313_lib import build
couple = [(.31,.21,.20,.19),(.34,.21,.17,.19),(.35,.21,.16,.19),(.34,.21,.17,.19),(.33,.21,.18,.21),(.34,.22,.17,.19),(.34,.22,.17,.22),(.34,.22,.17,.22)]
man = [(.52,.19,.18,.14),(.52,.19,.18,.14),(.52,.19,.18,.14),(.52,.19,.18,.14),(.52,.19,.18,.14),(.52,.19,.18,.14),(.52,.19,.18,.14),(.52,.19,.18,.14)]
wave = [(.30,.41,.70,.59),(.18,.41,.82,.59),(.08,.41,.92,.59),(.12,.41,.88,.59),(.0,.45,1.0,.55),None,None,None]
build(7310, "A", "lover", "female",
  [("to kiss on the balcony", "the couple", "female", couple),
   ("to look out of the window", "the man", "male", man),
   ("to hit the tower", "the big wave", "female", wave)],
  3.2,
  [("lovers", .43, .33, "female"), ("a lighthouse", .55, .52, "female"), ("a door", .33, .70, "female"), ("rocks", .20, .91, "female")],
  "What are the lovers doing?", "They are kissing on the balcony.", "female",
  "Couple = mixed pair, default voice female (evenId). The man inside the lamp room looks out through the glass (the couple also stand near the lamp, so no lamp phrase); small, box at minimum size. Wave is off from 2.7 (only foam on the rocks then); at 2.2 it is falling back.")
