import json
T=[i*0.5 for i in range(21)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(zip(("t","x","y","w","h"),(t,)+d[t])) for t in T]
w={0.0:(0,0.33,1,0.67),0.5:(0,0.33,1,0.67),1.0:(0,0.31,1,0.69),1.5:(0,0.31,1,0.69),2.0:(0,0.31,1,0.69),2.5:(0,0.29,1,0.71),
 3.0:(0.18,0.23,0.82,0.77),3.5:(0.2,0.28,0.8,0.72),4.0:(0.28,0.28,0.72,0.72),4.5:(0,0.4,1,0.6),5.0:(0.1,0.2,0.9,0.6),5.5:(0.18,0.3,0.62,0.44),
 6.0:(0,0.33,1,0.67),6.5:(0,0.33,1,0.67),7.0:(0,0.29,1,0.71),7.5:(0,0.28,1,0.72),8.0:(0,0.28,1,0.72),8.5:(0,0.28,1,0.72),
 9.0:(0,0.31,1,0.69),9.5:(0,0.31,1,0.69),10.0:(0,0.31,1,0.69)}
m={0.0:(0.1,0.04,0.42,0.28),0.5:(0.08,0.05,0.42,0.27),1.0:(0.02,0.08,0.42,0.22),1.5:(0.06,0.08,0.42,0.22),2.0:(0,0.08,0.32,0.22),2.5:(0,0.08,0.2,0.2),
 6.0:(0.1,0.1,0.4,0.22),6.5:(0.18,0.04,0.34,0.28),7.0:(0.28,0.08,0.19,0.2),7.5:(0.36,0.12,0.24,0.15),8.0:(0.4,0.12,0.24,0.15),8.5:(0.46,0.12,0.24,0.15),
 9.0:(0.46,0.15,0.24,0.15),9.5:(0.46,0.15,0.24,0.15),10.0:(0.42,0.15,0.24,0.15)}
c={"mediaId":5315,"level":"A","keyWord":"postcard","defaultVoice":"female",
"taps":[{"phrase":"to try on a red hat","target":"the woman","voice":"female","keys":K(w)},
{"phrase":"to hold many postcards","target":"the woman","voice":"female","keys":K(w)},
{"phrase":"to clap his hands","target":"the man","voice":"male","keys":K(m)}],
"stillS":10.0,
"nouns":[{"word":"a man","x":0.53,"y":0.24,"voice":"male"},{"word":"hats","x":0.55,"y":0.37,"voice":"female"},
{"word":"postcards","x":0.62,"y":0.62,"voice":"female"},{"word":"a camera","x":0.4,"y":0.86,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","holding","many","postcards."],"answerVoice":"female",
"notes":"Man (stallholder) claps at 6.5-7.0 s only; his boxes are tight (face/upper body) so they stay above the woman's box, which starts below his face and cuts the top of her head/hat in some frames. 3.0-5.5 s show only her hand/arm or her mirror reflection (5.5 s). Berets called 'hat' for level A."}
json.dump(c,open('content/5315.json','w'),indent=1)
