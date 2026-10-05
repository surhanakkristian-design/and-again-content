import json
def B(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
times=[i*0.5 for i in range(21)]
G=[B(0,.05,.42,.55),B(0,.06,.42,.54),B(0,.05,.42,.57),B(0,.04,.42,.54),B(0,.02,.45,.50),B(0,.02,.44,.52),B(0,.03,.44,.52),B(0,.04,.43,.54),B(0,.07,.38,.49),B(0,.06,.37,.50),B(0,.07,.36,.50),B(0,.07,.35,.50),B(0,.02,.36,.56),B(0,.03,.36,.52),B(0,.05,.34,.52),B(0,.06,.38,.50),B(0,.04,.42,.56),B(0,.07,.40,.52),B(0,.07,.42,.58),B(0,.09,.39,.57),B(0,.07,.44,.48)]
P=[B(.43,.05,.57,.57),B(.43,.06,.57,.56),B(.43,.05,.57,.68),B(.43,.03,.57,.68),B(.46,.02,.54,.60),B(.45,.03,.55,.60),B(.45,.04,.55,.66),B(.44,.03,.56,.64),B(.39,.05,.61,.60),B(.38,.04,.62,.60),B(.37,.05,.63,.60),B(.36,.05,.64,.60),B(.37,.02,.63,.62),B(.37,.01,.63,.62),B(.35,.02,.65,.62),B(.39,.04,.61,.60),B(.43,.04,.57,.56),B(.41,.06,.59,.56),B(.43,.06,.57,.62),B(.40,.06,.60,.66),B(.45,.04,.55,.58)]
def K(l): return [dict(t=t,**k) for t,k in zip(times,l)]
d={"mediaId":503,"level":"A","keyWord":"notebook","defaultVoice":"female",
"taps":[
 {"phrase":"to write in a notebook","target":"the woman in purple","voice":"female","keys":K(P)},
 {"phrase":"to clap her hands","target":"the woman with glasses","voice":"female","keys":K(G)},
 {"phrase":"to turn the pages","target":"the woman in purple","voice":"female","keys":K(P)}],
"stillS":4.0,
"nouns":[{"word":"a notebook","x":.44,"y":.61,"voice":"female"},{"word":"a glass","x":.86,"y":.70,"voice":"female"},{"word":"pens","x":.12,"y":.76,"voice":"female"},{"word":"a table","x":.74,"y":.94,"voice":"female"}],
"question":"What is the woman in purple doing?",
"answer":["She","is","writing","in","a","new","notebook."],
"answerVoice":"female",
"notes":"Only two targets (a cat is partly visible bottom left, too hidden to use). Boxes are split by a vertical line between the two women; the writing arm of the woman in purple reaches left of her box at 4.0-7.5 and 9.0-9.5. In 0.0-1.0 a hand with a pen near the notebook is hard to assign. Clapping is visible at 7.5-9.0."}
json.dump(d,open("content/503.json","w"),indent=1)
