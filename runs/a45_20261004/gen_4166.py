import json
def T(n): return [round(i*0.5,1) for i in range(n)]
def keys(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4166
t=T(24)
man={0.0:(0,.20,.29,.38),0.5:(0,.20,.25,.37),1.0:(0,.22,.26,.36),1.5:(0,.22,.30,.37),2.0:(0,.21,.34,.39),2.5:(.02,.21,.40,.41),
3.0:(.11,.22,.39,.42),3.5:(0,0,.58,1),4.0:(0,0,.60,1),4.5:(0,0,.92,1),5.0:(.12,0,.88,1),5.5:(.28,0,.72,1),6.0:(.40,0,.60,.97),
6.5:(.38,.20,.62,.76),7.0:(.30,.34,.42,.50),7.5:(0,.52,.80,.40),8.0:(0,.53,.82,.32),8.5:(0,.48,.80,.34),9.0:(0,.49,.90,.36),
9.5:(0,.49,.90,.38),10.0:(0,.24,.38,.36),10.5:(0,.28,1,.72),11.0:(0,.38,1,.62),11.5:(0,.36,1,.64)}
k=keys(t,man)
save({"mediaId":4166,"level":"A","keyWord":"enter","defaultVoice":"male",
"taps":[{"phrase":"to walk to the car","target":"the man","voice":"male","keys":k},
{"phrase":"to open the car door","target":"the man","voice":"male","keys":k},
{"phrase":"to enter the red car","target":"the man","voice":"male","keys":k}],
"stillS":2.5,
"nouns":[{"word":"a man","x":.24,"y":.38,"voice":"male"},{"word":"a car","x":.45,"y":.86,"voice":"male"},
{"word":"a tree","x":.62,"y":.14,"voice":"male"},{"word":"a bush","x":.72,"y":.40,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","getting","into","the","red","car."],"answerVoice":"male",
"notes":"Only one possible target (the man), so all three phrases share it. 7.5-10.0 s is a close-up where only his hand and forearm are visible: the box is on the hand/arm. At 7.0 s he is a dark figure inside the car. Key word 'enter' is in phrase 3; the answer uses the everyday 'getting into'. 'a bush' = the clipped hedge on the right."})

# 4167
h={0.0:(.24,.46,.50,.54),0.5:(.26,.46,.54,.54),1.0:(.21,.45,.53,.55),1.5:(.21,.45,.53,.55),2.0:(.26,.45,.52,.55),2.5:(.21,.46,.57,.54),
3.0:(.16,.47,.56,.53),3.5:(.12,.48,.60,.52),4.0:(.12,.53,.70,.47),4.5:(.12,.55,.70,.45),5.0:(.12,.54,.70,.46),5.5:(.12,.56,.70,.44),
6.0:(.12,.55,.70,.45),6.5:(.12,.53,.76,.47),7.0:(.08,.53,.72,.47),7.5:(.06,.51,.84,.49),8.0:(0,.38,.80,.62),8.5:(.10,.41,.72,.59),
9.0:(.06,.43,.68,.57),9.5:(.06,.46,.66,.54),10.0:(.02,.45,.74,.55),10.5:(0,.44,.80,.56),11.0:(0,.44,.76,.56),11.5:(0,.43,.80,.57)}
c={0.0:(.22,0,.78,.44),0.5:(.19,0,.81,.44),1.0:(.17,0,.83,.44),1.5:(.15,0,.85,.44),2.0:(.10,0,.90,.44),2.5:(.04,0,.96,.45),
3.0:(0,0,1,.47),3.5:(0,0,1,.48)}
e={4.0:(.33,.26,.32,.27),4.5:(.33,.25,.33,.30),5.0:(.32,.25,.34,.29),5.5:(.34,.24,.34,.32),6.0:(.32,.22,.36,.33),6.5:(.32,.19,.38,.34),
7.0:(.29,.15,.42,.38),7.5:(.26,.07,.50,.44)}
save({"mediaId":4167,"level":"B","keyWord":"exit","defaultVoice":"male",
"taps":[{"phrase":"to emerge from the cave","target":"the horse","voice":"male","keys":keys(t,h)},
{"phrase":"to tower over the beach","target":"the cliff","voice":"male","keys":keys(t,c)},
{"phrase":"to glow in the darkness","target":"the cave exit","voice":"male","keys":keys(t,e)}],
"stillS":6.5,
"nouns":[{"word":"an exit","x":.50,"y":.33,"voice":"male"},{"word":"a cave wall","x":.20,"y":.45,"voice":"male"},
{"word":"a horse","x":.46,"y":.78,"voice":"male"}],
"question":"Where is the horse heading?","answer":["It","is","heading","for","the","exit","of","the","cave."],"answerVoice":"male",
"notes":"Point-of-view ride: only the horse's neck and ears are visible, the box is on them. Inside the cave (4.0-7.5 s) the bright opening reaches down to the ears, so the exit box and the horse box are split at the ear tips. The cliff is a target only outside (0-3.5 s); inside the cave and after it, it is off. The horse is very dark at 4.0-5.5 s. Still at 6.5 s chosen so the key word (the exit) is visible; 'a cave wall' is placed on the lit left wall (the right wall is the same thing). Only 3 nouns: nothing else is identifiable in the dark."})

# 4168
t2=T(25)
A=(.02,.13,.78,.27); B=(.16,.10,.70,.29); L=(.03,.24,.80,.18)
r={0.0:A,0.5:B,1.0:(.02,.14,.78,.26),1.5:(.16,.11,.70,.28),2.0:(.28,.12,.48,.28),2.5:(.24,.10,.42,.30),3.0:(.24,.09,.42,.31),
3.5:(.40,.09,.42,.31),4.0:(.43,.09,.42,.31),4.5:(.44,.09,.38,.31),5.0:(.40,.04,.40,.36),10.0:A,10.5:B,11.0:(.02,.14,.78,.26),11.5:(.16,.11,.70,.28),12.0:A}
for x in [5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5]: r[x]=L
tt={x:(.22,.70,.49,.22) for x in t2}
bf={x:(.71,.66,.20,.15) for x in t2}
save({"mediaId":4168,"level":"A","keyWord":"slow","defaultVoice":"female",
"taps":[{"phrase":"to sleep on its back","target":"the rabbit","voice":"female","keys":keys(t2,r)},
{"phrase":"to walk very slowly","target":"the turtle","voice":"female","keys":keys(t2,tt)},
{"phrase":"to fly in the air","target":"the butterfly","voice":"female","keys":keys(t2,bf)}],
"stillS":8.0,
"nouns":[{"word":"the moon","x":.83,"y":.13,"voice":"female"},{"word":"a rabbit","x":.45,"y":.35,"voice":"female"},
{"word":"a butterfly","x":.74,"y":.72,"voice":"female"},{"word":"a turtle","x":.38,"y":.82,"voice":"female"}],
"question":"What is the turtle doing?","answer":["It","is","walking","very","slowly."],"answerVoice":"female",
"notes":"Split-screen cartoon (hare and tortoise). Level A, so the everyday words 'rabbit' and 'turtle' are used for the hare and the tortoise - the verifier may prefer 'tortoise'. The butterfly is small and sits right beside the turtle's head: its box starts exactly where the turtle's box ends (x 0.71). The moon is drawn in both halves; the pill is on the upper one. The butterfly and turtle pills are close (0.10 apart in y). Key word 'slow' appears as 'slowly'."})

# 4169
m={};b={}
left={0.0:.26,0.5:.27,1.0:.28,1.5:.28,2.0:.27,2.5:.28,3.0:.27,3.5:.26,4.0:.25,4.5:.25,5.0:.24,5.5:.24}
by={0.0:.35,0.5:.35,1.0:.36,1.5:.36,2.0:.36,2.5:.36,3.0:.37,3.5:.37,4.0:.37,4.5:.37,5.0:.38,5.5:.38}
for x,s in left.items():
    m[x]=(s,.35,round(1-s,2),.65); b[x]=(round(s-.19,2),by[x],.19,.14)
right={6.0:(.64,.41,.18,.17),6.5:(.63,.40,.18,.19),7.0:(.61,.41,.20,.19),7.5:(.59,.43,.22,.20),8.0:(.57,.43,.27,.22),8.5:(.57,.44,.30,.22),
9.0:(.55,.45,.42,.23),9.5:(.53,.45,.44,.24),10.0:(.49,.45,.47,.25),10.5:(.46,.45,.52,.27),11.0:(.46,.46,.54,.28),11.5:(.46,.46,.54,.31)}
for x,v in right.items():
    b[x]=v; m[x]=(0,.35,v[0],.65)
km=keys(t,m)
save({"mediaId":4169,"level":"A","keyWord":"look","defaultVoice":"male",
"taps":[{"phrase":"to look at the bear","target":"the man","voice":"male","keys":km},
{"phrase":"to sit in a boat","target":"the man","voice":"male","keys":km},
{"phrase":"to swim near the boat","target":"the big bear","voice":"male","keys":keys(t,b)}],
"stillS":8.5,
"nouns":[{"word":"trees","x":.50,"y":.15,"voice":"male"},{"word":"a river","x":.60,"y":.33,"voice":"male"},
{"word":"a cap","x":.32,"y":.45,"voice":"male"},{"word":"a bear","x":.74,"y":.55,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","taking","a","look","at","the","bear."],"answerVoice":"male",
"notes":"Two bears: the near one ('the big bear') is the target; the small far bear (upper left, in the river) also swims but not near the boat. The big bear passes BEHIND the man's head: until 5.5 s it is on the left of his hood (almost hidden at 5.0-5.5 s), from 6.0 s on the right. Man and bear boxes are split at the edge of the hood, so the man's box leaves out the part of his arm/shoulder on the bear's side. 'a bear' pill is on the near bear; no noun on the far one. Key word 'look' (noun) is in the answer."})
