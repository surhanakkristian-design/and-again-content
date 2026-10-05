import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
P={0.0:(.08,.34,.92,.46),0.5:(.08,.34,.92,.46),1.0:(0,.34,1,.48),1.5:(0,.34,1,.50),2.0:(0,.24,1,.57),2.5:(.08,.05,.84,.76),
3.0:(.02,0,.98,.88),3.5:(0,0,.96,.88),4.0:(.06,0,.94,.75),4.5:(.07,0,.93,.75),5.0:(.08,.02,.86,.88),5.5:(0,.05,.94,.86),
6.0:(.07,.13,.82,.67),6.5:(.21,.07,.63,.66),7.0:(0,.22,1,.55),7.5:(0,.26,1,.54),8.0:(0,.26,1,.56),8.5:(0,.21,.90,.50),
9.0:(.04,.22,.84,.66),9.5:(.04,.23,.84,.65),10.0:(.02,.23,.86,.70)}
M={8.0:(.72,0,.28,.25),8.5:(.22,0,.70,.20),9.0:(.20,0,.78,.21),9.5:(.18,0,.78,.22),10.0:(.18,0,.76,.22)}
c={"mediaId":550,"level":"A","keyWord":"pig","defaultVoice":"female",
"taps":[
 {"phrase":"to lie in the mud","target":"the pig","voice":"female","keys":keys(P)},
 {"phrase":"to stand behind the pig","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to drink from a bucket","target":"the pig","voice":"female","keys":keys(P)}],
"stillS":10.0,
"nouns":[{"word":"a pig","x":.38,"y":.42,"voice":"female"},{"word":"a bucket","x":.50,"y":.78,"voice":"female"},{"word":"a man","x":.50,"y":.12,"voice":"male"},{"word":"a fence","x":.88,"y":.30,"voice":"female"}],
"question":"What is the pig drinking from?",
"answer":["The","pig","is","drinking","from","a","bucket."],
"answerVoice":"female",
"notes":"The man appears only from 8.0 s, behind the pig; his face is cut off by the top edge. Where pig and man overlap (8.5-10.0 s) the boxes are split on the pig's back line, so the man's box is his upper body only. Pig lies in the mud 0-1.5 s, drinks 8.5-10.0 s. The fence is the wooden posts with wire at the right edge."}
json.dump(c,open('content/550.json','w'),indent=1)
