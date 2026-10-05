from gen_5401_5402_5403_5404_lib import *
T=times_of(5401)
man=keys(T,{2.0:(0.02,0.08,0.93,0.74),2.5:(0.02,0.08,0.93,0.74),3.0:(0.02,0.08,0.93,0.74)})
boy=keys(T,{3.5:(0.45,0.2,0.55,0.8),4.0:(0.28,0.17,0.66,0.83),4.5:(0.23,0.14,0.75,0.86),5.0:(0.12,0.12,0.88,0.88)})
wom=keys(T,{5.5:(0.02,0.03,0.96,0.95),6.0:(0.02,0.03,0.96,0.95),6.5:(0.02,0.03,0.96,0.95),7.0:(0.02,0.08,0.96,0.9),7.5:(0.02,0.08,0.96,0.9),8.0:(0.02,0.08,0.96,0.9)})
write(5401,{"mediaId":5401,"level":"A","keyWord":"wonder","defaultVoice":"male",
"taps":[{"phrase":"to play chess","target":"the man","voice":"male","keys":man},
{"phrase":"to cover his eyes","target":"the boy","voice":"male","keys":boy},
{"phrase":"to bite a pen","target":"the woman in the sweater","voice":"female","keys":wom}],
"stillS":10.0,
"nouns":[{"word":"a woman","x":0.5,"y":0.33,"voice":"female"},{"word":"a cup","x":0.86,"y":0.6,"voice":"male"},
{"word":"books","x":0.7,"y":0.75,"voice":"male"},{"word":"paper","x":0.45,"y":0.88,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","playing","chess."],"answerVoice":"male",
"notes":"Montage of 5 shots; first (0-1.5s, pen at chin) and last (8.5-10s, writing) woman may be the same person, so neither is a tap target. defaultVoice male (mixed group, evenId false)."})
