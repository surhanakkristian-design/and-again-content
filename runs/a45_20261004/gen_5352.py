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
woman={}
for t in T:
    if t<4.0: woman[t]=(0,0.04,0.72,0.66)
    elif t<4.5: woman[t]=(0,0.04,0.70,0.64)
    elif t<7.0: woman[t]=(0,0.06,0.72,0.62)
    else: woman[t]=(0,0.07,0.72,0.63)
lamp={t:(0.74,0.0,0.26,0.21) for t in T}
c={"mediaId":5352,"level":"B","keyWord":"frustration","defaultVoice":"female",
 "taps":[
  {"phrase":"to chew on a pencil","target":"the woman","voice":"female","keys":K(woman,T)},
  {"phrase":"to clutch her head","target":"the woman","voice":"female","keys":K(woman,T)},
  {"phrase":"to light up the desk","target":"the desk lamp","voice":"female","keys":K(lamp,T)}],
 "stillS":0.0,
 "nouns":[{"word":"a desk lamp","x":0.80,"y":0.10,"voice":"female"},
          {"word":"sticky notes","x":0.78,"y":0.24,"voice":"female"},
          {"word":"a pile of papers","x":0.80,"y":0.40,"voice":"female"},
          {"word":"a smartphone","x":0.37,"y":0.74,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","clutching","her","head","in","frustration."],
 "answerVoice":"female",
 "notes":"Static shot, one person. Pencil in mouth 0.0-3.5; hands on head 4.5-7.0, face in hands 7.5-10.0 (question/answer fits the middle and end). Woman box stops at x 0.72 so it does not touch the lamp box; her right hand on the keyboard (x 0.72-0.87) at 0-3.5 is outside the box. 'light up the desk' vs the phone screen that lights up at 2.5: phone not a target. Noun pencil avoided: a second pencil sits in her hair bun."}
json.dump(c,open('content/5352.json','w'),indent=1)
