import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x,y,w,h=b; w=min(w,round(1-x,2)); h=min(h,round(1-y,2))
        out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
    return out
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1)
# 5714
sq=K([(.08,.36,.52,.31),(.06,.37,.50,.30),(.06,.37,.50,.30),(.00,.43,.70,.24),(.36,.48,.48,.38),(.36,.52,.49,.25),(.38,.41,.40,.20),(.30,.40,.33,.21)])
save({"mediaId":5714,"level":"B","keyWord":"cemetery","defaultVoice":"female",
 "taps":[{"phrase":"to nibble a pine cone","target":"the squirrel","voice":"female","keys":sq},
         {"phrase":"to leap off a gravestone","target":"the squirrel","voice":"female","keys":sq},
         {"phrase":"to scamper across frosty grass","target":"the squirrel","voice":"female","keys":sq}],
 "stillS":3.7,
 "nouns":[{"word":"pine trees","x":0.50,"y":0.22,"voice":"female"},{"word":"a squirrel","x":0.47,"y":0.50,"voice":"female"},
          {"word":"a gravestone","x":0.47,"y":0.62,"voice":"female"},{"word":"grass","x":0.50,"y":0.85,"voice":"female"}],
 "question":"What is the squirrel doing?","answer":["The","squirrel","is","nibbling","a","pine","cone."],"answerVoice":"female",
 "notes":"Only one possible target (the squirrel), used for all three phrases. 'cemetery' is the whole scene, not placed as a noun. Grass is frosty/mossy."})
# 5715
fr=[(.57,.17,.43,.80),(.57,.17,.43,.80),(.57,.17,.43,.80),(.57,.17,.43,.80),(.57,.15,.43,.82),(.57,.14,.43,.83),(.57,.12,.43,.85),(.57,.11,.43,.86)]
bk=[(.30,.26,.27,.24)]*8
f=K(fr)
save({"mediaId":5715,"level":"B","keyWord":"censorship","defaultVoice":"female",
 "taps":[{"phrase":"to slice a handwritten letter","target":"the woman in front","voice":"female","keys":f},
         {"phrase":"to steady a metal ruler","target":"the woman in front","voice":"female","keys":f},
         {"phrase":"to sit beneath a stone arch","target":"the woman at the back","voice":"female","keys":K(bk)}],
 "stillS":2.2,
 "nouns":[{"word":"a stone arch","x":0.38,"y":0.22,"voice":"female"},{"word":"a desk lamp","x":0.14,"y":0.34,"voice":"female"},
          {"word":"envelopes","x":0.30,"y":0.51,"voice":"female"},{"word":"a letter","x":0.30,"y":0.60,"voice":"female"}],
 "question":"What is the woman in front doing?","answer":["She","is","cutting","a","letter","with","a","blade."],"answerVoice":"female",
 "notes":"Front woman's box split vertically at x=.57 from the back woman's box, so her hands/ruler (x .40-.57) fall outside her box. Two women both in green, named by position."})
# 5716
wm=K([(.05,.25,.37,.60),(.05,.26,.29,.58),(.00,.26,.32,.58),(.03,.26,.34,.58),(.10,.24,.30,.59),(.08,.24,.29,.61),(.05,.24,.28,.61),(.03,.24,.32,.61)])
pg=K([(.42,.56,.58,.15),(.34,.56,.66,.15),(.32,.56,.68,.15),(.37,.56,.63,.15),(.40,.56,.60,.15),(.37,.56,.63,.15),(.33,.56,.67,.15),(.35,.56,.65,.15)])
pp=K([(.73,.41,.27,.14),(.71,.41,.29,.14),(.68,.41,.29,.14),(.66,.41,.28,.14),(.64,.41,.26,.14),(.62,.41,.24,.14),(.60,.42,.24,.13),(.52,.41,.28,.14)])
save({"mediaId":5716,"level":"B","keyWord":"census","defaultVoice":"female",
 "taps":[{"phrase":"to point at each penguin","target":"the woman","voice":"female","keys":wm},
         {"phrase":"to waddle along the shore","target":"the penguins","voice":"female","keys":pg},
         {"phrase":"to gather around a box","target":"the people in the distance","voice":"female","keys":pp}],
 "stillS":0.7,
 "nouns":[{"word":"a beanie","x":0.25,"y":0.32,"voice":"female"},{"word":"an iceberg","x":0.52,"y":0.41,"voice":"female"},
          {"word":"penguins","x":0.70,"y":0.62,"voice":"female"},{"word":"a backpack","x":0.38,"y":0.71,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","counting","the","penguins","on","the","shore."],"answerVoice":"female",
 "notes":"Woman's box stops before the penguin line, so her pointing arm/hand is outside it. Distant group: two bend over the white box, one stands just behind. Counting is shown by pointing (and the 'Five, six' voice)."})
# 5717
wo=K([(.04,.41,.78,.51),(.10,.41,.72,.47),(.15,.42,.68,.46),(.13,.42,.68,.45),(.14,.43,.61,.42),(.20,.44,.46,.39),(.26,.45,.43,.34),(.27,.45,.47,.33)])
bd=K([(.08,.09,.54,.17),(.17,.11,.50,.18),(.20,.14,.64,.15),(.26,.17,.66,.15),(.20,.18,.72,.13),(.22,.19,.73,.14),(.34,.19,.66,.15),(.35,.21,.46,.14)])
save({"mediaId":5717,"level":"A","keyWord":"center","defaultVoice":"female",
 "taps":[{"phrase":"to spin round and round","target":"the woman","voice":"female","keys":wo},
         {"phrase":"to hold her arms out","target":"the woman","voice":"female","keys":wo},
         {"phrase":"to fly over the walls","target":"the birds","voice":"female","keys":bd}],
 "stillS":3.7,
 "nouns":[{"word":"the sky","x":0.50,"y":0.10,"voice":"female"},{"word":"a woman","x":0.52,"y":0.56,"voice":"female"},
          {"word":"sand","x":0.18,"y":0.68,"voice":"female"},{"word":"a circle","x":0.50,"y":0.86,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","spinning","in","the","center."],"answerVoice":"female",
 "notes":"Birds are small and scattered; one group box over all of them. 'center' kept in the keyword's US spelling."})
