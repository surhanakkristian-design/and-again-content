import json
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
T21=[i*0.5 for i in range(21)]; T19=[i*0.5 for i in range(19)]
def tap(p,tg,v,k): return {"phrase":p,"target":tg,"voice":v,"keys":k}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4559
man={0.0:(0.12,0.17,0.88,0.83),0.5:(0.18,0.17,0.82,0.83),1.0:(0.18,0.2,0.77,0.8),1.5:(0.2,0.2,0.75,0.8),
2.0:(0.3,0.22,0.6,0.78),2.5:(0.34,0.25,0.56,0.75),3.0:(0.4,0.28,0.48,0.72),3.5:(0.41,0.3,0.47,0.7),
4.0:(0.38,0.3,0.47,0.6),4.5:(0.45,0.3,0.4,0.55),5.0:(0.38,0.3,0.36,0.36),5.5:(0.42,0.28,0.34,0.36),
6.0:(0.4,0.26,0.34,0.3),6.5:(0.4,0.23,0.36,0.32),7.0:(0.38,0.25,0.36,0.33),7.5:(0.4,0.23,0.36,0.35),
8.0:(0.38,0.2,0.36,0.38),8.5:(0.38,0.18,0.38,0.4),9.0:(0.36,0.18,0.4,0.43),9.5:(0.36,0.18,0.42,0.45),10.0:(0.34,0.18,0.42,0.43)}
wom={0.5:(0.0,0.0,0.18,0.75),1.0:(0.0,0.2,0.18,0.65),1.5:(0.0,0.18,0.2,0.6),2.0:(0.0,0.15,0.3,0.75),2.5:(0.0,0.2,0.34,0.7),
3.0:(0.0,0.25,0.4,0.7),3.5:(0.05,0.27,0.36,0.68),4.0:(0.05,0.27,0.33,0.45),4.5:(0.27,0.28,0.18,0.37)}
km=keys(T21,man)
save({"mediaId":4559,"level":"B","keyWord":"console","defaultVoice":"male","taps":[
 tap("to clutch a yellow mug","the red-haired man","male",km),
 tap("to weep under a blanket","the red-haired man","male",km),
 tap("to stroke his arm gently","the woman","female",keys(T21,wom))],
 "stillS":1.0,"nouns":[noun("a mug",0.52,0.81,"male"),noun("a hoodie",0.5,0.66,"male"),noun("a blanket",0.78,0.56,"male"),noun("fairy lights",0.25,0.15,"male")],
 "question":"What are his friends doing?","answer":["They","are","consoling","their","weeping","friend."],"answerVoice":"male",
 "notes":"Tight group hug: only the red-haired man and the woman are targets (the other friends all do the same thing). Woman: at 0.0 only a sleeve is visible (off), at 0.5 only part of her face/arm at the left edge; hidden from 5.0. From 5.0 the man's box is his head only (rest covered by arms); mug partly hidden late. Boxes split along x between woman and man."})

# 4560
cox={0.0:(0.36,0.76,0.44,0.24),0.5:(0.24,0.75,0.56,0.25),1.0:(0.36,0.86,0.4,0.14),1.5:(0.34,0.83,0.48,0.17),2.0:(0.3,0.8,0.44,0.2),
2.5:(0.25,0.6,0.5,0.4),3.0:(0.25,0.6,0.52,0.4),3.5:(0.22,0.6,0.5,0.4),4.0:(0.17,0.58,0.47,0.34),4.5:(0.1,0.61,0.48,0.36),
5.0:(0.15,0.6,0.48,0.37),5.5:(0.17,0.63,0.46,0.36),6.0:(0.34,0.58,0.44,0.36),6.5:(0.58,0.57,0.42,0.36),
7.0:(0.22,0.68,0.56,0.32),7.5:(0.2,0.67,0.56,0.33),8.0:(0.2,0.66,0.5,0.34),8.5:(0.2,0.67,0.5,0.33),9.0:(0.2,0.68,0.5,0.32),
9.5:(0.22,0.68,0.5,0.32),10.0:(0.24,0.67,0.5,0.33)}
cyc={2.5:(0.3,0.19,0.2,0.14),3.0:(0.68,0.26,0.22,0.14),3.5:(0.1,0.26,0.22,0.14),4.5:(0.73,0.2,0.18,0.14),5.0:(0.21,0.2,0.18,0.14)}
row={7.0:(0.25,0.47,0.46,0.21),7.5:(0.24,0.47,0.42,0.2),8.0:(0.1,0.42,0.6,0.24),8.5:(0.12,0.4,0.56,0.27),9.0:(0.15,0.41,0.53,0.27),
9.5:(0.18,0.41,0.52,0.27),10.0:(0.2,0.39,0.52,0.28)}
save({"mediaId":4560,"level":"B","keyWord":"crew","defaultVoice":"female","taps":[
 tap("to wear bulky headphones","the cox","female",keys(T21,cox)),
 tap("to cycle along the towpath","the cyclist","male",keys(T21,cyc)),
 tap("to punch the air","the dark-haired rower","male",keys(T21,row))],
 "stillS":3.5,"nouns":[noun("a willow",0.4,0.13,"female"),noun("a cyclist",0.22,0.32,"male"),noun("a crew",0.68,0.5,"female"),noun("headphones",0.47,0.68,"female")],
 "question":"What is the crew doing?","answer":["The","crew","is","rowing","past","a","willow."],"answerVoice":"female",
 "notes":"Cox phrase is a state (her only unique action, steering, is not visible). Cyclist is tiny and only in 2.5-3.5, faint at 4.5/5.0; gender guessed male. The rower who punches the air is the man right in front of the cox in the last shot (7.0-10.0); in the earlier shots that seat holds a woman in mirrored sunglasses (generated-clip inconsistency), so he is off there. Cox/rower boxes split at the top of her headphones. 'a crew' pill sits on the line of rowers."})

