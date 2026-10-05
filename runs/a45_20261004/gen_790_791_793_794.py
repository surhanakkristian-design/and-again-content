import json
T21=[i*0.5 for i in range(21)]; T25=[i*0.5 for i in range(25)]
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 790
man={0.0:(.24,.36,.76,.64),0.5:(.28,.37,.72,.63),1.0:(.33,.47,.67,.53),1.5:(.18,0,.82,1),2.0:(.10,0,.90,1),2.5:(.07,0,.93,1),
3.0:(.10,.05,.90,.95),3.5:(0,0,1,.60),4.0:(0,0,.85,.58),4.5:(0,0,1,.52),5.0:(0,0,.88,.52),5.5:(0,0,.80,.42),6.0:(0,0,1,.42),
6.5:(0,0,1,.62),7.0:(0,0,1,.88),7.5:(0,0,1,.88),8.0:(.03,0,.97,.90),8.5:(.58,.14,.42,.86),9.0:(.58,.15,.42,.85),9.5:(.58,.14,.42,.86),10.0:(.66,.15,.34,.85)}
wom={8.5:(0,.24,.40,.76),9.0:(0,.26,.39,.74),9.5:(0,.26,.41,.74),10.0:(0,.22,.37,.78)}
hen={8.5:(.40,.63,.18,.20),9.0:(.39,.66,.19,.20),9.5:(.41,.65,.17,.22),10.0:(.39,.68,.24,.24)}
save({"mediaId":790,"level":"A","keyWord":"tomato","defaultVoice":"male","taps":[
 {"phrase":"to cut a tomato","target":"the man","voice":"male","keys":keys(T21,man)},
 {"phrase":"to wear a grey scarf","target":"the woman","voice":"female","keys":keys(T21,wom)},
 {"phrase":"to walk between the plants","target":"the chicken","voice":"male","keys":keys(T21,hen)}],
 "stillS":2.0,"nouns":[{"word":"a tomato","x":.40,"y":.55,"voice":"male"},{"word":"the sun","x":.38,"y":.24,"voice":"male"},{"word":"a man","x":.80,"y":.35,"voice":"male"}],
 "question":"What is the man cutting?","answer":["He","is","cutting","a","red","tomato."],"answerVoice":"male",
 "notes":"Woman and chicken are only in the last shot (8.5-10.0 s); the chicken is small and partly dark at 9.0. Woman's box is narrowed on the right so it does not overlap the chicken (her reaching hand is partly outside). Man = only hands/arms in 0-1.0 and 3.5-6.5. Woman's scarf is grey-beige."})

# 791
P={0.0:(0,.22,.34,.78),0.5:(0,.26,.29,.74),1.0:(0,.20,.24,.80),1.5:(0,.50,.76,.50),2.0:(0,.50,.52,.50),2.5:(.10,.58,.80,.42),
3.0:(.28,.72,.60,.28),3.5:(0,0,.50,1),4.0:(0,.06,.54,.94),4.5:(0,.45,.72,.50),5.0:(0,.58,.74,.42),5.5:(0,.46,.68,.54),
6.0:(0,.54,.46,.46),6.5:(0,.02,.57,.98),7.0:(0,.02,.57,.98),7.5:(0,.02,.32,.98),8.0:(0,.08,.58,.92),8.5:(0,.11,.59,.89),
9.0:(0,.23,.50,.77),9.5:(0,.23,.48,.77),10.0:(0,.11,.23,.83)}
B={0.0:(.46,.27,.36,.60),0.5:(.42,.26,.38,.61),1.0:(.36,.21,.38,.72),1.5:(.20,.09,.36,.41),2.0:(.26,.06,.30,.42),2.5:(.42,.08,.24,.40),
3.0:(.38,.14,.32,.56),3.5:(.52,.16,.30,.60),4.0:(.56,.20,.24,.60),4.5:(.08,.02,.38,.43),5.0:(0,0,.18,.56),6.0:(0,.03,.28,.50),
6.5:(.58,.14,.24,.52),7.0:(.58,.16,.24,.66),7.5:(.50,.16,.32,.76),8.0:(.60,.18,.22,.62),8.5:(.60,.21,.22,.62),9.0:(.52,.26,.30,.68),
9.5:(.50,.26,.30,.50),10.0:(.38,.21,.38,.68)}
save({"mediaId":791,"level":"A","keyWord":"tool","defaultVoice":"male","taps":[
 {"phrase":"to take a tool","target":"the man in pink","voice":"male","keys":keys(T21,P)},
 {"phrase":"to point at a tool","target":"the man in pink","voice":"male","keys":keys(T21,P)},
 {"phrase":"to stand behind the bike","target":"the man in blue","voice":"male","keys":keys(T21,B)}],
 "stillS":4.5,"nouns":[{"word":"tools","x":.78,"y":.72,"voice":"male"},{"word":"a hand","x":.56,"y":.52,"voice":"male"},{"word":"a man","x":.28,"y":.22,"voice":"male"},{"word":"a wall","x":.75,"y":.10,"voice":"male"}],
 "question":"What is the man in pink taking?","answer":["He","is","taking","a","tool","from","the","wall."],"answerVoice":"male",
 "notes":"Handheld clip, the two men overlap often; boxes are split between them (the man in blue loses his legs at 1.5, 4.5, 9.5; the man in pink loses his reaching hand at 9.5). The man in pink is often only a hand/arm. His shirt is light pink / lilac. Tools hang on a pegboard on the wall. A rooster walks by at 8.0-10.0 (not used)."})

