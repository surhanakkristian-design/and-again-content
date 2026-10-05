import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]
def b(t,x0,y0,x1,y1): return {"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
man={0.0:(.02,.27,.98,.62),0.5:(.02,.27,.98,.62),1.0:(.02,.27,.98,.62),1.5:(.02,.27,.98,.62),2.0:(.02,.25,.98,.62),2.5:(.02,.25,.98,.62),
3.0:(.02,.27,.98,.62),3.5:(.02,.27,.58,.82),4.0:(.02,.27,.52,.82),4.5:(.02,.27,.98,.47),5.0:(.02,.27,.54,.82)}
mug={3.5:(.59,.43,.79,.58),4.0:(.53,.38,.76,.54),4.5:(.58,.48,.78,.62),5.0:(.55,.50,.79,.66)}
mk=[b(t,*man[t]) for t in T]
gk=[b(t,*mug.get(t,(.61,.63,.87,.80))) for t in T]
pk=[b(t,*((.31,.10,.53,.24) if t in (2.0,2.5) else (.31,.13,.53,.27))) for t in T]
c={"mediaId":33,"level":"B","keyWord":"ache","defaultVoice":"male",
"taps":[{"phrase":"to clutch a swollen cheek","target":"the man","voice":"male","keys":mk},
{"phrase":"to give off steam","target":"the mug","voice":"male","keys":gk},
{"phrase":"to grow in a clay pot","target":"the plant","voice":"male","keys":pk}],
"stillS":0.0,
"nouns":[{"word":"a potted plant","x":.42,"y":.20,"voice":"male"},{"word":"a moustache","x":.55,"y":.41,"voice":"male"},
{"word":"an ice pack","x":.78,"y":.56,"voice":"male"},{"word":"a mug","x":.73,"y":.73,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","clutching","his","swollen","cheek","in","pain."],
"answerVoice":"male",
"notes":"Mug sits in front of / is held by the man: man box is cut (top part or left part) where the mug is lifted to his face (3.5-5.0). Key word 'ache' is not a visible noun; answer uses 'in pain'."}
json.dump(c,open('content/33.json','w'),indent=1,ensure_ascii=False)