# 4561
W={0.0:(0.33,0.51,0.47,0.49),0.5:(0.22,0.55,0.55,0.45),1.0:(0.3,0.54,0.52,0.46),1.5:(0.3,0.51,0.47,0.49),2.0:(0.33,0.52,0.5,0.48),
2.5:(0.22,0.56,0.53,0.44),3.0:(0.33,0.53,0.5,0.47),3.5:(0.32,0.51,0.46,0.49),4.0:(0.3,0.53,0.48,0.47),4.5:(0.33,0.51,0.48,0.49),
5.0:(0.33,0.53,0.5,0.47),5.5:(0.22,0.57,0.53,0.43),6.0:(0.32,0.51,0.47,0.49),6.5:(0.33,0.51,0.5,0.49),7.0:(0.22,0.57,0.52,0.43),
7.5:(0.25,0.57,0.6,0.43),8.0:(0.27,0.56,0.58,0.44),8.5:(0.28,0.55,0.57,0.45),9.0:(0.3,0.53,0.5,0.47),9.5:(0.3,0.53,0.46,0.47),10.0:(0.28,0.51,0.47,0.49)}
kw=keys(T21,W)
wil={t:(0.55,0.0,0.45,0.5) for t in T21}
save({"mediaId":4561,"level":"B","keyWord":"command","defaultVoice":"female","taps":[
 tap("to shout out commands","the woman in the cap","female",kw),
 tap("to wear a navy cap","the woman in the cap","female",kw),
 tap("to hang over the river","the willow","female",keys(T21,wil))],
 "stillS":4.0,"nouns":[noun("a willow",0.78,0.25,"female"),noun("the sky",0.3,0.1,"female"),noun("oars",0.14,0.545,"female"),noun("a cap",0.55,0.585,"female")],
 "question":"What is the woman in front doing?","answer":["She","is","shouting","commands","at","the","crew."],"answerVoice":"female",
 "notes":"'to shout out commands' is read from her wide-open mouth and headset microphone. Second phrase on her is a state (the rowers behind are bare-headed, mostly hidden and do the same rowing). Willow box is the fixed right-hand upper area; the tree drifts a little with the camera. 'oars' and 'a cap' pills are close in y (0.41 apart in x)."})

# 4562
Wm={0.0:(0,0,1,0.66),0.5:(0,0,1,0.56),1.0:(0,0,1,0.63),1.5:(0,0,1,0.64),2.0:(0,0,1,0.63),2.5:(0,0,1,0.63),3.0:(0,0,1,0.68),3.5:(0,0,1,0.67),4.0:(0,0,1,0.65),
4.5:(0.03,0.1,0.85,0.4),5.0:(0.0,0.12,0.82,0.38),5.5:(0.0,0.12,0.85,0.42),6.0:(0.02,0.27,0.8,0.59),6.5:(0.0,0.38,0.9,0.62),
7.0:(0.03,0.0,0.94,0.24),7.5:(0,0,1,0.5),8.0:(0,0.12,1,0.48),8.5:(0,0.17,1,0.48),9.0:(0,0.2,1,0.47)}
C={0.0:(0.33,0.66,0.45,0.3),0.5:(0.08,0.56,0.8,0.3),1.0:(0.07,0.63,0.72,0.23),1.5:(0.0,0.64,0.82,0.24),2.0:(0.03,0.63,0.8,0.23),2.5:(0.07,0.63,0.8,0.22),
3.0:(0.1,0.68,0.78,0.2),3.5:(0.08,0.67,0.8,0.23),4.0:(0.06,0.65,0.82,0.23),4.5:(0.3,0.5,0.26,0.16),5.0:(0.33,0.5,0.26,0.15),5.5:(0.3,0.54,0.26,0.14),
6.0:(0.38,0.86,0.22,0.14),7.0:(0,0.24,1,0.76),7.5:(0,0.5,1,0.5),8.0:(0,0.6,1,0.4),8.5:(0,0.65,1,0.35),9.0:(0,0.67,1,0.33)}
kw=keys(T19,Wm)
save({"mediaId":4562,"level":"A","keyWord":"direction","defaultVoice":"female","taps":[
 tap("to look at a compass","the woman","female",kw),
 tap("to point with her finger","the woman","female",kw),
 tap("to show the direction","the compass","female",keys(T19,C))],
 "stillS":5.0,"nouns":[noun("the sky",0.6,0.1,"female"),noun("a compass",0.45,0.57,"female"),noun("a sweater",0.3,0.75,"female"),noun("flowers",0.88,0.62,"female")],
 "question":"What is the woman looking at?","answer":["She","is","looking","at","a","compass."],"answerVoice":"female",
 "notes":"'the compass' = the small pocket compass on the moor (0.0-6.0) and the big ship's compass in the last shot (7.0-9.0): two objects, one name. The compass is always in front of her, so the boxes are split: woman above, compass below (her hands fall in the compass box; in the close-ups the top of the open lid is cut off by the split). She points only at 8.5-9.0. 'flowers' = the purple heather."})
