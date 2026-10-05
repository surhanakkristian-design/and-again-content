from gen_7103_7104_7105_7106_lib import write
m = [[.18,.31,.59,.61],[.16,.35,.63,.57],[.16,.35,.61,.59],[.13,.23,.67,.75],[.11,.17,.69,.81],[.11,.19,.70,.81],[.11,.22,.71,.78],[.16,.17,.66,.83]]
write(7106, "A", "feel sick", "male",
  [("to hold on to the rail", "the man", "male", m),
   ("to open his mouth wide", "the man", "male", m),
   ("to touch his chest", "the man", "male", m)],
  0.2,
  [("the sky", .50, .08, "male"), ("the sea", .15, .32, "male"), ("a man", .45, .52, "male"), ("a rope", .82, .64, "male")],
  "What is the man doing?", "He is holding on to the rail.", "male",
  "Only one person in the clip, so all three phrases use the man. Mouth opens wide only around 2.2-3.2 s; fist on chest 0.2-3.2 s, at 3.7 s both hands are on the rail.")
