import json
W=[(0,.50,.05,.50,.72),(.5,.50,.05,.50,.72),(1,.49,0,.51,.88),(1.5,.50,0,.50,.90),(2,.55,0,.45,.72),(2.5,.55,0,.45,.72),
(3,.55,.05,.45,.72),(3.5,.56,0,.44,.75),(4,.55,0,.45,.72),(4.5,0,.03,1,.70),(5,0,.03,1,.70),(5.5,0,.03,1,.70),(6,0,.03,1,.70),
(6.5,.41,.02,.59,.74),(7,.45,.10,.55,.76),(7.5,.62,.13,.38,.74),(8,.68,.10,.32,.72),(8.5,.72,.10,.28,.68),(9,.70,.12,.30,.75),
(9.5,.68,.13,.32,.75),(10,.68,.13,.32,.65)]
B={0:(.05,.28,.44,.66),.5:(.05,.28,.44,.66),1:(.03,.38,.45,.62),1.5:(.02,.37,.47,.63),2:(0,.17,.54,.40),2.5:(0,.17,.54,.42),
3:(0,.17,.54,.44),3.5:(0,.10,.55,.44),4:(0,.12,.54,.40),6.5:(0,.22,.40,.36),7:(0,.18,.43,.45)}
k=lambda t,b:{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
wk=[k(float(r[0]),r[1:]) for r in W]
bk=[k(float(r[0]),B[r[0]]) if r[0] in B else {"t":float(r[0]),"off":True} for r in W]
d={"mediaId":698,"level":"A","keyWord":"smoothie","defaultVoice":"female","taps":[
{"phrase":"to pour a smoothie","target":"the woman in orange","voice":"female","keys":wk},
{"phrase":"to add more fruit","target":"the woman in orange","voice":"female","keys":wk},
{"phrase":"to mix the fruit","target":"the blender","voice":"female","keys":bk}],
"stillS":5.5,"nouns":[{"word":"a smoothie","x":.48,"y":.75,"voice":"female"},{"word":"bananas","x":.17,"y":.86,"voice":"female"},
{"word":"strawberries","x":.78,"y":.93,"voice":"female"},{"word":"a woman","x":.60,"y":.25,"voice":"female"}],
"question":"What is the woman in orange doing?","answer":["She","is","pouring","a","smoothie","into","a","glass."],"answerVoice":"female",
"notes":"Blender and woman overlap (her hands are on the lid / handle); boxes are split along the line between the jug and her body. 'to mix the fruit' for the blender: the mixing is only seen at 0-0.5 s (fruit pieces turn into liquid). Friends appear from 7.5 s and also drink, so no drinking phrase was used. The question matches the pouring at 2-4 s and 6.5-7 s."}
json.dump(d,open("content/698.json","w"),indent=1,ensure_ascii=False)
