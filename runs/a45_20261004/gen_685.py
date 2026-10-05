import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
G={0.0:(0.13,0.30,0.63,0.50),0.5:(0.15,0.30,0.61,0.50),1.0:(0,0.12,0.88,0.88),1.5:(0,0.10,1,0.90),2.0:(0.15,0.24,0.61,0.56),
2.5:(0.13,0.30,0.71,0.50),3.0:(0.10,0.34,0.74,0.56),3.5:(0,0.33,0.74,0.57),4.0:(0.08,0.32,0.68,0.47),
5.5:(0.42,0.22,0.58,0.78),6.0:(0,0.24,1,0.40),6.5:(0,0.24,1,0.40),7.0:(0.08,0.20,0.84,0.50),7.5:(0.13,0.20,0.83,0.50),
8.0:(0.08,0.20,0.92,0.45),8.5:(0.20,0.42,0.33,0.44),9.0:(0.07,0.48,0.40,0.50),9.5:(0,0.47,0.35,0.53),10.0:(0,0.40,0.19,0.57)}
M={0.0:(0.78,0.12,0.22,0.88),0.5:(0.78,0.12,0.22,0.88),2.0:(0.78,0.12,0.22,0.88),2.5:(0.85,0.12,0.15,0.88),3.0:(0.85,0.12,0.15,0.88),
3.5:(0.75,0.15,0.25,0.85),4.0:(0.77,0.15,0.23,0.85),5.5:(0,0.42,0.40,0.26),6.0:(0,0.65,1,0.17),6.5:(0,0.65,1,0.18),
7.0:(0.52,0.71,0.48,0.14),7.5:(0.52,0.71,0.48,0.14),8.0:(0.50,0.66,0.50,0.14),8.5:(0.54,0.36,0.38,0.32),9.0:(0.60,0.44,0.40,0.34),
9.5:(0.48,0.46,0.52,0.32),10.0:(0.52,0.34,0.48,0.34)}
c={"mediaId":685,"level":"A","keyWord":"size","defaultVoice":"female",
"taps":[
{"phrase":"to try on hats","target":"the girl","voice":"female","keys":keys(G)},
{"phrase":"to hold a small mirror","target":"the girl","voice":"female","keys":keys(G)},
{"phrase":"to sell hats","target":"the man","voice":"male","keys":keys(M)}],
"stillS":1.5,
"nouns":[{"word":"the sky","x":0.16,"y":0.06,"voice":"female"},{"word":"a hat","x":0.50,"y":0.18,"voice":"female"},
{"word":"hair","x":0.19,"y":0.42,"voice":"female"},{"word":"a dress","x":0.50,"y":0.90,"voice":"female"}],
"question":"What is the girl doing?",
"answer":["She","is","trying","on","hats."],
"answerVoice":"female",
"notes":"Key word 'size' is abstract and not a visible noun; not used in the texts. 4.5 and 5.0 are close-ups of hands with hats (owner unclear): both targets off. 5.5-8.0: only the man's hands/arms are in the picture and they cross the girl; his box is the band with his hands, the girl's box ends above it (her lower dress is left out). 3.5: the girl's outstretched hand reaches into the man's box and his hand into hers. 'to sell hats' is a little inferential (he stands at the stall and takes coins at 8.0). At the end the man wears a hat himself, but only the girl tries hats on. Still 1.5 was chosen because it shows exactly one hat."}
json.dump(c,open("content/685.json","w"),indent=1)
