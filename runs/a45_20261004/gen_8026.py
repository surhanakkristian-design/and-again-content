from gen_8024_8025_8026_8029_lib import build
BM = [(.21,.21,.44,.78),(.21,.21,.45,.79),(.21,.21,.45,.79),(.22,.21,.45,.79),(.23,.19,.46,.81),(.21,.19,.51,.81),(.21,.19,.49,.81),(.21,.19,.50,.81)]
OM = [(.66,.45,.16,.20),(.67,.46,.16,.20),(.67,.47,.16,.20),(.68,.48,.15,.20),(.70,.48,.14,.22),(.73,.37,.13,.34),(.71,.32,.15,.39),(.72,.32,.14,.39)]
M='male'
build(8026,'A','tonight',M,[
 ('to take a selfie','the man in the blue shirt',M,BM),
 ('to touch his collar','the man in the blue shirt',M,BM),
 ('to tie his shoes','the man by the door',M,OM)],
 0.2,[('a lamp',.23,.25,M),('a window',.70,.21,M),('a phone',.56,.34,M),('a bottle',.18,.62,M)],
 'What is the man in blue doing?','He is taking a selfie.',M,
 'Blue-shirt man takes two phrases (the lamp box would overlap his head/shoulders). The man by the door ties his shoes 0.2-2.2, stands up from 2.7; his box is split from the selfie arm at x .65-.72, so his back edge is cut a little. Collar touch is at 0.2-0.7 only.')
