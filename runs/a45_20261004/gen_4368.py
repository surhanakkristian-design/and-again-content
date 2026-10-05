import json
O=None
# t: (woman, tree, lights)
K={
0.0:((.22,.28,.45,.72),O,O),
0.5:((.20,.28,.50,.72),O,O),
1.0:((.12,.22,.80,.78),O,O),
1.5:((.03,.19,.97,.81),O,O),
2.0:((.0,.19,1.0,.81),O,O),
2.5:((.34,.37,.66,.63),(.08,.0,.74,.37),O),
3.0:((.30,.42,.70,.58),(.0,.05,.62,.37),O),
3.5:((.46,.28,.54,.72),(.0,.05,.46,.93),O),
4.0:((.42,.33,.58,.67),(.0,.07,.42,.93),O),
4.5:((.46,.18,.54,.80),(.0,.07,.46,.90),O),
5.0:((.58,.22,.42,.78),(.0,.07,.32,.36),(.14,.43,.44,.14)),
5.5:((.56,.25,.44,.75),(.0,.08,.32,.37),(.14,.45,.42,.14)),
6.0:((.66,.17,.34,.80),(.0,.08,.32,.37),(.12,.45,.54,.14)),
6.5:((.63,.15,.37,.85),(.0,.06,.30,.39),(.12,.45,.51,.14)),
7.0:((.56,.23,.44,.77),(.0,.08,.30,.36),(.12,.44,.44,.14)),
7.5:((.46,.29,.54,.71),(.0,.23,.27,.31),(.05,.54,.41,.14)),
8.0:((.42,.31,.56,.69),(.0,.27,.22,.30),(.02,.58,.40,.14)),
8.5:((.42,.31,.56,.69),(.0,.27,.22,.30),(.02,.58,.40,.14)),
9.0:((.42,.32,.56,.68),(.0,.28,.20,.30),(.0,.62,.42,.14)),
9.5:((.42,.32,.56,.68),(.0,.28,.18,.30),(.0,.62,.42,.14)),
10.0:((.41,.32,.57,.68),(.0,.28,.18,.30),(.0,.62,.41,.14)),
10.5:((.41,.32,.57,.68),(.0,.27,.18,.28),(.0,.63,.41,.14)),
11.0:((.41,.32,.57,.68),(.0,.27,.18,.22),(.0,.64,.41,.14)),
11.5:((.41,.32,.57,.68),(.0,.27,.18,.22),(.0,.64,.41,.14)),
12.0:((.40,.32,.58,.68),(.0,.27,.18,.22),(.0,.64,.40,.14)),
}
def keys(i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
d={"mediaId":4368,"level":"B","keyWord":"light","defaultVoice":"female",
"taps":[
 {"phrase":"to light the bulbs","target":"the woman","voice":"female","keys":keys(0)},
 {"phrase":"to bear ripe lemons","target":"the lemon tree","voice":"female","keys":keys(1)},
 {"phrase":"to glow along the railing","target":"the string of bulbs","voice":"female","keys":keys(2)}],
"stillS":6.5,
"nouns":[{"word":"a lemon tree","x":0.18,"y":0.38,"voice":"female"},
 {"word":"the sun","x":0.55,"y":0.27,"voice":"female"},
 {"word":"bulbs","x":0.35,"y":0.51,"voice":"female"},
 {"word":"a folding table","x":0.55,"y":0.78,"voice":"female"}],
"question":"What is the woman lighting?",
"answer":["She","is","lighting","the","bulbs","along","the","railing."],
"answerVoice":"female",
"notes":"Lemon tree and woman overlap at 2.5-3.0 s: tree box = crown only there. From 5.0 s the tree box is the crown above the bulbs. Tree only partly in frame from 10.5 s (leaves at the left edge, lemons cut off). String of bulbs first lit at 4.5 s (one bulb in her hand) - box starts at 5.0 s. The right-most bulb beyond the woman is not in the lights box."}
json.dump(d,open("content/4368.json","w"),indent=1)
