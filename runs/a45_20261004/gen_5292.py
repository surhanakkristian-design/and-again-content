from lib_5290_5291_5292_5293 import write
O = {0.0:(.08,.25,.74,.48),0.5:(.09,.23,.77,.50),1.0:(.11,.23,.77,.50),1.5:(.09,.24,.77,.49),
     2.0:(.06,.29,.78,.44),2.5:(.03,.45,.81,.29),3.0:(0,.45,.80,.29)}
S = {5.0:(0,.22,1,.44),5.5:(0,.22,1,.44)}
F = {t:(0,.25,1,.39) for t in (7.5,8.0,8.5,9.0,9.5,10.0)}
write(5292, {"mediaId":5292,"level":"B","keyWord":"productive","defaultVoice":"male",
 "taps":[{"phrase":"to slump onto his keyboard","target":"the man at the computer","voice":"male","boxes":O},
         {"phrase":"to drool on an open book","target":"the student","voice":"male","boxes":S},
         {"phrase":"to sprawl on the sofa","target":"the man on the sofa","voice":"male","boxes":F}],
 "stillS":8.0,
 "nouns":[{"word":"a sofa","x":.15,"y":.64,"voice":"male"},
          {"word":"an alarm clock","x":.80,"y":.62,"voice":"male"},
          {"word":"a smartphone","x":.78,"y":.79,"voice":"male"},
          {"word":"a coffee table","x":.82,"y":.88,"voice":"male"}],
 "question":"What is the office worker doing?",
 "answer":["He","is","dozing","off","at","his","desk."],
 "answerVoice":"male",
 "notes":"Montage, one target per shot: office man 0.0-3.0, student in the library 5.0-5.5 (a drop of drool on the book), man on the sofa 7.5-10.0. The train shot (3.5-4.5, woman asleep on a young man's shoulder) and the park-bench sleeper (6.0-7.0, gender unclear) are not used. defaultVoice male: all main sleepers except the train woman are men. Student box also covers part of the book under his face."})
