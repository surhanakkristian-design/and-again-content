import json
def K(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def W(o): json.dump(o, open(f'content/{o["mediaId"]}.json','w'), indent=1, ensure_ascii=False)

# 4498
t=T(21)
girl={0.0:(0,.15,.30,.62),0.5:(0,.15,.30,.62),1.0:(0,.15,.30,.62),1.5:(0,.10,.27,.62),2.0:(0,.03,.24,.72),2.5:(0,0,.21,.78),3.0:(0,0,.20,.55),3.5:(0,0,.18,.45),10.0:(0,.20,.17,.60)}
boy={0.0:(.31,.22,.42,.52),0.5:(.31,.22,.42,.52),1.0:(.31,.22,.42,.55),1.5:(.28,.18,.43,.55),2.0:(.25,.13,.47,.55),2.5:(.22,.08,.52,.62),3.0:(.21,.02,.60,.85),3.5:(.20,0,.61,.92),4.0:(.15,0,.66,.85),4.5:(.15,0,.66,.90),5.0:(.10,0,.85,.95),5.5:(.08,0,.90,.95),6.0:(.03,0,.95,.85),6.5:(.05,0,.93,.87),7.0:(0,0,.95,.90),7.5:(0,.02,.95,.90),8.0:(0,.02,.95,.95),8.5:(.02,.04,.82,.92),9.0:(.03,.12,.80,.83),9.5:(.05,.17,.82,.75),10.0:(.18,.20,.72,.72)}
bean={0.0:(.74,.17,.24,.14),0.5:(.76,.16,.24,.14),1.0:(.74,.16,.26,.14),1.5:(.72,.09,.27,.30),2.0:(.73,.04,.27,.50),2.5:(.76,0,.24,.55),3.0:(.82,0,.18,.50),3.5:(.82,.02,.18,.45),4.0:(.82,0,.18,.30),4.5:(.82,0,.18,.30),8.5:(.85,.05,.15,.25),9.0:(.84,.10,.16,.50),9.5:(.88,.20,.12,.45)}
W({"mediaId":4498,"level":"B","keyWord":"sign","defaultVoice":"male",
 "taps":[
  {"phrase":"to hold out his cast","target":"the blond boy","voice":"male","keys":K(t,boy)},
  {"phrase":"to scribble in green","target":"the girl with braids","voice":"female","keys":K(t,girl)},
  {"phrase":"to wear a woollen beanie","target":"the boy in the beanie","voice":"male","keys":K(t,bean)}],
 "stillS":10.0,
 "nouns":[{"word":"a plaster cast","x":.55,"y":.55,"voice":"male"},{"word":"a sling","x":.55,"y":.68,"voice":"male"},{"word":"felt-tip pens","x":.70,"y":.89,"voice":"male"},{"word":"a bookshelf","x":.18,"y":.15,"voice":"male"}],
 "question":"What are the friends doing?",
 "answer":["They","are","signing","his","plaster","cast."],
 "answerVoice":"male",
 "notes":"Signing is done by several hands (girl in green at 0-1 s, orange pens of the off-screen redhead / beanie boy later), so no tap phrase uses 'sign'; the answer does. 'to scribble in green' = only the girl with braids writes in green (0.0-1.0 s; she holds the green marker to 3.5 s); the redhead holds a green cap but does not write. Beanie boy is half hidden behind the redhead at 0-1 s and at the frame edge at 8.5-9.5 s (narrow boxes). The girl's arm crosses into the boy's box (split at her body). Redhead girl is no target."})

# 4499
t=T(19)
man={0.0:(.08,.33,.76,.67),0.5:(.08,.35,.82,.65),1.0:(.05,.36,.70,.64),1.5:(0,.38,.92,.62),2.0:(0,.37,.90,.63),2.5:(0,.40,.86,.60),6.0:(0,.68,.55,.32),6.5:(.02,.43,.93,.57),7.0:(.03,.44,.90,.56),7.5:(.03,.43,.72,.57),8.0:(.05,.42,.95,.58),8.5:(.10,.42,.90,.58),9.0:(.08,.40,.70,.60)}
cas={0.5:(.80,0,.20,.18),1.0:(.68,0,.32,.30),1.5:(.52,0,.48,.36),2.0:(.42,0,.58,.36),2.5:(.35,0,.65,.39),3.0:(0,0,1,.65),3.5:(0,0,1,.70),4.0:(0,0,1,.62),4.5:(0,.33,1,.33),5.0:(0,.45,1,.33),6.5:(.62,0,.38,.32),7.0:(.27,.04,.70,.38),7.5:(.20,.04,.70,.37),8.0:(.22,.07,.68,.33),8.5:(.22,.07,.67,.33),9.0:(.20,.07,.66,.32)}
W({"mediaId":4499,"level":"A","keyWord":"visit","defaultVoice":"male",
 "taps":[
  {"phrase":"to visit old castles","target":"the man","voice":"male","keys":K(t,man)},
  {"phrase":"to carry a backpack","target":"the man","voice":"male","keys":K(t,man)},
  {"phrase":"to have tall stone towers","target":"the castle","voice":"male","keys":K(t,cas)}],
 "stillS":8.0,
 "nouns":[{"word":"a castle","x":.50,"y":.25,"voice":"male"},{"word":"trees","x":.15,"y":.45,"voice":"male"},{"word":"a path","x":.82,"y":.68,"voice":"male"},{"word":"a sweater","x":.50,"y":.80,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","visiting","an","old","castle."],
 "answerVoice":"male",
 "notes":"Only one person. 'the castle' = whichever castle building is in the shot (ruined tower 0.5-2.5 s, gatehouse/courtyard 3.0-5.0 s, big castle 6.5-9.0 s); its phrase is a state because it is a thing. At 2.0-2.5 s the ruined wall on the right edge runs down beside the man; the castle box covers only the part above him. At 6.0 s only the man's arm is in the picture."})

# 4500
t=T(21)
wj={0.0:(.42,.50,.32,.42),0.5:(.27,.33,.58,.67),1.0:(.28,.34,.56,.66),1.5:(.28,.33,.50,.67)}
gk={2.5:(.21,.46,.79,.24),3.0:(.14,.36,.73,.32)}
wd={5.5:(.18,.40,.66,.60),6.0:(.22,.47,.56,.53),6.5:(.28,.37,.56,.63),7.0:(.33,.32,.50,.68)}
W({"mediaId":4500,"level":"A","keyWord":"quick","defaultVoice":"female",
 "taps":[
  {"phrase":"to catch a small ball","target":"the woman in jeans","voice":"female","keys":K(t,wj)},
  {"phrase":"to catch a football","target":"the man in green","voice":"male","keys":K(t,gk)},
  {"phrase":"to catch a watermelon","target":"the woman in the dress","voice":"female","keys":K(t,wd)}],
 "stillS":10.0,
 "nouns":[{"word":"a ball","x":.38,"y":.38,"voice":"female"},{"word":"trees","x":.80,"y":.43,"voice":"female"},{"word":"a man","x":.55,"y":.58,"voice":"male"},{"word":"grass","x":.50,"y":.85,"voice":"female"}],
 "question":"What is the man in green doing?",
 "answer":["He","is","catching","a","football."],
 "answerVoice":"male",
 "notes":"Five short shots, five people; three are targets, each visible only in its own shot (the goalkeeper only 2.5-3.0 s). All three phrases are 'to catch' + a different object - the clip is about catching; the objects make them unique. The man in the kitchen (a glass jar) and the man with the beach ball are no targets. Key word 'quick' is an adjective and not used. Still 10.0 s: trees also stand at the left edge behind the ball; the pill is on the group at the right."})

# 4502
t=T(25)
mb={0.0:(0,0,1,1),0.5:(0,.52,.95,.48),1.0:(0,.58,1,.42),1.5:(0,.58,1,.42),2.0:(0,.58,1,.42)}
wo={2.5:(0,.33,1,.67),3.0:(0,.46,1,.54),3.5:(0,.49,1,.51),4.0:(0,.52,1,.48),4.5:(0,.58,1,.42),5.0:(.10,.65,.80,.35),5.5:(.20,.74,.70,.26),6.0:(.28,.84,.52,.16)}
ms={6.5:(.28,.30,.47,.70),7.0:(.27,.33,.48,.67),7.5:(.28,.35,.52,.65),8.0:(.25,.37,.57,.63),8.5:(.22,.39,.63,.61),9.0:(.15,.44,.72,.56),9.5:(.10,.47,.80,.53),10.0:(.06,.50,.86,.50),10.5:(.04,.52,.90,.48),11.0:(.05,.54,.90,.46),11.5:(.04,.56,.90,.44),12.0:(.05,.57,.90,.43)}
W({"mediaId":4502,"level":"B","keyWord":"ceiling","defaultVoice":"female",
 "taps":[
  {"phrase":"to stare at a lightbulb","target":"the man on the bed","voice":"male","keys":K(t,mb)},
  {"phrase":"to gaze at wooden beams","target":"the woman","voice":"female","keys":K(t,wo)},
  {"phrase":"to admire a painted dome","target":"the man in the suit","voice":"male","keys":K(t,ms)}],
 "stillS":1.5,
 "nouns":[{"word":"a ceiling","x":.50,"y":.38,"voice":"female"},{"word":"a lightbulb","x":.50,"y":.20,"voice":"female"},{"word":"a bed","x":.80,"y":.70,"voice":"female"},{"word":"a T-shirt","x":.45,"y":.82,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","gazing","at","the","wooden","beams."],
 "answerVoice":"female",
 "notes":"Three shots, one person each; all three look up, so each phrase names what that person looks at. At 0.0 s the man of the first shot is still upright and fills the picture (bulb not yet visible). The ceiling pill sits on the plain ceiling below the bulb, the wall starts at about y 0.47. Key word 'ceiling' is in the nouns, not in the answer."})
