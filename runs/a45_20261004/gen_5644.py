from gen_5644_5645_5646_5647_lib import write
man = [(.43,.34,.26,.38),(.43,.33,.26,.39),(.42,.35,.24,.38),(.43,.33,.23,.41),(.42,.33,.24,.41),(.42,.37,.24,.41),(.42,.44,.22,.37),(.42,.46,.22,.37)]
wom = [(.19,.54,.24,.34),(.19,.55,.24,.34),(.19,.55,.23,.35),(.19,.56,.24,.36),(.18,.57,.24,.36),(.18,.59,.24,.37),(.18,.64,.24,.34),(.18,.63,.24,.36)]
write(5644, "B", "beginning", "male",
 [("to paint a bold blue stripe", "the man", "male", man),
  ("to steady the ladder", "the woman", "female", wom),
  ("to gaze up at him", "the woman", "female", wom)],
 3.2,
 [("the sky", .25, .10, "male"), ("a paint roller", .78, .21, "male"), ("a stripe", .82, .40, "male"), ("a ladder", .48, .85, "male")],
 "What is the man doing?", "He is painting a bold blue stripe.", "male",
 "Man and woman boxes split at x=.42-.43 where her hand touches the ladder near his feet. Key word 'beginning' is abstract, not placed as a noun.")
