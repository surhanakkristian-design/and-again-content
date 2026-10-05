from gen_7102_7110_7111_7116_lib import write
man = [(.24,.28,.42,.31),(.34,.31,.36,.27),(.31,.29,.34,.28),(.26,.29,.40,.30),(.15,.27,.48,.28),(.30,.26,.45,.29),(.29,.26,.35,.33),(.04,.26,.62,.29)]
dog = [(.50,.82,.23,.18),(.55,.81,.21,.19),(.54,.80,.22,.20),(.58,.80,.20,.20),(.58,.79,.22,.21),(.60,.79,.21,.21),(.61,.78,.22,.22),(.65,.78,.22,.22)]
write(7110, "B", "fight off", "male", [
  ("to fight off the women", "the man", "male", man),
  ("to kneel on the bed", "the man", "male", man),
  ("to gaze up from the floor", "the dog", "male", dog)],
  0.2, [("a headboard", .58, .12, "male"), ("a bedside lamp", .11, .14, "male"), ("fairy lights", .22, .59, "male"), ("a dog", .62, .90, "male")],
  "What is the man doing?", "He is fighting off the women with pillows.", "male",
  "busy pillow fight; women move a lot, so two phrases use the man; dog is the only clear third target")
