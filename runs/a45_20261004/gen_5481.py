import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={0.0:(0,0,0.45,1.0),0.5:(0,0.08,0.6,0.92),1.0:(0,0.15,0.5,0.85),1.5:(0,0.13,0.5,0.87),2.0:(0,0.12,0.5,0.88),
   2.5:(0,0.12,0.5,0.88),3.0:(0,0.13,0.5,0.87),3.5:(0,0.13,0.5,0.87),
   9.5:(0.12,0.18,0.88,0.7),10.0:(0.1,0.15,0.9,0.6),10.5:(0,0.12,1.0,0.68),11.0:(0.05,0.14,0.92,0.72),11.5:(0.1,0.15,0.85,0.73),12.0:(0.05,0.15,0.9,0.72)}
M={0.0:(0.47,0.36,0.53,0.64),0.5:(0.62,0.35,0.38,0.65),1.0:(0.52,0.35,0.48,0.65),1.5:(0.52,0.35,0.48,0.65),2.0:(0.52,0.35,0.48,0.65),
   2.5:(0.52,0.35,0.48,0.65),3.0:(0.52,0.35,0.48,0.65),3.5:(0.52,0.35,0.48,0.65),4.0:(0.15,0.27,0.85,0.73),4.5:(0,0.25,1.0,0.75),5.0:(0.15,0.28,0.85,0.72)}
for t in (5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0): M[t]=(0,0,1.0,0.95)
c={"mediaId":5481,"level":"A","keyWord":"pink","defaultVoice":"female",
 "taps":[
  {"phrase":"to fill the washing machine","target":"the woman","voice":"female","keys":K(W)},
  {"phrase":"to wash the clothes","target":"the washing machine","voice":"female","keys":K(M)},
  {"phrase":"to smell a clean T-shirt","target":"the woman","voice":"female","keys":K(W)}],
 "stillS":2.0,
 "nouns":[{"word":"pink hair","x":0.25,"y":0.25,"voice":"female"},{"word":"a curtain","x":0.6,"y":0.1,"voice":"female"},
   {"word":"a washing machine","x":0.8,"y":0.46,"voice":"female"},{"word":"clothes","x":0.45,"y":0.86,"voice":"female"}],
 "question":"What is she putting in the machine?",
 "answer":["She","is","putting","clothes","in","the","washing","machine."],
 "answerVoice":"female",
 "notes":"Cuts: 4.0-9.0 close-ups of the machine (woman only a hand/arm -> off); 9.5-12.0 filmed from inside the drum (machine off, woman on). Woman/machine boxes split at x~0.5 in 0.0-3.5 where her arm reaches into the drum. 'to wash the clothes' -> machine: the drum turning 5.5-9.0; a learner could argue the woman washes clothes too. Key word pink is an adjective; noun pill 'pink hair' carries it."}
json.dump(c,open('content/5481.json','w'),indent=1)
