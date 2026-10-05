import json
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(zip(("t","x","y","w","h"),(t,)+d[t])) for t in T]
w={0.0:(0,0.68,0.28,0.24),0.5:(0.15,0.44,0.77,0.56),1.0:(0.24,0.43,0.76,0.57),1.5:(0,0.42,0.86,0.58),2.0:(0.26,0.41,0.46,0.59),
 2.5:(0.28,0.23,0.52,0.77),3.0:(0,0.12,1,0.88),3.5:(0.2,0,0.8,0.6),4.0:(0.2,0,0.8,0.6),4.5:(0.18,0,0.82,0.62),5.0:(0.15,0.04,0.85,0.62),
 5.5:(0.15,0.04,0.85,0.62),6.0:(0.13,0,0.87,0.68),6.5:(0.18,0,0.82,0.68),7.0:(0.14,0,0.86,0.68),7.5:(0.22,0,0.78,0.68),8.0:(0.2,0,0.8,0.68),
 8.5:(0.22,0,0.78,0.68),9.0:(0.1,0,0.9,0.68),9.5:(0.3,0.41,0.38,0.59),10.0:(0.02,0.42,0.96,0.58),10.5:(0.08,0.43,0.86,0.57),
 11.0:(0.09,0.45,0.86,0.55),11.5:(0.09,0.45,0.88,0.55),12.0:(0.02,0.44,0.96,0.56)}
c={"mediaId":5316,"level":"B","keyWord":"curly","defaultVoice":"female",
"taps":[{"phrase":"to wave a folding fan","target":"the woman","voice":"female","keys":K(w)},
{"phrase":"to sip red wine","target":"the woman","voice":"female","keys":K(w)},
{"phrase":"to spread her arms wide","target":"the woman","voice":"female","keys":K(w)}],
"stillS":6.5,
"nouns":[{"word":"curls","x":0.8,"y":0.12,"voice":"female"},{"word":"a wine glass","x":0.3,"y":0.42,"voice":"female"},
{"word":"potatoes","x":0.17,"y":0.7,"voice":"female"},{"word":"cured ham","x":0.62,"y":0.86,"voice":"female"}],
"question":"What is the woman drinking?","answer":["She","is","sipping","a","glass","of","red","wine."],"answerVoice":"female",
"notes":"Only one person is identifiable (bar guests are blurred), so all three phrases target the woman. 0.0 s shows only her hand with the fan (box on hand+fan). Key word 'curly' is an adjective, used as the noun 'curls' on her hair."}
json.dump(c,open('content/5316.json','w'),indent=1)
