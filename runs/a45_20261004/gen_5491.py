import json
def keys(lst):
    out=[]
    for row in lst:
        t=row[0]
        if len(row)==1: out.append({"t":t,"off":True}); continue
        x,y,w,h=row[1:]
        w=min(w,1-x); h=min(h,1-y)
        out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
trav=keys([
(0.0,0,0.15,0.44,0.85),(0.5,0,0.15,0.47,0.85),(1.0,0,0.2,0.58,0.8),(1.5,0,0.2,0.62,0.8),(2.0,0,0.14,0.5,0.86),(2.5,0,0.12,0.5,0.88),
(3.0,0.8,0.18,0.2,0.82),(3.5,0.6,0.2,0.4,0.8),(4.0,0.56,0.24,0.44,0.76),(4.5,0.56,0.24,0.44,0.76),(5.0,0.6,0.24,0.4,0.76),(5.5,0.58,0.24,0.42,0.76),
(6.0,0.6,0.2,0.4,0.8),(6.5,0.6,0.2,0.4,0.8),(7.0,0.6,0.2,0.4,0.8),(7.5,0.6,0.2,0.4,0.8),
(8.0,0.47,0.41,0.18,0.4),(8.5,0.38,0.41,0.22,0.4),(9.0,0.32,0.41,0.21,0.46),(9.5,0.3,0.41,0.23,0.48),
(10.0,0.32,0.39,0.19,0.46),(10.5,0.32,0.39,0.19,0.46),(11.0,0.33,0.39,0.19,0.47),(11.5,0.32,0.32,0.18,0.51),(12.0,0.33,0.37,0.18,0.45)])
wom=keys([
(0.0,0.47,0.4,0.53,0.6),(0.5,0.47,0.22,0.53,0.78),(1.0,0.6,0.38,0.4,0.62),(1.5,0.62,0.38,0.38,0.62),(2.0,0.58,0.38,0.42,0.62),(2.5,0.52,0.4,0.48,0.6),
(3.0,),(3.5,),(4.0,),(4.5,),(5.0,),(5.5,),(6.0,),(6.5,),(7.0,),(7.5,),
(8.0,0.22,0.42,0.25,0.48),(8.5,0.13,0.42,0.25,0.46),(9.0,0.12,0.47,0.2,0.4),(9.5,0.11,0.47,0.19,0.4),
(10.0,0.14,0.46,0.18,0.41),(10.5,0.14,0.46,0.18,0.41),(11.0,0.15,0.47,0.18,0.41),(11.5,0.1,0.47,0.22,0.41),(12.0,0.05,0.47,0.28,0.4)])
tray=keys([
(0.0,),(0.5,),(1.0,),(1.5,),(2.0,),(2.5,),
(3.0,0,0.36,0.6,0.64),(3.5,0,0.36,0.58,0.64),(4.0,0,0.36,0.55,0.64),(4.5,0,0.36,0.55,0.64),(5.0,0,0.38,0.58,0.62),(5.5,0,0.38,0.55,0.62),
(6.0,0,0.36,0.56,0.64),(6.5,0,0.36,0.56,0.64),(7.0,0,0.33,0.48,0.67),(7.5,0,0.5,0.44,0.5),
(8.0,0.66,0.44,0.32,0.42),(8.5,0.61,0.45,0.3,0.35),(9.0,0.54,0.5,0.21,0.35),(9.5,0.54,0.5,0.21,0.36),
(10.0,0.52,0.44,0.24,0.31),(10.5,0.52,0.44,0.22,0.31),(11.0,0.53,0.44,0.19,0.31),(11.5,0.51,0.44,0.19,0.31),(12.0,0.52,0.44,0.18,0.28)])
c={"mediaId":5491,"level":"B","keyWord":"welcome","defaultVoice":"male",
"taps":[{"phrase":"to accept a fresh coconut","target":"the traveller","voice":"male","keys":trav},
{"phrase":"to drape a flower garland","target":"the woman in the orange sarong","voice":"female","keys":wom},
{"phrase":"to carry a tray of coconuts","target":"the man with the tray","voice":"male","keys":tray}],
"stillS":3.0,
"nouns":[{"word":"a carved gate","x":0.5,"y":0.27,"voice":"male"},
{"word":"coconuts","x":0.3,"y":0.7,"voice":"male"},
{"word":"a tray","x":0.5,"y":0.8,"voice":"male"}],
"question":"How are the hosts greeting the traveller?",
"answer":["They","are","giving","him","a","warm","welcome."],
"answerVoice":"male",
"notes":"Shots: 0-2.5 garland close-up, 3.0-7.5 coconut tray (traveller only partly at the right edge: hair, arm, hands with the coconut), 8.0-12.0 wide group shot. The woman is boxed off at 3.0-7.5 (a woman with a garland may be her far in the background at 6.5-7.5, not boxed). In the group shot the tray is held by a man in a white shirt who may not be the older tray carrier of 3.0-7.5; the tap box follows whoever holds the tray. Woman target named by her orange batik sarong (another woman at the right wears a red sarong with a lilac top). defaultVoice male = the traveller; answer subject They -> male default."}
json.dump(c,open('/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/content/5491.json','w'),indent=1)
