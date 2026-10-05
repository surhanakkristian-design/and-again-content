import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
father={0.0:(0,.08,.66,.92),0.5:(0,.06,.86,.94),1.0:(0,0,.52,1.0),2.5:(0,.66,1,.32),3.0:(0,.26,1,.72),3.5:(0,.28,1,.70),
        4.0:(0,.29,1,.69),4.5:(0,.27,1,.71),5.0:(0,.25,.30,.40),5.5:(0,.31,.34,.35),6.0:(.02,.33,.35,.37),6.5:(.17,.54,.26,.28),
        7.0:(.32,.77,.20,.15),7.5:(.38,.77,.18,.14)}
child={0.0:(.66,.33,.34,.67),0.5:(.86,.55,.14,.45),1.0:(.55,.35,.45,.65),1.5:(.05,.36,.95,.64),2.0:(.18,.35,.72,.65)}
baby={2.5:(.10,0,.80,.66),3.0:(.24,0,.56,.26),3.5:(.20,.12,.62,.16),4.0:(.27,.09,.50,.20),4.5:(.28,.05,.52,.22)}
c={"mediaId":4727,"level":"A","keyWord":"father","defaultVoice":"male",
 "taps":[
  {"phrase":"to lift the baby up","target":"the father","voice":"male","keys":keys(father)},
  {"phrase":"to ride a blue bike","target":"the child on the bike","voice":"male","keys":keys(child)},
  {"phrase":"to sit on his shoulders","target":"the baby","voice":"male","keys":keys(baby)}],
 "stillS":5.0,
 "nouns":[{"word":"a father","x":.12,"y":.43,"voice":"male"},{"word":"a ball","x":.50,"y":.28,"voice":"male"},
          {"word":"a boy","x":.88,"y":.52,"voice":"male"},{"word":"grass","x":.40,"y":.80,"voice":"male"}],
 "question":"Who is sitting on the father's shoulders?",
 "answer":["The","baby","is","sitting","on","his","shoulders."],
 "answerVoice":"male",
 "notes":"Three targets in different shots. The baby sits on the father, so their boxes are split: at 2.5 s (baby held in front of him) the father box is only his legs below y .66 and the baby's lower legs fall into it; from 3.0 s the split runs at the top of the father's hair, the baby's legs beside his head are in the father box. The older boy of the ball game (5.0-7.5 s) is not a target. From 8.0 s the father is a dot in the aerial shot: off. The child on the bike is seen from behind, gender unclear, so the default voice. 'a father' is placed as the key word on the man at 5.0 s."}
json.dump(c,open('content/4727.json','w'),indent=1,ensure_ascii=False)
