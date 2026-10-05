import json
T=[round(i*0.5,1) for i in range(25)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
M={1.5:(0.0,0.0,0.36,0.64),2.0:(0.0,0.0,0.68,0.88),2.5:(0.0,0.05,0.76,0.95),3.0:(0.0,0.10,0.70,0.90),
   10.5:(0.0,0.13,0.10,0.55),11.0:(0.0,0.15,0.22,0.45),11.5:(0.05,0.17,0.29,0.19)}
W={3.5:(0.15,0.06,0.43,0.35),4.0:(0.11,0.05,0.45,0.36),4.5:(0.15,0.05,0.45,0.36),5.0:(0.14,0.06,0.45,0.36),
   5.5:(0.15,0.06,0.46,0.37),6.0:(0.14,0.05,0.46,0.37),6.5:(0.14,0.05,0.48,0.37),
   10.0:(0.0,0.17,0.27,0.50),10.5:(0.12,0.20,0.23,0.34),11.0:(0.25,0.21,0.24,0.15)}
D={3.5:(0.40,0.42,0.23,0.14),4.0:(0.40,0.42,0.23,0.14),4.5:(0.41,0.42,0.22,0.14),5.0:(0.40,0.43,0.23,0.14),
   5.5:(0.41,0.44,0.23,0.14),6.0:(0.41,0.43,0.22,0.14),6.5:(0.40,0.43,0.23,0.14),7.0:(0.42,0.38,0.20,0.15),
   7.5:(0.42,0.37,0.20,0.16),8.0:(0.41,0.37,0.20,0.16),8.5:(0.40,0.37,0.20,0.16),9.0:(0.37,0.37,0.22,0.16),
   9.5:(0.39,0.38,0.22,0.16),10.0:(0.42,0.38,0.20,0.16),10.5:(0.37,0.38,0.23,0.16),11.0:(0.22,0.37,0.21,0.14),
   11.5:(0.0,0.36,0.20,0.18)}
c={"mediaId":5357,"level":"A","keyWord":"fancy","defaultVoice":"male",
 "taps":[
  {"phrase":"to push an old pram","target":"the man in the tracksuit","voice":"male","keys":keys(M)},
  {"phrase":"to smile at the dog","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to wear sunglasses","target":"the dog","voice":"male","keys":keys(D)}],
 "stillS":8.0,
 "nouns":[{"word":"trees","x":0.25,"y":0.10,"voice":"male"},{"word":"a man","x":0.72,"y":0.30,"voice":"male"},
          {"word":"a dog","x":0.52,"y":0.46,"voice":"male"},
          {"word":"a pram","x":0.40,"y":0.62,"voice":"male"}],
 "question":"What is the man in white pushing?",
 "answer":["He","is","pushing","a","fancy","pram."],
 "answerVoice":"male",
 "notes":"Packet description does not match the clip in detail: the old pram is pushed by a young man in a dark tracksuit (1.5-3.0 s, caption 20 euro, not shown in the description); the dog wears sunglasses only in the chrome pram. Tracksuit man reappears small at the left at 10.5-11.5 (boxed); at 12.0 only a striped trouser leg (off). Woman boxed on her upper body above the dog (her lower body is behind the stroller). defaultVoice male: no single main person (three people), evenId false."}
json.dump(c,open('content/5357.json','w'),indent=1)
