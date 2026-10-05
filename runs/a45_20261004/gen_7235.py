from gen_7235_7237_7240_7241_lib import write
W = [(.21,.25,.50,.73),(.26,.26,.53,.73),(.31,.29,.60,.76),(.31,.28,.60,.84),(.28,.32,.67,.87),(.31,.31,.68,.87),(.30,.36,.67,.87),(.33,.33,.66,.86)]
D = [(.50,.45,.68,.62),(.53,.46,.72,.62),(.60,.49,.80,.68),(.61,.54,.82,.71),(.68,.52,.87,.73),(.69,.57,.97,.83),(.69,.61,.93,.85),(.67,.61,.97,.85)]
B = [(.70,.39,.97,.63),(.76,.34,1.0,.54),(.66,.16,.90,.45),(.60,.07,.92,.30),(.69,.0,.95,.27),(.60,.0,.86,.27),(.55,.04,.77,.30),(.55,.10,.79,.33)]
write(7235, "B", "hunt", "female",
  [("to chase a runaway balloon", "the woman", "female", W),
   ("to race beside the woman", "the dog", "female", D),
   ("to drift into the sky", "the red balloon", "female", B)],
  2.2,
  [("a balloon", .79, .09, "female"), ("a quad bike", .15, .47, "female"), ("a sheepdog", .76, .63, "female"), ("heather", .40, .90, "female")],
  "What is the woman doing?", "She is chasing a runaway balloon.", "female",
  "Woman and dog overlap at 0.2-1.7 s (dog runs just behind her legs): split boxes, woman's reaching arm partly outside her box at 0.2/0.7. Balloon's hanging can partly cut at 0.2 where her hand reaches it. 'the dog' = the sheepdog; the man on the quad bike is far and small, not a target. Key word 'hunt' is a verb, not placed.")
