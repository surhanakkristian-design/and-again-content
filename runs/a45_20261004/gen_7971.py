from gen_7968_7969_7970_7971_lib import write
wom = [(.38,.19,.32,.59),(.38,.19,.33,.60),(.38,.19,.32,.60),(.38,.19,.34,.60),(.38,.19,.34,.60),(.38,.19,.34,.60),(.37,.19,.33,.60),(.38,.19,.34,.60)]
man = [(.70,.20,.30,.72),(.71,.20,.29,.72),(.70,.20,.30,.72),(.72,.20,.28,.72),(.72,.20,.28,.74),(.72,.20,.28,.75),(.70,.20,.30,.78),(.72,.20,.28,.78)]
blu = [(.19,.36,.19,.35),(.18,.36,.20,.35),(.18,.37,.20,.36),(.18,.37,.20,.35),(.17,.36,.21,.37),(.17,.36,.21,.37),(.16,.36,.21,.37),(.16,.36,.22,.37)]
write(7971, "B", "scale", "female",
 [("to flex her biceps", "the boxer", "female", wom),
  ("to adjust the scale", "the man in the white shirt", "male", man),
  ("to punch the air", "the man in the blue jacket", "male", blu)],
 1.2,
 [("a boxing ring", .12, .25, "female"), ("a crowd", .12, .42, "female"), ("satin shorts", .48, .54, "female"), ("a weighing scale", .50, .81, "female")],
 "What is the boxer doing?", "She is flexing her biceps on the scale.", "female",
 "Boxer's raised left arm (x .18-.38) is outside her box: it lies above the man in the blue jacket, whose box takes that column. The white-shirt man's pointing hand over the scale beam is outside his box (split at x .70-.72). He slides the weight 0.2-2.7, fist bump 3.2-3.7. Blue-jacket man raises his fist throughout.")
