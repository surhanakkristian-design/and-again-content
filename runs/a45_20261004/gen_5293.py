from lib_5290_5291_5292_5293 import write
R = {0.5:(0,.06,.87,.43),1.0:(0,.06,.93,.45),1.5:(0,0,.40,.62),2.0:(0,.03,1,.60),
     3.5:(0,.29,.55,.33),4.0:(0,.38,1,.22),4.5:(0,.32,1,.27),5.0:(0,.36,1,.25),
     6.0:(0,.33,1,.40),6.5:(0,.37,1,.37),7.0:(0,.23,1,.52),7.5:(0,.20,1,.56),8.0:(0,.27,1,.46)}
F = {0.0:(0,.08,.25,.40),2.5:(0,.27,.38,.31),5.5:(.12,.29,.62,.40)}
C = {1.5:(.41,.08,.50,.30)}
write(5293, {"mediaId":5293,"level":"A","keyWord":"glove","defaultVoice":"male",
 "taps":[{"phrase":"to slide in the dirt","target":"the runner","voice":"male","boxes":R},
         {"phrase":"to bend down low","target":"the fielder","voice":"male","boxes":F},
         {"phrase":"to wear a face mask","target":"the catcher","voice":"male","boxes":C}],
 "stillS":5.5,
 "nouns":[{"word":"a wall","x":.35,"y":.20,"voice":"male"},
          {"word":"a cap","x":.62,"y":.33,"voice":"male"},
          {"word":"a glove","x":.68,"y":.55,"voice":"male"},
          {"word":"grass","x":.22,"y":.82,"voice":"male"}],
 "question":"What is the runner doing?",
 "answer":["He","is","sliding","in","the","dirt."],
 "answerVoice":"male",
 "notes":"Many short shots with different players; 'the runner' = the player sliding/diving in each shot (0.5-2.0, 3.5-5.0, 6.0-8.0). 3.0 is OFF for all: a player with a mitt dives in a dust cloud (could be the fielder), so no target there. The fielder is crouched/bent at 0.0, 2.5, 5.5. The catcher (face mask) is clearly visible only at 1.5 (one frame; at 1.0/7.5/8.0 only his mitt or mask edge shows, left OFF). Umpire at 2.5 not used."})
