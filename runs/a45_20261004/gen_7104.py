from gen_7103_7104_7105_7106_lib import write
j = [[.52,.33,.25,.25],[.57,.32,.25,.26],[.57,.32,.26,.28],[.58,.32,.25,.30],[.55,.31,.26,.28],[.55,.29,.26,.31],[.53,.29,.27,.32],[.51,.28,.28,.33]]
l = [[.81,.48,.19,.35],[.83,.48,.17,.36],[.84,.50,.16,.33],[.84,.53,.16,.33],[.83,.56,.17,.28],[.83,.58,.17,.32],None,None]
write(7104, "A", "favourite", "male",
  [("to ride a grey horse", "the man in green", "male", j),
   ("to blow a bubble", "the man in green", "male", j),
   ("to lead the grey horse", "the man in black", "male", l)],
  0.2,
  [("the sky", .15, .07, "male"), ("trees", .72, .15, "male"), ("a crowd", .15, .40, "male"), ("a horse", .66, .60, "male")],
  "What is the man in green doing?", "He is riding a grey horse.", "male",
  "The man leading the horse is only a dark edge at the right from 2.2 s and gone at 3.2-3.7 s (off). Fans also wear green scarves: target named 'the man in green' = the jockey in the green star shirt. Brown horses also visible in the still; 'a horse' pill on the grey one.")
