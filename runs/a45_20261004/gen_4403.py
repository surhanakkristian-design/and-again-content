import json
def keys(n, d):
    out=[]
    for i in range(n):
        t=i*0.5
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def dump(o): json.dump(o, open(f"content/{o['mediaId']}.json","w"), indent=1, ensure_ascii=False)

# 4403
m={0.0:(.2,.2,.7,.8),0.5:(.18,.2,.8,.8),1.0:(.2,.2,.7,.8),1.5:(.15,.2,.8,.8),2.0:(.08,.2,.92,.8),2.5:(.03,.2,.97,.8),
3.0:(.03,.18,.95,.82),3.5:(.08,.16,.92,.84),4.0:(.08,.05,.92,.95),4.5:(.03,.16,.94,.84),5.0:(0,.16,1,.84),5.5:(0,.18,1,.82),
6.0:(0,.16,1,.84),6.5:(0,.07,1,.93),7.0:(0,.14,1,.86),7.5:(0,.14,1,.86)}
for t in [8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0]: m[t]=(0,.1,1,.9)
k=keys(25,m)
dump({"mediaId":4403,"level":"B","keyWord":"layer","defaultVoice":"male",
"taps":[{"phrase":"to shiver with cold","target":"the man","voice":"male","keys":k},
{"phrase":"to pile on woollen layers","target":"the man","voice":"male","keys":k},
{"phrase":"to snuggle under the blankets","target":"the man","voice":"male","keys":k}],
"stillS":0.0,
"nouns":[{"word":"a cushion","x":.25,"y":.33,"voice":"male"},{"word":"blankets","x":.14,"y":.47,"voice":"male"},
{"word":"a jumper","x":.52,"y":.57,"voice":"male"},{"word":"a sofa","x":.17,"y":.84,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","piling","on","layers","of","blankets."],"answerVoice":"male",
"notes":"Only one possible target (the man), used for all three phrases. 'to shiver with cold' rests on 0.0-1.0 s (arms hugged around himself); it is read from posture. Key word 'layer' is in a phrase and the answer, not a noun slot (no single place for it on the still)."})

# 4404
man={0.0:(0,0,.95,1),0.5:(0,.03,1,.97),1.0:(0,.08,.88,.92),1.5:(0,.22,.88,.78),2.0:(0,.1,.92,.9),2.5:(0,0,1,1),
3.0:(0,0,.82,1),3.5:(0,0,.84,1),4.0:(0,0,.78,.9),4.5:(0,0,1,.9),5.0:(0,0,.66,.9),5.5:(0,0,.78,1),6.0:(0,0,.75,1),
6.5:(0,.47,.78,.53),7.0:(0,.45,.76,.55),7.5:(0,.45,.82,.55),8.0:(0,.36,.72,.64),8.5:(0,.37,.7,.6),9.0:(0,.47,.7,.53)}
wom={6.5:(0,.17,.3,.28),7.0:(0,.1,.28,.33),7.5:(0,.1,.3,.34),8.0:(0,.1,.3,.25),8.5:(0,.1,.3,.26),9.0:(0,.13,.28,.32)}
km=keys(19,man); kw=keys(19,wom)
dump({"mediaId":4404,"level":"B","keyWord":"injury","defaultVoice":"male",
"taps":[{"phrase":"to rinse an injured finger","target":"the man","voice":"male","keys":km},
{"phrase":"to apply a small plaster","target":"the man","voice":"male","keys":km},
{"phrase":"to carry on cooking","target":"the woman","voice":"female","keys":kw}],
"stillS":0.0,
"nouns":[{"word":"an injury","x":.52,"y":.51,"voice":"male"},{"word":"an apron","x":.25,"y":.78,"voice":"male"},
{"word":"a knife","x":.80,"y":.76,"voice":"male"},{"word":"a chopping board","x":.60,"y":.93,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","rinsing","his","injured","finger","under","the","tap."],"answerVoice":"male",
"notes":"The woman is small, blurred and only visible from 6.5 s (left edge, behind the man's arm). From 6.5 s the man's box is his hands only (his nose tip at the top left is left out) so that it does not overlap the woman's box. 'an injury' sits on the bleeding fingertip at 0.0 s. The answer describes the middle of the clip (2.5-4.5 s); the question is general."})

# 4405
S={0.0:(.05,.1,.95,.68),0.5:(.08,.1,.92,.68),1.0:(.05,.1,.95,.7),1.5:(.15,.1,.85,.7),2.0:(.05,.1,.95,.64),2.5:(.07,.14,.93,.62),
3.0:(.03,.18,.92,.67),3.5:(0,.2,.81,.7),4.0:(0,.22,.61,.55),4.5:(0,.22,.57,.55),5.0:(0,.28,.54,.57),5.5:(0,.26,.52,.6),
6.0:(.02,.22,.57,.55),6.5:(.05,.2,.76,.6),7.0:(.05,.22,.88,.65),7.5:(.05,.18,.95,.7),8.0:(.03,.12,.97,.65),8.5:(.03,.12,.97,.66),
9.0:(.02,.1,.98,.68),9.5:(.02,.1,.98,.68),10.0:(.02,.1,.98,.68)}
F={3.5:(.82,0,.18,.85),4.0:(.62,0,.38,.77),4.5:(.58,0,.42,.78),5.0:(.55,0,.45,.85),5.5:(.54,0,.46,.86),6.0:(.6,0,.4,.75),6.5:(.82,0,.18,.72)}
ks=keys(21,S); kf=keys(21,F)
dump({"mediaId":4405,"level":"A","keyWord":"help","defaultVoice":"male",
"taps":[{"phrase":"to sit at a desk","target":"the sitting man","voice":"male","keys":ks},
{"phrase":"to cover his nose","target":"the sitting man","voice":"male","keys":ks},
{"phrase":"to give him tissues","target":"the standing man","voice":"male","keys":kf}],
"stillS":8.0,
"nouns":[{"word":"a sweater","x":.68,"y":.52,"voice":"male"},{"word":"a laptop","x":.14,"y":.84,"voice":"male"},
{"word":"a box","x":.72,"y":.80,"voice":"male"},{"word":"a book","x":.45,"y":.94,"voice":"male"}],
"question":"What is the sitting man doing?",
"answer":["He","is","holding","a","tissue","to","his","nose."],"answerVoice":"male",
"notes":"The two men overlap from 4.0 to 6.0 s (the standing man leans over and reaches across): the boxes are split along a vertical line, so the sitting man's right shoulder falls into the standing man's box and the standing man's reaching hand into the sitting man's box. The standing man is off at 3.0 and 7.0 s (only a sliver at the right edge). Key word 'help' (noun) is not a visible thing, so it is in no slot; the helping is the third phrase."})

# 4406
W={0.0:(.08,0,.92,.48),0.5:(.08,0,.92,.42),1.0:(.05,0,.95,.35),1.5:(.15,.08,.85,.38),2.0:(.08,.05,.92,.37),2.5:(.05,.05,.95,.37),
3.0:(0,.05,1,.32),3.5:(0,.05,1,.32),4.0:(.05,.03,.95,.36),4.5:(0,.03,1,.29),5.0:(.1,.05,.9,.42),5.5:(.08,.05,.92,.48),
6.0:(.08,.03,.92,.44),6.5:(.44,.03,.56,.95),7.0:(.52,.05,.48,.93),7.5:(.1,.08,.9,.3),8.0:(.2,.1,.8,.56),8.5:(.13,.1,.87,.9),
9.0:(.43,.28,.57,.72),9.5:(.44,.28,.56,.72),10.0:(.44,.25,.56,.75),10.5:(.44,.25,.56,.75),11.0:(.44,.28,.56,.72)}
A={0.0:(0,.5,.72,.5),0.5:(0,.43,.7,.57),1.0:(0,.37,.8,.63),1.5:(0,.47,.48,.53),2.0:(0,.43,.5,.57),2.5:(0,.43,.52,.57),
3.0:(0,.38,.6,.62),3.5:(0,.38,.58,.62),4.0:(0,.4,.48,.57),4.5:(0,.33,.58,.67),5.0:(0,.48,.62,.52),5.5:(.05,.55,.9,.45),
6.0:(.05,.48,.93,.52),6.5:(0,.38,.42,.42),7.0:(0,.4,.5,.6),7.5:(.05,.4,.77,.6),8.0:(0,.68,.92,.32),
9.0:(0,0,.42,.86),9.5:(0,0,.42,.86),10.0:(0,0,.42,.75),10.5:(0,0,.42,.75),11.0:(0,0,.42,.8)}
kw=keys(23,W); ka=keys(23,A)
dump({"mediaId":4406,"level":"B","keyWord":"smooth","defaultVoice":"female",
"taps":[{"phrase":"to smooth out harsh stripes","target":"the makeup artist","voice":"male","keys":ka},
{"phrase":"to dab with a sponge","target":"the makeup artist","voice":"male","keys":ka},
{"phrase":"to keep her eyes shut","target":"the woman","voice":"female","keys":kw}],
"stillS":8.0,
"nouns":[{"word":"a hair clip","x":.74,"y":.20,"voice":"female"},{"word":"an eyebrow","x":.42,"y":.36,"voice":"female"},
{"word":"a makeup brush","x":.72,"y":.75,"voice":"female"},{"word":"a hoodie","x":.72,"y":.92,"voice":"female"}],
"question":"What is the makeup artist doing?",
"answer":["He","is","smoothing","out","the","harsh","stripes."],"answerVoice":"male",
"notes":"Until 8.0 s the makeup artist is only his hand with the sponge or brush; his face appears from 9.0 s (that is why the voice is male). His hand lies on the woman's face, so the boxes are split: the woman's box is the part of her head above the hand (her chin, neck and hoodie fall outside or into his box), at 6.5 and 7.0 s the split is vertical. He is off at 8.5 s (only a dark sleeve at the left edge). Her eyes are open at 6.5-7.5 s and from 9.0 s; 'to keep her eyes shut' holds for most of the clip and never for him. The key word is a verb, so it is in a phrase and the answer, not a noun slot."})
