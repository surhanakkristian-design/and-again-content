import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 85
t=T(19)
man={0.0:(0,0,.54,.98),0.5:(0,.25,.56,.38),1.0:(0,.18,.52,.60),1.5:(0,0,.60,1.0),2.0:(0,0,.54,.90),
 2.5:(0,.08,1.0,.92),3.0:(0,.28,.85,.72),4.5:(.08,.42,.80,.45),5.0:(.05,.28,.87,.72),5.5:(.03,.22,.80,.78),
 6.0:(0,.24,1.0,.76),6.5:(0,.32,.87,.68),7.0:(0,.28,.65,.72),7.5:(0,.26,.91,.74),8.0:(0,.20,1.0,.80),
 8.5:(0,.20,1.0,.80),9.0:(0,.24,1.0,.76)}
kid={0.0:(.55,.50,.40,.48),0.5:(.57,.36,.43,.64),1.0:(.52,.55,.48,.45),1.5:(.60,.38,.38,.62),2.0:(.54,.36,.40,.56),
 3.5:(.05,.05,.92,.95),4.0:(0,0,1.0,1.0),4.5:(.89,0,.11,1.0),5.0:(.90,0,.10,.24),5.5:(.84,0,.16,.36),
 6.0:(.86,0,.14,.22),6.5:(.70,0,.30,.32),7.0:(.66,0,.34,.50),7.5:(.91,.08,.09,.85)}
