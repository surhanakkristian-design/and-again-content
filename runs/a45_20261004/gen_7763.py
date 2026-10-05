import json,sys
vid=7763
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
def keys(rows): return [{"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} if r else {"t":t,"off":True} for t,r in zip(T,rows)]
frog=[(.24,.31,.45,.42),(.29,.35,.43,.39),(.30,.35,.43,.40),(.27,.33,.47,.42),(.26,.29,.49,.48),(.25,.26,.51,.52),(.24,.28,.52,.54)]
teach=[(.70,.27,.19,.23),(.72,.26,.18,.24),(.73,.26,.19,.25),(.75,.24,.20,.25),(.75,.24,.20,.25),(.76,.23,.21,.25),(.76,.28,.21,.26)]
left=[(0,.41,.23,.27),(0,.41,.22,.27),(0,.37,.20,.26),(0,.38,.20,.26),(0,.39,.20,.26),(0,.39,.20,.26),(0,.40,.20,.24)]
c={"mediaId":vid,"level":"B","keyWord":"biology","defaultVoice":"female",
"taps":[{"phrase":"to hold out a frog","target":"the smiling woman","voice":"female","keys":keys(frog)},
{"phrase":"to carry a tray of seedlings","target":"the teacher","voice":"female","keys":keys(teach)},
{"phrase":"to pull a disgusted face","target":"the woman on the left","voice":"female","keys":keys(left)}],
"stillS":0.7,
"nouns":[{"word":"a frog","x":.46,"y":.58,"voice":"female"},{"word":"a microscope","x":.20,"y":.67,"voice":"female"},
{"word":"seedlings","x":.82,"y":.38,"voice":"female"},{"word":"seed pods","x":.60,"y":.92,"voice":"female"}],
"question":"What is the smiling woman holding?",
"answer":["She","is","holding","a","frog","in","her","gloved","hands."],
"answerVoice":"female",
"notes":"Key word 'biology' is abstract, not placed. The frog only appears in her hands from 0.7 s; at 0.2 s she reaches out with open hands. The woman on the left looks down at 0.2-0.7 s and pulls a disgusted face from 1.2 s on. Teacher box is split from the smiling woman's shoulder where they overlap (2.2-3.2 s)."}
json.dump(c,open(f'content/{vid}.json','w'),indent=1)
