import json
times=[i*0.5 for i in range(21)]
split={0.0:.43,0.5:.43,1.0:.43,1.5:.44,2.0:.42,2.5:.42,3.0:.42,3.5:.43,4.0:.43,4.5:.43,5.0:.43,5.5:.44,6.0:.43,6.5:.42,7.0:.42,7.5:.42,8.0:.41,8.5:.40,9.0:.41,9.5:.42,10.0:.39}
def r(v): return round(v,2)
wom=[];exc=[];hou=[]
for t in times:
    s=split[t]; xs=.48 if t==10.0 else .50
    wom.append({"t":t,"x":xs,"y":s,"w":r(1-xs),"h":r(1-s)})
    exc.append({"t":t,"x":xs,"y":.20,"w":r(1-xs),"h":r(s-.20)})
    if t<=5.5: hb=(.03,.17,.56)
    elif t==6.0: hb=(.03,.24,.57)
    elif t==6.5: hb=(.03,.32,.57)
    elif t==10.0: hb=(.02,.37,.57)
    else: hb=(.02,.40,.61)
    hou.append({"t":t,"x":hb[0],"y":hb[1],"w":r(xs-hb[0]),"h":r(hb[2]-hb[1])})
d={"mediaId":4638,"level":"B","keyWord":"rubble","defaultVoice":"female",
"taps":[
 {"phrase":"to demolish a brick house","target":"the excavator","voice":"female","keys":exc},
 {"phrase":"to collapse into rubble","target":"the house","voice":"female","keys":hou},
 {"phrase":"to gesture towards the ruins","target":"the woman","voice":"female","keys":wom}],
"stillS":10.0,
"nouns":[{"word":"rubble","x":.20,"y":.50,"voice":"female"},
 {"word":"an excavator","x":.72,"y":.31,"voice":"female"},
 {"word":"a hard hat","x":.64,"y":.45,"voice":"female"},
 {"word":"a barrier","x":.22,"y":.72,"voice":"female"}],
"question":"What is happening to the house?",
"answer":["It","is","collapsing","into","rubble."],
"answerVoice":"female",
"notes":"Three targets overlap in the picture, so the boxes are split along straight lines: house = left of x 0.50, excavator = right of 0.50 above the top of the woman's helmet (arm and top of the cab only; the lower cab and tracks sit behind the woman's box), woman = right of 0.50 below that line (her outstretched left hand at 9.0-10.0 s reaches left of 0.50 and is outside her box). From 7.0 s the house is only a heap of rubble in dust; its box stays on the heap. The woman gestures only from 8.0 s."}
json.dump(d,open("content/4638.json","w"),indent=1,ensure_ascii=False)
