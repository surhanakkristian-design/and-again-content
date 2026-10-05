from gen_5648_5649_5650_5651_lib import *
bar=K([(0.38,0.23,0.31,0.75),(0.39,0.23,0.30,0.76),(0.33,0.22,0.36,0.77),(0.33,0.22,0.36,0.77),
       (0.28,0.21,0.40,0.79),(0.27,0.21,0.37,0.79),(0.24,0.20,0.38,0.80),(0.26,0.20,0.40,0.80)])
man=K([(0.69,0.32,0.26,0.38),(0.69,0.30,0.29,0.40),(0.69,0.30,0.29,0.40),(0.69,0.30,0.29,0.40),
       (0.69,0.29,0.29,0.42),(0.64,0.29,0.34,0.43),(0.62,0.27,0.36,0.45),(0.66,0.27,0.32,0.45)])
cat=K([(0.69,0.18,0.19,0.14),(0.69,0.16,0.19,0.14),(0.69,0.16,0.19,0.14),(0.69,0.16,0.19,0.14),
       (0.68,0.15,0.19,0.14),(0.67,0.14,0.19,0.14),(0.66,0.13,0.20,0.14),(0.66,0.13,0.19,0.14)])
write(5651,{"mediaId":5651,"level":"A","keyWord":"better","defaultVoice":"female",
 "taps":[{"phrase":"to hold a comb","target":"the barber","voice":"female","keys":bar},
         {"phrase":"to look very surprised","target":"the man on the right","voice":"male","keys":man},
         {"phrase":"to sleep by the window","target":"the cat","voice":"female","keys":cat}],
 "stillS":0.2,
 "nouns":[{"word":"a shelf","x":0.30,"y":0.15,"voice":"female"},{"word":"a cat","x":0.78,"y":0.28,"voice":"female"},
          {"word":"a comb","x":0.62,"y":0.38,"voice":"female"},{"word":"hair","x":0.82,"y":0.87,"voice":"female"}],
 "question":"What is the cat doing?",
 "answer":["It","is","sleeping","by","the","window."],"answerVoice":"female",
 "notes":"Key word 'better' (adjective) not placed. The barber's hand on the right man's chin (0.2-1.7) falls in his box (split at x 0.69). Both men touch their hair at some point (left man 1.2-2.2, right man 2.7-3.7), so no 'touch his hair' phrase; the left man is not a target. The right man looks shocked mostly from 1.2 on (at 0.2-0.7 only mildly). Cat box made 0.14 high, mostly sky/window above the cat, so it does not touch the right man's box. 'hair' = the cut hair on the floor. Two lamps, so no lamp noun."})
