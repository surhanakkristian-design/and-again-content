import json
def K(d, times):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
T=[i*0.5 for i in range(21)]
woman={0.0:(0.16,0.17,0.66,0.55),0.5:(0.16,0.17,0.66,0.55),1.0:(0.11,0.17,0.80,0.55),1.5:(0.16,0.17,0.68,0.55),
 2.0:(0.16,0.16,0.66,0.56),2.5:(0.15,0.17,0.67,0.55),3.0:(0.17,0.18,0.65,0.54),3.5:(0.27,0.17,0.56,0.55),
 4.0:(0.25,0.16,0.57,0.56),4.5:(0.26,0.17,0.56,0.55),5.0:(0.25,0.19,0.53,0.53),5.5:(0.27,0.19,0.57,0.53),
 6.0:(0.26,0.2,0.54,0.53),6.5:(0.27,0.2,0.53,0.53),7.0:(0.25,0.21,0.62,0.52),7.5:(0.26,0.2,0.59,0.53),
 8.0:(0.26,0.19,0.58,0.54),8.5:(0.26,0.19,0.59,0.54),9.0:(0.24,0.26,0.60,0.47),9.5:(0.26,0.38,0.58,0.34),
 10.0:(0.26,0.40,0.58,0.32)}
c={"mediaId":5353,"level":"B","keyWord":"paperwork","defaultVoice":"female",
 "taps":[
  {"phrase":"to clutch the phone receiver","target":"the woman","voice":"female","keys":K(woman,T)},
  {"phrase":"to reach for a sticky note","target":"the woman","voice":"female","keys":K(woman,T)},
  {"phrase":"to slump over her desk","target":"the woman","voice":"female","keys":K(woman,T)}],
 "stillS":6.0,
 "nouns":[{"word":"ring binders","x":0.18,"y":0.24,"voice":"female"},
          {"word":"a sticky note","x":0.86,"y":0.51,"voice":"female"},
          {"word":"a phone cord","x":0.68,"y":0.64,"voice":"female"},
          {"word":"paperwork","x":0.62,"y":0.85,"voice":"female"}],
 "question":"What is piling up on her desk?",
 "answer":["Paperwork","is","piling","up","on","her","desk."],
 "answerVoice":"female",
 "notes":"All three phrases on the woman: the only other people are blurred extras walking past (bearded man 0.5-2.0, a hand on her shoulder at 2.0, women 2.5/3.5), none doing anything that fits only them. 'reach for a sticky note' is visible only around 1.0 (she holds a note and pink highlighter). Slump 9.0-10.0. A sticky note lands on her head at 10.0. Paper stacks in front of her are not in her box."}
json.dump(c,open('content/5353.json','w'),indent=1)
