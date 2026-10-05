from gen_7213_7214_7215_7216_lib import write
W = [(.36,.33,.30,.67),(.36,.33,.30,.67),(.37,.33,.28,.67),(.37,.33,.27,.67),(.33,.30,.38,.70),(.35,.29,.44,.71),(.28,.27,.52,.73),(.27,.26,.53,.74)]
D = [(.08,.66,.27,.32),(.08,.66,.27,.33),(.04,.68,.32,.32),(.03,.68,.33,.32),(.0,.69,.32,.31),(.0,.71,.34,.29),(.0,.74,.27,.26),(.0,.77,.26,.23)]
M = [(.67,.30,.33,.48),(.67,.30,.33,.50),(.66,.31,.34,.47),(.66,.31,.34,.47),(.72,.56,.28,.26),(.82,.68,.18,.18),None,None]
write(7213, "B", "haven", "female", [
  ("to huddle under a blanket", "the woman", "female", W),
  ("to lie at her feet", "the dog", "female", D),
  ("to hand over a steaming mug", "the man in green", "male", M)],
  1.7, [("a blanket", .55, .88, "female"), ("a sheepdog", .20, .75, "female"), ("a kettle", .13, .64, "female"), ("a mug", .62, .52, "female")],
  "What is the woman doing?", ["She", "is", "cradling", "a", "hot", "mug."], "female",
  "Man in green: only his arm/hand at 2.2-2.7, off from 3.2. Woman/dog boxes split at the dog's back where the dog lies against the blanket. Hikers at the door (0.2-0.7) overlap the man-in-green box area. Haven not a visible noun.")
