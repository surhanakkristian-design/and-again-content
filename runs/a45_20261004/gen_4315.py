import json
T=[i*0.5 for i in range(19)]
w={0:(.33,.3,.34,.7),.5:(.3,.3,.46,.7),1:(.23,.28,.52,.72),1.5:(.15,.26,.68,.42),2:(0,.23,.92,.45),2.5:(.2,.28,.5,.72),3:(.12,.27,.58,.73),
3.5:(.25,.24,.5,.44),4:(.23,.38,.56,.3),4.5:(.17,.36,.63,.32),5:(.15,.34,.65,.34),5.5:(.27,.37,.42,.63),6:(.21,.35,.46,.65),
6.5:(.25,.34,.55,.34),7:(.29,.33,.55,.35),7.5:(.2,.33,.6,.35),8:(.23,.32,.48,.36),8.5:(.18,.31,.6,.37),9:(.19,.31,.53,.37)}
p3=(.26,.69,.48,.14); p12=(.22,.69,.56,.14); p10=(.2,.69,.6,.14)
price={1.5:p3,2:p3,3.5:p12,4:p12,4.5:p12,5:p12,6.5:p10,7:p10,7.5:p10,8:p10,8.5:p10,9:p10}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
d={"mediaId":4315,"level":"A","keyWord":"price","defaultVoice":"female",
"taps":[{"phrase":"to sit on the sofa","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to walk into a room","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to get higher and higher","target":"the price","voice":"female","keys":keys(price)}],
"stillS":4.5,
"nouns":[{"word":"a price","x":.5,"y":.73,"voice":"female"},{"word":"a sofa","x":.86,"y":.52,"voice":"female"},
{"word":"a window","x":.12,"y":.3,"voice":"female"},{"word":"a coat","x":.5,"y":.62,"voice":"female"}],
"question":"Where is the woman sitting?","answer":["She","is","sitting","on","the","sofa."],"answerVoice":"female",
"notes":"Only one person; the second target is the price caption burned into the picture (300, 1,200, 10,000 EUR). The caption lies on the woman's body, so her box ends above it (head and upper body) and the caption band is the price box. 'a price' pill sits on the caption, 'a coat' on her chest above it. 'a window' at 4.5 is the glass balcony door at the left edge. Two small people stand far in the background at 9.0 (left); the woman's box starts right of them."}
json.dump(d,open("content/4315.json","w"),indent=1)
