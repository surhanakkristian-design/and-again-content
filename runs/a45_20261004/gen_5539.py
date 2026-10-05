import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(L): return [{"t":t,"off":True} if b is None else {"t":t,"x":round(b[0],2),"y":round(b[1],2),"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,L)]
SA=[(.31,.33,.50,.47),(.36,.37,.58,.60),(.37,.37,.64,.61),(.42,.37,.71,.61),(.44,.37,.76,.63),(.45,.38,.73,.64),(.43,.39,.74,.66),(.35,.38,.71,.66)]
BU=[(.08,.47,.48,.80),(.01,.44,.36,.77),(0,.45,.30,.76),(0,.45,.23,.76),(.01,.46,.36,.75),(.10,.47,.40,.75),(.21,.48,.43,.75),(.22,.48,.35,.73)]
HU=[(.48,.57,.88,.81),(.36,.60,.98,.82),(.40,.61,1.0,.85),(.45,.61,1.0,.86),(.44,.63,1.0,.92),(.41,.65,1.0,.96),(.43,.66,1.0,.97),(.35,.66,1.0,.98)]
c={"mediaId":5539,"level":"B","keyWord":"ahead","defaultVoice":"male",
"taps":[
{"phrase":"to glance over his shoulder","target":"the sailor","voice":"male","keys":K(SA)},
{"phrase":"to throw up white spray","target":"the leading boat","voice":"male","keys":K(HU)},
{"phrase":"to mark the turning point","target":"the orange buoy","voice":"male","keys":K(BU)}],
"stillS":2.2,
"nouns":[{"word":"a sailor","x":.60,"y":.52,"voice":"male"},
{"word":"a buoy","x":.18,"y":.62,"voice":"male"},
{"word":"a sail","x":.86,"y":.42,"voice":"male"},
{"word":"the sky","x":.30,"y":.12,"voice":"male"}],
"question":"What is the sailor doing?",
"answer":["He","is","racing","ahead","of","the","other","boats."],
"answerVoice":"male",
"notes":"'the leading boat' box covers only the hull below the sailor's waist (split from the sailor box); the blue sail above belongs to it too but overlaps the sailor and the boats behind, so it is left out. The crew member in the cap is mostly hidden behind the sailor and is not a target. 'to mark the turning point' relies on the race context (the boat rounds the buoy). 'a sailor': small sailors in the boats behind are visible at 2.2 s, but the pill sits on the main man."}
json.dump(c,open("content/5539.json","w"),indent=1,ensure_ascii=False)
