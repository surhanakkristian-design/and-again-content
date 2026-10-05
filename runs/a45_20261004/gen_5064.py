import json
def keys(times, boxes):
    return [{"t":t,"off":True} if boxes.get(t) is None else {"t":t,"x":boxes[t][0],"y":boxes[t][1],"w":boxes[t][2],"h":boxes[t][3]} for t in times]
T=[i*0.5 for i in range(21)]
split={0.0:.25,0.5:.22,1.0:.21,1.5:.25,2.0:.25,2.5:.25,3.0:.29,3.5:.29,4.0:.23,4.5:.22,5.0:.25,5.5:.25,6.0:.23,6.5:.23,7.0:.31}
crowd={t:(0.0,0.0,1.0,round(s-0.01,2)) for t,s in split.items()}
band={t:(0.0,round(s+0.01,2),1.0,round(1-(s+0.01),2)) for t,s in split.items()}
crowd.update({7.5:(0.0,0.05,0.25,0.24),8.0:(0.0,0.08,0.22,0.28),8.5:(0.0,0.15,0.22,0.25),9.0:(0.0,0.22,0.30,0.18),9.5:(0.0,0.24,0.30,0.18),10.0:(0.0,0.28,0.30,0.16)})
dr={7.5:(0.10,0.30,0.30,0.22),8.0:(0.07,0.37,0.28,0.20),8.5:(0.06,0.41,0.28,0.18),9.0:(0.08,0.42,0.26,0.18),9.5:(0.08,0.44,0.26,0.18),10.0:(0.04,0.46,0.26,0.18)}
band.update({7.5:(0.0,0.54,0.85,0.46),8.0:(0.0,0.58,0.75,0.42),8.5:(0.0,0.60,0.75,0.40),9.0:(0.0,0.62,0.70,0.38),9.5:(0.0,0.64,0.70,0.36),10.0:(0.0,0.66,0.60,0.34)})
c={"mediaId":5064,"level":"B","keyWord":"trumpet","defaultVoice":"male",
"taps":[
 {"phrase":"to blow into their trumpets","target":"the trumpet players","voice":"male","keys":keys(T,band)},
 {"phrase":"to wave national flags","target":"the crowd","voice":"male","keys":keys(T,crowd)},
 {"phrase":"to beat their drums","target":"the drummers","voice":"male","keys":keys(T,dr)}],
"stillS":8.0,
"nouns":[{"word":"flags","x":0.35,"y":0.12,"voice":"male"},
 {"word":"a drum","x":0.27,"y":0.44,"voice":"male"},
 {"word":"an avenue","x":0.85,"y":0.55,"voice":"male"},
 {"word":"a trumpet","x":0.50,"y":0.73,"voice":"male"}],
"question":"What are the bandsmen doing?",
"answer":["They","are","marching","down","a","long","avenue."],
"answerVoice":"male",
"notes":"Three group targets. Trumpet players and crowd are split by a horizontal line under the crowd (plumes reach into it) up to 7.0; from 7.5 (avenue shot) the crowd box is the spectators/flags at the upper left, the drummers (two white drums, left of the column, small) sit between, and the trumpet box covers only the front rows below the drummers. Drummers only appear from 7.5 and are small; crowd also stands on the right edge late (not boxed). A few non-trumpet brass (none clear) - all front players hold trumpets."}
json.dump(c,open('content/5064.json','w'),indent=1)
