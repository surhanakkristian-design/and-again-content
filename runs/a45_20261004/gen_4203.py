import json
T=[i*0.5 for i in range(24)]
shark=[[.16,.39,.47,.27],[.18,.38,.44,.27],[.13,.38,.39,.27],[.13,.40,.37,.24],[.14,.39,.32,.24],[.18,.39,.36,.24],[.18,.40,.32,.25],[.20,.39,.33,.26],
[.28,.38,.25,.22],[.21,.39,.34,.24],[.21,.39,.32,.23],[.21,.39,.32,.23],[.16,.38,.46,.23],[.14,.37,.46,.24],[.16,.37,.51,.26],[.21,.37,.56,.27],
[.21,.36,.59,.29],[.22,.35,.60,.31],[.18,.34,.54,.30],[.22,.30,.38,.26],[.08,.31,.50,.22],[.14,.33,.42,.23],[.16,.37,.48,.19],[.20,.37,.31,.19]]
man=[[.63,.04,.37,.77],[.62,.07,.38,.71],[.52,.08,.43,.66],[.50,.09,.38,.67],[.46,.09,.40,.66],[.54,.10,.41,.67],[.50,.13,.40,.62],[.53,.13,.37,.63],
[.53,.11,.40,.62],[.55,.10,.38,.60],[.53,.09,.43,.60],[.53,.07,.45,.63],[.62,.07,.38,.66],[.60,.07,.40,.64],[.67,.11,.33,.62],[.77,.10,.23,.67],
[.80,.08,.20,.72],[.82,.08,.18,.72],[.72,.12,.28,.68],[.68,.09,.32,.72],[.74,.03,.26,.87],[.80,.03,.20,.87],[.67,.09,.33,.80],[.59,.15,.41,.75]]
def keys(b): return [{"t":t,"x":x,"y":y,"w":w,"h":h} for t,(x,y,w,h) in zip(T,b)]
d={"mediaId":4203,"level":"B","keyWord":"rescue","defaultVoice":"male",
"taps":[
 {"phrase":"to rescue a stranded shark","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to swim out to sea","target":"the shark","voice":"male","keys":keys(shark)},
 {"phrase":"to grip a shark's tail","target":"the man","voice":"male","keys":keys(man)}],
"stillS":2.0,
"nouns":[{"word":"a shark","x":.36,"y":.54,"voice":"male"},{"word":"swimming trunks","x":.68,"y":.46,"voice":"male"},
 {"word":"sand","x":.50,"y":.85,"voice":"male"},{"word":"the sea","x":.30,"y":.17,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","rescuing","a","stranded","shark."],
"answerVoice":"male",
"notes":"Man and shark overlap where he holds the tail: boxes split on a vertical line at his front leg, so the tail end of the shark and sometimes his front foot fall outside their box. Shark swims off only from 9.5 s. 'swimming trunks' pill sits on the neon shorts, not on the man as a whole."}
json.dump(d,open("content/4203.json","w"),indent=1,ensure_ascii=False)
