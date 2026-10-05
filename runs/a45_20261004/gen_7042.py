import json
def K(times, d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in times]
def B(x0,y0,x1,y1): return (x0,y0,round(x1-x0,2),round(y1-y0,2))
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom={0.2:B(.19,.16,.90,1.0),0.7:B(.17,.15,.92,1.0),1.2:B(.15,.14,.94,1.0),1.7:B(.15,.12,.95,1.0),
     2.2:B(.15,.10,.96,1.0),2.7:B(.14,.11,1.0,1.0),3.2:B(.07,.12,1.0,1.0),3.7:B(.05,.09,1.0,1.0)}
k=K(T,wom)
c={"mediaId":7042,"level":"A","keyWord":"digital camera","defaultVoice":"female",
 "taps":[
  {"phrase":"to take photos","target":"the woman","voice":"female","keys":k},
  {"phrase":"to lean on a fence","target":"the woman","voice":"female","keys":k},
  {"phrase":"to touch her hair","target":"the woman","voice":"female","keys":k}],
 "stillS":0.2,
 "nouns":[{"word":"a lighthouse","x":.33,"y":.21,"voice":"female"},{"word":"a digital camera","x":.40,"y":.34,"voice":"female"},
          {"word":"a fence","x":.14,"y":.55,"voice":"female"},{"word":"a backpack","x":.60,"y":.87,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","taking","photos","with","a","digital","camera."],
 "answerVoice":"female",
 "notes":"Only one person in the clip, so all three phrases target the woman. 'to touch her hair' happens at 3.2-3.7 s (she pushes her hair back). Box includes the dangling camera strap."}
json.dump(c,open("content/7042.json","w"),indent=1,ensure_ascii=False)
