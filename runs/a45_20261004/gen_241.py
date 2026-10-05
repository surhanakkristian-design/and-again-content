import json
T=[i*0.5 for i in range(19)]
M={0.0:(0,.13,1,.87),0.5:(.38,0,.62,.62),1.0:(.40,0,.60,.47),1.5:(.41,0,.59,.56),2.0:(.38,0,.62,.67),2.5:(.38,0,.62,.67),3.0:(0,.20,1,.80),3.5:(0,.10,1,.90),4.0:(0,0,1,1),4.5:(0,0,1,1),
   5.0:(.43,.03,.57,.70),5.5:(.26,.15,.74,.60),6.5:(0,.50,1,.50),7.0:(0,.52,.66,.48),7.5:(0,.50,.59,.50),8.0:(0,.50,.62,.50),8.5:(.03,.08,.97,.92),9.0:(0,.08,1,.92)}
W={7.0:(.68,.38,.25,.38),7.5:(.60,.40,.29,.29),8.0:(.63,.38,.29,.31)}
def keys(D):
    return [({"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} if t in D else {"t":t,"off":True}) for t in T]
c={"mediaId":241,"level":"A","keyWord":"drawing","defaultVoice":"male",
"taps":[
 {"phrase":"to sit on the steps","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to make a drawing","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to wear a yellow hat","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":8.0,
"nouns":[{"word":"a drawing","x":0.35,"y":0.52,"voice":"male"},{"word":"a hat","x":0.77,"y":0.43,"voice":"male"},{"word":"houses","x":0.45,"y":0.20,"voice":"male"},{"word":"a shirt","x":0.62,"y":0.85,"voice":"male"}],
"question":"What is the man showing the woman?",
"answer":["He","is","showing","her","his","drawing."],
"answerVoice":"male",
"notes":"Animated clip with many cuts. 0.5-2.5 and 5.0-5.5 are close-ups of the man's hand with the pencil: the box is on the hand. 6.0 shows only the drawing (man off). At 7.0-8.0 the man is seen from behind, his head and right shoulder touch the woman; his box covers his left arm, hands and back left of her, hers the hat, face and upper body. The woman is only in the clip at 7.0-8.0."}
json.dump(c,open('content/241.json','w'),indent=1,ensure_ascii=False)
