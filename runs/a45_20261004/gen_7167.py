from gen_7167_7168_7169_7170_lib import write
dog = [(.37,.45,.19,.18),(.40,.44,.19,.23),(.41,.41,.25,.32),(.41,.37,.29,.42),(.39,.37,.28,.44),(.34,.35,.28,.42),(.30,.34,.34,.44),(.26,.34,.36,.44)]
wom = [(.60,.22,.40,.46),(.60,.22,.40,.46),(.66,.19,.34,.50),(.70,.17,.30,.52),(.67,.22,.27,.50),(.62,.29,.32,.46),(.64,.25,.28,.51),(.62,.27,.31,.49)]
write(7167, "B", "get", "female",
 [("to drag an inflatable flamingo", "the dog", "female", dog),
  ("to spread her arms wide", "the woman", "female", wom),
  ("to hug the soaking wet dog", "the woman", "female", wom)],
 1.2,
 [("an inflatable flamingo", .18, .50, "female"), ("a golden retriever", .55, .60, "female"),
  ("a knitted jumper", .78, .33, "female"), ("wet sand", .45, .74, "female")],
 "What is the dog doing?", ["The", "dog", "is", "dragging", "an", "inflatable", "flamingo."], "female",
 "Woman and dog overlap from 2.2 s; boxes split at the dog's right edge, so part of the woman's head/arms behind the dog is outside her box. Flamingo not used as a tap target (attached to the dog's mouth). 'to hug' only true from ~2.7 s.")
