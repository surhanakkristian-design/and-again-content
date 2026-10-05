from gen_5401_5402_5403_5404_lib import *
T=times_of(5402)
mb={0.0:(0,0.26,0.52,0.74),0.5:(0,0.26,0.5,0.74),1.0:(0,0.25,0.54,0.75),1.5:(0,0.25,0.52,0.75)}
for t in (2.0,2.5,3.0,3.5,4.0): mb[t]=(0,0.08,0.99,0.92)
for t in T:
    if t>=4.5: mb[t]=(0,0,1,1)
man=keys(T,mb)
doc=keys(T,{0.0:(0.53,0.11,0.47,0.89),0.5:(0.51,0.11,0.49,0.89),1.0:(0.55,0.11,0.45,0.89),1.5:(0.53,0.11,0.47,0.89)})
write(5402,{"mediaId":5402,"level":"B","keyWord":"throat","defaultVoice":"male",
"taps":[{"phrase":"to examine his throat","target":"the doctor","voice":"female","keys":doc},
{"phrase":"to gulp down some water","target":"the young man","voice":"male","keys":man},
{"phrase":"to tilt his head back","target":"the young man","voice":"male","keys":man}],
"stillS":5.0,
"nouns":[{"word":"a plastic bottle","x":0.22,"y":0.1,"voice":"male"},{"word":"a throat","x":0.55,"y":0.5,"voice":"male"},
{"word":"a collar","x":0.27,"y":0.68,"voice":"male"},{"word":"a button","x":0.5,"y":0.86,"voice":"male"}],
"question":"What is the doctor doing?","answer":["She","is","examining","his","throat."],"answerVoice":"female",
"notes":"Doctor only visible 0-1.5 s; at 0-1.5 man and doctor boxes split near x 0.52 (her hand with the tongue depressor is near his mouth). Noun 'a throat' on the close-up neck at 5.0 s."})
