import json
def keys(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
woman=[(0.0,.36,.27,.60,.73),(0.5,.36,.27,.60,.73),(1.0,.34,.27,.58,.73),(1.5,.60,.11,.40,.56),
(2.0,.58,.08,.42,.56),(2.5,.58,.09,.42,.55),(3.0,.57,.09,.43,.55),(3.5,.57,.09,.43,.55),
(4.0,.64,.37,.36,.63),(4.5,.62,.37,.38,.63),(5.0,.62,.37,.38,.63),(5.5,.62,.37,.38,.63),(6.0,.63,.37,.37,.63),
(6.5,None),(7.0,.62,.37,.38,.63),(7.5,.62,.37,.38,.63),(8.0,.62,.38,.38,.62),(8.5,.58,.38,.42,.62),(9.0,.38,.40,.62,.60)]
off=[(0.0,None),(0.5,None),(1.0,None),(1.5,0,0,.58,.58),(2.0,0,0,.54,.72),(2.5,0,0,.54,.27),(3.0,0,0,.54,.26),(3.5,0,0,.48,.26),
(4.0,0,.03,.55,.80),(4.5,0,.03,.37,.77),(5.0,0,.03,.36,.77),(5.5,0,.03,.37,.77),(6.0,0,.02,.35,.78),(6.5,None),
(7.0,0,.04,.36,.76),(7.5,0,.04,.37,.76),(8.0,0,.04,.36,.76),(8.5,0,.04,.37,.76),(9.0,0,.04,.35,.76)]
d={"mediaId":5299,"level":"A","keyWord":"illegal","defaultVoice":"female",
"taps":[{"phrase":"to hold a jar of pickles","target":"the old woman","voice":"female","keys":keys(woman)},
{"phrase":"to open the suitcase","target":"the bald officer","voice":"male","keys":keys(off)},
{"phrase":"to smile at the officer","target":"the old woman","voice":"female","keys":keys(woman)}],
"stillS":5.0,
"nouns":[{"word":"sausages","x":0.40,"y":0.53,"voice":"female"},{"word":"a suitcase","x":0.35,"y":0.67,"voice":"female"},
{"word":"a jar","x":0.76,"y":0.71,"voice":"female"},{"word":"a headscarf","x":0.85,"y":0.46,"voice":"female"}],
"question":"What is the old woman holding?","answer":["She","is","holding","a","jar","of","pickles."],"answerVoice":"female",
"notes":"Officer opens the case 1.5-3.5 (only arm/hand visible) and holds it open from 4.0; a second officer stands in the back (not a target). t=6.5 is the scanner monitor cut, all off. Woman holds sausages 0-1.0 and the jar 4.0-9.0."}
json.dump(d,open("content/5299.json","w"),indent=1)
