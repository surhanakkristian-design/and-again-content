from w_7482_7483_7488_7492_lib import build
Q=[(.36,.38,.40,.30),(.35,.37,.40,.30),(.34,.37,.40,.31),(.34,.36,.42,.29),(.32,.35,.44,.30),(.27,.35,.48,.30),(.30,.33,.48,.32),(.31,.32,.51,.32)]
H=[(.10,.78,.62,.22),(.08,.78,.70,.22),(.10,.78,.60,.22),(.10,.82,.58,.18),(.18,.84,.55,.16),(.18,.86,.60,.14),None,None]
build(7488,'A','queen','female',[
 ('to lay an egg','the queen','female',Q),
 ('to be bigger than the others','the queen','female',Q),
 ('to shine in the sun','the honey','female',H)],
 0.2,[('a queen',.62,.54,'female'),('an egg',.70,.64,'female'),('honey',.47,.81,'female')],
 'What is the queen doing?','She is laying an egg.','female',
 'workers are a crowd of identical bees, none trackable as its own target, so queen has two phrases; honey cells leave the bottom of the frame at 3.2 s (off); egg is already at her tip from frame one')
