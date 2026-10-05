from gen_4816_4818_4820_4821 import *
T=[i*0.5 for i in range(19)]
Y={2.0:(0,0,0.46,0.77),2.5:(0,0,0.44,0.80),3.0:(0,0,0.44,0.80),3.5:(0,0,0.53,0.79),4.0:(0,0,0.47,0.72),4.5:(0,0.01,0.53,0.70),
5.0:(0,0.05,0.50,0.65),5.5:(0,0.06,0.55,0.64),6.0:(0,0.07,0.53,0.62),6.5:(0,0.07,0.55,0.62),7.0:(0,0.08,0.53,0.61),7.5:(0,0.08,0.52,0.62),
8.0:(0,0.10,0.50,0.62),8.5:(0,0.10,0.50,0.64),9.0:(0,0.12,0.50,0.62)}
W={0.0:(0.45,0,0.55,0.32),0.5:(0.48,0,0.52,0.34),1.0:(0.46,0,0.54,0.33),1.5:(0.48,0,0.52,0.43),2.0:(0.47,0,0.53,0.52),2.5:(0.44,0,0.36,0.58),
3.0:(0.44,0.05,0.33,0.56),3.5:(0.53,0.11,0.18,0.50),4.0:(0.47,0.16,0.22,0.46),4.5:(0.53,0.19,0.18,0.43),5.0:(0.50,0.21,0.21,0.40),
5.5:(0.55,0.21,0.18,0.41),6.0:(0.53,0.22,0.21,0.41),6.5:(0.55,0.21,0.21,0.42),7.0:(0.53,0.22,0.21,0.42),7.5:(0.52,0.23,0.23,0.42),
8.0:(0.50,0.24,0.25,0.42),8.5:(0.50,0.25,0.24,0.42),9.0:(0.50,0.25,0.24,0.43)}
O={2.5:(0.80,0,0.20,0.47),3.0:(0.77,0.08,0.23,0.50),3.5:(0.71,0.15,0.29,0.43),4.0:(0.69,0.19,0.31,0.39),4.5:(0.71,0.22,0.29,0.36),
5.0:(0.71,0.23,0.29,0.35),5.5:(0.73,0.23,0.27,0.35),6.0:(0.74,0.24,0.26,0.35),6.5:(0.76,0.23,0.24,0.36),7.0:(0.74,0.24,0.26,0.35),
7.5:(0.75,0.24,0.25,0.36),8.0:(0.75,0.25,0.25,0.36),8.5:(0.74,0.25,0.26,0.37),9.0:(0.74,0.26,0.26,0.37)}
write({"mediaId":4818,"level":"B","keyWord":"heel","defaultVoice":"male",
"taps":[{"phrase":"to lead the way","target":"the young man","voice":"male","keys":K(T,Y)},
{"phrase":"to wear black leggings","target":"the woman","voice":"female","keys":K(T,W)},
{"phrase":"to bring up the rear","target":"the older man","voice":"male","keys":K(T,O)}],
"stillS":0.5,
"nouns":[{"word":"an index finger","x":0.33,"y":0.17,"voice":"male"},{"word":"a sock","x":0.66,"y":0.42,"voice":"male"},
{"word":"a stiletto heel","x":0.57,"y":0.62,"voice":"male"},{"word":"floorboards","x":0.45,"y":0.85,"voice":"male"}],
"question":"What are the three people doing?","answer":["They","are","trying","to","walk","in","stiletto","heels."],"answerVoice":"male",
"notes":"Opening close-up (0-1.5) shows a foot on a spike heel and a pointing hand; owner not identifiable, so the young man is off there; the woman's legs (black leggings, one grey sock) are visible in the background from 0.0. 'to bring up the rear': the older man is always the furthest back (his feet highest in the picture). defaultVoice male = the leading young man as main person. Woman's outstretched arms reach into neighbours' boxes; split at the body lines."})
