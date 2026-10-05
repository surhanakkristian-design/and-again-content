import json
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(zip(("t","x","y","w","h"),(t,)+d[t])) for t in T]
d={0.0:(0.3,0,0.45,0.79),0.5:(0.34,0,0.43,0.79),1.0:(0.28,0,0.53,0.79),1.5:(0.27,0,0.58,0.79),2.0:(0.26,0,0.58,0.76),2.5:(0.25,0,0.68,0.79),
 3.0:(0.14,0,0.86,1),3.5:(0.05,0,0.8,1),4.0:(0.03,0.16,0.97,0.84),4.5:(0,0.14,1,0.86),5.0:(0.12,0.17,0.86,0.83),5.5:(0.23,0.22,0.56,0.62),
 6.0:(0.22,0.22,0.54,0.6),6.5:(0.28,0.22,0.48,0.62),7.0:(0.29,0.24,0.52,0.6),7.5:(0.17,0.24,0.58,0.62),8.0:(0.17,0.22,0.63,0.6),
 8.5:(0.27,0.26,0.47,0.58),9.0:(0.26,0.17,0.44,0.58),9.5:(0.27,0.23,0.48,0.73),10.0:(0.12,0.16,0.8,0.78),10.5:(0.18,0.15,0.62,0.81),
 11.0:(0.17,0.16,0.64,0.82),11.5:(0.17,0.16,0.64,0.82),12.0:(0.16,0.15,0.64,0.79)}
g={0.0:(0,0.4,0.3,0.24),0.5:(0,0.36,0.33,0.26),1.0:(0,0.31,0.27,0.27),1.5:(0,0.26,0.26,0.27),2.0:(0,0.19,0.25,0.3),2.5:(0,0.13,0.24,0.32)}
c={"mediaId":5317,"level":"B","keyWord":"ruffle","defaultVoice":"female",
"taps":[{"phrase":"to swirl her ruffled skirt","target":"the dancer","voice":"female","keys":K(d)},
{"phrase":"to stamp her heels","target":"the dancer","voice":"female","keys":K(d)},
{"phrase":"to strum a guitar","target":"the guitarist","voice":"male","keys":K(g)}],
"stillS":12.0,
"nouns":[{"word":"light bulbs","x":0.25,"y":0.21,"voice":"female"},{"word":"the sky","x":0.6,"y":0.06,"voice":"female"},
{"word":"ruffles","x":0.48,"y":0.66,"voice":"female"},{"word":"a wooden stage","x":0.8,"y":0.88,"voice":"female"}],
"question":"What is the dancer doing?","answer":["She","is","swirling","her","ruffled","skirt."],"answerVoice":"female",
"notes":"Guitarist clearly visible only 0-2.5 s (later hidden behind the dancer, off). In 0-2.5 s the dancer's box starts right of the guitarist's guitar, so the left edge of her wide skirt is cut. The two clapping women were not used (both clap, no phrase fits only one). 'to stamp her heels' is visible as footwork (heels hit the stage), strongest at 5.5-9.5 s."}
json.dump(c,open('content/5317.json','w'),indent=1)
