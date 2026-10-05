from gen_7968_7969_7970_7971_lib import write
wom = [(.37,.35,.33,.65),(.40,.35,.30,.65),(.37,.35,.35,.65),(.40,.35,.34,.65),(.36,.33,.42,.67),(.36,.33,.44,.67),(.36,.36,.36,.64),(.36,.33,.34,.67)]
bus = [(.70,.24,.26,.48),(.70,.22,.28,.50),(.72,.19,.27,.45),(.74,.16,.26,.45),(.78,.12,.22,.45),(.80,.10,.20,.45),(.72,.18,.28,.45),(.70,.15,.30,.45)]
blu = [(0,.33,.37,.32),(0,.33,.40,.32),(0,.34,.37,.32),(0,.34,.40,.32),(0,.30,.36,.34),(0,.29,.36,.34),(0,.33,.36,.34),(0,.34,.36,.32)]
write(7969, "B", "rush hour", "female",
 [("to snap a selfie", "the woman in the red jacket", "female", wom),
  ("to hold a briefcase overhead", "the businessman", "male", bus),
  ("to lean against a pole", "the man in the blue coat", "male", blu)],
 1.2,
 [("hand straps", .12, .20, "female"), ("a briefcase", .78, .24, "female"), ("a beanie", .49, .41, "female"), ("a puffer jacket", .58, .74, "female")],
 "What is the businessman doing?", "He is holding his briefcase overhead.", "male",
 "Selfie shot, three people overlap: woman box split at the man in blue (her outstretched arm lies over him, bottom-left, outside her box) and at the businessman (her right shoulder edge cut). Businessman box excludes the left end of the briefcase at 0.2-0.7. Man in blue box = face and shoulder only (y .3-.65); the lower blue coat lies under the woman's arm.")
