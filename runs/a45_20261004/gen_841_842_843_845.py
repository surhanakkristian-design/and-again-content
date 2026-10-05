import json
def K(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
def keys(d,n): return [K(i*0.5,d.get(i*0.5)) for i in range(n)]
def out(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 841
W={0:(.74,.18,.26,.30),.5:(.60,.08,.40,.26),1:(.45,.03,.55,.26)}
I={0:(.44,.30,.29,.20),.5:(.35,.35,.45,.35),1:(.28,.30,.47,.40)}
for t in (1.5,2,2.5,3,3.5,4.5,5):
    W[t]=(.15,.08,.83,.51); I[t]=(.15,.60,.70,.21)
W[4]=(.15,.08,.83,.47); I[4]=(.15,.56,.70,.25)
W[5.5]=(.42,.13,.40,.52); I[5.5]=(.03,.31,.38,.20)
W[6]=(.49,.11,.33,.54); I[6]=(.02,.16,.46,.28)
W[6.5]=(.55,.11,.27,.54); I[6.5]=(.06,.06,.48,.35)
W[7]=(.02,.20,.20,.45); I[7]=(.22,.05,.55,.70)
W[7.5]=(.08,.02,.76,.50); I[7.5]=(.36,.54,.44,.17)
W[8]=(.0,.03,.85,.48); I[8]=(.34,.53,.45,.19)
W[8.5]=(.18,.11,.70,.42); I[8.5]=(.39,.54,.40,.17)
W[9]=(.18,.12,.67,.40); I[9]=(.40,.53,.38,.18)
W[9.5]=(.15,.12,.70,.40); I[9.5]=(.36,.53,.40,.18)
for t in (10,10.5,11,11.5):
    W[t]=(.15,.09,.68,.43); I[t]=(.33,.53,.45,.17)
for t in (12,12.5):
    W[t]=(.15,.09,.72,.43); I[t]=(.38,.53,.42,.17)
W[13]=(.08,.13,.92,.39); I[13]=(.38,.54,.44,.17)
W[13.5]=(.36,.28,.30,.48); W[14]=(.34,.28,.32,.36); W[14.5]=(.36,.27,.32,.37); W[15]=(.34,.28,.32,.36)
kw=keys(W,31); ki=keys(I,31)
out({"mediaId":841,"level":"A","keyWord":"melt","defaultVoice":"female",
 "taps":[{"phrase":"to put ice into a kettle","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to melt in a kettle","target":"the ice","voice":"female","keys":ki},
         {"phrase":"to pour water into a pool","target":"the woman","voice":"female","keys":kw}],
 "stillS":10.0,
 "nouns":[{"word":"a woman","x":.42,"y":.25,"voice":"female"},{"word":"a kettle","x":.60,"y":.48,"voice":"female"},
          {"word":"a laptop","x":.16,"y":.60,"voice":"female"},{"word":"ice","x":.58,"y":.90,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","melting","ice","in","a","kettle."],"answerVoice":"female",
 "notes":"Two targets only (woman, ice): the kettle/bowl always overlap them. Woman and ice overlap in most frames, boxes split (ice = lower band where the cubes are; at 7.0 the woman keeps only her left arm strip). 0-1.0 only the woman's arm is visible. 'ice' pill is on the loose cube on the table, not in the kettle, to keep it apart from 'a kettle'. From 11.5 the ice is mostly water. Before the kettle (1.5-5.0) she uses a small torch on the ice."})

# 842
B={0:(.18,.24,.43,.49),.5:(.18,.25,.45,.48),1:(.18,.26,.44,.47),1.5:(.18,.26,.45,.50),2:(.12,.22,.49,.50),2.5:(.05,.21,.56,.51),3:(.08,.22,.50,.50),3.5:(.08,.22,.50,.50)}
M={0:(.62,0,.38,.62),.5:(.64,0,.36,.62),1:(.63,0,.37,.62),1.5:(.64,0,.36,.62),2:(.62,0,.38,.62),2.5:(.62,0,.38,.62),3:(.60,0,.40,.62),3.5:(.60,0,.40,.62)}
L={t:(0,.73,1.0,.17) for t in B}; L[0]=L[.5]=L[1]=(0,.74,1.0,.17); L[1.5]=(0,.77,1.0,.14)
out({"mediaId":842,"level":"A","keyWord":"baby","defaultVoice":"female",
 "taps":[{"phrase":"to pick up a letter","target":"the baby","voice":"female","keys":keys(B,8)},
         {"phrase":"to sit behind the baby","target":"the woman","voice":"female","keys":keys(M,8)},
         {"phrase":"to lie on the floor","target":"the letters","voice":"female","keys":keys(L,8)}],
 "stillS":2.0,
 "nouns":[{"word":"a baby","x":.40,"y":.44,"voice":"female"},{"word":"a woman","x":.78,"y":.13,"voice":"female"},
          {"word":"letters","x":.45,"y":.80,"voice":"female"},{"word":"the floor","x":.60,"y":.94,"voice":"female"}],
 "question":"What is the baby doing?","answer":["The","baby","is","picking","up","a","letter."],"answerVoice":"female",
 "notes":"Baby sits in front of the woman, they overlap: woman box = right strip (face, right arm), baby box = centre/left; her left arm and lap fall outside her box. Top row of letters (y .67-.73) left to the baby box (his hand/feet are there). Baby lifts the orange K at 0.5-1.0; the woman only touches letters."})

# 843
Y={0:(0,.66,.35,.34),.5:(0,.72,.45,.28),1:(0,.66,.42,.34),1.5:(0,.68,.42,.32),
   3:(.10,.42,.78,.58),3.5:(.08,.55,.78,.45),4:(.17,.52,.70,.48),4.5:(.12,.42,.86,.58),5:(.10,.22,.78,.78),5.5:(.09,.16,.76,.82),
   6:(.17,.29,.60,.71),6.5:(.27,.38,.50,.62),7:(.31,.62,.20,.36),7.5:(.29,.62,.20,.38),8:(.28,.65,.21,.35),8.5:(.29,.66,.23,.34),
   9:(.24,.72,.27,.28),9.5:(.24,.76,.27,.24),10:(.22,.82,.29,.18)}
BK={0:(.36,.48,.55,.35),.5:(.46,.37,.48,.31),1:(.40,.30,.40,.27),1.5:(.38,.25,.37,.24),2:(0,.72,.94,.28),2.5:(0,.42,.86,.50)}
BL={7:(.34,.29,.36,.27),7.5:(.37,.25,.33,.27),8:(.36,.21,.33,.26),8.5:(.38,.17,.29,.24),9:(.38,.14,.27,.20),9.5:(.40,.12,.24,.18),10:(.41,.11,.22,.16)}
out({"mediaId":843,"level":"A","keyWord":"up","defaultVoice":"female",
 "taps":[{"phrase":"to go up on a rope","target":"the basket","voice":"female","keys":keys(BK,21)},
         {"phrase":"to climb up a ladder","target":"the woman in yellow","voice":"female","keys":keys(Y,21)},
         {"phrase":"to fly up into the sky","target":"the balloon","voice":"female","keys":keys(BL,21)}],
 "stillS":5.0,
 "nouns":[{"word":"a woman","x":.42,"y":.44,"voice":"female"},{"word":"a ladder","x":.70,"y":.62,"voice":"female"},
          {"word":"shoes","x":.38,"y":.92,"voice":"female"},{"word":"the sky","x":.25,"y":.10,"voice":"female"}],
 "question":"What is the woman in yellow doing?","answer":["She","is","climbing","up","a","ladder."],"answerVoice":"female",
 "notes":"Key word 'up' is in all three phrases and the answer. Woman in yellow: at 2.0-2.5 off (only her hand at 2.5). On the roof (7.0-10.0) she stands right next to the woman in green; her box touches that woman a little. The far balloon speck at 4.0-6.5 is left off. At 0-1.5 the woman in yellow is the one pulling the rope."})

# 845
G={0:(.18,.29,.70,.40),.5:(.03,.04,.52,.62),1:(.02,.05,.50,.62),1.5:(.18,.07,.42,.58),2:(.19,.07,.40,.58),2.5:(.18,.07,.40,.59),
   3:(.07,.10,.60,.56),3.5:(.09,.10,.58,.56),4:(.17,.28,.54,.37),4.5:(.13,.08,.50,.57),5:(.13,.08,.47,.58),5.5:(.13,.08,.46,.58),
   6:(.17,.13,.44,.53),6.5:(.10,.17,.54,.49),7:(.10,.17,.53,.49)}
S={0:(.05,.70,.88,.22),.5:(.05,.67,.90,.25),1:(.05,.68,.88,.24),1.5:(.05,.66,.90,.26),4:(.13,.66,.74,.16),4.5:(.15,.66,.72,.16),5:(.15,.67,.74,.16)}
V={2:(0,.66,1.0,.34),2.5:(.60,.30,.40,.24),5:(.80,.33,.20,.16),5.5:(.60,.32,.40,.26)}
out({"mediaId":845,"level":"B","keyWord":"vanishing","defaultVoice":"female",
 "taps":[{"phrase":"to sketch a spiral","target":"the girl","voice":"female","keys":keys(G,15)},
         {"phrase":"to vanish without a trace","target":"the spiral","voice":"female","keys":keys(S,15)},
         {"phrase":"to sweep across the beach","target":"the wave","voice":"female","keys":keys(V,15)}],
 "stillS":5.0,
 "nouns":[{"word":"a spiral","x":.50,"y":.72,"voice":"female"},{"word":"a wooden stick","x":.19,"y":.28,"voice":"female"},
          {"word":"denim shorts","x":.38,"y":.38,"voice":"female"},{"word":"clouds","x":.86,"y":.15,"voice":"female"}],
 "question":"What is the girl doing?","answer":["She","is","sketching","a","spiral","in","the","sand."],"answerVoice":"female",
 "notes":"Key word 'vanishing' is not a visible noun; it is carried by the phrase 'to vanish without a trace'. The wave is one rectangle only: at 2.0 the lower band (thick foam bottom left + water over the drawing), at 2.5/5.5 the foam line right of the girl, at 5.0 the foam entering at the right edge; faint foam at 6.0+ is off. At 0.0 and 4.0 the stick tip reaches into the spiral box (split at the feet line)."})
