from gen_4816_4818_4820_4821 import *
T=[i*0.5 for i in range(19)]
W={0.0:(0,0.10,0.68,0.90),0.5:(0,0.07,0.86,0.93),1.0:(0,0.04,1,0.96),1.5:(0,0.03,0.92,0.97),2.0:(0,0.02,0.88,0.98),2.5:(0,0.02,1,0.98),
3.0:(0,0.03,0.66,0.97),3.5:(0,0.03,0.70,0.97),4.0:(0,0.03,0.48,0.97),4.5:(0,0,0.47,1),5.0:(0,0.02,0.48,0.98),5.5:(0,0.02,0.47,0.98),
6.0:(0,0.02,0.62,0.98),6.5:(0,0,0.55,1),7.0:(0,0,0.44,1),7.5:(0,0,0.41,1),8.0:(0,0,0.48,1),8.5:(0,0,0.49,1),9.0:(0,0,0.45,1)}
M={0.0:(0.82,0.42,0.18,0.29),3.0:(0.66,0.32,0.32,0.68),3.5:(0.70,0.30,0.30,0.70),4.0:(0.48,0.22,0.52,0.78),4.5:(0.47,0.21,0.53,0.79),
5.0:(0.48,0.19,0.52,0.81),5.5:(0.47,0.19,0.53,0.81),6.0:(0.62,0.13,0.38,0.87),6.5:(0.55,0.10,0.45,0.90),7.0:(0.44,0.05,0.56,0.95),
7.5:(0.41,0,0.59,1),8.0:(0.48,0.10,0.52,0.90),8.5:(0.49,0.02,0.51,0.98),9.0:(0.45,0.10,0.55,0.90)}
write({"mediaId":4816,"level":"A","keyWord":"heart","defaultVoice":"female",
"taps":[{"phrase":"to touch her chest","target":"the woman","voice":"female","keys":K(T,W)},
{"phrase":"to show him her watch","target":"the woman","voice":"female","keys":K(T,W)},
{"phrase":"to wear a green T-shirt","target":"the man","voice":"male","keys":K(T,M)}],
"stillS":4.0,
"nouns":[{"word":"a woman","x":0.20,"y":0.42,"voice":"female"},{"word":"a man","x":0.72,"y":0.45,"voice":"male"},
{"word":"a watch","x":0.66,"y":0.88,"voice":"female"},{"word":"the sky","x":0.70,"y":0.10,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","touching","her","chest."],"answerVoice":"female",
"notes":"Key word heart is not a visible noun (hand on chest), so not a slot. Man is visible small at t=0.0 (green shirt, right) then hidden behind her until 3.0; marked off 0.5-2.5. From 6.5 her arm with the watch reaches across the man's shirt; box split at the line between their heads, so part of her arm lies in his box."})
