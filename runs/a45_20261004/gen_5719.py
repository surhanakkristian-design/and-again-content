import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(lst): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) if b else {"t":t,"off":True} for t,b in zip(T,lst)]
woman=K([(.24,.25,.42,.28),(.25,.25,.42,.30),(.24,.25,.36,.31),(.22,.25,.38,.37),(.21,.21,.37,.36),(.17,.20,.45,.38),(.06,.20,.48,.40),(.03,.20,.60,.40)])
off=K([(.20,.53,.80,.47),(.20,.55,.80,.45),(.36,.56,.64,.44),(.60,.37,.40,.63),(.58,.41,.42,.59),(.42,.58,.58,.42),(.36,.60,.64,.40),(.32,.60,.68,.40)])
c={"mediaId":5719,"level":"B","keyWord":"certification","defaultVoice":"female",
"taps":[
 {"phrase":"to press a brass seal","target":"the official","voice":"female","keys":off},
 {"phrase":"to hold up the certificate","target":"the official","voice":"female","keys":off},
 {"phrase":"to smile with delight","target":"the young woman","voice":"female","keys":woman}],
"stillS":3.7,
"nouns":[{"word":"a chandelier","x":0.60,"y":0.07,"voice":"female"},{"word":"a potted plant","x":0.80,"y":0.21,"voice":"female"},
 {"word":"a cardigan","x":0.17,"y":0.52,"voice":"female"},{"word":"a certificate","x":0.66,"y":0.62,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","smiling","with","delight."],
"answerVoice":"female",
"notes":"The official is only hands, arm and dark sleeve (gender not clear), so voice = defaultVoice. Woman box and official box are split horizontally around y 0.53-0.60; at 1.7 the official's hand on the lever covers the woman's face (inside her box) and his box is the arm on the right. 'to press a brass seal' fits 0.2-1.7, 'to hold up the certificate' 2.7-3.7. Key word 'certification' not visible as a noun; 'a certificate' used instead."}
json.dump(c,open('content/5719.json','w'),indent=1)
