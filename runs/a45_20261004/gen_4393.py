import json
O=None
# (man with the bag, man in yellow)
K={
0.0:((.0,.18,1.0,.82),O),0.5:((.08,.33,.90,.67),O),1.0:((.08,.22,.78,.78),O),1.5:((.08,.15,.84,.85),O),
2.0:((.07,.10,.80,.90),O),2.5:((.15,.07,.68,.78),O),
3.0:((.53,.08,.47,.92),(.26,.43,.19,.17)),
3.5:((.42,.09,.58,.91),(.21,.43,.21,.16)),
4.0:((.10,.15,.90,.85),O),4.5:((.0,.26,1.0,.74),O),
5.0:(O,O),5.5:(O,O),6.0:(O,O),
6.5:((.08,.03,.92,.97),O),7.0:((.0,.22,.90,.78),O),7.5:((.0,.20,.90,.80),O),
8.0:((.05,.18,.93,.82),O),8.5:((.08,.18,.92,.82),O),9.0:((.08,.20,.92,.80),O),
}
def keys(i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
d={"mediaId":4393,"level":"A","keyWord":"chat","defaultVoice":"male",
"taps":[
 {"phrase":"to open a small bag","target":"the man with the bag","voice":"male","keys":keys(0)},
 {"phrase":"to feed the birds","target":"the man with the bag","voice":"male","keys":keys(0)},
 {"phrase":"to run by the sea","target":"the man in yellow","voice":"male","keys":keys(1)}],
"stillS":2.5,
"nouns":[{"word":"a cap","x":0.50,"y":0.15,"voice":"male"},
 {"word":"a bench","x":0.14,"y":0.42,"voice":"male"},
 {"word":"a bag","x":0.52,"y":0.53,"voice":"male"},
 {"word":"birds","x":0.35,"y":0.91,"voice":"male"}],
"question":"What are the three men doing?",
"answer":["They","are","chatting","by","the","sea."],
"answerVoice":"male",
"notes":"The man in yellow (runner) is small and only at 3.0-3.5 s, about one second to tap; chosen because nothing fits only the man in sunglasses (others on the long bench at 5.0-6.0 s also wear sunglasses, the third man also has a grey beard). Man with the bag is off at 5.0-6.0 s (row of other people on the bench). At 7.5-9.0 s his box also covers part of the man in sunglasses behind him (not a target). Pigeons are visible only at 2.5 s (the still). The answer's subject is the three men of the last shot (the third only partly in the picture at the left edge); chatting is read from their laughing faces turned to each other."}
json.dump(d,open("content/4393.json","w"),indent=1)
