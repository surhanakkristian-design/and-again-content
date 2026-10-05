import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=b; x=max(0,x);y=max(0,y);x2=min(1,x2);y2=min(1,y2)
            out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
man={0.0:(0,0.44,1,1),0.5:(0,0.42,1,1),1.0:(0,0.57,0.94,1),1.5:(0,0.45,1,1),2.0:(0,0.45,1,1),2.5:(0,0.45,1,1),
 3.0:(0,0.38,1,1),3.5:(0.02,0.43,1,1),4.0:(0.3,0.33,1,1),4.5:(0.33,0.32,1,1),5.0:(0.36,0.32,1,1),5.5:(0.39,0.32,1,1),
 6.0:(0.41,0.34,1,1),6.5:(0.4,0.35,1,1),7.0:(0.42,0.36,1,1),7.5:(0.43,0.36,1,1),8.0:(0.44,0.35,1,1),8.5:(0.44,0.36,1,1),
 9.0:(0.48,0.68,0.66,0.86),9.5:(0.44,0.67,0.63,0.87),10.0:(0.43,0.66,0.61,0.86),10.5:(0.41,0.66,0.6,0.86),
 11.0:(0.36,0.65,0.65,0.86),11.5:(0.36,0.65,0.65,0.86),12.0:(0.36,0.66,0.66,0.86)}
statue={4.0:(0,0.06,0.2,0.44),4.5:(0.03,0.07,0.25,0.44),5.0:(0.07,0.07,0.3,0.45),5.5:(0.12,0.08,0.35,0.45),
 6.0:(0.15,0.09,0.38,0.47),6.5:(0.15,0.09,0.37,0.47),7.0:(0.18,0.09,0.4,0.5),7.5:(0.22,0.09,0.41,0.48),
 8.0:(0.22,0.09,0.42,0.48),8.5:(0.22,0.09,0.42,0.48)}
c={"mediaId":5448,"level":"B","keyWord":"billboard","defaultVoice":"male",
 "taps":[
  {"phrase":"to fling his arms wide","target":"the man","voice":"male","keys":K(man)},
  {"phrase":"to lean over the railing","target":"the man","voice":"male","keys":K(man)},
  {"phrase":"to hold up a torch","target":"the statue","voice":"male","keys":K(statue)}],
 "stillS":2.0,
 "nouns":[{"word":"a skyscraper","x":0.58,"y":0.15,"voice":"male"},
  {"word":"a billboard","x":0.36,"y":0.38,"voice":"male"},
  {"word":"a red jacket","x":0.55,"y":0.72,"voice":"male"},
  {"word":"a zebra crossing","x":0.15,"y":0.9,"voice":"male"}],
 "question":"What is he doing on the ferry?",
 "answer":["He","is","leaning","over","the","railing."],
 "answerVoice":"male",
 "notes":"Two taxis and many billboards in the city shot, so they are not tap targets; the man is the only person-target (two phrases, different shots). Statue target includes its pedestal. Man is small in the canyon shot (9-12 s); boxes padded to the minimum size."}
json.dump(c,open('content/5448.json','w'),indent=1)
