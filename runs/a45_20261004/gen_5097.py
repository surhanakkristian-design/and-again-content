import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
man={0.0:(0,0.03,1,0.97),0.5:(0,0.05,1,0.95),1.0:(0,0.06,1,0.94),1.5:(0,0.07,1,0.93),
 2.0:(0.15,0.19,0.48,0.67),2.5:(0.10,0.19,0.52,0.66),3.0:(0.08,0.31,0.48,0.64),3.5:(0.06,0.31,0.48,0.63),
 4.0:(0.02,0.18,0.53,0.67),4.5:(0.02,0.18,0.52,0.66),5.0:(0,0.16,0.50,0.69),5.5:(0,0.16,0.52,0.68),
 6.0:(0,0.05,1,0.95),6.5:(0,0,1,1),7.0:(0,0,0.85,1),7.5:(0,0.10,0.95,0.90),8.0:(0,0.07,1,0.93),8.5:(0,0.13,1,0.87),9.0:(0,0.40,1,0.60)}
wom={2.5:(0.82,0.28,0.18,0.40),3.0:(0.82,0.29,0.18,0.38),3.5:(0.80,0.29,0.20,0.38),
 4.0:(0.80,0.27,0.20,0.40),4.5:(0.80,0.26,0.20,0.41),5.0:(0.78,0.27,0.22,0.40),5.5:(0.78,0.27,0.22,0.40)}
c={"mediaId":5097,"level":"A","keyWord":"music","defaultVoice":"male",
"taps":[
 {"phrase":"to play the guitar","target":"the man with the guitar","voice":"male","keys":K(man)},
 {"phrase":"to raise his hand","target":"the man with the guitar","voice":"male","keys":K(man)},
 {"phrase":"to hold a baby","target":"the woman with the baby","voice":"female","keys":K(wom)}],
"stillS":4.0,
"nouns":[{"word":"the sky","x":0.65,"y":0.08,"voice":"male"},
 {"word":"a guitar","x":0.17,"y":0.47,"voice":"male"},
 {"word":"a baby","x":0.89,"y":0.38,"voice":"male"},
 {"word":"a guitar case","x":0.55,"y":0.82,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","playing","music","in","the","street."],"answerVoice":"male",
"notes":"Main target the street musician (all frames). He throws his strumming hand up at 6.5-7.0 ('to raise his hand'); the clapping onlookers at 7.5-9.0 do not raise a hand above the head. The woman holding the toddler is visible only in the wide shot 2.0-5.5 at the right edge (at 2.0 only a sliver at the edge, set off); off in the close shots. Baby noun voice = default (gender unclear)."}
json.dump(c,open('content/5097.json','w'),indent=1)
