from w_7403_7406_7407_7408_lib import build
man = [(.32,.30,.45,.47),(.31,.30,.46,.47),(.30,.30,.48,.48),(.29,.30,.50,.48),(.24,.30,.54,.49),(.22,.30,.57,.49),(.14,.30,.64,.49),(.56,.22,.40,.63)]
cool = [(.78,.37,.21,.27),(.78,.37,.21,.27),(.79,.38,.21,.28),(.80,.39,.20,.27),(.79,.39,.21,.26),(.80,.40,.20,.25),(.79,.40,.21,.27),None]
fla = [(.12,.26,.19,.28),(.12,.26,.19,.28),(.11,.26,.19,.30),(.10,.26,.19,.30),(.05,.25,.19,.30),(.03,.24,.19,.31),None,None]
build(7403,'B','pack','male',[
 ('to force the van door shut','the man in sunglasses','male',man),
 ('to perch on a cooler','the man on the cooler','male',cool),
 ('to stick out of the van','the pink flamingo','male',fla)],
 0.2,[('surfboards',.28,.15,'male'),('a frisbee',.47,.73,'male'),('a beach ball',.70,.84,'male'),('a cooler',.86,.57,'male')],
 'What is the man in sunglasses doing?','He is forcing the van door shut.','male',
 'Key word pack (verb) not a visible noun. Cooler man covers his face from 2.2, mostly out of frame at 3.7 (off). Flamingo hidden by the closing door from 3.2 (off). Main man box cut at its right edge where his back foot reaches past the cooler man (split at x .78). Cooler pill sits on the cooler under the sitting man.')