save({"mediaId":85,"level":"B","keyWord":"betray","defaultVoice":"male",
 "taps":[
  {"phrase":"to tumble into the hay","target":"the man","voice":"male","keys":K(t,man)},
  {"phrase":"to fold his arms confidently","target":"the man","voice":"male","keys":K(t,man)},
  {"phrase":"to grin mischievously","target":"the child","voice":"male","keys":K(t,kid)}],
 "stillS":0.0,
 "nouns":[{"word":"cypress trees","x":.72,"y":.24,"voice":"male"},{"word":"a bun","x":.22,"y":.05,"voice":"male"},
  {"word":"dungarees","x":.73,"y":.83,"voice":"male"},{"word":"a hay bale","x":.40,"y":.95,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","tumbling","into","the","hay."],"answerVoice":"male",
 "notes":"Child's gender is not clear (description says 'kid'), so target 'the child' with the default (male) voice. At 0.5/1.0 only the two hands (pinky promise) are visible: boxed as man (left hand) and child (right arm). Where the child stands close to the man the boxes are split on a vertical line (1.5, 2.0), the child's outstretched hand falls into the man's box. 7.0: the man's right shoulder is cut off by the child's box. 'a bun' = the man's hair bun; two tractors in the still, so no 'tractor'."})

# 86
t=T(21)
W={0.0:(0,0,.55,.33),0.5:(0,0,.53,.37),1.0:(0,0,.55,.60),1.5:(0,.04,.59,.78),2.0:(0,.12,.56,.62),2.5:(0,.12,.55,.52),
 3.0:(0,.13,.55,.55),3.5:(0,.11,.53,.55),4.0:(0,.17,.52,.45),4.5:(0,.14,.48,.38),5.0:(0,.13,.52,.58),5.5:(0,.11,.50,.60),
 6.0:(0,.07,.52,.56),6.5:(0,.10,.49,.55),7.0:(0,.10,.52,.49),7.5:(0,.15,.48,.50),8.0:(0,.15,.49,.45),8.5:(0,0,.34,.60)}
M={0.0:(.56,0,.44,.34),0.5:(.54,0,.46,.38),1.0:(.55,0,.45,.64),1.5:(.60,.02,.40,.62),2.0:(.56,0,.44,.52),2.5:(.55,.05,.45,.55),
 3.0:(.55,.06,.45,.60),3.5:(.53,.08,.47,.62),4.0:(.52,.04,.48,.60),4.5:(.50,.02,.50,.60),5.0:(.52,.06,.48,.65),5.5:(.50,.05,.50,.77),
 6.0:(.52,0,.48,.70),6.5:(.50,.02,.50,.60),7.0:(.52,.03,.48,.80),7.5:(.48,.05,.52,.64),8.0:(.50,.02,.50,.58),8.5:(.50,0,.50,.62),
 9.0:(.48,0,.52,.70),9.5:(.27,0,.47,.58),10.0:(0,0,.55,.54)}
Wt={0.0:(.68,.56,.32,.34),0.5:(.62,.52,.38,.33),2.0:(0,0,.20,.12),2.5:(0,0,.40,.12),3.0:(0,0,.40,.13),3.5:(0,0,.42,.11),
 4.0:(0,.02,.50,.15),4.5:(.02,0,.46,.14),5.0:(0,0,.44,.13),5.5:(.05,0,.40,.11),6.0:(.20,0,.22,.07),6.5:(.02,0,.40,.10),
 7.0:(0,0,.34,.10),7.5:(0,0,.36,.15),8.0:(0,0,.32,.15),9.0:(0,.02,.35,.58),9.5:(0,0,.26,.58)}
save({"mediaId":86,"level":"B","keyWord":"bill","defaultVoice":"female",
 "taps":[
  {"phrase":"to unfold the long bill","target":"the woman","voice":"female","keys":K(t,W)},
  {"phrase":"to count out the banknotes","target":"the bearded man","voice":"male","keys":K(t,M)},
  {"phrase":"to wear a black apron","target":"the waiter","voice":"male","keys":K(t,Wt)}],
 "stillS":9.5,
 "nouns":[{"word":"a waiter","x":.14,"y":.22,"voice":"male"},{"word":"a bill","x":.50,"y":.68,"voice":"female"},
  {"word":"banknotes","x":.50,"y":.78,"voice":"female"},{"word":"a carafe","x":.87,"y":.48,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","unfolding","the","long","bill."],"answerVoice":"female",
 "notes":"The waiter stands behind the woman's head in most frames: his box is only the strip above her headband (small, below the minimum height in places), his body beside her head falls into her box. 0.0/0.5: only the waiter's hand with a cloth is visible (boxed as the waiter). 8.5 and 10.0: waiter only a sliver -> off. 9.0: a raised hand at x .35-.48 belongs to nobody clearly, left outside both boxes. Waiter phrase is a state (he does no clear action of his own). Woman's hands reaching under the man's arm (1.5, 2.0, 5.0) fall partly outside her box. 'a bill' and 'banknotes' pills are close (0.10 in y)."})

# 87
b={0.0:(.21,.21,.55,.56),0.5:(.18,.20,.56,.57),1.0:(.20,.21,.54,.56),1.5:(.20,.19,.54,.58),2.0:(.17,.17,.58,.60),
 2.5:(.18,.17,.58,.60),3.0:(.13,.18,.78,.58),3.5:(.13,.19,.80,.59),4.0:(.04,.20,.96,.58),4.5:(.18,.20,.76,.58),
 5.0:(.24,.29,.60,.48),5.5:(.11,.08,.89,.63),6.5:(.70,.55,.26,.16),7.0:(.02,.40,.28,.18),7.5:(.31,.42,.25,.21),
 8.0:(.31,0,.60,.36),8.5:(.17,.10,.65,.56),9.0:(.16,.19,.60,.67),9.5:(.16,.23,.56,.68),10.0:(.14,.24,.58,.62)}
k=K(t,b)
save({"mediaId":87,"level":"A","keyWord":"bird","defaultVoice":"male",
 "taps":[{"phrase":"to sing a song","target":"the bird","voice":"male","keys":k},
  {"phrase":"to sit on a branch","target":"the bird","voice":"male","keys":k},
  {"phrase":"to fly over the grass","target":"the bird","voice":"male","keys":k}],
 "stillS":0.0,
 "nouns":[{"word":"a bird","x":.48,"y":.42,"voice":"male"},{"word":"a branch","x":.72,"y":.73,"voice":"male"},
  {"word":"grass","x":.45,"y":.92,"voice":"male"},{"word":"the sky","x":.62,"y":.06,"voice":"male"}],
 "question":"What is the bird doing?",
 "answer":["The","bird","is","singing","on","a","branch."],"answerVoice":"male",
 "notes":"Only one target (the bird). 6.0: bird out of frame -> off. 6.5: only a small blurred reddish blob at about (0.82, 0.63) that is probably the flying bird, boxed, not certain. 'the sky' is the pale sky behind the upper branches; 'a branch' sits on the branch the bird stands on (other branches are in the picture)."})

# 88
t=T(15)
d={0.0:(.02,.17,.86,.83),0.5:(.02,.16,.88,.84),1.0:(0,.14,.88,.86),1.5:(.02,.19,.89,.81),2.0:(.02,.19,.86,.81),
 2.5:(.02,.19,.88,.81),3.0:(.03,.20,.86,.80),3.5:(.04,.20,.88,.80),4.0:(.09,.13,.82,.87),4.5:(.08,.15,.81,.85),
 5.0:(.14,.18,.75,.82),5.5:(.11,.17,.78,.83),6.0:(.12,.16,.77,.84),6.5:(.14,.21,.75,.79),7.0:(.14,.19,.75,.81)}
k=K(t,d)
save({"mediaId":88,"level":"A","keyWord":"dog","defaultVoice":"female",
 "taps":[{"phrase":"to look at the camera","target":"the dog","voice":"female","keys":k},
  {"phrase":"to turn its head","target":"the dog","voice":"female","keys":k},
  {"phrase":"to have long ears","target":"the dog","voice":"female","keys":k}],
 "stillS":0.5,
 "nouns":[{"word":"a dog","x":.50,"y":.40,"voice":"female"},{"word":"the sky","x":.55,"y":.08,"voice":"female"},
  {"word":"a house","x":.15,"y":.59,"voice":"female"}],
 "question":"What is the dog doing?",
 "answer":["The","dog","is","looking","at","the","camera."],"answerVoice":"female",
 "notes":"Only the dog can be a target: of the person only the two arms are visible, left and right of the dog, so no box for them (the arms lie partly inside the dog's box). From 4.0 (cut) the dog is very close and seen from below/behind, no face visible; the description's 'sniffs the lens' cannot be read from the picture, so no 'smell' phrase. 'to turn its head' is at about 2.0. Third phrase is a state. Only 3 nouns: everything else comes in pairs (ears, paws, arms) or is on the dog."})
