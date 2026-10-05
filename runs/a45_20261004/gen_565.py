import json
def keys(d,T):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def write(id,n,level,kw,dv,taps,still,nouns,q,a,av,notes):
    T=[i*0.5 for i in range(n)]
    json.dump({"mediaId":id,"level":level,"keyWord":kw,"defaultVoice":dv,
      "taps":[{"phrase":p,"target":tg,"voice":v,"keys":keys(k,T)} for p,tg,v,k in taps],
      "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
      "question":q,"answer":a,"answerVoice":av,"notes":notes},open(f'content/{id}.json','w'),indent=1)
# 565
W={0.0:(.17,.27,.26,.42),0.5:(0,.36,.24,.18),1.0:(0,.36,.25,.17),2.5:(.10,.24,.33,.50),3.0:(.13,.42,.28,.52),3.5:(.17,.41,.26,.52),
 4.0:(.21,.41,.22,.37),4.5:(.26,.41,.18,.35),6.0:(.18,.35,.25,.43),6.5:(.16,.36,.24,.43),7.0:(.15,.47,.29,.48),7.5:(.17,.31,.29,.69),
 8.0:(.10,.27,.35,.73),8.5:(.07,.25,.36,.75),9.0:(.07,.26,.38,.74)}
M={0.0:(.62,.29,.29,.41),1.5:(0,.16,1,.84),2.0:(0,.15,1,.85),2.5:(.47,.24,.53,.48),3.0:(.56,.45,.32,.49),3.5:(.55,.42,.33,.51),
 4.0:(.57,.41,.28,.39),4.5:(.57,.41,.28,.37),5.0:(.80,.70,.20,.24),5.5:(.54,.52,.46,.24),6.0:(.53,.39,.36,.39),6.5:(.56,.35,.38,.44),
 7.0:(.50,.47,.42,.48),7.5:(.46,.33,.50,.67),8.0:(.45,.30,.55,.70),8.5:(.43,.29,.57,.71),9.0:(.45,.30,.55,.70)}
write(565,19,"B","politics","male",[("to shake a chef's hand","the woman","female",W),("to raise both fists","the man","male",M),("to wipe off green paint","the man","male",M)],
 0.0,[("a dome",.50,.19,"male"),("a canvas",.50,.44,"male"),("an easel",.50,.63,"male"),("cobblestones",.50,.86,"male")],
 "What are the two candidates doing?",["They","are","shaking","hands","in front of","the","crowd."],"male",
 "Woman and man are both main -> mixed, evenId false -> male default. At 0.5/1.0 only the woman's orange-sleeved pointing hand is visible (boxed as the woman). At 5.0 a bare hand at the bottom right is boxed as the man (his teal sleeve follows at 5.5, wiping the green stripe) - a guess. The woman shakes the chef's hand at 3.5 and then seems to pin a rosette on him (4.0-4.5); the man shakes hands with the WOMAN at 7.5-9.0, so 'a chef's hand' keeps the phrase on her only. The chef (3.0-7.0) and the canvas were not used as targets: both overlap the candidates. 'candidates' and 'crowd' appear only in question/answer. Key word 'politics' is abstract, no noun slot.")
# 566
man={0.0:(.07,.08,.73,.92),0.5:(.05,.13,.58,.87),1.0:(.08,0,.56,.80),1.5:(.15,0,.32,.44),4.0:(.25,.36,.18,.14),4.5:(.27,.36,.18,.14)}
girl={4.0:(.41,.51,.18,.14),4.5:(.41,.51,.18,.14),5.0:(.19,.22,.72,.78),5.5:(.25,.08,.75,.92),6.0:(.23,.12,.77,.80),6.5:(.25,.12,.75,.80),
 7.0:(.24,.12,.76,.86),7.5:(.25,.12,.75,.84),8.0:(.25,.11,.75,.80)}
dr={2.0:(.14,.24,.37,.22),2.5:(.13,.24,.32,.22)}
write(566,17,"B","pollute","female",[("to empty a rusty barrel","the man","male",man),("to lift a metal bucket","the girl","female",girl),("to hover above the water","the dragonfly","female",dr)],
 6.5,[("a ponytail",.84,.30,"female"),("a raincoat",.70,.46,"female"),("a river",.20,.65,"female"),("a bucket",.68,.74,"female")],
 "What is the man doing?",["He","is","emptying","a","barrel","into","the","river."],"male",
 "Man + girl -> mixed, evenId true -> female default. The dragonfly is visible only at 2.0 and 2.5 (short tap window). At 0.0-1.0 the man's box also holds much of the barrel he is hugging; at 1.5 only his legs. At 4.0/4.5 man and girl are tiny (minimum boxes; the man's box takes in part of the truck). Key word 'pollute' is a verb: not in the texts, the answer shows the act. 'a river' pill sits on the clean water left of the girl.")
# 567
def c(x,y): return (round(x-.09,2),round(y-.07,2),.18,.14)
sn=[(.20,.51),(.25,.52),(.33,.52),(.44,.54),(.55,.55),(.62,.55),(.66,.54),(.70,.52),(.72,.48),(.76,.47),(.76,.48),(.78,.49),(.78,.50),(.80,.51),(.77,.51),(.75,.50),(.70,.48),(.66,.47),(.61,.47),(.58,.46),(.56,.46)]
S={i*0.5:c(*p) for i,p in enumerate(sn)}
Wm={1.5:(0,.10,.18,.47),2.0:(0,0,.30,.54),2.5:(0,0,.36,.50),3.0:(0,0,.46,.62),3.5:(0,0,.50,.61),4.0:(0,0,.46,.59),4.5:(0,0,.46,.59),5.0:(0,0,.40,.57),
 5.5:(0,0,.34,.48),6.0:(0,0,.32,.36),6.5:(0,0,.28,.36),7.0:(0,0,.30,.37),7.5:(0,0,.22,.38),8.0:(0,0,.18,.30),8.5:(0,0,.18,.30),9.0:(0,0,.18,.40),9.5:(0,0,.18,.33),10.0:(0,0,.18,.30)}
