import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
G={0.0:(0,0,.42,.33),0.5:(0,0,.40,.34),1.0:(0,.03,.40,.33),1.5:(0,.07,.56,.93),2.0:(0,.13,.56,.87),2.5:(0,.07,.76,.93),
3.0:(0,.08,.72,.92),3.5:(0,.14,.73,.86),4.0:(.02,.07,.72,.80),4.5:(.08,.08,.72,.92),5.0:(.03,.11,.66,.89),5.5:(.10,.15,.68,.85),
6.0:(.10,.15,.80,.85),6.5:(.28,.16,.72,.84),7.0:(.22,.21,.66,.79),7.5:(.22,.22,.66,.78),8.0:(.08,.22,.66,.78),8.5:(0,.20,.88,.80),
9.0:(.17,.20,.67,.80),9.5:(.16,.20,.66,.80),10.0:(.17,.21,.61,.79)}
W={0.0:(.46,0,.54,.32),0.5:(.46,0,.54,.32),1.0:(.46,.02,.54,.32),1.5:(.58,.07,.42,.62),2.0:(.57,.14,.43,.40),2.5:(.78,.07,.22,.55),
3.0:(.73,.18,.27,.56),3.5:(.75,.22,.25,.65),4.0:(.76,.33,.24,.48),4.5:(.82,.52,.18,.40),5.0:(.80,.58,.20,.42)}
c={"mediaId":547,"level":"A","keyWord":"phone","defaultVoice":"female",
"taps":[
 {"phrase":"to talk on the phone","target":"the woman with the braid","voice":"female","keys":keys(G)},
 {"phrase":"to wear glasses","target":"the woman with glasses","voice":"female","keys":keys(W)},
 {"phrase":"to wave her hand","target":"the woman with the braid","voice":"female","keys":keys(G)}],
"stillS":1.5,
"nouns":[{"word":"a phone","x":.56,"y":.72,"voice":"female"},{"word":"a table","x":.28,"y":.62,"voice":"female"},{"word":"flowers","x":.52,"y":.42,"voice":"female"}],
"question":"What is the woman without glasses doing?",
"answer":["She","is","talking","on","the","phone."],
"answerVoice":"female",
"notes":"Two women; the one with glasses is only partly in frame at 0-1.0 s (torso, head cut off) and a sliver at 4.5-5.0 s, off from 5.5 s. 'to wear glasses' is a state: both women hold tea cups, so no action fits only her. A small black bird stands on the wall from 8.0 s; not used (dark, small). Wave is at 8.5-9.0 s only. Dress is teal, so the question avoids a colour."}
json.dump(c,open('content/547.json','w'),indent=1)
