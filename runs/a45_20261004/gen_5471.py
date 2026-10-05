import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
M={0.0:(0.29,0.31,0.71,0.69),0.5:(0.22,0.32,0.78,0.68),1.0:(0.19,0.33,0.81,0.67),1.5:(0.19,0.32,0.81,0.68),
 2.0:(0.0,0.20,0.51,0.80),2.5:(0.0,0.45,0.48,0.40),3.0:(0.0,0.46,0.44,0.42),3.5:(0.28,0.86,0.44,0.14),
 4.0:(0.0,0.36,0.49,0.64),4.5:(0.0,0.38,0.48,0.62),5.0:(0.54,0.38,0.44,0.62),5.5:(0.54,0.34,0.44,0.66),
 6.0:(0.60,0.31,0.40,0.56),6.5:(0.80,0.46,0.20,0.14),7.0:(0.80,0.48,0.20,0.14),7.5:(0.48,0.34,0.52,0.66),
 9.0:(0.55,0.38,0.45,0.62),9.5:(0.68,0.38,0.32,0.62),10.0:(0.68,0.37,0.32,0.63),10.5:(0.66,0.38,0.34,0.54),
 11.0:(0.65,0.39,0.35,0.52),11.5:(0.64,0.41,0.36,0.50),12.0:(0.65,0.41,0.35,0.48)}
L={2.5:(0.29,0.24,0.70,0.21),3.0:(0.29,0.26,0.69,0.20),3.5:(0.52,0.23,0.19,0.63),4.0:(0.50,0.30,0.18,0.24),4.5:(0.49,0.31,0.18,0.24)}
c={"mediaId":5471,"level":"B","keyWord":"level","defaultVoice":"male",
"taps":[{"phrase":"to straighten a picture frame","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to admire the finished wall","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to rest against a picture frame","target":"the spirit level","voice":"male","keys":keys(L)}],
"stillS":8.0,
"nouns":[{"word":"a clock","x":0.22,"y":0.33,"voice":"male"},{"word":"a wooden shelf","x":0.30,"y":0.61,"voice":"male"},
{"word":"a wall hanging","x":0.71,"y":0.48,"voice":"male"},{"word":"a wooden floor","x":0.65,"y":0.86,"voice":"male"}],
"question":"Where is the man resting his hands?","answer":["He","is","resting","his","hands","on","his","hips."],"answerVoice":"male",
"notes":"Only one person; man used for two phrases, the yellow spirit level is the third target (2.5-4.5 s, on top of / beside the frames). At 2.5-4.5 his hand holds the level: boxes split (level above / man below at 2.5-3.0; man head+torso left of the level at 4.0-4.5). At 3.5 only his forearm shows at the bottom. A second, decorative spirit level sits on a shelf at 9.0-12.0 (not tapped, it does not rest against a frame). 'level' is an adjective key word, not placed as a noun. Man is off at 8.0-8.5 (empty wall)."}
json.dump(c,open('content/5471.json','w'),indent=1)
