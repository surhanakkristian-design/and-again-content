import json
times=[i*0.5 for i in range(19)]
M={0.0:(.17,.36,.54,.64),0.5:(.16,.35,.57,.65),1.0:(.12,.26,.88,.74),1.5:(.06,.26,.63,.74),2.0:(.09,.27,.62,.73),
2.5:(.15,.27,.60,.73),3.0:(.08,.27,.64,.73),3.5:(.09,.30,.66,.70),4.0:(.07,.33,.76,.67),4.5:(.07,.32,.73,.68),
5.0:(.07,.34,.66,.66),5.5:(.07,.35,.93,.65),6.0:(.11,.31,.62,.69),6.5:(.10,.33,.63,.67),7.0:(.08,.39,.63,.61),
7.5:(.12,.39,.60,.61),8.0:(.09,.37,.59,.63),8.5:(.08,.35,.60,.65),9.0:(.08,.37,.60,.63)}
T={2.0:(.80,.31,.20,.17),2.5:(.77,.31,.23,.20),3.0:(.73,.22,.27,.50),3.5:(.76,.10,.24,.70),4.0:(0,.07,1.0,.25),4.5:(0,.02,1.0,.28)}
def keys(D):
    return [{"t":t,**dict(zip("xywh",D[t]))} if t in D else {"t":t,"off":True} for t in times]
c={"mediaId":5360,"level":"B","keyWord":"metro","defaultVoice":"male",
 "taps":[
  {"phrase":"to go through the barrier","target":"the young man","voice":"male","keys":keys(M)},
  {"phrase":"to pull into the station","target":"the train","voice":"male","keys":keys(T)},
  {"phrase":"to have bleached hair","target":"the young man","voice":"male","keys":keys(M)}],
 "stillS":3.5,
 "nouns":[{"word":"a metro train","x":0.24,"y":0.28,"voice":"male"},
          {"word":"glasses","x":0.50,"y":0.43,"voice":"male"},
          {"word":"a varsity jacket","x":0.55,"y":0.64,"voice":"male"},
          {"word":"the platform","x":0.86,"y":0.88,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","walking","through","a","crowded","station."],
 "answerVoice":"male",
 "notes":"Barrier = ticket gate, only shown at 1.0-1.5 s. Train boxed 2.0-4.5 s only where it is not behind the man (side strip at 3.0/3.5, top band at 4.0/4.5); interior shots 5.0+ count as off. Question answer refers to the crowded platform scene 6.0-9.0 s."}
json.dump(c,open('content/5360.json','w'),indent=1)
