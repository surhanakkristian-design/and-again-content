from gen_7167_7168_7169_7170_lib import write
man = [(.68,.32,.22,.28),(.69,.32,.22,.28),(.69,.32,.23,.28),(.70,.32,.23,.28),(.68,.32,.26,.29),(.70,.31,.27,.30),(.64,.29,.34,.32),(.64,.31,.33,.30)]
wom = [(.50,.37,.18,.25),(.51,.38,.18,.24),(.51,.38,.18,.24),(.52,.38,.18,.24),(.50,.38,.18,.24),(.52,.38,.18,.24),(.46,.37,.18,.25),(.46,.37,.18,.25)]
car = [(0,.37,.50,.27),(0,.37,.51,.27),(0,.37,.51,.27),(0,.37,.52,.27),(0,.36,.50,.28),(0,.36,.52,.28),(0,.36,.46,.29),(0,.37,.46,.28)]
write(7168, "B", "give a lift", "male",
 [("to hold the door open", "the man", "male", man),
  ("to climb into the passenger seat", "the woman", "female", wom),
  ("to have its headlights on", "the car", "male", car)],
 0.2,
 [("a church spire", .66, .33, "male"), ("a vintage car", .25, .50, "male"),
  ("a ribbon", .55, .79, "male"), ("petals", .50, .93, "male")],
 "What is the man doing?", ["He", "is", "holding", "the", "passenger", "door", "open."], "male",
 "People are small. The woman is mostly hidden inside the car (head behind windscreen/door, feet below); her box covers the door gap and is split from the man's box at his left edge. Car box covers only the front half (bonnet + headlights) so it does not overlap the people. defaultVoice male: the man is the main actor (gives the lift).")
