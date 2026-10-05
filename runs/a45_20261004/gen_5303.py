import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2],2),"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
# woman: (left, top, right) bottom = 1.0
wl={0.0:(.19,.21,.86),0.5:(.19,.21,.85),1.0:(.19,.21,.86),1.5:(.19,.21,.88),2.0:(.20,.21,.87),2.5:(.20,.21,.87),
3.0:(.21,.21,.87),3.5:(.22,.21,.87),4.0:(.24,.22,.86),4.5:(.26,.22,.86),5.0:(.27,.22,.87),5.5:(.28,.25,.87),
6.0:(.28,.28,.88),6.5:(.27,.29,1.0),7.0:(.27,.31,1.0),7.5:(.29,.32,1.0),8.0:(.34,.34,1.0),8.5:(.37,.37,1.0),
9.0:(.39,.40,1.0),9.5:(.41,.43,.89),10.0:(.43,.46,1.0),10.5:(.41,.49,1.0),11.0:(.20,.50,.78),11.5:(.08,.50,1.0),12.0:(.15,.50,1.0)}
w={t:(a,b,c-a,round(1-b,2)) for t,(a,b,c) in wl.items()}
cp={0.0:(0,.40,.18,.15),0.5:(0,.40,.18,.15),1.0:(0,.40,.18,.16),1.5:(0,.40,.18,.15),2.0:(0,.40,.19,.16),2.5:(0,.40,.19,.16),
3.0:(0,.40,.20,.17),3.5:(.01,.41,.20,.16),4.0:(.03,.39,.20,.17),4.5:(.06,.40,.19,.16),5.0:(.07,.42,.19,.17),5.5:(.08,.42,.19,.18),
6.0:(.08,.42,.19,.19),6.5:(.07,.43,.19,.17),7.0:(.08,.44,.18,.17),7.5:(.10,.45,.18,.17),8.0:(.12,.45,.21,.20),8.5:(.15,.46,.21,.21),
9.0:(.17,.48,.21,.21),9.5:(.19,.50,.21,.22),10.0:(.19,.52,.23,.19),10.5:(.21,.54,.19,.17)}
d={"mediaId":5303,"level":"A","keyWord":"snowflake","defaultVoice":"female",
"taps":[{"phrase":"to catch snowflakes","target":"the woman in yellow","voice":"female","keys":keys(w)},
{"phrase":"to open her arms","target":"the woman in yellow","voice":"female","keys":keys(w)},
{"phrase":"to walk together","target":"the two people behind her","voice":"female","keys":keys(cp)}],
"stillS":2.0,
"nouns":[{"word":"a church","x":0.80,"y":0.14,"voice":"female"},{"word":"a hat","x":0.50,"y":0.31,"voice":"female"},
{"word":"a scarf","x":0.40,"y":0.51,"voice":"female"},{"word":"snow","x":0.88,"y":0.86,"voice":"female"}],
"question":"What is the woman in yellow doing?","answer":["She","is","catching","snowflakes","on","her","glove."],"answerVoice":"female",
"notes":"Third target is the pair walking in the background on the left (gender unclear); off from 11.0 when only one of them is half-hidden behind the woman. Their box sits against the woman's left side, so the woman's box is cut on the left (her left sleeve/mitten and outstretched left arm at 9.0-10.5 fall outside). 'glove' used for her mitten (A-level). The woman does not clearly walk away at the end, she turns round with open arms."}
json.dump(d,open("content/5303.json","w"),indent=1)
