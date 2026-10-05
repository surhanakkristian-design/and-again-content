from gen_8019_8020_8021_8023_lib import build
woman = [(.31,.27,.36,.53),(.33,.27,.43,.52),(.38,.30,.43,.47),(.35,.27,.40,.52),(.38,.27,.36,.55),(.37,.27,.39,.55),(.38,.28,.35,.57),(.38,.26,.43,.56)]
man = [(.67,.29,.27,.43),(.76,.28,.24,.45),(.81,.30,.19,.42),(.75,.28,.25,.46),(.74,.28,.26,.48),(.76,.28,.24,.48),(.73,.29,.27,.48),(.81,.28,.19,.48)]
baker = [(0,.20,.27,.31)]*8
build(8020, 'B', 'temptation', 'female',
 [('to lean towards the cake', 'the woman in lilac', 'female', woman),
  ('to drag her away', 'the man in navy', 'male', man),
  ('to hold out a slice', 'the baker', 'male', baker)],
 2.2,
 [('an awning', .78, .22, 'female'), ('a street lamp', .51, .12, 'female'), ('a chocolate cake', .23, .53, 'female'), ('pastries', .25, .70, 'female')],
 'What is the woman in lilac doing?', 'She is leaning towards the chocolate cake.', 'female',
 'Woman and man hold hands, so their boxes are split at the joined hands; at 3.2 s their feet touch, split there too. The woman in the yellow coat behind them is not a target. Baker box covers head, arm and the slice above the glass counter.')
