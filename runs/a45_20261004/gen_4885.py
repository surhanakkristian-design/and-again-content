import json
# t: (woman x0,y0,x1,y1), (group x0,y0,x1,y1)
D={0.0:((.10,.22,.63,.95),(.63,.38,.93,.58)),
0.5:((.08,.22,.62,.98),(.62,.39,.92,.60)),
1.0:((.02,.18,.61,1.0),(.61,.41,.90,.61)),
1.5:((.06,.21,.63,1.0),(.63,.43,.90,.61)),
2.0:((.10,.19,.66,1.0),(.66,.44,.89,.61)),
2.5:((.10,.20,.65,1.0),(.65,.43,.89,.60)),
3.0:((.08,.20,.64,1.0),(.64,.45,.87,.62)),
3.5:((.08,.21,.63,1.0),(.63,.44,.88,.62)),
4.0:((.13,.21,.62,.93),(.62,.42,.87,.61)),
4.5:((.15,.23,.62,.89),(.62,.41,.87,.63)),
5.0:((.16,.23,.61,.94),(.61,.42,.85,.62)),
5.5:((.15,.22,.63,.94),(.63,.43,.87,.63)),
6.0:((.11,.24,.60,.93),(.60,.42,.88,.64)),
6.5:((.11,.25,.60,.96),(.60,.43,.87,.68)),
7.0:((.12,.28,.58,.99),(.58,.47,.86,.69)),
7.5:((.14,.27,.63,1.0),(.63,.46,.87,.67)),
8.0:((.13,.22,.62,.99),(.62,.48,.87,.69)),
8.5:((.04,.21,.60,1.0),(.60,.47,.83,.68)),
9.0:((0.0,.22,.50,1.0),(.50,.47,.80,.70))}
def k(t,b):
    x0,y0,x1,y1=b; return {"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
T=[i*0.5 for i in range(19)]
wk=[k(t,D[t][0]) for t in T]; gk=[k(t,D[t][1]) for t in T]
c={"mediaId":4885,"level":"A","keyWord":"street","defaultVoice":"female",
"taps":[{"phrase":"to hold up a small flag","target":"the woman","voice":"female","keys":wk},
{"phrase":"to lead the group","target":"the woman","voice":"female","keys":wk},
{"phrase":"to follow the woman","target":"the group","voice":"female","keys":gk}],
"stillS":4.0,
"nouns":[{"word":"the sky","x":0.65,"y":0.08,"voice":"female"},{"word":"a flag","x":0.22,"y":0.27,"voice":"female"},
{"word":"people","x":0.76,"y":0.5,"voice":"female"},{"word":"a street","x":0.75,"y":0.82,"voice":"female"}],
"question":"Where is the woman walking?","answer":["She","is","walking","up","the","street."],"answerVoice":"female",
"notes":"The woman's outstretched right arm often reaches over the group; boxes are split at her body's right edge, so the arm tip lies in the group box at 0.5/1.5/3.5/4.0/4.5 s. 'Up the street': the street climbs behind her (camera walks backwards in front of her)."}
json.dump(c,open('content/4885.json','w'),indent=1)
