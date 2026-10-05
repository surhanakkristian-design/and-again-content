import json
W="the woman"; M="the man"
OFF=None
K={
0.0:((0,.20,.95,.80),OFF),
0.5:((.05,.17,.95,.83),OFF),
1.0:((.02,.13,.98,.87),OFF),
1.5:((0,.05,.81,.85),(.82,.34,.18,.50)),
2.0:((0,0,.72,.60),(.73,.18,.27,.60)),
2.5:((0,0,.56,.86),(.57,.17,.43,.50)),
3.0:((0,0,.64,.52),(.65,.15,.35,.55)),
3.5:((0,0,1,.68),OFF),
4.0:((0,0,1,.66),OFF),
4.5:((.08,.04,.73,.72),(.82,.32,.18,.32)),
5.0:((.11,.16,.70,.60),(.82,.35,.18,.45)),
}
def keys(i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
d={"mediaId":657,"level":"A","keyWord":"serve","defaultVoice":"female",
"taps":[
 {"phrase":"to serve the food","target":W,"voice":"female","keys":keys(0)},
 {"phrase":"to pour some water","target":W,"voice":"female","keys":keys(0)},
 {"phrase":"to look at his food","target":M,"voice":"male","keys":keys(1)}],
"stillS":4.5,
"nouns":[{"word":"a jug","x":.24,"y":.47,"voice":"female"},
 {"word":"a glass","x":.54,"y":.74,"voice":"female"},
 {"word":"a fork","x":.22,"y":.83,"voice":"female"},
 {"word":"a table","x":.60,"y":.92,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","serving","food","to","the","man."],
"answerVoice":"female",
"notes":"Two targets only (woman, man); two phrases share the woman. The man is visible 1.5-3.0 s (looks at his bowl 2.5-3.0 s), off at 3.5-4.0 s, and only a sliver of his face at the right edge at 4.5 s (box kept at min width, please check) and 5.0 s. A third diner is cut by the left edge at 4.5-5.0 s, not used; the woman's box starts right of him. 2.0-3.0 s: the woman leans over the man, boxes split vertically, her tray's right end / serving hand reach into his box. 'a fork': a second fork lies at the far right of the table at 4.5 s; the pill is on the left one. 'jug' may be slightly above A1."}
json.dump(d,open("content/657.json","w"),indent=1,ensure_ascii=False)
