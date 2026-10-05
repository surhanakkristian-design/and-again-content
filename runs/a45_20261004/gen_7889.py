from lib_7884_7887_7888_7889 import build
WO = [(.38,.57,.52,.28),(.41,.57,.49,.28),(.37,.60,.53,.25),(.36,.58,.55,.27),(.36,.51,.63,.34),(.40,.56,.60,.30),(.42,.64,.58,.25),(.39,.65,.61,.26)]
MH = [(.11,.44,.27,.32),(.11,.45,.29,.31),(.04,.45,.32,.31),(.02,.45,.33,.30),(0,.47,.34,.30),(.04,.50,.35,.27),(.05,.52,.36,.27),(.02,.53,.36,.26)]
K = [(.08,.18,.24,.16),(.15,.17,.24,.16),(.16,.22,.21,.14),(.14,.28,.20,.14),(.01,.28,.24,.17),(0,.22,.18,.20),(0,.14,.25,.20),(.08,.07,.23,.21)]
build(7889,'A','leisure','male',[
 ('to stretch her arms','the woman','female',WO),
 ('to swing in a hammock','the man in the hammock','male',MH),
 ('to fly in the sky','the kite','male',K)],
 3.2,[('a kite',.15,.19,'male'),('a tree',.62,.30,'male'),('a hammock',.35,.52,'male'),('a dog',.83,.92,'male')],
 'What is the woman doing?',['She','is','stretching','her','arms.'],'female',
 'Mixed group -> defaultVoice male (evenId false). Woman box starts right of the hammock man box, so her bare feet (x .2-.3) are outside; it also covers the man in the blue vest lying beside her (not a target), who seems to hold the kite string. The vest man raises one arm only; the woman stretches both arms (clearest 2.2-2.7).')