F={0.0:(.18,.61,.22,.14),0.5:(.21,.62,.20,.14),1.0:(.24,.63,.24,.14),1.5:(.28,.64,.28,.14),2.0:(.25,.67,.38,.14),2.5:(.30,.67,.58,.14),3.0:(.34,.64,.54,.14),
 3.5:(.30,.62,.64,.19),4.0:(.27,.63,.56,.22),4.5:(.24,.63,.54,.24),5.0:(.22,.65,.56,.32),5.5:(.31,.67,.52,.30),6.0:(.40,.67,.44,.31),6.5:(.48,.65,.47,.34),
 7.0:(.37,.69,.52,.31),7.5:(.18,.76,.46,.17),8.0:(.11,.74,.38,.18),8.5:(.04,.72,.34,.20),9.0:(.02,.68,.27,.22),9.5:(0,.68,.90,.22),10.0:(.02,.67,.80,.24)}
write(567,21,"A","pond","male",[("to point at the fish","the woman","female",Wm),("to sit on a leaf","the snail","male",S),("to swim under the water","the fish","male",F)],
 0.0,[("flowers",.60,.14,"male"),("a snail",.20,.50,"male"),("a pond",.62,.62,"male"),("stones",.35,.80,"male")],
 "What is the woman pointing at?",["She","is","pointing","at","the","fish","in","the","pond."],"female",
 "Woman + man -> mixed, evenId false -> male default. 'the fish' = the group of orange fish, one box round all of them. The woman points at 3.0-4.5 and touches the water at 5.0; from 6.0 only her arm/hands at the left edge, from 8.0 a sleeve sliver (minimum box, may take in part of the man). Her box also covers the small frog on the stone next to her fist (the frog is no target: it jumps in at 7.0 but always overlaps her). The man has no action of his own. The snail is small (minimum box). 'flowers' = the purple irises across the top.")
# 568
Ww={0.5:(0,.71,.48,.20),1.0:(0,.73,.86,.27),1.5:(.12,.55,.88,.45),2.0:(.24,.48,.76,.36),2.5:(.23,.49,.77,.30),3.0:(.17,.49,.83,.36),3.5:(.14,.44,.86,.42),
 4.0:(.19,.47,.81,.31),4.5:(.22,.50,.78,.30),5.0:(.22,.53,.78,.39),5.5:(.23,.55,.77,.39),6.0:(.29,.52,.71,.29),6.5:(.35,.50,.65,.29),7.0:(.37,.51,.63,.25),
 7.5:(.37,.51,.63,.25),8.0:(.34,.49,.66,.26),8.5:(.32,.49,.68,.27),9.0:(.29,.50,.71,.40),9.5:(.27,.52,.73,.42),10.0:(.24,.50,.76,.36)}
R={0.0:(.42,.20,.23,.30),0.5:(.49,.22,.24,.33),1.0:(.34,.16,.31,.31),1.5:(.28,.37,.36,.18),4.0:(.19,.33,.24,.14),4.5:(.17,.34,.33,.16),5.0:(.12,.39,.40,.14),
 5.5:(.15,.40,.35,.15),6.0:(.19,.37,.21,.15),6.5:(.22,.35,.22,.15),7.0:(.19,.35,.25,.15),7.5:(.12,.34,.33,.15),8.0:(.05,.33,.45,.14),8.5:(.02,.32,.45,.15),
 9.0:(0,.33,.44,.15),9.5:(0,.33,.45,.15),10.0:(0,.32,.44,.15)}
G={0.0:(.12,.18,.21,.30),0.5:(.31,.23,.18,.28),1.0:(.65,.24,.18,.38),1.5:(.82,.17,.18,.30),3.0:(.82,.12,.18,.36),3.5:(.82,.07,.18,.36),4.0:(.82,.07,.18,.30),
 4.5:(.82,.13,.18,.27),5.0:(.75,.15,.23,.24),5.5:(.52,.17,.26,.27),6.0:(.46,.38,.20,.14),7.0:(.52,.37,.20,.14),7.5:(.55,.36,.20,.14),8.0:(.55,.34,.26,.14),
 8.5:(.47,.33,.47,.15),9.0:(.45,.34,.51,.15),9.5:(.46,.34,.50,.16),10.0:(.45,.34,.51,.15)}
write(568,21,"A","pool","female",[("to lie on an orange ring","the woman","female",Ww),("to run to the pool","the man in red shorts","male",R),("to jump after his friend","the man in green shorts","male",G)],
 10.0,[("flowers",.50,.09,"female"),("chairs",.20,.27,"female"),("a ring",.33,.63,"female"),("a pool",.45,.86,"female")],
 "What are the two men doing?",["They","are","jumping","into","the","pool."],"female",
 "The woman is in almost every frame, but the question is about the men -> answerVoice = default (female, evenId true). The man in red runs and jumps at 0.0-1.5, is hidden by his splash at 2.0-3.5; the man in green walks to the edge, jumps at 5.5 and is hidden at 6.5. In the water the shorts are hardly visible: left head = red, right head = green (kept by position). At 8.5-10.0 the floating men's arms overlap, boxes split at x 0.45-0.47. 'chairs' = the two white sunbeds on the left (more sunbeds on the right with a person on them). 'a ring' pill sits on the left part of the ring, next to the woman's head.")
