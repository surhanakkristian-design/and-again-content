from gen_5575_5576_5578_5579_lib import *
wom=B([(0.00,0.14,0.52,0.84),(0.00,0.13,0.52,0.83),(0.03,0.14,0.53,0.80),(0.09,0.14,0.55,0.79),
       (0.13,0.14,0.51,0.74),(0.16,0.18,0.56,0.75),(0.10,0.38,0.58,0.73),(0.14,0.32,0.57,0.72)])
man=B([(0.52,0.09,1.00,0.99),(0.52,0.09,1.00,1.00),(0.58,0.10,1.00,1.00),(0.60,0.10,1.00,0.99),
       (0.51,0.10,1.00,0.94),(0.59,0.10,1.00,0.91),(0.59,0.11,1.00,0.89),(0.59,0.11,0.98,0.86)])
write(5578,{"mediaId":5578,"level":"B","keyWord":"assignment","defaultVoice":"female",
 "taps":[{"phrase":"to salute with a pout","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to hand her a peeler","target":"the man","voice":"male","keys":man},
         {"phrase":"to crouch beside the sacks","target":"the woman","voice":"female","keys":wom}],
 "stillS":2.7,
 "nouns":[{"word":"tents","x":0.20,"y":0.19,"voice":"female"},{"word":"a cooking pot","x":0.62,"y":0.37,"voice":"female"},
          {"word":"potatoes","x":0.30,"y":0.80,"voice":"female"}],
 "question":"What is the man handing her?",
 "answer":["He","is","handing","her","a","potato","peeler."],"answerVoice":"male",
 "notes":"Key word 'assignment' (abstract) not placed. Only two people, so the woman carries two phrases (salute at 0.2-0.7, crouch at 3.2-3.7). The peeler hand-over is at 0.2-0.7; boxes split at x 0.52 through the hands. 'potatoes' and the sacks are one place, so no 'a sack' noun."})
