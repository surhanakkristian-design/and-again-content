import json
T=[i*0.5 for i in range(21)]
C=[(.07,.07,.93,.93),(.04,.07,.96,.93),(.29,.07,.71,.93),(.23,.07,.77,.93),(.21,.07,.79,.93),(.21,.08,.79,.92),(.21,.1,.79,.9),(.46,.2,.54,.8),(.53,.26,.47,.74),(.48,.26,.52,.74),(.33,.24,.67,.76),(.22,.2,.78,.8),(.34,.2,.66,.8),(.47,.18,.53,.82),(.54,.26,.46,.74),(.64,.26,.36,.74),(.76,.3,.24,.7),(.57,.24,.43,.76),(.47,.2,.53,.8),(.43,.2,.57,.8),(.41,.22,.52,.78)]
S=[None]*11+[(0,.25,.21,.75),(0,.23,.33,.77),(0,.24,.43,.76),(0,.26,.42,.74),(0,.26,.5,.74),(0,.27,.5,.73),(0,.26,.5,.74),(0,.26,.46,.74),(0,.25,.42,.75),(0,.25,.4,.75)]
k=lambda L:[{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,L)]
d={"mediaId":546,"level":"A","keyWord":"perfume","defaultVoice":"female",
"taps":[{"phrase":"to put on perfume","target":"the woman in blue","voice":"female","keys":k(C)},
{"phrase":"to smell her wrist","target":"the woman in blue","voice":"female","keys":k(C)},
{"phrase":"to wear a yellow scarf","target":"the woman in the scarf","voice":"female","keys":k(S)}],
"stillS":0.5,
"nouns":[{"word":"a tree","x":.45,"y":.1,"voice":"female"},{"word":"a woman","x":.82,"y":.32,"voice":"female"},{"word":"perfume","x":.43,"y":.53,"voice":"female"},{"word":"a table","x":.3,"y":.79,"voice":"female"}],
"question":"What is the woman in blue doing?","answer":["She","is","putting","perfume","on","her","wrist."],"answerVoice":"female",
"notes":"Two women: 'the woman in blue' (blue-green shirt, curly hair, alone 0-5 s) and 'the woman in the scarf' (comes in at 5.5 s; a thin strip of her at 5.0 s is left off). The woman in the scarf has only a state phrase: both women hold the bottle and both wave their hands, so no simple action fits only her. From 6.5 s it is the woman in the scarf who holds the bottle and sprays; 'to put on perfume' still fits only the woman in blue (on her own wrist, 0-0.5 s). Boxes split along the line between the women where their hands meet (5.5, 6.0, 9.0-10.0 s). 'wrist' may be a little above A1. 'perfume' labels the small bottle. Shirt colour is blue-green: check 'in blue' is clear enough."}
json.dump(d,open("content/546.json","w"),indent=1,ensure_ascii=False)
