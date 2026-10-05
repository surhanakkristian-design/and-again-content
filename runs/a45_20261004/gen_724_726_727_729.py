import json
OFF=None
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n,step=0.5): return [round(i*step,1) for i in range(n)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 724
t=T(29)
diver={1.0:(.30,.21,.65,.74),1.5:(.36,.18,.44,.47),2.0:(.40,.45,.28,.22),2.5:(.42,.57,.27,.16),
 4.5:(.40,.19,.20,.14),5.0:(.41,.16,.20,.15),5.5:(.40,.10,.20,.15),6.0:(.40,.09,.20,.15),6.5:(.43,.18,.20,.15),
 9.0:(.32,.05,.22,.16),9.5:(.36,.22,.20,.20)}
splash={3.0:(.38,.48,.34,.26),3.5:(.32,.44,.58,.31),4.0:(.25,.47,.60,.32),7.0:(.27,.49,.48,.24),7.5:(.17,.30,.55,.35),
 8.0:(.17,.30,.64,.40),8.5:(.12,.30,.80,.40),10.0:(.29,.43,.40,.42),10.5:(.26,.02,.56,.85),11.0:(.15,.0,.68,.93),
 11.5:(.0,.0,1.0,.74),12.0:(.0,.0,.72,.62),12.5:(.0,.0,.40,.64)}
woman={12.5:(.41,.45,.34,.22),13.0:(.38,.46,.34,.32),13.5:(.40,.48,.58,.41),14.0:(.33,.43,.40,.26)}
save({"mediaId":724,"level":"A","keyWord":"splash","defaultVoice":"female",
 "taps":[
  {"phrase":"to jump into the pool","target":"the diver","voice":"female","keys":keys(t,diver)},
  {"phrase":"to shoot up very high","target":"the splash","voice":"female","keys":keys(t,splash)},
  {"phrase":"to laugh in the water","target":"the woman in the pool","voice":"female","keys":keys(t,woman)}],
 "stillS":10.0,
 "nouns":[{"word":"a splash","x":.47,"y":.62,"voice":"female"},{"word":"the sun","x":.55,"y":.14,"voice":"female"},
  {"word":"a tower","x":.25,"y":.33,"voice":"female"},{"word":"umbrellas","x":.78,"y":.75,"voice":"female"}],
 "question":"What can you see in the pool?",
 "answer":["There","is","a","big","splash","in","the","pool."],
 "answerVoice":"female",
 "notes":"Clip has 5 shots with three different jumpers (a man in shorts 1.0-2.5, a jumper on the high tower 4.5-6.5, a woman 9.0-9.5). 'the diver' = whoever is jumping in each shot (never two at once), so the target is a role, not one person; voice left at default. 'the splash' boxes only where white water is up; at 2.5 the diver's head is inside the first small splash, so that time belongs to the diver. Spectators filming with phones were not used (several do it). 'shoot up' is a little above A1. 4.5: diver is only a tiny head on top of the tower."})

# 726
t=T(21)
w={0.0:(0,.43,.47,.57),0.5:(0,.44,.45,.56),1.0:(0,.43,.45,.57),1.5:(0,.41,.45,.59),2.0:(0,.41,.50,.59),2.5:(0,.41,.50,.59),
 6.0:(0,.43,.49,.57),6.5:(0,.43,.50,.57),7.0:(0,.47,.51,.53),7.5:(0,.54,.48,.46),8.0:(0,.67,.49,.33),8.5:(0,.68,.49,.32),
 9.0:(0,.68,.50,.32),9.5:(0,.68,.50,.32),10.0:(0,.68,.50,.32)}
m={0.0:(.48,.33,.52,.67),0.5:(.46,.35,.54,.65),1.0:(.46,.33,.54,.67),1.5:(.46,.34,.54,.66),2.0:(.51,.34,.49,.66),2.5:(.51,.33,.49,.67),
 6.0:(.50,.34,.50,.66),6.5:(.51,.34,.49,.66),7.0:(.52,.36,.48,.64),7.5:(.50,.44,.50,.56),8.0:(.50,.58,.50,.42),8.5:(.50,.65,.50,.35),
 9.0:(.51,.66,.49,.34),9.5:(.51,.66,.49,.34),10.0:(.51,.66,.49,.34)}
d={3.0:(.03,.64,.79,.16),3.5:(.10,.64,.80,.16),4.0:(.20,.64,.80,.17),4.5:(.30,.65,.70,.16),5.0:(.40,.69,.55,.15),5.5:(.50,.69,.46,.15)}
save({"mediaId":726,"level":"A","keyWord":"spring","defaultVoice":"female",
 "taps":[
  {"phrase":"to point with her finger","target":"the woman","voice":"female","keys":keys(t,w)},
  {"phrase":"to take off his jacket","target":"the man","voice":"male","keys":keys(t,m)},
  {"phrase":"to swim on the water","target":"the ducks","voice":"female","keys":keys(t,d)}],
 "stillS":10.0,
 "nouns":[{"word":"flowers","x":.40,"y":.15,"voice":"female"},{"word":"grass","x":.60,"y":.58,"voice":"female"},
  {"word":"a woman","x":.26,"y":.82,"voice":"female"},{"word":"a man","x":.73,"y":.82,"voice":"male"}],
 "question":"What is the man taking off?",
 "answer":["He","is","taking","off","his","jacket."],
 "answerVoice":"male",
 "notes":"Key word 'spring' is not a visible thing, so it is not a noun slot and not in the answer. 'the ducks' = the whole family (mother + ducklings) in one box, a group target; they are blurred in the background behind the bud. The man takes off the jacket at 6.0 and by 6.5 the T-shirt too. At 2.0/2.5 the woman's pointing hand reaches a little into the man's box (split at x 0.50)."})

# 727
t=T(11)
w={0.0:(0,.19,.80,.61),0.5:(.11,.19,.63,.66),1.0:(0,.19,.97,.72),1.5:(0,.19,.86,.72),2.0:(.39,.16,.61,.67),2.5:(.40,.24,.50,.68),
 3.0:(.20,.25,.68,.72),3.5:(.19,.33,.70,.65),4.0:(.19,.34,.70,.59),4.5:(.19,.17,.59,.77),5.0:(.19,.20,.62,.78)}
tp={2.0:(0,.39,.38,.14),2.5:(0,.52,.39,.14),3.0:(0,.77,.19,.14),3.5:(0,.78,.18,.14),4.0:(0,.79,.18,.14),4.5:(0,.80,.18,.14),5.0:(0,.86,.18,.14)}
save({"mediaId":727,"level":"B","keyWord":"sprint","defaultVoice":"female",
 "taps":[
  {"phrase":"to win the sprint","target":"the woman","voice":"female","keys":keys(t,w)},
  {"phrase":"to catch her breath","target":"the woman","voice":"female","keys":keys(t,w)},
  {"phrase":"to mark the finish line","target":"the red ribbon","voice":"female","keys":keys(t,tp)}],
 "stillS":2.5,
 "nouns":[{"word":"a ribbon","x":.20,"y":.59,"voice":"female"},{"word":"a braid","x":.60,"y":.31,"voice":"female"},
  {"word":"trainers","x":.64,"y":.84,"voice":"female"},{"word":"a running track","x":.27,"y":.94,"voice":"female"}],
 "question":"What is the runner doing?",
 "answer":["She","is","sprinting","towards","the","finish","line."],
 "answerVoice":"female",
 "notes":"The men behind her (0.0-1.0, left edge) also sprint, so no phrase uses bare 'to sprint'; they are not a target (her back leg crosses them). At 2.0 the ribbon runs across her body: ribbon box = the free part left of her, her box starts at x 0.39 and so loses her back leg. From 3.0 the ribbon lies on the track at the left edge (tiny). 'trainers' are spiked running shoes."})

# 729
t=T(21)
s={0.0:(.32,.33,.38,.61),0.5:(.34,.22,.40,.66),1.0:(.35,.10,.42,.66),1.5:(.28,.29,.61,.68),2.0:(.24,.20,.50,.62),2.5:(.34,.24,.44,.68),
 3.0:(0,.15,.87,.50),3.5:(0,.19,.84,.48),4.0:(0,.20,.76,.44),4.5:(.01,.14,.78,.56),5.0:(.04,.20,.78,.69),5.5:(.08,.24,.74,.66),
 6.0:(.04,.20,.74,.54),6.5:(.01,.16,.77,.54),7.0:(0,.29,1.0,.57),7.5:(0,.23,1.0,.48),8.0:(0,.23,.90,.28),8.5:(.04,.26,.84,.30),
 9.0:(.02,.20,.72,.52),9.5:(0,.34,.70,.37),10.0:(.52,.22,.42,.30)}
k=keys(t,s)
save({"mediaId":729,"level":"A","keyWord":"squirrel","defaultVoice":"male",
 "taps":[
  {"phrase":"to climb up a tree","target":"the squirrel","voice":"male","keys":k},
  {"phrase":"to eat a nut","target":"the squirrel","voice":"male","keys":k},
  {"phrase":"to run along a branch","target":"the squirrel","voice":"male","keys":k}],
 "stillS":6.0,
 "nouns":[{"word":"a squirrel","x":.35,"y":.56,"voice":"male"},{"word":"a nut","x":.66,"y":.46,"voice":"male"},
  {"word":"a branch","x":.25,"y":.68,"voice":"male"},{"word":"leaves","x":.30,"y":.86,"voice":"male"}],
 "question":"What is the squirrel eating?",
 "answer":["The","squirrel","is","eating","a","nut."],
 "answerVoice":"male",
 "notes":"Only one possible target (the squirrel), used for all three phrases. At 10.0 it is a blurred shape jumping away behind leaves. The nut pill sits close to the squirrel's face; the squirrel pill is on its body."})
