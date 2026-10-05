import json
W="the woman in blue"; M="the man"; G="the woman with glasses"
OFF=None
K={
0.0:((.10,.31,.80,.50),OFF,OFF),
0.5:((.36,.32,.56,.48),(0,.18,.35,.40),OFF),
1.0:((.06,.44,.88,.42),(0,.15,.82,.28),OFF),
1.5:((.33,.31,.67,.67),(0,.09,.32,.50),OFF),
2.0:((.32,.29,.35,.69),(0,.08,.31,.48),(.68,.22,.32,.42)),
2.5:((.28,.27,.41,.71),(0,0,.27,.56),(.70,.24,.30,.40)),
3.0:((.27,.11,.42,.87),(0,.12,.26,.50),(.70,.18,.30,.44)),
3.5:((.28,.09,.43,.89),(0,.08,.27,.56),(.72,.18,.28,.44)),
4.0:((.31,.08,.39,.92),(0,.04,.30,.50),(.71,.11,.29,.46)),
4.5:((.31,.08,.40,.92),(0,.04,.30,.50),(.72,.11,.28,.50)),
5.0:((.31,.08,.42,.92),(0,.06,.30,.56),(.74,.20,.26,.48)),
5.5:((0,0,.62,.68),OFF,OFF),
6.0:((0,0,.62,.78),OFF,OFF),
6.5:((0,0,.65,1),OFF,OFF),
7.0:((0,0,.65,1),OFF,OFF),
7.5:((.36,.14,.33,.80),(0,.20,.35,.42),(.70,.20,.30,.65)),
8.0:((.37,.18,.31,.62),(0,.20,.36,.34),(.70,.20,.30,.54)),
8.5:((.37,.18,.30,.62),(0,.24,.36,.32),(.68,.24,.32,.50)),
9.0:((.37,.18,.30,.74),(0,.27,.36,.35),(.68,.24,.32,.58)),
}
def keys(i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
d={"mediaId":655,"level":"A","keyWord":"serious","defaultVoice":"female",
"taps":[
 {"phrase":"to paint a black line","target":W,"voice":"female","keys":keys(0)},
 {"phrase":"to run into the room","target":M,"voice":"male","keys":keys(1)},
 {"phrase":"to blow a small horn","target":G,"voice":"female","keys":keys(2)}],
"stillS":8.0,
"nouns":[{"word":"a hat","x":.50,"y":.27,"voice":"female"},
 {"word":"glasses","x":.82,"y":.37,"voice":"female"},
 {"word":"paper","x":.58,"y":.78,"voice":"female"},
 {"word":"a table","x":.50,"y":.88,"voice":"female"}],
"question":"What is the woman in blue doing?",
"answer":["She","is","painting","a","black","line","on","paper."],
"answerVoice":"female",
"notes":"Three people stand very close; boxes are split, so the woman in blue's box holds her head and body but not always her arms where the man is in front/behind (0.5, 1.5, 7.5-9.0 s). At 1.0 s the man is directly behind her: split horizontally at y 0.43-0.44 (his box takes her hair bun). 5.5-7.0 s is a top-down close-up of her arm painting the line; her box covers arm and line. The friend with orange glasses is read as a woman (ponytail) - verifier please check; voice female. The man runs in at 0.5-1.0 s; horn at 2.0-2.5 s only. Both friends hold spoons over their eyes, so not used. Key word 'serious' is an adjective, not placed."}
json.dump(d,open("content/655.json","w"),indent=1,ensure_ascii=False)
