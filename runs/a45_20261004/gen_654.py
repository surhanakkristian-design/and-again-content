import json
Y="the woman in yellow"; G="the woman with glasses"; M="the man"
OFF=None
# t: (Y, G, M)
K={
0.0:((.31,.43,.18,.19),(.50,.43,.18,.19),OFF),
0.5:((.31,.43,.18,.19),(.50,.43,.18,.19),OFF),
1.0:((0,.24,.62,.76),(.63,.24,.37,.76),OFF),
1.5:((0,.25,.55,.75),(.56,.25,.44,.75),OFF),
2.0:((0,0,.57,1),(.58,0,.42,1),OFF),
2.5:((0,0,.57,1),(.58,0,.42,1),OFF),
3.0:((0,0,.57,1),(.58,0,.42,1),OFF),
3.5:((0,.05,.57,.95),(.58,.05,.42,.95),OFF),
4.0:((0,0,.52,1),(.53,0,.47,1),OFF),
4.5:((0,0,.51,1),(.52,0,.48,1),OFF),
5.0:((0,.05,.52,.95),(.53,.05,.47,.95),OFF),
5.5:((0,.08,.51,.92),(.52,.05,.48,.95),OFF),
6.0:(OFF,OFF,(.30,.58,.28,.30)),
6.5:(OFF,OFF,(.31,.42,.48,.48)),
7.0:((0,.27,.48,.73),(.50,.27,.50,.73),OFF),
7.5:((0,.27,.48,.73),(.50,.27,.50,.73),OFF),
8.0:((0,.26,.48,.74),(.50,.26,.50,.74),OFF),
8.5:((0,.26,.48,.74),(.50,.26,.50,.74),OFF),
9.0:((0,.03,.49,.97),(.50,.03,.50,.97),OFF),
9.5:((0,.05,.49,.95),(.50,.05,.50,.95),OFF),
10.0:((0,.05,.48,.95),(.49,.05,.51,.95),OFF),
}
def keys(i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
d={"mediaId":654,"level":"A","keyWord":"secret","defaultVoice":"female",
"taps":[
 {"phrase":"to whisper a secret","target":Y,"voice":"female","keys":keys(0)},
 {"phrase":"to listen to her friend","target":G,"voice":"female","keys":keys(1)},
 {"phrase":"to look over the wall","target":M,"voice":"male","keys":keys(2)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":.60,"y":.11,"voice":"female"},
 {"word":"a lantern","x":.19,"y":.25,"voice":"female"},
 {"word":"a mountain","x":.62,"y":.23,"voice":"female"},
 {"word":"glasses","x":.75,"y":.41,"voice":"female"}],
"question":"What is the woman in yellow doing?",
"answer":["She","is","whispering","a","secret","to","her","friend."],
"answerVoice":"female",
"notes":"Close-ups 1.0-5.5 s and 9.0-10.0 s: the two women overlap, boxes split along the line between the faces; the whispering hand of the woman in yellow (2.0-3.0 s) reaches into the other woman's box. Man only at 6.0-6.5 s. Both women put a finger to their lips, so that action is not used. 'to listen to her friend' = the woman with glasses while being whispered to (2-3 s). A second lantern is cut by the top right corner at 8.0 s; the pill is on the full one on the left. A small key floats at the mouth at 5.5 s (clip effect), not used."}
json.dump(d,open("content/654.json","w"),indent=1,ensure_ascii=False)
