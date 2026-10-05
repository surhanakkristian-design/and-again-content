import json
T=[i*0.5 for i in range(30)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
dog={0.0:(.37,.26,.25,.17),0.5:(.39,.27,.25,.16),1.0:(.42,.29,.23,.16),1.5:(.44,.30,.23,.16),2.0:(.44,.30,.23,.15),2.5:(.44,.31,.23,.14),
3.0:(.44,.32,.23,.14),3.5:(.44,.32,.23,.15),4.0:(.44,.32,.24,.15),4.5:(.44,.39,.23,.19),5.0:(.47,.50,.29,.19),5.5:(.61,.51,.38,.19),
6.0:(.71,.52,.28,.18),6.5:(.55,.49,.36,.21),7.0:(.33,.50,.40,.21),7.5:(.17,.50,.36,.21),8.0:(.20,.52,.25,.20),8.5:(.21,.55,.21,.18),
9.0:(.21,.57,.23,.19),9.5:(.22,.57,.20,.19),10.0:(.28,.60,.20,.17),10.5:(.37,.60,.24,.16),11.0:(.44,.58,.22,.17),11.5:(.45,.55,.20,.18),
12.0:(.39,.32,.20,.16),12.5:(.37,.30,.20,.16),13.0:(.41,.31,.20,.14),13.5:(.44,.32,.19,.14),14.0:(.42,.32,.19,.14),14.5:(.43,.32,.19,.14)}
man={7.0:(0,.28,.14,.32),7.5:(0,.29,.16,.32),8.0:(0,.28,.19,.34),8.5:(.05,.30,.15,.33),9.0:(.08,.34,.13,.30),9.5:(.08,.37,.14,.26),
10.0:(.09,.37,.18,.27),10.5:(.08,.40,.19,.25),11.0:(.13,.42,.20,.21),12.0:(.13,.40,.22,.23),12.5:(0,.34,.26,.28)}
bike={0.0:(.25,.55,.38,.20),0.5:(.29,.55,.36,.18),1.0:(.36,.54,.30,.18),1.5:(.39,.54,.30,.17),2.0:(.39,.53,.29,.17),2.5:(.39,.53,.30,.17),
3.0:(.39,.54,.29,.17),3.5:(.38,.54,.30,.16),4.0:(.35,.55,.30,.14),9.0:(.30,.49,.26,.08),9.5:(.42,.48,.17,.20),10.0:(.35,.47,.24,.13),
10.5:(.34,.47,.26,.12),11.0:(.34,.48,.26,.10),11.5:(.34,.47,.26,.08),12.0:(.36,.48,.24,.16),12.5:(.37,.48,.24,.15),13.0:(.39,.51,.23,.14),
13.5:(.40,.51,.22,.14),14.0:(.40,.48,.22,.14),14.5:(.41,.48,.20,.14)}
c={"mediaId":4099,"level":"A","keyWord":"back","defaultVoice":"male",
"taps":[{"phrase":"to sit on the mattresses","target":"the dog","voice":"male","keys":keys(dog)},
{"phrase":"to wear a red shirt","target":"the man in the red shirt","voice":"male","keys":keys(man)},
{"phrase":"to carry the mattresses","target":"the motorbike","voice":"male","keys":keys(bike)}],
"stillS":2.5,
"nouns":[{"word":"buildings","x":.45,"y":.25,"voice":"male"},{"word":"a dog","x":.56,"y":.38,"voice":"male"},
{"word":"mattresses","x":.56,"y":.49,"voice":"male"},{"word":"a motorbike","x":.54,"y":.62,"voice":"male"}],
"question":"Where is the dog sitting?",
"answer":["It","is","sitting","on","the","mattresses."],"answerVoice":"male",
"notes":"Key word 'back' is an adverb, not placed as a noun and not used in the texts (the dog jumps back up at 12 s). Motorbike is hidden behind the fallen mattresses 4.5-8.5 s (off) and partly behind the dog 9-11.5 s (slim boxes split from the dog). Man in the red shirt only visible 7-12.5 s (11.5 hidden behind the load). 'to carry the mattresses': the two men lift them back, but only the motorbike carries them along the road. Second man (rider, dark clothes) is not a target."}
json.dump(c,open('content/4099.json','w'),indent=1)
