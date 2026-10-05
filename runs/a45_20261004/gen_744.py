import json
OFF=None
# t: (man, woman)
K={
0.0:(OFF,(.18,.18,.76,.56)),
0.5:((.06,0,.42,.46),(.50,.25,.50,.44)),
1.0:((.05,.26,.55,.50),(.61,.50,.39,.50)),
1.5:((0,0,.62,.80),(.64,.03,.36,.76)),
2.0:((0,0,.50,.90),(.51,.03,.49,.62)),
2.5:((0,0,.48,.80),(.50,.02,.50,.62)),
3.0:((0,.08,.56,.84),(.58,.15,.42,.72)),
3.5:((0,.18,.50,.82),(.60,.30,.40,.70)),
4.0:((0,.10,.50,.90),(.60,.22,.40,.78)),
4.5:((.05,.25,.50,.75),(.56,.34,.44,.66)),
5.0:((.03,.30,.41,.70),(.45,.37,.50,.63)),
5.5:((0,.28,.48,.72),(.50,.36,.48,.64)),
6.0:((0,.25,.54,.75),(.57,.34,.43,.66)),
6.5:((0,.22,.51,.78),(.52,.33,.48,.67)),
7.0:((0,.24,.41,.76),(.42,.38,.53,.62)),
7.5:((0,.25,.39,.75),(.40,.37,.42,.63)),
8.0:((0,.20,.40,.80),(.41,.31,.37,.66)),
8.5:((0,.16,.38,.84),(.46,.24,.33,.62)),
9.0:((0,.17,.38,.83),(.50,.27,.28,.42)),
9.5:((0,.15,.36,.85),OFF),
10.0:((0,.13,.45,.87),OFF),
}
def keys(i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
d={"mediaId":744,"level":"A","keyWord":"stranger","defaultVoice":"female",
"taps":[
 {"phrase":"to hold an umbrella","target":"the man","voice":"male","keys":keys(0)},
 {"phrase":"to drop her papers","target":"the woman","voice":"female","keys":keys(1)},
 {"phrase":"to get on the bus","target":"the woman","voice":"female","keys":keys(1)}],
"stillS":6.0,
"nouns":[{"word":"an umbrella","x":.45,"y":.16,"voice":"female"},
 {"word":"a bus","x":.52,"y":.36,"voice":"female"},
 {"word":"a man","x":.20,"y":.62,"voice":"male"},
 {"word":"papers","x":.70,"y":.58,"voice":"female"}],
"question":"What is the man holding?",
"answer":["He","is","holding","an","umbrella","over","her."],
"answerVoice":"male",
"notes":"Only two usable targets: the red bus is behind both people from 5.0 s on, so a bus box would overlap theirs; the woman has two phrases. Key word 'stranger' cannot be seen as such (the man is the stranger), so the noun slot says 'a man'. Both people pick up papers, so that action is not used. The man also holds the closed umbrella at 0.5 s. Woman hidden behind the closed bus doors at 9.5-10.0 s. At 1.0-3.0 s the two crouch close together: boxes split between them, hands reach across."}
json.dump(d,open("content/744.json","w"),indent=1,ensure_ascii=False)
