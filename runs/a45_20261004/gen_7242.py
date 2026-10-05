from gen_7242_7243_7244_7245_lib import write
man = [(.44,.33,.35,.45),(.38,.32,.46,.46),(.36,.32,.52,.67),(.35,.30,.63,.70),(.30,.27,.68,.73),(.19,.26,.81,.74),(.19,.24,.81,.76),(.0,.22,1.0,.78)]
woman = [(.05,.36,.39,.48),(.05,.36,.33,.53),(.12,.36,.24,.63),(.13,.36,.22,.63),(.05,.34,.25,.65),(.0,.34,.19,.66),(.0,.37,.18,.30),None]
write(7242, "B", "immigrant", "male",
 [("to gaze up at the snowflakes", "the young man", "male", man),
  ("to wrap a parka around him", "the young woman", "female", woman),
  ("to clutch the warm parka", "the young man", "male", man)],
 0.2,
 [("a bobble hat", .23, .40, "male"), ("a taxi", .88, .45, "male"), ("a suitcase", .66, .72, "male"), ("a cardboard box", .40, .88, "male")],
 "What is the woman doing?", "She is wrapping a parka around him.", "female",
 "Camera pushes in; the woman leaves the frame at the left edge (sliver at 3.2 s, off at 3.7 s). Man holds the parka closed from about 2.2 s. Key word 'immigrant' is not a visible noun, not placed.")
