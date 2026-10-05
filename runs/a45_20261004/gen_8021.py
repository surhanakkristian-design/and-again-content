from gen_8019_8020_8021_8023_lib import build
woman = [(.31,.24,.18,.38),(.34,.20,.19,.43),(.33,.19,.19,.43),(.24,.20,.22,.43),(.24,.24,.24,.40),(.24,.24,.29,.41),(.27,.25,.24,.41),(.27,.25,.23,.41)]
man = [(.49,.32,.17,.53),(.53,.33,.20,.54),(.52,.28,.21,.60),(.46,.27,.25,.65),(.48,.26,.24,.68),(.53,.25,.21,.69),(.51,.27,.23,.66),(.50,.27,.23,.67)]
pigeon = [(.66,.25,.18,.14),(.58,.19,.18,.14),(.52,.12,.18,.16),(.30,.06,.18,.14),None,None,None,None]
build(8021, 'B', 'threshold', 'male',
 [('to step over the threshold', 'the man', 'male', man),
  ('to hold up a key', 'the woman', 'female', woman),
  ('to flap its wings', 'the pigeon', 'male', pigeon)],
 2.2,
 [('a light bulb', .52, .10, 'male'), ('a front door', .22, .72, 'male'), ('a flowerpot', .72, .71, 'male'), ('a threshold', .72, .80, 'male')],
 'What is the man doing?', 'He is carrying her over the threshold.', 'male',
 'The woman is in the man\'s arms, so the two boxes are split vertically between her head and his head: her box holds her raised arm, head and upper body, her legs over his arm fall in his box. The pigeon flies past only 0.2-1.7 s (at 1.2 s motion blur looks like two birds). Woman holds the key high 0.2-1.7 s, at shoulder height later. defaultVoice male: couple, evenId false.')
