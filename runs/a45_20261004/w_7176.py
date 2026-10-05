from w_7176_7177_7178_7182_lib import write
woman = [(.37,.38,.63,.64),(.37,.38,.62,.64),(.37,.38,.64,.64),(.38,.38,.65,.64),(.37,.38,.64,.64),(.31,.36,.59,.64),(.30,.38,.59,.67),(.30,.38,.58,.67)]
goat  = [(.63,.42,.77,.63),(.62,.42,.76,.63),(.64,.42,.77,.63),(.65,.42,.79,.63),(.64,.41,.79,.63),(.59,.41,.80,.63),(.59,.41,.77,.64),(.58,.40,.77,.64)]
man   = [(.13,.41,.29,.62)]*8
write(7176, "A", "go by bus", "female",
 [("to take off her hat", "the woman with the hat", "female", woman),
  ("to look into the bus", "the goat", "female", goat),
  ("to hold a chicken", "the man at the back", "male", man)],
 3.7,
 [("a goat", .68, .47, "female"), ("a hat", .50, .58, "female"), ("a basket", .18, .76, "female"), ("a window", .87, .33, "female")],
 "What is the goat doing?", "It is looking into the bus.", "female",
 "Goat head sits right next to the woman's hat brim at 0.2-2.2; boxes split at the hat brim / goat face. Man at the back holds a brown hen (small). Woman takes off the hat at about 2.5-3.0.")
