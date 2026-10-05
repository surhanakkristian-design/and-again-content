from gen_5575_5576_5578_5579_lib import *
wom=B([(0.22,0.07,0.88,0.38),(0.23,0.02,0.78,0.38),(0.22,0.01,0.86,0.38),(0.08,0.03,0.86,0.37),
       (0.06,0.04,0.63,0.33),(0.07,0.05,0.61,0.33),(0.18,0.02,0.61,0.42),(0.18,0.01,0.58,0.43)])
man=B([(0.27,0.38,0.79,0.86),(0.28,0.38,0.80,0.88),(0.31,0.38,0.83,0.93),(0.32,0.37,0.86,0.99),
       (0.40,0.33,0.82,1.00),(0.42,0.33,0.75,1.00),(0.46,0.42,0.88,1.00),(0.44,0.43,0.86,1.00)])
rop=B([(0.04,0.28,0.22,0.55),(0.04,0.32,0.23,0.57),(0.10,0.38,0.30,0.62),(0.14,0.42,0.32,0.67),
       (0.17,0.47,0.36,0.73),(0.19,0.50,0.39,0.78),(0.23,0.52,0.43,0.81),(0.24,0.52,0.43,0.81)])
write(5579,{"mediaId":5579,"level":"B","keyWord":"assistance","defaultVoice":"male",
 "taps":[{"phrase":"to scramble onto the wall","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to give her a boost","target":"the man","voice":"male","keys":man},
         {"phrase":"to hang in loose coils","target":"the rope","voice":"male","keys":rop}],
 "stillS":3.7,
 "nouns":[{"word":"a stone wall","x":0.78,"y":0.18,"voice":"male"},{"word":"a rope","x":0.34,"y":0.67,"voice":"male"},
          {"word":"a wooden door","x":0.86,"y":0.82,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","giving","her","a","boost."],"answerVoice":"male",
 "notes":"Key word 'assistance' (abstract) not placed. Woman and man boxes split horizontally at the man's head (0.2-1.7) / at his hands (2.2-2.7): the woman's lower legs and the boot he holds fall in the man's box. The boost is shown 0.2-2.7; at 3.2-3.7 he only looks up at her. Rope = the coil hanging on the wall; its loose end on the ground is outside the box."})
