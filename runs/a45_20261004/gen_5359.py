import json
times=[i*0.5 for i in range(25)]
def hip(t):
    if t<=5.5: return dict(x=0.27,y=0.19,w=0.42,h=0.53)
    if t<=9.0: return dict(x=0.29,y=0.22,w=0.40,h=0.50)
    return None
def wom(t):
    if t<10.0: return dict(x=0.70,y=0.28,w=0.30,h=0.72)
    return dict(x=0.71,y=0.31,w=0.29,h=0.69)
def keys(f):
    out=[]
    for t in times:
        b=f(t)
        out.append({"t":t,**b} if b else {"t":t,"off":True})
    return out
c={"mediaId":5359,"level":"A","keyWord":"hippo","defaultVoice":"female",
 "taps":[
  {"phrase":"to point at the hippo","target":"the woman","voice":"female","keys":keys(wom)},
  {"phrase":"to go under the water","target":"the hippo","voice":"female","keys":keys(hip)},
  {"phrase":"to wear a cap","target":"the woman","voice":"female","keys":keys(wom)}],
 "stillS":1.0,
 "nouns":[{"word":"water","x":0.40,"y":0.10,"voice":"female"},
          {"word":"a hippo","x":0.45,"y":0.40,"voice":"female"},
          {"word":"a cap","x":0.88,"y":0.36,"voice":"female"},
          {"word":"a fence","x":0.20,"y":0.86,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","pointing","at","the","hippo."],
 "answerVoice":"female",
 "notes":"Hippo sinks; boxed while its body is still visible under the surface (to 9.0 s), off from 9.5 s. Woman box excludes her pointing hand to keep clear of the hippo box."}
json.dump(c,open('content/5359.json','w'),indent=1)
