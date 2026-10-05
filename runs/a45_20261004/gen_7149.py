from lib_7147_7148_7149_7150 import build
att = [(.66,.50,.92,.78)]*7 + [(.68,.50,.88,.79)]
woman = [(.07,.49,.27,.73),(.07,.49,.28,.75),(.07,.49,.27,.76),(.07,.50,.25,.78),
         (.10,.50,.29,.79),(.10,.50,.31,.80),(.07,.50,.32,.84),(.06,.52,.33,.88)]
car = [(.28,.55,.66,.79),(.29,.55,.66,.79),(.28,.55,.66,.80),(.26,.55,.66,.80),
       (.30,.55,.66,.80),(.31,.55,.66,.81),(.32,.55,.66,.82),(.33,.55,.68,.82)]
build(7149,'B','gas station','male',[
 ('to refuel a muddy car','the attendant','male',att),
 ('to take off her helmet','the woman','female',woman),
 ('to be caked in mud','the rally car','male',car)],
 1.2,[('a gas station',.60,.10,'male'),('a dust storm',.25,.22,'male'),('a rally car',.50,.66,'male'),('a tumbleweed',.78,.90,'male')],
 'What is the attendant doing?','He is refueling a muddy rally car.','male',
 'Attendant holds the nozzle in the car with his left hand and stretches his right arm towards the pump (the description says he points at the queue; not clear in frames, so not used). The woman driver wears her helmet at 0.2-1.2 (taking it off, face hidden), carries it from 1.7. The second driver keeps the helmet on throughout, so the helmet phrase is unique. Third target is the rally car (a state, no action fits a thing only it does; the queue cars are clean). Two tumbleweeds (big one front right, small one at the left by the woman\'s feet): the tumbleweed pill sits on the big one, no noun on the small one. US spelling refueling (gas station).')
