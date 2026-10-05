import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
def K(b): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in zip(T,b)]
woman=[(.06,.40,.42,.38),(.10,.39,.40,.41),(.08,.39,.42,.48),(.07,.37,.46,.54),(.00,.35,.50,.62),(.00,.35,.48,.63),(.00,.34,.45,.66)]
man=[(.58,.42,.25,.36),(.52,.35,.31,.47),(.54,.34,.32,.53),(.56,.33,.30,.58),(.50,.33,.34,.64),(.48,.31,.38,.69),(.45,.31,.43,.69)]
guide=[(.84,.39,.16,.30),(.84,.38,.16,.33),(.87,.38,.13,.26),(.87,.40,.13,.24),(.85,.38,.15,.30),(.86,.38,.14,.28),(.88,.38,.12,.30)]
c={"mediaId":7021,"level":"A","keyWord":"date","defaultVoice":"female",
"taps":[
 {"phrase":"to give him a sunflower","target":"the woman in red","voice":"female","keys":K(woman)},
 {"phrase":"to take the sunflower","target":"the man in beige trousers","voice":"male","keys":K(man)},
 {"phrase":"to hold a rope","target":"the woman in black","voice":"female","keys":K(guide)}],
"stillS":2.2,
"nouns":[{"word":"birds","x":0.62,"y":0.26,"voice":"female"},{"word":"a sunflower","x":0.51,"y":0.48,"voice":"female"},
 {"word":"a table","x":0.40,"y":0.74,"voice":"female"},{"word":"a helmet","x":0.12,"y":0.40,"voice":"female"}],
"question":"What is the woman in red doing?",
"answer":["She","is","giving","him","a","sunflower."],
"answerVoice":"female",
"notes":"Man takes the sunflower only from about 2.2 s; before that he stands up and laughs. Woman and man boxes split at their meeting hands (x about .45-.50). Guide in black is only partly visible at the right edge at 1.2-1.7 s. Key word 'date' is abstract, not placed; 'birds' = the two toucans on the line."}
json.dump(c,open('content/7021.json','w'),indent=1)
