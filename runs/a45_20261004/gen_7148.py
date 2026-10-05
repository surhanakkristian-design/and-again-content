from lib_7147_7148_7149_7150 import build
woman = [(.12,.33,.51,.77),(.16,.32,.51,.78),(.21,.33,.51,.79),(.26,.31,.55,.79),
         (.17,.28,.56,.81),(.05,.26,.51,.85),(0,.23,.51,.87),(0,.24,.53,.90)]
dog = [(.51,.56,.70,.70),(.51,.56,.75,.70),(.51,.56,.70,.70),(.55,.56,.74,.70),
       (.56,.54,.75,.68),(.51,.54,.70,.68),(.51,.54,.70,.68),(.54,.54,.73,.68)]
build(7148,'B','gallery','female',[
 ('to roller-skate along the porch','the woman','female',woman),
 ('to spread her arms wide','the woman','female',woman),
 ('to lie on the floorboards','the dog','female',dog)],
 2.7,[('a ceiling fan',.45,.25,'female'),('a fern',.83,.38,'female'),('a dog',.60,.63,'female'),('a gallery',.50,.90,'female')],
 'What is the woman doing?','She is roller-skating along the porch.','female',
 'Key word gallery = the long covered porch; its pill sits on the wet floorboards in the foreground. The dog lies behind the woman between her legs/right hand; woman and dog boxes are split vertically, so her right hand is outside her box in most frames. A second person stands far back in the doorway (tiny, not a target).')
