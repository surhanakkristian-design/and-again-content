import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
man=[(.32,.28,.27,.59),(.32,.29,.27,.59),(.32,.31,.27,.59),(.33,.33,.29,.59),(.31,.38,.30,.58),(.31,.39,.30,.59),(.31,.46,.30,.54),(.31,.45,.31,.55)]
clm=[(.59,.27,.39,.47),(.59,.28,.40,.47),(.59,.30,.40,.47),(.62,.31,.38,.39),(.61,.21,.39,.50),(.61,.22,.39,.50),(.61,.24,.39,.50),(.62,.24,.38,.50)]
red=[(.14,.57,.18,.22),(.14,.58,.18,.21),(.12,.61,.20,.19),(.08,.59,.25,.23),(.07,.62,.24,.22),(.08,.63,.23,.22),(.08,.64,.23,.22),(.03,.68,.28,.20)]
d={"mediaId":5533,"level":"A","keyWord":"advise","defaultVoice":"male",
"taps":[{"phrase":"to point up at the wall","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to climb the wall","target":"the woman on the wall","voice":"female","keys":K(clm)},
{"phrase":"to raise both arms","target":"the woman in the red top","voice":"female","keys":K(red)}],
"stillS":3.7,
"nouns":[{"word":"a wall","x":0.86,"y":0.76,"voice":"male"},
{"word":"a window","x":0.55,"y":0.40,"voice":"male"},
{"word":"a man","x":0.40,"y":0.62,"voice":"male"},
{"word":"mats","x":0.55,"y":0.92,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","pointing","up","at","the","wall."],
"answerVoice":"male",
"notes":"Man's pointing hand nearly touches the climber's head (0.2-2.7); boxes split at x~0.59-0.62, so the tip of his arm falls in the climber's box. Red-top woman drinks at 0.2-1.2 and raises both arms from 1.7 on; the climber only ever has one arm up. Man claps at 3.7 (pointing 0.2-2.7)."}
json.dump(d,open("content/5533.json","w"),indent=1)
