import json
def k(L): return [{"t":t,"x":x,"y":y,"w":w,"h":h} for t,x,y,w,h in L]
boy=k([(0.0,.50,.07,.50,.63),(0.5,.42,.05,.58,.60),(1.0,.49,.10,.51,.52),(1.5,.52,.16,.48,.62),(2.0,.45,.10,.55,.60),
(2.5,.48,.10,.52,.56),(3.0,.50,.18,.50,.67),(3.5,0,.02,.52,.44),(4.0,0,.08,.57,.35),(4.5,0,.03,.50,.42),
(5.0,0,0,.50,.45),(5.5,0,.05,.57,.40),(6.0,0,.01,.50,.44),(6.5,0,.01,.50,.44),(7.0,0,.11,.57,.34),
(7.5,0,.11,.50,.34),(8.0,0,.08,.52,.37),(8.5,0,.08,.54,.37),(9.0,.42,.39,.40,.30),(9.5,.34,.34,.66,.37),
(10.0,.31,.44,.55,.26),(10.5,.33,.44,.50,.26),(11.0,.33,.43,.50,.27),(11.5,.31,.43,.52,.26),(12.0,.31,.42,.52,.27)])
dog=k([(0.0,.05,.26,.43,.47),(0.5,.05,.30,.36,.40),(1.0,.03,.37,.44,.44),(1.5,.10,.37,.40,.42),(2.0,.03,.38,.41,.42),
(2.5,.02,.39,.44,.42),(3.0,.02,.39,.45,.53),(3.5,.33,.47,.22,.14),(4.0,.33,.44,.25,.15),(4.5,.37,.46,.22,.14),
(5.0,.37,.46,.22,.14),(5.5,.34,.46,.24,.14),(6.0,.34,.46,.23,.14),(6.5,.37,.46,.22,.14),(7.0,.33,.46,.25,.14),
(7.5,.37,.46,.22,.14),(8.0,.34,.46,.24,.14),(8.5,.33,.46,.24,.14),(9.0,.08,.48,.26,.25),(9.5,.08,.50,.25,.25),
(10.0,.07,.50,.23,.26),(10.5,.07,.50,.25,.26),(11.0,.07,.50,.25,.26),(11.5,.07,.50,.23,.26),(12.0,.07,.49,.23,.26)])
d={"mediaId":4642,"level":"B","keyWord":"pit","defaultVoice":"male",
"taps":[
 {"phrase":"to shovel out the sand","target":"the boy","voice":"male","keys":boy},
 {"phrase":"to stick out its tongue","target":"the dog","voice":"male","keys":dog},
 {"phrase":"to toss sand into the air","target":"the boy","voice":"male","keys":boy}],
"stillS":6.5,
"nouns":[{"word":"a pit","x":.52,"y":.77,"voice":"male"},
 {"word":"a spade","x":.50,"y":.61,"voice":"male"},
 {"word":"a mound","x":.78,"y":.50,"voice":"male"},
 {"word":"the sky","x":.70,"y":.20,"voice":"male"}],
"question":"What is the boy digging?",
"answer":["He","is","digging","a","deep","pit."],
"answerVoice":"male",
"notes":"Three shots: from above (0-3.0 s), low angle with the spade (3.5-8.5 s), wide final shot (9.0-12.0 s). In the low-angle shot the dog is small behind the boy's hand and the spade; its box is the minimum size and the boy's box is cut at y 0.45 there, so his knees, lower arm and the spade are outside his box. The dog's tongue is only visible in the final shot (9.0-12.0 s). The boy tosses sand up at 9.5 s (flying sand also at 1.5 and 3.0 s). 'a spade' pill sits on the blade, 'a mound' on the heap to the right, 'a pit' in the hole."}
json.dump(d,open("content/4642.json","w"),indent=1,ensure_ascii=False)
