from gen_5575_5576_5578_5579_lib import *
red=B([(0.19,0.25,0.63,0.59),(0.24,0.29,0.65,0.62),(0.44,0.42,0.64,0.79),(0.42,0.40,0.64,0.79),
       (0.41,0.38,0.62,0.77),(0.41,0.37,0.61,0.75),(0.39,0.38,0.64,0.73),(0.40,0.36,0.67,0.72)])
blu=B([(0.03,0.60,0.66,0.86),(0.04,0.62,0.66,0.85),(0.04,0.55,0.44,0.83),(0.05,0.55,0.42,0.83),
       (0.10,0.54,0.41,0.80),(0.12,0.54,0.41,0.79),(0.14,0.54,0.39,0.80),(0.14,0.54,0.40,0.80)])
man=B([(0.67,0.43,0.98,0.87),(0.67,0.43,0.97,0.86),(0.65,0.42,0.93,0.85),(0.66,0.43,0.96,0.83),
       (0.63,0.42,0.98,0.81),(0.62,0.40,0.94,0.80),(0.66,0.42,0.94,0.79),(0.68,0.43,0.96,0.79)])
write(5576,{"mediaId":5576,"level":"B","keyWord":"assault","defaultVoice":"female",
 "taps":[{"phrase":"to raise her arms triumphantly","target":"the woman in red","voice":"female","keys":red},
         {"phrase":"to sprawl in the snow","target":"the woman in blue","voice":"female","keys":blu},
         {"phrase":"to clutch a snowball","target":"the man in blue","voice":"male","keys":man}],
 "stillS":3.7,
 "nouns":[{"word":"the sky","x":0.30,"y":0.10,"voice":"female"},{"word":"pine trees","x":0.84,"y":0.30,"voice":"female"},
          {"word":"a snowsuit","x":0.53,"y":0.56,"voice":"female"},{"word":"a snowman","x":0.54,"y":0.73,"voice":"female"}],
 "question":"What is the woman in blue doing?",
 "answer":["She","is","sprawling","in","the","snow."],"answerVoice":"female",
 "notes":"Key word 'assault' (abstract) not placed as a noun. The woman in red raises her arms in triumph only at 3.2-3.7 (earlier she jumps and lands). The man in blue holds a snowball clearly at 0.7-1.7; later his hands are less clear. The woman in red's legs overlap the woman in blue's legs; boxes split vertically (woman in blue = head and torso side) from 1.2 on, horizontally at 0.2-0.7. The bearded man in red is not a target; he overlaps the man in blue's box at 2.2-3.2."})
