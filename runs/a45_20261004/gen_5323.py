import json
T=[i*0.5 for i in range(25)]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=r; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
man=[(0,0,0.50,0.97),(0,0,0.42,0.95),(0,0,0.38,0.97),(0,0,0.36,0.95),(0,0,0.80,0.90),(0,0.08,0.80,0.75),(0,0.16,0.82,0.68),(0,0.18,0.80,0.68),
(0,0.02,0.70,0.90),(0,0,0.65,0.96),(0,0,0.44,0.85),(0,0,0.22,0.95),(0,0,0.37,0.90),(0,0,0.54,0.84),(0.04,0.09,0.56,0.86),(0.21,0.23,0.48,0.54),
(0.18,0.14,0.46,0.33),(0.30,0.44,0.24,0.20),None,None,(0.38,0.42,0.18,0.14),(0.38,0.40,0.22,0.14),(0.35,0.41,0.25,0.14),(0.36,0.39,0.24,0.14),(0.38,0.39,0.26,0.14)]
boy=[(0.82,0.51,0.18,0.16)]*4+[None]*11+[(0.80,0.48,0.20,0.38),(0.76,0.48,0.24,0.42),(0.62,0.44,0.36,0.40),(0.60,0.46,0.38,0.38),(0.62,0.46,0.36,0.38),
(0.62,0.43,0.37,0.40),(0.66,0.42,0.33,0.36),(0.62,0.44,0.37,0.36),(0.64,0.45,0.35,0.36),(0.66,0.44,0.33,0.38)]
c={"mediaId":5323,"level":"A","keyWord":"stone","defaultVoice":"male",
"taps":[{"phrase":"to throw a big stone","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to jump into the lake","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to wear a grey hat","target":"the boy","voice":"male","keys":K(boy)}],
"stillS":0.0,
"nouns":[{"word":"a stone","x":0.27,"y":0.82,"voice":"male"},{"word":"a lake","x":0.62,"y":0.20,"voice":"male"},{"word":"a man","x":0.14,"y":0.28,"voice":"male"}],
"question":"What is the man throwing?","answer":["He","is","throwing","a","big","stone."],"answerVoice":"male",
"notes":"Man throws the stone (4.5-5.5 s) and dives in (7.5-8.5 s); off while hidden in the splash (9.0-9.5 s). Boy in the grey bucket hat only partly in frame at 0-1.5 s (hat at the right edge), off 2.0-7.0 s. The girl beside him is not a target."}
json.dump(c,open('content/5323.json','w'),indent=1)
