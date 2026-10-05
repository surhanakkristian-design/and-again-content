import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2]-d[t][0],2),"h":round(d[t][3]-d[t][1],2)} for t in T]
M={0.0:(0.25,0.37,0.67,0.75),0.5:(0.07,0.16,0.92,0.85),1.0:(0.02,0.24,0.88,1.0),1.5:(0.30,0.53,1.0,1.0),
   2.0:(0.0,0.33,1.0,0.95),2.5:(0.0,0.34,1.0,0.95),3.0:(0.0,0.33,1.0,0.95),3.5:(0.29,0.30,1.0,0.90),
   4.0:(0.19,0.30,1.0,0.92),4.5:(0.0,0.70,0.22,0.95),5.0:(0.0,0.55,1.0,1.0),5.5:(0.33,0.50,1.0,1.0),
   6.0:(0.10,0.35,0.92,0.88),6.5:(0.27,0.36,0.87,0.88),7.0:(0.16,0.35,0.90,0.90),7.5:(0.20,0.35,0.92,0.90),
   8.0:(0.10,0.34,0.98,0.90),8.5:(0.30,0.37,0.72,0.66),9.0:(0.30,0.38,0.68,0.68)}
G={3.5:(0.0,0.32,0.28,0.86),4.0:(0.0,0.28,0.18,0.80)}
c={"mediaId":4933,"level":"A","keyWord":"wheel","defaultVoice":"male",
 "taps":[
  {"phrase":"to drive a bus","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to press a red button","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to wave at the driver","target":"the woman in green","voice":"female","keys":keys(G)}],
 "stillS":7.0,
 "nouns":[{"word":"a wheel","x":0.45,"y":0.68,"voice":"male"},
          {"word":"a tie","x":0.50,"y":0.55,"voice":"male"},
          {"word":"a door","x":0.74,"y":0.42,"voice":"male"},
          {"word":"passengers","x":0.15,"y":0.42,"voice":"male"}],
 "question":"What is the man holding?",
 "answer":["He","is","holding","the","steering","wheel."],
 "answerVoice":"male",
 "notes":"Woman in green waves at 3.5-4.0 (he waves back at 3.5, but only she waves AT the driver); at 4.0 she is cut by the left edge and her box is split from his reaching hand at x 0.18-0.19. A second woman in a denim jacket boards behind her (not a target). 1.5/4.5/5.0/5.5 show only his hand; 8.5/9.0 = his reflection in the side mirror."}
json.dump(c,open('content/4933.json','w'),indent=1)
