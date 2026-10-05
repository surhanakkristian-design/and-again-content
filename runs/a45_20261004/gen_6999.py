from gen_6997_6998_6999_7000_lib import build
w=[(0,.16,1,.84),(0,.18,1,.82),(0,.27,1,.73),(.18,.34,.65,.66),(.24,.39,.64,.61),(.14,.46,.66,.54),(.28,.52,.55,.48),(.28,.60,.54,.40)]
build(6999,"B","creator","female",[
 ("to cheer with raised arms","the woman","female",w),
 ("to turn towards the castle","the woman","female",w),
 ("to gaze up at the castle","the woman","female",w)],
 1.7,[("an ice castle",.50,.12,"female"),("a fur hat",.53,.40,"female"),("a crowd",.85,.50,"female"),("a barrier",.12,.63,"female")],
 "What is the woman looking up at?","She is gazing up at the ice castle.","female",
 "Only one clear target: the castle and the crowd lie behind the woman and would overlap her box, so all three phrases are on the woman. Key word 'creator' is not a visible noun (not placed). Chainsaw only half visible at the bottom edge at 0.2-0.7.")
