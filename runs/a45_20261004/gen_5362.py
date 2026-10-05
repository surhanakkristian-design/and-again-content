import json
times=[i*0.5 for i in range(19)]
F=(0,.18,1,.82)
M={0.0:F,0.5:F,1.0:F,1.5:F,2.0:F,2.5:(.81,.64,.19,.19),4.0:(.38,.22,.62,.78),4.5:(.40,.24,.60,.76),
5.0:(.41,.26,.59,.74),5.5:(.41,.25,.59,.75),6.0:(.41,.25,.59,.75),6.5:(.03,.22,.96,.78),7.0:(.15,.19,.72,.81),
7.5:(.02,.25,.94,.75),8.0:(.13,.27,.80,.73),8.5:(.11,.29,.89,.71),9.0:(.30,.32,.70,.68)}
S={2.5:(.15,.13,.65,.87),3.0:(.15,.12,.72,.88),3.5:(.14,.14,.72,.86),4.0:(0,.19,.37,.81),4.5:(0,.20,.39,.80),
5.0:(0,.20,.40,.80),5.5:(0,.20,.40,.80),6.0:(0,.20,.40,.80)}
def keys(D):
    return [{"t":t,**dict(zip("xywh",D[t]))} if t in D else {"t":t,"off":True} for t in times]
c={"mediaId":5362,"level":"A","keyWord":"silly","defaultVoice":"male",
 "taps":[
  {"phrase":"to put on sunglasses","target":"the young man","voice":"male","keys":keys(M)},
  {"phrase":"to hold lots of sunglasses","target":"the stand","voice":"male","keys":keys(S)},
  {"phrase":"to wear a necklace","target":"the young man","voice":"male","keys":keys(M)}],
 "stillS":8.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.10,"voice":"male"},
          {"word":"sunglasses","x":0.55,"y":0.43,"voice":"male"},
          {"word":"the sea","x":0.14,"y":0.53,"voice":"male"},
          {"word":"a fishing boat","x":0.18,"y":0.80,"voice":"male"}],
 "question":"What is the young man wearing?",
 "answer":["He","is","wearing","silly","red","sunglasses."],
 "answerVoice":"male",
 "notes":"Stand = the spinning sunglasses rack (2.5-6.0 s); at 2.5 only the man's hand is visible at the right edge. A small white yacht is far left at 8.0 s, hence 'a fishing boat' for the blue-and-white boat. Key word 'silly' (adjective) used in the answer."}
json.dump(c,open('content/5362.json','w'),indent=1)
