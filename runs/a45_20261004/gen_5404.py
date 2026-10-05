from gen_5401_5402_5403_5404_lib import *
T=times_of(5404)
mb={0.0:(0,0.1,0.85,0.6),0.5:(0,0.1,0.88,0.6),1.0:(0,0.1,0.75,0.65),1.5:(0,0.1,0.68,0.7),
2.0:(0,0.18,0.66,0.62),2.5:(0,0.18,0.66,0.62),3.0:(0,0.19,0.64,0.62),3.5:(0,0.14,0.63,0.6),
4.0:(0,0.17,0.6,0.56),4.5:(0,0.15,0.55,0.58),5.0:(0,0,1,0.66),5.5:(0,0.08,0.72,0.56),
6.0:(0,0.16,0.68,0.44),6.5:(0,0,0.92,0.62),7.0:(0,0.11,0.73,0.5),7.5:(0.08,0.13,0.6,0.46),
8.0:(0,0.12,0.72,0.43),8.5:(0,0.1,0.72,0.41),9.0:(0,0.07,0.72,0.39),9.5:(0,0.05,0.97,0.4),
10.0:(0,0.04,0.99,0.41),10.5:(0,0.04,0.99,0.41),11.0:(0,0.02,1,0.42),11.5:(0,0.02,1,0.42),12.0:(0,0.02,1,0.42)}
pb={5.0:(0.3,0.69,0.42,0.14),5.5:(0.33,0.65,0.38,0.14),6.0:(0.36,0.61,0.35,0.16),6.5:(0.36,0.63,0.36,0.15),
7.0:(0.36,0.62,0.36,0.15),7.5:(0.35,0.6,0.37,0.17),8.0:(0.36,0.56,0.36,0.21),8.5:(0.35,0.52,0.38,0.25),
9.0:(0.35,0.47,0.38,0.33),9.5:(0.34,0.46,0.37,0.54),10.0:(0.33,0.46,0.38,0.53),10.5:(0.33,0.46,0.38,0.53),
11.0:(0.33,0.45,0.37,0.55),11.5:(0.33,0.45,0.37,0.55),12.0:(0.33,0.45,0.37,0.55)}
man=keys(T,mb); pile=keys(T,pb)
write(5404,{"mediaId":5404,"level":"A","keyWord":"greedy","defaultVoice":"male",
"taps":[{"phrase":"to add more toast","target":"the young man","voice":"male","keys":man},
{"phrase":"to smile at the camera","target":"the young man","voice":"male","keys":man},
{"phrase":"to grow very tall","target":"the pile of toast","voice":"male","keys":pile}],
"stillS":4.0,
"nouns":[{"word":"a man","x":0.25,"y":0.38,"voice":"male"},{"word":"toast","x":0.73,"y":0.57,"voice":"male"},
{"word":"a toaster","x":0.72,"y":0.72,"voice":"male"},{"word":"a table","x":0.3,"y":0.9,"voice":"male"}],
"question":"What is the man making?","answer":["He","is","making","a","lot","of","toast."],"answerVoice":"male",
"notes":"From 9.5 s the toast pile stands in front of the man's torso: man box = head/shoulders above the pile (y < ~0.45), pile box below, so his hands holding the knife lower down are outside both boxes. 'to smile at the camera' is clearest at 11.0-12.0 s; he grins throughout. Pile box starts at 5.0 s when the first slice lies on the plate."})
