import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
WO={0.2:(.10,.27,.46,.63),0.7:(.16,.27,.39,.66),1.2:(.16,.25,.38,.73),1.7:(.16,.25,.39,.75),2.2:(.14,.24,.40,.76),2.7:(.12,.22,.43,.78),3.2:(.07,.21,.45,.79),3.7:(.04,.20,.46,.80)}
MA={0.2:(.56,.28,.34,.62),0.7:(.55,.28,.36,.64),1.2:(.54,.27,.37,.70),1.7:(.55,.27,.40,.72),2.2:(.54,.26,.42,.74),2.7:(.55,.24,.45,.76),3.2:(.52,.23,.48,.77),3.7:(.50,.22,.50,.78)}
k=lambda t,v:{"t":t,"x":v[0],"y":v[1],"w":v[2],"h":round(min(v[3],1-v[1]),2)}
wk=[k(t,WO[t]) for t in T]
c={"mediaId":5679,"level":"B","keyWord":"break the news","defaultVoice":"female",
 "taps":[{"phrase":"to touch his arm gently","target":"the woman","voice":"female","keys":wk},
  {"phrase":"to grip an empty crate","target":"the man","voice":"male","keys":[k(t,MA[t]) for t in T]},
  {"phrase":"to show him a document","target":"the woman","voice":"female","keys":wk}],
 "stillS":0.2,
 "nouns":[{"word":"a street lamp","x":0.16,"y":0.15,"voice":"female"},{"word":"the sky","x":0.66,"y":0.12,"voice":"female"},
  {"word":"a shed","x":0.89,"y":0.37,"voice":"female"},{"word":"a wooden crate","x":0.70,"y":0.76,"voice":"female"}],
 "question":"What is the man holding?",
 "answer":["He","is","holding","an","empty","wooden","crate."],"answerVoice":"male",
 "notes":"Woman and man stand close; boxes split at x ~.50-.56, so her hand on his arm (x ~.58-.65) and the paper (to ~.66) fall partly in the man's box. She lifts the paper to show it from 1.2; at 0.2-0.7 it is low by her hip. 'document' = the white sheet of paper (content not readable). A background worker on the right also holds a paper, so the phrase is 'show him', not 'hold'. defaultVoice female: woman leads the scene."}
json.dump(c,open('content/5679.json','w'),indent=1)
