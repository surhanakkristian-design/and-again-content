import json
T=[i*0.5 for i in range(30)]
def mk(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":round(d[t][3],2)} if t in d else {"t":t,"off":True}) for t in T]
# t: (kayak top y or None, kayak x, kayak w, paddlers box or None, river top, river bottom or None)
R={0.0:(.58,0,.75,(.31,.20,.18,.14),.34),0.5:(.54,0,1,(.31,.19,.18,.14),.33),1.0:(.53,0,.75,(.31,.17,.18,.14),.31),
1.5:(.53,0,1,(.41,.14,.18,.14),.28),2.0:(.56,0,.85,(.38,.10,.18,.14),.24),2.5:(None,0,1,(.38,.16,.18,.14),.30),
3.0:(.43,0,1,(.36,.16,.18,.14),.30),3.5:(.85,0,1,(.35,.14,.18,.14),.28),4.0:(.56,0,.80,(.35,.12,.18,.14),.26),
4.5:(.61,0,1,(.41,.12,.18,.14),.26),5.5:(.50,.15,.60,(.56,.20,.18,.14),.35),6.0:(.66,0,1,(.54,.18,.18,.14),.32),
6.5:(.52,.30,.70,(.56,.16,.18,.14),.30),7.0:(.58,0,1,(.59,.14,.18,.14),.28),7.5:(.62,0,1,(.61,.13,.18,.14),.27),
8.5:(.64,0,1,(.53,.18,.18,.14),.32),9.0:(.59,0,1,(.53,.20,.18,.14),.34),9.5:(.62,0,1,(.51,.21,.18,.14),.35),
10.0:(None,0,1,None,.32),10.5:(None,0,1,(.45,.26,.36,.15),.41),11.0:(.60,0,1,(.42,.25,.40,.14),.39),
11.5:(.61,0,1,(.44,.21,.45,.14),.35),12.0:(.62,0,1,(.50,.20,.26,.14),.34),12.5:(.54,0,1,(.59,.27,.39,.14),.41),
13.0:(.56,0,1,(.36,.28,.58,.14),.42),13.5:(.55,0,1,(.35,.28,.62,.14),.42),14.0:(.56,0,1,(.33,.28,.67,.14),.42),
14.5:(.55,0,1,(.33,.28,.67,.14),.42)}
kay={};pad={};riv={}
for t,(ky,kx,kw,p,rt) in R.items():
    if p and p[2]==.18: p=(p[0],round(p[1]+.03,2),p[2],p[3]); rt=round(rt+.03,2)
    if ky is not None: kay[t]=(kx,ky,kw,1-ky)
    if p: pad[t]=p
    rb = ky if ky is not None else (.82 if t==10.0 else (.76 if t==10.5 else 1.0))
    riv[t]=(0,rt,1,rb-rt)
d={"mediaId":4079,"level":"B","keyWord":"rush","defaultVoice":"male",
"taps":[{"phrase":"to bounce over the waves","target":"the yellow kayak","voice":"male","keys":mk(kay)},
{"phrase":"to foam between dark rocks","target":"the river","voice":"male","keys":mk(riv)},
{"phrase":"to wait on the bank","target":"the paddlers","voice":"male","keys":mk(pad)}],
"stillS":14.0,
"nouns":[{"word":"a forest","x":.28,"y":.14,"voice":"male"},{"word":"paddlers","x":.62,"y":.36,"voice":"male"},
{"word":"the river","x":.28,"y":.49,"voice":"male"},{"word":"a kayak","x":.50,"y":.80,"voice":"male"}],
"question":"What is the river doing?","answer":["The","river","is","rushing","between","the","rocks."],"answerVoice":"male",
"notes":"POV clip: only a hand of the kayaker shows, so no person is the main target; defaultVoice by odd id. River box = the band of water between the far bank and the bow (water beside the bow belongs to the kayak box, to avoid overlap). Paddlers are tiny until about 10.5 s (minimum-size box). All off at 5.0 and 8.0 (spray whiteout); kayak off at 2.5, 10.0, 10.5 (hidden by foam / not in frame); kayak only faintly visible through foam at 3.5, 5.5, 6.0, 8.5, 12.0. 'a kayak' pill is on the yellow bow; red and pink kayaks also lie on the bank under the 'paddlers' pill. The rocks of the answer are passed earlier in the clip (0-9.5 s), not in the still."}
json.dump(d,open("content/4079.json","w"),indent=1)
