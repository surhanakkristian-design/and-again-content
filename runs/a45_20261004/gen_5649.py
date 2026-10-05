from gen_5648_5649_5650_5651_lib import *
mid=K([(0.36,0.11,0.28,0.57),(0.36,0.11,0.29,0.57),(0.36,0.11,0.28,0.58),(0.36,0.11,0.29,0.58),
       (0.35,0.10,0.29,0.61),(0.35,0.12,0.29,0.62),(0.35,0.15,0.30,0.59),(0.38,0.09,0.28,0.66)])
blu=K([(0.18,0.36,0.18,0.36),(0.17,0.36,0.19,0.37),(0.16,0.37,0.20,0.38),(0.14,0.37,0.22,0.38),
       (0.13,0.38,0.22,0.39),(0.10,0.38,0.25,0.41),(0.10,0.38,0.25,0.43),(0.11,0.39,0.27,0.44)])
wom=K([(0.64,0.41,0.27,0.36),(0.65,0.42,0.26,0.38),(0.64,0.42,0.27,0.39),(0.65,0.44,0.29,0.40),
       (0.64,0.46,0.29,0.40),(0.64,0.44,0.31,0.44),(0.65,0.44,0.30,0.46),(0.66,0.44,0.29,0.46)])
write(5649,{"mediaId":5649,"level":"A","keyWord":"best","defaultVoice":"male",
 "taps":[{"phrase":"to hold up a skateboard","target":"the man in the middle","voice":"male","keys":mid},
         {"phrase":"to clap his hands","target":"the man in blue","voice":"male","keys":blu},
         {"phrase":"to touch his leg","target":"the woman","voice":"female","keys":wom}],
 "stillS":0.2,
 "nouns":[{"word":"the sky","x":0.50,"y":0.06,"voice":"male"},{"word":"palm trees","x":0.86,"y":0.39,"voice":"male"},
          {"word":"a bottle","x":0.58,"y":0.86,"voice":"male"}],
 "question":"What is the man in blue doing?",
 "answer":["He","is","clapping","his","hands."],"answerVoice":"male",
 "notes":"Key word 'best' (adjective) not a noun, not placed. The woman's hands touch the middle man's thigh and the man in blue stands close: middle box split at x~0.36 (left) and ~0.64 (right), so the raised fist / skateboard tip are cut a little. At 3.7 the man in blue puts a hand on the winner instead of clapping (he claps 0.2-3.2). Skateboards not used as a noun (three of them)."})
