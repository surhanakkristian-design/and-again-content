import json
T=[i*0.5 for i in range(19)]
W={0:(.13,.21,.85,.73),.5:(.06,.22,.92,.72),1:(.05,.23,.85,.72),1.5:(.14,.23,.82,.72),2:(.05,.22,.90,.73),2.5:(.03,.21,.94,.73),3:(0,.21,.97,.77),
3.5:(.28,.05,.72,.95),4:(.31,.05,.69,.95),4.5:(.36,.05,.64,.95),5:(.20,.05,.80,.95),5.5:(.39,.05,.61,.95),
7.5:(.78,.24,.22,.64),8:(.68,.21,.32,.63),8.5:(.43,.20,.57,.56),9:(.36,.21,.64,.74)}
J={3.5:(0,.20,.27,.45),4:(0,.20,.30,.42),4.5:(0,.20,.35,.42),5:(0,.30,.19,.44),5.5:(0,.20,.38,.50)}
def k(t,b): return {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True}
wk=[k(t,W.get(t)) for t in T]
d={"mediaId":4476,"level":"A","keyWord":"hall","defaultVoice":"female",
"taps":[
{"phrase":"to drink a small coffee","target":"the woman","voice":"female","keys":wk},
{"phrase":"to pour milk into a cup","target":"the jug","voice":"female","keys":[k(t,J.get(t)) for t in T]},
{"phrase":"to point at a cake","target":"the woman","voice":"female","keys":wk}],
"stillS":9.0,
"nouns":[{"word":"a cake","x":.22,"y":.49,"voice":"female"},{"word":"a woman","x":.82,"y":.56,"voice":"female"},{"word":"a cup","x":.60,"y":.73,"voice":"female"},{"word":"a table","x":.40,"y":.91,"voice":"female"}],
"question":"Where is the woman sitting?",
"answer":["She","is","sitting","in","a","big","hall."],
"answerVoice":"female",
"notes":"Three shots: coffee bar (0-3 s), milk poured into her cup (3.5-5.5 s, jug and hand from the left), big cafe hall (6-9 s; she is in the picture only from 7.5 s). Only two usable targets: the guests and the waiter in the hall are tiny and short, so two phrases share the woman. In the pouring shot the split is vertical at the jug's right edge, so her fingertips under the cup fall outside her box. Key word 'hall' is the whole room and has no single place for a pill, so it is in the answer, not in the nouns; 'at a table' would also be a true answer to the question. 'a table' = the marble table in front (other tables are small in the background)."}
json.dump(d,open("content/4476.json","w"),indent=1,ensure_ascii=False)
