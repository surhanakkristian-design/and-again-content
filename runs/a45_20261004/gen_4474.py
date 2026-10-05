import json
T=[i*0.5 for i in range(21)]
W=[(0,.11,1,.68),(0,.13,1,.67),(.03,.13,.92,.72),(0,.13,.95,.69),(.05,.14,.87,.66),(.46,.05,.54,.93),(.38,.08,.62,.92),(.42,.08,.58,.92),(.62,.08,.38,.92),(.05,.08,.95,.90),(0,.09,1,.90),(0,0,1,.55),(0,0,1,.66),(.05,.12,.95,.60),(0,.17,.97,.68),(0,.17,.97,.68),(0,.16,1,.61),(0,.16,1,.61),(0,.17,1,.72),(0,.17,1,.75),(0,.16,1,.60)]
M={0:(0,0,1,.11),.5:(0,0,1,.13),1:(0,0,1,.13),1.5:(0,0,1,.13),2:(0,0,1,.14)}
J={2.5:(0,0,.46,.58),3:(0,0,.38,.70),3.5:(0,0,.42,.68),4:(0,0,.62,.57)}
def k(t,b): return {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True}
d={"mediaId":4474,"level":"A","keyWord":"menu","defaultVoice":"female",
"taps":[
{"phrase":"to eat chocolate cake","target":"the woman","voice":"female","keys":[k(t,b) for t,b in zip(T,W)]},
{"phrase":"to pour milk into a cup","target":"the jug","voice":"female","keys":[k(t,J.get(t)) for t in T]},
{"phrase":"to show the prices","target":"the menu","voice":"female","keys":[k(t,M.get(t)) for t in T]}],
"stillS":2.0,
"nouns":[{"word":"a menu","x":.28,"y":.09,"voice":"female"},{"word":"a coffee machine","x":.20,"y":.37,"voice":"female"},{"word":"a woman","x":.58,"y":.55,"voice":"female"},{"word":"a spoon","x":.40,"y":.86,"voice":"female"}],
"question":"What is the woman eating?",
"answer":["She","is","eating","a","piece","of","chocolate","cake."],
"answerVoice":"female",
"notes":"Three shots: counter with the menu boards (0-2 s), milk poured into her cup (2.5-4 s, the jug and a hand come in from the left), grand cafe with cake (5.5-10 s). The menu boards sit behind her head, so the menu box is only the strip above her hair and the woman's box starts at the top of her hair. In the pouring shot the jug hides the left half of her: the split is vertical along the jug's right edge, so her left arm falls outside her box there (at 4.0 her box is only the right 38 % with her visible eye and right hand). She eats the cake only from 8.0 s."}
json.dump(d,open("content/4474.json","w"),indent=1,ensure_ascii=False)
