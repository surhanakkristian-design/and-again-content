from lib_7896_7897_7898_7900 import write
man = [(.22,.36,.45,.41),(.23,.36,.46,.43),(.23,.39,.5,.38),(.21,.38,.55,.45),(.26,.40,.67,.5),(.28,.41,.72,.5),(.30,.42,.70,.52),(.29,.41,.71,.53)]
kn  = [(0,.40,.22,.35),(0,.40,.23,.35),(0,.40,.23,.35),(0,.40,.21,.36),(0,.39,.26,.39),(0,.39,.28,.39),(0,.41,.30,.38),(0,.41,.29,.38)]
red = [(.67,.33,.18,.39),(.69,.31,.18,.4),(.73,.32,.18,.38),(.76,.31,.18,.4),(.74,.26,.22,.14),(.74,.27,.22,.14),(.72,.18,.26,.24),(.71,.24,.27,.17)]
write(7898, "B", "lowest", "male",
 [("to bend backwards under the pole", "the man in blue", "male", man),
  ("to kneel beside the post", "the woman in green", "female", kn),
  ("to punch the air", "the red-haired woman", "female", red)],
 0.2,
 [("the sky", .6, .06, "male"), ("a thatched roof", .22, .22, "male"), ("a bamboo pole", .28, .46, "male"), ("sand", .5, .88, "male")],
 "What is the man in blue doing?", "He is bending backwards under the bamboo pole.", "male",
 "From t=2.2 the limbo man's body covers the red-haired woman; her box is cut to the part above his head (head, raised fist). Earlier his right hand/foot touch her area, split at her left edge. 'to punch the air' = her raised fist at 3.2-3.7 (others raised arms only at the start). Key word 'lowest' not used (no natural fit).")
