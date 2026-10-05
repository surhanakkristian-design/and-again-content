import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2]-d[t][0],2),"h":round(d[t][3]-d[t][1],2)} for t in T]
P={0.0:(0.25,0.16,0.82,0.83),0.5:(0.40,0.16,0.96,0.82),1.0:(0.33,0.18,0.94,0.93),
   1.5:(0.0,0.12,1.0,1.0),2.0:(0.0,0.12,1.0,1.0),2.5:(0.0,0.12,1.0,1.0),
   3.0:(0.08,0.60,0.58,1.0),3.5:(0.18,0.60,0.72,1.0),
   4.0:(0.0,0.08,1.0,1.0),4.5:(0.0,0.08,1.0,1.0),5.0:(0.0,0.08,1.0,1.0),
   5.5:(0.0,0.10,0.96,1.0),6.0:(0.0,0.15,0.95,1.0),6.5:(0.0,0.15,0.93,1.0),7.0:(0.0,0.10,0.90,1.0),7.5:(0.0,0.10,0.92,1.0),
   8.0:(0.0,0.08,1.0,1.0),8.5:(0.0,0.08,1.0,1.0),9.0:(0.0,0.10,1.0,1.0)}
K=keys(P)
c={"mediaId":4934,"level":"B","keyWord":"headset","defaultVoice":"female",
 "taps":[
  {"phrase":"to pull a wheeled suitcase","target":"the pilot","voice":"female","keys":K},
  {"phrase":"to put on her headset","target":"the pilot","voice":"female","keys":K},
  {"phrase":"to give a thumbs-up","target":"the pilot","voice":"female","keys":K}],
 "stillS":8.0,
 "nouns":[{"word":"a peaked cap","x":0.50,"y":0.17,"voice":"female"},
          {"word":"a headset","x":0.83,"y":0.37,"voice":"female"},
          {"word":"a seat belt","x":0.47,"y":0.78,"voice":"female"}],
 "question":"What is the pilot wearing?",
 "answer":["She","is","wearing","a","green","headset."],
 "answerVoice":"female",
 "notes":"Only one person: the pilot is the target of all three phrases. 1.5-2.5: she stands at a glass wall and a second pilot (apparently her reflection) salutes back; box covers both, since it is the same woman. 3.0-3.5 only her hand on the overhead switches; 5.5-7.5 seen from behind, box covers her arm reaching to the thrust lever. Only 3 nouns: the microphone boom was left out so it is not confused with the headset."}
json.dump(c,open('content/4934.json','w'),indent=1)
