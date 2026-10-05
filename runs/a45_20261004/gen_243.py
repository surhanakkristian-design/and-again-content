import json
T=[i*0.5 for i in range(21)]
W={0.0:(0,0,1,1),0.5:(0,.32,1,.68),1.0:(0,.06,1,.94),1.5:(0,.05,1,.95),2.0:(0,.02,1,.98),2.5:(0,.02,1,.98),
   3.0:(.45,.18,.50,.82),3.5:(.50,.20,.47,.80),4.0:(.38,.16,.62,.84),4.5:(.36,.11,.64,.89),5.0:(.37,.17,.63,.83),
   5.5:(.15,0,.80,.95),6.0:(0,0,1,.82),6.5:(0,0,1,.82),7.0:(0,0,.95,.85),7.5:(.03,.08,.97,.92),8.0:(.02,.08,.98,.92),8.5:(.02,.08,.98,.92),
   9.0:(.02,.15,.98,.85),9.5:(.06,.05,.83,.95),10.0:(.21,.20,.59,.80)}
M={3.0:(0,.16,.44,.60),3.5:(0,.17,.49,.60),4.0:(0,.13,.37,.35),4.5:(.02,.11,.33,.40),5.0:(.03,.15,.33,.40)}
def keys(D):
    return [({"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} if t in D else {"t":t,"off":True}) for t in T]
c={"mediaId":243,"level":"A","keyWord":"dressing","defaultVoice":"female",
"taps":[
 {"phrase":"to put on a sweater","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to help her get dressed","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to look in the mirror","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":10.0,
"nouns":[{"word":"a hat","x":0.50,"y":0.28,"voice":"female"},{"word":"a bag","x":0.57,"y":0.61,"voice":"female"},{"word":"a door","x":0.13,"y":0.47,"voice":"female"},{"word":"jeans","x":0.46,"y":0.81,"voice":"female"}],
"question":"What is the man doing?",
"answer":["He","is","helping","her","get","dressed."],
"answerVoice":"male",
"notes":"The man stands right behind the woman at 3.0-5.0 only; the boxes are split along a vertical line beside her head, so at 3.0-3.5 his box also covers the jacket he holds and a strip of her sweater. The thumbs-up hand at 8.5-9.0 has no visible owner, so the man is off there and the hand lies inside the woman's box. At 7.5-9.0 the woman's box covers her and her mirror reflection. 5.5-7.0 show only her legs and boots."}
json.dump(c,open('content/243.json','w'),indent=1,ensure_ascii=False)