# 793
W={0.0:(.06,.03,.84,.60),0.5:(.03,0,.97,.63),1.0:(.03,0,.97,.68),1.5:(.03,0,.97,.68),2.0:(.16,.26,.32,.47),2.5:(.19,.27,.41,.45),
3.0:(.16,.27,.35,.46),3.5:(.16,.29,.30,.45),4.0:(.17,.28,.33,.45),4.5:(.18,.27,.35,.46),5.0:(.21,.27,.40,.47),5.5:(.23,.27,.40,.47),
6.0:(.22,.27,.41,.47),6.5:(.20,.27,.43,.47),7.0:(.20,.29,.45,.45),7.5:(.26,.25,.40,.42),8.0:(.29,.22,.41,.32),8.5:(.21,.14,.63,.38),
9.0:(.15,.12,.72,.50),9.5:(.11,.14,.83,.48),10.0:(.11,.14,.83,.40)}
save({"mediaId":793,"level":"A","keyWord":"top","defaultVoice":"female","taps":[
 {"phrase":"to lift a big stone","target":"the woman","voice":"female","keys":keys(T21,W)},
 {"phrase":"to put stones on top","target":"the woman","voice":"female","keys":keys(T21,W)},
 {"phrase":"to open her arms","target":"the woman","voice":"female","keys":keys(T21,W)}],
 "stillS":10.0,"nouns":[{"word":"a woman","x":.52,"y":.28,"voice":"female"},{"word":"stones","x":.50,"y":.72,"voice":"female"},{"word":"the sky","x":.70,"y":.08,"voice":"female"},{"word":"grass","x":.80,"y":.60,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","putting","a","stone","on","top."],"answerVoice":"female",
 "notes":"Only one usable target (the woman); a second person in green is just a sliver at the left edge until 4.0 s. Key word 'top' is not used as a noun slot (would label the same place as 'stones'); it is in a phrase and the answer. Her box overlaps the stone pile where she stands behind it."})

# 794
H={1.0:(.39,.34,.20,.26),1.5:(.36,.28,.25,.33),2.0:(.40,.60,.20,.15),2.5:(.36,.50,.30,.19),3.5:(0,.50,.52,.50),4.0:(.10,.47,.74,.53),
5.5:(.33,.48,.59,.52),6.0:(.33,.58,.30,.26),6.5:(.35,.58,.30,.26),9.5:(.34,.81,.38,.19),10.0:(.36,.81,.31,.19),10.5:(.41,.57,.23,.17)}
S={1.0:(.60,.46,.40,.54),1.5:(.66,.40,.34,.60),4.5:(0,.12,.62,.76),5.0:(0,.16,.62,.84),7.0:(.50,.07,.50,.73),7.5:(.50,.07,.50,.73),
8.0:(.30,.10,.70,.70),8.5:(.29,.08,.71,.72),9.0:(.28,.08,.72,.76),10.5:(.34,.74,.36,.13),11.0:(.30,.53,.40,.27),11.5:(.30,.53,.40,.25),12.0:(.30,.53,.40,.23)}
Bo={1.0:(.18,.62,.36,.24),1.5:(.20,.62,.42,.36),4.5:(.64,.46,.36,.36),5.0:(.64,.44,.36,.38),7.0:(0,.44,.48,.36),7.5:(0,.44,.48,.36),
8.0:(0,.46,.28,.34),8.5:(0,.44,.27,.36),9.0:(0,.46,.26,.36),11.0:(.38,.35,.26,.18),11.5:(.36,.35,.30,.18),12.0:(.36,.35,.28,.18)}
save({"mediaId":794,"level":"B","keyWord":"tournament","defaultVoice":"male","taps":[
 {"phrase":"to rearrange the wooden portraits","target":"the man in the straw hat","voice":"male","keys":keys(T25,H)},
 {"phrase":"to carry the champion","target":"the bearded man","voice":"male","keys":keys(T25,S)},
 {"phrase":"to defeat a huge opponent","target":"the small boy","voice":"male","keys":keys(T25,Bo)}],
 "stillS":11.0,"nouns":[{"word":"lanterns","x":.50,"y":.11,"voice":"male"},{"word":"a beard","x":.50,"y":.62,"voice":"male"},{"word":"an apron","x":.82,"y":.72,"voice":"male"},{"word":"a crowd","x":.45,"y":.90,"voice":"male"}],
 "question":"What is the bearded man doing?","answer":["He","is","carrying","the","champion","on","his","shoulders."],"answerVoice":"male",
 "notes":"Many cuts. All three targets off in the wide opening (0.0-0.5, figures too tiny) and in shots of other wrestlers (2.0-3.0 only the man in the straw hat is in the background). At 6.0-6.5 only the two clasped arms fill the picture (owners not identifiable): bearded man and boy set off there, the hat man behind is boxed although his head is hidden. At 4.5-5.0 the bearded man seems to pin the same bald child before the final (AI inconsistency); the boy beats him at 8.0-9.0. A bearded spectator is in the background at 2.5. Key word 'tournament' is not a visible noun, so not in the slots. defaultVoice male = the boy/bearded man as main persons (crowd is mixed; evenId would give female)."})
