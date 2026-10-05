import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={0.0:(.46,.42,.54,.26),0.5:(.62,.50,.38,.23),1.0:(.82,.58,.18,.24),2.0:(.76,0,.24,.32),2.5:(.56,.13,.44,.67),
3.0:(.50,.17,.50,.73),3.5:(.24,.09,.76,.78),4.0:(.18,.15,.82,.72),4.5:(.18,.15,.82,.72),5.0:(.32,.12,.68,.86),
5.5:(.69,.30,.31,.56),6.0:(.69,.38,.31,.48),6.5:(.76,.38,.24,.48),9.0:(.46,.57,.54,.33),9.5:(.58,.18,.42,.64),10.0:(.57,.26,.43,.74)}
M={5.5:(0,.09,.67,.91),6.0:(0,.10,.67,.88),6.5:(0,.12,.68,.86),9.5:(0,.18,.44,.82),10.0:(0,.26,.44,.74)}
c={"mediaId":316,"level":"A","keyWord":"freezer","defaultVoice":"female",
"taps":[
{"phrase":"to open the freezer","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to hold a bag of peas","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to hold the ice cream","target":"the man","voice":"male","keys":keys(M)}],
"stillS":6.0,
"nouns":[{"word":"a spoon","x":.76,"y":.45,"voice":"female"},{"word":"ice cream","x":.52,"y":.62,"voice":"female"},
{"word":"a hat","x":.14,"y":.26,"voice":"female"},{"word":"a freezer","x":.65,"y":.86,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","holding","a","bag","of","peas."],
"answerVoice":"female",
"notes":"The woman opens the freezer at 0.0-1.0 s with only her arm in the picture (beige sleeve; she closes it at 9.0 s). At 5.5-6.5 s the hand with the spoon at the right is taken as the woman's (same beige sleeve) and boxed as the woman. 7.0-8.0 s: a hand shows a bag of berries and one berry, owner not identifiable -> both targets off. 'a freezer' at 6.0 s sits on the open freezer drawer seen from above (weak spot: only the drawer is visible there)."}
json.dump(c,open("content/316.json","w"),indent=1,ensure_ascii=False)
