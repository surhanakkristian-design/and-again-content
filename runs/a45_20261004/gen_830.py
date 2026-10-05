import json
T=[i*0.5 for i in range(10)]
def keys(d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2]-d[t][0],2),"h":round(d[t][3]-d[t][1],2)} for t in T]
W={0.0:(0,.19,.52,1),0.5:(0,.19,.49,1),1.0:(0,.21,.52,1),1.5:(0,.20,.50,1),2.0:(0,.18,.53,1),2.5:(0,.17,.50,1),3.0:(0,.16,.49,1),3.5:(0,.15,.49,1),4.0:(0,.14,.47,1),4.5:(0,.15,.48,1)}
M={0.0:(.53,.37,1,.97),0.5:(.50,.37,1,.97),1.0:(.53,.38,1,1),1.5:(.51,.38,1,1),2.0:(.54,.37,1,.97),2.5:(.51,.37,1,.97),3.0:(.50,.36,1,1),3.5:(.50,.36,1,1),4.0:(.48,.36,1,1),4.5:(.49,.38,1,1)}
kw,km=keys(W),keys(M)
c={"mediaId":830,"level":"B","keyWord":"explain","defaultVoice":"female",
"taps":[{"phrase":"to gesture at the tablet","target":"the grey-haired woman","voice":"female","keys":kw},
{"phrase":"to grip a stylus","target":"the young man","voice":"male","keys":km},
{"phrase":"to glance up at her","target":"the young man","voice":"male","keys":km}],
"stillS":0.0,
"nouns":[{"word":"a blazer","x":.15,"y":.55,"voice":"female"},{"word":"books","x":.76,"y":.24,"voice":"female"},
{"word":"a tablet","x":.80,"y":.72,"voice":"female"},{"word":"a stylus","x":.68,"y":.85,"voice":"female"}],
"question":"What is the grey-haired woman doing?","answer":["She","is","explaining","something","on","the","tablet."],"answerVoice":"female",
"notes":"Two usable targets. The woman stands in front of the seated man and her arm crosses his chest, so the boxes are split by a vertical line between their faces (x about 0.5): the left part of the man's sweater falls inside the woman's box - weak spot. The background woman and the tablet were not used as targets because their boxes would overlap the man's. The man glances up 0-3.5 s and looks down at 4.0-4.5 s; he holds the stylus all clip. 'explaining' is shown by her pointing and talking."}
json.dump(c,open('content/830.json','w'),indent=1)
