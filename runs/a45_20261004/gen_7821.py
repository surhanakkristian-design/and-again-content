from lib_7820_7821_7823_7824 import *
wo=[(.31,.34,.87,.76),(.33,.34,.88,.76),(.32,.37,.79,.88),(.38,.33,.72,.81),(.40,.29,.71,.85),(.40,.29,.73,.89),(.38,.27,.74,.92),(.41,.25,.80,.99)]
bl=[(.14,.44,.31,.69),(.14,.44,.33,.69),(.13,.42,.32,.70),(.12,.42,.33,.69),(.10,.39,.32,.71),(.08,.47,.35,.75),(.02,.57,.37,.80),(.01,.58,.36,.84)]
save({"mediaId":7821,"level":"B","keyWord":"excel","defaultVoice":"female",
 "taps":[tap("to balance on one hand","the woman in red","female",wo),
         tap("to point at the camera","the woman in red","female",wo),
         tap("to bow down to the ground","the man in blue","male",bl)],
 "stillS":2.2,
 "nouns":[nn("a pillar",.12,.12,"female"),nn("a bomber jacket",.56,.45,"female"),nn("a speaker",.70,.62,"female"),nn("a bucket hat",.23,.81,"female")],
 "question":"What is the man in blue doing?",
 "answer":["He","is","bowing","down","to","the","ground."],
 "answerVoice":"male",
 "notes":"At 0.2-0.7 s the woman's left arm and head reach in front of the man in blue; her box is cut at his right edge (x 0.31-0.33). The man in blue leans forward in the crowd until 2.2 s, kneels at 2.7 s and bows to the ground at 3.2-3.7 s. She points at the camera only at 3.7 s. Key word 'excel' (verb) is not used in the texts."})
