from w_7378_7379_7381_7382_lib import write
# boxes as x0,y0,x1,y1
man = [(.16,.21,.50,.74),(.16,.20,.53,.76),(.17,.19,.53,.78),(.13,.19,.52,.78),(.12,.18,.54,.80),(.18,.16,.68,.85),(.22,.15,.79,.99),(.14,.14,.76,1)]
woman = [(.51,.36,.74,.68),(.54,.36,.79,.71),(.54,.36,.81,.70),(.53,.37,.84,.73),(.55,.38,.89,.74),(.69,.39,.94,.76),(.80,.41,.99,.74),(.77,.44,1,.76)]
off = [(0,.30,.15,.80),(0,.29,.15,.78),(0,.29,.16,.92),(0,.31,.12,.93),(0,.38,.11,.93),(0,.29,.17,.93),(0,.30,.21,.99),(0,.32,.13,.97)]
write(7378, "B", "murderer", "male",
 [("to stare blankly ahead", "the man in the suit", "male", man),
  ("to sob into a coat", "the woman", "female", woman),
  ("to grip the man's arm", "the police officer", "male", off)],
 0.2,
 [("a murderer", .30, .38, "male"), ("a tall window", .52, .10, "male"), ("a water jug", .74, .73, "male"), ("a file", .66, .84, "male")],
 "What is the woman in black doing?", "She is sobbing into a dark coat.", "female",
 "police officer is mostly cut off at the left edge (narrow boxes, split from the man's arm); 'a murderer' pill placed on the handcuffed man in the dock")
