import json
B=[(0,.03,.96,.97)]*3+[(0,.03,1,.97),(0,0,1,1),(0,0,1,1),(0,0,1,1),(0,.02,1,.98),(0,.03,1,.97),(0,.03,.94,.97),(0,.03,.98,.97),(.08,.05,.92,.95),(.06,.05,.84,.95),(0,.04,1,.96),(0,.04,1,.96),(0,.07,1,.93),(.06,.07,.94,.93),(0,.07,1,.93),(.03,.07,.95,.93),(0,.08,1,.92),(0,.07,1,.93)]
keys=[{"t":i*0.5,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for i,b in enumerate(B)]
c={"mediaId":4272,"level":"A","keyWord":"gold","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to put on gold earrings","to wear a big hat","to carry two bags"]],
"stillS":8.0,
"nouns":[{"word":"a hat","x":.50,"y":.15,"voice":"female"},{"word":"a scarf","x":.50,"y":.37,"voice":"female"},{"word":"a belt","x":.50,"y":.67,"voice":"female"},{"word":"trousers","x":.52,"y":.88,"voice":"female"}],
"question":"What is the woman wearing?","answer":["She","is","wearing","a","big","hat."],"answerVoice":"female",
"notes":"Only one target (the woman), used for all three phrases; she fills the frame. Key word 'gold' is an adjective, used in phrase 1. Question is open (she wears many things); model answer names the hat."}
json.dump(c,open('content/4272.json','w'),indent=1)
