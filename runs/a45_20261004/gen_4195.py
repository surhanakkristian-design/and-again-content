import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
sun={0.0:(.45,.22,.20,.14),0.5:(.45,.22,.20,.14),1.0:(.45,.23,.20,.14),1.5:(.44,.23,.20,.14),2.0:(.44,.22,.20,.14),
2.5:(.43,.22,.20,.14),3.0:(.42,.21,.20,.14),3.5:(.40,.20,.20,.14),4.0:(.40,.16,.20,.14),4.5:(.43,.27,.20,.13),
5.0:(.42,.21,.20,.14),5.5:(.42,.17,.20,.14),6.0:(.44,.15,.20,.14),6.5:(.45,.13,.20,.14),7.0:(.45,.11,.20,.14),
7.5:(.47,.06,.20,.14),8.0:(.45,.0,.22,.14)}
sc={}
for t in [0,.5,1,1.5,2,2.5,3,3.5,4]: sc[float(t)]=(.20,.51,.60,.49)
sc.update({4.5:(.22,.41,.62,.59),5.0:(.20,.42,.62,.58),5.5:(.20,.42,.62,.58),6.0:(.18,.41,.64,.59),6.5:(.18,.52,.64,.48),
7.0:(.20,.60,.60,.40),7.5:(.22,.52,.60,.48),8.0:(.22,.47,.58,.53),8.5:(.25,.46,.58,.54),9.0:(.24,.45,.56,.55),
9.5:(.18,.58,.66,.42),10.0:(.08,.52,.72,.48),10.5:(.08,.47,.70,.53),11.0:(.08,.48,.70,.52),11.5:(.08,.50,.70,.50),12.0:(.08,.49,.70,.51)})
wh={9.5:(.48,.44,.20,.14),10.0:(.60,.36,.20,.15),10.5:(.47,.32,.22,.14),11.0:(.49,.33,.22,.14),11.5:(.49,.34,.22,.15),12.0:(.48,.33,.22,.15)}
c={"mediaId":4195,"level":"A","keyWord":"break","defaultVoice":"male",
"taps":[{"phrase":"to break into pieces","target":"the scooter","voice":"male","keys":K(sc)},
{"phrase":"to shine in the sky","target":"the sun","voice":"male","keys":K(sun)},
{"phrase":"to roll across the road","target":"the wheel","voice":"male","keys":K(wh)}],
"stillS":12.0,
"nouns":[{"word":"a wheel","x":.59,"y":.41,"voice":"male"},{"word":"a basket","x":.34,"y":.52,"voice":"male"},
{"word":"shoes","x":.50,"y":.88,"voice":"male"},{"word":"the road","x":.60,"y":.15,"voice":"male"}],
"question":"What is happening to the scooter?",
"answer":["The","scooter","is","breaking","into","pieces."],"answerVoice":"male",
"notes":"First-person clip; rider only seen as arms/knees (male, default voice male). Scooter box includes the hands on the handlebars. The wheel is only visible from 9.5 s; from 9.5 s the scooter box is cut below the wheel box, so the basket top falls outside it. Sun leaves the frame after 8.0 s."}
json.dump(c,open("content/4195.json","w"),indent=1)
