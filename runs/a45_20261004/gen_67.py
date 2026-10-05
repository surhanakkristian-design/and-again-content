import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
M={0.0:(0.18,0.20,0.82,0.80),0.5:(0.20,0.33,0.80,0.67),1.0:(0.32,0.29,0.68,0.71),1.5:(0.46,0.26,0.54,0.74),2.0:(0.48,0.22,0.52,0.78),
   2.5:(0.47,0.14,0.53,0.86),3.0:(0.46,0.17,0.54,0.83),3.5:(0.46,0.14,0.54,0.86),4.0:(0.45,0.12,0.55,0.88),4.5:(0.36,0.05,0.64,0.95),
   5.0:(0.27,0.04,0.73,0.96),5.5:(0.26,0.0,0.74,1.0),6.0:(0.18,0.0,0.82,1.0),6.5:(0.25,0.0,0.75,1.0),7.0:(0.08,0.04,0.92,0.96),
   7.5:(0.08,0.07,0.92,0.93),8.0:(0.14,0.07,0.86,0.93),8.5:(0.17,0.06,0.83,0.94),9.0:(0.27,0.11,0.73,0.89),9.5:(0.35,0.14,0.65,0.86),10.0:(0.48,0.14,0.52,0.86)}
W={1.0:(0.0,0.48,0.20,0.52),1.5:(0.0,0.33,0.44,0.67),2.0:(0.0,0.31,0.46,0.69),2.5:(0.0,0.25,0.46,0.75),3.0:(0.0,0.26,0.40,0.74),
   3.5:(0.0,0.26,0.38,0.74),4.0:(0.0,0.23,0.40,0.77),4.5:(0.0,0.24,0.30,0.76),5.0:(0.0,0.30,0.18,0.70),
   9.0:(0.0,0.33,0.18,0.67),9.5:(0.0,0.23,0.32,0.77),10.0:(0.0,0.21,0.35,0.79)}
c={"mediaId":67,"level":"A","keyWord":"banana","defaultVoice":"male",
 "taps":[
  {"phrase":"to peel a banana","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to point at the banana","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to eat a banana","target":"the man","voice":"male","keys":keys(M)}],
 "stillS":8.5,
 "nouns":[{"word":"a man","x":0.78,"y":0.25,"voice":"male"},{"word":"a banana","x":0.40,"y":0.56,"voice":"male"},
          {"word":"a parrot","x":0.14,"y":0.68,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","eating","a","banana."],
 "answerVoice":"male",
 "notes":"Two targets (man twice): the parrot is small, appears only from 6.5 s and has no simple A-level action phrase (it stands on a railing). The woman is only a thin sliver at the left edge at 0.0, 0.5, 5.5 and 6.0 (set off) and is out of frame 6.5-8.5. She points at the banana at 2.5 s only. 'peel' is A2. Only 3 nouns: the peeled, bitten banana at 8.5 s is the key word."}
json.dump(c,open('content/67.json','w'),indent=1)
