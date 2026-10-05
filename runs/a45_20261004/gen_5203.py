import json
T=[i*0.5 for i in range(19)]
def K(d): return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,**dict(zip("xywh",d[t]))) for t in T]
M={0.5:(0.28,0.27,0.14,0.36),1.0:(0.29,0.25,0.5,0.75),1.5:(0.26,0.23,0.73,0.77),2.0:(0.29,0.18,0.67,0.82),2.5:(0.28,0.37,0.3,0.63),
   3.0:(0.4,0.33,0.3,0.67),3.5:(0.63,0.2,0.37,0.8),4.0:(0.82,0.21,0.18,0.7),4.5:(0.76,0.17,0.24,0.15),
   6.5:(0.7,0.26,0.3,0.2),7.0:(0.66,0.26,0.32,0.3),7.5:(0.67,0.26,0.26,0.2),8.0:(0.66,0.26,0.21,0.15),9.0:(0.56,0.24,0.18,0.14)}
W={2.0:(0.17,0.38,0.11,0.55),2.5:(0.05,0.38,0.22,0.6),3.0:(0.02,0.37,0.36,0.63),3.5:(0.09,0.36,0.35,0.64),4.0:(0.04,0.37,0.58,0.63),4.5:(0.2,0.35,0.55,0.65)}
c={"mediaId":5203,"level":"B","keyWord":"relative","defaultVoice":"male",
 "taps":[
  {"phrase":"to push the front door open","target":"the man in the patterned jumper","voice":"male","keys":K(M)},
  {"phrase":"to carry a covered cake","target":"the man in the patterned jumper","voice":"male","keys":K(M)},
  {"phrase":"to hold a strawberry cake","target":"the woman in the grey cardigan","voice":"female","keys":K(W)}],
 "stillS":8.5,
 "nouns":[{"word":"a bouquet","x":0.1,"y":0.4,"voice":"male"},{"word":"a coat rack","x":0.3,"y":0.31,"voice":"male"},
          {"word":"a fountain","x":0.57,"y":0.22,"voice":"male"},{"word":"champagne glasses","x":0.56,"y":0.43,"voice":"male"}],
 "question":"What are the relatives doing?",
 "answer":["They","are","raising","their","glasses","for","a","toast."],
 "answerVoice":"male",
 "notes":"Crowded family scene; only two targets are reliably trackable (man in the patterned jumper, woman in the grey cardigan with the strawberry cake). Woman off from 5.0 on (not identifiable in the crowd), off at 0.5-1.5 (hidden behind the man). Man's cake sits under a glass dome ('covered'), the woman's is open with cream and strawberries. Man off at 8.5 (face only, too close to the white-haired man), small at 9.0 (top centre). Key word 'a relative' not used as a noun pill (no single person is identifiable as 'a relative')."}
json.dump(c,open('content/5203.json','w'),indent=1)
