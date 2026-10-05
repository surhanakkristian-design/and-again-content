import json
def K(times, boxes):
    return [{"t":t,"off":True} if boxes.get(t) is None else dict(t=t,x=boxes[t][0],y=boxes[t][1],w=boxes[t][2],h=boxes[t][3]) for t in times]
T=[i*0.5 for i in range(19)]
man={0.0:(0,0.02,0.79,0.98),0.5:(0.02,0.02,0.77,0.97),1.0:(0.08,0.03,0.72,0.97),1.5:(0.13,0.06,0.77,0.94),2.0:(0.13,0.03,0.6,0.97),2.5:(0.1,0,0.76,1),3.0:(0.08,0.22,0.84,0.78),3.5:(0.08,0.11,0.86,0.89),4.0:(0.08,0.03,0.84,0.97),4.5:(0.12,0.2,0.82,0.8),5.0:(0.1,0.22,0.84,0.78),5.5:(0.08,0,0.84,1),6.0:(0.05,0.05,0.72,0.95),6.5:(0,0.04,0.76,0.96),7.0:(0,0.05,0.76,0.95),7.5:(0,0.06,0.76,0.94),8.0:(0,0.1,0.7,0.9),8.5:(0,0.13,0.69,0.87),9.0:(0,0.15,0.58,0.85)}
doc={0.0:(0.8,0.08,0.2,0.88),0.5:(0.8,0.1,0.2,0.8),6.5:(0.77,0.1,0.23,0.9),7.0:(0.77,0.15,0.23,0.85),7.5:(0.77,0.13,0.23,0.87),8.0:(0.75,0.16,0.25,0.84),8.5:(0.7,0.18,0.3,0.82),9.0:(0.6,0.21,0.4,0.79)}
d={"mediaId":5016,"level":"A","keyWord":"knee","defaultVoice":"male",
"taps":[
 {"phrase":"to bend his knees","target":"the young man","voice":"male","keys":K(T,man)},
 {"phrase":"to wear round glasses","target":"the young man","voice":"male","keys":K(T,man)},
 {"phrase":"to hold a small hammer","target":"the doctor","voice":"female","keys":K(T,doc)}],
"stillS":9.0,
"nouns":[{"word":"glasses","x":0.22,"y":0.26,"voice":"male"},{"word":"a cupboard","x":0.62,"y":0.19,"voice":"male"},{"word":"a doctor","x":0.84,"y":0.5,"voice":"female"},{"word":"a knee","x":0.3,"y":0.76,"voice":"male"}],
"question":"What is the doctor holding?",
"answer":["She","is","holding","a","small","hammer."],
"answerVoice":"female",
"notes":"Doctor is a grey-haired woman. Between 1.0 and 6.0 only a thin strip of her coat shows at the right edge, so she is marked off there (too small to tap). Only two possible targets; the young man carries two phrases. 'a hammer' = reflex hammer, kept simple for level A."}
json.dump(d,open("content/5016.json","w"),indent=1)
