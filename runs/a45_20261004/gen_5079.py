import json,os
H=os.path.dirname(os.path.abspath(__file__))
def keys(times,d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in times]
T=[i*0.5 for i in range(25)]
wom={0.0:(0.10,0.38,0.90,0.62),0.5:(0.15,0.38,0.72,0.62),1.0:(0.26,0.40,0.54,0.60),1.5:(0.03,0.41,0.93,0.59),2.0:(0.24,0.42,0.40,0.58),2.5:(0.0,0.42,0.77,0.58),
 3.0:(0.0,0.15,1.0,0.85),3.5:(0.0,0.16,1.0,0.84),4.0:(0.03,0.13,0.97,0.87),4.5:(0.05,0.13,0.95,0.87),5.0:(0.0,0.12,1.0,0.88),5.5:(0.0,0.13,1.0,0.87),
 6.0:(0.0,0.10,1.0,0.90),6.5:(0.0,0.11,1.0,0.89),7.0:(0.0,0.12,1.0,0.88),7.5:(0.0,0.13,1.0,0.87),
 8.0:(0.08,0.0,0.63,0.47),8.5:(0.23,0.02,0.54,0.60),9.0:(0.20,0.18,0.54,0.68),9.5:(0.16,0.30,0.56,0.70),10.0:(0.29,0.32,0.53,0.68),10.5:(0.28,0.34,0.50,0.66),
 11.0:(0.10,0.31,0.90,0.69),11.5:(0.03,0.33,0.97,0.67),12.0:(0.07,0.39,0.88,0.61)}
ban={0.0:(0.0,0.0,1.0,0.38),0.5:(0.0,0.0,1.0,0.37),1.0:(0.0,0.0,1.0,0.40),1.5:(0.0,0.0,1.0,0.41),2.0:(0.0,0.0,1.0,0.42),2.5:(0.0,0.0,1.0,0.42)}
wk=keys(T,wom)
c={"mediaId":5079,"level":"B","keyWord":"pyramid","defaultVoice":"female",
"taps":[
 {"phrase":"to bite into a taco","target":"the young woman","voice":"female","keys":wk},
 {"phrase":"to climb the stone steps","target":"the young woman","voice":"female","keys":wk},
 {"phrase":"to hang across the street","target":"the paper banners","voice":"female","keys":keys(T,ban)}],
"stillS":9.5,
"nouns":[{"word":"the sky","x":0.50,"y":0.10,"voice":"female"},{"word":"a pyramid","x":0.55,"y":0.29,"voice":"female"},
 {"word":"a straw bag","x":0.50,"y":0.60,"voice":"female"},{"word":"steps","x":0.78,"y":0.87,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","biting","into","a","juicy","taco."],"answerVoice":"female",
"notes":"Three shots: street with paper banners (0.0-2.5), fruit market close-up eating a taco (3.0-7.5), stone steps and the top of the ruin with the pyramid behind (8.0-12.0). The pyramid was NOT used as a tap target because from 9.0 on the woman stands right in front of it (head/arms over it), no clean split; it is a noun on the 9.5 still. The banner box covers the whole upper street above her head; at 0.0 a few banners at the right edge hang lower than the box. Woman boxes at 9.0-10.5 overlap the distant pyramid in the picture (not a target). Market vendor in the blurred background (3.0-7.5) is not used."}
json.dump(c,open(f"{H}/content/5079.json","w"),indent=1)
