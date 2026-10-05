from gen_8024_8025_8026_8029_lib import build
W = [(.12,.27,.58,.62),(.12,.27,.58,.62),(.11,.27,.59,.62),(.11,.27,.59,.62),(.10,.27,.63,.63),(.10,.27,.63,.64),(.10,.29,.61,.64),(.10,.29,.63,.64)]
C = [(.71,.50,.24,.15),(.71,.50,.25,.15),(.71,.51,.25,.14),(.72,.51,.26,.15),(.74,.51,.24,.14),(.74,.51,.25,.15),(.74,.51,.25,.14),(.74,.52,.26,.14)]
F='female'
build(8025,'A','tomorrow',F,[
 ('to hold a small clock','the woman',F,W),
 ('to put the clock down','the woman',F,W),
 ('to sleep on the bed','the cat',F,C)],
 3.7,[('a window',.40,.12,F),('a lamp',.86,.38,F),('a cat',.86,.58,F),('a clock',.36,.56,F)],
 'What is the woman doing?','She is holding a small clock.',F,
 'Only two living targets (woman, cat); the woman takes two phrases. She holds/winds the clock 0.2-2.2 and has put it down by 2.7 (it stands next to her). Question asked about the main part of the clip (0.2-2.2); at the end she clenches her fists.')
