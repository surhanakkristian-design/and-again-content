import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
young={0.0:(0.08,0.19,0.84,0.62),0.5:(0.08,0.17,0.87,0.6),1.0:(0.2,0.12,0.78,0.78),1.5:(0.2,0.16,0.8,0.8),
 2.0:(0.14,0.17,0.72,0.58),2.5:(0.14,0.18,0.74,0.58),3.0:(0,0.28,1.0,0.72),3.5:(0.08,0.14,0.92,0.86),
 4.0:(0,0.17,1,0.83),4.5:(0,0.17,1,0.83),5.0:(0,0.08,1,0.92),5.5:(0,0.13,1,0.87),6.0:(0,0.05,1,0.95),6.5:(0,0,1,1),
 7.0:(0,0.22,0.78,0.78),7.5:(0,0.25,0.8,0.75),8.0:(0,0.26,0.74,0.74),8.5:(0,0.25,0.76,0.75),9.0:(0,0.28,0.76,0.72)}
old={7.0:(0.8,0.13,0.2,0.55),7.5:(0.82,0.12,0.18,0.45),8.0:(0.76,0.19,0.24,0.38),8.5:(0.78,0.18,0.22,0.32),9.0:(0.78,0.2,0.22,0.35)}
c={"mediaId":5314,"level":"A","keyWord":"basket","defaultVoice":"female",
"taps":[{"phrase":"to hold a snow globe","target":"the young woman","voice":"female","keys":K(young)},
{"phrase":"to carry a big basket","target":"the young woman","voice":"female","keys":K(young)},
{"phrase":"to hold two hats","target":"the older woman","voice":"female","keys":K(old)}],
"stillS":8.0,
"nouns":[{"word":"an umbrella","x":0.2,"y":0.12,"voice":"female"},{"word":"hats","x":0.5,"y":0.33,"voice":"female"},
{"word":"postcards","x":0.55,"y":0.73,"voice":"female"},{"word":"a basket","x":0.35,"y":0.88,"voice":"female"}],
"question":"What is the young woman carrying?","answer":["She","is","carrying","a","big","basket."],"answerVoice":"female",
"notes":"Older woman only from 7.0 s (at 6.5 s only her hand on the hats shows, kept off); her box is kept to her face/upper body right of the young woman's arm. Young woman box covers whole frame at 6.5 s. Many small towers in the still, so no tower noun."}
json.dump(c,open('content/5314.json','w'),indent=1)
