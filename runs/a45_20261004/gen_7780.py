from gen_7777_7778_7779_7780_lib import write
G = [(.24,.22,.70,.34),(.24,.21,.56,.38),(.24,.21,.60,.37),(.25,.21,.60,.39),(.26,.20,.60,.41),(.27,.21,.60,.39),(.29,.22,.58,.40),(.34,.22,.55,.40)]
W = [(0,.45,.23,.55),(0,.45,.23,.55),(0,.46,.23,.54),(0,.46,.24,.54),(0,.46,.25,.54),(0,.45,.26,.55),(0,.45,.28,.55),(0,.45,.33,.55)]
H = [(.36,.57,.44,.25),(.32,.60,.48,.21),(.30,.59,.43,.22),(.37,.61,.43,.21),(.36,.62,.44,.21),(.33,.61,.45,.22),(.36,.63,.44,.21),(.38,.63,.42,.21)]
write(7780, "B", "close up", "female",
  [("to stick out its tongue", "the giraffe", "female", G),
   ("to lean on the railing", "the woman", "female", W),
   ("to hold out a twig", "the hands", "female", H)],
  2.2, [("clouds", .75, .12, "female"), ("a giraffe", .55, .32, "female"), ("a twig", .60, .59, "female"), ("a watch", .36, .78, "female")],
  "What is the giraffe doing?", "It is eating a leafy twig.", "female",
  "Hands = the viewer's (POV), gender unknown, default voice. Giraffe box = head only (neck runs behind the hands); its left ear is cut at x .24-.34 to keep clear of the woman's box. Woman box = her upper body; her lower body is behind the viewer's left sleeve. A ranger far in the background also stands at a fence, too small to compete. Key word 'close up' not a noun.")
