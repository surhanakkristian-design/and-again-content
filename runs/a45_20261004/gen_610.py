import json
times=[i*0.5 for i in range(21)]
def keys(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in times]
man={0.0:(0,0,.18,1.0),0.5:(0,0,.18,.55),1.0:(0,0,.32,.28),1.5:(0,.05,.42,.42),2.0:(0,0,.44,.50),2.5:(0,0,.40,.92),3.0:(0,0,.52,1.0),3.5:(0,0,.55,1.0),
4.0:(0,.05,.50,.95),4.5:(0,.05,.46,.95),5.0:(0,.05,.42,.95),5.5:(0,.08,.70,.30),6.0:(0,.05,.77,.31),6.5:(0,.08,.72,.28),7.0:(0,.08,.69,.31),7.5:(0,.08,.69,.32),8.0:(0,.06,.69,.28)}
wom={5.5:(.82,.15,.18,.23),6.0:(.78,.08,.22,.29),6.5:(.73,.08,.27,.30),7.0:(.70,.08,.30,.31),7.5:(.70,.08,.30,.32),8.0:(.70,.08,.30,.30),8.5:(.75,.08,.25,.30),9.0:(.68,.08,.32,.29),9.5:(.68,.08,.32,.30),10.0:(.70,.08,.30,.30)}
pum={2.5:(.82,.28,.18,.40),3.0:(.68,.28,.32,.70),3.5:(.56,.30,.44,.70),4.0:(.50,.30,.50,.62),4.5:(.46,.28,.54,.65),5.0:(.42,.32,.58,.65),5.5:(.30,.38,.70,.60),6.0:(.20,.37,.80,.58),6.5:(.10,.38,.90,.56),7.0:(.05,.39,.95,.56),7.5:(.05,.40,.95,.54),8.0:(.07,.38,.93,.56),8.5:(.08,.38,.92,.56),9.0:(.08,.37,.92,.60),9.5:(.10,.38,.90,.57),10.0:(.12,.38,.88,.56)}
c={"mediaId":610,"level":"A","keyWord":"ribbon","defaultVoice":"female",
"taps":[{"phrase":"to carry three ribbons","target":"the man in the cap","voice":"male","keys":keys(man)},
{"phrase":"to hug the big pumpkin","target":"the woman in the hat","voice":"female","keys":keys(wom)},
{"phrase":"to be big and orange","target":"the big pumpkin","voice":"female","keys":keys(pum)}],
"stillS":9.0,
"nouns":[{"word":"a ribbon","x":.52,"y":.56,"voice":"female"},{"word":"a pumpkin","x":.70,"y":.74,"voice":"female"},{"word":"a hat","x":.82,"y":.19,"voice":"female"},{"word":"flags","x":.32,"y":.10,"voice":"female"}],
"question":"What is on the big pumpkin?","answer":["There","is","a","blue","ribbon","on","the","pumpkin."],"answerVoice":"female",
"notes":"Man = the judge in the flat cap (0-8 s; 0-2 s only his arm/jacket edge at the left, a bystander in a blue shirt stands behind the ribbons at 1.0-2.0 and is not him). Woman in the straw hat appears from 5.5 s. Man/woman/pumpkin overlap from 5.5 s: boxes are split horizontally (people above about y .38, pumpkin below), so the man's lower sleeve and the woman's hugging arm lie in the pumpkin box. A second, smaller orange pumpkin is in the background at 1.0-2.5 s (pumpkin phrase is a state). 'a hat' = the straw hat; crowd men wear small caps far behind. defaultVoice female: mixed clip, evenId true."}
json.dump(c,open('content/610.json','w'),indent=1,ensure_ascii=False)
