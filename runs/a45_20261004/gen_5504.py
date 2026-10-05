import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
W={0.0:(0.06,0.02,0.94,0.82),0.5:(0.18,0.0,0.82,0.84),1.0:(0.38,0.02,0.62,0.83),1.5:(0.25,0.02,0.75,0.82),
2.0:(0.15,0.0,0.85,0.8),2.5:(0.15,0.0,0.85,0.82),3.0:(0.13,0.0,0.87,0.88),3.5:(0.03,0.0,0.97,0.9),
4.0:(0.0,0.0,1.0,0.8),4.5:(0.0,0.0,1.0,0.8),5.0:(0.0,0.0,1.0,0.95),5.5:(0.05,0.0,0.95,0.88),
6.0:(0.0,0.0,1.0,0.65),6.5:(0.0,0.0,1.0,0.65),7.0:(0.0,0.0,1.0,0.65),7.5:(0.0,0.0,1.0,0.8),
8.0:(0.0,0.18,0.55,0.82),8.5:(0.0,0.14,0.6,0.86),9.0:(0.0,0.13,0.6,0.87),9.5:(0.0,0.17,0.6,0.83),10.0:(0.0,0.17,0.6,0.83)}
P={8.0:(0.55,0.0,0.45,1.0),8.5:(0.6,0.0,0.4,1.0),9.0:(0.6,0.0,0.4,1.0),9.5:(0.6,0.0,0.4,1.0),10.0:(0.6,0.0,0.4,1.0)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":5504,"level":"B","keyWord":"send","defaultVoice":"female",
"taps":[{"phrase":"to write a letter by hand","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to seal an envelope","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to stand on the pavement","target":"the postbox","voice":"female","keys":keys(P)}],
"stillS":0.0,
"nouns":[{"word":"a desk lamp","x":0.13,"y":0.21,"voice":"female"},
{"word":"a fountain pen","x":0.22,"y":0.6,"voice":"female"},
{"word":"a sheet of paper","x":0.33,"y":0.76,"voice":"female"},
{"word":"a cardigan","x":0.75,"y":0.48,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","writing","a","letter","with","a","fountain","pen."],
"answerVoice":"female",
"notes":"Only one person; two phrases share the woman. She presses the envelope flap down 6.0-7.5 s (sealing). The postbox appears only in the last shot 8.0-10.0 s; her hand reaches into the postbox area at the slot, so the woman/postbox boxes are split at x 0.55-0.60 and part of her hand falls in the postbox box. Key word 'send' is a verb, not placed."}
json.dump(c,open('content/5504.json','w'),indent=1)
