import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
brush={0.0:(0,.48,.56,.24),0.5:(0,.12,.40,.25),1.0:(0,.43,.76,.50),1.5:(0,.38,.64,.50),2.0:(0,.31,.64,.42),2.5:(0,.30,.50,.40),
3.0:(0,.33,.48,.48),3.5:(0,.38,.53,.52),4.0:(0,.39,.67,.48),4.5:(0,.29,.53,.37)}
shirt={1.5:(.66,0,.34,1),2.0:(.66,0,.34,1),2.5:(.52,0,.48,1),3.0:(.50,0,.50,1),3.5:(.55,0,.45,1),4.0:(.69,0,.31,1),4.5:(.55,0,.45,1),
5.0:(0,0,1,1),5.5:(0,0,1,1),6.0:(0,0,1,1),6.5:(0,0,1,1),
7.0:(.52,0,.48,1),7.5:(.54,0,.46,1),8.0:(.54,0,.46,1),8.5:(.62,0,.38,1),9.0:(.58,0,.42,1),9.5:(.57,0,.43,1),10.0:(.55,0,.45,1)}
scarf={7.0:(0,0,.50,.72),7.5:(0,0,.52,.70),8.0:(0,0,.52,.66),8.5:(0,0,.60,.68),9.0:(0,0,.56,.72),9.5:(0,0,.55,.72),10.0:(0,0,.53,.66)}
c={"mediaId":282,"level":"B","keyWord":"eyeshadow","defaultVoice":"female",
"taps":[
 {"phrase":"to pick up gold eyeshadow","target":"the brush","voice":"female","keys":keys(brush)},
 {"phrase":"to wear a headscarf","target":"the woman in the headscarf","voice":"female","keys":keys(scarf)},
 {"phrase":"to show off golden eyelids","target":"the woman in the shirt","voice":"female","keys":keys(shirt)}],
"stillS":9.5,
"nouns":[{"word":"a headscarf","x":.28,"y":.12,"voice":"female"},{"word":"eyeshadow","x":.78,"y":.30,"voice":"female"},
 {"word":"a collar","x":.76,"y":.71,"voice":"female"},{"word":"a button","x":.80,"y":.89,"voice":"female"}],
"question":"What is the brush picking up?",
"answer":["It","is","picking","up","gold","eyeshadow."],
"answerVoice":"female",
"notes":"Close-up 1.5-6.5 is the face of the woman in the shirt: there her box is the part of the frame right of the brush box (rectangles cannot follow the diagonal brush), full frame at 5.0-6.5. In the two-shot her shirt reaches under the other woman at the lower left; her box is only the right column. 'to wear a headscarf' is a state: the friend has no clear action of her own. Eyeshadow pill sits on her gold eyelid at 9.5."}
json.dump(c,open('content/282.json','w'),indent=1)
