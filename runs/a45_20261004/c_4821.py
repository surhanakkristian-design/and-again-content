from gen_4816_4818_4820_4821 import *
T=[i*0.5 for i in range(13)]
W={0.0:(0.27,0.41,0.19,0.14),0.5:(0.29,0.41,0.19,0.14),1.0:(0.29,0.41,0.19,0.14),1.5:(0.38,0.41,0.18,0.14),2.0:(0.24,0.19,0.42,0.72),
2.5:(0.10,0,0.68,0.97),3.0:(0.06,0,0.80,1),3.5:(0.20,0.07,0.80,0.93),4.0:(0.12,0,0.88,0.88),4.5:(0.12,0,0.88,0.90),
5.0:(0.10,0,0.81,1),5.5:(0.13,0,0.80,1),6.0:(0.08,0.04,0.82,0.96)}
S={0.0:(0.46,0.27,0.18,0.14),0.5:(0.48,0.27,0.18,0.14),1.0:(0.48,0.27,0.18,0.14),1.5:(0.42,0.27,0.18,0.14),
2.5:(0.79,0.06,0.20,0.18),3.0:(0.86,0.08,0.14,0.18),5.0:(0.91,0.27,0.09,0.15),5.5:(0.93,0.29,0.07,0.15),6.0:(0.90,0.26,0.10,0.18)}
write({"mediaId":4821,"level":"B","keyWord":"sunset","defaultVoice":"female",
"taps":[{"phrase":"to approach the car","target":"the woman","voice":"female","keys":K(T,W)},
{"phrase":"to lean towards the window","target":"the woman","voice":"female","keys":K(T,W)},
{"phrase":"to glow above the horizon","target":"the sun","voice":"female","keys":K(T,S)}],
"stillS":2.5,
"nouns":[{"word":"the sun","x":0.86,"y":0.14,"voice":"female"},{"word":"a pizza box","x":0.45,"y":0.43,"voice":"female"},
{"word":"a summer dress","x":0.45,"y":0.58,"voice":"female"},{"word":"tarmac","x":0.17,"y":0.88,"voice":"female"}],
"question":"What is the barefoot woman doing?","answer":["She","is","handing","a","pizza","box","through","the","window."],"answerVoice":"female",
"notes":"Key word 'sunset' is not a placeable noun; 'the sun' slot instead. 0-1.5 the woman is a tiny figure right under the sun: boxes kept apart (woman below/left, sun above). Sun off at 2.0 (behind her head), 3.5-4.5 (behind her hair); at 3.0 and 5.0-6.0 it is only a bright part-disc at the right edge, so those sun boxes are narrow (0.07-0.14) to stay clear of her. Answer = final action (hands the box through the open window at 6.0); she walks towards the car before that."})
