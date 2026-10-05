from gen_5515_5516_5518_5519_lib import write
W = [(.27,.14,.85,.78),(.42,.12,.86,.84),(.28,.12,.84,.79),(.43,.12,.88,.80),(.44,.10,.84,.80),(.43,.09,.85,.82),(.44,.08,.85,.81),(.45,.08,.86,.83)]
R = [(.12,.78,.62,.92),(.18,.62,.42,.84),(.14,.79,.45,.93),(.14,.80,.62,.94),(.13,.80,.60,.94),(.12,.82,.62,.96),(.12,.81,.62,.95),(.11,.83,.62,.97)]
write(5515, "B", "abuse", "female",
 [("to stamp on her racket", "the woman", "female", W),
  ("to clench her fists", "the woman", "female", W),
  ("to bend under her foot", "the racket", "female", R)],
 2.7,
 [("a racket", .26, .84, "female"), ("a tennis ball", .69, .88, "female"), ("a bench", .90, .70, "female"), ("a fence", .20, .40, "female")],
 "What is the woman doing?", ["She", "is", "stamping", "on", "her", "racket."], "female",
 "Woman's feet touch the racket: woman box bottom cut at the racket line, racket box starts there. Racket bends only around 0.7 s.")
