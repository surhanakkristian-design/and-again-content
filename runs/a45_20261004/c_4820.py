from gen_4816_4818_4820_4821 import *
T=[i*0.5 for i in range(25)]
B={0.0:(0.05,0.23,0.94,0.77),0.5:(0,0.13,0.74,0.87),1.0:(0,0.12,0.47,0.88),1.5:(0,0.11,0.49,0.89),2.0:(0,0.03,0.37,0.97),2.5:(0,0.03,0.35,0.97),
3.0:(0,0.06,0.78,0.94),3.5:(0,0.04,0.78,0.96),4.0:(0,0.04,0.76,0.96),4.5:(0,0.03,0.30,0.97),5.0:(0,0.03,0.30,0.97),5.5:(0.02,0.03,0.85,0.97),
6.0:(0,0.03,0.87,0.97),6.5:(0,0.03,0.87,0.97),7.0:(0,0.04,0.87,0.96),7.5:(0,0.03,0.86,0.97),8.0:(0.03,0.02,0.83,0.98),8.5:(0,0.02,0.30,0.98),
9.0:(0,0.08,0.22,0.92),9.5:(0,0.10,0.27,0.90),10.0:(0,0.11,0.42,0.89),10.5:(0,0.10,0.42,0.90),11.0:(0,0.10,0.36,0.90),11.5:(0,0.10,0.34,0.90),12.0:(0,0.11,0.29,0.89)}
D={0.5:(0.74,0.16,0.26,0.84),1.0:(0.48,0.12,0.52,0.88),1.5:(0.50,0.11,0.50,0.89),2.0:(0.55,0.05,0.45,0.95),2.5:(0.58,0.06,0.42,0.94),
3.0:(0.78,0,0.22,1),3.5:(0.78,0,0.22,1),4.0:(0.76,0,0.24,1),4.5:(0.30,0.10,0.70,0.90),5.0:(0.30,0.10,0.70,0.90),5.5:(0.87,0.08,0.13,0.92),
6.0:(0.87,0.05,0.13,0.95),6.5:(0.87,0.05,0.13,0.95),7.0:(0.87,0.05,0.13,0.95),7.5:(0.86,0.05,0.14,0.95),8.0:(0.86,0,0.14,1),
8.5:(0.30,0.10,0.70,0.90),9.0:(0.22,0.08,0.71,0.92),9.5:(0.27,0.10,0.73,0.90),10.0:(0.42,0.10,0.58,0.90),10.5:(0.42,0.09,0.58,0.91),
11.0:(0.36,0.09,0.64,0.91),11.5:(0.34,0.07,0.66,0.93),12.0:(0.29,0.09,0.71,0.91)}
write({"mediaId":4820,"level":"A","keyWord":"same","defaultVoice":"female",
"taps":[{"phrase":"to shout at her friend","target":"the blonde woman","voice":"female","keys":K(T,B)},
{"phrase":"to cry and laugh","target":"the dark-haired woman","voice":"female","keys":K(T,D)},
{"phrase":"to smile at her friend","target":"the blonde woman","voice":"female","keys":K(T,B)}],
"stillS":6.0,
"nouns":[{"word":"hair","x":0.22,"y":0.55,"voice":"female"},{"word":"a dress","x":0.48,"y":0.72,"voice":"female"},
{"word":"a bracelet","x":0.84,"y":0.92,"voice":"female"},{"word":"a pink light","x":0.78,"y":0.17,"voice":"female"}],
"question":"What are the two women doing?","answer":["They","are","hugging","each","other."],"answerVoice":"female",
"notes":"Question has no time word (8-word limit); the hug is the last and longest action (8.5-12.0). Only two people, so the blonde woman takes two phrases (shout 3.0-4.0, smile 5.5-8.0). Key word 'same' is an adjective, no noun slot. From 5.5 to 8.0 the dark-haired woman is only a thin strip (hair/shoulder) at the right edge; boxes there are 0.13-0.14 wide. In the hug (8.5-12.0) the bodies overlap; boxes split at the line between the blonde's head/hair and the dark-haired woman's face. 'a pink light' = the pink neon tube top right at 6.0."})
