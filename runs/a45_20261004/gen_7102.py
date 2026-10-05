from gen_7102_7110_7111_7116_lib import write
pork = [(.19,.40,.62,.17),(.18,.40,.62,.17),(.18,.39,.66,.19),(.16,.39,.69,.19),(.15,.37,.79,.22),(.12,.36,.77,.23),(.10,.35,.85,.25),(.08,.33,.86,.29)]
drip = [(.54,.57,.20,.16),(.52,.57,.21,.18),(.51,.58,.22,.19),(.49,.58,.27,.21),(.49,.59,.30,.24),(.49,.59,.32,.25),(.47,.60,.37,.28),(.46,.62,.40,.26)]
raw = [(0,.66,.33,.24),(0,.67,.29,.23),(0,.68,.32,.22),(0,.70,.31,.20),(0,.72,.30,.26),(0,.72,.30,.26),(0,.77,.26,.23),(0,.78,.22,.22)]
write(7102, "B", "fat", "female", [
  ("to sizzle in hot fat", "the pork in the pan", "female", pork),
  ("to drip onto the stove", "the dripping fat", "female", drip),
  ("to rest on a chopping board", "the raw pork", "female", raw)],
  0.2, [("fat", .61, .67, "female"), ("a cast-iron pan", .20, .53, "female"), ("wooden spoons", .43, .24, "female"), ("a cleaver", .17, .90, "female")],
  "What is dripping onto the stove?", "Melted fat is dripping onto the stove.", "female",
  "no people: defaultVoice from evenId; dripping-fat box covers the stream from the pan rim to the puddle")
