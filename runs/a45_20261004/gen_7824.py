from lib_7820_7821_7823_7824 import *
wo=[(.19,.41,.58,.83),(.14,.43,.58,.84),(.11,.42,.60,.86),(.07,.44,.56,.87),(.06,.44,.54,.89),(.03,.43,.58,.89),(0,.43,.53,.89),(0,.43,.55,.88)]
mn=[(.58,.24,.97,.60),(.58,.26,.96,.62),(.60,.25,.91,.65),(.56,.28,.95,.63),(.54,.28,.95,.67),(.58,.28,.98,.69),(.53,.29,1.0,.69),(.55,.29,.99,.67)]
save({"mediaId":7824,"level":"B","keyWord":"faster","defaultVoice":"female",
 "taps":[tap("to crouch low on her board","the woman","female",wo),
         tap("to race ahead of him","the woman","female",wo),
         tap("to stretch out his arms","the man","male",mn)],
 "stillS":2.7,
 "nouns":[nn("the sky",.20,.06,"female"),nn("a dune",.55,.22,"female"),nn("a tree",.41,.44,"female"),nn("a sandboard",.22,.84,"female")],
 "question":"Who is going faster?",
 "answer":["The","woman","is","going","faster","than","the","man."],
 "answerVoice":"female",
 "notes":"The two riders overlap in the picture (her hips and his legs/board), so the boxes are split along a vertical line between them (x 0.53-0.60): the man's left arm and the left part of his shirt fall outside his box, and the woman's hips are partly cut at 1.7-2.2 s. 'faster' is judged from the picture: she is in front, low and spraying sand, he rides upright behind her. The four-wheel-drive car below is too small and close to her head for a noun slot."})
