from gen_5405_5406_5407_5408_lib import *
T=[i*0.5 for i in range(19)]
w={0.0:(0,0,0.80,0.48),0.5:(0.08,0,0.88,0.52),1.0:(0.08,0,0.82,0.55),1.5:(0.10,0,0.72,0.62),2.0:(0,0,0.80,0.76),
 2.5:(0.06,0,0.80,0.88),3.0:(0.08,0,0.68,0.88),3.5:(0.13,0,0.66,0.87),4.0:(0.10,0,0.67,0.93),4.5:(0.10,0,0.67,0.93),
 5.0:(0.12,0.05,0.64,0.80),5.5:(0.15,0.05,0.60,0.80),6.0:(0.23,0.08,0.48,0.84),6.5:(0.20,0.13,0.57,0.71),
 7.0:(0.20,0.11,0.52,0.71),7.5:(0.23,0.15,0.52,0.62),8.0:(0.22,0.15,0.62,0.57),8.5:(0.40,0.36,0.54,0.30),9.0:(0.36,0.42,0.56,0.24)}
k=K(T,w)
write(5406,{"mediaId":5406,"level":"A","keyWord":"toe","defaultVoice":"female",
 "taps":[
  {"phrase":"to step on a shell","target":"the woman","voice":"female","keys":k},
  {"phrase":"to hold up a shell","target":"the woman","voice":"female","keys":k},
  {"phrase":"to jump onto a towel","target":"the woman","voice":"female","keys":k}],
 "stillS":1.5,
 "nouns":[{"word":"toes","x":0.24,"y":0.56,"voice":"female"},
          {"word":"a shell","x":0.46,"y":0.65,"voice":"female"},
          {"word":"sand","x":0.50,"y":0.88,"voice":"female"},
          {"word":"the sea","x":0.84,"y":0.08,"voice":"female"}],
 "question":"What is the woman stepping on?",
 "answer":["She","is","stepping","on","a","shell."],
 "answerVoice":"female",
 "notes":"Only the woman is a clear target (people in the sea are tiny and in the background), so all three phrases use her; in 0-1.5 s only her legs and feet are visible. Still at 1.5 s: toes on the left foot, the shell just below."})
