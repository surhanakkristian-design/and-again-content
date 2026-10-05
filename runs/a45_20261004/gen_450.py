import json
def keys(d,T):
    out=[]
    for t in T:
        b=d.get(t)
        if not b: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=b
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
T=[i*0.5 for i in range(21)]
L={0.0:(0,.26,1,.64),0.5:(0,.26,1,.64),1.0:(0,.28,1,.66),1.5:(0,.28,1,.66),2.0:(0,.26,.96,.63),2.5:(0,.19,1,.62),3.0:(0,.21,.96,.66),
3.5:(0,.22,1,.67),4.0:(0,.27,1,.67),4.5:(0,.34,.92,.66),5.0:(0,.42,.55,.57),6.0:(.18,.78,.50,1),6.5:(.28,.46,.56,.87),7.0:(.37,.36,.70,.94),
7.5:(.42,.26,.77,.84),8.0:(.32,.20,.71,.75),8.5:(.35,.17,.67,.88),9.0:(.35,.20,.70,.92),9.5:(.37,.20,.70,.91),10.0:(.37,.20,.71,.94)}
k=keys(L,T)
c={"mediaId":450,"level":"A","keyWord":"lizard","defaultVoice":"female",
"taps":[{"phrase":"to sit in the sun","target":"the lizard","voice":"female","keys":k},
{"phrase":"to lift its head","target":"the lizard","voice":"female","keys":k},
{"phrase":"to climb up the wall","target":"the lizard","voice":"female","keys":k}],
"stillS":4.0,
"nouns":[{"word":"a cactus","x":0.30,"y":0.06,"voice":"female"},{"word":"a shadow","x":0.74,"y":0.21,"voice":"female"},
{"word":"a lizard","x":0.42,"y":0.44,"voice":"female"},{"word":"a stone","x":0.50,"y":0.82,"voice":"female"}],
"question":"What is the lizard doing?",
"answer":["It","is","climbing","up","the","wall."],"answerVoice":"female",
"notes":"Only one possible target (the lizard), used for all three phrases. 5.0: only its tail shows under the cactus (thin box); 5.5: only the cactus -> off. The cactus is only a strip at the top of the 4.0 still (pill sits on it); the shadow pill is on the big shadow top right (the lizard has a small shadow of its own under it). No person: evenId true -> female."}
json.dump(c,open('content/450.json','w'),indent=1)
