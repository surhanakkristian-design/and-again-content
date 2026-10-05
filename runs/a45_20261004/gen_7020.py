import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in zip(T,b)]
man=[(.30,.29,.49,.54),(.13,.30,.57,.57),(.29,.29,.57,.56),(.28,.32,.45,.56),(.28,.31,.43,.58),(.29,.30,.43,.63),(.29,.29,.43,.67),(.29,.28,.43,.68)]
old=[(.80,.36,.20,.42),(.77,.38,.23,.40),(.86,.38,.14,.42),(.80,.37,.20,.43),(.80,.37,.20,.43),(.80,.37,.20,.44),(.80,.37,.20,.45),(.80,.38,.20,.45)]
bucket=[(.70,.83,.25,.13),(.71,.82,.26,.15),(.69,.85,.27,.14),(.73,.84,.25,.15),(.71,.86,.27,.14),(.72,.87,.28,.13),(.72,.86,.22,.14),(.72,.86,.22,.14)]
c={"mediaId":7020,"level":"B","keyWord":"darling","defaultVoice":"female",
"taps":[
 {"phrase":"to embrace a woman in red","target":"the man in the camel coat","voice":"male","keys":K(man)},
 {"phrase":"to tip his hat","target":"the old man on the right","voice":"male","keys":K(old)},
 {"phrase":"to lie on its side","target":"the metal bucket","voice":"female","keys":K(bucket)}],
"stillS":2.2,
"nouns":[{"word":"a clock","x":0.68,"y":0.29,"voice":"female"},{"word":"a lantern","x":0.71,"y":0.16,"voice":"female"},
 {"word":"a suitcase","x":0.22,"y":0.90,"voice":"female"},{"word":"a steam train","x":0.16,"y":0.34,"voice":"female"}],
"question":"What is the couple doing?",
"answer":["They","are","embracing","on","the","platform."],
"answerVoice":"female",
"notes":"Man and woman overlap completely, so only the man is a tap target (his box covers the hugging pair). Old man tips/raises his hat mainly at 0.2-0.7 s, then holds it at his chest. Bucket is cut by the bottom edge at 3.2-3.7 s. Key word 'darling' is not a visible noun; defaultVoice female (mixed couple, evenId true)."}
json.dump(c,open('content/7020.json','w'),indent=1)
