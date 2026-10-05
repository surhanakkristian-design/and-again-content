import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)})
    return out
# x0,y0,x1,y1
W={0.0:(.08,0,.80,.87),0.5:(.08,0,.82,.87),1.0:(.16,.18,.80,.87),1.5:(0,0,1,1),2.0:(.18,.14,.80,.87),2.5:(.18,.14,.82,.87),
3.0:(.08,.13,.80,.87),3.5:(.08,.13,.82,.87),4.0:(.08,.10,.80,.87),4.5:(.08,.10,.82,.87),5.0:(.08,.10,.78,.87),5.5:(.08,.10,.80,.87),
6.0:(.18,.09,.84,.87),6.5:(.22,.22,.95,.88),7.0:(.20,.28,1,.89),7.5:(.17,.30,.99,.90),8.0:(.16,.34,.94,.85),8.5:(.14,.34,.95,.84),
9.0:(.13,.36,.92,.91),9.5:(.15,.36,.92,.91),10.0:(.11,.33,.90,.81)}
M={0.0:(.55,.88,.80,1),0.5:(.56,.88,.80,1),1.0:(.52,.88,.78,1),1.5:None,2.0:(.52,.88,.76,1),2.5:(.55,.88,.79,1),3.0:(.52,.88,.76,1),
3.5:(.54,.88,.78,1),4.0:(.52,.88,.76,1),4.5:(.53,.88,.77,1),5.0:(.48,.88,.74,1),5.5:(.52,.88,.76,1),6.0:(.50,.88,.74,1),
6.5:(.52,.89,.76,1),7.0:(.50,.90,.75,1),7.5:(.50,.91,.75,1),8.0:(.50,.86,.74,1),8.5:(.52,.86,.76,1),9.0:(.50,.92,.74,1),
9.5:(.52,.92,.76,1),10.0:(.50,.86,.76,1)}
c={"mediaId":812,"level":"B","keyWord":"trust","defaultVoice":"female",
"taps":[{"phrase":"to dangle from a rope","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to secure the rope below","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to spread her arms wide","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":8.5,
"nouns":[{"word":"a rope","x":.25,"y":.17,"voice":"female"},{"word":"a harness","x":.68,"y":.50,"voice":"female"},
{"word":"a cliff","x":.20,"y":.86,"voice":"female"},{"word":"trees","x":.72,"y":.68,"voice":"female"}],
"question":"What is the climber doing?","answer":["She","is","dangling","from","a","rope."],"answerVoice":"female",
"notes":"The man (belayer) is tiny at the bottom edge and partly cut off; his box is thin (split from the woman's box) and at 9.5-10.0 only his head shows. 1.5 s is a close-up of the woman's hands on the knot: whole frame = the woman. Key word 'trust' is abstract, not used as a noun."}
json.dump(c,open('content/812.json','w'),indent=1)
