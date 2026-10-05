import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
M={0.0:(0,0.18,0.24,0.36),0.5:(0,0.24,0.74,0.76),1.0:(0,0.25,0.72,0.75),
4.5:(0,0.27,0.68,0.73),5.0:(0,0.27,0.76,0.73),5.5:(0,0.30,0.82,0.70),6.0:(0,0.03,1.0,0.46),6.5:(0,0.04,0.82,0.96),
7.0:(0,0.08,0.95,0.92),7.5:(0,0.04,1.0,0.96),8.0:(0,0.03,1.0,0.97),8.5:(0,0.06,0.76,0.94),9.0:(0,0.09,0.50,0.91)}
D={1.5:(0.64,0.38,0.36,0.32),2.0:(0.52,0.41,0.48,0.42),2.5:(0.50,0.63,0.50,0.27),3.0:(0.70,0.35,0.30,0.58),3.5:(0.70,0.35,0.30,0.58),
4.0:(0.17,0.50,0.83,0.50),4.5:(0.68,0.03,0.32,0.97),5.0:(0.76,0.06,0.24,0.94),5.5:(0.82,0.13,0.18,0.87),6.0:(0.58,0.49,0.42,0.44),
6.5:(0.82,0.62,0.18,0.30),8.5:(0.76,0.70,0.24,0.26),9.0:(0.50,0.28,0.50,0.72)}
S={0.0:(0.55,0.16,0.45,0.84),0.5:(0.74,0.16,0.26,0.84),1.0:(0.72,0.18,0.28,0.82),1.5:(0,0,0.64,1.0),2.0:(0,0,0.52,1.0),2.5:(0,0,1.0,0.63),
3.0:(0,0,0.70,1.0),3.5:(0,0,0.70,1.0),4.0:(0,0,0.88,0.50),8.5:(0.82,0.38,0.18,0.31),9.0:(0.60,0.14,0.36,0.14)}
c={"mediaId":723,"level":"B","keyWord":"spine","defaultVoice":"male",
"taps":[
{"phrase":"to clutch his lower back","target":"the young man","voice":"male","keys":keys(M)},
{"phrase":"to point at the spine","target":"the doctor","voice":"female","keys":keys(D)},
{"phrase":"to hang on a metal stand","target":"the skeleton","voice":"male","keys":keys(S)}],
"stillS":2.5,
"nouns":[{"word":"a shoulder blade","x":0.27,"y":0.29,"voice":"male"},{"word":"ribs","x":0.25,"y":0.45,"voice":"male"},
{"word":"a spine","x":0.50,"y":0.57,"voice":"male"},{"word":"a finger","x":0.68,"y":0.69,"voice":"male"}],
"question":"What is the doctor pointing at?",
"answer":["She","is","pointing","at","the","spine."],"answerVoice":"female",
"notes":"Cartoon clip with cuts. Doctor is only a hand/arm at 1.5-3.5, 6.0, 6.5 and 8.5 (identifiable as hers from 4.0 on); at 1.0 only her fingertip shows at the right edge inside the skeleton box, set off. Close-ups 1.5-4.0: skeleton fills the frame, its box is cut where the doctor's hand lies (2.0 the split runs along the spine). 4.5-6.0 doctor and man overlap heavily: split by a vertical line, her pointing arm falls in the man's box; at 6.0 the split is horizontal (man = head and chest, doctor = hand below). 9.0 skeleton box holds only the skull, the rest is behind the doctor. Man clutches his back at 0.5-1.0 only. Skeleton phrase is a state (it is a model on a wheeled stand, seen at 0.0-1.0). Two shoulder blades and ribs on both sides exist; the pills sit on the left ones."}
json.dump(c,open("content/723.json","w"),indent=1)
