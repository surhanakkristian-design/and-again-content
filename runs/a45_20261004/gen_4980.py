import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
full=(0.0,0.0,1.0,1.0)
coffee={2.5:full,3.0:full}
flowers={3.5:full,4.0:full,4.5:full}
group={6.5:(0.0,0.4,1.0,1.0),7.0:(0.0,0.47,1.0,1.0),7.5:(0.0,0.47,1.0,1.0),8.0:(0.0,0.48,1.0,1.0),8.5:(0.0,0.48,1.0,1.0),9.0:(0.0,0.5,1.0,1.0)}
c={"mediaId":4980,"level":"A","keyWord":"to breathe","defaultVoice":"female",
 "taps":[
  {"phrase":"to smell his coffee","target":"the man with the coffee","voice":"male","keys":keys(coffee)},
  {"phrase":"to smell the flowers","target":"the woman with the flowers","voice":"female","keys":keys(flowers)},
  {"phrase":"to spread their arms wide","target":"the group of friends","voice":"female","keys":keys(group)}],
 "stillS":8.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"female"},
          {"word":"hills","x":0.50,"y":0.43,"voice":"female"},
          {"word":"people","x":0.50,"y":0.62,"voice":"female"}],
 "question":"What are the friends doing?",
 "answer":["They","are","taking","a","deep","breath."],
 "answerVoice":"female",
 "notes":"Five shots, each a full-frame close-up except the group: coffee man 2.5-3.0 and flower woman 3.5-4.5 boxes are the whole frame. The curly woman in the denim jacket in the group shot may be the flower woman; left inside the group box there (boxes may not overlap). Only 3 nouns (the group shot has no other clear separate objects). Key word is a verb, used in the answer as 'a deep breath'."}
json.dump(c,open('content/4980.json','w'),indent=1)
