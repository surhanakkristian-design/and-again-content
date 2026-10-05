import json
T=[i/2 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
m1={0.0:(0.08,0.23,0.78,0.58),0.5:(0.1,0.0,0.88,0.7),1.0:(0.36,0.35,1.0,1.0),1.5:(0.27,0.35,1.0,1.0),2.0:(0.22,0.38,0.9,1.0),
 2.5:(0.18,0.39,0.82,1.0),3.0:(0.02,0.41,0.5,1.0),3.5:(0.0,0.4,0.38,1.0),4.0:(0.0,0.35,0.18,0.55),
 7.0:(0.02,0.36,0.2,0.56),8.0:(0.0,0.32,0.34,0.52),8.5:(0.02,0.32,0.33,0.52),9.0:(0.02,0.33,0.3,0.52),9.5:(0.02,0.33,0.29,0.52),
 10.0:(0.0,0.33,0.3,0.52),10.5:(0.0,0.33,0.3,0.52),11.0:(0.0,0.33,0.29,0.52),11.5:(0.0,0.33,0.25,0.52),12.0:(0.0,0.32,0.25,0.52)}
pc={1.0:(0.1,0.31,0.34,0.5),1.5:(0.08,0.26,0.27,0.47),2.0:(0.2,0.24,0.44,0.38),2.5:(0.33,0.24,0.62,0.38),3.0:(0.5,0.25,0.79,0.5),
 3.5:(0.63,0.23,0.86,0.46),4.0:(0.62,0.18,0.97,0.6),4.5:(0.55,0.13,1.0,0.75),5.0:(0.33,0.1,0.92,0.9),5.5:(0.19,0.18,0.81,0.9),
 6.0:(0.14,0.31,0.66,0.9),6.5:(0.21,0.32,0.68,0.9),7.0:(0.43,0.34,0.75,0.98),8.0:(0.55,0.34,0.76,0.52),8.5:(0.51,0.32,0.72,0.52),
 9.0:(0.5,0.33,0.7,0.52),9.5:(0.5,0.33,0.71,0.52),10.0:(0.5,0.33,0.72,0.52),10.5:(0.5,0.33,0.74,0.52),11.0:(0.5,0.33,0.72,0.52),
 11.5:(0.5,0.33,0.72,0.52),12.0:(0.49,0.33,0.71,0.52)}
dk={3.0:(0.1,0.27,0.3,0.41),3.5:(0.15,0.26,0.42,0.4),4.0:(0.19,0.23,0.37,0.37),4.5:(0.22,0.22,0.54,0.46),
 6.0:(0.66,0.17,1.0,0.72),6.5:(0.71,0.13,1.0,0.7),7.0:(0.76,0.12,1.0,0.9),7.5:(0.72,0.1,1.0,0.45),8.0:(0.8,0.1,1.0,0.55),
 8.5:(0.74,0.23,1.0,0.6),9.0:(0.71,0.27,1.0,0.58),9.5:(0.72,0.27,1.0,0.58),10.0:(0.73,0.28,1.0,0.55),10.5:(0.75,0.28,1.0,0.55),
 11.0:(0.74,0.28,1.0,0.56),11.5:(0.73,0.28,1.0,0.56),12.0:(0.72,0.28,1.0,0.56)}
c={"mediaId":5047,"level":"A","keyWord":"living room","defaultVoice":"male",
"taps":[
 {"phrase":"to hold the remote","target":"the man with the remote","voice":"male","keys":keys(m1)},
 {"phrase":"to carry the popcorn","target":"the man in the blue T-shirt","voice":"male","keys":keys(pc)},
 {"phrase":"to bring a blanket","target":"the woman with dark hair","voice":"female","keys":keys(dk)}],
"stillS":6.0,
"nouns":[{"word":"a clock","x":0.30,"y":0.19,"voice":"male"},{"word":"a lamp","x":0.31,"y":0.30,"voice":"male"},
 {"word":"popcorn","x":0.30,"y":0.49,"voice":"male"},{"word":"a blanket","x":0.88,"y":0.42,"voice":"male"}],
"question":"What are they eating?",
"answer":["They","are","eating","popcorn."],"answerVoice":"male",
"notes":"One continuous handheld shot. Background people overlap a lot at 1.0-3.5: boxes are split along the line between them (the man with the remote loses his head top / arm at 2.0-2.5, the man in blue keeps only his upper body behind the sofa). The woman with dark hair is off at 2.0-2.5 and 5.0-5.5 (hidden / tiny behind the man in blue) and only appears from 3.0. The man with the remote is off 4.5-6.5 (out of frame) and 7.5 (under the blanket); the man in blue is off at 7.5 (blanket). Still 6.0 chosen because only one blanket is visible then (a second, pink blanket appears later). 'living room' is the whole scene, not placed as a pill. Answer 'They' = the group, defaultVoice male (main person = man with the remote)."}
json.dump(c,open('content/5047.json','w'),indent=1)
