from gen_5401_5402_5403_5404_lib import *
T=times_of(5403)
wb={0.0:(0,0.29,0.7,0.71),0.5:(0,0.3,0.81,0.7),1.0:(0,0.31,0.81,0.69),1.5:(0,0.31,0.81,0.69),
2.0:(0,0.29,0.73,0.71),2.5:(0,0.3,0.72,0.7),3.0:(0,0.31,0.71,0.69),3.5:(0,0.53,0.45,0.47),
4.0:(0,0.5,0.82,0.5),4.5:(0,0.5,0.82,0.5),5.0:(0,0.55,0.52,0.45),5.5:(0,0.55,0.47,0.45),
6.0:(0,0.31,0.77,0.69),6.5:(0.19,0.32,0.66,0.68),7.0:(0.23,0.34,0.6,0.66),7.5:(0.21,0.34,0.63,0.66),
8.0:(0.18,0.33,0.63,0.67),8.5:(0.19,0.33,0.62,0.67),9.0:(0.2,0.33,0.6,0.67)}
tb={6.5:(0,0.4,0.18,0.17),7.0:(0,0.37,0.22,0.2),7.5:(0,0.34,0.2,0.22),8.0:(0,0.31,0.17,0.22),8.5:(0,0.32,0.18,0.22),9.0:(0,0.32,0.19,0.22)}
wom=keys(T,wb); tr=keys(T,tb)
write(5403,{"mediaId":5403,"level":"A","keyWord":"time","defaultVoice":"female",
"taps":[{"phrase":"to look at her watch","target":"the woman","voice":"female","keys":wom},
{"phrase":"to write in a notebook","target":"the woman","voice":"female","keys":wom},
{"phrase":"to arrive at the station","target":"the red train","voice":"female","keys":tr}],
"stillS":2.0,
"nouns":[{"word":"the sky","x":0.12,"y":0.2,"voice":"female"},{"word":"a timetable","x":0.8,"y":0.42,"voice":"female"},
{"word":"a watch","x":0.43,"y":0.73,"voice":"female"},{"word":"a coat","x":0.2,"y":0.88,"voice":"female"}],
"question":"What is the woman looking at?","answer":["She","is","looking","at","her","watch."],"answerVoice":"female",
"notes":"Red train only visible 6.5-9.0 s at the left edge, partly behind the woman; boxes split vertically there (woman box starts at x~0.2, so her left shoulder/sleeve is outside both boxes). 'to arrive at the station': train is moving in on the platform, may not fully stop in the clip."})
