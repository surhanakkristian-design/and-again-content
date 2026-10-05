import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
W={3.5:(.52,.13,.48,.62),4.0:(.36,.11,.46,.41),4.5:(.15,.12,.45,.40),5.0:(.05,.13,.39,.49),5.5:(.03,.17,.34,.52),
6.0:(.02,.17,.33,.50),6.5:(.03,.17,.33,.48),7.0:(.0,.18,.40,.52),7.5:(.0,.19,.42,.58),8.0:(.0,.18,.43,.50),
8.5:(.0,.19,.40,.50),9.0:(.0,.19,.37,.58),9.5:(.0,.18,.41,.52),10.0:(.0,.17,.45,.52)}
M={4.5:(.78,.05,.22,.65),5.0:(.62,.07,.38,.80),5.5:(.55,.09,.45,.78),6.0:(.53,.08,.47,.72),6.5:(.54,.09,.46,.72),
7.0:(.58,.11,.42,.72),7.5:(.60,.13,.40,.70),8.0:(.61,.12,.39,.68),8.5:(.58,.12,.42,.70),9.0:(.55,.12,.45,.80),
9.5:(.59,.14,.41,.72),10.0:(.63,.11,.37,.72)}
D={4.0:(.82,.18,.18,.14),4.5:(.60,.19,.18,.14),5.0:(.44,.22,.18,.14),5.5:(.37,.23,.18,.14),6.0:(.35,.23,.18,.14),
6.5:(.36,.22,.18,.14),7.0:(.40,.23,.18,.14),7.5:(.42,.24,.18,.14),8.0:(.43,.23,.18,.14),8.5:(.40,.23,.18,.14),
9.0:(.37,.23,.18,.14),9.5:(.41,.22,.18,.14),10.0:(.45,.23,.18,.14)}
c={"mediaId":360,"level":"A","keyWord":"hand sanitizer","defaultVoice":"female",
"taps":[{"phrase":"to look over the seat","target":"the dog","voice":"female","keys":keys(D)},
{"phrase":"to have a black beard","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to sit beside the man","target":"the woman next to the man","voice":"female","keys":keys(W)}],
"stillS":10.0,
"nouns":[{"word":"hand sanitizer","x":.22,"y":.77,"voice":"female"},{"word":"a dog","x":.56,"y":.32,"voice":"female"},
{"word":"a man","x":.78,"y":.62,"voice":"male"},{"word":"a table","x":.58,"y":.88,"voice":"female"}],
"question":"What are they putting on their hands?",
"answer":["They","are","putting","hand sanitizer","on","their","hands."],"answerVoice":"female",
"notes":"Two women in teal: the camera-side woman with the braid (0-3 s, later only her arms from the bottom left) and the woman seated next to the man (from 3.5 s). The woman target is the seated one only; the first woman is never boxed. Man and seated woman do the same actions as the first woman (rub hands, eat, drink), so the man got a state phrase. The man's stretched-out hands are often outside his box because they lie in front of the woman / dog; the dog sits between the two heads, so the woman's right shoulder and the man's left edge are cut by the dog box. 'hand sanitizer' kept as one chip."}
json.dump(c,open("content/360.json","w"),indent=1)
