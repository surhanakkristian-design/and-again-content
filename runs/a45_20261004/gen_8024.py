from gen_8024_8025_8026_8029_lib import build
GW = [(.07,.29,.41,.60),(.13,.28,.35,.62),(.13,.28,.35,.63),(.11,.27,.37,.65),(.01,.26,.46,.70),(.03,.26,.43,.68),(.01,.25,.45,.70),(.03,.26,.44,.69)]
BL = [(.49,.30,.21,.48),(.49,.30,.21,.48),(.49,.30,.22,.47),(.49,.30,.24,.50),(.48,.27,.24,.48),(.47,.27,.25,.53),(.47,.26,.28,.58),(.48,.26,.28,.58)]
F='female'
build(8024,'B','to be honest',F,[
 ('to twirl in a tulle dress','the woman in the green dress',F,GW),
 ('to grin with excitement','the woman in the green dress',F,GW),
 ('to watch with folded arms','the blonde woman',F,BL)],
 2.7,[('a tulle dress',.30,.66,F),('a leather skirt',.64,.53,F),('pendant lamps',.22,.14,F),('trainers',.30,.88,F)],
 'What is the blonde woman doing?','She is watching with folded arms.',F,
 'Two targets only: the woman at the rail and the man behind are mostly hidden behind the two women, so the green-dress woman takes two phrases. Her swinging skirt overlaps the blonde woman; boxes split at x~.47-.49 (dress hem to the right of the split is cut). At 2.2 the skirt blur fills the bottom of the frame.')
