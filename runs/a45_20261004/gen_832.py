import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)})
    return out
M={0.0:(.17,.28,.90,.76),0.5:(.42,.25,1,.74),1.0:(.10,.26,.82,.70),1.5:(.26,.25,.88,.72),2.0:(.16,.24,.88,.67),2.5:(.26,.18,1,.70),
3.0:(.63,.17,1,.82),3.5:(.61,.17,1,.82),4.0:(.38,.20,1,.76),4.5:(.36,.19,.82,.51),5.0:(.35,.19,.80,.58),5.5:(.34,.19,.90,.60),
6.0:(.38,.21,.92,.54),6.5:(.40,.22,.88,.52),7.0:(.36,.09,.83,.53),7.5:(.33,.15,.82,.54),8.0:(.31,.17,.78,.47),8.5:(.36,.12,.77,.47),9.0:(.35,.13,.75,.51)}
O={3.0:(.28,.27,.62,.60),3.5:(.18,.27,.60,.62),4.0:(0,.48,.36,.76),4.5:(.08,.40,.34,.58),5.0:(.09,.40,.34,.59),5.5:(.09,.40,.33,.59),
6.0:(.08,.40,.33,.58),6.5:(.10,.40,.36,.58),7.0:(.08,.36,.35,.52),7.5:(.12,.34,.31,.49),8.0:(.09,.36,.30,.52),8.5:(.10,.36,.34,.52),9.0:(.10,.36,.33,.52)}
S={4.5:(.64,.52,.92,.85),5.0:(.36,.60,.92,.96),5.5:(.22,.62,.98,.96),6.0:(.22,.58,.95,.95),6.5:(.13,.60,.98,.94),7.0:(.02,.56,1,.90),
7.5:(.06,.56,1,.90),8.0:(.02,.55,1,.89),8.5:(.02,.55,1,.89),9.0:(.02,.56,1,.90)}
c={"mediaId":832,"level":"A","keyWord":"unpack","defaultVoice":"male",
"taps":[{"phrase":"to unpack his suitcase","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to sit on the bed","target":"the purple toy","voice":"male","keys":keys(O)},
{"phrase":"to lie on the floor","target":"the long scarf","voice":"male","keys":keys(S)}],
"stillS":8.5,
"nouns":[{"word":"clothes","x":.17,"y":.14,"voice":"male"},{"word":"a towel","x":.20,"y":.32,"voice":"male"},
{"word":"a suitcase","x":.46,"y":.50,"voice":"male"},{"word":"a scarf","x":.50,"y":.78,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","unpacking","his","suitcase."],"answerVoice":"male",
"notes":"Cartoon with camera changes. The toy octopus appears at 3.0 s (held by the man at 3.0-3.5 s, boxes split between his hands and his head; then it sits on the pillow/bed), the scarf at 4.5 s. Weak spots: while the man pulls the scarf out (4.5-6.0 s) its upper part runs across his body and over his head, so the scarf box covers only the part below the suitcase / on the floor and the upper part lies in the man's box; at 7.5 s the toy is half hidden behind the lifted suitcase (small box); at 7.0 s the man's head is hidden by the suitcase he lifts and the toy sits in front of his left elbow, so his box starts right of the toy and misses his left arm. The man's boots under the bed (0, 2.0, 4.5 s) are outside his box. 'to sit on the bed' = the toy; at 3.0-3.5 s it is still in his hands."}
json.dump(c,open('content/832.json','w'),indent=1)
