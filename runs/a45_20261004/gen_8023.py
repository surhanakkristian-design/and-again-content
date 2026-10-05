from gen_8019_8020_8021_8023_lib import build
woman = [(.12,.25,.50,.49),(.15,.33,.57,.42),(.11,.35,.62,.42),(.10,.35,.62,.45),(.11,.33,.62,.45),(.06,.28,.70,.52),(.04,.28,.62,.50),(.08,.27,.66,.53)]
man = [(.62,.38,.37,.37),(.72,.39,.28,.36),(.73,.41,.27,.38),(.72,.42,.28,.40),(.73,.45,.27,.45),(.76,.41,.24,.38),(.66,.35,.34,.45),(.74,.44,.26,.40)]
build(8023, 'B', 'tightly', 'female',
 [('to kneel on the suitcase', 'the woman', 'female', woman),
  ('to tug at the zip', 'the man', 'male', man),
  ('to fall over backwards', 'the man', 'male', man)],
 0.2,
 [('a curtain', .22, .30, 'female'), ('a cat', .18, .51, 'female'), ('a suitcase', .35, .76, 'female'), ('a rug', .80, .88, 'female')],
 'What is the woman doing?', 'She is kneeling on the suitcase.', 'female',
 'Man and woman are close: their boxes are split vertically between her face and his head, so his hands on the zip (0.7-2.7 s) mostly fall inside her box. The cat and the curtain were not used as targets because they overlap the woman\'s box. He falls back onto the floor between 2.7 and 3.7 s.')
