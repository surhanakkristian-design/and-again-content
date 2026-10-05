import json
T=[i*0.5 for i in range(10)]
def keys(d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2]-d[t][0],2),"h":round(d[t][3]-d[t][1],2)} for t in T]
D={0.0:(0,.30,.54,1),0.5:(0,.30,.53,1),1.0:(0,.31,.55,1),1.5:(0,.29,.55,1),2.0:(0,.28,.53,1),2.5:(0,.28,.50,1),3.0:(0,.29,.49,1),3.5:(0,.29,.50,1),4.0:(0,.28,.52,1),4.5:(0,.28,.54,1)}
B={0.0:(.55,.30,1,1),0.5:(.54,.31,1,1),1.0:(.56,.31,1,1),1.5:(.56,.30,1,1),2.0:(.54,.29,1,1),2.5:(.51,.29,1,1),3.0:(.50,.29,1,1),3.5:(.51,.29,1,1),4.0:(.53,.28,1,1),4.5:(.55,.28,1,1)}
kd,kb=keys(D),keys(B)
c={"mediaId":828,"level":"A","keyWord":"surprised","defaultVoice":"female",
"taps":[{"phrase":"to look very surprised","target":"the blonde woman","voice":"female","keys":kb},
{"phrase":"to lift her cup high","target":"the blonde woman","voice":"female","keys":kb},
{"phrase":"to lean on the table","target":"the dark-haired woman","voice":"female","keys":kd}],
"stillS":0.0,
"nouns":[{"word":"a sweater","x":.18,"y":.66,"voice":"female"},{"word":"a jacket","x":.82,"y":.60,"voice":"female"},
{"word":"a cake","x":.51,"y":.82,"voice":"female"},{"word":"a table","x":.50,"y":.93,"voice":"female"}],
"question":"How does the blonde woman look?","answer":["She","looks","very","surprised."],"answerVoice":"female",
"notes":"Only two targets (the two women); the blonde has two phrases. She lifts her cup with one hand from 2.0 s; the dark-haired woman keeps hers low with both hands and rests her elbows on the table the whole clip. The boxes are split along the gap between their hands (they nearly touch at 2.5-3.5 s). 'a cake' = the small pastry on the plate. Surprised face is clearest 0-1.5 s; later both laugh."}
json.dump(c,open('content/828.json','w'),indent=1)
