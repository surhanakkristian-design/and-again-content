import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
woman={0.0:(0,.05,1,.95),0.5:(0,0,1,1),1.0:(0,.08,1,.92),6.0:(0,0,.79,.65),6.5:(0,0,.79,.65),
7.0:(0,.07,.50,.62),7.5:(0,.07,.50,.63),8.0:(0,.15,.50,.53),8.5:(0,.18,.50,.52),9.0:(0,.20,.50,.56),9.5:(0,.20,.50,.56),10.0:(0,.20,.49,.50)}
man={2.0:(0,0,.95,.95),2.5:(0,0,.65,.70),3.0:(0,.02,.90,.85),3.5:(0,.08,.92,.92),4.0:(0,0,1,.95),4.5:(0,.05,.58,.87),
5.0:(0,.40,.52,.52),5.5:(0,.28,.62,.65),6.0:(.80,0,.20,.36),6.5:(.80,0,.20,.36),
7.0:(.51,.07,.49,.90),7.5:(.51,.08,.49,.90),8.0:(.51,.14,.29,.86),8.5:(.51,.16,.27,.84),9.0:(.51,.17,.28,.83),9.5:(.51,.17,.28,.83),10.0:(.50,.16,.31,.84)}
cat={8.0:(.81,.08,.19,.20),8.5:(.80,.09,.20,.20),9.0:(.80,.15,.20,.17),9.5:(.80,.13,.20,.17),10.0:(.82,.13,.18,.16)}
c={"mediaId":154,"level":"A","keyWord":"charger","defaultVoice":"male",
"taps":[
 {"phrase":"to shout at her phone","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to look for a charger","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to sit behind the man","target":"the cat","voice":"male","keys":keys(cat)}],
"stillS":8.0,
"nouns":[{"word":"a charger","x":.44,"y":.78,"voice":"male"},{"word":"a phone","x":.60,"y":.68,"voice":"male"},
 {"word":"a cat","x":.88,"y":.20,"voice":"male"},{"word":"tea","x":.15,"y":.69,"voice":"male"}],
"question":"What is the man looking for?",
"answer":["He","is","looking","for","a","charger."],
"answerVoice":"male",
"notes":"6.0-6.5 close-up of hands: owner of the hands unclear (red shirt behind = woman, so the left part is boxed as the woman; the grey sliver top right as the man). 8.0-10.0 the man's box is cut at x~0.80 so it does not overlap the cat behind his shoulder (his right shoulder is outside the box). Cat is partly hidden at 7.0-7.5 (off). Charger and phone pills are close (0.10 in y). defaultVoice male: the man does most of the action, could also be female."}
json.dump(c,open("content/154.json","w"),indent=1)
