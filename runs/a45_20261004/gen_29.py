import json
W={2.0:(0,.20,.49,.80),2.5:(0,.20,.47,.80),3.0:(0,.23,.48,.77),3.5:(0,.24,.49,.76),4.0:(0,.25,.49,.75),4.5:(0,.25,.49,.75),
10.0:(0,0,.41,1),10.5:(0,0,.43,1),11.0:(0,0,.95,.55),11.5:(0,0,.90,.61),12.0:(0,0,.60,1),12.5:(0,0,.62,1),13.0:(0,0,.64,1),13.5:(0,0,.61,1),14.0:(0,0,.59,1)}
S={0.0:(0,.32,.84,.68),0.5:(0,.32,.84,.68),1.0:(0,.32,.84,.68),1.5:(0,.32,.84,.68),
2.0:(.50,.33,.50,.67),2.5:(.48,.33,.52,.67),3.0:(.49,.33,.51,.67),3.5:(.50,.33,.50,.67),4.0:(.50,.34,.50,.66),4.5:(.50,.34,.50,.66),
10.0:(.42,.38,.58,.62),10.5:(.44,.38,.56,.62),11.0:(.46,.56,.54,.44),11.5:(.55,.62,.45,.38),12.0:(.61,.50,.39,.50),12.5:(.63,.52,.37,.48),
13.0:(.65,.54,.35,.46),13.5:(.62,.55,.38,.45),14.0:(.60,.54,.40,.46)}
M={5.0:(.22,.26,.60,.37),5.5:(.24,.29,.59,.36),6.0:(.28,.30,.56,.37),6.5:(.15,0,.85,1),7.0:(.25,0,.75,1),7.5:(.15,.18,.62,.64),8.0:(.15,.18,.62,.64),
8.5:(.10,.18,.90,.64),9.0:(.08,.19,.92,.65),9.5:(.08,.19,.92,.65)}
T=[i/2 for i in range(29)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
o={"mediaId":29,"level":"A","keyWord":"telescope","defaultVoice":"female",
"taps":[{"phrase":"to look through the telescope","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to stand on three legs","target":"the telescope","voice":"female","keys":keys(S)},
{"phrase":"to shine in the night sky","target":"the moon","voice":"female","keys":keys(M)}],
"stillS":4.0,
"nouns":[{"word":"a telescope","x":.72,"y":.44,"voice":"female"},{"word":"a hat","x":.38,"y":.37,"voice":"female"},
{"word":"a jacket","x":.22,"y":.60,"voice":"female"},{"word":"the sky","x":.60,"y":.10,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","looking","through","a","telescope."],"answerVoice":"female",
"notes":"Woman and telescope overlap in 2.0-4.5 (split at x about 0.49; her hand on the control rod is right of the line) and in the close-ups 10.0-14.0 (eyepiece in front of her face: the woman's box is the left part or the upper part of the frame). The bright streak at 8.5-9.5 lies inside the moon's box; 'to shine in the night sky' is meant for the moon. 'a hat' and 'a jacket' are both on the woman but far apart on a large figure."}
json.dump(o,open("content/29.json","w"),indent=1)
