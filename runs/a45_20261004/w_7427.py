from w_7421_7422_7425_7427_lib import build
W=[[.18,.29,.68,.51],[.42,.28,.36,.53],[.25,.29,.66,.52],[.21,.28,.63,.53],[.33,.27,.37,.51],[.43,.27,.27,.52],[.35,.29,.50,.50],[.28,.29,.64,.51]]
M=[[.00,.40,.18,.28],[.00,.40,.18,.28],[.00,.41,.20,.29],[.02,.40,.18,.30],[.03,.39,.20,.30],[.03,.40,.20,.29],[.03,.40,.20,.30],[.03,.40,.20,.30]]
build(7427,'B','picture','female',
 [("to twirl in the sunlight","the woman","female",W),
  ("to spread her arms wide","the woman","female",W),
  ("to lean against the doorframe","the man","male",M)],
 3.7,
 [("an arched window",.62,.17,"female"),("a pallet",.37,.58,"female"),("a wheelbarrow",.84,.62,"female"),("rubble",.15,.72,"female")],
 "What is the woman doing?","She is twirling in the sunlight.","female",
 "Key word 'picture' is a verb, so it is not a noun slot. At 0.2 and 1.7 the woman's left hand nearly reaches the man: boxes split at x~.18-.21, the tip of her hand may be cut. 'a pallet' = the stack of wooden pallets leaning on the wall behind her.")
