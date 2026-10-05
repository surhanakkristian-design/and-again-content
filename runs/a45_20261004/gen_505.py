import json
O={"off":True}
def B(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
times=[i*0.5 for i in range(21)]
M=[B(0,.20,.60,.45),B(0,.18,.61,.46),B(0,.14,.63,.45),B(0,.14,.61,.43),B(0,.13,.66,.44),B(0,.05,.71,.63),B(0,0,.79,.80),B(0,0,.95,.75),B(0,0,.93,.64),B(0,0,1.0,.64),B(0,0,1.0,.70),B(0,0,.80,.63),B(0,0,.66,.59),B(0,.13,.59,.52),B(0,.18,.60,.45),B(0,.11,.44,.74),B(0,.10,.43,.64),B(0,.11,.50,.52),B(0,.20,.50,.50),B(0,.11,.50,.52),B(0,0,.48,.44)]
W=[B(.62,.25,.38,.40),B(.62,.24,.38,.40),B(.65,.18,.35,.41),B(.64,.19,.36,.38),B(.68,.19,.32,.38),B(.72,.08,.28,.52),B(.80,0,.20,.33),O,O,O,O,B(.81,0,.19,.45),B(.67,.08,.33,.51),B(.60,.22,.40,.43),B(.62,.23,.38,.40),B(.58,.20,.42,.38),B(.60,.18,.40,.41),B(.51,.15,.49,.48),B(.51,.25,.49,.45),B(.51,.18,.49,.45),B(.50,0,.50,.44)]
Bo=[B(.45,.66,.35,.14),B(.45,.65,.37,.14),B(.43,.60,.36,.14),B(.39,.58,.34,.14),B(.41,.58,.30,.14),O,O,O,O,O,O,O,B(.40,.60,.38,.14),B(.39,.66,.35,.14),B(.38,.64,.32,.14),B(.45,.59,.26,.14),B(.44,.60,.31,.14),B(.34,.64,.36,.14),B(.35,.71,.35,.14),B(.33,.64,.36,.15),B(.25,.45,.44,.14)]
def K(l): return [dict(t=t,**k) for t,k in zip(times,l)]
d={"mediaId":505,"level":"A","keyWord":"nut","defaultVoice":"male",
"taps":[
 {"phrase":"to open a nut","target":"the man","voice":"male","keys":K(M)},
 {"phrase":"to have long hair","target":"the woman","voice":"female","keys":K(W)},
 {"phrase":"to be full of nuts","target":"the bowl","voice":"male","keys":K(Bo)}],
"stillS":0.0,
"nouns":[{"word":"a man","x":.25,"y":.50,"voice":"male"},{"word":"a woman","x":.80,"y":.42,"voice":"female"},{"word":"nuts","x":.63,"y":.72,"voice":"male"},{"word":"a table","x":.50,"y":.88,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","opening","a","nut."],
"answerVoice":"male",
"notes":"Two state phrases: both people sit, laugh and eat nuts, so no action fits only the woman; the bowl is a thing. 'open a nut' chosen over 'crack' for level A. Woman is OFF at 3.5-5.0 (only a faceless edge of her shawl behind the man's arm). Bowl is OFF at 2.5-5.5 (mostly hidden behind his hands in the close-up). Man/woman boxes end above the bowl box, so the man's hands at the table are outside his box in some frames (7.5, 8.0 use a narrower, taller man box that keeps his hands). A small bird sits on the pergola in some frames, not used."}
json.dump(d,open("content/505.json","w"),indent=1)
