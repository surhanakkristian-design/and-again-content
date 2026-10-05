import json
T=[i*0.5 for i in range(25)]
def mk(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
grey={0.0:(0,0.28,0.52,0.72),0.5:(0,0.27,0.49,0.73),1.0:(0,0.27,0.32,0.73),1.5:(0,0.27,0.18,0.6),2.0:(0,0.26,0.18,0.22),
 2.5:(0,0.25,0.18,0.37),3.0:(0,0.26,0.22,0.4),3.5:(0,0.26,0.2,0.4)}
denim={4.0:(0,0.32,0.5,0.68),4.5:(0,0.32,0.37,0.68),5.0:(0,0.35,0.18,0.65),5.5:(0,0.38,0.18,0.62),6.0:(0,0.5,0.18,0.2),6.5:(0,0.5,0.18,0.2)}
robe={7.5:(0.4,0.38,0.2,0.6),8.0:(0.27,0.36,0.47,0.58),8.5:(0.18,0.34,0.66,0.63),9.0:(0.06,0.35,0.88,0.65),9.5:(0.05,0.34,0.95,0.66),
 10.0:(0.02,0.33,0.98,0.67),10.5:(0,0.33,1,0.67),11.0:(0,0.32,1,0.68),11.5:(0,0.31,1,0.69),12.0:(0,0.31,1,0.69)}
c={"mediaId":5479,"level":"B","keyWord":"robe","defaultVoice":"female",
 "taps":[{"phrase":"to peek around the door","target":"the woman in grey","voice":"female","keys":mk(grey)},
  {"phrase":"to wear a denim shirt","target":"the woman in denim","voice":"female","keys":mk(denim)},
  {"phrase":"to throw her arms wide","target":"the woman in the robe","voice":"female","keys":mk(robe)}],
 "stillS":10.0,
 "nouns":[{"word":"the ceiling","x":0.5,"y":0.1,"voice":"female"},{"word":"handbags","x":0.5,"y":0.32,"voice":"female"},
  {"word":"a robe","x":0.5,"y":0.72,"voice":"female"},{"word":"a marble floor","x":0.17,"y":0.86,"voice":"female"}],
 "question":"What is the barefoot woman doing?",
 "answer":["She","is","throwing","her","arms","wide."],"answerVoice":"female",
 "notes":"Three women in three separate shots, never together. Woman in grey only a sliver at the left edge 1.5-2.0 (min-size boxes). Phrase 2 is a state because both the first and second women open doors. Woman in denim only a hand at the left edge 6.0-6.5; set OFF at 7.0. 'handbags' = the row of bags on the top back shelf just above her head."}
json.dump(c,open('content/5479.json','w'),indent=1)
