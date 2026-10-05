import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
m={0.0:(0.36,0.02,0.64,0.98),0.5:(0.05,0,0.95,1.0),1.0:(0,0,1,1),1.5:(0.58,0,0.42,1.0),2.0:(0.38,0.05,0.62,0.95),
2.5:(0.45,0.09,0.55,0.91),3.0:(0.30,0.10,0.70,0.90),3.5:(0.64,0.08,0.36,0.92),4.0:(0.76,0.08,0.24,0.92),4.5:(0.16,0.11,0.84,0.89),
5.0:(0.42,0.11,0.58,0.89),5.5:(0.18,0.15,0.82,0.85),6.0:(0.26,0.10,0.74,0.88),6.5:(0.36,0.07,0.64,0.83),7.0:(0.42,0.05,0.58,0.95),
7.5:(0,0,1,1),8.0:(0.47,0.08,0.53,0.84),8.5:(0.47,0.12,0.53,0.80),9.0:(0.47,0,0.53,1.0),9.5:(0.56,0.08,0.44,0.92),10.0:(0.52,0.10,0.48,0.90)}
k=keys(m)
c={"mediaId":4541,"level":"B","keyWord":"filthy","defaultVoice":"male",
"taps":[
 {"phrase":"to wipe the filthy counter","target":"the man","voice":"male","keys":k},
 {"phrase":"to rinse a grey cloth","target":"the man","voice":"male","keys":k},
 {"phrase":"to spray the smeared mirror","target":"the man","voice":"male","keys":k}],
"stillS":3.0,
"nouns":[{"word":"a mirror","x":0.22,"y":0.30,"voice":"male"},{"word":"a cloth","x":0.40,"y":0.50,"voice":"male"},
 {"word":"a tap","x":0.28,"y":0.65,"voice":"male"},{"word":"a basin","x":0.38,"y":0.78,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","wiping","the","filthy","counter","with","a","cloth."],
"answerVoice":"male",
"notes":"Only one person, so all three phrases share the man; the boxes follow the real man, his mirror image sits partly inside them at 4.5-5.5 s (no other target). Key word 'filthy' (adjective) is in phrase 1 and the answer. He wipes the counter at 0.0-1.5 s and 7.5 s, rinses the cloth under the tap at 6.0-7.0 s, sprays the mirror at 3.5-4.0 s. He also mops the floor at 8.0-8.5 s (not used)."}
json.dump(c,open("content/4541.json","w"),indent=1)
