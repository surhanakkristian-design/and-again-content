from gen_7131_7132_7134_7136_lib import write
woman=[(.27,.44,.38,.56),(.27,.43,.40,.57),(.27,.42,.40,.58),(.27,.41,.40,.59),(.22,.39,.42,.61),(.20,.36,.44,.64),(.17,.32,.45,.68),(.19,.28,.47,.72)]
torn=[(.20,.06,.42,.28)]*4+[(.20,.06,.42,.27),(.22,.06,.42,.26),(.22,.06,.42,.25),(.24,.06,.42,.21)]
left=[(0,.57,.26,.43)]*4+[(0,.54,.21,.46),(0,.54,.19,.46),None,None]
write(7132,"B","footage","female",[
 ("to show off her footage","the woman","female",woman),
 ("to loom over the fields","the tornado","female",torn),
 ("to point at the camera screen","the man on the left","male",left)],
 2.2,[("a tornado",.42,.22,"female"),("a pickup truck",.66,.41,"female"),("footage",.47,.64,"female"),("a raincoat",.34,.85,"female")],
 "What is the woman in yellow showing?","She is showing the tornado footage.","female",
 "Pointing man (dark hair, back to camera, left foreground) set off at 3.2/3.7: he is squeezed to the left edge behind the orange-hood man and overlaps the woman's coat. 'footage' pill sits on the flip-out screen showing the recorded tornado.")
