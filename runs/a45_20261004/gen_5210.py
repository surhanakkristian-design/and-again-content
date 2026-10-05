import json
from gen_5208_5209_5210_5211_lib import build
times=json.load(open("frames/5210/info.json"))["times"]
woman={0.0:(.18,.10,.47,.30),0.5:(.30,0,.46,.47),1.0:(.25,.02,.43,.36),1.5:(.27,.03,.40,.33),2.0:(.26,.06,.36,.32),
 2.5:(.30,.08,.32,.29),3.0:(.30,.09,.33,.30),3.5:(.40,.12,.30,.25),4.0:(.50,.15,.24,.24),4.5:(.53,.19,.24,.21),
 5.0:(.42,.24,.24,.18),5.5:(.45,.22,.20,.16),6.0:(.53,.16,.18,.17),6.5:(.58,.14,.18,.18),7.0:(.51,.11,.18,.17),
 7.5:(.52,.13,.18,.16),8.0:(.50,.16,.18,.17),8.5:(.51,.21,.18,.17),9.0:(.49,.28,.18,.16),9.5:(.52,.28,.18,.16),10.0:(.44,.29,.18,.16)}
goose={0.0:(.05,.40,.62,.60),0.5:(.10,.47,.60,.53),1.0:(.12,.38,.53,.62),1.5:(.20,.36,.57,.64),2.0:(.14,.38,.55,.62),
 2.5:(.18,.37,.48,.63),3.0:(0,.40,1,.56),3.5:(0,.38,1,.48),4.0:(0,.39,1,.27),4.5:(.24,.40,.76,.21),5.0:(.50,.42,.50,.17),
 5.5:(.36,.38,.44,.20),6.0:(.20,.36,.68,.27),6.5:(.10,.33,.74,.36),7.0:(.30,.30,.38,.53),7.5:(.34,.30,.36,.58),
 8.0:(.34,.35,.33,.44),8.5:(.33,.42,.35,.45),9.0:(.32,.49,.35,.48),9.5:(.31,.52,.36,.48),10.0:(.30,.60,.34,.40)}
build(5210,"B","retreat","female",[
 ("to spread its wings","the goose","female",goose),
 ("to clutch a sandwich","the woman in purple","female",woman),
 ("to take over the blanket","the goose","female",goose)],
 8.0,[("a pond",.15,.30,"female"),("a bench",.75,.34,"female"),("a goose",.50,.58,"female"),("sandwiches",.45,.90,"female")],
 "What are the friends doing?",["They","are","retreating","from","the","goose."],"female",
 "One continuous handheld shot. Woman in purple (lilac cardigan) holds a sandwich almost throughout; her box is cut off above the goose where the goose's neck/wings cover her (0-5.0). From 5.0 a fourth friend (dark hair, light-blue shirt) joins; the purple woman is small in the background from 5.5 on. defaultVoice female (mixed group, evenId true). Answer is about the group's retreat (2.0-6.0); at the end they stand watching.",times)
