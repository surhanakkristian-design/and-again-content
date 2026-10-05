import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def W(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4316
t=T(25)
man={0.0:(0,.18,.45,.82),0.5:(0,.45,.56,.55),1.0:(0,.50,.57,.50),1.5:(.05,.18,.90,.70),2.0:(.03,.06,.90,.72),
2.5:(.07,.10,.86,.63),3.0:(.05,.10,.83,.63),3.5:(.05,.15,.82,.60),4.0:(0,.10,.90,.63),4.5:(0,.12,.90,.75),
5.0:(0,.12,.90,.83),5.5:(0,.10,.88,.80),6.0:(.03,.08,.88,.65),6.5:(.05,.10,.93,.63),7.0:(0,.37,.55,.63),
7.5:(0,.30,.58,.70),8.0:(0,.48,.58,.52),8.5:(0,.48,.58,.52),9.0:(0,.50,.58,.50),9.5:(0,.50,.58,.50),
10.0:(0,.48,.56,.52),10.5:(0,.48,.56,.52),11.0:(0,.50,.54,.50),11.5:(0,.36,.57,.64),12.0:(0,.18,.36,.82)}
wom={0.0:(.60,.17,.40,.60),0.5:(.60,.15,.40,.62),1.0:(.58,.17,.42,.68),7.0:(.56,.17,.44,.63),7.5:(.60,.17,.40,.68),
8.0:(.60,.15,.40,.62),8.5:(.60,.15,.40,.62),9.0:(.60,.17,.40,.68),9.5:(.60,.17,.40,.66),10.0:(.57,.15,.43,.62),
10.5:(.57,.15,.43,.62),11.0:(.55,.17,.45,.68),11.5:(.58,.17,.42,.68),12.0:(.58,.15,.42,.62)}
W({"mediaId":4316,"level":"A","keyWord":"sorry","defaultVoice":"male","taps":[
 {"phrase":"to clean the laptop","target":"the man","voice":"male","keys":K(t,man)},
 {"phrase":"to cross her arms","target":"the woman","voice":"female","keys":K(t,wom)},
 {"phrase":"to give her flowers","target":"the man","voice":"male","keys":K(t,man)}],
 "stillS":12.0,
 "nouns":[{"word":"a clock","x":.18,"y":.18,"voice":"male"},{"word":"a man","x":.13,"y":.42,"voice":"male"},
  {"word":"flowers","x":.70,"y":.50,"voice":"male"},{"word":"a laptop","x":.80,"y":.77,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","giving","the","woman","flowers."],"answerVoice":"male",
 "notes":"Clip order differs from the packet description: it opens and ends on the wide shot with the woman. Key word 'sorry' (adjective) cannot be shown without sound, so it is not in the texts. Woman is off in the close-ups (1.5-6.5 s). At 7.0 and 11.5 s the man's hands reach under/in front of the woman; boxes split at x 0.55-0.57. The woman's arms are crossed 0.0-1.0 and 7.0-9.0 s only."})

# ---------- 4317
t=T(21)
man={0.0:(0,0,.62,.50),0.5:(.05,0,.69,.62),1.0:(0,0,.68,.70),1.5:(0,.02,.68,.68),2.0:(0,.04,.76,.60),2.5:(0,.04,.76,.66),
3.0:(0,.04,.70,.85),3.5:(0,.04,.78,.82),4.0:(.03,.04,.74,.76),4.5:(0,.13,.70,.57),5.0:(0,.13,.60,.60),5.5:(0,.08,.42,.62),
6.5:(0,.12,.38,.52),7.0:(0,.06,.55,.66),7.5:(0,.04,.67,.68),8.0:(.02,.20,.67,.50),8.5:(.02,.23,.70,.50),9.0:(.02,.08,.63,.72),
9.5:(0,.04,.67,.68),10.0:(0,.08,.53,.52)}
wom={0.0:(.63,.03,.37,.78),0.5:(.75,.02,.25,.75),1.0:(.69,.10,.31,.80),1.5:(.69,.10,.31,.75),2.0:(.77,.12,.23,.70),2.5:(.77,.12,.23,.66),
3.0:(.71,.14,.29,.78),3.5:(.79,.14,.21,.72),4.0:(.78,.14,.22,.68),4.5:(.71,.14,.29,.68),5.0:(.61,.14,.39,.78),5.5:(.50,.13,.50,.80),
6.0:(.50,.13,.50,.70),6.5:(.50,.13,.50,.70),7.0:(.56,.15,.44,.78),7.5:(.68,.16,.32,.76),8.0:(.70,.14,.30,.68),8.5:(.73,.14,.27,.66),
9.0:(.66,.15,.34,.77),9.5:(.68,.16,.32,.76),10.0:(.54,.15,.46,.67)}
W({"mediaId":4317,"level":"A","keyWord":"apologize","defaultVoice":"male","taps":[
 {"phrase":"to dry the wet book","target":"the man","voice":"male","keys":K(t,man)},
 {"phrase":"to smile at him","target":"the woman","voice":"female","keys":K(t,wom)},
 {"phrase":"to bring a coffee","target":"the man","voice":"male","keys":K(t,man)}],
 "stillS":10.0,
 "nouns":[{"word":"a lamp","x":.72,"y":.12,"voice":"male"},{"word":"a woman","x":.80,"y":.42,"voice":"female"},
  {"word":"a cup","x":.42,"y":.67,"voice":"male"},{"word":"a table","x":.50,"y":.85,"voice":"male"}],
 "question":"What is the man bringing her?","answer":["He","is","bringing","her","a","cup","of","coffee."],"answerVoice":"male",
 "notes":"Key word 'apologize' needs the sound, so it is not in the texts. The two people sit very close: boxes are split along a vertical line, the woman's forearm on the table is partly outside her box in the early frames. The woman smiles from about 7.5 s; the man also smiles at the end, 'at him' ties the phrase to her. Man is out of frame at 6.0 s."})

# ---------- 4318
t=T(21)
P=(0,.04,.20,.22)
man={0.0:(.03,.26,.97,.74),0.5:(.03,.26,.97,.74),1.0:(0,.28,1,.72),1.5:(0,.28,1,.72),2.0:(0,.26,1,.74),2.5:(0,.26,1,.74),
3.0:(0,.27,1,.73),3.5:(0,.22,1,.78),4.0:(0,.27,1,.73),4.5:(0,.27,1,.73),5.0:(0,.27,1,.73),5.5:(0,.22,1,.78),6.0:(0,.22,1,.78),
6.5:(0,.22,1,.78),7.0:(0,.22,1,.78),7.5:(0,.28,.92,.72),8.0:(0,0,.97,.97),8.5:(0,0,1,1),9.0:(0,.03,.95,.97),9.5:(0,.10,1,.90),10.0:(.03,.17,.97,.83)}
perf={0.0:P,0.5:P,1.0:(0,.06,.20,.22),1.5:(0,.06,.20,.22),2.0:P,2.5:P,3.0:(0,.05,.18,.22),4.0:(0,.05,.18,.22),4.5:(0,.05,.18,.22),5.0:(0,.05,.18,.22),7.5:(0,.06,.18,.22)}
W({"mediaId":4318,"level":"B","keyWord":"applause","defaultVoice":"male","taps":[
 {"phrase":"to applaud above his head","target":"the bearded man","voice":"male","keys":K(t,man)},
 {"phrase":"to perform on the stage","target":"the performer","voice":"male","keys":K(t,perf)},
 {"phrase":"to beam with delight","target":"the bearded man","voice":"male","keys":K(t,man)}],
 "stillS":0.5,
 "nouns":[{"word":"a stage","x":.22,"y":.26,"voice":"male"},{"word":"sunglasses","x":.76,"y":.28,"voice":"male"},
  {"word":"a beard","x":.68,"y":.48,"voice":"male"},{"word":"a sleeve","x":.36,"y":.76,"voice":"male"}],
 "question":"What is the bearded man doing?","answer":["He","is","applauding","the","performer","on","the","stage."],"answerVoice":"male",
 "notes":"Key word 'applause' is not a visible noun; the answer uses the verb 'applauding'. The performer is small, blurred and at the left edge (clear 0-2.5 s, a sliver 3.0-5.0 and 7.5 s; from 9.0 s seen only through the man's raised arms, set off). The performer's gender is unclear, voice = default. The whole audience claps, so the clapping phrase is tied to the bearded man by 'above his head' (from 8.0 s). The man's box starts just under the performer's box, cutting 1-2 % off the top of his sunglasses in some frames. Pills 'a stage' and 'sunglasses' are 0.54 apart in x at nearly the same y."})

# ---------- 4319
t=T(23)
art={0.0:(0,.56,.76,.44),0.5:(0,.44,.56,.56),1.0:(0,.57,.76,.43),1.5:(0,.59,1,.41),2.0:(0,.53,.70,.33),2.5:(0,0,.52,1),3.0:(0,0,.40,1),
3.5:(0,0,.40,1),4.0:(0,.08,.38,.92),4.5:(0,.42,.44,.58),5.0:(0,.38,.42,.62),5.5:(0,.35,.40,.65),6.0:(0,.35,.66,.65),6.5:(0,.40,.84,.60),
7.0:(0,.57,.84,.43),7.5:(0,.58,.84,.42),8.0:(0,.40,.80,.60),8.5:(0,0,.39,1),9.0:(0,0,.38,1),9.5:(0,0,.39,1),10.0:(0,0,.39,1),10.5:(0,0,.50,1),11.0:(0,0,.39,1)}
wom={0.0:(.18,0,.82,.55),0.5:(.20,0,.80,.43),1.0:(.20,0,.80,.56),1.5:(.20,0,.80,.58),2.0:(.38,0,.62,.52),2.5:(.53,.18,.47,.82),3.0:(.41,.25,.59,.75),
3.5:(.41,.24,.59,.76),4.0:(.40,.23,.60,.77),4.5:(.45,.05,.55,.95),5.0:(.48,.08,.52,.92),5.5:(.48,.08,.52,.92),6.0:(.36,0,.64,.34),6.5:(.28,0,.72,.39),
7.0:(.22,0,.78,.56),7.5:(.22,0,.78,.57),8.0:(.25,0,.75,.39),8.5:(.40,.20,.60,.80),9.0:(.39,.23,.61,.77),9.5:(.40,.20,.60,.80),10.0:(.40,.18,.60,.82),
10.5:(.51,.18,.49,.82),11.0:(.40,.18,.60,.82)}
W({"mediaId":4319,"level":"B","keyWord":"blend","defaultVoice":"female","taps":[
 {"phrase":"to blend the foundation","target":"the make-up artist","voice":"female","keys":K(t,art)},
 {"phrase":"to keep her eyes closed","target":"the woman in the towel","voice":"female","keys":K(t,wom)},
 {"phrase":"to apply dark lipstick","target":"the make-up artist","voice":"female","keys":K(t,art)}],
 "stillS":10.0,
 "nouns":[{"word":"a mirror","x":.48,"y":.17,"voice":"female"},{"word":"a towel","x":.80,"y":.26,"voice":"female"},
  {"word":"a palette","x":.40,"y":.57,"voice":"female"},{"word":"a cardigan","x":.14,"y":.76,"voice":"female"}],
 "question":"What is the make-up artist doing?","answer":["She","is","blending","the","foundation","with","a","sponge."],"answerVoice":"female",
 "notes":"In the close-ups (0-2.0, 4.5-8.0 s) only the make-up artist's hand is in the picture: her box is the hand with sponge / lipstick, the woman's box is the rest of the face, split along a horizontal line, so part of the woman's chin and cheek lies outside her box there. In the wide shots the artist's arm reaches across the woman; boxes split along a vertical line. The woman's eyes are closed 0-5.5 s and open at the end. 'a palette' (eyeshadow palette on the table) is small; 'sponge' in the answer is not among the phrases/nouns but is clearly shown."})
