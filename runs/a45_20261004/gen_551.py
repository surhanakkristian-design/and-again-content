import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def boxes(lst, start=0.0):
    return {start+i*0.5:b for i,b in enumerate(lst)}
def write(id,level,kw,dv,taps,still,nouns,q,a,av,notes):
    json.dump({"mediaId":id,"level":level,"keyWord":kw,"defaultVoice":dv,
      "taps":[{"phrase":p,"target":tg,"voice":v,"keys":keys(k)} for p,tg,v,k in taps],
      "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
      "question":q,"answer":a,"answerVoice":av,"notes":notes},open(f'content/{id}.json','w'),indent=1)
# 551
pg=boxes([(.13,.31,.51,.41),(.02,.32,.67,.44),(0,.33,.80,.56),(.16,.16,.58,.66),(.06,.09,.70,.38),(.06,.18,.76,.38),(.06,.54,.80,.46),(.16,.34,.70,.66),
 (0,.19,.79,.71),(0,.26,.79,.64),(0,.41,.89,.58),(0,.21,.79,.77),(.35,.10,.50,.58),(.04,0,.78,.51),(.16,.20,.64,.55),(0,0,.71,.56),(.11,0,.85,.39),(.03,.03,.91,.58),(.01,.22,.78,.62),(0,.26,.71,.60),(0,.22,.74,.52)])
write(551,"A","pigeon","male",[("to walk between the chairs","the big pigeon","male",pg),("to fly over a fountain","the big pigeon","male",pg),("to land on a roof","the big pigeon","male",pg)],
 10.0,[("the sky",.60,.12,"male"),("a pigeon",.35,.42,"male"),("a roof",.62,.58,"male"),("a wall",.65,.90,"male")],
 "Where does the pigeon land?",["It","lands","on","a","roof."],"male",
 "Only one real target (the main pigeon); other pigeons appear small in the background at 4.0-5.5 and several birds take off at 6.0, where the box is on the central bird and is a guess. No person is the main subject, evenId false -> male. Question in present simple (a finished event, not something going on).")
# 553
man=boxes([(.28,0,.49,.24),(.24,0,.56,.25),(.21,0,.63,.44),(.24,0,.76,.76),(.60,.18,.40,.70),(.54,.41,.46,.59),(.51,.42,.49,.58),(.51,.41,.49,.59),
 (0,.15,.46,.34),(0,0,.49,.69),(0,0,.40,.99),(0,0,.64,1.0),(0,0,.32,.95),(0,.02,.18,.31)])
for t in (8.0,8.5,9.0,9.5,10.0): man[t]=(0,.14,.58,.86)
pl={7.0:(.10,.29,.50,.18),7.5:(.16,.29,.50,.18)}
for t in (8.0,8.5,9.0,9.5,10.0): pl[t]=(.59,.31,.41,.20)
write(553,"B","pitch","male",[("to mow the pitch","the man in the cap","male",man),("to plant a corner flag","the man in the cap","male",man),("to train in the background","the players","male",pl)],
 10.0,[("a flat cap",.38,.23,"male"),("players",.78,.41,"male"),("a pitch",.80,.68,"male"),("a corner flag",.55,.80,"male")],
 "What is the groundskeeper doing?",["The","groundskeeper","is","mowing","the","pitch."],"male",
 "At 4.0-5.0 only the man's boot and leg are visible (boxed as the man). At 8.0-10.0 the man's box stops at x 0.58 so it does not overlap the players; his right elbow sticks out past it. Players are tiny. 'groundskeeper' appears only in question/answer.")
# 554
w=boxes([(.24,.19,.55,.77),(.32,.17,.50,.80),(.23,.16,.61,.84),(.28,.15,.50,.84),(.29,.16,.47,.69),(.26,.19,.50,.68),(.16,.19,.64,.80),(.26,.19,.52,.78),(.36,.21,.45,.63),(.26,.21,.56,.68),(.31,.17,.50,.82),(.31,.16,.51,.84),(.28,.18,.50,.63),(.30,.16,.48,.65),(.26,.17,.44,.64),(.24,.36,.52,.44),(.28,.44,.39,.38),(.09,.13,.45,.61),(.20,.38,.54,.54),(.20,.43,.56,.50),(.10,.42,.74,.40)])
write(554,"A","place","female",[("to carry a mat","the woman","female",w),("to look for a place","the woman","female",w),("to sit on a mat","the woman","female",w)],
 10.0,[("an umbrella",.65,.13,"female"),("the sea",.35,.33,"female"),("a woman",.42,.58,"female"),("a mat",.22,.76,"female")],
 "What is the woman looking for?",["She","is","looking","for","a","place","to","sit."],"female",
 "One target only: a man appears for a single frame (7.0, putting up the umbrella) and tiny walkers in the far background. 'to look for a place' rests on her shading her eyes and scanning at 3.5-4.0. Key word 'place' is abstract, so it is not a noun slot.")
# 555
wm=boxes([(0,0,.25,.68),(0,0,.32,.76),(0,0,.40,.76),(0,0,.38,.97),(0,0,.30,.98),(0,0,.20,.92),(0,.02,.20,.90),(0,.04,.20,.74),(0,.06,.32,.72),(0,.07,.38,.88),(0,.01,.44,.96),(0,0,.43,.97),(0,0,.44,.97),(0,0,.42,.88),(0,0,.50,.95),(0,0,.33,.90),(0,0,.33,.90),(0,0,.34,.88)],1.5)
mn=boxes([(.72,.16,.28,.22),(.60,.27,.40,.37),(.68,.05,.32,.65),(.43,0,.57,.67),(.43,0,.57,.74),(.40,0,.60,.79),(.48,0,.52,.74),(.72,.38,.28,.37),(.78,0,.22,.66),(.56,0,.44,.26),(.80,0,.20,.16),(.70,0,.30,.26),(.51,0,.49,.48),(.57,0,.43,.54),(.65,0,.35,.42),(.74,0,.26,.32)],2.5)
ct=boxes([(.78,.48,.22,.20),(.76,.44,.24,.40),(.72,.52,.28,.36),(.76,.62,.24,.38),(.68,.80,.32,.20),(.60,.84,.40,.16),(.50,.70,.42,.30),(.52,.76,.36,.24),(.52,.84,.38,.16),(.58,.75,.38,.25),(.65,.76,.35,.24),(.76,.76,.24,.24),(.78,.84,.22,.16)],1.0)
write(555,"A","plant","female",[("to point at a leaf","the woman","female",wm),("to clean a big leaf","the man","male",mn),("to stand on two legs","the cat","female",ct)],
 5.5,[("a window",.40,.14,"female"),("a woman",.14,.30,"female"),("plants",.70,.44,"female"),("a cat",.80,.90,"female")],
 "What is the woman pointing at?",["She","is","pointing","at","a","plant."],"female",
 "In the picture the MAN's hands wipe the leaf with the cloth (the description says the woman). The man is mostly an arm/hands until 6.5, then a face at the top right. Woman at 1.5-2.0 is legs only; 0.0-1.0 off (the watering can's holder is not visible, so no 'to water' phrase). The cat stands on its back legs only at 5.5-6.0. 'plants' = the group on the windowsill; plants are everywhere in the room.")
