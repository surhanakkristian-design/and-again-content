import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
man={2.0:(0,.08,.75,.92),2.5:(0,.24,.66,.76),3.0:(0,.27,1,.73),3.5:(0,.23,.78,.77),4.0:(0,.30,1,.70),4.5:(0,.27,1,.73),5.0:(.02,.33,.95,.67),5.5:(0,.34,.38,.26),7.0:(.33,.34,.20,.14)}
por={7.5:(.05,.18,.87,.82),8.0:(.17,.19,.80,.81),8.5:(.19,.17,.75,.83),9.0:(.22,.24,.68,.76),9.5:(.22,.24,.68,.76),10.0:(.15,.15,.78,.85),10.5:(.12,.17,.82,.83),11.0:(.09,.17,.79,.83),11.5:(.09,.15,.76,.85),12.0:(.10,.15,.80,.85)}
mk=keys(man); pk=keys(por)
d={"mediaId":4468,"level":"B","keyWord":"porter","defaultVoice":"male",
"taps":[
{"phrase":"to grab a paper bag","target":"the man in the bright shirt","voice":"male","keys":mk},
{"phrase":"to hand over some banknotes","target":"the man in the bright shirt","voice":"male","keys":mk},
{"phrase":"to balance a silver teapot","target":"the porter","voice":"male","keys":pk}],
"stillS":12.0,
"nouns":[{"word":"a teapot","x":.56,"y":.22,"voice":"male"},{"word":"a cushion","x":.40,"y":.45,"voice":"male"},{"word":"a rug","x":.50,"y":.57,"voice":"male"},{"word":"a porter","x":.50,"y":.92,"voice":"male"}],
"question":"What is the porter doing?",
"answer":["He","is","carrying","a","towering","pile","of","rugs."],
"answerVoice":"male",
"notes":"Two targets whose boxes never coexist: the bald man in the bright shirt (2.0-5.5 s, head only at 7.0 s) and the porter (pile with legs in sandals seen from behind, 7.5-12 s). 0-1.5 s show only hands (off for both). 6.0/6.5 show only the pile, carrier not identifiable (off for both). Doubt: at 5.5-7 s the bright-shirt man seems to hold the pile himself, so the porter phrase is about the teapot (on the load from 10 s), not about carrying. From 7.5 s an arm reaches in from behind the load (banknotes at 7.5/8.0, hand on the teapot 10-11 s) and a bald head shows at its right edge at 11.5 s: probably the bright-shirt man walking beside the porter; it lies inside the porter box and the man is set off there. He takes the bag by its handles at 2.0-2.5 s and holds banknotes out at 3.5-4.5 s. The pill of the key word a porter sits on his legs, the only visible part of him. a cushion = the red one; a rug = the rolled rug."}
json.dump(d,open("content/4468.json","w"),indent=1,ensure_ascii=False)
